# Exercise 1: Foundation

This exercise introduces you to the basic structure of an MCP server using Python and the FastMCP framework.

## Learning Objectives

- Understand the basic structure of an MCP server
- Learn how to create a FastMCP server instance
- Understand how to run the server with stdio transport

## Tasks

1. Import the necessary MCP server components
2. Create a new FastMCP server with the name 'ABBYYBankMCP-Python' and version '1.0.0'
3. Set instructions for the LLM to know what this server can be used to do
4. Add logging to let the user know the server is running
5. Run the server with stdio transport

## Running the Exercise

```bash
cd py/exercise-reference/1-foundation
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [MCP Core Architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector) 
