# import numpy as np

customers = ['James', 'John', 'Robert', 'Mary', 'Patricia', 'Jennifer']
salary = [155000, 755000,  455000, 1255000, 635000, 575000]
taxes = [55800, 317100, 182000, 451800, 171450, 71400]

perc = [(i / j)*100 for i, j in zip(taxes, salary)]

for h, i, j in zip(perc, salary, customers):
    if i > 555000 and h < 30:
        print(j)

