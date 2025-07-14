from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage,ToolMessage,SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END
from langgraph.prebuilt import ToolNode

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.5-flash",
    temperature=0.2,
)

document_content=""

class state(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]


@tool #converte funzione python in tool utilizzabile da agente
def update(content: str) -> str:
    pass