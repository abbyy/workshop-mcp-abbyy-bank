import { ABBYYBankMCP } from "./index.js";
import { z } from 'zod';
import { processUtilityBill } from './documentAI.js';

export async function initializeTools(agent: ABBYYBankMCP) {

  // todo: create submit application tool
  

  agent.server.tool(
    "upload-utility-bill",
    "Upload and process an image of a utility bill",
    {
      documentFilepath: z.string().describe("The path to the document file to process")
    },
    async ({ documentFilepath }: { documentFilepath: string }) => {
      try {
        const billData = await processUtilityBill(documentFilepath);
        
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
}
