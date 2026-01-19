from langchain_anthropic import ChatAnthropic
from langchain_core.prompts import ChatPromptTemplate
from langchain_classic.agents import create_tool_calling_agent, AgentExecutor
from tools import save_tool

class AISummary:
    def __init__(self, transcript = "transcript.txt"):
        self.transcript = transcript
        self.llm = ChatAnthropic(model="claude-sonnet-4-5-20250929")

    def summarize(self):
        with open(self.transcript, 'r') as f:
            self.content = f.read()
            self.generate_prompt()
            self.call_AI()
        
    def generate_prompt(self):
        self.prompt = ChatPromptTemplate.from_messages(
            [
                ("system", "You are an expert summarization AI. Provide concise and informative summaries. The given transcript is from a recorded conversation that may contain informal language and filler words. Focus on extracting key points, main ideas, and relevant details while omitting unnecessary filler content."),
                ("user", f"Summarize the following transcript:\n{self.content}")
            ]
        )

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
        raw_response = self.executor.run(self.prompt)
        print(raw_response)