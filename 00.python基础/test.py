# import sys,time
# j = '#'
# if __name__ == '__main__':
#   for i in range(1,61):
#     j += '#'
#     sys.stdout.write(str(int((i/60)*100))+'% '+j+'->'+ "\r")
#     sys.stdout.flush()
#     time.sleep(0.5)
# print

import time
j = '#'
if __name__ == '__main__':
  for i in range(1,61):
    j += '#'
    print(str(int((i/60)*100))+'%'+j+'\r', end='')
    time.sleep(0.5)
