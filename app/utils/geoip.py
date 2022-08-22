import logging

import geoip2.database

from app.config import settings

logger = logging.getLogger(__name__)


def get_ip_info(public_ip):
    with geoip2.database.Reader(settings.GEO_IP_DATABASE_PATH) as reader:
        response = reader.city(public_ip)
        return response
