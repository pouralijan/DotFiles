
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Syntax highlighting Move to after/python.vim
if exists("$VIRTUAL_ENV")
  let g:loaded_python_provider=0
  let g:python3_host_prog=substitute(system("which python3 | head -n2 | tail -n1"), '\n', '', 'g')
else
  let g:loaded_python_provider=0
  let g:python3_host_prog=substitute(system("which python3"), '\n', '', 'g')
endif

let g:python_highlight_all=1

set smartindent
set shiftwidth=4
set softtabstop=4
set tabstop=4
set expandtab

set colorcolumn=100

""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
" Folding -- Config for file type in after file
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
set foldenable
set foldlevelstart=10  " default folding level when buffer is opened
set foldnestmax=10     " maximum nested fold
set foldmethod=indent  " fold based on indentation
""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
