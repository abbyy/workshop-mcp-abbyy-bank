from document_ai import process_utility_bill

def register_tools(mcp, state):
    @mcp.tool()
    async def upload_utility_bill(documentFilepath: str) -> dict:
        try:
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
