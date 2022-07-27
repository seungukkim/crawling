# -*- coding: cp949 -*-
# ����(State) + �ൿ(Action)
class Person:
    """
    ����� ǥ���ϴ� Ŭ����

    ...
    Attribute
    ---------
    name : str
        name of the person
    age: int
        age of the person
    
    Methods
    -------
    info(additional=""):
        Print the person's name, age, and etc
    """
    def __init__(self,name,age):
        """
        Construct all the cecessary attributes for the person object


        Parameters
        -----------

            name: str
                name of person
            age: int
                age of the person
        """

        self.name = name
        self.age = age

    def info(self, additional=None): 
        # self�� �����ϱ� ������ init���� ���� ���� �˾Ƽ� ���޵ȴ�.
        """
        ����..

        Parameters
        ----------
        additional : str
            More information that will be displayed(default is None)

        Returns 
        -------
        None
        """

        print(f'My name is {self.name}. I am {self.age} years old')
if __name__ =="__main__":
    # �ν��Ͻ�ȭ
    evan=Person("Evan",age=20)
    print(evan.info())

    a=Person("A",10)
    print(a.info())

    print(Person.__doc__)
    help(Person)