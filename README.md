# DAuth 

Python FastAPI ABAC Realization.

---
## Getting started
Requirements:

- `redis` - for cache support
- `databases` - for database support

Install:

```bash
pip install dauth
```

After installing import main functions by 
```python
from dauth import auth
```

Library represents function 
```python
def Policy(
    subject_call: Callable, 
    resource_type: Any, 
    method: str, 
    check_callback: Callable,
    database_callback: Union[Callable, None] = None,
    cache_callback: Union[Callable, None] = None
)
```

- `subject_callback` - Is function that library put in FastAPI `Depends `. Usually function returns user which tries to work with `resource`
- `resource_type` - Is `str` which on which User tries to get access
- `method` - Is API method by which working endpoint
- `check_callback` - Is function that realize Policy's check. Function take arguments:
    ```python
    check_callback(subject, resource_type, item_id, method, db, cache)
    ```
- - `subject` is result of `Depends(subject_callback)`
- - `resource_type` is argument of `Policy()`
- - `item_id` __(by default '*')__ is providing by FastAPI decorator `@app.get(/test/{item_id})`
- - `method` is argument of `Policy()`
- - `db` is database connection, result of `Depends(database_callback)`
- - `cache` is redis connection, result of `Depends(cache_callback)`
- `database_callback` - Is a function for getting database connecion
- `cache_callback` - Is a function for getting Redis connection
---
## Examples
Simple usage
```python
from fastapi import FastAPI, Depends
from dauth import auth

app = FastAPI()

def is_admin(subject, resource_type, item_id, method, db, cache):
    if 'admin' not in subject.scopes:
        raise auth.DENY

@app.get("/test")
# function get_user_auth returns User's object
def test(
    user = Depends(auth.Policy(
        get_user_auth, 
        'test', 
        'get', 
        is_admin
    ))
):
    return {"message":"Good"}


@app.get("/test_with_db")
# function get_database returns Databases connection
def test_db(
    user = Depends(auth.Policy(
        get_user_auth, 
        'test', 
        'get', 
        is_admin, 
        database_callback=get_database
    ))
):
    return {"message":"Good"}

@app.get("/test_with_cache")
# function get_cache returns Redis connection
def test_cache(
    user = Depends(auth.Policy(
        get_user_auth, 
        'test', 
        'get', 
        is_admin, 
        cache_callback=get_cache
    ))
):
    return {"message":"Good"}
```

---
Developed by [DenVilk](https://github.com/denvilk)
