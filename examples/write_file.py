#!/bin/env python3
import c_utils

f = c_utils.create_file("test.txt")


words = ["I","do","not","like","green"]
f.dump(words)
words = ["eggs","and","ham","."]
f.dump(words)
wrds = ["I","do","not","like","them","sam","I","am","."]
f.dump(words)

f.finalize()
