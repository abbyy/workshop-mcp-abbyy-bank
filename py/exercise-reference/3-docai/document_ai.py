import base64
import asyncio
from typing import Dict, Any
from dataclasses import dataclass
from abbyy_document_ai import DocumentAi

@dataclass
class UtilityBillData:
    full_name: str
    account_number: str
    address: Dict[str, str]
    issue_date: str
    utility_provider: str

# todo: Initialize the Document AI client with the API key

def read_file_as_base64(file_path: str) -> str:
    """Read a file and return its base64 encoded content"""
    with open(file_path, 'rb') as file:
        file_content = file.read()
        return base64.b64encode(file_content).decode('utf-8')

async def process_utility_bill(image_path: str) -> UtilityBillData:
    """
    Process a utility bill image using Document AI
    Args:
        image_path: Path to the utility bill image file
    Returns:
        UtilityBillData object with extracted information
    """
    # todo: Implement the logic to process the utility bill
