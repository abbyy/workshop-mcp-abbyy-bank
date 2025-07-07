from mcp.server.fastmcp import FastMCP
import sys

# Create a new FastMCP server
mcp = FastMCP(
    name="ABBYYBankMCP-Python",
    version="1.0.0",
    instructions="This server can help a customer open a new bank account"
)

async def main():
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    mcp.run(transport='stdio')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 
