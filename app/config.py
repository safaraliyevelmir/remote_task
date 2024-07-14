from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # jwt secret key
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # database url
    DATABASE_URL: str

    # smtp server
    SMTP_SERVER: str
    SMTP_PORT: int
    SMTP_USERNAME: str
    SMTP_PASSWORD: str

    class Config:
        env_file = ".env"

settings = Settings()

    