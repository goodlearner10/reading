#!/usr/bin/python3

import os,sys

ret = os.fork()
# fork()
# 자식 프로세스인 경우 0, 부모 프로세스인 경우 CPID 반환
if ret == 0:
    print("자식 프로세스: pid={}, 부모 프로세스의 pid={}".format(os.getpid(),os.getppid()))
    exit()
elif ret > 0:
    print("부모 프로세스 pid={}, 자식 프로세스의 pid={}".format(os.getpid(),ret))
    exit()
    
sys.exit(1)

# 반환값 두 번 출력 됨
# exit(), wait()을 통해 제어하는게 아니기 때문에 어떤게 먼저 실행될지는 장담할 수 없음
          