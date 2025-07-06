def register_prompts(mcp, state):
    @mcp.prompt(title="Open Bank Account", description="Begin the bank account application process with ABBYY Bank")
    def open_bank_account() -> dict:
        return {
            "messages": [
                {
                    "role": "user",
                    "content": {
                        "type": "text",
                        "text": "I'd like to open a bank account with ABBYY Bank, please."
                    }
                }
            ]
        } 
