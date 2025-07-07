# Workshop: Creating a Document Processing MCP Server

Companion app for the "AI Agents in the World of IDP" workshop presented at ABBYY DevCon 2025 by Matt Netkow.

## How it works

The workshop is available in two languages: TypeScript and Python. If you prefer Python, work within the `py` folder, otherwise `ts`.

See `TUTORIAL.md` for written instructions. Otherwise, Matt will guide you through each exercise across two sessions.

Repo structure:
- `workspace`: Write code and make changes in here.
- `exercise-reference` folder contains six exercises. Do not make any changes. The files at the root contain instructions on what to implement or change. The `solution` folder contains the solutions in case you get stuck or would like a reference.

## Running the Complete Solution

The `completed` folder within `exercise-reference` contains the complete, working solution after Exercise 6. 

### Python

In a terminal, change into the `completed` directory then:

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
# Create virtual environment and activate it
uv venv
source .venv/bin/activate
# Run MCP inspector tool
uv run mcp dev index.py
```

### TypeScript

In a terminal, change into the `completed` directory then:

```bash
# Install all dependencies
npm install
# Build the MCP server
npm run build
# Build the server then run MCP inspector tool
npm run inspect
```

## Where to go from here
Finished early or curious to explore more? Here are some ideas:

- Add Validation: business logic to verify utility bill data, such as a rule that the bill must be dated no more than three months ago.
- Incorporate Proof of identity: Driver’s License file upload and verification using the ABBYY Vantage API – see TUTORIAL.md for login info.
- Implement Streamable HTTP: Utilize MCP server within a web app. [View Streamable HTTP spec.](https://modelcontextprotocol.io/specification/2025-06-18/basic/transports#streamable-http)


