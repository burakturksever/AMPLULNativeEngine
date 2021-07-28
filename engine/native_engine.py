import os
import sys
import subprocess
from engine.langs import langs, cmds
from engine.file_creator import FileCreator
import ast
import json

class NativeEngine:

    def __init__(self, lang):
        self._type = langs[lang]
        self._file_creator = FileCreator(self._type)

    def native_run(self, code_string):
        self._code_string = code_string
        self._create_file()
        self._output = self._call_subprocess().decode()
        self._output = self._try_eval() 
        self._file_creator.destroy_files()       

    def _create_file(self):
        with self._file_creator.create() as f:
            f.write(self._code_string)
            f.close()

    def _call_subprocess(self):
        if cmds[self._type]['exec_type'] == 'direct_run':
            run_cmd_arg_list = [cmds[self._type]['run_cmd']]
            for an_arg in cmds[self._type]['run_args']:
                if an_arg == 'file_in':
                    run_cmd_arg_list.append(self._file_creator.file_path)
                else:
                    run_cmd_arg_list.append(an_arg)
            out = subprocess.check_output(run_cmd_arg_list)
        elif cmds[self._type]['exec_type'] == 'compiled':
            compile_cmd_arg_list = [cmds[self._type]['comp_cmd']]
            for an_arg in cmds[self._type]['comp_args']:
                if an_arg == 'file_in':
                    compile_cmd_arg_list.append(self._file_creator.file_path)
                elif an_arg == 'file_out':
                    compile_cmd_arg_list.append(self._file_creator.file_path.split('.')[1])
                else:
                    compile_cmd_arg_list.append(an_arg)
            subprocess.call(compile_cmd_arg_list)
            run_cmd_arg_list = cmds[self._type]['run_cmd']
            for an_arg in cmds[self._type]['run_args']:
                if an_arg == 'file_in':
                    run_cmd_arg_list += self._file_creator.file_path.split('.')[1]
            out = subprocess.check_output(run_cmd_arg_list)
        return out

    def _try_eval(self):
        try:
            return json.loads(self._output)
        except:
            return self._output
        
    def get_output(self):
        return self._output