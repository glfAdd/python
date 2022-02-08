# 文档

##### 参考案例

```
Tmux + vim
https://kxcblog.com/post/terminal/2.tmux-tutorial/

plugin
https://zhuanlan.zhihu.com/p/382092667
https://github.com/ayamir/nvimdots/wiki/Plugins

https://zhuanlan.zhihu.com/p/434727338?utm_source=wechat_session&utm_medium=social&s_r=0
https://github.com/nshen/learn-neovim-lua


lsp-status

参考 0207
https://alpha2phi.medium.com/neovim-lsp-and-dap-using-lua-3fb24610ac9f
```

##### 命令

```
:set filetype					查看编码
:h key-notation				查看键盘映射
```

##### [neovim map](https://neovim.io/doc/user/map.html)

# 安装 - neovim

##### install - linux

```bash
$ wget https://github.com/neovim/neovim/releases/download/v0.6.0/nvim-linux64.tar.gz
$ tar zxvf nvim-linux64.tar.gz
$ mkdir -p /opt/neovim-0.6.0
# 移动到 opt
$ ln -s /opt/neovim-0.6.0/bin/nvim /usr/bin/nvim
```

##### install - mac

```bash
$ wget https://github.com/neovim/neovim/releases/download/v0.6.1/nvim-macos.tar.gz

# mac 系统不允许修改 /usr/bin/ 目录
$ ln -s /opt/nvim-osx64/bin/nvim /usr/local/bin/nvim
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

# 快捷键

##### 分屏幕

```
$ vim -On file1 file2 file3		垂直分
$ vim -on file1 file2 file3 	水平

C+w s			上下分割当前打开的文件
:sp filename	上下分割, 并打开一个新的文件
C+w v			左右分割当前打开的文件
:vsp filename	左右分割，并打开一个新的文件

C+w L
C+w H
C+w K
C+w J

C+W =			让所有的屏都有一样的高度
C+W +			增加高度
C+W -			减少高度
C+w w			把光标移到下一个的屏中

C+w c			关闭
C+w q			如果只剩最后 1 个则退出 Vim
```

##### 移动光标

```
0				移动至行首
^				跳至行首的第一个字符
$				跳至行尾
#				开始向文件头的方向搜索光标所在位置的单词的下一个出现位置
*				开始向文件尾的方向搜索光标所在位置的单词的下一个出现位置
R				开始替换
C + b			上一页
C + f			下一页
C - u 			上翻半页
C - d 			下翻半页

yX  			给出一个移动命令 X （如 h、j、H、L 等），复制适当数量的字符、单词或者从光标开始到一定数量的行
yy 或 Y 			复制当前整行
.   			重复最后一个命令

:n  			下一个文件，编辑多个指定文件时，该命令加载下一个文件。
:e 				file  加载新文件来替代当前文件
:r 				file  将新文件的内容插入到光标所在位置的下一行
:w file  		将当期打开的缓存区保存为file。如果是追加到已存在的文件中，则使用 ：w >> file 命令
:r! command  	执行 command 命令，并将命令的输出插入到光标所在位置的下一行

fa				下一个a出现的位置
Fa				上一个a出现的位置
;				重复一次f F 命令

5gg		
5G
gd 				跳至当前光标所在的变量的声明处	
ctrl + o 		回调到上次的位置

/hello			向下搜索
?hello			向上搜索
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



| Command 命令 | Normal  常规模式 | Visual 可视化模式 | Operator Pending 运算符模式 | Insert Only 插入模式 | Command Line 命令行模式 |
| ------------ | ---------------- | ----------------- | --------------------------- | -------------------- | ----------------------- |
| `:map`       | y                | y                 | y                           |                      |                         |
| `:nmap`      | y                |                   |                             |                      |                         |
| `:vmap`      |                  | y                 |                             |                      |                         |
| `:omap`      |                  |                   | y                           |                      |                         |
| `:map!`      |                  |                   |                             | y                    | y                       |
| `:imap`      |                  |                   |                             | y                    |                         |
| `:cmap`      |                  |                   |                             |                      | y                       |

