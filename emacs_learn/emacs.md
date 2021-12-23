## 安装

> [官网](http://www.gnu.org/software/emacs/emacs.html)
>
> version 27.2
>
> [下载地址](http://ftp.gnu.org/gnu/emacs/)

##### install - centos

```bash
$ dnf install emacs
$ dnf remove emacs

安装编译的依赖
$ dnf install gnutls-devel
$ wget https://mirrors.nju.edu.cn/gnu/emacs/emacs-27.2.tar.xz
$ xz -d emacs-27.2.tar.xz
$ tar xvf emacs-27.2.tar
$ ./configure --prefix=/opt/emacs
$ make
$ make install
$ ln -s /opt/emacs/bin/emacs /usr/bin/emacs
```

##### install - ubuntu

```
$ apt-get install emacs
$ apt-get remove emacs

安装编译的依赖
$ apt-get install libgtk2.0-dev libxpm-dev libjpeg-dev libgif-dev libtiff-dev libgnutls28-dev libncurses-dev
$ ./configure --prefix=/opt/emacs
$ make
$ make install
$ ln -s /opt/emacs/bin/emacs /usr/bin/emacs
```

##### 运行

```bash
$ emacs -nw
$ emacs
```

## 配置

##### 文件

```
~/.emacs
```

##### 

```
emacs中输入M-x customize-variable RET package-archives，
进入之后可以看到当前的package源
```

##### 设置

```
;; 字符编码

```



##### 配置扩展仓库

```
(setq package-archives '(("gnu" . "http://mirrors.ustc.edu.cn/elpa/gnu/")
                         ("melpa" . "http://mirrors.ustc.edu.cn/elpa/melpa/")
                         ("melpa-stable" . "http://mirrors.ustc.edu.cn/elpa/melpa-stable/")
                         ("org" . "http://mirrors.ustc.edu.cn/elpa/org/")))
```

##### 安装包

```
M-x list-packages 查看所有(安装/未安装)包
M-x package-refresh-contents 更新缓存

C-s django-snippets 搜索
i - 选择要安装的包
d - 选择要删除的包
U - 升级已安装的包
x - 执行操作
d - 选择要删除的包
```

##### 自定义包安装路径

```
~/.emacs.d/package
```

##### 代码补全

> [github](https://github.com/auto-complete/auto-complete/blob/master/doc/manual.md)

- install

  ```
  (require 'package)
  (add-to-list 'package-archives '("melpa" . "https://melpa.org/packages/"))
  ;; 自动打开
  (global-auto-complete-mode t)
  (package-initialize)
  ```

- setting

  ```
  M-x package-list-packages
  M-x package-install auto-complete
  ```

- use

  ```
  手动打开
  M-x auto-complete-mode
  ```

##### 主题

> [github](https://github.com/sellout/emacs-color-theme-solarized)

```
$ git clone https://github.com/sellout/emacs-color-theme-solarized.git

$ wget https://github.com/sellout/emacs-color-theme-solarized/archive/refs/heads/master.zip
$ unzip https://github.com/sellout/emacs-color-theme-solarized/archive/refs/heads/master.zip












```



```
代码自动补全
elpy python 
jedi
company



auto-complete 




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
;;用来改默认路径的
(setq default-directory "E:/Sangber/cpp")


 
 
 
 
 
 
 
 
```



