# Exercise 6: Resources and Prompts

This exercise introduces you to MCP resources and prompts for enhanced functionality.

## Learning Objectives

- Understand how to implement MCP resources
- Learn how to create and use MCP prompts
- Understand how to expose data through resources
- Learn how to provide predefined prompts for common actions

## Tasks

1. Create a resource for customer information that retrieves utility bill data from state
2. Create a prompt for opening a bank account with ABBYY Bank
3. Register both resources and prompts with the MCP server
4. Understand how resources and prompts enhance the user experience

## Running the Exercise

```bash
cd py/exercise-reference/6-resources-prompts
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [MCP Resources Documentation](https://modelcontextprotocol.io/docs/concepts/resources)
- [MCP Prompts Documentation](https://modelcontextprotocol.io/docs/concepts/prompts) 
