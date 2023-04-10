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


va = A(a=2, b='b', c=1.0, d=(2,4))  # Ok
assert va.a == 2
va.a = 5
assert va.a == 5
va.a = '5'  # raises AttributeTypeError (a should be int)
va = A(c=1.0)  # Ok, using default values
va = A(c='c')  # raises AttributeTypeError (c should be float)
va = (b='c')  # raises AttributeRequiredError (a is missing)

```
