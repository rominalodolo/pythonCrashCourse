from employee import Employee 
from sales import Sales
from accounting import Accounting


Employee1 = Sales('Romina', 'Lodolo', 9409050025083, 'lodoloromina@gmail.com', 'Assistant', 'R20 000', 'PTA')
Employee2 = Accounting('Sally', 'Door', 9503190025082, 'sallydoor@hotmail.com', 'CA', 'R50 000', 'CT')
Employee3 = Sales('John', 'Wick', 7012070025083, 'wickyj@gmail.com', 'Intern', 'R6 000', 'Joburg')
Employee4 = Sales('Jane', 'Taz', 9909050025083, 'Janetaz1@gmail.com', 'Manager', 'R40 000', 'Joburg')
Employee5 = Accounting('Willma', 'Cul', 7603190025082, 'CulWilma@hotmail.com', 'CA', 'R50 000', 'PTA')
Employee6 = Accounting('Patty', 'Cake', 8909010025083, 'pattycake@gmail.com', 'Intern', 'R8 000', 'PTA')


Employee1.displayInfo()
Employee2.displayInfo()
Employee3.displayInfo()
Employee4.displayInfo()
Employee5.displayInfo()
Employee6.displayInfo()
