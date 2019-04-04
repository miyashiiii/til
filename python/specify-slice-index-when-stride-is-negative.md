## specify-slice-index-when-stride-is-negative.md

ステップに負の数を指定すると、indexの指定が逆順になる。

```python
a[end:start] # if stride is negative
```

```python
>>> a[1:7:2]
[2, 4, 6]
>>> a[1:7:-2]
[]
>>> a[7:1:-2]
[8, 6, 4]
```
