import { DocumentAi } from "@abbyy-sdk/document-ai";
import fs from 'fs';

// Initialize the Document AI client with the API key
const documentAi = new DocumentAi({
  apiKeyAuth: "abbyy_KaADPZtabT2IITvoTozOzZqsUMFFFPb4A63BiFDsDuX27vreL",
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
 * Process a utility bill image using Document AI
 * @param imageUrl URL of the utility bill image
 */
export async function processUtilityBill(imageUrl: string): Promise<UtilityBillData> {
  try {
    const extractRequest = await documentAi.models.utilityBill.beginFieldExtraction({
      inputSource: {
        base64EncodedContent: readFileAsBase64(imageUrl),
        name: "utility-bill.jpg"
      },
    });
    
    const documentId = extractRequest.documents?.[0]?.id;
    if (!documentId) {
      throw new Error("Failed to process document");
    }
    
    // Poll for the result
    let processed = false;
    let response;
    while (!processed) {
      await new Promise((resolve) => setTimeout(resolve, 500));
      response = await documentAi.models.utilityBill.getExtractedFields({
        documentId: documentId,
      });
      processed = response.utilityBill?.meta.status === "Processed";
    }

    // Extract relevant fields
    let responseFields = response?.utilityBill?.fields;
    return {
      fullName: responseFields?.customer?.name || "Unknown",
      accountNumber: responseFields?.customer?.accountNumber || "Unknown",
      address: {
        street: responseFields?.issuer?.address || "Unknown"
      },
      issueDate: responseFields?.billDate?.toString() || "",
      utilityProvider: responseFields?.issuer?.name || ""
    };
  } catch (error) {
    console.error("Error processing utility bill:", error);
    throw error;
  }
}

function readFileAsBase64(filePath: string): string {
  const file = fs.readFileSync(filePath);
  return file.toString("base64");
}

// Export the Document AI client for direct use if needed
export default DocumentAi; 
