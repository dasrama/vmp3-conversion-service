from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_KEY: str
    REGION_NAME: str = "ap-south-1"

    class Config:
        env_file=".env"