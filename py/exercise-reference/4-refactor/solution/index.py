from mcp.server.fastmcp import FastMCP
import sys
from tools import register_tools

class ABBYYBankMCP:
    def __init__(self):
        self.mcp = FastMCP(
            name="ABBYYBankMCP-Python",
            version="1.0.0",
            instructions="This server can help a customer open a new bank account"
        )
        self.state = {
            "documents": {
                "utilityBill": None
            }
        }
        register_tools(self.mcp, self.state)
    
    def run(self):
        self.mcp.run(transport='stdio')

async def main():
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    server = ABBYYBankMCP()
    server.run()

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 
