import logging
import requests
import allure
from typing import Any, Dict, Optional
from src.framework.core.config import settings

logger = logging.getLogger(__name__)

class BaseClient:
    def __init__(self, base_url: Optional[str] = None):
        self.base_url = base_url or settings.base_url
        self.session = requests.Session()

    def _request(self, method: str, endpoint: str, **kwargs) -> requests.Response:
        url = f"{self.base_url}{endpoint}"
        
        # Log request as curl for transparency
        self._log_request(method, url, **kwargs)
        
        response = self.session.request(method, url, timeout=settings.timeout, **kwargs)
        
        # Log and attach response
        self._log_response(response)
        self._attach_allure(method, url, response, **kwargs)
        
        return response

    def _log_request(self, method: str, url: str, **kwargs):
        headers = kwargs.get("headers", {})
        data = kwargs.get("json") or kwargs.get("data")
        curl = f"curl -X {method} '{url}'"
        for k, v in headers.items():
            curl += f" -H '{k}: {v}'"
        if data:
            curl += f" -d '{data}'"
        
        logger.info(f"API Request: {curl}")

    def _log_response(self, response: requests.Response):
        logger.info(f"API Response [{response.status_code}]: {response.text[:500]}")

    def _attach_allure(self, method: str, url: str, response: requests.Response, **kwargs):
        with allure.step(f"{method} {url}"):
            allure.attach(
                str(kwargs.get("headers")),
                name="Request Headers",
                attachment_type=allure.attachment_type.TEXT
            )
            if kwargs.get("json"):
                allure.attach(
                    str(kwargs.get("json")),
                    name="Request Body",
                    attachment_type=allure.attachment_type.JSON
                )
            allure.attach(
                f"Status: {response.status_code}\nBody: {response.text}",
                name="Response",
                attachment_type=allure.attachment_type.TEXT
            )
