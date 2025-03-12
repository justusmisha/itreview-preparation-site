from fastapi import APIRouter
from app.core.AI_service.yandex_client import YandexGPTClient
from app.database.schemas.YandexScheme import YandexScheme


router = APIRouter()

@router.post('/yandex')
async def get_yandex_task_endpoint(request: YandexScheme) -> str:
    yandex_client = YandexGPTClient()
    message = await yandex_client.run(request.message)
    return message
