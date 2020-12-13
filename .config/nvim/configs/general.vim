set iskeyword+=-                      	" treat dash separated words as a word text object"
set formatoptions-=cro                  " Stop newline continution of comments

set pumheight=10                        " Makes popup menu smaller
set ruler              			" Show the cursor position all the time
set mouse=                              " Disable your mouse
set laststatus=2                        " Always display the status line
set cursorline                          " Enable highlighting of the current line
set showtabline=2                       " Always show tabs
set nobackup                            " This is recommended by coc
set nowritebackup                       " This is recommended by coc
set shortmess+=c                        " Don't pass messages to |ins-completion-menu|.
set signcolumn=yes                      " Always show the signcolumn, otherwise it would shift the text each time
set incsearch

set encoding=utf-8                      " The encoding displayed
set fileencoding=utf-8                  " The encoding written to file
set enc=utf-8
set fileencoding=utf-8
set fileencodings=ucs-bom,utf8,prc

set guifont=Monaco:h11
set guifontwide=NSimsun:h12

" New stuff
set notimeout nottimeout
set scrolloff=1
set sidescroll=1
set sidescrolloff=1
set display+=lastline
set backspace=eol,start,indent
set nostartofline
let $NVIM_TUI_ENABLE_TRUE_COLOR=1
set mmp=1300
set autochdir                           " Your working directory will always be the same as your working directory
set foldcolumn=2                        " Folding abilities

" You can't stop me
cmap w!! w !sudo tee %

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
" file type recognition
filetype on
filetype plugin on
filetype indent on
