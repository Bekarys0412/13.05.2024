class Person:
    def __init__(self,name):
        self.name=name
    def get_info(self):
        print("Аты:",self.name)

class Emplouyea(Person):
    def job (self,job_name):
        print("Аты:"+ self.name,"Жұмысы:"+job_name)
Emplouyea_obj=Emplouyea("Бекарыс")
Emplouyea_obj.job("Programmer")