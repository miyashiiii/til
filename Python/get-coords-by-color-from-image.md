## get-coords-by-color-from-image.md

色情報が[128, 0, 0]の座標を取得

```python
indices = np.where(np.all(img == [128, 0, 0], axis=-1))
```
