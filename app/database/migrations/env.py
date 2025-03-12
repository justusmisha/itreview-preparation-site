# import sys
# import os

# sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))

import asyncio
from logging.config import fileConfig
from sqlalchemy.ext.asyncio import create_async_engine
from alembic import context
from app.database.base import Base
from app.database.models import *


# Загружаем конфигурацию Alembic
config = context.config

# Устанавливаем логирование, если указано в конфиге
if config.config_file_name:
    fileConfig(config.config_file_name)

# Метаданные для автогенерации
target_metadata = Base.metadata

# URL подключения к базе
DATABASE_URL = config.get_main_option("sqlalchemy.url")

# Создаем асинхронный движок с использованием asyncpg
engine = create_async_engine(DATABASE_URL, future=True, pool_pre_ping=True)

async def run_migrations_online():
    """Запуск миграций в онлайн-режиме."""
    async with engine.begin() as connection:
        await connection.run_sync(lambda sync_conn: context.configure(connection=sync_conn, target_metadata=target_metadata))
        await connection.run_sync(lambda sync_conn: context.run_migrations())


def run_migrations_offline():
    """Запуск миграций в оффлайн-режиме."""
    context.configure(
        url=DATABASE_URL,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
