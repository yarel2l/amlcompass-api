import sys
import logging

logger = logging.getLogger(__name__)

def custom_exception_handler(exc_type, exc_value, exc_traceback):
    # Si se trata de un ConnectionError, se registra solo el mensaje
    if issubclass(exc_type, (ConnectionError, AttributeError)):
        logger.error(exc_value)
    else:
        # Para otros tipos de error, se utiliza el handler por defecto
        sys.__excepthook__(exc_type, exc_value, exc_traceback)

sys.excepthook = custom_exception_handler


from amlcompass_api.client import AMLCompassAPIClient
from amlcompass_api import exceptions
from amlcompass_api import response

__all__ = [
    "AMLCompassAPIClient",
    "exceptions",
    "response"
]
