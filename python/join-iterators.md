## join-iterators

```
>>> [n for n in range(3)]
[0, 1, 2]
>>> [n for n in range(3,6)]
[3, 4, 5]
>>> [n for n in itertools.chain(range(3), range(3,6))]
[0, 1, 2, 3, 4, 5]
```
