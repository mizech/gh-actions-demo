class CsvUtil:
    @staticmethod
    def to_csv_line(values: list) -> str:
        if values == None:
            raise Exception("Values can not be None.")

        results: list[str] = []
        for item in values:
            if item != None and len(item) > 0:
                results.append(item)

        if len(results) == 0:
            return ""
        else:
            return ",".join(results)
