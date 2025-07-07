# Exercise 3: Document AI Integration

This exercise introduces you to integrating ABBYY Document AI for processing utility bills.

## Learning Objectives

- Understand how to integrate ABBYY Document AI with MCP
- Learn how to process documents using the Document AI API
- Understand how to handle async operations and polling
- Learn how to extract structured data from documents

## Tasks

1. Uncomment the import for process_utility_bill and UtilityBillData from document_ai
2. Implement the process_utility_bill function in document_ai.py using ABBYY Document AI
3. Use the utility bill model with base64 encoded content
4. Handle the async nature of document processing with polling
5. Extract relevant fields from the processed document

## Running the Exercise

```bash
cd py/exercise-reference/3-docai
uv sync
uv run python index.py
```

## Testing with MCP Inspector

```bash
uv run mcp inspect --server "uv run python index.py"
```

## Resources

- [ABBYY Document AI Documentation](https://docs.abbyy.com/quickstart)
- [ABBYY Document AI Python SDK](https://github.com/abbyy/document-ai-python) 
