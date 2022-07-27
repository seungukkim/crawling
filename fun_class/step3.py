# -*- coding: cp949 -*-

#fun_class/data

def main():
    print("파일 불러오기 시작")
    with open("data/news_article.txt",encoding="cp949")as file:
        text = file.read()
    print("파일 불러오기 완료")
    
    n=0
    for word in text.split():
        if word in ['카카오','노동자']:
            n += 1
    print("단어 개수:",n)
if __name__ == "__main__":
    main()