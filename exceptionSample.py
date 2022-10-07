import sys
import os

try:

    #print(100/0)
    os.remove('C:/test3.txt')
    
except:
    print(sys.exc_info()[1],'Exception Occured')
else:
    print('No exception')
finally:
    print("default")
