## 1channel-to-3channel

```python
def one_channel_to_three_channel(one_channel):
    return np.stack([one_channel, one_channel, one_channel], axis=2)
```
or


```python
def one_channel_to_three_channel(one_channel):
    return cv2.merge([[one_channel, one_channel, one_channel])
```
