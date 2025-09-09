from pydantic_settings import BaseSettings


class Settings(BaseSettings):
    AWS_ACCESS_KEY_ID: str
    AWS_SECRET_KEY: str
    REGION_NAME: str = "ap-south-1"
    VIDEO_QUEUE: str = "VIDEO_QUEUE"
    MP3_QUEUE: str = "MP3_QUEUE"
    class Config:
        env_file=".env"