##### 参考

```
https://github.com/cabins/.emacs.d

elpa包管理功能
```



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
$ dnf install gnutls-devel make gcc clang ncurses-devel 
$ wget https://mirrors.nju.edu.cn/gnu/emacs/emacs-27.2.tar.xz
$ xz -d emacs-27.2.tar.xz
$ tar xvf emacs-27.2.tar

$ ./configure --prefix=/opt/emacs (不用这个)
$ ./configure --prefix=/opt/emacs --without-x (用这个)

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
~/.emacs.d/init.el
```

##### 配置扩展仓库

```
(setq package-archives '(("gnu" . "http://mirrors.ustc.edu.cn/elpa/gnu/")
                         ("melpa" . "http://mirrors.ustc.edu.cn/elpa/melpa/")
                         ("melpa-stable" . "http://mirrors.ustc.edu.cn/elpa/melpa-stable/")
                         ("org" . "http://mirrors.ustc.edu.cn/elpa/org/")))
```

##### use-package

```
 (use-package smooth-scrolling 
    :ensure t ;是否一定要确保已安装
    :defer nil ;是否要延迟加载 
    :init (setq smooth-scrolling-margin 2) ;初始化参数 
    :config (smooth-scrolling-mode t) ;基本配置参数 
    :bind ;快捷键的绑定 
    :hook) ;hook模式的绑定

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

##### 按键说明

| Emacs 功能键 | 缩写 | 对应键盘按键(PC/Mac) |
| ------------ | ---- | -------------------- |
| Control      | C    | Ctrl / Control       |
| Meta         | M    | Alt / Option         |
| Shift        | S    | Shift / Shift        |
| Super        | s    | Win / Command        |
| Hyper        | H    | 无                   |
| DEL          |      | backspace            |

```
C-a
C-x b
C-S-<mouse-1>  同时按下 Control 键和 Shift 键, 然后鼠标左键点击
```

|      |                          |                           |
| ---- | ------------------------ | ------------------------- |
| M-x  | execute-extended-command | 输入命令, 单词用 - 或空格 |
| C-g  |                          | 取消命令输入或运行卡住时  |
|      |                          |                           |
|      |                          |                           |
|      | previouse-line           | 上移一行                  |

```



M-a 光标移至句首， M-e 光标移至句尾。整个文件： 。注意这里需要同时按下 Meta 键、 Shift 键和逗号/句号键。


C-a
C-e
M-a
M-e		
M-< 	文件开头
M->		文件末尾
M-r		中 / 上 / 下


C-v		下一页
M-v 	上一页



C-d		
M-k		删除至句尾
C-k		删除至行尾


C-SPC   选择模式
M-w 	复制选中的区域
C-w 	剪切选中的区域
C-y


C-/
C-_
C-x u
C-g C-/	重做一次

C-u 12 C-n		向下 12 行, 默认是 4 次


标记与跳转

上文提到的选中键 C-SPC 不仅是选中文本这么简单的功能，它的本质是设定一个标记（mark）。Emacs 还有一个标记跳转功能，例如我们先在文本的第一行，按下两次 C-SPC（这样我们即打了标记，又没有选中文本），然后光标移动到别的位置（甚至以后学过之后，到别的文件），这时候按下 C-x C-SPC 或 C-u C-SPC，即可立刻跳转回刚刚的位置。同样的，有更好用的插件可以辅助这一功能即上文提到的 counsel。





想要跳到特定的行，M-g M-g 加行号、回车即可



```

##### 小操作

```
1. 不选中文本, 按 2 次 C-SPC
2. 移动到其他地方
3. C-u C-SPC 回刚刚的位置
```

##### 

```


```



```

evil 插件，可以在 Emacs 上使用 Vi 的操作






mac 改键盘按键
https://karabiner-elements.pqrs.org/


```



> https://aifreedom.com/technology/112

```

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

```
C-o 光标下插入空白行
C-e 回车
C-x C-o 删除1个 / 删除多个只剩1个

C-y 粘贴

C-a 行首
C-e 行尾
C-k 删除光标后所有
C-/ 撤销


```





## 优化

##### 查看启动时间

```
M-x emacs-init-time
```

## 示例 

> ~/.emacs.d/init.el

```
					; ================== 源 ==================
(setq package-archives '(
    ("melpa" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/melpa/")
    ("gnu" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/gnu/")
    ("org" . "http://mirrors.tuna.tsinghua.edu.cn/elpa/org/")))

;; 个别时候会出现签名校验失败
(setq package-check-signature nil)
;; 初始化包管理器
(require 'package)
;; 刷新软件源索引
(unless (bound-and-true-p package--initialized)
    (package-initialize))
(unless package-archive-contents
    (package-refresh-contents))

					; ================== 基础设置 ==================
;; 行号类型: relative(相对行号), visual, t
(setq display-line-numbers-type 'relative)
(global-display-line-numbers-mode t)

;; 自动补全括号
(electric-pair-mode t)
;; 括号匹配高亮
(show-paren-mode t)

;; 设置系统的编码,避免各处的乱码
(prefer-coding-system 'utf-8)
(set-default-coding-systems 'utf-8)
(set-terminal-coding-system 'utf-8)
(set-keyboard-coding-system 'utf-8)
(setq default-buffer-file-coding-system 'utf-8)
;; 设置垃圾回收阈值, 加速启动速度
(setq gc-cons-threshold most-positive-fixnum)

					; ================== use-package ==================
(unless (package-installed-p 'use-package)
    (package-refresh-contents)
    (package-install 'use-package))
```

