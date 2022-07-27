# -*- coding: cp949 -*-

import contextlib
import step6
import time

@contextlib.contextmanager
def openReadOnly(fileName):



    read_file = open(fileName, mode='r',encoding="cp949")
    print("okay1")
    yield read_file 
    #yield�� ���ڸ��� ���� ���� �ڵ�� ���ư��� ������ ���� �ڵ尡 ������ �ٽ� yield �κ��� �����Ϸ� �´�.
    print("okay2")
    read_file.close()

def main(fileName):
    with openReadOnly(fileName)as file:
        text = file.read()

    n=0
    for word in text.split():
        if word in ['īī��','�뵿��']:
            n += 1
    print("�ܾ� ����:",n)

if __name__=="__main__":
    fileName="data/news_article.txt"
    with step6.timer():
        main(fileName)
        time.sleep(0.25)