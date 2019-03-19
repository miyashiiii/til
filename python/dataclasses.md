## dataclasses

python3.7で追加された新機能。

`__init__()` や `__repr__()` のような特殊メソッドを勝手に生成する

例：

```
@dataclass
class InventoryItem:
    '''Class for keeping track of an item in inventory.'''
    name: str
    unit_price: float
    quantity_on_hand: int = 0

    def total_cost(self) -> float:
        return self.unit_price * self.quantity_on_hand
```

https://docs.python.org/ja/3/library/dataclasses.html
