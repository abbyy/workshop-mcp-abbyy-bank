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

# Initialize the Document AI client with the API key
document_ai = DocumentAi(api_key_auth="your key")

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
    try:
        extract_request = document_ai.models.utility_bill.begin_field_extraction(request={
            "input_source": {
                "base64EncodedContent": read_file_as_base64(image_path),
                "name": "utility-bill.jpg"
            }
        })
        
        document_id = extract_request.documents[0].id
        if not document_id:
            raise Exception("Failed to process document")
        
        # Poll for the result
        processed = False
        response = None
        while not processed:
            await asyncio.sleep(0.5)  # Wait 500ms
            response = document_ai.models.utility_bill.get_extracted_fields(
                document_id=document_id
            )
            processed = response.utility_bill.meta.status == "Processed"

        # Extract relevant fields
        response_fields = response.utility_bill.fields
        return UtilityBillData(
            full_name=response_fields.customer.name,
            account_number=response_fields.customer.account_number,
            address={
                "street": response_fields.issuer.address
            },
            issue_date=str(response_fields.bill_date),
            utility_provider=response_fields.issuer.name
        )
    except Exception as error:
        print(f"Error processing utility bill: {error}")
        raise error 
