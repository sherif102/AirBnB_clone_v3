#!/usr/bin/python3
import hashlib

she = hashlib.md5()
he = hashlib.md5()
she.update(b"sheriff081")
he.update(b"sheriff081")
print(she.digest())
print(he.digest())