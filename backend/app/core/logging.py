import pathlib
import logging

from app.core.config import settings

BASE_PATH = pathlib.Path(__file__).resolve().parent.parent
LOGS_PATH = BASE_PATH/"Logs"
LOGS_PATH.mkdir(parents=True,exist_ok=True)

def setup_logging():
    """
     Configure application logging.
    """
    logging.basicConfig(
        level=settings.LOG_LEVEL,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        handlers=[logging.FileHandler(LOGS_PATH/"app.log"),logging.StreamHandler()]
    )

    # logger = logging.getLogger(__name__)
    logger = logging.getLogger("ai-prompt-playground")
    return logger

logger = setup_logging()

# if __name__ == "__main__":
#     setup_logging()