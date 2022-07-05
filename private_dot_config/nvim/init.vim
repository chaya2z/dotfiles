"dein Scripts-----------------------------
if &compatible
  set nocompatible               " Be iMproved
endif

" Required:
set runtimepath+=/home/chaya2z/.cache/dein/repos/github.com/Shougo/dein.vim

" Required:
let s:dein_dir = '~/.cache/dein'
if dein#load_state(s:dein_dir)
  call dein#begin(s:dein_dir)
  
  let s:toml = '~/.config/nvim/dein.toml'
  let s:lazy_toml = '~/.config/nvim/lazy_dein.toml'
  call dein#load_toml(s:toml, {'lazy': 0})
  call dein#load_toml(s:lazy_toml, {'lazy': 1})

  call dein#end()
  call dein#save_state()
endif

" Let dein manage dein
" Required:
call dein#add('/home/chaya2z/.cache/dein/repos/github.com/Shougo/dein.vim')

" Add or remove your plugins here like this:
"call dein#add('Shougo/neosnippet.vim')
"call dein#add('Shougo/neosnippet-snippets')

" Required:
filetype plugin indent on
syntax enable

" If you want to install not installed plugins on startup.
if dein#check_install()
  call dein#install()
endif

"End dein Scripts-------------------------

" import config
source ~/.config/nvim/common.vim

