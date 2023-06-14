import secrets
import os
from typing import Any, Dict, Optional
from pydantic import BaseSettings, PostgresDsn, validator
from dotenv import load_dotenv
load_dotenv()


class Settings(BaseSettings):
    ENV: str = 'development'
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = os.getenv("SECRET_KEY")
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8



    POSTGRES_SERVER: str = os.environ.get("POSTGRES_SERVER")
    POSTGRES_USER: str = os.environ.get('POSTGRES_USER')
    POSTGRES_PASSWORD: str = os.environ.get('POSTGRES_PASSWORD')
    POSTGRES_DB: str = os.environ.get('POSTGRES_DB')

    QUEUE_HOST: str = os.environ.get('QUEUE_HOST') or 'localhost'
    QUEUE_PORT: str = os.environ.get('QUEUE_PORT') or '6379'
    QUEUE_DB: str = os.environ.get('QUEUE_DB') or 1

    AWS_S3_ACCESS_KEY_ID: str = os.environ.get('AWS_S3_ACCESS_KEY_ID')
    AWS_S3_SECRET_ACCESS_KEY: str = os.environ.get('AWS_S3_SECRET_ACCESS_KEY')
    S3_BUCKET_NAME: str = os.environ.get('S3_BUCKET_NAME')
    REGION_NAME: str = os.environ.get('REGION_NAME')
    S3_URL: str = os.environ.get('S3_URL')

    BACKEND_URL: str = os.environ.get('BACKEND_URL')

    SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] = None

    @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
        if isinstance(v, str):
            return v
        return PostgresDsn.build(
            scheme="postgresql",
            user=values.get("POSTGRES_USER"),
            password=values.get("POSTGRES_PASSWORD"),
            host=values.get("POSTGRES_SERVER"),
            path=f"/{values.get('POSTGRES_DB') or ''}",
        )

    class Config:
        case_sensitive = True


settings = Settings()
