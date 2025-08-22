"""
Author: Cao Boyuan
Date: 2025-08-22
Description: Week 2 - Day 5: OOP Practice
"""

class Student():
    def __init__(self,name,score):
        self.name=name
        self.score=score
    
    def show_information(self):
        print(f'Name:{self.name},Score:{self.score}')
    
    def update_score(self,score):
        if score<0 or score>100 :
            print('Invalid score.Please enter a score between 0 and 100')
        else:
            self.score=score
            print(f'score updated to {self.score}')

if __name__=='__main__':
    student1=Student('cby',99)
    student2=Student('alx',88)
    student3=Student('alc',30)
    student1.show_information()
    student2.show_information()
    student3.show_information()
    student1.update_score(101)  # Invalid score
    student2.update_score(95)   # Valid score
    student2.show_information()  # Show updated score