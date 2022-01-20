##### 参考

```
https://github.com/cabins/.emacs.d

elpa包管理功能

Emacs高手修炼手册: https://www.jianshu.com/p/42ef1b18d959
视频
https://www.zhihu.com/search?type=content&q=Emacs%E9%AB%98%E6%89%8B%E4%BF%AE%E7%82%BC%E6%89%8B%E5%86%8C%2015
```

# 安装

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

# 配置

> 使用语法 elisp

> 参考
>
> https://www.jianshu.com/p/e9f9a5df96c2
>
> https://www.scanbuf.net/post/manual/basic-config/
>
> 
>
> https://blog.csdn.net/neo_liukun/article/details/115189475?spm=1035.2023.3001.6557&utm_medium=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~Rate-5.nonecase&depth_1-utm_source=distribute.pc_relevant_bbs_down.none-task-blog-2~default~OPENSEARCH~Rate-5.nonecase
>
> 
>
> https://www.cnblogs.com/eat-and-die/p/10309681.html !!!!!!!

##### 源分类

```
gnu: 一般是必备的，其它的 elpa 中的包会依赖 gnu 中的包
melpa: 滚动升级，收录了的包的数量最大
melpa-stable: 依据源码的 Tag （Git）升级，数量比 melpa 少，因为很多包作者根本不打 Tag
org: 仅仅为了 org-plus-contrib 这一个包，org 重度用户使用
marmalade: 似乎已经不维护了，个人不推荐
```

##### ~/.emacs.d 目录结构

```

~/.emacs.d/lisp
插件配置文件目录，配置文件命名格式为init-xxx.el
~/.emacs.d/site-lisp
放置无法从elpa或其它仓库获取的第三方插件，本目录及其子目录须在启动时添加到load-path
~/.emacs.d/init.el
初始化load-path，初始化elpa，加载各插件配置文件等


mkdir -p ~/.emacs.d/lisp
mkdir -p ~/.emacs.d/site-lisp
```

##### 配置文件分类

```

Emacs 还可以有一个默认的初始化文件 default.el ，位于 Emacs 的任何标准的 package 搜索目录下

Emacs 还有配置文件 (site-wide startup file)，称为 site-start.el ，也位于 Emacs 的任何标准的 package 搜索目录下

Emacs 加载 package 中的配置是优先加载 site-start.el , 最后加载 default.el
Emacs 启动时，可以使用 -q 或 –no-init-file 选项来阻止 Emacs 加载初始化文件

inhibit-default-init 设置为 t ，那么 Emacs 不会加载 default.el
可以使用 –no-site-file 来禁止 Emacs 加载 site-start.el 配置文件

early-init.el 特殊的初始化配置文件.该配置文件在初始化 package 系统和 GUI 之前加载。

```

#####

```


after-init-hook 之后完成的（参看 startup 简介）如果用户选项 package-enable-at-startup 被禁用，也就是 package-enable-at-startup 的值为 nil ，那么自动加载就不会被执行。 所以可以控制 package 的加载


```





##### ~/.emacs.d/early-init.el

> 最先执行的配置文件

```lisp
;; 关闭启动界面
(setq inhibit-startup-screen t)
;; 关闭自动加载
;;(setq package-enable-at-startup nil)
;; 禁止改变 frame 大小
(setq frame-inhibit-implied-resize t)
;; 隐藏菜单栏
(push '(menu-bar-lines . 0) default-frame-alist)
;; 隐藏工具栏
(push '(tool-bar-lines . 0) default-frame-alist)
;; 隐藏滚动条
(push '(vertical-scroll-bars) default-frame-alist)
;; 前景色(设置后影响主题)
;;(add-to-list 'default-frame-alist '(foreground-color . "#E0DFDB"))
;; 背景色(设置后影响主题)
;;(add-to-list 'default-frame-alist '(background-color . "#102372"))
;; 行号类型: relative(相对行号), visual
(setq display-line-numbers-type 'relative)
;; 显示行号
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
```

