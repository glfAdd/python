## 安装

##### install

> [官网](https://www.vim.org/)
>
> [github](https://github.com/vim/vim)

```bash
卸载编译安装的 vim
$ sudo make uninstall

安装依赖
$ yum install python36 python36-devel ncurses-devel

$ yum remove vim
$ git clone https://github.com/vim/vim.git
$ cd vim/src
$ ./configure --with-features=huge --enable-multibyte --enable-rubyinterp=yes --enable-python3interp=yes --disable-selinux --enable-cscope --with-python3-command=python3.6
$ make clean
$ make
$ sudo make install
$ ln -s /usr/local/bin/vim /usr/bin/vim
```

##### 配置文件

```
Vim 的全局配置一般在/etc/vim/vimrc或者/etc/vimrc，对所有用户生效
用户个人的配置在 ~/.vimrc
```

##### 查看是否支持 python2 / python3

> python2 和 python3 不能同时支持

```
$ vim --version
```

##### 插件管理

> https://github.com/junegunn/vim-plug

- 安装 vim-plug

  ```bash
  $ curl -fLo ~/.vim/autoload/plug.vim --create-dirs https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  ```

- 安装插件

  ```bash
  call plug#begin('~/.vim/plugged')
  
  call plug#end()
  ```

- 插件命令

  | Command                             | Description                                                  |
  | ----------------------------------- | ------------------------------------------------------------ |
  | `PlugInstall [name ...] [#threads]` | Install plugins                                              |
  | `PlugUpdate [name ...] [#threads]`  | Install or update plugins                                    |
  | `PlugClean[!]`                      | Remove unlisted plugins (bang version will clean without prompt) |
  | `PlugUpgrade`                       | Upgrade vim-plug itself                                      |
  | `PlugStatus`                        | Check the status of plugins                                  |
  | `PlugDiff`                          | Examine changes from the previous update and the pending changes |
  | `PlugSnapshot[!] [output path]`     | Generate script for restoring the current snapshot of the plugins |

## 插件

##### 安装字体

> https://github.com/ryanoasis/nerd-fonts

```


```

##### 状态栏

> https://github.com/vim-airline/vim-airline

- install

  ```
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'
  ```

- setting

  ```
  
  ```

##### 代码补全

> https://github.com/skywind3000/vim-auto-popmenu

- install

  ```
  Plug 'skywind3000/vim-dict'
  Plug 'skywind3000/vim-auto-popmenu'
  ```

- setting

  ```
  " 设定需要生效的文件类型，如果是 "*" 的话，代表所有类型
  let g:apc_enable_ft = {'text':1, 'markdown':1, 'php':1}
  " 设定从字典文件以及当前打开的文件里收集补全单词，详情看 ':help cpt'
  set cpt=.,k,w,b
  " 不要自动选中第一个选项。
  set completeopt=menu,menuone,noselect
  " 禁止在下方显示一些啰嗦的提示
  set shortmess+=c
  ```

##### 目录树

> https://github.com/preservim/nerdtree

- install

  ```
  Plug 'preservim/nerdtree'
  ```

- setting

  ```
  nnoremap <F3> :NERDTreeToggle<CR>
  autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif
  ```

##### 模糊查询

> https://github.com/Yggdroot/LeaderF

- install

  ```
  Plug 'Yggdroot/LeaderF', { 'do': ':LeaderfInstallCExtension' }
  ```

- uninstall

  ```
  :LeaderfInstallCExtension
  :LeaderfUninstallCExtension
  ```

- setting

  ```
  " 关闭头像
  let g:Lf_ShowDevIcons = 0
  ```

- use

  ```
  :Leaderf
  
  查询文件, 默认是从根目录内的文件中查找
  :Leaderf file
  
  默认是再当前文件中查找函数
  :Leaderf function
  
  模糊查询字符串
  :Leaderf rg
  
  查询最近打开过的文件
  :Leaderf mru
  ```

##### 注释

> https://github.com/preservim/nerdcommenter

- install

  ```
  Plug 'preservim/nerdcommenter'
  ```

- setting

  ```
  " 注释和文字中间额外增加 1 个空格
  let g:NERDSpaceDelims = 1
  
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

##### 代码格式化

> https://github.com/vim-autoformat/vim-autoformat

- install

  ```
  Plug 'Chiel92/vim-autoformat'
  ```

- setting

  - python 支持

    ```
    pip install autopep8
    ```

  - java 支持

    ```
    ```

  - 其他设置

    ```
    nnoremap <F6> :Autoformat<CR>
    let g:autoformat_autoindent = 0
    let g:autoformat_retab = 0
    let g:autoformat_remove_trailing_spaces = 0
    ```

- use

  ```
  :Autoformat
  ```


##### 语法检测

> https://github.com/dense-analysis/ale

- install

  ```
  Plug 'dense-analysis/ale'
  ```

- setting

  - python 支持

    ```
    pip install flake8
    ```


##### 运行代码

> https://github.com/skywind3000/asyncrun.vim [文档](https://github.com/skywind3000/asyncrun.vim/blob/master/README-cn.md)
>
> https://github.com/skywind3000/asynctasks.vim [文档](https://github.com/skywind3000/asynctasks.vim/blob/master/README-cn.md)
>

- install

  ```
  Plug 'skywind3000/asyncrun.vim'
  " asyncrun 任务管理插件
  Plug 'skywind3000/asynctasks.vim'
  ```

- setting

  ```
  " asyncrun 运行时自动打开高度为 6 的 quickfix 窗口, 不然你看不到任何输出                 
  let g:asyncrun_open = 10    
  ```

- use

  ```
  运行 python
  :AsyncRun -cwd=$(VIM_FILEDIR) python "$(VIM_FILEPATH)"
  
  :AsyncRun python code_test.py
  ```

##### 断点调试

> [github](https://github.com/puremourning/vimspector)
>
> https://www.bbsmax.com/A/lk5a13l051/
>
> https://www.5axxw.com/wiki/content/jifl0q
>

- install

  ```
  Plug 'puremourning/vimspector'
  ```
  
- setting

  - 语言支持
  
    ```bash
    $ cd /home/glfadd/.vim/plugged/vimspector
    $ ./install_gadget.py --help
    $ ./install_gadget.py --enable-python
    
    # 会自动生成 /home/glfadd/.vim/plugged/vimspector/gadgets/linux/.gadgets.json
    # ${gadgetDir} 代表着存放.gadgets.json的目录
    ```
  
  - 快捷键设置
  
    ```
    # vimspector预设了vscode mode和human mode两套键盘映射
    
    let g:vimspector_enable_mappings = 'HUMAN'
    或
    let g:vimspector_enable_mappings = 'VISUAL_STUDIO'
    ```
  
- 示例代码

  ```
  /home/glfadd/.vim/plugged/vimspector/support/test
  ```
  
- .vimspector.json 文件参数

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
  
- 自定义变量

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

- 预定义变量

  ```
  ```

- use

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
            "program": "${workspaceRoot}/moo.py",
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

- HUMAN

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

- VISUAL_STUDIO

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



## 完整例子

> 参考https://zhuanlan.zhihu.com/p/30022074

```
set number
" 鼠标支持
set mouse=a
"行号都为相对于该行的相对行号
set relativenumber
set encoding=utf-8
"括号匹配
set showmatch
"设置Tab长度为4空格
set tabstop=4
"设置自动缩进长度为4空格
set shiftwidth=4
"继承前一行的缩进方式，适用于多行注释
set autoindent
"关闭与vi的兼容模式
set nocompatible
"不自动折行
set nowrap
"高亮行
set cursorline
"高亮列
set cursorcolumn
"设置高亮的颜色
"highlight CursorLine   cterm=NONE ctermbg=gray ctermfg=green guibg=NONE guifg=NONE
"highlight CursorColumn cterm=NONE ctermbg=gray ctermfg=green guibg=NONE guifg=NONE
"尺寸线
set cc=120

"nnoremap <C-J> <C-W><C-J>
"nnoremap <C-K> <C-W><C-K>
"nnoremap <C-L> <C-W><C-L>
"nnoremap <C-H> <C-W><C-H>


call plug#begin('~/.vim/plugged')
" 状态栏
Plug 'vim-airline/vim-airline'
Plug 'vim-airline/vim-airline-themes'

" 目录树
Plug 'preservim/nerdtree'

" 代码补全
Plug 'skywind3000/vim-dict'
Plug 'skywind3000/vim-auto-popmenu'

" 模糊查询
Plug 'Yggdroot/LeaderF', { 'do': ':LeaderfInstallCExtension' }

" 代码注释
Plug 'preservim/nerdcommenter'

" 代码格式化
Plug 'Chiel92/vim-autoformat'

" 语法检测
Plug 'dense-analysis/ale'


" 代码运行
Plug 'skywind3000/asyncrun.vim'
Plug 'skywind3000/asynctasks.vim'

" debug
Plug 'puremourning/vimspector'


call plug#end()

" --------------------------------- setting


" --------------------------------- skywind3000/vim-auto-popmenu
" 设定需要生效的文件类型，如果是 "*" 的话，代表所有类型
let g:apc_enable_ft = {'*':1}
" 设定从字典文件以及当前打开的文件里收集补全单词，详情看 ':help cpt'
set cpt=.,k,w,b
" 不要自动选中第一个选项。
set completeopt=menu,menuone,noselect
" 禁止在下方显示一些啰嗦的提示
set shortmess+=c


" --------------------------------- Yggdroot/LeaderF
let g:Lf_ShowDevIcons = 0


" --------------------------------- preservim/nerdcommenter
let g:NERDDefaultAlign = 'left'
let g:NERDTrimTrailingWhitespace = 1


" --------------------------------- Chiel92/vim-autoforma
nnoremap <C-l> :Autoformat <CR>


" --------------------------------- skywind3000/asyncrun.vim
" asyncrun 运行时自动打开高度为 6 的 quickfix 窗口, 不然你看不到任何输出                 
let g:asyncrun_open = 10    


" --------------------------------- preservim/nerdtree
nnoremap <F3> :NERDTreeToggle<CR>
autocmd bufenter * if (winnr("$") == 1 && exists("b:NERDTree") && b:NERDTree.isTabTree()) | q | endif


" --------------------------------- puremourning/vimspector
let g:vimspector_enable_mappings = 'HUMAN'
"syntax enable



```





