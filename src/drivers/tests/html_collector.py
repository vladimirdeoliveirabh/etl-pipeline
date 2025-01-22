from typing import List, Dict


class HtmlCollectorSpy:

    def __init__(self):
        self.collect_essential_information_attributes = {}

    def collect_essential_information(self, html: str) -> List[Dict[str, str]]:
        self.collect_essential_information_attributes["html"] = html
        return [{"name": 'someName', "link": 'https://something.com'}]
