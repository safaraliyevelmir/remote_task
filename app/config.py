from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    # jwt secret key
    SECRET_KEY: str
    ALGORITHM: str
    ACCESS_TOKEN_EXPIRE_MINUTES: int
    # database url
    DATABASE_URL: str
    
    class Config:
        env_file = ".env"

settings = Settings()

    