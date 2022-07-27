# -*- coding: cp949 -*-

import contextlib
import step6
import time

@contextlib.contextmanager
def openReadOnly(fileName):



    read_file = open(fileName, mode='r',encoding="cp949")
    print("okay1")
    yield read_file 
    #yield를 보자마자 원래 돌던 코드로 돌아가기 떄문에 원래 코드가 끝나고 다시 yield 부분을 실행하러 온다.
    print("okay2")
    read_file.close()

def main(fileName):
    with openReadOnly(fileName)as file:
        text = file.read()

    n=0
    for word in text.split():
        if word in ['카카오','노동자']:
            n += 1
    print("단어 개수:",n)

if __name__=="__main__":
    fileName="data/news_article.txt"
    with step6.timer():
        main(fileName)
        time.sleep(0.25)