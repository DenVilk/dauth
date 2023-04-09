from typing import Any, Callable, Union
from fastapi import HTTPException, Depends

DENY = HTTPException(status_code=403, detail="Permission denied.")


def Policy(
    subject_callback: Callable, 
    resource_type: str, 
    method: str, 
    check_callback: Callable
):
    '''Function that give opportunity to work with Fastapi Depends'''
    def _check(
        subject: Any = Depends(subject_callback), 
        item_id: Union[str, int]="*"
    ):
        '''Function that checks policy'''
        check_callback(subject, resource_type, item_id, method)
        return subject

    return _check