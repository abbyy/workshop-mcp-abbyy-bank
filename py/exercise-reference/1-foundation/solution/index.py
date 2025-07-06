from mcp.server import Server
from mcp.server.stdio import stdio_server
import sys

# Create a new Server
# - Use the name 'ABBYYBankMCP' and a version of '1.0.0'
# - Set instructions for the LLM to know what this server can be used to do (to start, it can help a customer open a new bank account)
# The MCP Python SDK docs, for reference: https://github.com/modelcontextprotocol/python-sdk
# Core architecture: https://modelcontextprotocol.io/docs/concepts/architecture
# MCP Inspector: https://modelcontextprotocol.io/docs/tools/inspector
# "python -m mcp.inspector python index.py" to see the inspector in action

server = Server(
    name="ABBYYBankMCP",
    version="1.0.0",
    instructions="This server can help a customer open a new bank account"
)

async def main():
    # create a new stdio server
    async with stdio_server() as (read_stream, write_stream):
        # connect the server to the transport
        await server.run(
            read_stream,
            write_stream,
        )
    
    # add a log (using print) to the console to let the user know the server is running
    print("Server is running", file=sys.stderr)

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except Exception as error:
        print(f'Fatal error in main(): {error}', file=sys.stderr)
        sys.exit(1) 
