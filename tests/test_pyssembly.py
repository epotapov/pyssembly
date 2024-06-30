from pyssembly import pyssembly

def test_run_all():
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
    pys = pyssembly.Pyssembly()
    assert pys.run_all(code)