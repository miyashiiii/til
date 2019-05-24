## loop-with-index


統合言語クエリ（LINQ）のSelectメソッドを使って、インデックス付きでループを回せる。

```csharp
string[] fruits = {"apple", "banana", "mango", "orange", "passionfruit", "grape"}
var query = fruits.Select((fruit, index) =>
                      new { index, str = fruit.Substring(0, index) });

foreach (var obj in query)
{
    Console.WriteLine("{0}", obj);
}
```

https://docs.microsoft.com/ja-jp/dotnet/api/system.linq.enumerable.select?view=netframework-4.8
