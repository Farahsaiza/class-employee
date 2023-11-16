class employe () :
    def __init__(self, number, name, cin, sales, bonus_hrs, base_salary ) :
        self.number =  number
        self.name  =  name
        self.cin =  cin
        self.sales = sales
        self.bonus_hrs =  bonus_hrs
        self.base_salary = base_salary

    def info(self):
        print("the employee number : {}, his/her name is: {}, cin: {}, sales : {},  bonus_hrs: {}, base_salary: {}"
              .format(self.number , self.name , self.cin , self.sales , self.bonus_hrs , self.base_salary))
        

emp1 = employe(1, "Hicham", "EE127854", 10000, 15 ,8500 )
emp2 = employe(2, "Fatima", "EE109214", 7052, 12 ,7800 )
emp3 = employe(3, "Hassan", "EE038198", 6940, 10 ,7300 )

emp1.info()
emp2.info()
emp3.info()
