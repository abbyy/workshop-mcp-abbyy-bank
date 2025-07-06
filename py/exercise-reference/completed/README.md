# ABBYY Bank MCP Server - Completed Solution

This is the completed Python implementation of the ABBYY Bank MCP server that helps customers open bank accounts by processing utility bills.

## Features

- **Document Processing**: Upload and process utility bills using ABBYY Document AI
- **Bank Account Application**: Complete workflow for opening a bank account
- **MCP Integration**: Full Model Context Protocol server with tools, resources, and prompts
- **Mock Document AI**: Includes a mock implementation for testing (replace with real ABBYY SDK in production)

## Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the server:
   ```bash
   python src/index.py
   ```

## Testing with MCP Inspector

To test the server with the MCP Inspector:

```bash
python -m mcp.inspector python src/index.py
```

## Available Tools

- **upload-utility-bill**: Upload and process a utility bill image
- **submit-application**: Submit the completed application to the bank

## Available Resources

- **customer-info**: Access processed customer information from utility bills

## Available Prompts

- **open-bank-account**: Start the bank account application process

## File Structure

```
src/
├── index.py          # Main server entry point
├── tools.py          # Tool implementations
├── document_ai.py    # Document AI integration
├── resources.py      # Resource implementations
└── prompts.py        # Prompt implementations
```

## Production Deployment

To use this in production:

1. Replace the mock Document AI implementation with the real ABBYY SDK
2. Add proper error handling and logging
3. Configure environment variables for API keys
4. Add authentication and security measures 
