import base64
import asyncio
from typing import Dict, Any
from dataclasses import dataclass

# Note: In a real implementation, you would import the ABBYY SDK
# from abbyy_sdk import DocumentAi

@dataclass
class UtilityBillData:
    full_name: str
    account_number: str
    address: Dict[str, str]
    issue_date: str
    utility_provider: str

# Mock Document AI client for demonstration
# In a real implementation, you would use the actual ABBYY SDK
class MockDocumentAi:
    def __init__(self, api_key: str):
        self.api_key = api_key
    
    class Models:
        class UtilityBill:
            async def begin_field_extraction(self, input_source: Dict[str, Any]):
                # Mock response
                return {
                    "documents": [{"id": "mock-document-id"}]
                }
            
            async def get_extracted_fields(self, document_id: str):
                # Mock processed response
                return {
                    "utilityBill": {
                        "meta": {"status": "Processed"},
                        "fields": {
                            "customer": {
                                "name": "John Doe",
                                "accountNumber": "1234567890"
                            },
                            "issuer": {
                                "address": "123 Main St",
                                "name": "Electricity Company"
                            },
                            "billDate": "2024-01-01"
                        }
                    }
                }
    
    @property
    def models(self):
        return self.Models()

# Initialize the Document AI client with the API key
# In production, use: document_ai = DocumentAi(api_key="your_api_key_here")
document_ai = MockDocumentAi(api_key="abbyy_KaADPZtabT2IITvoTozOzZqsUMFFFPb4A63BiFDsDuX27vreL")

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
        extract_request = await document_ai.models.utility_bill.begin_field_extraction({
            "inputSource": {
                "base64EncodedContent": read_file_as_base64(image_path),
                "name": "utility-bill.jpg"
            }
        })
        
        document_id = extract_request.get("documents", [{}])[0].get("id")
        if not document_id:
            raise Exception("Failed to process document")
        
        # Poll for the result
        processed = False
        response = None
        while not processed:
            await asyncio.sleep(0.5)  # Wait 500ms
            response = await document_ai.models.utility_bill.get_extracted_fields({
                "documentId": document_id
            })
            processed = response.get("utilityBill", {}).get("meta", {}).get("status") == "Processed"

        # Extract relevant fields
        response_fields = response.get("utilityBill", {}).get("fields", {})
        return UtilityBillData(
            full_name=response_fields.get("customer", {}).get("name", "Unknown"),
            account_number=response_fields.get("customer", {}).get("accountNumber", "Unknown"),
            address={
                "street": response_fields.get("issuer", {}).get("address", "Unknown")
            },
            issue_date=str(response_fields.get("billDate", "")),
            utility_provider=response_fields.get("issuer", {}).get("name", "")
        )
    except Exception as error:
        print(f"Error processing utility bill: {error}")
        raise error 
