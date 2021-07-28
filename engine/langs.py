langs = {
    'LANG_P': 'python',
    'LANG_C': 'c',
    'LANG_J': 'java'
}

cmds = {
    'python': {
        'exec_type': 'direct_run',
        'run_cmd': 'python3',
        'run_args': ['file_in']
    },
    'c': {
        'exec_type': 'compiled',
        'comp_cmd': 'gcc',
        'comp_args': ['file_in', '-o' ,'file_out'],
        'run_cmd': './',
        'run_args': ['file_in']
    },
    'java': {
        'exec_type': 'direct_run',
        'run_cmd': 'java',
        'run_args': ['file_in']
    }
}

exts = {
    'python': '.py',
    'c': '.c',
    'java': '.java'
}