import linecache
import torch
import torchspy

from torchspy.utility.formatting import bytes_human_readable, spaced_string
from torchspy.utility.logging import Logger, PrintLogger, FileLogger
from typing import Callable, Optional

__all__ = ['profile_memory']


class profile_memory(torchspy.trace):
    """Profile memory usage of every executed line of code.

    >>> with profile_memory(file_filter=lambda f: f.startswith("code/")):
            a = torch.ones(5)
            b = torch.zeros(5)
            c = a + b

    Args:
        file_filter: function to filter the files which should be traced.
        output_file: logging file, if None, printing to terminal instead.
        min_abs_memory: minimal number of diff bytes to log line.
    """

    def __init__(self, file_filter: Optional[Callable[[str], bool]] = None,
                 output_file: Optional[str] = None,
                 min_abs_memory: int = 0):
        super(profile_memory, self).__init__(activation_func=file_filter,
                                             tracing_func=self.tracing_func)
        self._logger: Logger = FileLogger(output_file) if output_file is not None else PrintLogger()
        self._last_line = ""
        self._last_memory_usage = 0
        self._min_num_bytes = min_abs_memory

    def tracing_func(self, frame, event, args):
        lineno = frame.f_lineno
        filename = frame.f_code.co_filename
        line = linecache.getline(filename, lineno).replace("\n", "")

        memory_usage = torch.cuda.memory_allocated()
        diff_memory = memory_usage - self._last_memory_usage
        if abs(diff_memory) >= self._min_num_bytes:
            diff_memory = f"Memory: {bytes_human_readable(diff_memory)}"
            location = f"{filename}[{lineno}]"
            info = spaced_string(location, diff_memory, self._last_line, spacings=[120, 12])
            self._logger.log(info)

        self._last_line = line
        self._last_memory_usage = memory_usage

    def __exit__(self, exc_type, exc_val, exc_tb):
        super(profile_memory, self).__exit__(exc_type, exc_val, exc_tb)
        self._logger.close()
