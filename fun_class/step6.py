# -*- coding: cp949 -*-

import contextlib
import time

@contextlib.contextmanager
def timer():
    # �ð� ����
    print("start")
    start = time.time()
    yield
    print("end")
    end = time.time()
    print("(�ð�����(Elapsed):{:.2f}��)".format(end-start))

def main():
    with timer():
        print("�󸶳� ���� �ɸ����?")
        time.sleep(1)

if __name__ =="__main__":
    main()