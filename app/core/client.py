import aiohttp
import ssl

from app.database.schemas.httpScheme import HTTPScheme


class AioHttpClient:
    def __init__(self):
        self.session = None
        self.ssl_context = ssl.create_default_context()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE  # Disable SSL verification

    async def __aenter__(self):
        self.session = aiohttp.ClientSession()
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        if self.session:
            await self.session.close()

    async def request(self, method, url, **kwargs) -> HTTPScheme:
        if not self.session:
            raise RuntimeError("Session is not initialized. Use 'async with' to create a session.")
        async with self.session.request(method, url, ssl=self.ssl_context, **kwargs) as response:
            return HTTPScheme(
                    status=response.status,
                    headers=dict(response.headers),
                    text=await response.text() if await response.text() else None,
                )
