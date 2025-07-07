import { ABBYYBankMCP } from "./index.js";

export async function initializePrompts(agent: ABBYYBankMCP) {

  agent.server.registerPrompt(
  "open-bank-account",
  {
			title: 'Open Bank Account',
			description: 'Begin the bank account application process with ABBYY Bank',
			argsSchema: {}
	},
  async () => {
    return {
				messages: [
					{
						role: 'user',
						content: {
							type: 'text',
							text: `I'd like to open a bank account with ABBYY Bank, please.`
						},
					},
				],
      }
   }
)
}
