## plualize

第一引数に応じて、第二引数の文字列を単数系/複数形に変換する。
```ruby
>> helper.pluralize(0, "error")
=> "0 errors"
>> helper.pluralize(1, "error")
=> "1 error"
>> helper.pluralize(5, "error")
=> "5 errors"
```