##### 键表

```
<k0> - <k9> 小键盘 0 到 9 *keypad-0* *keypad-9* 
<S-...> Shift＋键 *shift* *<S-* 
<C-...> Control＋键 *control* *ctrl* *<C-* 
<M-...> Alt＋键 或 meta＋键 *meta* *alt* *<M-* <A-...> 同 <m-...> *<A-* <t_xx> termcap 里的 "xx" 入口键<Esc><D> CommandAlt 可以是 <M-key>或<A-key>
```

##### 特殊参数

```
<buffer> <silent> <special> <script> <expr> <unique> 
```

##### buffer

```
打开nvim a.py b.py
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
:e /path/to/file 也可以打开文件到当前 buffer 中
:new 和 
:vnew
:badd {filename} 添加到缓冲区，光标保持在当前缓冲
```

##### 终端模式

```
打开
:terminal
:term
:te
:te bash
:te zsh:terminal {cmd}                当前窗口创建缓冲区

:split | terminal {cmd}      横向分割创建窗口
:vsplit | terminal {cmd}     纵向分割创建窗口
:tabedit | terminal {cmd}        新标签页创建窗口# 纵向分屏
:vs term
://$SHELL# 横向分屏
:split term://$SHELL# 新标签打开
:tabe term://$SHELL命令行中执行插入（i）或者附加（a）操作就可以进入命令行的交互模式。


退出终端模式
<c-\><c-n>C-w
```



##### 查看命令行历史

```
普通模式下:
    q/ 查看使用/输入的搜索历史
    q? 查看使用？输入的搜索历史
    q: 查看命令行历史
```

# packer.nvim

