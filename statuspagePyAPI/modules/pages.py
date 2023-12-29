from typing import Union, Dict, Any

from requests import Response

from statuspagePyAPI.modules.custom_session import CustomSession

from statuspagePyAPI.utils.response_handler import ResponseHandler


class Pages(ResponseHandler):
    def __init__(self, api_key: str, base_url: str, raw_response: bool = False):
        super().__init__(raw_response)
        self._api_key: str = api_key
        self._base_url: str = base_url
        self._session = CustomSession(api_key)

    def get_pages(self) -> Union[Dict[str, Any], Response]:
        """
        获取页面列表
        :return: 返回页面列表
        """
        url = f'{self._base_url}/pages'
        response = self._session.get(url)
        return self.process_response(response)

    def get_page(self, page_id: str) -> Union[Dict[str, Any], Response]:
        """
        获取页面信息
        :param page_id: 页面ID
        :return: 返回页面信息
        """
        url = f'{self._base_url}/pages/{page_id}'
        response = self._session.get(url)
        return self.process_response(response)

    def update_page(self, page_id: str, **kwargs: Any) -> Union[Dict[str, Any], Response]:
        """
        更新页面信息
        :param page_id: 页面ID
        :param kwargs: 详见 https://developer.statuspage.io/#operation/patchPagesPageId
        :return: 返回更新后的页面信息
        """
        url = f'{self._base_url}/pages/{page_id}'
        response = self._session.patch(url, json={'page': kwargs})
        return self.process_response(response)
