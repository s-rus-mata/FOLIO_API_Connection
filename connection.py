import aiohttp
import ssl
import certifi
# import config
import os
from dotenv import load_dotenv

load_dotenv("private.env")


class Connection:
    def __init__(self):
        self.api_url = os.getenv("API_URL")
        self.tenant = os.getenv("API_TENANT")
        self.username = os.getenv("API_USERNAME")
        self.password = os.getenv("API_PASSWORD")
        self.token = None
        self.ssl_context = ssl.create_default_context(cafile=certifi.where())

    async def get_token(self):
        # Si ya hay token, verificar que siga funcionando
        if self.token and await self._is_token_valid(self.token):
            return self.token

        # Obtener nuevo token
        url = f"{self.api_url}/authn/login"
        headers = {
            "Content-Type": "application/json",
            "x-okapi-tenant": self.tenant
        }
        payload = {
            "username": self.username,
            "password": self.password
        }

        async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=self.ssl_context)) as session:
            async with session.post(url, json=payload, headers=headers) as response:
                if response.status == 201:
                    self.token = response.headers.get("x-okapi-token")
                    return self.token
                else:
                    text = await response.text()
                    raise Exception(f"❌ Error al obtener token: {response.status} {text}")

    async def _is_token_valid(self, token):
        """Hace una llamada simple protegida para ver si el token sigue siendo válido."""
        test_url = f"{self.api_url}/users?limit=1"  # Endpoint liviano y común
        headers = {
            "x-okapi-token": token,
            "x-okapi-tenant": self.tenant,
            "Content-Type": "application/json"
        }

        try:
            async with aiohttp.ClientSession(connector=aiohttp.TCPConnector(ssl=self.ssl_context)) as session:
                async with session.get(test_url, headers=headers) as response:
                    return response.status != 401
        except Exception as e:
            print(f"⚠️ Error al validar token: {e}")
            return False
