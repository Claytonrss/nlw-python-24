from typing import Dict
from src.drivers.barcode_handler import BarcodeHandler

class CreateTagController:
    def create(self, product_code: str) -> Dict:
        path_tag = self.__create_tag(product_code)
        return self.__format_response(path_tag)

    def __create_tag(self, product_code: str) -> str:
        path_tag = BarcodeHandler().create_barcode(product_code)
        return path_tag

    def __format_response(self, path_tag: str) -> Dict:
        return {
            "data": {
                "type": "Tag Image",
                "count": 1,
                "path": f'{path_tag}.png'
            }
        }
