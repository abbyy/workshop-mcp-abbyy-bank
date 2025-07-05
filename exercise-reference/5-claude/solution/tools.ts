import { ABBYYBankMCP } from "./index.js";
import { z } from 'zod';
import { processUtilityBill, UtilityBillData } from './documentAI.js';

export async function initializeTools(agent: ABBYYBankMCP) {

  let billData: UtilityBillData = undefined;

  agent.server.tool("submit-application", "Submit the application to the bank", {}, async () => {
    if (billData === undefined) {
      return {
        content: [{
          type: "text",
          text: "Application cannot be submitted yet. Please upload the required documents."
        }]
      };
    }

    return {
      content: [{
        type: "text",
        text: "Application submitted successfully to ABBYY bank. We'll be in touch shortly after reviewing your application."
      }]
    };
  });

  agent.server.tool(
    "upload-utility-bill",
    "Upload and process an image of a utility bill",
    {
      documentFilepath: z.string().describe("The path to the document file to process")
    },
    async ({ documentFilepath }: { documentFilepath: string }) => {
      try {
        billData = await processUtilityBill(documentFilepath);
        
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
