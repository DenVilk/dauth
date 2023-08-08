from typing import Any, Callable, Optional, Union
from fastapi import HTTPException, Depends
from databases import Database
from redis import Redis

DENY = HTTPException(status_code=403, detail="Permission denied.")


def Policy(
    subject_callback: Callable, 
    resource_type: str, 
    method: str, 
    check_callback: Callable,
    database: Optional[Database] = None,
    cache: Optional[Redis] = None
):
    '''Function that give opportunity to work with Fastapi Depends'''
    def _check(
        subject: Any = Depends(subject_callback), 
        item_id: Union[str, int] = "*",
    ) -> Any:
        '''Function that checks policy'''
        check_callback(subject, resource_type, item_id, method, database, cache)
        return subject

    return _check

def AnyUser(*args, **kwargs):
    pass