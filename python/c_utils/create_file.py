import os
import sys
from ctypes import cdll,c_void_p,c_int,c_char_p,Structure,byref,POINTER



class create_file():

    def __init__(self,filename,max_buffer_size=10,library="/usr/local/lib/libwrite_file.so"):
        ''' 
            Set up all the necessary items for a new file
        '''
        self.c_lib = cdll.LoadLibrary(library)
        self.c_lib.init_file.restype = POINTER(c_void_p)
        self.wr = self.c_lib.init_file(filename.encode(),max_buffer_size)

    def process_list(self,L):
        ''' 
            Convert a Python list of strings to a ctypes array which meshes with char** in c 
        '''

        arr = (c_char_p * len(L))()
        arr[:] = [x.encode('utf-8') for x in L]
        return arr


    def dump(self,words):
        ''' 
            Put list of words into a buffer 
        ''' 
        arr = self.process_list(words)
        self.c_lib.dump(self.wr,len(words),arr)

    def finalize(self):
        ''' 
            Cleanup file handles and free memory 
        '''
        self.c_lib.cleanup(self.wr)


