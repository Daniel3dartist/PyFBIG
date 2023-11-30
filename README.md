# PyFBIG (Python - Fake Brazilian ID Generator)
[![PyPI version](https://badge.fury.io/py/pyFBIG.svg)](https://badge.fury.io/py/pyFBIG) ![python tests](https://github.com/Daniel3dartist/PyFBIG/actions/workflows/ci.yml/badge.svg) [![codecov](https://codecov.io/gh/Daniel3dartist/PyFBIG/graph/badge.svg?token=E3NHE9ATHM)](https://codecov.io/gh/Daniel3dartist/PyFBIG) ![GitHub License](https://img.shields.io/github/license/Daniel3dartist/PyFBIG)
 PyFBIG is a package that generates fake data for you. Do you need to test something with Brazilian identification such as RG, CPF, Driver's License, CRM, COREN, etc.? PyFBIG is for you.

# How to use
### Install
```
pip install pyFBIG
```
### Examples:
```
from pyFBIG import FakeID

fake = FakeID()

cpf = fake.cpf()
print(cpf)
# 163.710.406-50

rg = fake.rg()
print(rg)
# 86103044

rg = fake.rg(is_complete=True)
print(rg)
# {
#  'name':'Lucimara Santos Lemos',
#  'gender': 'F',
#  'birth': {
#    'day': '21/10/1954',
#    'city':'Pocos de Caldas',
#    'state':'MG'
#     },
#  'org': {
#     'name': 'PC',
#     'state': 'MG',
#         },
#  'affiliation': {
#    'father': 'Ronaldo Castro Lemos', 
#    'mother': 'Sophia Santos Lemos'
#    },
#  'rg': MG88103067
# }

crm = fake.crm()
print(crm)
# 40635352-0/BR
```

# About the project
It is still in the prototyping and development phase. Feel free to contribute and suggest improvements.
