" --------------------------------
" Add our plugin to the path
" --------------------------------
python3 import sys
python3 import vim
python3 sys.path.append(vim.eval('expand("<sfile>:h")'))

" --------------------------------
"  Function(s)
" --------------------------------
function! AutoHeader()
python3 << endOfPython

from auto_header import insert_missing_header

insert_missing_header()

endOfPython
endfunction

" --------------------------------
"  Expose our commands to the user
" --------------------------------
command! AutoHeader call AutoHeader()
