# Exercise 2: Tools

This exercise introduces you to MCP tools and how to implement them in Python.

## Learning Objectives

- Understand how to define and implement MCP tools
- Learn how to handle tool parameters and return values
- Understand error handling in tools
- Learn how to manage state in an MCP server

## Tasks

1. Add tools capabilities to the server
2. Define the "upload-utility-bill" tool with a documentFilepath parameter
3. Implement a mock process_utility_bill function that returns fake UtilityBillData
4. Store the extracted UtilityBillData in the state
5. Handle errors and return appropriate error responses

## Running the Exercise

```bash
cd py/exercise-reference/2-tools
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [MCP Tools Documentation](https://modelcontextprotocol.io/docs/concepts/tools)
- [FastMCP Tools](https://github.com/modelcontextprotocol/python-sdk) 
