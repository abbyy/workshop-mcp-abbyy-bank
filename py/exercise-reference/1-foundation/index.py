# from mcp.server import Server
# from mcp.server.stdio import stdio_server

# Create a new Server
# - Use the name 'ABBYYBankMCP' and a version of '1.0.0'
# - Set instructions for the LLM to know what this server can be used to do (to start, it can help a customer open a new bank account)
# The MCP Python SDK docs, for reference: https://github.com/modelcontextprotocol/python-sdk
# Core architecture: https://modelcontextprotocol.io/docs/concepts/architecture
# MCP Inspector: https://modelcontextprotocol.io/docs/tools/inspector
# "python -m mcp.inspector python index.py" to see the inspector in action

async def main():
    # create a new stdio server
    # connect the server to the transport
    
    # add a log (using print) to the console to let the user know the server is running
    pass

if __name__ == "__main__":
    import asyncio
    try:
        asyncio.run(main())
    except Exception as error:
        print(f'Fatal error in main(): {error}', file=sys.stderr)
        sys.exit(1) 
