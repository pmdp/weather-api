import logging

import httpx

from app.config import settings

logger = logging.getLogger(__name__)


async def do_request_to_current_weather(params):
    headers = {
        "Accept": "application/json"
    }
    with httpx.Client(headers=headers, params=params) as client:
        response = client.get(settings.OPENWEATHER_CURRENT_API_ENDPOINT, headers=headers, params=params)
        logger.info(
            f"Request to weather API done: status:({response.status_code}), content:({response.text})")
        return response.status_code, response.text
