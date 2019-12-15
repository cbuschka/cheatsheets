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
with open('output.txt', 'w') as file:
  file.write('Hi there!')
```

=> calls __enter__() of entering and __exit__() on leaving the context
