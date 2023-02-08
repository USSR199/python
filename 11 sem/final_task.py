#f(x) = -12x^4*sin(cos(x)) - 18x^3+5x^2 + 10x - 30

#Определить корни

#Найти интервалы, на которых функция возрастает

#Найти интервалы, на которых функция убывает

#Построить график

#Вычислить вершину

#Определить промежутки, на котором f > 0

#Определить промежутки, на котором f < 0

from sympy import *
from sympy.plotting import plot

x = sympy.Symbol('x')
f = -12*(x**4)*sin(cos(x)) - 18*x**3 + 5*x**2 + 10*x - 30

k = sympy.solve(f, x)
print('Корни уравнения =>')
print(k)

diff = sympy.diff(f, x)

print('Интервалы, на которых функция возрастает =>')
print(sympy.solve(diff > 0, x))

print('Интервалы, на которых функция убывает =>')
print(sympy.solve(diff < 0, x))

sympy.plotting.plot(f)

print('Вершина(ы) =>')
print(sympy.solve(diff, x))

print('Промежутки, на которых f > 0 =>')
print(sympy.solve(f > 0, x))

print('Промежутки, на которых f < 0 =>')
print(sympy.solve(f < 0, x))
