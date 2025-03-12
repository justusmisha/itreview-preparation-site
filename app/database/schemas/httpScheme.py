from typing import Optional

from pydantic import BaseModel


class HTTPScheme(BaseModel):
    status: int
    headers: dict[str, str]
    text: Optional[str]
