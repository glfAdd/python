## 默认操作

##### 启动是分屏幕

```bash
1. 垂直分
$ vim -On file1 file2 file3 ...

2. 水平
$ vim -on file1 file2 file3 ...
```

##### 分屏

```bash
1. 上下分割当前打开的文件
C+w s

2. 上下分割, 并打开一个新的文件
:sp filename

3. 左右分割当前打开的文件
C+w v

4. 左右分割，并打开一个新的文件
:vsp filename
```

##### 移动光标

```
C+w l
C+w h
C+w k
C+w j

把光标移到下一个的屏中
C+w w



0		移动至行首
^		跳至行首的第一个字符
$		跳至行尾
R		开始替换
C + b		上一页
C + f		下一页
C - u 		上翻半页
C - d 		下翻半页


yX  	给出一个移动命令 X （如 h、j、H、L 等），复制适当数量的字符、单词或者从光标开始到一定数量的行
yy 或 Y 复制当前整行
.   	重复最后一个命令

:n  下一个文件，编辑多个指定文件时，该命令加载下一个文件。
:e file  加载新文件来替代当前文件
:r file  将新文件的内容插入到光标所在位置的下一行
:q  退出并放弃更改
:w file  将当期打开的缓存区保存为file。如果是追加到已存在的文件中，则使用 ：w >> file 命令
:wq  保存当前文件的内容并退出。等效于 x! 和 ZZ
:r! command  执行 command 命令，并将命令的输出插入到光标所在位置的下一行

fa		下一个a出现的位置
Fa		上一个a出现的位置
;		重复一次f F 命令

5gg		
5G
gd 		跳至当前光标所在的变量的声明处		

#　		开始向文件头的方向搜索光标所在位置的单词的下一个出现位置
*　		开始向文件尾的方向搜索光标所在位置的单词的下一个出现位置

/hello		向下搜索
?hello		向上搜索

^ 跳至行首的第一个字符
$ 跳至行尾
```

##### 移动分屏

```
C+w L
C+w H
C+w K
C+w J
```

##### 调整高度

```
1. 让所有的屏都有一样的高度。
C+W =

2. 增加高度
C+W +

3. 减少高度
C+W -
```

##### 关闭

```
C+w c

如果只剩最后 1 个则退出 Vim
C+w q
```

##### 替换命令

```
from和to都可以是任何字符串, 其中from还可以是正则表达式
:[range]s/from/to/[flags]
把from指定的字符串替换成to指定的字符串，from可以是正则表达式。


1. 替换当前行中的内容
:s/from/to/     ：  将当前行中的第一个from，替换成to。如果当前行含有多个 from，则只会替换其中的第一个。
:s/from/to/g    ：  将当前行中的所有from都替换成to。
:s/from/to/gc   ：  将当前行中的所有from都替换成to，但是每一次替换之前都会询问请求用户确认此操作。


2.  替换某一行的内容：
:.s/from/to/g   ：  在当前行进行替换操作。
:33s/from/to/g  ：  在第33行进行替换操作。
:$s/from/to/g   ：  在最后一行进行替换操作。

3.  替换某些行的内容
:10,20s/from/to/g   ：  对第10行到第20行的内容进行替换。
:1,$s/from/to/g     ：  对第一行到最后一行的内容进行替换（即全部文本）。
:1,.s/from/to/g     ：  对第一行到当前行的内容进行替换。
:.,$s/from/to/g     ：  对当前行到最后一行的内容进行替换。
:'a,'bs/from/to/g   ：  对标记a和b之间的行（含a和b所在的行）进行替换。 其中a和b是之前用m命令所做的标记。

4.  替换所有行的内容
:%s/from/to/g   ：  对所有行的内容进行替换。

5.2 [range]
不写range   ：  默认为光标所在的行。
.           ：  光标所在的行。
1           ：  第一行。
$           ：  最后一行。
33          ：  第33行。
'a          ：  标记a所在的行（之前要使用ma做过标记）。
.+1         ：  当前光标所在行的下面一行。
$-1         ：  倒数第二行。（这里说明我们可以对某一行加减某个数值来取得相对的行）。
22,33       ：  第22～33行。
1,$         ：  第1行 到 最后一行。
1,.         ：  第1行 到 当前行。
.,$         ：  当前行 到 最后一行。
'a,'b       ：  标记a所在的行 到标记b所在的行。

%           ：  所有行（与 1,$ 等价）。

?chapter?   ：  从当前位置向上搜索，找到的第一个chapter所在的行。（ 其中chapter可以是任何字符串或者正则表达式。
/chapter/   ：  从当前位置向下搜索，找到的第一个chapter所在的行。（ 其中chapter可以是任何字符串或者正则表达式。

注意，上面的所有用于range的表示方法都可以通过 +、- 操作来设置相对偏移量。

5.3 [flags]
无      ：  只对指定范围内的第一个匹配项进行替换。
g       ：  对指定范围内的所有匹配项进行替换。
c       ：  在替换前请求用户确认。
e       ：  忽略执行过程中的错误。

注意：上面的所有flags都可以组合起来使用，比如 gc 表示对指定范围内的
所有匹配项进行替换，并且在每一次替换之前都会请用户确认。
```



