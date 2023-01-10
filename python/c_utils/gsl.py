from ctypes import CDLL, RTLD_GLOBAL
from ctypes import c_double, c_size_t, POINTER

class gsl():

    def __init__(self):
        ''' 
            Load GSL library
        '''
        self.gslcblas = CDLL('/usr/lib64/libgslcblas.so',mode=RTLD_GLOBAL)
        self.libgsl = CDLL('/usr/lib64/libgsl.so')

    def process_list(self,L,dtype):
        ''' 
            Convert a Python list into whatever dtype is specified for C 
        '''
        arr = (dtype * len(L))(*L)
        arr[:] = [x for x in L]
        return arr

    def stats_correlation(self,a1,a2):
        a1 = self.process_list(a1,c_double)
        a2 = self.process_list(a2,c_double)
        stride = c_size_t(1)
        length = c_size_t(len(a1))

        self.libgsl.gsl_stats_correlation.restype = c_double
        self.libgsl.gsl_stats_correlation.argtypes = [
            POINTER(c_double), 
            c_size_t,
            POINTER(c_double),
            c_size_t,
            c_size_t
            ]
        answer = self.libgsl.gsl_stats_correlation(a1, stride, a2, stride, length)
        return answer
