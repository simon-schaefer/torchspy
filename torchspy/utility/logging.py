from typing import Protocol


class Logger(Protocol):

    def log(self, message: str):
        ...

    def close(self):
        ...


class PrintLogger:

    @staticmethod
    def log(message: str):
        print(message)

    @staticmethod
    def close():
        pass


class FileLogger:

    def __init__(self, file: str, mode: str = "w+"):
        self.output_file = open(file, mode=mode)

    def log(self, message: str):
        self.output_file.write(message + "\n")

    def close(self):
        self.output_file.close()
