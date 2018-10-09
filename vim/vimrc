let g:gruvbox_contrast_dark='hard'
colorscheme gruvbox
set background=dark
set t_Co=256
set synmaxcol=2048
"":set clipboard^=unnamed

" " Copy to clipboard
vnoremap  <leader>y  "+y
nnoremap  <leader>Y  "+yg_
nnoremap  <leader>y  "+y
nnoremap  <leader>yy  "+yy

" " Paste from clipboard
nnoremap <leader>p "+p
nnoremap <leader>P "+P
vnoremap <leader>p "+p
vnoremap <leader>P "+P

"f5 to execute
nnoremap <silent> <F5> :!python %<CR>
" ctrl-s to save 
:nmap <c-s> :w<CR>
" ctrl-q to quit without saving 
:nmap <c-q> :q!<CR>
set pastetoggle=<F10>

" new tab ctrl-t
:nmap <c-t> :tabe<CR>

""NERDTREE F2 to open and close
map <F2> :NERDTreeToggle<CR>
map  <C-l> :tabn<CR>
map  <C-h> :tabp<CR>
map  <C-n> :tabnew<CR>

" Syntastic Configuration
set statusline+=%#warningmsg#
set statusline+=%{SyntasticStatuslineFlag()}
set statusline+=%*
:let g:syntastic_loc_list_height=5

let g:syntastic_always_populate_loc_list = 1
let g:syntastic_auto_loc_list = 1
let g:syntastic_check_on_open = 1
" let g:syntastic_check_on_wq = 0
" let g:syntastic_enable_elixir_checker = 1
" let g:syntastic_elixir_checkers = ["elixir"]


"" Python mode config
""Disable rope to avoid hanging
let g:pymode_rope = 0 
let g:pymode_options_colorcolumn = 0

""tagbar config
""map to F8
nmap <F8> :TagbarToggle<CR>

set nocompatible              
filetype off                  
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
set visualbell

Plugin 'gmarik/vundle'
Plugin 'Buffergator'
Plugin 'scrooloose/nerdtree'
Bundle 'jistr/vim-nerdtree-tabs'
Plugin 'davidhalter/jedi-vim'
Plugin 'vim-syntastic/syntastic'
Bundle 'klen/python-mode'
Plugin 'easymotion/vim-easymotion'
Plugin 'vim-airline/vim-airline'
Plugin 'vim-airline/vim-airline-themes'
Plugin 'Townk/vim-autoclose'
Plugin 'universal-ctags/ctags'
Plugin 'majutsushi/tagbar'
Plugin 'sheerun/vim-polyglot'
Plugin 'flazz/vim-colorschemes'
Plugin 'chriskempson/base16-vim'
Plugin 'ctrlpvim/ctrlp.vim'
Plugin 'mileszs/ack.vim'
Plugin 'morhetz/gruvbox'
Plugin 'tpope/vim-fugitive'
Plugin 'nvie/vim-flake8'
Bundle 'vim-ruby/vim-ruby'
Plugin 'xmledit'


call vundle#end()            " required
filetype plugin indent on    " required
let g:AutoClosePreserveDotReg = 0
"""" END Vundle Configuration 


