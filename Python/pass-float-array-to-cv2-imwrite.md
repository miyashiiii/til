## pass-float-array-to-cv2-imwrite

cv2.imwrite()にfloatのarrayを渡すと、intに丸められる。

```python
>>> a = np.array([[[0.5,0.5,0.5]]])
>>> cv2.imwrite("a.jpg",a)
True
>>> cv2.imread("a.jpg")
array([[[0, 0, 0]]], dtype=uint8)
```

```python
>>> a = np.array([[[0.51,0.51,0.51]]])
>>> cv2.imwrite("a.jpg",a)
True
>>> cv2.imread("a.jpg")
array([[[1, 1, 1]]], dtype=uint8)
```


