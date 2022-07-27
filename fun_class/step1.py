# -*- coding: cp949 -*-

def cnt_letter(content,letter):
    """���ڸ� ���� �Լ��Դϴ�.!!
    Args:
        content(str):Ž�� ���ڿ�
        letter(str):ã�� ���ڿ�

    Returns:
        int 
    
    Raises:
        ValueError: ���� Return ���� ���ڰ� �ƴϸ� ������ �߻���Ų��. 
    
    """
    print("�Լ� �׽�Ʈ!")
    if (not isinstance(letter, str)) or len(letter) != 1:
        raise ValueError('`letter` �ݵ�� ���ڿ��� �մϴ�.')
    return (len([char for char in content if char == letter]))
#isinstance(letter,str) => letter�� ��Ʈ������ �˾ƺ��ϴ�.    

if __name__ == "__main__":
    # print(cnt_letter())
    docstring = cnt_letter.__doc__
    border = '#' *28
    print('{}\n{}\n{}'.format(border, docstring, border))

    cal= cnt_letter("abcdabdeeafe","a")
    print(cal)
    print('-----------------')
    print(help(cnt_letter))
