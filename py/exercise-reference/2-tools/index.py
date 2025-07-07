from mcp.server.fastmcp import FastMCP
import sys
from dataclasses import dataclass
from typing import Dict

# TODO: add tools capabilities to the server
mcp = FastMCP(
    name="ABBYYBankMCP-Python",
    version="1.0.0",
    instructions="This server can help a customer open a new bank account"
)

# TODO: define the "upload-utility-bill" tool
# include documentFilepath as a string parameter pointing to the utility bill file
# process the utility bill and return the extracted UtilityBillData
# store the extracted UtilityBillData in the state
# catch and return errors
# See: https://modelcontextprotocol.io/docs/concepts/tools

# TODO: Define state to store OCR'd document data
state = {}

# TODO: implement the process_utility_bill with fake UtilityBillData for now
async def process_utility_bill(documentFilepath: str):
    pass

@dataclass
class UtilityBillData:
    full_name: str
    account_number: str
    address: Dict[str, str]
    issue_date: str
    utility_provider: str

async def main():
    print("Starting ABBYY Bank MCP server...", file=sys.stderr)
    mcp.run(transport='stdio')

if __name__ == "__main__":
    import asyncio
    asyncio.run(main()) 
