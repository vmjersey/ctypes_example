# ctypes_example


## How to use this library

   1.  Proceeduraly 
```
import smacky

lib = write_file/libwrite_file.so
f = smacky.create_file(lib)


words = ["I","do","not","like","green"]
f.dump(words)
words = ["eggs","and","ham","."]
f.dump(words)
wrds = ["I","do","not","like","them","sam","I","am","."]
f.dump(words)

f.finalize()
```
                