##### ~/.emacs.d/init.el

> 配置文件入口

```lisp
;; 添加源
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


;; 使用 use-package 管理扩展
(unless (package-installed-p 'use-package) 
    (package-refresh-contents) 
    (package-install 'use-package))


;; use-package 全局设置
(eval-and-compile 
    (setq use-package-always-ensure t)
    (setq use-package-always-defer t)
    (setq use-package-always-demand nil) 
    (setq use-package-expand-minimally t) 
    (setq use-package-verbose t))

(require 'use-package)

;; 主题
(use-package gruvbox-theme 
    :init (load-theme 'gruvbox-dark-soft t))

;; 底部状态栏
(use-package smart-mode-line 
    :init 
    (setq sml/no-confirm-load-theme t) 
    (setq sml/theme 'respectful) 
    (sml/setup))


;; 测试启动耗时
(use-package benchmark-init 
  :init (benchmark-init/activate) 
  :hook (after-init . benchmark-init/deactivate))


;; 快捷键提示
(use-package which-key 
  :defer nil 
  :config (which-key-mode))


(custom-set-variables
 ;; custom-set-variables was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 '(package-selected-packages '(gruvbox-theme use-package)))
(custom-set-faces
 ;; custom-set-faces was added by Custom.
 ;; If you edit it by hand, you could mess it up, so be careful.
 ;; Your init file should contain only one such instance.
 ;; If there is more than one, they won't work right.
 )
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

# packages

##### use-package

> 管理包安装

```
 (use-package smooth-scrolling 
    :ensure t ;是否一定要确保已安装
    :defer nil ;是否要延迟加载 
    :init (setq smooth-scrolling-margin 2) ;初始化参数 
    :config (smooth-scrolling-mode t) ;基本配置参数 
    :bind ;快捷键的绑定 
    :hook) ;hook模式的绑定

```

- install

  ```lisp
  ;; 使用 use-package 管理扩展
  (unless (package-installed-p 'use-package) 
      (package-refresh-contents) 
      (package-install 'use-package))
  
  
  ;; use-package 全局设置
  (eval-and-compile 
      (setq use-package-always-ensure t)
      (setq use-package-always-defer t)
      (setq use-package-always-demand nil) 
      (setq use-package-expand-minimally t) 
      (setq use-package-verbose t))
  
  (require 'use-package)
  ```

- setting

  ```
  ```

- use

  ```
  
  ```

##### 主题

> [github](https://github.com/greduan/emacs-theme-gruvbox)

- install

  ```lisp
  (use-package gruvbox-theme 
      :init (load-theme 'gruvbox-dark-soft t))
  ```

- setting

  ```
  ```

- use

  ```
  ```

##### 底部状态栏

- install

  ```
  (use-package smart-mode-line 
      :init 
      (setq sml/no-confirm-load-theme t) 
      (setq sml/theme 'respectful) 
      (sml/setup))
  ```

##### 启动耗时工具

> 自带的  `M-x emacs-init-time` 显示信息少

- install

  ```
  (use-package benchmark-init 
    :init (benchmark-init/activate) 
    :hook (after-init . benchmark-init/deactivate))
  ```

- setting

  ```
  
  ```

- use

  ```
  树状统计图
  M-x benchmark-init/show-durations-tree
  
  列表统计图
  M-x benchmark-init/show-durations-tabulated
  ```

##### 快捷键提示

- install

  ```
  (use-package which-key 
    :defer nil 
    :config (which-key-mode))
  ```

- setting

  ```
  ```

- use

  ```
  输入完停顿一下会出现提示框
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



```
evil 插件，可以在 Emacs 上使用 Vi 的操作


mac 改键盘按键
https://karabiner-elements.pqrs.org/

```



> https://aifreedom.com/technology/112





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

# python

```
https://fhxisdog.github.io/2019/11/emacs%E6%90%AD%E5%BB%BApython%E5%BC%80%E5%8F%91%E7%8E%AF%E5%A2%83/
```

# 优化

