import json
from app.core.client import AioHttpClient
from app.core import config


class YandexGPTClient:
    def __init__(self):
        self.url = config.YANDEX_URL

        if config.IAM_TOKEN:
            self.headers = {'Authorization': f'Bearer {config.IAM_TOKEN}'}
        elif config.YANDEX_API_KEY:
            self.headers = {'Authorization': f'Api-Key {config.YANDEX_API_KEY}'}
        else:
            self.headers = {}

    async def run(self, message:str=None) -> str:
        if message:
            config.YANDEX_BODY_JSON["messages"][-1]["text"] = message

        # Асинхронно делаем запрос к YandexGPT
        async with AioHttpClient() as client:
            resp = await client.request('POST', self.url, headers=self.headers, data=json.dumps(config.YANDEX_BODY_JSON))

        if resp.status != 200:
            raise RuntimeError(
                f"Invalid response received: code: {resp.status}"
            )
        return json.loads(resp.text).get("result", {}).get("alternatives", [{}])[0].get("message", {}).get("text", "")

