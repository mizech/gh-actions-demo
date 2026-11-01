# import typing
from typing import TypeVar

class Paginator:
    T = TypeVar("T")

    @staticmethod
    def get_page(items: list[T], page_number: int, page_size: int) -> list[T]:
        if items is None:
            raise Exception("Items can't be none.")
        if page_number <= 0:
            raise Exception("Page number must be greater then zero.")
        if page_size <= 0:
            raise Exception("Page size must be greate then zero.")

        results = []
        start = (page_number - 1) * page_size
        i = start

        while i < (start + page_size) and i < len(items):
            results.append(items[i])
            i += 1
        
        return results
         
