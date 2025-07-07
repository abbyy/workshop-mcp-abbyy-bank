from tools import register_tools
from resources import register_resources
from prompts import register_prompts
from mcp.server.fastmcp import FastMCP

# Create the FastMCP server
mcp = FastMCP("ABBYYBankMCP")

# State for the server
state = {
    "documents": {
        "utilityBill": None
    }
}

# Register tools, resources, and prompts
register_tools(mcp, state)
register_resources(mcp, state)
register_prompts(mcp, state)

if __name__ == "__main__":
    mcp.run(transport='stdio') 
