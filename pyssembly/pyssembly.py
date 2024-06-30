import ctypes
import os
import subprocess
from loguru import logger as log

class PyssemblyError(Exception):
    def __init__(self, message):
        self.message = message

class Pyssembly:
    def __init__(self):
        self.code_file = 'temp.asm'
        self.obj_file = 'temp.o'
        self.shared_file = 'temp.so'
        self.exec_file = 'temp'

    def _remove_files(self) -> None:
        os.remove(self.code_file)
        os.remove(self.obj_file)
        os.remove(self.exec_file)

    def _assembler_all(self, asm_code:str) -> bool:
        with open(self.code_file, 'w') as f:
            f.write(asm_code)

        try:
            subprocess.run(['nasm', '-f', 'elf64', self.code_file, '-o', self.obj_file])
            subprocess.run(['ld', self.obj_file, '-o', self.exec_file])
        except subprocess.CalledProcessError as e:
            log.error(e)
        return True


    def _assembler_create(self, asm_code:str) -> bool:
        pass

    
    def run_all(self, asm_code:str) -> bool:
        '''Run a whole function written in Assembly'''
        assembled = self._assembler_all(asm_code=asm_code)
        if not assembled:
            raise PyssemblyError(message="Assembly wasn't assembled correctly!")
        try:
            subprocess.run(['./' + self.exec_file])
        except subprocess.CalledProcessError as e:
            log.error(e)
            return False
        finally:
            self._remove_files()
        return True
            

if __name__ == '__main__':
    code = '''
        section     .text
        global      _start 
        _start: 
            mov     edx,len   
            mov     ecx,msg   
            mov     ebx,1   
            mov     eax,4   
            int     0x80   
            mov     eax,1  
            int     0x80   
        section     .data
        msg     db  'Hello world',0xa  
        len     equ $ - msg 
    '''
    pys = Pyssembly()
    pys.run_all(code)