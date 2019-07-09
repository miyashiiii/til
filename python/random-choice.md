## random choice

任意のリストから指定した数の要素をランダムに選択するメソッド。
意外と調べたことなかった、多分今まで必要なときは `l = l[random.randint(len(l))]` とか書いてた

```
import random

fruits = ["apple", "banana", "orange", "grape"]

# 一つ選択
print(random.choice(fruits) # "banana"
# 複数選択（重複可）
Print(random.choices(fruits, k=3) # ['orange', 'orange', 'banana']
# 複数選択（重複不可）
Print(random.sample(fruits, k=3) # ['apple', 'orange', 'grape']
```
