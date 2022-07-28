import os
import sys

from typing import Callable, Optional


class trace:

    def __init__(self, activation_func: Optional[Callable[[str], bool]], tracing_func: Callable):
        self.activation_func = activation_func
        self.tracing_func = tracing_func

    def __enter__(self):
        def event_tracing(frame, event, args):
            file_path = os.path.abspath(frame.f_code.co_filename)
            if self.activation_func is None or self.activation_func(file_path):
                return self.tracing_func
            return None

        sys.settrace(event_tracing)

    def __exit__(self, exc_type, exc_val, exc_tb):
        sys.settrace(None)
