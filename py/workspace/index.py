# from mcp.server.fastmcp import FastMCP
import sys

# Create the FastMCP server


if __name__ == "__main__":
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    mcp.run(transport='stdio') 
