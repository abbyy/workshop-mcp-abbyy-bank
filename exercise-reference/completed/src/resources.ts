import { ABBYYBankMCP } from "./index.js";
import { z } from 'zod';

export async function initializeResources(agent: ABBYYBankMCP) {

  agent.server.registerResource(
  "customer-info",
  "abbyy-bank://customer-info",
  {
    fullName: z.string().describe("The full name of the customer"),
    accountNumber: z.string().describe("The account number of the customer"),
    address: z.object({
      street: z.string().describe("The street of the customer's address")
    }).describe("The address of the customer"),
  },
  async (uri) => {
    return {
      contents: [{ 
        type: "text",
        text: JSON.stringify(agent.state.documents.utilityBill, null, 2),
        uri: uri.toString()
      }]
    };
  }
);
}
