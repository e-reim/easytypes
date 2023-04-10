# easytypes
Easy typed structures for Python with optional field checking and runtime type checking. Based on class decorators and ``typeguard`` package for type checking.

## How to define a simple data class
```
from easytypes import safe_type, Required

@safe_type  # You cannot: add new attrs; not set (or delete) the required attrs; assign wrong types
class A:
    a: int  # Type checking, not required, no default value
    b: str = '5'  # Type checking, not required, the default value is '5'
    c: float = Required()  # Type checking, required, no default value
    d: Tuple[int, int] = Required(2, 3)  # Type checking, required, the default value is (2, 3)
```
## And how does that class work
```
>>> va = A(a=2, b='b', c=1.0, d=(2,4))  # Ok
>>> assert va.a == 2
>>> va.a = 5
>>> assert va.a == 5
>>> va = A(c=1.0)  # Ok, using default values
>>> va = A(c=1.0, q=2)  # raises AttributeNotAllowed 
>>> va.q = 0  # raises AttributeNotAllowed
>>> va.a = '5'  # raises AttributeTypeError (a should be int)
>>> va = A(c='c')  # raises AttributeTypeError (c should be float)
>>> va = (b='c')  # raises AttributeRequired (a is missing)


```
