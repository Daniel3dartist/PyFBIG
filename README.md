# PyFBIG
Python - Fake Brazilian ID Generator is a package that generates fake data for you. Do you need to test something with Brazilian identification such as RG, CPF, Driver's License, CRM, COREN, etc.? PyFBIG is for you.

# How to use
### Exemple:

```
pip install pyFNIG
```

```
from pyFBIG import FakeID

fake = FakeID()

cpf = fake.cpf()
print(cpf)
# 163.710.406-50

rg = fake.rg()
print(rg)
# MG86103044
```

# About the project
It is still in the prototyping and development phase. Feel free to contribute and suggest improvements.