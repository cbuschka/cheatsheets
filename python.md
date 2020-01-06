### main block

```python
if __name__ == '__main__':
    main()
```

### list comprehension

```python
new_list = [expression(i) for i in old_list if filter(i)]
```

### iterate over map
```python
for key, value in a_dict.items():
  print(key, '->', value)
```

or

```python
for item in a_dict.items():
  print(key, '->', value)
```

### templates

```python
props = { "user": "conni", "age": 42 }
text = "the user {conni} is {age}".format(**props)
```

### with context

```python
with open('output.txt', 'w') as file and with open('output.txt', 'w') as file2:
  file.write('Hi there!')
  file2.write('Here I am.')
```

=> calls ```__enter__()``` of entering and ```__exit__()``` on leaving the context

### managed context
```python
class MyResourceManager:
  def __enter__(self):
    return resource

  def __exit__(self, type, value, traceback):
    pass

def get_rsc():
  return MyResourceManager()

with get_rsc() as r:
  r.foo()
```

### mocking

```python
from unittest.mock import MagicMock

thing = ProductionClass()
thing.method = MagicMock(return_value=3)
```
### mocking functions from imported modules
[stackoverflow answer](https://stackoverflow.com/questions/16134281/python-mocking-a-function-from-an-imported-module)

### parse json

```python
import json

with open('file.json') as f:
  data = json.load(f)
```

### rest client
```python
import requests

resp = requests.get('https://todolist.example.com/tasks/')
if resp.status_code != 200:
  ...
for todo_item in resp.json():
  ...
```

### decorator
```python
@decorator
def wrapped(f, x):
  def wrappedf(f, x):
    return f(x)
  return wrappedf

@wrapped
def myfunc(x):
  print(x)
```

### dynamic class
```python
MyType = ("MyType", (object), {x:1})
my = MyType()
print my.x
```

### slicing
```python
as = [1, 2, 3, 4, 5, 6, 7, 8 , 9]
bs = as[1:6:2]
```
