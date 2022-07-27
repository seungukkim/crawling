# -*- coding: cp949 -*-

class Person:
    # attribute
    def __init__(self,name,age):
        self.name =name
        self.age= age

    def whoAmI(self):
        print("I am Person Class")
    
    def singing(self,song):
        return "{} {}을 노래합니다.".format(self.name,song)
    
    def dancing(self):
        return "{} 현재 춤을 춘다.".format(self.name)


class  Korean(Person):

    def __init__(self, name, age):
        super().__init__(name, age)        
        print("Korean class is ready")

    def whoAmI(self):
        print("I am korean class")

    
    def study(self):
        print("fast runner")


class  Japan(Person):

    def __init__(self, name, age):
        super().__init__(name, age)        
        print("Japan class is ready")

    def whoAmI(self):
        print("I am Japan class")   
    def liar(self):
        print("I am liar")





if __name__ =="__main__":
    # kim = Person("Kim",30)
    # kim.whoAmI()
    # print(kim.dancing())
    # print(kim.singing("000"))

    kor_kim= Korean("kor_Kim",20)
    print(kor_kim.singing("000"))
    jpn_hisa=Japan("jpn_hisa",33)
    jpn_hisa.whoAmI()
    print(jpn_hisa.liar())
    print(jpn_hisa.dancing())
    