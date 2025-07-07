# ABBYY Bank MCP Python Exercises

This directory contains a series of exercises for building an MCP (Model Context Protocol) server using Python and the FastMCP framework. The exercises guide you through creating a bank account onboarding system that integrates with ABBYY Document AI.

## Exercise Overview

The exercises are designed to be completed in sequence, with each building upon the previous:

1. **Foundation** - Basic MCP server setup
2. **Tools** - Implementing MCP tools for document processing
3. **Document AI** - Integrating ABBYY Document AI for utility bill processing
4. **Refactor** - Improving code structure and organization
5. **Claude** - Enhancing LLM instructions and workflow
6. **Resources & Prompts** - Adding MCP resources and prompts

## Prerequisites

- Python 3.10 or higher
- [uv](https://docs.astral.sh/uv/) package manager
- ABBYY Document AI API key (for exercises 3-6)

## Getting Started

1. Navigate to any exercise directory:
   ```bash
   cd py/exercise-reference/1-foundation
   ```

2. Install dependencies:
   ```bash
   uv sync
   ```

3. Run the exercise:
   ```bash
   uv run python index.py
   ```

4. Test with MCP Inspector:
   ```bash
   uv run mcp inspect --server "uv run python index.py"
   ```

## Exercise Structure

Each exercise contains:
- `index.py` - Main server file with TODO comments
- `solution/` - Directory containing completed solutions
- `pyproject.toml` - Project dependencies
- `README.md` - Exercise-specific instructions

## Sample Documents

The exercises use sample utility bills located in `../../sample-documents/`:
- `UtilityBill_1.pdf`
- `UtilityBill_2.pdf`

## Key Concepts

### FastMCP Framework
The exercises use the FastMCP framework, which provides a simple way to create MCP servers in Python:

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP(
    name="MyServer",
    version="1.0.0",
    instructions="Server description"
)
```

### Tools
MCP tools are functions that can be called by the LLM:

```python
@mcp.tool()
async def my_tool(parameter: str) -> dict:
    # Tool implementation
    return {"content": [{"type": "text", "text": "Result"}]}
```

### Resources
MCP resources provide access to data:

```python
@mcp.resource("my-resource://data")
def my_resource() -> dict:
    return {
        "contents": [{
            "type": "text",
            "text": "Resource data"
        }]
    }
```

### Prompts
MCP prompts provide predefined text for common actions:

```python
@mcp.prompt(name="My Prompt", description="Description")
def my_prompt() -> str:
    return "Predefined text"
```

## ABBYY Document AI Integration

Exercises 3-6 integrate with ABBYY Document AI for processing utility bills. The integration:

1. Reads PDF files and converts them to base64
2. Sends documents to ABBYY Document AI for processing
3. Polls for completion and extracts structured data
4. Returns customer information in a standardized format

## Troubleshooting

### Common Issues

1. **Import Errors**: Make sure you've run `uv sync` to install dependencies
2. **API Key Issues**: Ensure your ABBYY Document AI API key is valid
3. **File Path Issues**: Use absolute paths or ensure sample documents are accessible

### Getting Help

- Check the exercise-specific README files for detailed instructions
- Review the solution files if you get stuck
- Consult the MCP documentation for general concepts

## Next Steps

After completing all exercises, you'll have a fully functional MCP server that can:
- Process utility bills using ABBYY Document AI
- Manage application state
- Provide a complete bank account onboarding workflow
- Expose data through resources and prompts

This foundation can be extended to support additional document types, validation rules, and integration with other banking systems. 
