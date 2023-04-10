# easytypes
Easy typed structures for Python with optional field checking and runtime type checking. Based on class decorators and ``typeguard`` package for type checking.

```
from easytypes import safe_type, Required

@safe_type  # You cannot: add new attrs; not set (or delete) the required attrs; assign wrong types
class A:
    a: int  # Type checking, not required, no default value
    b: str = '5'  # Type checking, not required, the default value is '5'
    c: float = Required()  # Type checking, required, no default value
    d: Tuple[int, int] = (2, 3)  # Type checking, not required, the default value is (2, 3)
```
