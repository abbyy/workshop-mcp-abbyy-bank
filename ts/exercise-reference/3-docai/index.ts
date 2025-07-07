import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
import { z } from 'zod';
// todo: uncomment this 
//import { processUtilityBill, UtilityBillData } from './documentAI.js';

const server = new McpServer({
    name: 'ABBYYBankMCP',
    version: '1.0.0',
    capabilities: { tools: {} },
  }, {
    instructions: 'This server can help a customer open a new bank account'
  });

server.tool(
    "upload-utility-bill",
    "Upload and process an image of a utility bill",
    {
      documentFilepath: z.string().describe("The path to the document file to process")
    },
    async ({ documentFilepath }: { documentFilepath: string }) => {
      try {
        const billData = await processUtilityBill(documentFilepath);
        
        // Store the processed data
        state.documents.utilityBill = billData;
        
        return {
          content: [{
            type: "text",
            text: JSON.stringify({
              status: "success",
              message: "Utility bill processed successfully",
              data: billData
            }, null, 2)
          }]
        };
      } catch (error) {
        console.error("Error processing utility bill:", error);
        return {
          isError: true,
          content: [{
            type: "text",
            text: `Error processing utility bill: ${error instanceof Error ? error.message : String(error)}`
          }]
        };
      }
    }
  );

// State to store documents and validation results
const state = {
  documents: {
    utilityBill: null as UtilityBillData | null
  }
};

// todo: remove in favor of the interface in documentAI.ts
export interface UtilityBillData {
  fullName: string;
  accountNumber: string;
  address: {
    street: string;
  };
  issueDate: string;
  utilityProvider: string;
}

// todo: remove in favor of the function in documentAI.ts
const processUtilityBill = async (documentFilepath: string) => {
  return {
    fullName: "John Doe",
    accountNumber: "1234567890",
    address: {
      street: "123 Main St",
    },
    issueDate: "2024-01-01",
    utilityProvider: "Electricity Company"
  }
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
