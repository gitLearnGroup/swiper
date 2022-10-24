from loguru import logger
from django.conf import settings
import os

LOGGER_BASE_DIR = os.path.join(settings.BASE_DIR, 'logs')


def debug_filter(record):
    return record['level'].name == 'DEBUG'


def info_filter(record):
    return record['level'].name == 'INFO'


logger.add(
    sink=f'{LOGGER_BASE_DIR}/DEBUG.log',
    level='DEBUG',
    format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}",
    filter=debug_filter,
    rotation='1 week',
    retention='4 week',
    compression='zip'
)


logger.add(
    sink=f'{LOGGER_BASE_DIR}/INFO.log',
    level='INFO',
    format="{time:YYYY-MM-DD at HH:mm:ss} {level} {message}",
    filter=info_filter,
    rotation='1 week',
    retention='4 week',
    compression='zip'
)

logger.add(
    sink=f'{LOGGER_BASE_DIR}/WARNING.log',
    level='WARNING',
    format="{time:YYYY-MM-DD at HH:mm:ss} {level} {module}-{name} {message}",
    rotation='1 week',
    retention='4 week',
    compression='zip'
)

logger.add(
    sink=f'{LOGGER_BASE_DIR}/ERROR.log',
    level='ERROR',
    format="{time:YYYY-MM-DD at HH:mm:ss} {level} {module}-{name}**{process}-{thread} {message}",
    rotation='1 week',
    retention='4 week',
    compression='zip'
)