## 键盘映射

##### 查看键盘映射

```
:h key-notation
```



| Command 命令 | Normal  常规模式 | Visual 可视化模式 | Operator Pending 运算符模式 | Insert Only 插入模式 | Command Line 命令行模式 |
| ------------ | ---------------- | ----------------- | --------------------------- | -------------------- | ----------------------- |
| `:map`       | y                | y                 | y                           |                      |                         |
| `:nmap`      | y                |                   |                             |                      |                         |
| `:vmap`      |                  | y                 |                             |                      |                         |
| `:omap`      |                  |                   | y                           |                      |                         |
| `:map!`      |                  |                   |                             | y                    | y                       |
| `:imap`      |                  |                   |                             | y                    |                         |
| `:cmap`      |                  |                   |                             |                      | y                       |

![vim键盘映射](./image/vim键盘映射.png)

```
remap
noremap
nnoremap
vnoremap


<CR> 相当于命令最后按回车键
<Return> 相当于 <CR>
<Enter> 相当于 <CR>
```

##### 键表

```
<k0> - <k9> 小键盘 0 到 9 *keypad-0* *keypad-9* 
<S-...> Shift＋键 *shift* *<S-* 
<C-...> Control＋键 *control* *ctrl* *<C-* 
<M-...> Alt＋键 或 meta＋键 *meta* *alt* *<M-* 
<A-...> 同 <m-...> *<A-* 
<t_xx> termcap 里的 "xx" 入口键
<Esc>

<D> Command
Alt 可以是 <M-key>或<A-key>



```

##### 特殊参数

```
<buffer> 
<silent> 
<special> 
<script> 
<expr> 
<unique> 
```

## buffer

```
打开
nvim a.py b.py


:ls, :buffers       列出所有缓冲区
:bn[ext]            下一个缓冲区
:bp[revious]        上一个缓冲区
:b {number, expression}     跳转到指定缓冲区


:sb 3               分屏并打开编号为3的Buffer
:vertical sb 3      同上，垂直分屏
:vertical rightbelow sfind file.txt


:bd
:bd! 不保存退出
:bd3


:e /path/to/file 也可以打开文件到 buffer 中
:new 和 :vnew
:badd {filename} 添加到缓冲区，光标保持在当前缓冲

```

## 终端模式

```
打开
:terminal
:term
:te

:te bash
:te zsh

:terminal {cmd}                当前窗口创建缓冲区
:split | terminal {cmd}      横向分割创建窗口
:vsplit | terminal {cmd}     纵向分割创建窗口
:tabedit | terminal {cmd}        新标签页创建窗口




# 纵向分屏
:vs term://$SHELL

# 横向分屏
:split term://$SHELL

# 新标签打开
:tabe term://$SHELL



命令行中执行插入（i）或者附加（a）操作就可以进入命令行的交互模式。



<c-\><c-n>
C-w
```



