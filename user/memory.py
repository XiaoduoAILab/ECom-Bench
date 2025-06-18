from mcp.server.fastmcp import FastMCP

mcp = FastMCP("customer")

@mcp.tool()
async def get_user_tool() -> str:
    """Get user tool"""
    return "may someday user need tools, that is why we make this"

if __name__ == "__main__":
    mcp.run(transport="stdio")