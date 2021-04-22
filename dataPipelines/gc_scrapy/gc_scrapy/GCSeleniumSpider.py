# -*- coding: utf-8 -*-
import scrapy

from dataPipelines.gc_scrapy.gc_scrapy.runspider_settings import general_settings, selenium_settings
from dataPipelines.gc_scrapy.gc_scrapy.middleware_utils.selenium_request import SeleniumRequest
from dataPipelines.gc_scrapy.gc_scrapy.GCSpider import GCSpider


class GCSeleniumSpider(GCSpider):
    """
        Selenium Spider with settings applied and selenium request returned for the standard parse method used in crawlers
    """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    custom_settings = {**general_settings, **selenium_settings}
    selenium_request_overrides: dict

    def start_requests(self):
        """
            Applies selenium_request_overrides dict and returns a selenium response instead of standard scrapy response
        """
        yield SeleniumRequest(
            url=self.start_urls[0],
            callback=self.parse,
            wait_time=5,
            **self.selenium_request_overrides
        )
