## type inference

`var`で型推論してくれる。
右辺の型が明確であれば、あえて明示する必要はない。
以下のようなコードは冗長。

```csharp
List<int> list = new List<int> { 1, 84, 95, 95, 40, 6 }
```

↓型推論の是非
https://ufcpp.net/study/csharp/sp3_var.html

