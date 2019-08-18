---
title: Test Markdown
subtitle: Each post also has a subtitle
tags:
  - Markdown
abbrlink: 66cfa612
date: 2017-02-22 10:20:26
---

列举一些常用的 `markdown` 语法, 作为测试以及备忘。

<!-- more -->

You can write regular [markdown](http://markdowntutorial.com/) here and Jekyll will automatically convert it to a nice webpage.  I strongly encourage you to [take 5 minutes to learn how to write in markdown](http://markdowntutorial.com/) - it'll teach you how to transform regular text into bold/italics/headings/tables/etc.

Markdown 语法手册

-----

### 1. 分级标题  
使用 === 表示一级标题，使用 --- 表示二级标题
你也可以选择在行首加井号表示不同级别的标题 (H1-H6)，例如：# H1, ## H2, ### H3
一般来说都是使用 #号 来使用, 注意 #号 需要顶格写
示例：

```
这是一个一级标题
===
这是一个二级标题
----
### 这是一个三级标题
```

---

### 2. 斜体和粗体
使用 `* `和 `**` 表示斜体和粗体

示例：

> 这是\*斜体\* 这是\*\*粗体\*\*    
 这是*斜体*   这是**粗体**

 这是*斜体*   这是**粗体**

-----

### 3. 链接
使用 \[描述](链接地址) 为文字增加链接

示例：

> 这是去往\[本人博客\](http://doudou0o.github.com/blog) 的链接  
  这是去往 [本人博客](http://doudou0o.github.com/blog) 的链接
  
-----

### 4. 插入图像
使用 \!\[描述](图片链接) 插入图像(好像插入时保持原图片大小)
*和链接比较类似,唯一的区别就是前面有一个!*
在Hexo 中本地图片使用 \!\[本地图片]({{ site.url }}/img/a.jpg)

示例：
在线图片
\!\[图片\](https://assets-cdn.github.com/images/modules/logos_page/Octocat.png)
![图片](https://assets-cdn.github.com/images/modules/logos_page/Octocat.png)

本地图片
\!\[本地图片](./{{ title }}/start.jpg)
\!\[本地图片](./{{ abbrlink }}/start.jpg)
![本地图片](./{{ abbrlink }}/start.jpg)

大小控制图片
```
<img src="./{{ abbrlink }}/start.jpg" alt="logo" width="50%" height="50%" />
```

<img src="./{{ abbrlink }}/start.jpg" alt="logo" width="50%" height="50%" />


-----

### 5. 文字引用
使用 > 表示文字引用
同 #号 一样需要定格写否则没有效果而且上下需要有空格

示例：

> 你好我是引用文档

-----

### 6. 无序列表
使用 *，+，- 表示无序列表
都是需要顶格写且前后得有空行

示例：

+ 无序列表项 一
+ 无序列表项 二
+ 无序列表项 三

-----

### 7. 有序列表
使用数字和点表示有序列表。例: 1. xxxx 注意要有一个空格!

示例：
1. 有序列表项 一
2. 有序列表项 二
3. 有序列表项 三

-----

### 8. 行内代码块
使用 \`代码\` 表示行内代码块
好像在行内代码块中不会高亮

示例：
此行内有一个行内代码块`java vs cpp`

-----

### 9. 代码块
代码块使用    

>\`\`\` python(或者~~~)    
balabala    
\`\`\`    

包裹起来而且可以加上所用的语言,也可以不加    
另外由于 Pygments 或 Rouge 的使用,可以用    

 

包裹更加好看(不要加行号! 不然会超级难看)    

~~~ruby
def show
  @widget = Widget(params[:id])
  respond_to do |format|
    format.html # show.html.erb
    format.json { render json: @widget }
  end
end
~~~    

-----

### 10. 表格

| Number | Next number | Previous number |
| :------ |:--- | :--- |
| Five | Six | Four |
| Ten | Eleven | Nine |
| Seven | Eight | Six |
| Two | Three | One |

-----

### 11. Todo 列表

使用带有 [ ] 或 [x] （未完成或已完成）项的列表语法撰写一个待办事宜列表
并且支持子列表嵌套以及混用Markdown语法，示例：

    - [ ] **买菜**
        - [ ] 小排
        - [x] 鸡肉
        - [ ] 番茄
        - [x] 辣椒
            - [x] 小辣椒
            - [x] 红辣椒

        
生成 这样一个 Todo 列表：
        
- [ ] **买菜**
	- [ ] 小排
	- [x] 鸡肉
	- [ ] 番茄
	- [x] 辣椒
		- [x] 小辣椒
		- [x] 红辣椒

-----

### 12. 注脚

使用 \[^keyword\] 表示注脚

这是一个注脚[^footnote]的样例


-----

### 13. 页内链接(hexo下暂时无效没找到正确的姿势)

```
先在某处设定一个锚点`<a id="jump" name="jump">锚点</a>`类似这样
然后使用 `\[结论\](\#jump) `这样的方法就可以在页内跳转
或者在标题后面跟上ID也可以同样跳转`### 标题 {#ID}`

示例:    
[示例1](#jump)    
[示例2](#ID2)    
```

        
[^footnote]: 这是一个 *注脚*
