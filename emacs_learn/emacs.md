## 安装

> [官网](http://www.gnu.org/software/emacs/emacs.html)
>
> version 27.2
>
> [下载地址](http://ftp.gnu.org/gnu/emacs/)

##### install

```bash
$ dnf install emacs
$ dnf remove emacs


安装编译的依赖
$ dnf install gnutls-devel
$ wget http://ftp.gnu.org/gnu/emacs/emacs-27.2.tar.xz
$ xz -d emacs-27.2.tar.xz
$ tar xvf emacs-27.2.tar
$ ./configure --prefix=/opt/emacs
$ make
$ make install
$ ln -s /opt/emacs/bin/emacs /usr/bin/emacs
```

## 快捷键

> https://aifreedom.com/technology/112

```
C = ctrl
M = Alt
S = Shift
```



| 快捷键  | 说明       |
| ------- | ---------- |
| C-x C-s | 保存文件   |
| C-x C-w | 另存为     |
| C-x C-c | 关闭emacs  |
| C-f     | l          |
| C-b     | h          |
| C-p     | k          |
| C-n     | j          |
| M-f     | 后一个单词 |
| M-b     | 前一个单词 |
| C-a     | 行首       |
| C-e     | 行尾       |
| C-v     | 向下翻一页 |
| M-v     | 向上翻一页 |
| M-<     | 到文件开头 |
| M->     | 到文件末尾 |
|         |            |
|         |            |

## 配置文件

> ~/.emacs

```

 
 
 
 
 
 
 
 
```



