# -*- coding: cp949 -*-

#fun_class/data

def main():
    print("���� �ҷ����� ����")
    with open("data/news_article.txt",encoding="cp949")as file:
        text = file.read()
    print("���� �ҷ����� �Ϸ�")
    
    n=0
    for word in text.split():
        if word in ['īī��','�뵿��']:
            n += 1
    print("�ܾ� ����:",n)
if __name__ == "__main__":
    main()