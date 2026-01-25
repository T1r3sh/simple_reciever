import os
from dotenv import load_dotenv

load_dotenv()


class Settings:

    API_TOKEN: str = os.getenv("API_TOKEN", "asdf")
    DEBUG: bool = os.getenv("DEBUG", "false").lower() == "true"
    DATA_DIR: str = os.getenv("DATA_DIR", "data")

    # API settings
    API_V1_PREFIX: str = "/api/v1"
    PROJECT_NAME: str = "DataReceiverAPI"
    VERSION: str = "1.0.0"
    DESCRIPTION: str = "Апи для принятия данных Сергея"


settings = Settings()
