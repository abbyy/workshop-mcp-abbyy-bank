import json

def register_resources(mcp, state):
    @mcp.resource("abbyy-bank://customer-info")
    def customer_info() -> dict:
        return {
            "contents": [{
                "type": "text",
                "text": json.dumps(state["documents"]["utilityBill"], indent=2) if state["documents"]["utilityBill"] else "No customer information available",
                "uri": "abbyy-bank://customer-info"
            }]
        } 
