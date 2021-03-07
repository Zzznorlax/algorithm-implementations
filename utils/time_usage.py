import timeit
import inspect

from functools import wraps
from logging import Logger
from typing import Optional


DEFAULT_LOGGER_KWARG_KEY = "debug_logger"


def log_time_usage(logger_kwarg_key: str = DEFAULT_LOGGER_KWARG_KEY):
    """Logs time usage of func
    """

    def log_time_usage_inner(f):
        sig = inspect.signature(f)

        @wraps(f)
        def d_f(*args, **kwargs):

            # Get kwargs and args
            bound_args = sig.bind(*args, **kwargs)
            bound_args.apply_defaults()
            wrapped_args = dict(bound_args.arguments)

            # Check if using cache is needed
            logger: Optional[Logger] = wrapped_args.get(logger_kwarg_key, None)

            start = timeit.default_timer()

            result = f(*args, **kwargs)

            stop = timeit.default_timer()

            if isinstance(logger, Logger):
                logger.debug(msg="{}, Execution time: {}".format(f.__name__, stop - start))

            return result

        return d_f

    return log_time_usage_inner
