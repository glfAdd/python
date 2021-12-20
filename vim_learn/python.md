## 安装

##### install

```bash
$ yum install neovim

$ apt-get install neovim
```

##### 配置文件

```
/home/glfadd/.config/nvim/init.vim
```

##### 支持 python2 / python3

```
1. 查看是否支持 python
:checkhealth


2. 安装插件
$ pip install neovim


3. (可选)设置 python3_host_prog 如果没有设置就使用当前虚拟环境的
let g:python3_host_prog='/home/glfadd/miniconda3/bin/python'


4. (可选)设置 python_host_prog
```

##### 插件管理

> https://github.com/junegunn/vim-plug

- 安装 vim-plug

  ```bash
  $ mkdir -p  ~/.config/nvim/autoload
  $ mkdir -p  ~/.config/nvim/plugged
  $ cd ~/.config/nvim/autoload
  $ wget https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  ```

- 安装插件

  ```bash
  call plug#begin('~/.config/nvim/plugged')
  
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

- uninstall

  ```
  
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

    

  ```
  ```

  

##### git

- install

  ```
  ```

  

##### debug

- install

  ```
  ```

  



## 完整例子

```
"基础设置
set number

"行都为相对于该行的相对行号
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
set cc=80


call plug#begin('~/.config/nvim/plugged')
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
"Plug 'vim-syntastic/syntastic'
Plug 'dense-analysis/ale'

call plug#end()


" ------------- setting
let g:python3_host_prog='/home/glfadd/miniconda3/bin/python'


" ------------- skywind3000/vim-auto-popmenu
" 设定需要生效的文件类型，如果是 "*" 的话，代表所有类型
let g:apc_enable_ft = {'*':1}
" 设定从字典文件以及当前打开的文件里收集补全单词，详情看 ':help cpt'
set cpt=.,k,w,b
" 不要自动选中第一个选项。
set completeopt=menu,menuone,noselect
" 禁止在下方显示一些啰嗦的提示
set shortmess+=c


" ------------- Yggdroot/LeaderF
let g:Lf_ShowDevIcons = 0


" ------------- preservim/nerdcommenter
let g:NERDDefaultAlign = 'left'
let g:NERDTrimTrailingWhitespace = 1


" ------------- Chiel92/vim-autoforma
nnoremap <F3> :Autoformat<CR>

```





