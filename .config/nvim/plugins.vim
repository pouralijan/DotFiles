" auto-install vim-plug
if empty(glob('~/.config/nvim/autoload/plug.vim'))
  silent !curl -fLo ~/.config/nvim/autoload/plug.vim --create-dirs
    \ https://raw.githubusercontent.com/junegunn/vim-plug/master/plug.vim
  "autocmd VimEnter * PlugInstall
  autocmd VimEnter * PlugInstall | source $MYVIMRC
endif

call plug#begin('~/.local/share/nvim/autoload/plugged')
   " Intellisense
   Plug 'neoclide/coc.nvim', {'branch': 'release'}

   ""  Text Navigation
   Plug 'unblevable/quick-scope'

   "" Status Line
   Plug 'vim-airline/vim-airline'
   Plug 'vim-airline/vim-airline-themes'

   " " Interactive code
   Plug 'metakirby5/codi.vim'

   " " Git
   Plug 'airblade/vim-gitgutter'
   Plug 'mhinz/vim-signify'
   Plug 'tpope/vim-fugitive'
   Plug 'tpope/vim-rhubarb'
   Plug 'junegunn/gv.vim'
   Plug 'rhysd/git-messenger.vim'

   " emoji
   Plug 'junegunn/vim-emoji'


   " Terminal
   Plug 'voldikss/vim-floaterm'

   " Cool Icons
   Plug 'ryanoasis/vim-devicons'

   " Smooth scroll
   Plug 'psliwka/vim-smoothie'

   " Snippets
   Plug 'honza/vim-snippets'
   Plug 'mattn/emmet-vim'

   " Closetags
   Plug 'alvan/vim-closetag'

   " Better tabline
   " Plug 'mg979/vim-xtabline'
   " Plug 'pacha/vem-tabline'

   " " undo time travel
   " Plug 'mbbill/undotree'

   Plug 'preservim/nerdtree'
   Plug 'preservim/nerdtree' | Plug 'Xuyuanp/nerdtree-git-plugin'
   


   " " Change dates fast
   " Plug 'tpope/vim-speeddating'

   " " Themes
   " Plug 'ayu-theme/ayu-vim'
   " Plug 'whatyouhide/vim-gotham'
   " Plug 'wadackel/vim-dogrun'
   " Plug 'challenger-deep-theme/vim', { 'as': 'challenger-deep' }
   " Plug 'ajmwagar/vim-deus'
   " Plug 'Badacadabra/vim-archery'
   " Plug 'kristijanhusak/vim-hybrid-material'
   " Plug 'tomasr/molokai'
   " Plug 'fmoralesc/molokayo'
   Plug 'arcticicestudio/nord-vim'
   " Plug 'mhartington/oceanic-next'
   " Plug 'rakr/vim-one'
   " 
   " TagBar
   " "Plug 'majutsushi/tagbar'
   Plug 'preservim/tagbar'

   " " Better Comments
   " Plug 'tpope/vim-commentary'

   " " See what keys do like in emacs
   " Plug 'liuchengxu/vim-which-key'

   " " async tasks
   " Plug 'skywind3000/asynctasks.vim'
   " Plug 'skywind3000/asyncrun.vim'

   " Latex live preview
   Plug 'xuhdev/vim-latex-live-preview', { 'for': 'tex' }

   " Dart and Flutter
   Plug 'dart-lang/dart-vim-plugin'
   Plug 'natebosch/vim-lsc'
   Plug 'natebosch/vim-lsc-dart'
   Plug 'thosakwe/vim-flutter'

"    " Convert binary, hex, etc..
"    Plug 'glts/vim-radical'

"    " Repeat stuff
"    Plug 'tpope/vim-repeat'

"    " Useful for React Commenting 
"    Plug 'suy/vim-context-commentstring'

