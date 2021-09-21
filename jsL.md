# 匿名函数

## 将匿名函数赋值给其他,可以复制给事件或者变量等

```
const fun1=function(a){
    return a*a;
}

```



## 自调用（定义调用合在一起）

```
(function (){
    console.log("匿名函数1");
}())
```



## 自调用（加各种符号: !,+,-,~,void）

```
!function(){
    console.log("匿名函数2");
}()
```



