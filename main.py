from app.core.AI_service.yandex_client import YandexGPTClient
import asyncio


async def main() -> None:
    yandex_client = YandexGPTClient()
    print(await yandex_client.run("Напиши задание которое может попасться на собеседовании при прохождении на вакансию Python разработчик по теме контекстный менеджер"))


if __name__ == "__main__":
    asyncio.run(main())