"    " highlight all matches under cursor
"    " Plug 'RRethy/vim-illuminate'
"    " Surround
"    Plug 'tpope/vim-surround'
"    " Files
"    Plug 'tpope/vim-eunuch'
"    " Have the file system follow you around
"    Plug 'airblade/vim-rooter'
"    " auto set indent settings
"    Plug 'tpope/vim-sleuth'
"    " Better Syntax Support
"    " Plug 'nvim-treesitter/nvim-treesitter'
"    Plug 'sheerun/vim-polyglot'
"    " Auto pairs for '(' '[' '{'
"    Plug 'jiangmiao/auto-pairs'

"    " Themes
"    Plug 'christianchiarulli/nvcode.vim'
"    " Plug 'ChristianChiarulli/nv-code'
"    " Plug 'kyazdani42/blue-moon'
"    Plug 'kevinhwang91/rnvimr'

"    " FZF
"    Plug 'junegunn/fzf', { 'do': { -> fzf#install() } }
"    Plug 'junegunn/fzf.vim'



"    " Start Screen
"    Plug 'mhinz/vim-startify'

"    " Vista
"    Plug 'liuchengxu/vista.vim'



"    " Debugging
"    " Plug 'puremourning/vimspector'
"    " Find and replace
"    Plug 'ChristianChiarulli/far.vim'
"    " Plug 'brooth/far.vim'
"    " Auto change html tags
"    Plug 'AndrewRadev/tagalong.vim'
"    " live server
"    Plug 'turbio/bracey.vim'
"    " Swap windows
"    Plug 'wesQ3/vim-windowswap'
"    " Markdown Preview
"    Plug 'iamcco/markdown-preview.nvim', { 'do': 'cd app & npm install'  }
"    " Easily Create Gists
"    Plug 'mattn/vim-gist'
"    Plug 'mattn/webapi-vim'
"    " Colorizer
"    Plug 'norcalli/nvim-colorizer.lua'
"    " Rainbow brackets
"    " Plug 'luochen1990/rainbow'
"    " Async Linting Engine
"    " TODO make sure to add ale config before plugin
"    " Plug 'dense-analysis/ale'
"    " Better Whitespace
"    Plug 'ntpeters/vim-better-whitespace'
"    " Multiple Cursors
"    " TODO add this back in change from C-n
"    " Plug 'mg979/vim-visual-multi', {'branch': 'master'}
"    Plug 'moll/vim-bbye'
"    " Plug 'yuezk/vim-js'
"    " Plug 'maxmellon/vim-jsx-pretty'
"    " Plug 'jelera/vim-javascript-syntax'
"    " Plugin Graveyard
"
"    " jsx syntax support
"    " Typescript syntax
"    " Plug 'HerringtonDarkholme/yats.vim'
"    " Multiple Cursors
"    " Plug 'terryma/vim-multiple-cursors'
"    " Plug 'kaicataldo/material.vim'
"    " Plug 'NLKNguyen/papercolor-theme'
"    " Plug 'tomasiser/vim-code-dark'
"    " Vim Wiki
"    " Plug 'https://github.com/vimwiki/vimwiki.git'
"    " Better Comments
"    " Plug 'jbgutierrez/vim-better-comments'
"    " Echo doc
"    " Plug 'Shougo/echodoc.vim'
"    " Plug 'hardcoreplayers/spaceline.vim'
"    " Plug 'kaicataldo/material.vim', { 'branch': 'main' }
"    " Plug 'arcticicestudio/nord-vim'
"    " Ranger
"    " Plug 'francoiscabrol/ranger.vim'
"    " Plug 'rbgrouleff/bclose.vim'
"    " Making stuff
"    " Plug 'neomake/neomake'
"    " Plug 'mhinz/vim-signify'
"    " Plug 'easymotion/vim-easymotion'
"    " Plug 'preservim/nerdcommenter'
"    " Plug 'brooth/far.vim'
"    " Plug 'atishay/far.vim'
"  endif
"

call plug#end()

" Automatically install missing plugins on startup
autocmd VimEnter *
  \  if len(filter(values(g:plugs), '!isdirectory(v:val.dir)'))
  \|   PlugInstall --sync | q
  \| endif
