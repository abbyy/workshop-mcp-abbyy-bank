# Exercise 4: Refactoring

This exercise focuses on refactoring the code to improve structure and maintainability.

## Learning Objectives

- Understand how to organize MCP server code into classes
- Learn how to separate concerns by moving tools to separate modules
- Understand the benefits of modular code structure
- Learn best practices for MCP server organization

## Tasks

1. Wrap the server in a new class called ABBYYBankMCP
2. Move the utility bill tool from index.py to tools.py
3. Create a register_tools function to organize tool registration
4. Maintain the same functionality while improving code structure

## Running the Exercise

```bash
cd py/exercise-reference/4-refactor
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [Python Classes and Objects](https://docs.python.org/3/tutorial/classes.html)
- [MCP Best Practices](https://modelcontextprotocol.io/docs/concepts/architecture) 
