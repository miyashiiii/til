## functools.reduce

https://docs.python.org/ja/3/library/functools.html#functools.reduce

```python
functools.reduce(function, iterable[, initializer])
```

`2引数のfunctionをiterableの要素に対して左から右に累積的に適用し、iterableを単一の値に集約します。`
```python
from functools import python
>>> reduce(lambda x, y: x + y, [1, 2, 3, 4, 5])  # ((((1+2)+3)+4)+5)
15
```

