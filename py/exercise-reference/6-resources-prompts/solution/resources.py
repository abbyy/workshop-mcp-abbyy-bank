import json
from dataclasses import asdict

def register_resources(mcp, state):
    @mcp.resource("abbyy-bank://customer-info")
    def customer_info() -> dict:
        utility_bill = state["documents"]["utilityBill"]
        if utility_bill:
            # Convert dataclass to dict for JSON serialization
            bill_dict = asdict(utility_bill)
            text_content = json.dumps(bill_dict, indent=2)
        else:
            text_content = "No customer information available"
            
        return {
            "contents": [{
                "type": "text",
                "text": text_content,
                "uri": "abbyy-bank://customer-info"
            }]
        } 
