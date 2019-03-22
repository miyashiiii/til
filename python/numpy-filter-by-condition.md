## numpy-filter-by-condition


```python
>>> X = np.array([51, 55, 14, 19, 0, 4])
array([51 55 14 19 0 4])
```

### boolean indexを取得

```python
>>> X > 15
array([True, True, False, True, False, False])
```

### 条件に合致する要素をカウント

```python
>>> np.sum(X > 15)
array([True, True, False, True, False, False])
```

### 条件に合致する要素を取得

```python
>>> X[X > 15]
array([51, 55, 19])
```

### 条件に合致する要素のindexを取得

```python
>>> np.where(X > 15)
array([0, 1, 3])
```

