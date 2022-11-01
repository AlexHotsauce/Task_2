#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# Завдання 2: Написати програму, котра приймає на вхід матрицю зі значеннями 1 або 0 (живий або
# мертвий стани) та ітеративно замінює значення в матриці за наступними правилами:
# ● якщо в живої клітини два чи три живих сусіди, то вона лишається жити;
# ● якщо в живої клітини один чи немає живих сусідів, то вона помирає від «самотності»;
# ● якщо в живої клітини чотири та більше живих сусідів, то вона помирає від «перенаселення»;
# ● якщо в мертвої клітини рівно три живих сусіди, то вона оживає.
# Кожна клітинка має вісім сусідів.

# Формат відповіді:
# ● Код програми, котра виводить 7-му ітерацію наступного початкового стану:
# [[1,0,0,0,0,0,0],
# [0,0,1,0,0,1,1],
# [1,0,0,1,0,0,1],
# [0,1,1,0,1,1,0],
# [1,1,1,1,0,0,1],
# [1,1,1,1,1,1,1],
# [1,1,0,1,1,0,1]]


# In[ ]:


import pandas as pd
import numpy as np
from random import randint


# In[ ]:


a = [
    [1, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0, 0, 1],
    [0, 1, 1, 0, 1, 1, 0],
    [1, 1, 1, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1],
    [1, 1, 0, 1, 1, 0, 1],
]
n = len(a)
for i in range(n-1):
    for j in range(n-1):
        a[i][j] = a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
        if a[i][j] >= 4 or a[i][j] <=1:
            a[i][j] = 0
        if a[i][j] == 3 or a[i][j] == 2:
            a[i][j] = 1
print(*a, sep='\n')


# In[ ]:


# Завдання 2.1*: Модифікувати програму так, щоб вона випадково генерувала початковий стан матриці з
# заданим розміром і мала можливість безкінечно симулювати ітерації.


# In[ ]:


n = int(input('Enter number of rows: '))
m = int(input('Enter number of columns: '))
a = [[randint(0, 1) for j in range(m)] for i in range(n)]
while True:
    input('Enter any key to generate the matrix: ')
    for i in range(n-1):
        for j in range(n-1):
            a[i][j] = a[i-1][j-1]+a[i-1][j]+a[i-1][j+1]+a[i][j-1]+a[i][j+1]+a[i+1][j-1]+a[i+1][j]+a[i+1][j+1]
            if a[i][j] >= 4 or a[i][j] <= 1:
                a[i][j] = 0
            if a[i][j] == 3 or a[i][j] == 2:
                a[i][j] = 1
    print(*a, sep='\n')


# In[ ]:


# Завдання 2.2**: Візуалізувати симуляцію ітерацій (matplotlib / seaborn / plotly / etc)


# In[ ]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[ ]:


sns.swarmplot(data=a)

