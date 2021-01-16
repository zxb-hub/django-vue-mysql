### 常用浏览器
- webkit内核（v8内核）
   + 谷歌Chrome
   + Safari
   + Opera >=V14
   + 国产浏览器
   + 手机浏览器
   + ...
- Gecko
   + 火狐Firefox
- Presto
   + Opera <V14
- Trident
   + IE
   + IE EDGE开始采用双内核（其中包含Chrome迷你）


谷歌浏览器的控制台（F12/fn+F12）
- Elements：查看结构样式，可以修改这些内容
- Console：查看输出结果和调试信息，是JS调试的利器
- Sources:查看项目源码
- Network：查看当前网站所有资源请求信息（包括和服务器传输的http报文信息）、加载时间（根据加载时间进行项目优化）
- Application:查看当前网站的数据存储和资源文件（可以盗图）


书
- JavaScript高级程序教程（第三版）
- es6.runyifeng.com
- 你不知道的JavaScript
- javaScript权威指南


### js作为客户端语言
> 按照js相关语法，去操作页面中的元素，有时还要操作浏览器里面的一些功能
- ECMCcript3/5/6...：js语法规范（变量、数据类型、操作语句等等）
- DOM（ document object model ）：文档对象模型，提供一些js的属性和方法，用来操作页面中的DOM元素
- BOM（browser object model）：浏览器对象模型，提供一些js的属性和方法，用来操作浏览器的

### js中的变量 Variable
> 变量：可变的量，在编程语言当中，变量就是一个名字，用来存储和代表不同值的东西
```
    //ES3 老语法
    var a = 12;
    console.log(a);//=>输出的是a代表的值12
    
    //ES6
    let b = 100;
    

    const c = 1000;
    c = 200;//=>报错：const创建的变量，存储的值不能被修改（可以理解为常量）

    //创建函数也相当于在创建变量
    function fn（）{}

    //创建类也相当于创建变量
    class A{}
    //ES6的模块导入也可以创建变量
    import b from ./b.js;
    //Symbol 创建唯一值
    let n = symbol(100);
    let m = symbol(100);
    n == m;//返回false

```

### js命名规则
- 严格区分大小写
- 使用数字、字母、下划线、$，数字不能作为开头（一般用JQ获取的用$作为开头，_一般公共变量都是以_作为开头）
- 驼峰命名法:首字母小写，其余每个有意义的单词首字母大写（命名尽可能语义化明显，使用英文单词）（常用缩写：add/insert/create/new(新增)、update(修改)、delete/del/rm/remove(删除)、sel/select/query/get(查询)、info（信息）... ）

### js常用数据类型
- 基本数据类型
   + 数字 number 
       常规数字和NaN
   + 字符串string
       所有用单引号和双引号、反引号包起来的都叫字符串
   + 布尔 bollean
       true/false
   + 空对象指针null
   + 未定义undefined
- 引用数据类型
   + 对象数据类型object
      + {} 普通对象
      + [] 数组对象
      + /^$/ 正则对象
      + Math数学函数对象
      + 日期对象
      + ... 
   + 函数数据类型function


## number数字类型
> 包含数字、NaN

### NaN
> Not a Number:不是一个数，但是属于数字类型
      NaN和任何值（包括自己）都不相等：NaN!=NaN


```
// console.log([val]):在控制台输出内容
console.log('hello world');

```


### isNaN
> 检测一个值是否为非有效数字，如果不是有效数字返回TRUE，反之是有效数字返回FALSE


在使用isNaN进行检测的时候，首先会验证检测的值是否为数字类型，如果不是，先基于Number（）这个方法，把值转换为数字类型，然后再检测
```
console.log(isNaN('10'));//=>FLASE

```


## toString()
> 转化字符串
```
console.log([12,3].toString());//=>'12,3'
```

### 把其它数据类型转化数字类型
- Number([val])
- parseInt/praseFloat([val],[进制]):也是转化为数字的方法，对于字符串来说，他是从左到右依次查找有效数字字符，直到遇到非有效数字字符，停止查找（不管后面是否还有有效数字，都不在查找），把找到的值 
- == 进行比较时，可能要出现把其他类型转化为数字（'10'==10  =>true）




#### 匿名函数
### 匿名函数之匿名函数表达式：
> 把一个匿名函数本身作为值赋值给其他东西，这种函数一般不是手动触发执行，而是靠其他程序驱动触发执行（例如:触发某种事件的时候把它执行等 ）
```
document.body.onclick = funtion(){} //当body中的onclick被触发时，执行函数
setTimeout(function(){},1000);     //设置定时器，一秒钟后触发function()
```
### 匿名函数之自执行函数:
>创建一个匿名函数，紧接着就把当前函数加小括号执行
```
(function(n){
     //n=>100
})(100);
```



### 传统基于操作系统DOM的方法实现业务需求
- 想操作谁就先获取谁
- 给某元素绑定某事件
- 在事件触发的时候修改元素样式

```
//document.getElementById([]):在整个文档中，通过元素的Id获取到当前这个元素对象

let functionName = document.getElementById('')；


//元素对象.onxxx = function(){}:事件绑定，xxx为时间类型（click（当点击时）、mouseover（鼠标滑过的时候）、mousedown（鼠标按下的时候）、keydown（键盘按下的时候）....）

functionName.onclick = function(){
   // 元素对象.style.xxx=xxx：为修改元素样式的某个值(操作的是元素行内样式，所以如果没有写在行内，js中基于.style.xxx无法获取样式)
   detail.style.display = 'block';
}
```