from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor

class AISummary:
    def __init__(self, transcript = "transcript.txt"):
        self.transcript = transcript
        self.llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

    def summarize(self):
        with open(self.transcript, 'r') as f:
            self.content = f.read()
            self.text = ("".join(self.content))
            self.generate_prompt()
            self.call_AI()
            self.write_to_file()
        
    def generate_prompt(self):
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an expert summarization AI. Provide concise and informative summaries. The query is a raw transcript from a recorded conversation that may contain informal language and filler words. Focus on extracting key points, main ideas, and relevant details while omitting unnecessary filler content."),
                ("placeholder", "{chat_history}"),
                ("human", "{query}"),
                ("placeholder", "{agent_scratchpad}"),
            ]
        )

    def parse_response(self):
        output = self.raw_response['output']
        text_response = output[0]['text']
        return text_response

    def write_to_file(self, file = "summary.txt"):
        self.summary = self.parse_response()
        with open(file, 'w') as f:
            f.write(self.summary)
        print(f"Summary saved to {file}")

    def call_AI(self):
        self.agent = create_tool_calling_agent(
            llm=self.llm,
            prompt=self.prompt,
            tools=[],
        )
        self.executor = AgentExecutor.from_agent_and_tools(
            agent=self.agent,
            tools=[],
            verbose=True
        )
        self.raw_response = self.executor.invoke({"query": self.text})
        print(f"raw response: {self.raw_response}")
        print("parsing response...")
