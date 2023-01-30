
> 编译原理实践课程

# 添加功能

可以定义无数个 `struct`，以及可以声明不同类型的 `struct` 变量。
# 原文
略微写一下 `README` 吧，详细的有空再写。

构造一个编译器是一个非常繁琐的过程，不过当你亲自构造一个词素、文法、并构造其独特的语义之后，你就会明白其中奥秘所在。

## 开门见山（词法分析和语法分析）

我们想要一个新的定义，首先考虑是否添加了新的词素，然后最重要的是怎么构造其文法。文法可以理解为人的骨架，这直接影响到你的程序的通用性。

对于 `struct` ​ 来说，我们需要添加一个新的词素 `structID​`，因为我们需要使用它声明 $struct$ 类型的变量。

### struct定义语句

对于 `struct定义` 来说，其文法是

```
<struct定义语句> ::= <struct> <structID> <{> <struct变量定义> <}> <;>
```

其中除 `<struct变量定义>` 外都是终结符，我们要为他写新的产生式

```
<struct变量定义> ::= <数据类型> <标识符> <;> <struct变量定义>
<struct变量定义> ::= <空>
```

典型的无限次重复的生成子句，学过编译的应该都懂

通过上面的文法，我们就可以对以下 `C​` 语言源程序分析

```
struct student{
    char* name; // 姓名
    char* college;
    char* major;
    int num; // 学号
    int age; // 年龄
    float score;
};
```

### struct声明语句

$struct$ 声明语句的作用是解析 `student Su={"yi fan","GXU","CS",5,21,145.0};` 

```
<struct声明语句> ::= <structID> <标识符> <=> <{> <struct常量> <}> <;>
```

`structID`​ 我们前面介绍过，是一种新的数据类型

这里的重点在于 `struct​` 常量

```
< struct常量> ::= <常量> <struct分割符号> <struct常量>
< struct常量> ::= <空>
<struct分割符号> ::= <,>
<struct分割符号> ::= <空>
```

同样的无限次重复的子句

这样的话，词法分析和语法分析的工作基本上就完成了。

## 语义分析（为语法赋予灵魂）

在这里要处理的问题就是：如何将 `struct` ​ 定义语句和 `struct` 声明语句联系起来呢？

在全局变量这里建立一个 `hashtable​` 表，其 `key` 的值是 `struct` 的名字，其 `value` 是一个列表，这里列表中记录了这个 `struct​` 中定义的**变量**数量。（我有点偷懒，在全局定义了一个列表，默认一个 `struct​` ... 欢迎大家 `pull request`)

<img src="http://picture-suyifan.oss-cn-shenzhen.aliyuncs.com/img/image-20210705143233863.png" alt="image-20210705143233863" style="zoom: 50%;" />

第一个 `goon(1)` 去匹配数据类型，第二个 `goon(1)` 去匹配标识符（ `struct​` 内部变量的标识符），这里 `temp[-1]` 就是表示符的词素，类似于这样子 `('ID', 'Sunum', 70)`。加入到预先定义的全局变量中。

**这样我们就可以在 `struct​` 声明的地方使用了**

<img src="http://picture-suyifan.oss-cn-shenzhen.aliyuncs.com/img/image-20210705143710226.png" alt="image-20210705143710226" style="zoom: 50%;" />

第一个 `goon(1)` 匹配常量，这样 `temp[-1]` 里面就会存储该常量的词素，如果这个词素是字符串类型的，我们就生成一个**常量**的四元式（汇编输出字符串要在数据段定义），四元式的第四个就去上面定义的表中找，**这样就做到了值和标识符的一一对应**。

# 汇编生成

1. 字符串的四元式怎么办

![image-20210705144140129](http://picture-suyifan.oss-cn-shenzhen.aliyuncs.com/img/image-20210705144140129.png)

在数据段定义部分，就检索一遍四元式：

这里的 `four[i][3]` 是这个四元式的最后一项，也就是标识符号，后面输出的时候会用到，`four[i][1]` 就是字符串的值。

结果类似以下汇编语句：`GG DB '801 yyds!',13,10,'$'`

## 测试

### 源程序

```
#include <stdio.h>
struct student{
    char* name; // 姓名
    char* college; // 学校
    char* major; // 专业
    int num; // 学号
    int age; // 年龄
    float score;
};
int main(){
    int i = 0;
    int num_140=0;
    float sum=0;
    student Su={"yi fan","GXU","CS",5,21,145.0};
    if(Su.score < 140) {
        flag = -1;
    }
    else {
        flag=1;
    }
    printf("%s\n",Su.name);
    printf("%s\n",Su.college);
    printf("%s\n",Su.major);
    printf("%d\n",Su.num);
    printf("%d\n",Su.age);
    printf("%d\n",Su.score);
    printf("%d\n",flag);
}
```

### 汇编程序

```
include io.inc
.model small
.stack
.data
        DW 100 DUP(0)
Suname	DB 'yi fan',13,10,'$'
Sucollege	DB 'GXU',13,10,'$'
Sumajor	DB 'CS',13,10,'$'
.code
.startup
        MOV AX,0
        MOV DS:[0],AX
        MOV AX,0
        MOV DS:[2],AX
        MOV AX,0
        MOV DS:[4],AX
        MOV AX,5
        MOV DS:[6],AX
        MOV AX,21
        MOV DS:[8],AX
        MOV AX,145
        MOV DS:[10],AX
        MOV AX,DS:[10]
        MOV BX,140
        CMP AX,BX
        JL CODE2

CODE1:
        MOV AX,0
        MOV DS:[12],AX
        JMP CODE3

CODE2:
        MOV AX,1
        MOV DS:[12],AX
CODE3:
        MOV AX,DS:[12]
        MOV BX,0
        CMP AX,BX
        JE CODE5

CODE4:
        MOV AX,-1
        MOV DS:[16],AX
        JMP CODE6

CODE5:
        MOV AX,1
        MOV DS:[16],AX
CODE6:
        MOV DX,OFFSET Suname
        MOV AH,9
        INT 21H
        MOV DX,OFFSET Sucollege
        MOV AH,9
        INT 21H
        MOV DX,OFFSET Sumajor
        MOV AH,9
        INT 21H
        MOV AX,DS:[6]
        call dispuib
        call dispcrlf
        MOV AX,DS:[8]
        call dispuib
        call dispcrlf
        MOV AX,DS:[10]
        call dispuib
        call dispcrlf
        MOV AX,DS:[16]
        call dispuib
        call dispcrlf

CODE7:
.exit
END
```

### 运行结果

![image-20210705144904574](http://picture-suyifan.oss-cn-shenzhen.aliyuncs.com/img/image-20210705144904574.png)

# tips

1、`vscode​` 上有一个很好用的插件：`TSAM​`，用来在 `dosbox` 里运行汇编程序

2、`struct` ​ 结构体涉及到词法，文法的修改比较多。可以看一下我 ​`switch case​` 的实现，语义分析这里的**回填**构造的很巧妙

3、编译器有一点小错误就又可能找很久的 `Bug​` ，一定要有耐心

4、可以先从一个不太好的文法开始写，比如写死的文法（`struct` 中的变量固定）然后一步一步修改

