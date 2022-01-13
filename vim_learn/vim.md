##### 参考案例

```
http://47.112.232.56/github/zh/61928120c295597421382002.html
https://github.com/vim-vdebug/vdebug


Tmux + vim
https://kxcblog.com/post/terminal/2.tmux-tutorial/


https://zhuanlan.zhihu.com/p/267856388



plugin
https://zhuanlan.zhihu.com/p/382092667
https://github.com/ayamir/nvimdots/wiki/Plugins


配色
https://www.cnblogs.com/jhssd/p/6803689.html


https://www.cnblogs.com/cniwoq/p/13272746.html
```

## 安装 - vim  

##### install

> [官网](https://www.vim.org/)
>
> [github](https://github.com/vim/vim)

```bash
# 1. 卸载编译安装的 vim
$ sudo make uninstall

# 2. 安装依赖
$ yum install python36 python36-devel ncurses-devel
$ yum remove vim

# 3. clone
$ git clone https://github.com/vim/vim.git
如果 github clone 速度慢使用国内镜像下载
$ git clone https://github.com.cnpmjs.org/vim/vim.git

# 4. 编译
$ cd vim/src
$ ./configure --with-features=huge --enable-multibyte --enable-rubyinterp=yes --enable-python3interp=yes --disable-selinux --enable-cscope --with-python3-command=python3.6 --prefix=/opt/vim
$ make clean
$ make
$ sudo make install

# 5. 软连接
$ ln -s /opt/vim/bin/vim /usr/bin/vim
```

##### 配置文件

```
Vim 的全局配置一般在/etc/vim/vimrc或者/etc/vimrc，对所有用户生效
用户个人的配置在 ~/.vimrc
```

##### 支持 python2 / 3

```
$ vim --version
```

## 安装 - neovim

##### install

```bash
$ wget https://github.com/neovim/neovim/releases/download/v0.6.0/nvim-linux64.tar.gz
$ tar zxvf nvim-linux64.tar.gz
$ mkdir -p /opt/neovim-0.6.0
# 移动到 opt
$ ln -s /opt/neovim-0.6.0/bin/nvim /usr/bin/nvim
```

##### 配置文件

```
~/.config/nvim/init.vim
```

##### 支持 python2 / 3

```bash
1. 查看是否支持 python
:checkhealth


2. 安装插件
$ pip install neovim
$ pip3 install neovim
```

## vim plug

> [github](https://github.com/junegunn/vim-plug)

##### install

```bash
$ sh -c 'curl -fLo "${XDG_DATA_HOME:-$HOME/.local/share}"/nvim/site/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim'
```

##### setting

```
call plug#begin('~/.vim/plugged')

call plug#end()
```

##### 命令

| Command                             | Description                                                  |
| ----------------------------------- | ------------------------------------------------------------ |
| `PlugInstall [name ...] [#threads]` | Install plugins                                              |
| `PlugUpdate [name ...] [#threads]`  | Install or update plugins                                    |
| `PlugClean[!]`                      | Remove unlisted plugins (bang version will clean without prompt) |
| `PlugUpgrade`                       | Upgrade vim-plug itself                                      |
| `PlugStatus`                        | Check the status of plugins                                  |
| `PlugDiff`                          | Examine changes from the previous update and the pending changes |
| `PlugSnapshot[!] [output path]`     | Generate script for restoring the current snapshot of the plugins |

##### PlugInstall 安装失败

```
修改 /home/glfadd/.vim/autoload/plug.vim

1. 将
let fmt = get(g:, 'plug_url_format', 'https://git::@github.com/%s.git')
改为
let fmt = get(g:, 'plug_url_format', 'https://git::@github.com.cnpmjs.org/%s.git')


2. 将
\ '^https://git::@github\.com', 'https://github.com', '')
改为
\ '^https://git::@github.com.cnpmjs\.org', 'https://github.com.cnpmjs.org', '')
```

## 依赖

##### node.js 支持

- 安装 yarn

  - fedora / centos

    ```bash
    $ curl -sL https://dl.yarnpkg.com/rpm/yarn.repo -o /etc/yum.repos.d/yarn.repo
    $ dnf install yarn
    ```

  - ubuntu

    ```bash
    $ aptitude install dnf
    ```

- 设置

  ```bash
  $ npm install -g neovim
  ```

##### clipboard 支持

查看帮助信息

```
:help clipboard
```

安装

```bash
$ aptiotude install xsel
```

## coc

> [github](https://github.com/neoclide/coc.nvim)
>
> [文档](https://github.com/neoclide/coc.nvim/wiki/Language-servers)
>
> 参考 https://www.pythonf.cn/read/133307
>
> 快捷键参考 https://www.starky.ltd/2021/05/30/vim-configuration-with-coc-support-rust-c-python-complete/

coc.nvim 是针对 neovim 的智能感知插件, 基于微软的  LSP (Language Server Protocol) 协议

##### 安装

> 必须安装 nodejs >= 12.12 才能使用

```
Plug 'neoclide/coc.nvim', {'branch': 'release'}
```

##### 命令

```
:CocInfo

安装命令:CocInstall 插件名
移除命令:CocUninstall 插件名
查看已安装:CocList extensions
更新命令:CocUpdate
```

##### 面板

```
安装面板
:CocInstall coc-marketplace

# 打开面板
:CocList marketplace

# 搜索python 相关子插件
:CocList marketplace pythonjjjkk
```

##### install - 参数补全 / 片段补全

> [github](https://github.com/neoclide/coc-snippets)

- 需要先安装  honza/vim-snippets

  > [github](https://github.com/honza/vim-snippets)

  ```
  Plug 'honza/vim-snippets'
  ```

- 安装

  ```
  :CocInstall coc-snippets
  ```

##### install - python

> [github](https://github.com/fannheyward/coc-pyright)

- 安装补全插件  

  ```
  :CocInstall coc-pyright
  或
  :CocInstall coc-python (停止更新了)
  ```

- 编辑 coc-setting.json(未使用)

  ```json
  
  ```

- pip 包. 会使用当前的 python 环境

  ```
  pip install autopep8
  ```

##### install - java

> [github](https://github.com/neoclide/coc-java)

```
:CocInstall coc-java
```

##### 配置文件

```
保存在 /home/glfadd/.config/nvim/coc-settings.json 中

:CocConfig


https://github.com/fannheyward/coc-pyright/blob/master/package.json
https://github.com/microsoft/pyright/blob/main/docs/configuration.md
```

##### 安装问题 1

- 问题描述

  ```
  [coc.nvim] build/index.js not found, please install dependencies and compile coc.nvim by: yarn install
  ```

- 解决办法

  ```bash
  $ cd ~/.vim/plugged/coc.nvim
  $ yarn install
  $ yarn build
  ```

- 验证

  ```
  安装成功后再次进入 nvim 显示如下消息
  
  [coc.nvim] creating data directory: /home/gong/.config/coc
  ```

##### 安装问题 2

- 问题描述

  ```
  [defx] Vim(call):E117: Unknown function: _defx_init                                                                                                                                                                                
  [defx] function defx#util#call_defx[2]..defx#start[10]..defx#initialize[1]..defx#init#_initialize[5]..defx#init#_channel, line 26
  Error detected while processing function defx#util#call_defx[2]..defx#start[10]..defx#initialize[1]..defx#init#_initialize[5]..defx#init#_channel[32]..defx#init#_python_version_check:
  line    9:
  E121: Undefined variable: g:defx#_python_version_check
  
  ```

- 解决办法

  ```
  :UpdateRemotePlugins
  ```
  

## plugin

##### gruvbox 配色

> [github](https://github.com/morhetz/gruvbox)
>
> [详细设置](https://github.com/morhetz/gruvbox/wiki/Configuration#ggruvbox_contrast_dark)

- install

  ```
  Plug 'morhetz/gruvbox'
  ```

##### font - 字体(未使用)

> [github](https://github.com/ryanoasis/nerd-fonts)

```bash
$ sudo ./install.sh
```

##### vim-airline 状态栏

> [vim-airline](https://github.com/vim-airline/vim-airline)
>
> [vim-airline-themes](https://github.com/vim-airline/vim-airline-themes)
>
> [文档](https://github.com/vim-airline/vim-airline/blob/master/doc/airline.txt)

- install

  ```
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  ```

##### fzf 模糊查询

> [github](https://github.com/junegunn/fzf.vim)

- install

  ```
  Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
  Plug 'junegunn/fzf.vim'
  ```

- use

  ```
  :Files			当前目录下搜索
  :Files /opt		指定目录
  
  :Buffer			打开 buffer
  
  
  Files 模式下使用 tab 多选文件
  
  ```

- 命令

  参考 https://blog.csdn.net/weixin_33982670/article/details/88742016

  | Command          | List                                                         |
  | ---------------- | ------------------------------------------------------------ |
  | `Files [PATH]`   | 普通文件查找 (similar to `:FZF`)                             |
  | `GFiles [OPTS]`  | git文件查找 (`git ls-files`)                                 |
  | `GFiles?`        | git文件查找 (`git status`)                                   |
  | `Buffers`        | buffer文件切换                                               |
  | `Colors`         | Color schemes                                                |
  | `Ag [PATTERN]`   | ag search result (`ALT-A` to select all, `ALT-D` to deselect all) |
  | `Lines [QUERY]`  | 在buffer里的文件中寻找含有某个关键词的行                     |
  | `BLines [QUERY]` | 在当前buffer里查找包含某关键词的行                           |
  | `Tags [QUERY]`   | 以Tag查找 (`ctags -R`)                                       |
  | `BTags [QUERY]`  | Tags in the current buffer                                   |
  | `Marks`          | Marks                                                        |
  | `Windows`        | Windows                                                      |
  | `Locate PATTERN` | `locate` command output                                      |
  | `History`        | `v:oldfiles` and open buffers                                |
  | `History:`       | 命令历史查找                                                 |
  | `History/`       | Search history                                               |
  | `Snippets`       | Snippets (UltiSnips)                                         |
  | `Commits`        | Git commits (requires fugitive.vim)                          |
  | `BCommits`       | Git commits for the current buffer                           |
  | `Commands`       | Commands                                                     |
  | `Maps`           | Normal mode mappings                                         |
  | `Helptags`       | Help tags [1](https://blog.csdn.net/weixin_33982670/article/details/88742016#helptags) |
  | `Filetypes`      | File types                                                   |

##### dashboard-nvim 启动页面

> [github](https://github.com/glepnir/dashboard-nvim)
>
> [开始画面顶部图片](https://github.com/glepnir/dashboard-nvim/wiki/Ascii-Header-Text)

- 依赖: 3 个必须安装一个 (用 fzf)

  > [vim-clap](https://github.com/liuchengxu/vim-clap)
  >
  > [fzf.vim](https://github.com/junegunn/fzf.vim)
  >
  > [telescope.nvim](https://github.com/nvim-lua/telescope.nvim)

- install

  ```
  Plug 'glepnir/dashboard-nvim'
  ```

- setting

  ```
  let g:dashboard_default_executive ='fzf'
  ```

##### vista.vim 函数和变量查看

> [github](https://github.com/liuchengxu/vista.vim) 
>
> [文档](https://github.com/liuchengxu/vista.vim/blob/master/doc/vista.txt)
>
> 依赖: 需要插件 coc.vim

- install

  ```
  Plug 'liuchengxu/vista.vim'
  ```

- use

  ```
  Vista 打开
  Vista! 关闭
  Vista!! 打开/关闭
  ```

##### defx.nvim 文件树

> [github](https://github.com/Shougo/defx.nvim)
>
> https://blog.csdn.net/Marshall001/article/details/115494459

- 依赖

  ```
  Neovim 0.4.0 or Vim8.2+
  Python3.6.1+
  coc.vim
  
  $ pip3 install --user pynvim
  ```

- install

  ```
  if has('nvim')
    Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' }
  else
    Plug 'Shougo/defx.nvim'
    Plug 'roxma/nvim-yarp'
    Plug 'roxma/vim-hug-neovim-rpc'
  endif
  ```

- setting

  ```
  
  ```
  
- use

  ```
  删除/复制等文件操作时提示:
  E21: Cannot make changes, 'Modifiable' is off
  
  :set ma
  :set noma
  
  ```

- 问题1

  ```
  描述: 
  remote/host: python3 host registered plugins ['defx']
  remote/host: generated rplugin manifest: /home/glfadd/.local/share/nvim/rplugin.vim
  
  
  :checkhealth
  ```

  

```

```







##### vim-easy-align 文本对齐

> [github](https://github.com/junegunn/vim-easy-align)
>
> https://www.shuzhiduo.com/A/qVdePZb5Pg/

- install

  ```
  Plug 'junegunn/vim-easy-align'
  ```

- setting

  ```
  
  ```

##### bufexplorer 列表切换 buffer

> [github](https://github.com/jlanzarotta/bufexplorer)

- install

  ```
  Plug 'jlanzarotta/bufexplorer'
  ```

- setting

  ```
  nmap <Leader>bl :BufExplorer<CR> 普通打开
  <Leader>bt 切换打开/关闭
  <Leader>bs 强制水平拆分打开
  <Leader>bv 强制垂直劈开
  ```

##### nerdcommenter 代码注释

> [github](https://github.com/preservim/nerdcommenter)

- install

  ```
  Plug 'preservim/nerdcommenter'
  ```

- setting

  ```
  " 注释和文字中间额外增加 1 个空格
  let g:NERDSpaceDelims = 1m
  
  " 将行注释符左对齐, 不是按照代码缩进注释
  let g:NERDDefaultAlign = 'left'
  
  " 注释对末尾空白符修剪
  let g:NERDTrimTrailingWhitespace = 1
  ```

- use

  ```
  <leader>cc   加注释
  <leader>cu   解开注释
  <leader>c<space>  加上/解开注释, 智能判断
  <leader>cy   先复制, 再注解(p可以进行黏贴)
  ```

##### vim-translator 词典

> [github](https://github.com/voldikss/vim-translator):

- install

  ```
  Plug 'voldikss/vim-translator'
  ```



- 翻译句子

  ```
  
  ```

##### vim-fugitive git工具

> [github](https://github.com/tpope/vim-fugitive)

- install

  ```
  Plug 'tpope/vim-fugitive'
  ```
  
- use

  ```
  :Git status
  :Git diff
  ```

##### markdown

```
https://github.com/plasticboy/vim-markdown

https://zhuanlan.zhihu.com/p/84773275
```

##### vim-floaterm 内置终端

```
https://blog.csdn.net/weixin_39795268/article/details/111344410
```

> [github](https://github.com/voldikss/vim-floaterm)
>
> [文档](https://github.com/voldikss/vim-floaterm/blob/master/doc/floaterm.txt)

- install

  ```
  Plug 'voldikss/vim-floaterm'
  ```

- setting

  ```
  - g:floaterm_keymap_new 打开
  - g:floaterm_keymap_prev
  - g:floaterm_keymap_next
  - g:floaterm_keymap_first
  - g:floaterm_keymap_last
  - g:floaterm_keymap_hide
  - g:floaterm_keymap_show
  - g:floaterm_keymap_kill
  - g:floaterm_keymap_toggle 隐藏/重新打开该窗口
  ```

- use

  ```
  
  ```

##### toggleterm.nvim - 终端

> [github](https://github.com/akinsho/toggleterm.nvim)

```



```



#####  undotree

> [github](https://github.com/mbbill/undotree)

- install

  ```
  Plug 'mbbill/undotree'
  ```

- setting

  ```
  ```

- use

  ```
  


## 断点调试

> [github](https://github.com/puremourning/vimspector)
>
> https://www.5axxw.com/wiki/content/jifl0q
>

##### install

```
Plug 'puremourning/vimspector'
```

##### 语言支持

会下载文件到 `~/.vim/plugged/vimspector/gadgets/linux/download` 目录下

自动生成 `~/.vim/plugged/vimspector/gadgets/linux/.gadgets.json`文件

- 方式 1

```bash
$ cd /home/glfadd/.vim/plugged/vimspector
$ ./install_gadget.py --help
$ ./install_gadget.py --enable-python

# 会自动生成 ~/.vim/plugged/vimspector/gadgets/linux/.gadgets.json
# ${gadgetDir} 代表着存放.gadgets.json的目录
```

- 方式 2

```
tab 补全
:VimspectorInstall debugpy
```

- 方式 3 (推荐)

```
let g:vimspector_install_gadgets = ['debugpy']

执行
:VimspectorInstall
:VimspectorUpdate
```

##### 示例代码

```
/home/glfadd/.vim/plugged/vimspector/support/test
```

##### configurations 优先级

```
1. vimspector 先在当前目录向父目录递归搜索, 如果查找到了 .vimspector.json, 则使用其中的配置，并将其所在的目录设定为项目根目录

2. 如果未查找到，在 vimspector 安装目录 ./configurations/<os>/<filetype>/*.json 的配置文件, 将打开的文件的目录设置为项目根目录。
	/home/glfadd/.vim/plugged/vimspector/configurations/linux/_all/python.json
```

##### .vimspector.json 文件参数

| 参数           | 说明                                                        | 是否必填 |
| -------------- | :---------------------------------------------------------- | -------- |
| adapters       | 调试适配器配置，如果不是进行远程调试，一般不需要设置        |          |
| configurations | 配置字段字典                                                |          |
| adapter        | 使用的调试配置器名称                                        | 是       |
| variables      | 用户定义的变量                                              |          |
| configuration  | 配置名字                                                    | 是       |
| remote-request | 远程调试使用                                                |          |
| remote-cmdLine | 远程调试使用                                                |          |
| request        | 调试的类型，lauch或attach                                   |          |
| type           | cppdgb(GDB/LLDB)或cppvsdbg(Visutal Studio Windows debugger) |          |

##### 自定义变量

```
可以在variable中定义变量。

    {
      "configurations": {
        "some-configuration": {
          "variables": {
            "gdbserver-version": {
              "shell": [ "/path/to/my/scripts/get-gdbserver-version" ],
              "env": {
                "SOME_ENV_VAR": "Value used when running above command"
              }
            },
            "some-other-variable": "some value"
          }
        }
      }
    }

其中gdbserver-version和some-other-variable都是用户定义的变量，可以像预定义变量一样使用。

可以调用外部命令，将外部命令的输出赋给变量。gdbserver-version的值就是/path/to/my/scripts/get-gdbserver-version的输出。

还可以在运行vimspector时输入变量的值。最典型的运例子是程序参数的传递，vimspector调试的程序的参数以数组的形式传递，在配置文件中将args设置为一个在运行时用户输入的变量，就可以模拟命令行的效果。

用户输入值的变量用"*${variable-neme}表示，比如以下配置：

      "args": [ "*${CommandLineArgs}" ]

在运行时vimspector会要求用户输入值，如果用户输入1、2、3,args就会被拓展成["1", "2", "3"]传递给程序。

```

##### 预定义变量

![预定义变量](./image/预定义变量.png)

##### use

>  在每个项目目录中创建 .vimspector.json 用来设置调试的参数

- python

  ```json
  {
    "configurations": {
      "run": {
        "adapter": "debugpy",
        "default": true,
        "configuration": {
          "request": "launch",
          "program": "${workspaceRoot}/${file}",
          "cwd": "${workspaceRoot}",
          "stopOnEntry": true
        },
        "breakpoints": {
          "exception": {
            "raised": "N",
            "uncaught": "",
            "userUnhandled": ""
          }
        }
      }
    }
  }
  ```

##### 自定义按键

```
nmap <F5> <Plug>VimspectorContinue
```

##### HUMAN

| Key          | Function                     | API                                                          |
| ------------ | ---------------------------- | ------------------------------------------------------------ |
| `F5`         | 调试时，继续。否则启动调试。 | `vimspector#Continue()`                                      |
| `F3`         | Stop debugging.              | `vimspector#Stop()`                                          |
| `F4`         | 使用相同的配置重新启动调试。 | `vimspector#Restart()`                                       |
| `F6`         | Pause debugee.               | `vimspector#Pause()`                                         |
| `F9`         | 切换当前行上的行断点。       | `vimspector#ToggleBreakpoint()`                              |
| `<leader>F9` | 切换当前行上的条件行断点。   | `vimspector#ToggleBreakpoint( { trigger expr, hit count expr } )` |
| `F8`         | 为游标下的表达式添加函数断点 | `vimspector#AddFunctionBreakpoint( '<cexpr>' )`              |
| `F10`        | Step Over                    | `vimspector#StepOver()`                                      |
| `F11`        | Step Into                    | `vimspector#StepInto()`                                      |
| `F12`        | 跳出当前功能范围             | `vimspector#StepOut()`                                       |

##### VISUAL_STUDIO

| Key             | Function                     | API                                             |
| --------------- | ---------------------------- | ----------------------------------------------- |
| `F5`            | 调试时，继续。否则启动调试。 | `vimspector#Continue()`                         |
| `Shift F5`      | Stop debugging.              | `vimspector#Stop()`                             |
| `Ctrl Shift F5` | 使用相同的配置重新启动调试。 | `vimspector#Restart()`                          |
| `F6`            | Pause debugee.               | `vimspector#Pause()`                            |
| `F9`            | 切换当前行上的行断点。       | `vimspector#ToggleBreakpoint()`                 |
| `Shift F9`      | 为游标下的表达式添加函数断点 | `vimspector#AddFunctionBreakpoint( '<cexpr>' )` |
| `F10`           | Step Over                    | `vimspector#StepOver()`                         |
| `F11`           | Step Into                    | `vimspector#StepInto()`                         |
| `Shift F11`     | 跳出当前功能范围             | `vimspector#StepOut()`                          |

## pip

##### 性能测试

```
pip install line_profiler
```

## config - neovim

```
call plug#begin('~/.vim/plugged')
Plug 'morhetz/gruvbox'                                      " neovim 主题
Plug 'vim-airline/vim-airline'                              " 状态栏
Plug 'vim-airline/vim-airline-themes'                       " 状态栏主题
Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }         " 模糊查询
Plug 'junegunn/fzf.vim' 
Plug 'glepnir/dashboard-nvim'                               " 启动页面(依赖fzf)
Plug 'neoclide/coc.nvim', {'branch': 'release'}             " 代码补全
if has('nvim')                                      
  Plug 'Shougo/defx.nvim', { 'do': ':UpdateRemotePlugins' } " 文件树
else
  Plug 'Shougo/defx.nvim'
  Plug 'roxma/nvim-yarp'
  Plug 'roxma/vim-hug-neovim-rpc'
endif
Plug 'preservim/nerdcommenter'                              " 代码注释
Plug 'junegunn/vim-easy-align'                              " 文本对齐
Plug 'tpope/vim-fugitive'                                   " git
Plug 'mbbill/undotree'                                      " 撤销树
Plug 'voldikss/vim-translator'                              " 翻译工具
Plug 'liuchengxu/vista.vim'                                 " 函数和变量
Plug 'puremourning/vimspector'                              " 代码调试
Plug 'voldikss/vim-floaterm'                                " 窗口内悬浮终端
Plug 'akinsho/toggleterm.nvim'                              " 内置窗口
Plug 'jlanzarotta/bufexplorer'                              " 列表切换 buffer
Plug 'honza/vim-snippets'                                   " 代码块补全
call plug#end()


" ************************************* setting
let mapleader=','

set encoding=utf-8         " 编码
set fenc=utf-8
set number                 " 显示行号
set noswapfile             " 不生成swap文件
set nobackup               " 不备份文件
set relativenumber         " 行都为相对于该行的相对行号
set showmatch              " 括号匹配
set tabstop=4              " 设置Tab长度为4空格
set shiftwidth=4           " 设置自动缩进长度为4空格
set expandtab              " 使用空格代替制表符
set history=1000           " 操作历史记录数
set autoindent             " 继承前一行的缩进方式，适用于多行注释
set nocompatible           " 关闭与vi的兼容模式
set nowrap                 " 不自动折行
set ignorecase             " 搜索时忽略大小写
set cursorline             " 高亮行
set t_Co=256               " 开启256色支持
set cmdheight=1            " 底部命令行高度
set clipboard+=unnamedplus " 打通系统和 vim 剪切板
set ma                     " defx 插件操作文件需要
set guioptions=            " 去掉两边的scrollbar ???
set hidden
set updatetime=300
set shortmess+=c

" 移动窗口快捷键
nnoremap <C-J> <C-W><C-J> 
nnoremap <C-K> <C-W><C-K>
nnoremap <C-L> <C-W><C-L>
nnoremap <C-H> <C-W><C-H>

" buffer 切换
noremap <Tab> :bn<CR> 
noremap <S-Tab> :bp<CR>
noremap <Leader><Tab> :Bw<CR>
noremap <Leader><S-Tab> :Bw!<CR>
noremap <C-t> :tabnew split<CR>


" ************************************* morhetz/gruvbox 主题
set background=dark                  " 设置背景为黑色 light / dark
colorscheme gruvbox                  " 设置主题为 gruvbox
let g:gruvbox_contrast_dark = 'soft' " soft / medium / hard
let g:gruvbox_contrast_dark = 'soft'


" ************************************* jlanzarotta/bufexplorer 切换 buffer 列表
let g:bufExplorerDefaultHelp = 0              " 不显示帮助说明
let g:bufExplorerShowRelativePath = 0         " 显示绝对路径
let g:bufExplorerSortBy = 'number'            " 按照 buffer 序号排序
let g:bufExplorerDisableDefaultKeyMapping = 1 " 禁用默认按键

nmap <Leader>bl :BufExplorer<CR> " 打开 buffer 列表


" ************************************* fzf.vim 模糊查询文件


" ************************************* neoclide/coc.nvim
nmap <leader>rn <Plug>(coc-rename) " 重命名
xmap <leader>qq <Plug>(coc-format)  " 格式化代码
nmap <leader>qq <Plug>(coc-format)
inoremap <silent><expr> <c-space> coc#refresh() " 手动触发补全

" 使用 tab 切换补全
inoremap <expr> <Tab> pumvisible() ? "\<C-n>" : "\<Tab>"
inoremap <expr> <S-Tab> pumvisible() ? "\<C-p>" : "\<S-Tab>"

nmap <silent> [g <Plug>(coc-diagnostic-prev) " 上一个参数
nmap <silent> ]g <Plug>(coc-diagnostic-next) " 下一个参数
nmap <silent> gd <Plug>(coc-definition) " 跳转到源代码
nmap <silent> gy <Plug>(coc-type-definition)
nmap <silent> gi <Plug>(coc-implementation)
nmap <silent> gr <Plug>(coc-references) " 在当前文件/目录下跳转


" ************************************* glepnir/dashboard-nvim
let g:dashboard_default_executive ='fzf' " 这里使用 fzf
nmap <Leader>ss :<C-u>SessionSave<CR>
nmap <Leader>sl :<C-u>SessionLoad<CR>
nnoremap <silent> <Leader>dh :DashboardFindHistory<CR>
nnoremap <silent> <Leader>df :DashboardFindFile<CR>
nnoremap <silent> <Leader>dc :DashboardChangeColorscheme<CR>
nnoremap <silent> <Leader>da :DashboardFindWord<CR>
nnoremap <silent> <Leader>db :DashboardJumpMark<CR>
nnoremap <silent> <Leader>dn :DashboardNewFile<CR>

" 按键说明
let g:dashboard_custom_shortcut={
  \ 'last_session'       : 'Leader d l',
  \ 'find_history'       : 'Leader d h',
  \ 'find_file'          : 'Leader d f',
  \ 'new_file'           : 'Leader d n',
  \ 'change_colorscheme' : 'Leader d c',
  \ 'find_word'          : 'Leader d a',
  \ 'book_marks'         : 'Leader d b',
  \ }

" 设置按键前面的图表, 必须先定义一个变量, 否则报错
let g:dashboard_custom_shortcut_icon = {}
let g:dashboard_custom_shortcut_icon['last_session'] = ''
let g:dashboard_custom_shortcut_icon['find_history'] = ''
let g:dashboard_custom_shortcut_icon['find_file'] = ''
let g:dashboard_custom_shortcut_icon['new_file'] = ''
let g:dashboard_custom_shortcut_icon['change_colorscheme'] = ''
let g:dashboard_custom_shortcut_icon['find_word'] = ''
let g:dashboard_custom_shortcut_icon['book_marks'] = ''

" 开始的图形
let g:dashboard_custom_header = [
   \' ███████████████████████████ ',
   \' ███████▀▀▀░░░░░░░▀▀▀███████ ',
   \' ████▀░░░░░░░░░░░░░░░░░▀████ ',
   \' ███│░░░░░░░░░░░░░░░░░░░│███ ',
   \' ██▌│░░░░░░░░░░░░░░░░░░░│▐██ ',
   \' ██░└┐░░░░░░░░░░░░░░░░░┌┘░██ ',
   \' ██░░└┐░░░░░░░░░░░░░░░┌┘░░██ ',
   \' ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██ ',
   \' ██▌░│██████▌░░░▐██████│░▐██ ',
   \' ███░│▐███▀▀░░▄░░▀▀███▌│░███ ',
   \' ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██ ',
   \' ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██ ',
   \' ████▄─┘██▌░░░░░░░▐██└─▄████ ',
   \' █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████ ',
   \' ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████ ',
   \' █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████ ',
   \' ███████▄░░░░░░░░░░░▄███████ ',
   \' ██████████▄▄▄▄▄▄▄██████████ ',
   \ ]


" ************************************* vim-airline/vim-airline 状态栏
let g:airline#extensions#tabline#enabled = 1        " 开启tabline
let g:airline#extensions#tabline#buffer_nr_show = 1 " 显示buffer编号
let g:bufferline_modified = '+'                     " 缓冲区已修改的符号
let g:airline_theme='silver'

" 切换 buffer 快捷键
nmap <leader>1 <Plug>AirlineSelectTab1
nmap <leader>2 <Plug>AirlineSelectTab2
nmap <leader>3 <Plug>AirlineSelectTab3
nmap <leader>4 <Plug>AirlineSelectTab3
nmap <leader>5 <Plug>AirlineSelectTab3
nmap <leader>6 <Plug>AirlineSelectTab3
nmap <leader>7 <Plug>AirlineSelectTab3
nmap <leader>8 <Plug>AirlineSelectTab3
nmap <leader>9 <Plug>AirlineSelectTab3
nmap <leader>0 <Plug>AirlineSelectTab3


" ************************************* preservim/nerdcommenter 注释
let g:NERDSpaceDelims = 1 " 注释后面增加 1 个空格
let g:NERDDefaultAlign = 'left'
let g:NERDTrimTrailingWhitespace = 1


" ************************************* junegunn/vim-easy-align 文字对齐
xmap ga <Plug>(EasyAlign)
nmap ga <Plug>(EasyAlign)


" ************************************* mbbill/undotree
nnoremap <Leader>t :UndotreeToggle<CR>


" ************************************* voldikss/vim-translator 词典
let g:translator_window_type = 'popup'      " 弹出窗口中显示。
let g:translator_target_lang = 'zh'         " 目标语言为中文。
let g:translator_source_lang = 'auto'       " 源语言自动识别。
let g:translator_default_engines = ['bing'] " 使用的翻译工具。

nmap <silent> <Leader>w <Plug>TranslateW " 翻译光标下的文本，在窗口中显示翻译内容
vmap <silent> <Leader>w <Plug>TranslateWV "翻译光标下的文本，在窗口中显示翻译内容
" nmap <silent> <Leader>r <Plug>TranslateR " 替换光标下的文本为翻译内容
" vmap <silent> <Leader>r <Plug>TranslateRV " 替换光标下的文本为翻译内容


" ************************************* liuchengxu/vista.vim 文件函数变量
let g:vista_default_executive = 'coc'            " 默认显示 tags 的工具
let g:vista_echo_cursor_strategy ='floating_win' " 启用悬浮窗预览
let g:vista_sidebar_width = 30                   " 侧边栏宽度.
let g:vista_echo_cursor = 1                      " 设置为0，以禁用光标移动时的回显.
let g:vista_cursor_delay = 400                   " 当前游标上显示详细符号信息的时间延迟.
let g:vista_close_on_jump = 0                    " 跳转到一个符号时，自动关闭vista窗口.
let g:vista_stay_on_open = 1                     " 打开vista窗口后移动到它.
let g:vista_blink = [2, 100]                     " 跳转到标记后闪烁光标2次，间隔100ms.
let g:vista_icon_indent = ["╰─▸ ", "├─▸ "]       " 展示样式

" 状态栏显示函数名称
function! NearestMethodOrFunction() abort
  return get(b:, 'vista_nearest_method_or_function', '')
endfunction
set statusline+=%{NearestMethodOrFunction()}

nmap <silent> <Leader>vl :Vista!!<CR> " 隐藏


" ************************************* puremourning/vimspector
let g:vimspector_enable_mappings = 'HUMAN'  " 按键方案 HUMAN / VISUAL_STUDIO
let g:vimspector_install_gadgets = ['debugpy'] " 安装语言支持, 使用 VimspectorInstall 安装


nmap <Leader>dc <Plug>VimspectorContinue
nmap <Leader>ds <Plug>VimspectorStop
nmap <Leader>dr <Plug>VimspectorRestart
nmap <Leader>dk <Plug>VimspectorPause
nmap <Leader>dv <Plug>VimspectorToggleBreakpoint
nmap <Leader>dp <Plug>VimspectorAddFunctionBreakpoint
nmap <Leader>do <Plug>VimspectorStepOver
nmap <Leader>di <Plug>VimspectorStepInto
nmap <Leader>dt <Plug>VimspectorStepOut
" nmap <F7> <Plug>VimspectorRestart


" ************************************* voldikss/vim-floaterm 悬浮内置终端
let g:floaterm_keymap_new = '<Leader>ft'    " 新建
let g:floaterm_keymap_toggle = '<Leader>fh' " 隐藏
let g:floaterm_keymap_prev = '<Leader>fp'   " 上一个
let g:floaterm_keymap_next = '<Leader>fn'   " 下一个
let g:floaterm_keymap_kill = '<Leader>fc'   " 关闭
let g:floaterm_position = 'center'          " 在中间显示
let g:floaterm_width=0.9
let g:floaterm_height=0.9


" ************************************* akinsho/toggleterm.nvim 内置终端
nmap <silent> <Leader>th :ToggleTerm size=20 direction=horizontal<CR>
nmap <silent> <Leader>tv :ToggleTerm direction=vertical<CR>
nmap <silent> <Leader>tf :ToggleTerm direction=float<CR>
nmap <silent> <Leader>tt :ToggleTerm direction=tab<CR>


" ************************************* Shougo/defx.nvim
call defx#custom#option('_', {
      \ 'winwidth': 30,
      \ 'split': 'vertical',
      \ 'direction': 'topleft',
      \ 'show_ignored_files': 0,
      \ 'buffer_name': '',
      \ 'toggle': 1,
      \ 'resume': 1
      \ })

autocmd FileType defx call s:defx_my_settings()
function! s:defx_my_settings() abort
  nnoremap <silent><buffer><expr> <CR>
  \ defx#do_action('open')
  nnoremap <silent><buffer><expr> c
  \ defx#do_action('copy')
  nnoremap <silent><buffer><expr> m
  \ defx#do_action('move')
  nnoremap <silent><buffer><expr> p
  \ defx#do_action('paste')
  nnoremap <silent><buffer><expr> l
  \ defx#do_action('open')
  nnoremap <silent><buffer><expr> E
  \ defx#do_action('open', 'vsplit')
  nnoremap <silent><buffer><expr> P
  \ defx#do_action('preview')
  nnoremap <silent><buffer><expr> o
  \ defx#do_action('open_tree', 'toggle')
  nnoremap <silent><buffer><expr> K
  \ defx#do_action('new_directory')
  nnoremap <silent><buffer><expr> N
  \ defx#do_action('new_file')
  nnoremap <silent><buffer><expr> M
  \ defx#do_action('new_multiple_files')
  nnoremap <silent><buffer><expr> C
  \ defx#do_action('toggle_columns', 'mark:indent:icon:filename:type:size:time')
  nnoremap <silent><buffer><expr> S
  \ defx#do_action('toggle_sort', 'time')
  nnoremap <silent><buffer><expr> d
  \ defx#do_action('remove')
  nnoremap <silent><buffer><expr> r
  \ defx#do_action('rename')
  nnoremap <silent><buffer><expr> !
  \ defx#do_action('execute_command')
  nnoremap <silent><buffer><expr> x
  \ defx#do_action('execute_system')
  nnoremap <silent><buffer><expr> yy
  \ defx#do_action('yank_path')
  nnoremap <silent><buffer><expr> .
  \ defx#do_action('toggle_ignored_files')
  nnoremap <silent><buffer><expr> ;
  \ defx#do_action('repeat')
  nnoremap <silent><buffer><expr> h
  \ defx#do_action('cd', ['..'])
  nnoremap <silent><buffer><expr> ~
  \ defx#do_action('cd')
  nnoremap <silent><buffer><expr> q
  \ defx#do_action('quit')
  nnoremap <silent><buffer><expr> <Space>
  \ defx#do_action('toggle_select') . 'j'
  nnoremap <silent><buffer><expr> *
  \ defx#do_action('toggle_select_all')
  nnoremap <silent><buffer><expr> j
  \ line('.') == line('$') ? 'gg' : 'j'
  nnoremap <silent><buffer><expr> k
  \ line('.') == 1 ? 'G' : 'k'
  nnoremap <silent><buffer><expr> <C-l>
  \ defx#do_action('redraw')
  nnoremap <silent><buffer><expr> <C-g>
  \ defx#do_action('print')
  nnoremap <silent><buffer><expr> cd
  \ defx#do_action('change_vim_cwd')
endfunction

```





