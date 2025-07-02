// import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
// import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'

// Create a new McpServer
// - Use the name 'ABBYYBankMCP' and a version of '1.0.0'
// - Set instructions for the LLM to know what this server can be used to do (to start, it can help a customer open a new bank account)
// The MCP TypeScript SDK docs, for reference: https://github.com/modelcontextprotocol/typescript-sdk
// Core architecture: https://modelcontextprotocol.io/docs/concepts/architecture
// MCP Inspector: https://modelcontextprotocol.io/docs/tools/inspector
// "npm run inspect" to see the inspector in action

async function main() {
	// create a new StdioServerTransport
	// connect the server to the transport

	// add a log (using console.error) to the console to let the user know the server is running
}

main().catch((error) => {
	console.error('Fatal error in main():', error)
	process.exit(1)
})
