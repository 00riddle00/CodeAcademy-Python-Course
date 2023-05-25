2 **4
# 16

**{"name": "John"}
# SyntaxError: invalid syntax

dict(name="John")
# {'name': 'John'}

dict({"name": "John"})
# {'name': 'John'}

dict(**{"name": "John"})
# {'name': 'John'}

dict([("foo", 100), ("bar", 200)])
# {'foo': 100, 'bar': 200}

dict({("foo", 100), ("bar", 200)})
# {'foo': 100, 'bar': 200}

dict(foo=100, bar=200)
# {'foo': 100, 'bar': 200}

dict({"one": 1, "three": 3}, two=2)
# {'one': 1, 'three': 3, 'two': 2}
