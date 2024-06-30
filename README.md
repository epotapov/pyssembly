# pyssembly
Python module to run inline assembly inside a python script.

## Build 
Open the module in vscode and build the container using Docker.

## Functionality
Currently you can write simple functions in python and immediately execute them.

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
    pys = pyssembly()
    pys.run_all(code)

## Todo
1. Simple inline assembly instructions
2. Extended inline assembly
