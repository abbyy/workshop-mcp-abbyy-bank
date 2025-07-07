from tools import register_tools
from resources import register_resources
from prompts import register_prompts
from mcp.server.fastmcp import FastMCP
import sys

# Create the FastMCP server
mcp = FastMCP(
    name="ABBYYBankMCP-Python",
    version="1.0.0",
    instructions="""
    This app assists customers with opening a new bank account with the fictional ABBYY Bank. 
    Due to the sensitive nature of the application, only use the tools provided to assist the customer.
    When the customer asks to open a bank account, begin by asking for a utility bill to verify their identity and using the upload-utility-bill tool to process it.
    If the utility bill processed successfully, ask the customer if they would like to proceed with submitting their application. 
    If they do, use the submit-application tool to submit the application to the bank.
    If they do not, thank them for their time and end the conversation.    
""",
)

# State for the server
state = {
    "documents": {
        "utilityBill": None
    }
}

# Register tools, resources, and prompts
register_tools(mcp, state)
register_resources(mcp, state)
register_prompts(mcp)

if __name__ == "__main__":
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    mcp.run(transport='stdio') 
