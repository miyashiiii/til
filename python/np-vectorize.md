## np.vectorize()
https://docs.scipy.org/doc/numpy/reference/generated/numpy.vectorize.html

```python
>>> def myfunc(a, b):
...     "Return a-b if a>b, otherwise return a+b"
...     if a > b:
...         return a - b
...     else:
...         return a + b
>>> vfunc = np.vectorize(myfunc)
>>> vfunc([1, 2, 3, 4], 2)
array([3, 4, 1, 2])
```

引数に関数を渡すと、引数の配列の各要素に対して渡された関数(myfunc)の処理を行うラッパー関数を作る。
内部的にはfor文を回しているだけらしいので、見た目はスッキリするがパフォーマンスはfor文と変わらないらしい.

> The vectorize function is provided primarily for convenience, not for performance. The implementation is essentially a for loop.



ちなみに、配列の各要素に対して処理を行う関数を[universal function (ufunc)](https://docs.scipy.org/doc/numpy/reference/ufuncs.html)と呼ぶらしい
