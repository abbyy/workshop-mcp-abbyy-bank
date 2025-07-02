import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

// TODO: add tools capabilities
const server = new McpServer({
    name: 'ABBYYBankMCP',
    version: '1.0.0',
  }, {
    instructions: 'This server can help a customer open a new bank account'
  });

// TODO: define the "upload-utility-bill" tool
// include documentFilepath as a string parameter pointing to the utility bill file
// process the utility bill and return the extracted UtilityBillData
// store the extracted UtilityBillData in the state
// catch and return errors
// See: https://modelcontextprotocol.io/docs/concepts/tools

// TODO: Define state to store OCR'd document data
const state = {};
  
// TODO: implement the processUtilityBill with fake UtilityBillData for now
const processUtilityBill = async (documentFilepath: string) => {}

// todo: add this interface
export interface UtilityBillData {
  fullName: string;
  accountNumber: string;
  address: {
    street: string;
  };
  issueDate: string;
  utilityProvider: string;
}

async function main() {
	// create a new StdioServerTransport
  const transport = new StdioServerTransport();
	// connect the server to the transport
  await server.connect(transport);

	// add a log (using console.error) to the console to let the user know the server is running
  console.error('Server is running');
}

main().catch((error) => {
	console.error('Fatal error in main():', error)
	process.exit(1)
})
