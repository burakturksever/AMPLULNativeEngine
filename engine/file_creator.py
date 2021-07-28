import os
import sys
import hashlib
from datetime import datetime as dt
from engine.langs import exts, cmds
from pathlib import Path

class FileCreator:

    def __init__(self, lang):
        self._lang = lang
        self._temp_dir = './engine/temp/'

    def _hash_func(self):
        string_hash = dt.now().isoformat() + self._lang
        return hashlib.sha1(string_hash.encode('utf-8')).hexdigest()

    def create(self):
        Path('./engine/temp/').mkdir(parents=True, exist_ok=True)
        path = os.getcwd() + '/engine/temp/' + self._hash_func() + exts[self._lang]
        self._set_file_stream(path)
        self.file_path = path
        return self.file_stream

    def _set_file_stream(self, path):
        self.file_stream = open(path, 'w')

    def destroy_files(self):
        filelist = [ f for f in os.listdir(self._temp_dir)]
        for f in filelist:
            os.remove(os.path.join(self._temp_dir, f))