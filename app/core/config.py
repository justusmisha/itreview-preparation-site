import os
from dotenv import load_dotenv
import json

load_dotenv()

YANDEX_API_KEY_ID = os.environ.get("YANDEX_API_KEY_ID")
YANDEX_API_KEY = os.environ.get("YANDEX_API_KEY")
CATALOG_ID = os.environ.get("CATALOG_ID")
YANDEX_URL = os.environ.get("YANDEX_URL")
IAM_TOKEN = os.environ.get("IAM_TOKEN")

YANDEX_BODY_JSON = {
  "modelUri": f"gpt://{CATALOG_ID}/yandexgpt",
  "completionOptions": {
    "stream": False,
    "temperature": 0.6,
    "maxTokens": "2000",
    "reasoningOptions": {
      "mode": "DISABLED"
    }
  },
  "messages": [
    {
      "role": "system",
      "text": "Ты умный ассистент для написания тестовых заданий для собеседований"
    },
    {
      "role": "user",
      "text": "Напиши задание которое может попасться на "
              "собеседовании при прохождении на вакансию Python разработчик "
              "по теме декоратор"
    }
  ]
}