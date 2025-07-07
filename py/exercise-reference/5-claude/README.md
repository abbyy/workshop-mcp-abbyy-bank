# Exercise 5: Claude Instructions

This exercise focuses on improving the instructions provided to Claude for better interaction.

## Learning Objectives

- Understand how to write effective instructions for LLMs
- Learn how to define clear workflows and processes
- Understand how to create tools that work together
- Learn how to handle application state and validation

## Tasks

1. Update the instructions to provide a robust description of the bank account workflow
2. Create a submit-application tool that validates the required documents
3. Implement proper workflow logic in the instructions
4. Ensure the tools work together to provide a complete user experience

## Running the Exercise

```bash
cd py/exercise-reference/5-claude
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [Claude Instructions Best Practices](https://docs.anthropic.com/claude/docs)
- [MCP Tools and Workflows](https://modelcontextprotocol.io/docs/concepts/tools) 
