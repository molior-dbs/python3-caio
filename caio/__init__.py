from caio.version import *
import platform

from .abstract import AbstractContext, AbstractOperation

from . import python_aio
from . import python_aio_asyncio


try:
    from . import linux_aio
    from . import linux_aio_asyncio
except ImportError:
    linux_aio = None            # type: ignore
    linux_aio_asyncio = None    # type: ignore

try:
    from . import thread_aio
    from . import thread_aio_asyncio
except ImportError:
    thread_aio = None           # type: ignore
    thread_aio_asyncio = None   # type: ignore


prefered = list(filter(None, [linux_aio, thread_aio, python_aio]))[0]


Context = prefered.Context      # type: ignore
Operation = prefered.Operation  # type: ignore


__all__ = (
    "Context",
    "Operation",
    "AsyncioContext",
    "AbstractContext",
    "AbstractOperation",
    "__version__",
    "__author__",
)
