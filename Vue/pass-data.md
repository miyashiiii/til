## pass-data

### 親コンポーネントから子のdataを変更

```vue
<template>
  <Child ref="refChild" />
</template>
<script>
  changeData(data) {
    var child = this.$refs.refChild
    child.data = data
  },
</script>
```

### 子コンポーネントから親のメソッドを呼ぶ

#### templateから

```vue
<v-btn @click="$emit('changeData')" >Change Data</v-btn>
```

#### メソッドから

```js
changeData(data) {
  this.$emit('changeData', data) 
}
```

