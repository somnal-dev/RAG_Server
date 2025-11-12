import os

from dotenv import load_dotenv

load_dotenv()

class ServerConfig:
    HOST: str = os.getenv("HOST")
    PORT: int = int(os.getenv("PORT"))

    class Config:
        env_file = ".env"

serverConfig = ServerConfig()