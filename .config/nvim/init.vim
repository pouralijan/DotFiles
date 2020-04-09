" Specify a directory for plugins
" - For Neovim: ~/.local/share/nvim/plugged
" - Avoid using standard Vim directory names like 'plugin'
call plug#begin('~/.local/share/nvim/plugged')

if has('nvim')
  " UI related
  Plug 'vim-airline/vim-airline'
  Plug 'vim-airline/vim-airline-themes'

  " Better Visual Guide
  Plug 'Yggdroot/indentLine'

  " syntax check
  Plug 'scrooloose/syntastic'

  " Autocomplete
  " Plug 'ncm2/ncm2'
  " Plug 'roxma/nvim-yarp'
  " Plug 'ncm2/ncm2-bufword'
  " Plug 'ncm2/ncm2-path'
  " Plug 'ncm2/ncm2-jedi'
  " Plug 'Shougo/deoplete.nvim', { 'do': ':UpdateRemotePlugins' }
  " Plug 'zchee/deoplete-clang'
  " Plug 'valloric/youcompleteme'

  " Html
  Plug 'mattn/emmet-vim'

  " Formater
  Plug 'Chiel92/vim-autoformat'


  " Color
  Plug 'dracula/vim'

  " NerdTree
  Plug 'scrooloose/nerdtree'
  Plug 'Xuyuanp/nerdtree-git-plugin'

  " Git
  Plug 'airblade/vim-gitgutter'

  " Plug 'lambdalisue/suda.vim'
  " Plug 'metakirby5/codi.vim'

endif

" Initialize plugin system
call plug#end()

let g:deoplete#enable_at_startup = 1

" set HTML auto complite key
let g:user_emmet_leader_key=','


set nocompatible


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Tab and Space
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set smartindent
set shiftwidth=4
set softtabstop=4
set tabstop=4
set noexpandtab
set autoindent
set copyindent
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Search
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Show search resualt on center of screen.
nnoremap n nzz
nnoremap N Nzz
set incsearch       " search as characters are entered
set hlsearch        " highlight matche
set ignorecase      " ignore case when searching
set smartcase       " ignore case if search pattern is lower case
                    " case-sensitive otherwise
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" UI Config
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" Colors
let $NVIM_TUI_ENABLE_TRUE_COLOR=1
syntax enable                " enable syntax processing
colorscheme default
set background=dark

augroup numbertoggle
  autocmd!
  autocmd BufEnter,FocusGained,InsertLeave,WinEnter * if &nu | set rnu   | endif
  autocmd BufLeave,FocusLost,InsertEnter,WinLeave   * if &nu | set nornu | endif
augroup END

set hidden
set number relativenumber     " show line number
set showcmd                   " show command in bottom bar
set cursorline                " highlight current line
set wildmenu                  " visual autocomplete for command menu
set showmatch                 " highlight matching brace
set laststatus=2              " window will always have a status line
set nobackup
set noswapfile
let &colorcolumn="80,".join(range(120,999),",")  " Move it to after file
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Folding -- Config for file type in after file
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set foldenable
set foldlevelstart=10  " default folding level when buffer is opened
set foldnestmax=10     " maximum nested fold
set foldmethod=syntax  " fold based on indentation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

" file type recognition
filetype on
filetype plugin on
filetype indent on


" showmode since using vim-airline; otherwise use 'set showmode'
set noshowmode

" open new split panes to right and below (as you probably expect)
set splitright
set splitbelow

" keep cursor vertical in 20% on top or bottom.
augroup VCenterCursor
  au!
  au BufEnter,WinEnter,WinNew,VimResized *,*.*
        \ let &scrolloff=winheight(win_getid()) * 20 / 100
augroup END




" Toggle NERDTree
" Can't get <C-Space> by itself to work, so this works as Ctrl - space - space
" https://github.com/neovim/neovim/issues/3101
" http://stackoverflow.com/questions/7722177/how-do-i-map-ctrl-x-ctrl-o-to-ctrl-space-in-terminal-vim#answer-24550772
nnoremap <C-Space> :NERDTreeToggle<CR>
nmap <C-@> <C-Space>
nnoremap <silent> <Space> :NERDTreeToggle<CR>

autocmd StdinReadPre * let s:std_in=1
autocmd VimEnter * if argc() == 1 && isdirectory(argv()[0]) && !exists("s:std_in") | exe 'NERDTree' argv()[0] | wincmd p | ene | exe 'cd '.argv()[0] | endif

" Automatically delete the buffer of the file you just deleted with NerdTree
let NERDTreeAutoDeleteBuffer = 1

" let NERDTreeMapOpenInTab = 1

autocmd BufWinEnter * NERDTreeMirror

" =====================================
" vim-airline status
" configure: https://github.com/vim-airline/vim-airline#user-content-extensible-pipeline
" =====================================
"let g:airline_theme='deus theme'
" show buffers (if only one tab)

"let g:airline#extensions#tabline#enabled = 1
"let g:airline#extensions#tabline#buffer_nr_show = 1

"let g:airline#extensions#tabline#show_tab_nr = 1
"let g:airline#extensions#tabline#tab_nr_type= 2
"let g:airline#extensions#tabline#show_tab_type = 0

"let s:hidden_all = 0



" move line up or down with <C-j> or <C-k>.
nnoremap <C-j> :m-2<CR>
nnoremap <C-k> :m+<CR>

" function! MyOpen(infile)
"   echo "MyOpen ......"
"   try
"     tab drop a:infile
"   catch
"     tabnew a:infile
"   endtry
" endfunction
" 
" function! SwitchSourceAndHeader()
"   "update!
"   set path+=**
"   if (expand ("%:e") == "cpp")
"     let filename = expand("%:t:r").".h"
"     if bufnr(filename) > 0
"       let filepath = findfile(expand("%:t:r").".h", "**")
"       echo filepath
"       call MyOpen(filepath)
"     else
"       tabfind %:t:r.h
"     endif
"   else
"     let filename = expand("%:t:r").".cpp"
"     if bufnr(filename) > 0
"       let filepath = findfile(expand("%:t:r").".cpp", "**")
"       echo filepath
"       call MyOpen(filepath)
"     else
"       tabfind %:t:r.cpp
"     endif
"   endif
" endfunction
" 
" map <F4> :call SwitchSourceAndHeader()<CR>


""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" syntastic recommended settings
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
let g:syntastic_check_on_wq = 0

let g:syntastic_python_checkers = ['pylint']

let g:syntastic_c_config_file=".vim_syntax"
let g:syntastic_cpp_config_file=".vim_syntax"
let g:syntastic_cpp_check_header = 1
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""


" let g:ycm_global_ycm_extra_conf = '.ycm_extra_conf.py'


