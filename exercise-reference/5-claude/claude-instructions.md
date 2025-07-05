## Claude Desktop Instructions

Full details found [in MCP docs](https://modelcontextprotocol.io/quickstart/user).

Download Claude if you haven't already: https://claude.ai/download

Open Claude Settings, then Developer tab.

Click on "Edit Config."

This will create a configuration file at:

- macOS: `~/Library/Application\ Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

Open up the configuration file in any text editor. Replace the file contents with this. Note the `args` will be different based on your username and path to this repository on your filesystem.

```json
{
  "mcpServers": {
    "ABBYY-Bank-Account": {
      "command": "node",
      "args": [
        "/Users/USERNAME/Documents/src/abbyy/mcp/workshop-mcp-abbyy-bank/exercise-reference/dist/index.js"
      ]
    },
  }
}
```

Save the file, then restart Claude.

Upon restarting, you should see a slider  icon in the bottom left corner of the input box.

After clicking on the slider icon, you should see the tools that come with the ABBYY Bank MCP Server.


