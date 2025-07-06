#!/usr/bin/env python3
"""
Simple test script to verify the ABBYY Bank MCP server can be imported and initialized.
"""

import sys
import asyncio
from src.index import ABBYYBankMCP

async def test_server():
    """Test that the server can be created and initialized"""
    try:
        print("Creating ABBYY Bank MCP server...")
        agent = ABBYYBankMCP()
        
        print("Initializing server...")
        await agent.init()
        
        print("✅ Server created and initialized successfully!")
        print(f"Server name: {agent.server.name}")
        print(f"Server version: {agent.server.version}")
        print(f"Server capabilities: {agent.server.capabilities}")
        
        return True
    except Exception as e:
        print(f"❌ Error testing server: {e}")
        return False

if __name__ == "__main__":
    success = asyncio.run(test_server())
    sys.exit(0 if success else 1) 