> [github](https://github.com/wbthomason/packer.nvim)

##### install

```bash
$ git clone --depth 1 https://github.com/wbthomason/packer.nvim ~/.local/share/nvim/site/pack/packer/start/packer.nvim
```

##### setting

创建文件 `/.config/nvim/lua/plugins.lua`

```
return require('packer').startup(function()
  -- Packer can manage itself
  use 'wbthomason/packer.nvim'
end)
```

##### 命令

```
-- Regenerate compiled loader file
:PackerCompile

-- Remove any disabled or unused plugins
:PackerClean

-- Clean, then install missing plugins
:PackerInstall

-- Clean, then update and install plugins
:PackerUpdate

-- Perform `PackerUpdate` and then `PackerCompile` ( 安装 / 更新)
:PackerSync

-- Loads opt plugin immediately
:PackerLoad completion-nvim ale
```

# 依赖

##### node

> lsp 需要

```bash
$ brew install node
```

##### devicons 字体

> [homepage](https://www.nerdfonts.com/)
>
> [devicons](https://github.com/vorillaz/devicons)

- mac

  ```bash
  $ brew tap homebrew/cask-fonts
  $ brew install --cask font-hack-nerd-font
  
  
  在终端中选择安装的字体, 字体的名字包含 "Nerd"
  ```

- ubuntu

  ```
  ```

- Centos / fedora

  ```
  
  ```

```
https://github.com/webinstall/webi-installers/tree/main/nerdfont


https://webinstall.dev/nerdfont/

```

##### clipboard 支持

Vim 与系统共用剪切板

查看帮助信息

```
:help clipboard
```

安装

```bash
$ aptiotude install xsel
```

# lsp

##### alpha-nvim

> [github](https://github.com/goolord/alpha-nvim)
>
> [展示](https://github.com/goolord/alpha-nvim/discussions/16)
>
> [开始画面顶部图片](https://github.com/glepnir/dashboard-nvim/wiki/Ascii-Header-Text)

```

```

#####  lualine.nvim

> 状态栏
>
> [github](https://github.com/nvim-lualine/lualine.nvim)

```
+-------------------------------------------------+
| A | B | C                             X | Y | Z |
+-------------------------------------------------+
```

```
branch (git branch)
buffers (shows currently available buffers)
diagnostics (diagnostics count from your preferred source)
diff (git diff status)
encoding (file encoding)
fileformat (file format)
filename
filesize
filetype
hostname
location (location in file in line:column format)
mode (vim mode)
progress (%progress in file)
tabs (shows currently available tabs)
```

##### trouble.nvim

> 错误列表
>
> [github](https://github.com/folke/trouble.nvim)

```

```

##### git

> [github]()

```
https://github.com/lewis6991/gitsigns.nvim
```

##### 滚动条

```
https://github.com/Xuyuanp/scrollbar.nvim
```



##### nvim-tree.lua

> 文件管理
>
> [github](https://github.com/kyazdani42/nvim-tree.lua)

```
nnoremap <C-n> :NvimTreeToggle<CR>
nnoremap <leader>r :NvimTreeRefresh<CR>
nnoremap <leader>n :NvimTreeFindFile<CR>
```

```
o 打开关闭文件夹
a 创建文件
r 重命名
x 剪切
c 拷贝
p 粘贴
d 删除
```

##### bufferline

> [github](https://github.com/akinsho/bufferline.nvim)

```

```

##### which-key.nvim

> [github](https://github.com/folke/which-key.nvim)

```

```

##### nvim-treesitter

> 语法高亮
>
> [github](https://github.com/nvim-treesitter/nvim-treesitter)

```bash
# 查看已安装的 Language parser
:TSInstallInfo

# 手动安装 Language parser
:TSInstall python
:TSInstall java
:TSInstall comment
:TSInstall json
:TSInstall lua
:TSInstall markdown
:TSInstall vim
:TSInstall yaml


# 显示/隐藏 高亮
:TSBufToggle highlight
```

##### telescope

> 历史文件搜索
>
> [github](https://github.com/nvim-telescope/telescope.nvim)

```

```

##### Comment.nvim

> 注释
>
> [github](https://github.com/numToStr/Comment.nvim)

```
另一个没使用的, 不知道好不好用
https://github.com/terrortylor/nvim-comment

VISUAL mode
`gc` - Toggles the region using linewise comment
`gb` - Toggles the region using blockwise comment

```

- normal

  `gcc` - Toggles the current line using linewise comment
  `gbc` - Toggles the current line using blockwise comment
  `[count]gcc` - Toggles the number of line given as a prefix-count using linewise
  `[count]gbc` - Toggles the number of line given as a prefix-count using blockwise
  `gc[count]{motion}` - (Op-pending) Toggles the region using linewise comment
  `gb[count]{motion}` - (Op-pending) Toggles the region using linewise comment

- visual

  `gc` - Toggles the region using linewise comment
  `gb` - Toggles the region using blockwise comment

##### windwp/nvim-autopairs

> 符号配对 []{}()''""
>
> [github](https://github.com/windwp/nvim-autopairs)

```
```

##### 命令模糊匹配 : /

```
https://github.com/gelguy/wilder.nvim
```



##### lsp

> [github](https://github.com/williamboman/nvim-lsp-installer#available-lsps)
>
> 参考 https://zhuanlan.zhihu.com/p/444836713?utm_source=wechat_session&utm_medium=social&utm_oi=1269928803658530816
>
> [语言对应的语言服务器](https://github.com/williamboman/nvim-lsp-installer#available-lsps)

命令 

```
:LspInstallInfo						打开您的语言服务器的图形概览
:LspInstall [--sync] [server] ...	安装/重新安装语言服务器。如果传递参数，则以阻塞方式运行--sync（仅推荐用于脚本目的）。
:LspUninstall [--sync] <server> ...	卸载语言服务器。如果传递参数，则以阻塞方式运行--sync（仅推荐用于脚本目的）。
:LspUninstallAll [--no-confirm]		卸载所有语言服务器
:LspInstallLog						在新选项卡窗口中打开日志文件
:LspPrintInstalled					打印所有已安装的语言服务器


:LspInstall pyright				python
:LspInstall jdtls					java
:LspInstall jsonls				json
:LspInstall yamlls				yaml
:LspInstall lemminx				xml


:LspInfo
```

##### nvim-cmp

> [github](https://github.com/hrsh7th/nvim-cmp)

```



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

##### vim-easy-align 文本对齐

> [github](https://github.com/junegunn/vim-easy-align)

- install

  ```
  Plug 'junegunn/vim-easy-align'
  ```

- use

  ```bash
  # 原文本
  abc   |    1901 |2300000
  histort |19012021 |   C001H2
  PersonAction    |2201        |             HHKI!HA
  
  
  # ga|
  abc          | 1901 |2300000
  histort      | 19012021 |   C001H2
  PersonAction | 2201        |             HHKI!HA
  
  
  # ga2|
  abc          | 1901     | 2300000
  histort      | 19012021 | C001H2
  PersonAction | 2201     | HHKI!HA
  ```

  

  ```bash
  # 原文本
  abc,       1901
  histort   ,19012021,     C001H2
  PersonAction  ,    2201                     ,HHKI!HA
  
  
  # ga*,
  abc,          1901
  histort,      19012021, C001H2
  PersonAction, 2201,     HHKI!HA
  
  
  # ga向右的箭头*,
  abc          , 1901
  histort      , 19012021 , C001H2
  PersonAction , 2201     , HHKI!HA
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

- 查看文件历史版本

  ```
  :Gdiff
  :Gdiff HEAD
  :Gdiff aaffdfds (版本号)
  :h :Gdiff
  ```

##### markdown

> [github](https://github.com/plasticboy/vim-markdown)

##### preview - markdown 实时预览

> [github](https://github.com/iamcco/markdown-preview.nvim)

- install

  ```
  Plug 'iamcco/markdown-preview.nvim', {'do': 'cd app & yarn install'}
  ```

- use

  ```
  web:
  http://127.0.0.1:8151/page/1
  
  打开预览
  :MarkdownPreview
  
  停止预览
  :MarkDownPreviewStop
  ```

- 问题 1

  - 问题描述

    ```
    安装失败
    ```

  - 解决办法

    ```bash
    进入插件 app 目录
    $ ~/.vim/plugged/markdown-preview.nvim/app
    
    执行 install.sh 脚本
    $ ./install.sh
    ```

- 问题 2

  - 描述

    ```
    执行 MarkdownPreview 时报错: 
    E492: Not an editor command: MarkdownPreview
    ```

  - 原因

    ```
    打开的文件不是 .md
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

#####  undotree

> [github](https://github.com/mbbill/undotree)

- install

  ```
  Plug 'mbbill/undotree'
  ```

# 未使用

##### [代码运行](https://github.com/skywind3000/asyncrun.vim)



# 断点调试

> [github](https://github.com/puremourning/vimspector)
>
> https://www.5axxw.com/wiki/content/jifl0q
>
> Vimpector 有两类配置: 调试适配器配置 和 调试会话配置
>
> 示例代码 `~/.vim/plugged/vimspector/support/test`

##### 调试适配器配置

优先级由低到高, 高优先级覆盖低优先级的 adapters

- 由 `install_gadget.py` 自动生成的 `our-path-to-vimspector/gadgets/<os>/.gadgets.json`, 用户不应该修改
- 在 `your-path-to-vimspector/gadgets/<os>/.gadgets.d/*.json` 用户自定义目录, 需要自己创建
- 在 vim 工作目录向父目录递归搜索到的第一个 `.gadgets.json`
- `.vimspector.json` 中定义的 adapters

##### 调试会话配置

- 每当打开一个新的调试会话时，vimspector 都会在当前目录向父目录递归搜索，如果查找到了 `.vimspector.json`，则使用其中的配置，并将其所在的目录设定为项目根目录. 
- 如果未查找到, 则使用 `<your-path-to-vimspector>/configurations/<os>/<filetype>/*.json` 的配置文件, 将打开的文件的目录设置为项目根目录

##### install

```
Plug 'puremourning/vimspector'
```

##### 命令

```bash
# 查看日志
:VimspectorToggleLog

# 查看信息
:VimspectorDebugInfo

:VimspectorUpdate

# 关闭调试模式
:VimspectorReset
或
:call vimspector#Reset()

# 清除所有断点
:call vimspector#ClearBreakpoints()
```

##### 语言支持

自动下载文件到 `~/.vim/plugged/vimspector/gadgets/linux/download` 目录下

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
:VimspectorInstall debugpy
```

- 方式 3 (推荐)

```
let g:vimspector_install_gadgets = ['debugpy']

执行
:VimspectorInstall
:VimspectorUpdate
```

##### 语言支持 - 指定版本(启动失败)

```
1. 到 github 上下载 zip 的文件

2. 使用命令计算 sha256
$ sha256sum debugpy-1.5.1.zip

3. 修改 ~/.vim/plugged/vimspector/python3/vimspector/gadgets.py 文件中的 version 和 checksum
1.5.1
00cf8235b88880bc2d8f59e8f6585208a43e6f14017cdf11d3a0bb2aeb4fff79
4. 重新安装


Downloading https://github.com/microsoft/debugpy/archive/v1.5.1.zip to /home/glfadd/.vim/plugged/vimspector/gadgets/linux/download/debugpy/1.5.1/v1.5.1.zip
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
| request        | 调试的类型，launch（启动程序） 或 attach（连接进程）        |          |
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

```
${workspaceFolder} 			当前工作目录(根目录)
${workspaceFolderBasename}	当前文件的父目录
${file}						当前打开的文件名(完整路径)
${relativeFile} 			当前根目录到当前打开文件的相对路径(包括文件名)
${relativeFileDirname} 		当前根目录到当前打开文件的相对路径(不包括文件名)
${fileBasename} 			当前打开的文件名(包括扩展名)
${fileBasenameNoExtension}	当前打开的文件名(不包括扩展名)
${fileDirname} 				当前打开文件的目录
${fileExtname} 				当前打开文件的扩展名
${cwd} 						启动时task工作的目录
${lineNumber} 				当前激活文件所选行
${selectedText} 			当前激活文件中所选择的文本
${execPath} 				vscode执行文件所在的目录
${defaultBuildTask} 		默认编译任务(build task)的名字
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

##### 窗口

- vimspector.Variables

  ```
  变量
  ```

- vimspector.Variables

  ```
  监视窗口 (想看哪个变量在这里打印)
  
  insert 模式输入变量, <CR> 确定
  <CR>展开/折叠
  <DEL>删除
  ```

- vimspector.StackTrace 

  ```
  线程
  <CR>展开/折叠
  ```

- 终端输出

  ```bash
  # 切换模式
  :VimspectorShowOutput <TAB> 
  
  
  # 有4中模式
      vimspector.Output:stderr		
      vimspector.Console				交互模式也是控制台输出命令的模式
      _vimspector_log_Vimspector
      vimspector.Output:server
  
  
  # Console 模式
  	insert 模式输入变量, <CR> 确定

### python

> 配置文件路径 `~/.vim/plugged/vimspector/configurations/linux/python/`
>
> [python debug 完整参数](https://github.com/microsoft/debugpy/wiki/Debug-configuration-settings)
>
> JSON配置文件允许C-style注释
>
> ​	`// comment to end of line ...`
>
> ​	`/* inline comment ... */` 

##### python-flask.json

```
"console": "integratedTerminal"		是否在屏幕右侧插入外部终端

"console": "externalTerminal"	
"stopOnEntry": false				是否在程序入口点暂停
```



- 方式1 : 没有指定 python 的环境变量, 默认使用系统的

  ```json
  {
      "configurations":{
          "run":{
              "adapter":"debugpy",
              "default":true,
              "configuration":{
                  "request":"launch",
                  "program":"${file}",
                  "cwd":"${workspaceRoot}",
                  "stopOnEntry":true,
                  "logging":{
                      "engineLogging":true
                  }
              },
              "breakpoints":{
                  "exception":{
                      "raised":"N",
                      "uncaught":"",
                      "userUnhandled":""
                  }
              }
          }
      }
  }
  ```

- 方式 2: 在 `configurations` 外面使用 `variables` 自定义变量指定 python 环境变量, 开始调试的时候需要输入参数

  ```json
  {
      "variables" : {
          "MyPythonPath": "python"
      },
      "configurations":{
          "run":{
              "adapter":"debugpy",
              "default":true,
              "configuration":{
                  "python": "${MyPythonPath}",
                  "request":"launch",
                  "program":"${file}",
                  "cwd":"${workspaceRoot}",
                  "stopOnEntry":true,
                  "logging":{
                      "engineLogging":true
                  }
              },
              "breakpoints":{
                  "exception":{
                      "raised":"N",
                      "uncaught":"",
                      "userUnhandled":""
                  }
              }
          }
      }
  }
  ```

- 方式 3 (推荐): 与 `adapter` 同级使用 `variables` 执行 `shell` 命令获取当前的 python 环境变量

  ```json
  {
      "configurations": {
          "my-python-run": {
              "adapter": "debugpy", 
              "variables": {
                  "MyPythonPath": {
                      "shell": "which python"
                  }
              },
              "default": true,
              "configuration": {
                  "python": "${MyPythonPath}",
                  "request": "launch",
                  "cwd": "${workspaceRoot}",
                  "stopOnEntry": false,
                  "console": "externalTerminal",
                  "logging": {
                      "engineLogging": true
                  },
                  "name": "Python: Flask",
                  "type": "python",
                  "module": "flask",
                  "env": {
                      "FLASK_APP": "aaaa.py",
                      "FLASK_ENV": "development",
                      "FLASK_DEBUG": "0"
                  },
                  "args": [
                      "run",
                      "--no-debugger"
                  ],
                  "jinja": true,
                  "host": "127.0.0.1"
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

##### python-flask.json

```json
{
    "configurations": [
        {
            "name": "Python: Current File",
            "type": "python",
            "request": "launch",
            "program": "${file}",
            "console": "integratedTerminal"
        }
    ]
}
```



### java

##### 示例 - java.json

路径 `~/.vim/plugged/vimspector/configurations/linux/java/java.json`

```json



```

##### 远程调试

```
用debugpy启动应用程序，指定--listen参数。有关详细信息，请参阅debugpy文档。
```

##### 启动时指定参数

```
:call vimspector#LaunchWithSettings( dict )
参数是带有以下键的dict：

configuration：（可选）要启动的调试配置的名称
<anything else>：（可选）要设置的变量的名称
这使得一些集成和自动化。例如，如果您有一个名为Run Test的配置，其中包含一个名为${Test}的替换变量，则可以编写一个映射，该映射最终执行：

vimspector#LaunchWithSettings( #{ configuration: 'Run Test'
                                \Test: 'Name of the test' } )
这将启动Run Test配置，并将${Test}设置为'Name of the test'，而vispector不会提示用户输入或确认这些内容。
```

##### 问题 1

```
flask 断点不停止
https://github.com/puremourning/vimspector/discussions/412
https://github.com/puremourning/vimspector/discussions/482


原因, 不支持 python 多线程应用调试

```





# python

##### import 管理

>  [github](https://github.com/PyCQA/isort)
>
> https://blog.csdn.net/u010751000/article/details/119013304

- 安装

  ```bash
  $ pip install isort
  # 支持 requirements
  $ pip install isort[requirements_deprecated_finder]
  # 支持 requirements 和 pipfile
  $ pip install isort[requirements_deprecated_finder,pipfile_deprecated_finder]
  ```

- 使用

  ```bash
  # 多个文件
  $ isort a.py b.py
  
  # 文件夹
  $ isort .
  
  # 智能平衡格式
  $ isort a.py -e
  
  # 查看不同, 不执行
  $ isort a.py --diff
  
  # 如果上面无法执行, 使用下面的命令
  $ python -m isort code_test.py --diff
  
  # 忽略某行
  import module  # isort:skip
  或
  from xyz import (abc,  # isort:skip
                   yo,
                   hey)                
  ```

