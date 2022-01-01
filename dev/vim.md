```

syntax on    "开启语法高亮"
let g:solarized_termcolors=256    "solarized主题设置在终端下的设置"
set nowrap    "设置不折行"
set fileformat=unix    "设置以unix的格式保存文件"
set cindent        "设置C样式的缩进格式"
set tabstop=4    "设置table长度"
set shiftwidth=4        "同上"
set scrolloff=5        "距离顶部和底部5行"
set laststatus=2    "命令行为两行"
set backspace=2
set selection=exclusive
set selectmode=mouse,key
set matchtime=5
set incsearch
set hlsearch        "高亮搜索项"
set noexpandtab        "不允许扩展table"
set whichwrap+=,h,l
set autoread
"set cursorline        "突出显示当前行"
"set cursorcolumn        "突出显示当前列"
"set splitbelow
"set splitright
set tw=160



Plug 'Yggdroot/indentLine'                "缩进对齐标注"
Plug 'mileszs/ack.vim'                    "在项目里全局搜索某个单词"
Plug 'tmhedberg/SimpylFold'               "自定义标注"
Plug 'bronson/vim-trailing-whitespace'    "表出末尾空格 可以删除"



" airline
" 使用powerline打过补丁的字体
"let g:airline_powerline_fonts = 1

" tabline中当前buffer两端的分隔字符
let g:airline#extensions#tabline#left_sep = ' '
" tabline中未激活buffer两端的分隔字符
let g:airline#extensions#tabline#left_alt_sep = '|'

" color scheme

map <F2> :bp<CR>
map <F3> :bn<CR>


" 窗口调整

nnoremap ˙ <C-W><
nnoremap ¬ <C-W>>
nnoremap ∆ <C-W>+
nnoremap ˚ <C-W>-


au BufNewFile,BufRead *
\ set tabstop=4 |
\ set softtabstop=4 |
\ set shiftwidth=4 |
\ set expandtab |
\ set autoindent |
\ set fileformat=unix |
\ set list listchars=tab:>-







" tagbar跳转
"nmap <F3> :TagbarToggle<CR>
map <Leader>e :TagbarToggle<CR>


" ack
" i 忽略大小写
"nnoremap <Leader>a :Ack!<Space>
"ack
"<Leader>c进行搜索，同时不自动打开第一个匹配的文件"
map <Leader>c :Ack!<Space>
"调用ag进行搜索
if executable('ag')
  let g:ackprg = 'ag --vimgrep'
endif
"高亮搜索关键词
let g:ackhighlight = 1
"修改快速预览窗口高度为15
let g:ack_qhandler = "botright copen 15"
"在QuickFix窗口使用快捷键以后，自动关闭QuickFix窗口
let g:ack_autoclose = 1
"使用ack的空白搜索，即不添加任何参数时对光标下的单词进行搜索，默认值为1，表示开启，置0以后使用空白搜索将返回错误信息
let g:ack_use_cword_for_empty_search = 1
"部分功能受限，但对于大项目搜索速度较慢时可以尝试开启
"let g:ack_use_dispatch = 1



" 删除末尾空格
map <leader>q :FixWhitespace<cr>



```

