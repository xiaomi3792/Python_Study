# 数据容器
在Python中，有个**数据容器（Container）的概念。

其中包括字符串，由'range（）'函数生成的等差数列，列表（List）、元组（Tuple）、集合（Set）、字典（Dictionary）。

Sequence Type | Set | Map
---|---|---
Sting | Set | Dictionary
range() | Frozen Set |
List | |
Tuple | |
Bytes | |

## 迭代（Iterate）
数据容器里的元素是可以被**迭代的**（Iterable），它们其中包含的元素，可以被逐个访问，以便被处理。

## 列表（List）
列表和字符串一样，是个*有序类型*（Sequence Type）的容器，其中包含着有索引编号的元素。

## 1.3 元组（Tuple）
元组和列表的主要区别有两个：
> - List是可变有序容器，Tuple是不可变有序容器。
> - List用方括号标识[]，Tuple用圆括号标识（）

元组是不可变序列，所以，你没办法从里面删除元素。

但是，你可以在末尾追加元素。所以，严格意义上，对元组来讲，“不可变”的是意思说，“当前已有部分不可变”

List 和 Tuple 的区别。首先是使用场景，在将来需要更改的时候，创建 List；在将来不需要更改的时候，创建 Tuple。其次，从计算机的角度来看，Tuple 相对于 List 占用更小的内存。

## 1.4 集合（Set）
**集合** (Set) 这个容器类型与列表不同的地方在于，首先它不包含重合元素，其次它是无序的；进而，集合又分为两种，Set，可变的。Frozen Set，不可变的。

