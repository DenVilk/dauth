# DAuth 

Python FastAPI ABAC Realization.

---
## Getting started
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
    check_callback: Callable
)
```

- `subject_callback` - Is function that library put in FastAPI `Depends `. Usually function returns user which tries to work with `resource`
- `resource_type` - Is `str` which on which User tries to get access
- `method` - Is API method by which working endpoint
- `check_callback` - Is function that realize Policy's check. Function take arguments:
    ```python
    check_callback(subject, resource_type, item_id, method)
    ```
- - `subject` is result of `Depends(subject_callback)`
- - `resource_type` is argument of `Policy()`
- - `item_id` __(by default '*')__ is providing by FastAPI decorator `@app.get(/test/{item_id})`
- - `method` is argument of `Policy()`

---
## Examples
Simple usage
```python
from fastapi import Depends
from dauth import auth

app = FastAPI()

def is_admin(subject, resource_type, item_id, method):
    if 'admin' not in subject.scopes:
        raise auth.DENY

@app.get("/test")
# function get_user_auth returns User's object
def test(user = Depends(auth.Policy(get_user_auth, 'test', 'get', is_admin))):
    return {"message":"Good"}
```

---
Developed by [DenVilk](https://github.com/denvilk)