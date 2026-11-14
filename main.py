import asyncio
from connection import Connection
from dotenv import load_dotenv

load_dotenv("private.env")

# Ejemplo de uso
if __name__ == "__main__":
    async def main():
        conn = Connection()
        token = await conn.get_token()
        print(f"✅ Token: {token}")

    asyncio.run(main())