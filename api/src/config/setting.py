from typing import Any, Dict, Optional

from pydantic_settings  import BaseSettings
from pydantic import validator


class Settings(BaseSettings):

    API_V1_STR: str = "/api/v1"
    APP_NAME: str="test_api"
    DOMAIN: str="0.0.0.0"
    DEBUG_MODE: bool = True
    # FAST_APP:str
    BACKEND_PORT: int=8000


    @validator("BACKEND_PORT", pre=True)
    def SetPortDefault(cls, v: str):
        if v:
            return v
        return 8001

settings = Settings()
