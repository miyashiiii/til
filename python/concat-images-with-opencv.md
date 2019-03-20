## concat images with opencv

### 縦に結合
```python
im_v = cv2.vconcat([im1, im2])
```

### 横に結合
```python
im_h = cv2.hconcat([im1, im2])
```

### リストで渡したままの形に結合する（正方行列にのみ対応）

```python
def concat_tile(im_list_2d):
    im_list_v = [hconcat_resize_min(im_list_h) for im_list_h in im_list_2d]
    return vconcat_resize_min(im_list_v)

im_tile = concat_tile([
                     [im1, im2, im3],
                     [im4, im5, im6],
                     [im7, im8, im9]
                 ])
```

参考：
https://note.nkmk.me/python-opencv-hconcat-vconcat-np-tile/

