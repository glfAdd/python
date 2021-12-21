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
Ctrl+w s

2. 上下分割, 并打开一个新的文件
:sp filename

3. 左右分割当前打开的文件
Ctrl+w v

4. 左右分割，并打开一个新的文件
:vsp filename
```

##### 移动光标

```
Ctrl+w l
Ctrl+w h
Ctrl+w k
Ctrl+w j

把光标移到下一个的屏中
Ctrl+w w
```

##### 移动分屏

```
Ctrl+w L
Ctrl+w H
Ctrl+w K
Ctrl+w J
```

##### 调整高度

```
1. 让所有的屏都有一样的高度。
Ctrl+W =

2. 增加高度
Ctrl+W +

3. 减少高度
Ctrl+W -
```

##### 关闭

```
Ctrl+w c

如果只剩最后 1 个则退出 Vim
Ctrl+w q
```

