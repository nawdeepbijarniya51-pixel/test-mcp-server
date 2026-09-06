from fastmcp import FastMCP


mcp = FastMCP(name = "Test Server")


@mcp.tool(name = "add", description = "Adds two numbers")
def add_tool(a: int, b: int):
    return a + b

@mcp.tool(name = "dice", description = "Rolls a dice with a specified number of sides")
def dice_roll_tool(no_roll: int) -> list[int]:
    import random
    return [random.randint(1, 6) for _ in range(no_roll)]

if __name__ == "__main__":
    mcp.run(transport="http",host="0.0.0.0",port=8000)