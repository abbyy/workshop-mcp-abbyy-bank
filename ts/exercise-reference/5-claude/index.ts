
// todo: update the instructions to provide a robust description of how the bank account workflow should work
export class ABBYYBankMCP {
  server = new McpServer({
    name: 'ABBYYBankMCP',
    version: '1.0.0',
    capabilities: { tools: {}},
  }, {
    instructions: `This app assists customers with opening a new bank account with the fictional ABBYY Bank. 
    Due to the sensitive nature of the application, only use the tools provided to assist the customer.
    When the customer asks to open a bank account, begin by asking for a utility bill to verify their identity and using the upload-utility-bill tool to process it.
    If the utility bill processed successfully, ask the customer if they would like to proceed with submitting their application. 
    If they do, use the submit-application tool to submit the application to the bank.
    If they do not, thank them for their time and end the conversation.`
  });
}

