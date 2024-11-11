import sys
from convert import *

if __name__ == '__main__':
    print(sys.argv)

    s = 0
    for i in range(1, len(sys.argv)):
        s += str_to_float(sys.argv[i])
    print(round(s, 3))



