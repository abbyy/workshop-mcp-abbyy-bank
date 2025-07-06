# ABBYY Bank MCP Workshop Tutorial

Welcome to the ABBYY Bank MCP Workshop! This tutorial will guide you through building a Model Context Protocol (MCP) server that helps customers open bank accounts by processing utility bills using ABBYY's Document AI.

## Prerequisites

- Node.js (v18 or higher)
- npm or yarn
- An ABBYY Document AI API key (get one at https://developer.abbyy.com)
- Claude Desktop (for testing the final MCP server)

## Setup

1. Navigate to the `workspace` directory
2. Run `npm install` to install dependencies
3. Copy the sample documents from `sample-documents/` to your workspace if needed

## Exercise 1: Foundation - Basic MCP Server Setup

**Objective**: Create a basic MCP server with proper configuration and transport setup.

**Starting Point**: `exercise-reference/1-foundation/index.ts`

**What You Need to Do**:

1. **Uncomment the imports** at the top of the file:
   ```typescript
   import { McpServer } from '@modelcontextprotocol/sdk/server/mcp.js'
   import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js'
   ```

2. **Create the MCP server** before the `main()` function:
   ```typescript
   const server = new McpServer({
     name: 'ABBYYBankMCP',
     version: '1.0.0',
   }, {
     instructions: 'This server can help a customer open a new bank account'
   });
   ```

3. **Complete the main() function**:
   - Create a new `StdioServerTransport`
   - Connect the server to the transport
   - Add a console log to indicate the server is running

**Expected Result**: A basic MCP server that can start up and connect via stdio transport.

**To Test**: Run `npm run build` and `npm run inspect` to see the server in action.

---

## Exercise 2: Tools - Adding Document Upload Capability

**Objective**: Add tool capabilities to the MCP server for processing utility bills.

**Starting Point**: `exercise-reference/2-tools/index.ts`

**What You Need to Do**:

1. **Add tools capability** to the server configuration:
   ```typescript
   const server = new McpServer({
     name: 'ABBYYBankMCP',
     version: '1.0.0',
     capabilities: { tools: {} },
   }, {
     instructions: 'This server can help a customer open a new bank account'
   });
   ```

2. **Define the state object** to store processed documents:
   ```typescript
   const state = {
     documents: {
       utilityBill: null as UtilityBillData | null
     }
   };
   ```

3. **Implement the processUtilityBill function** with mock data:
   ```typescript
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
   ```

4. **Add the upload-utility-bill tool** using `server.tool()`:
   - Tool name: "upload-utility-bill"
   - Description: "Upload and process an image of a utility bill"
   - Parameter: `documentFilepath` as a string
   - Implementation: Call `processUtilityBill`, store result in state, return success/error response

**Expected Result**: An MCP server with a tool that can accept file paths and return mock utility bill data.

**To Test**: Run `npm run build` and `npm run inspect`, then test the tool with a sample document path.

---

## Exercise 3: Document AI Integration

**Objective**: Integrate ABBYY Document AI to process real utility bills.

**Starting Point**: `exercise-reference/3-docai/`

**What You Need to Do**:

1. **Install the ABBYY SDK**:
   ```bash
   npm install @abbyy-sdk/document-ai
   ```

2. **Update your API key** in `documentAI.ts`:
   ```typescript
   const documentAi = new DocumentAi({
     apiKeyAuth: "YOUR_ABBYY_API_KEY_HERE",
   });
   ```

3. **Implement the processUtilityBill function** in `documentAI.ts`:
   - Use `documentAi.models.utilityBill.beginFieldExtraction()`
   - Pass the base64-encoded file content
   - Poll for completion using `getExtractedFields()`
   - Extract and return the relevant fields (customer name, account number, address, etc.)

4. **Update index.ts**:
   - Uncomment the import for `processUtilityBill` and `UtilityBillData`
   - Remove the duplicate interface and mock function

**Expected Result**: An MCP server that can process real utility bill images using ABBYY Document AI.

**To Test**: Use the sample documents in `sample-documents/` to test the real document processing.

---

## Exercise 4: Code Refactoring

**Objective**: Refactor the code into a cleaner, more maintainable structure.

**Starting Point**: `exercise-reference/4-refactor/`

**What You Need to Do**:

1. **Create the ABBYYBankMCP class** in `index.ts`:
   - Move the server configuration into the class
   - Add a state property to store documents
   - Add an `init()` method to initialize tools

2. **Move the tool implementation** to `tools.ts`:
   - Create an `initializeTools()` function that takes an `ABBYYBankMCP` instance
   - Move the `upload-utility-bill` tool from `index.ts` to this function
   - Update the tool to use `agent.state` and `agent.server`

3. **Update the main function** to use the new class structure

**Expected Result**: Cleaner, more organized code with better separation of concerns.

**To Test**: Ensure the server still works as expected after refactoring.

---

## Exercise 5: Enhanced Instructions and Workflow

**Objective**: Improve the MCP server instructions and add a complete bank account application workflow.

**Starting Point**: `exercise-reference/5-claude/`

**What You Need to Do**:

1. **Update the server instructions** in `index.ts` to provide a comprehensive workflow description:
   - Explain the bank account opening process
   - Specify when to use each tool
   - Include error handling and validation steps

2. **Add a new tool** in `tools.ts`:
   - Tool name: "submit-application"
   - Description: "Submit the application to the bank"
   - Implementation: Check if utility bill is processed, then return success message

3. **Configure Claude Desktop** (optional for testing):
   - Follow the instructions in `claude-instructions.md`
   - Update the configuration file with your path
   - Restart Claude to see the MCP tools

**Expected Result**: An MCP server with clear instructions and a complete workflow for bank account applications.

**To Test**: Use Claude Desktop to interact with the MCP server and test the complete workflow.

---

## Exercise 6: Resources and Prompts

**Objective**: Add MCP resources and prompts to enhance the user experience.

**Starting Point**: `exercise-reference/6-resources-prompts/`

**What You Need to Do**:

1. **Implement prompts** in `prompts.ts`:
   - Create an `initializePrompts()` function
   - Register a "open-bank-account" prompt that provides a starting message for the workflow

2. **Implement resources** in `resources.ts`:
   - Create an `initializeResources()` function
   - Register a "customer-info" resource that returns the processed utility bill data
   - Use the ABBYY Bank URI scheme (`abbyy-bank://customer-info`)

3. **Update the main class** to initialize both prompts and resources

**Expected Result**: An MCP server with prompts to guide users and resources to access processed data.

**To Test**: Use Claude Desktop to test the prompts and access the customer information resource.

---

## Final Testing

Once you've completed all exercises:

1. **Build the project**: `npm run build`
2. **Test with MCP Inspector**: `npm run inspect`
3. **Test with Claude Desktop**: Follow the configuration instructions to connect your MCP server
4. **Test the complete workflow**:
   - Start a conversation about opening a bank account
   - Upload a utility bill using the provided sample documents
   - Submit the application
   - Access customer information through resources

## Troubleshooting

- **API Key Issues**: Ensure your ABBYY Document AI API key is valid and has the necessary permissions
- **Build Errors**: Check that all imports are correct and dependencies are installed
- **MCP Connection Issues**: Verify the configuration file path in Claude Desktop settings
- **Document Processing Errors**: Check that the sample documents are accessible and in the correct format

## Next Steps

After completing the tutorial, consider these enhancements:

- Add validation logic for utility bill data (e.g., bill must be recent)
- Implement additional document types (driver's license, passport)
- Add error handling and retry logic for API calls
- Create a web interface using MCP's HTTP transport
- Add more sophisticated business logic for account approval

## Resources

- [MCP TypeScript SDK Documentation](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Core Architecture](https://modelcontextprotocol.io/docs/concepts/architecture)
- [MCP Inspector](https://modelcontextprotocol.io/docs/tools/inspector)
- [ABBYY Document AI Documentation](https://docs.abbyy.com/quickstart)
- [Claude Desktop MCP Setup](https://modelcontextprotocol.io/quickstart/user)

Happy coding! 🚀 
