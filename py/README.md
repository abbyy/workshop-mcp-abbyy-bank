# ABBYY Bank MCP Workshop - Python Version

This is the Python equivalent of the TypeScript MCP workshop for building a Model Context Protocol (MCP) server that helps customers open bank accounts by processing utility bills using ABBYY's Document AI.

## Prerequisites

- Python 3.8 or higher
- pip
- An ABBYY Document AI API key (get one at https://developer.abbyy.com)
- Claude Desktop (for testing the final MCP server)

## Setup

1. Navigate to the `py` directory
2. Create a virtual environment: `python -m venv venv`
3. Activate the virtual environment:
   - On macOS/Linux: `source venv/bin/activate`
   - On Windows: `venv\Scripts\activate`
4. Install dependencies: `pip install -r requirements.txt`
5. Copy the sample documents from `../sample-documents/` to your workspace if needed

## Exercise Structure

The exercises follow the same structure as the TypeScript version:

- `exercise-reference/1-foundation/` - Basic MCP server setup
- `exercise-reference/2-tools/` - Adding document upload capability
- `exercise-reference/3-docai/` - Document AI integration
- `exercise-reference/4-refactor/` - Code refactoring
- `exercise-reference/5-claude/` - Enhanced instructions and workflow
- `exercise-reference/6-resources-prompts/` - Resources and prompts

Each exercise contains:
- `index.py` - The starting point with commented code
- `solution/index.py` - The completed solution

## Testing

To test an exercise:
1. Navigate to the exercise directory
2. Run the solution: `python solution/index.py`
3. Use the MCP Inspector: `python -m mcp.inspector python solution/index.py`

## Key Differences from TypeScript

- Uses the Python MCP SDK instead of TypeScript
- Async/await patterns with Python's asyncio
- Python-style imports and module structure
- Different package management with pip and requirements.txt 
