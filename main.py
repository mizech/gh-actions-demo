from csv_util import CsvUtil

def exec():
    words = ["apple", None, "banana", "kiwi"]
    result = CsvUtil.to_csv_line(values=words)
    print(result)

if __name__ == "__main__":
    exec()