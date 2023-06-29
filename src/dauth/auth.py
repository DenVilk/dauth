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
    database_callback: Optional[Callable] = None,
    cache_callback: Optional[Callable] = None
):
    '''Function that give opportunity to work with Fastapi Depends'''
    def _check(
        subject: Any = Depends(subject_callback), 
        item_id: Union[str, int] = "*",
        db: Optional[Database] = Depends(database_callback),
        cache: Optional[Redis] = Depends(cache_callback)
    ) -> Any:
        '''Function that checks policy'''
        check_callback(subject, resource_type, item_id, method, db, cache)
        return subject

    return _check
