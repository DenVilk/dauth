from typing import Any, Callable, Union, Annotated
from fastapi import HTTPException, Depends
from databases import Database
from redis import Redis

DENY = HTTPException(status_code=403, detail="Permission denied.")


def Policy(
    subject_callback: Callable, 
    resource_type: str, 
    method: str, 
    check_callback: Callable,
    database_callback: Union[Callable, None] = None,
    cache_callback: Union[Callable, None] = None
):
    '''Function that give opportunity to work with Fastapi Depends'''
    def _check(
        subject: Any = Depends(subject_callback), 
        item_id: Union[str, int] = "*",
        db: Database = Depends(database_callback),
        cache: Redis = Depends(cache_callback)
    ) -> Any:
        '''Function that checks policy'''
        check_callback(subject, resource_type, item_id, method, db, cache)
        return subject

    return _check
