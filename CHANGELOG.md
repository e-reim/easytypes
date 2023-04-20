# easytypes change log

## 0.5.1
Initial beta version
##0.5.2
Seems to be fully functional
##0.5.3
A small fix that affects a potential bug that happens if a base type has checks on, and a derived type does not. `__setattr__` and `__delattr` are now always present, not just if needed.
##0.5.4
Fixed a typo in README.md
##0.5.5
\_\_debug\_\_ off now disables all the checks by default. Though you still switch them on
