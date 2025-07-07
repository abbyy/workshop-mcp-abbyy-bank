def register_prompts(mcp):
    @mcp.prompt(name="Open Bank Account", description="Begin the bank account application process with ABBYY Bank")
    def open_bank_account() -> str:
        return "I'd like to open a bank account with ABBYY Bank, please." 
