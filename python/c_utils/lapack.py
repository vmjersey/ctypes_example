from ctypes import CDLL,POINTER,byref,c_double,c_int

class lapack():

    def __init__(self):
        ''' 
            Load Lapack library
        '''
        self.c_lib = CDLL('/usr/lib64/liblapack.so.3')

    def process_list(self,L,dtype):
        ''' 
            Convert a Python list into whatever dtype is specified for C 
        '''

        arr = (dtype * len(L))(*L)
        arr[:] = [x for x in L]
        return arr

    def dgesv(self,a,b,rows,cols,lda,ldb):
        '''
            The routine solves for X the system of linear equations A*X = B
            source:  https://www.intel.com/content/www/us/en/develop/documentation/onemkl-lapack-examples/top/lapack-routines-linear-equations/gesv-function/dgesv-example/dgesv-example-c.html
        '''
        
        a = self.process_list(a,c_double)
        b = self.process_list(b,c_double)

        rows = c_int(rows)
        ipiv = [0]*rows.value
        ipiv = self.process_list(ipiv,c_int)

        nrhs = c_int(3)
        lda = c_int(rows.value) 
        ldb = c_int(rows.value)
        info = c_int(0)

        self.c_lib.dgesv_.argtypes = [POINTER(c_int),POINTER(c_int),POINTER(c_double),POINTER(c_int),POINTER(c_int),POINTER(c_double),POINTER(c_int),POINTER(c_int)]
        self.c_lib.dgesv_(byref(rows), byref(nrhs), a, byref(lda), ipiv, b, byref(ldb), byref(info));

        return b

