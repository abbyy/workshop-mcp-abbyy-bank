import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { initializeTools } from './tools.js';

export class ABBYYBankMCP {
  server = new McpServer({
    name: 'ABBYYBankMCP',
    version: '1.0.0',
    capabilities: { tools: {} },
  }, {
    instructions: 'This server can help a customer open a new bank account'
  });

  async init() {
		await initializeTools(this);
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
