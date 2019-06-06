## method-call-dynamically

Swicherクラスのインスタンスswitcherから、methodNameで指定されたメソッドを呼ぶ

```CSharp
swicher.GetType().GetMethod(methodName).invoke(swicher, null);
```

invokeの第一引数はインスタンス(staticメソッドならnull)、第二引数にはパラメータをObject[]の形で渡す
