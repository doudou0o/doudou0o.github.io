---
title: 10. Regular Expression Matching
date: 2017-02-27 15:30:10
mathjax: true
---

leetcode \#10 Regular Expression Matching 题目详解, 看网上帖子说的不清楚都是直接给代码也没个例子，所以起个帖子记录下自己的思路。

本文主要讲述递归解法和动态规划解法的思想。

<!-- more -->

# 10. Regular Expression Matching*

原文要求如下：

Implement regular expression matching with support for `'.'` and `'*'`.
```
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the **entire** input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
isMatch("aaaa","ab*a*c*a") → true #自己加的
```

### 解法有两种

### 递归
递归想法比较简单代码也比较清楚，但耗时很长复杂度是指数级别
考虑递归思想时，只需要考虑终结情况，和当前情况，其他的任由递归完成
当前情况的考虑如下：
因为`*`号是最复杂的情况甚至可以发生0次于是分成两种情况分别考虑：p[1] 为 `*` 和 p[1] 不为 `*`

1. `p[1] != *` 时：说明当前p[0]不会发生0-n次的变化直接对比就可以，剩下的交给递归
  1. `s[0] == p[0]` 判等（这个相等包含了`.`的情况，后面相同）
  2. 递归判断 `isMatch(s[1:],p[1:])` 两个子串
2. `p[1] == *` 时：说明当前p[0]会发生0-n次的变化，而且都是有效的
  1. 假设发生 0次 ：那么直接将p[0,1]跳过进行递归 `isMatch(s,p[2:])`
  2. 假设发生 1次以上：那么得先判等，然后s+1进行递归 `s[0]==p[0] and isMatch(s[1:],p)`

好了所有情况都考虑好了，就可以直接上代码了，递归思想还是比较简单，直接看代码可能比看上述文字更加简单直接。

> talk is cheep show me code：

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if p=="":
            return s==""

        if len(p)>1 and '*' == p[1]:
            return self.isMatch(s, p[2:]) or ((s!="" and (s[0]==p[0] or '.'==p[0])) and self.isMatch(s[1:], p))
        else:
            return (s!="" and (s[0]==p[0] or '.'==p[0])) and self.isMatch(s[1:], p[1:])
```

### 动态规划
动态规划处理这个问题，更加有效，复杂度为 `O(N*M)`.但是不同于递归直接看代码，动态规划我简直还是先看状态公式更加明了。
用dp[i][j]来代表 s[0:i] 与 p[0:j] 是否匹配，初始化 dp[0][0]=1(空串匹配空串)

$$ 
dp[i][j]=
\begin{cases}
dp[i][j-1],                             &  p[j-1]为\* 考虑到\*只重复1次
\\\\dp[i][j-2],                         &  p[j-1]为\* 考虑到\*只重复0次
\\\\dp[i-1][j]\;\&\&\;S[i-1]==P[j-2],   &  p[j-1]为\* 考虑到\*只重复多次
\\\\dp[i-1][j-1] \;\&\&\; S[i-1]=P[j-1],&  p[j-1]不为\*
\end{cases}
$$

从状态公式基本也能看的明白，要计算 dp[i][j] 的值，要分成两个情况，两个情况分别处理后就能将dp填满，则最后的结果就是 dp[len(s)][len(p)]的值

如果看公式还有点不清楚，来举个栗子：` s="ccd" , p="a*c*d" `
dp的矩阵情况如下：

| # | ^ | a | \* | c | \* | d |
| --- | --- | --- | --- | --- | --- | --- |
| ^ | 1 | 0 | 1 | 0 | 1 | 0 |
| c | 0 | 0 | 0 | 1 | <font color=blue>1</font> | 0 |
| c | 0 | 0 | 0 | 0 | <font color=red>1</font> | 0 |
| d | 0 | 0 | 0 | 0 | 0 | 1 |

蓝色那个是因为 dp[i][j-1]=1 所以这个\*只重复1的匹配结果，因此可以为 1
红色那个是因为 dp[i-1][j]=1 && s[i-1]==p[j-2] 代表已经被重复过了，不止1次，但依然可以被继续重复下去

> talk is cheep show me code：

```python
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        lens = len(s)
        lenp = len(p)
        dp = [[False for col in range(lenp+1)] for row in range(lens+1)]
        dp[0][0] = True

        for j in range(1, lenp+1):
            dp[0][j] = p[j-1]=='*' and dp[0][j-2]==1

        for i in range(1, lens+1):
            for j in range(1, lenp+1):
                if p[j-1] == '*':
                    dp[i][j] = dp[i][j-2] or dp[i][j-1] or (dp[i-1][j] and (s[i-1]==p[j-2] or '.'==p[j-2]))
                else:
                    dp[i][j] = dp[i-1][j-1] and (s[i-1]==p[j-1] or '.'==p[j-1])

        return dp[lens][lenp]
```
