
from fastmcp import FastMCP
import random

mcp = FastMCP("SimpleMCP")


@mcp.tool()
def generate_random_number():
    """Generate a random number between 1 and 100."""
    return random.randint(1, 100)


@mcp.tool()
def add_numbers(a: int, b: int):
    """Add two numbers and return their sum."""
    return a + b


if __name__ == "__main__":
    mcp.run(transport="http", host="0.0.0.0", port=8000)