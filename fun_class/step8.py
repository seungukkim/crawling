# -*- coding: cp949 -*-
# 상태(State) + 행동(Action)
class Person:
    """
    사람을 표현하는 클래스

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
        # self가 존재하기 때문에 init에서 받은 값이 알아서 전달된다.
        """
        설명..

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
    # 인스턴스화
    evan=Person("Evan",age=20)
    print(evan.info())

    a=Person("A",10)
    print(a.info())

    print(Person.__doc__)
    help(Person)