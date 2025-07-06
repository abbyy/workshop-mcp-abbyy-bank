import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { initializeTools } from './tools.js';
import { initializeResources } from './resources.js';
import { initializePrompts } from './prompts.js';
import { UtilityBillData } from './documentAI.js';

export class ABBYYBankMCP {
  state = {
    documents: {
      utilityBill: null as UtilityBillData | null,
    }
  };
  

  server = new McpServer({
    name: 'ABBYYBankMCP',
    version: '1.0.0',
    capabilities: { tools: {}, resources: {}, prompts: {} },
  }, {
    instructions: `This app assists customers with opening a new bank account with the fictional ABBYY Bank. 
    Due to the sensitive nature of the application, only use the tools provided to assist the customer.
    When the customer asks to open a bank account, begin by asking for a utility bill to verify their identity and using the upload-utility-bill tool to process it.
    If the utility bill processed successfully, ask the customer if they would like to proceed with submitting their application. 
    If they do, use the submit-application tool to submit the application to the bank.
    If they do not, thank them for their time and end the conversation.`
  });

  async init() {
		await initializeTools(this);
		await initializeResources(this);
		await initializePrompts(this);
	}
}

async function main() {
  const agent = new ABBYYBankMCP();
  await agent.init();
  // create a new StdioServerTransport
  const transport = new StdioServerTransport();
	// connect the server to the transport
  await agent.server.connect(transport);

	// add a log (using console.error) to the console to let the user know the server is running
  console.error('Server is running');
}

main().catch((error) => {
	console.error('Fatal error in main():', error)
	process.exit(1)
})
