// Remember to run npm install @abbyy-sdk/document-ai
import { DocumentAi } from "@abbyy-sdk/document-ai";
import fs from 'fs';

// Initialize the Document AI client with the API key
const documentAi = new DocumentAi({
  apiKeyAuth: "Get key from https://developer.abbyy.com",
});

// Interface for utility bill data
export interface UtilityBillData {
  fullName: string;
  accountNumber: string;
  address: {
    street: string;
  };
  issueDate: string;
  utilityProvider: string;
}

/**
 * TODO: Process a utility bill image using Document AI
 * Use the utility bill model with base64 encoded content
 * @param imageUrl URL of the utility bill image
 */
export async function processUtilityBill(imageUrl: string): Promise<UtilityBillData> {
  // for hints, check out: https://docs.abbyy.com/quickstart
}

function readFileAsBase64(filePath: string): string {
  const file = fs.readFileSync(filePath);
  return file.toString("base64");
}

// Export the Document AI client for direct use if needed
export default DocumentAi; 
