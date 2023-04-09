try:
    import fastapi
except ImportError as e:
    print("FastAPI should be installed.")
    raise e

from . import auth

__all__ = [
    'auth'
]
