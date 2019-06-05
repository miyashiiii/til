## generics

型に依存しない汎用処理を記述できる
```CSharp
// Declare the generic class.
public class GenericList<T>
{
    public void Add(T input) { }
}
class TestGenericList
{
    private class ExampleClass { }
    static void Main()
    {
        // Declare a list of type int.
        GenericList<int> list1 = new GenericList<int>();
        list1.Add(1);

        // Declare a list of type string.
        GenericList<string> list2 = new GenericList<string>();
        list2.Add("");

        // Declare a list of type ExampleClass.
        GenericList<ExampleClass> list3 = new GenericList<ExampleClass>();
        list3.Add(new ExampleClass());
    }
}
```

https://docs.microsoft.com/ja-jp/dotnet/csharp/programming-guide/generics/

また、指定する型に制約をつけられる

https://docs.microsoft.com/ja-jp/dotnet/csharp/programming-guide/generics/constraints-on-type-parameters
