import logging

# logging.getLogger('numba').setLevel(logging.WARNING)

class LogSuppressFilter(logging.Filter):
    def filter(self, record):
        return False

logger = logging.getLogger("uvicorn.error")
logger.addFilter(LogSuppressFilter())


logger = logging.getLogger("matplotlib")
logger.addFilter(LogSuppressFilter())

logger = logging.getLogger("matplotlib.font_manager")
logger.addFilter(LogSuppressFilter())


# logger.propagate = False

logger = logging.getLogger("multipart.multipart")
logger.propagate = False

logging.getLogger('asyncio').setLevel(logging.WARNING)
