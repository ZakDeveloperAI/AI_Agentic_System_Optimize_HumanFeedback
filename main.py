from typing import TypedDict, Annotated, Sequence
from dotenv import load_dotenv

from langchain_core.messages import BaseMessage,ToolMessage,SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.tools import tool


from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START,END
from langgraph.prebuilt import ToolNode

load_dotenv()



#al momento non uso db vettoriale
document_content=""

class state(TypedDict):
    messages: Annotated[Sequence[BaseMessage],add_messages]


@tool #converte funzione python in tool utilizzabile da agente
def update(content: str) -> str:
    """Updates the document with the provided content."""
    global document_content
    document_content = content
    return f"Document updated successfully. the current content is: \n{document_content}"

@tool
def save(filename:str)->str: #I'll use simple text for this project no json
    """Saves the current document content to the specified text filename and finish the process.
    
    Args:
    filename: Name for the text file.
    """
    global document_content
    
    if not filename.endswith(".txt"):
        filename += ".txt"
    
    
    try:
        with open(filename, "w", encoding="utf-8") as f:
            f.write(document_content)
        return f"Document saved successfully to {filename}."
    except Exception as e:
        return f"Failed to save document: {str(e)}"
    
tools=[update,save]

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    temperature=0.2,
).bind_tools(tools)