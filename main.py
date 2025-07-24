from dotenv import load_dotenv
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import PydanticOutputParser
from langchain.agents import create_tool_calling_agent, AgentExecutor
from tools import duckduckgo_tool, wiki_tool, save_tool

# load_dotenv()

llm = ChatOpenAI(model="gpt-4o", temperature=0.3)

class ResearchResponse(BaseModel):
    title: str
    summary: str
    sources: list[str]
    tools_used: list[str]

parser = PydanticOutputParser(pydantic_object=ResearchResponse)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system",
         """
        You are a research assitant that will help generate a research paper.
        Answer the user query and use neccessary tools.
        Wrap the output in this format and provide no other text\n{format_instructions}
         """
        ),
        ("placeholder", "{chat_history}"),
        ("human", "{query}"),
        ("placeholder", "{agent_scratchpad}")

    ]
).partial(format_instructions=parser.get_format_instructions())

tools = [duckduckgo_tool, wiki_tool, save_tool]
agent = create_tool_calling_agent(
    llm=llm,
    prompt=prompt,
    tools = tools
)

# AgentExecutor will automatically handle chat_history and agent_scratchpad
executor = AgentExecutor(agent=agent, tools=tools, verbose=True) # verbose is to see the agent's thought process
query = input("What can I help you research?")
raw_response = executor.invoke({"query": query})

print(raw_response)