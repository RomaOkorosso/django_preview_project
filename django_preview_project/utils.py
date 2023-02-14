import datetime
import logging

from rest_framework.request import Request


def log(request: Request):
    logger = logging.getLogger('django')
    time = datetime.datetime.now()
    logger.exception(time.strftime("%Y-%m-%d %H:%M:%S") + ' - ' + str(request.user))
