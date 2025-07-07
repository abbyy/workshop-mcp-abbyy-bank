from mcp.server.fastmcp import FastMCP
import sys
from dataclasses import dataclass
from typing import Dict

# TODO: uncomment this 
# from document_ai import process_utility_bill, UtilityBillData

mcp = FastMCP(
    name="ABBYYBankMCP-Python",
    version="1.0.0",
    instructions="This server can help a customer open a new bank account"
)

@mcp.tool()
async def upload_utility_bill(documentFilepath: str) -> dict:
    try:
        # TODO: use the real process_utility_bill function
        bill_data = await process_utility_bill(documentFilepath)
        
        # Store the processed data
        state["documents"]["utilityBill"] = bill_data
        
        return {
            "content": [{
                "type": "text",
                "text": f"Utility bill processed successfully\n\nCustomer Information:\n- Full Name: {bill_data.full_name}\n- Account Number: {bill_data.account_number}\n- Address: {bill_data.address['street']}\n- Issue Date: {bill_data.issue_date}\n- Utility Provider: {bill_data.utility_provider}"
            }]
        }
    except Exception as error:
        print(f"Error processing utility bill: {error}")
        return {
            "isError": True,
            "content": [{
                "type": "text",
                "text": f"Error processing utility bill: {str(error)}"
            }]
        }

# State to store documents and validation results
state = {
    "documents": {
        "utilityBill": None
    }
}

# TODO: remove in favor of the dataclass in document_ai.py
@dataclass
class UtilityBillData:
    full_name: str
    account_number: str
    address: Dict[str, str]
    issue_date: str
    utility_provider: str

# TODO: remove in favor of the function in document_ai.py
async def process_utility_bill(documentFilepath: str) -> UtilityBillData:
    return UtilityBillData(
        full_name="John Doe",
        account_number="1234567890",
        address={"street": "123 Main St"},
        issue_date="2024-01-01",
        utility_provider="Electricity Company"
    )

async def main():
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    mcp.run(transport='stdio')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 
