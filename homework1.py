from pulp import LpMaximize, LpProblem, LpVariable, value

model = LpProblem("Maximize_Production", LpMaximize)

lemonade = LpVariable("Lemonade", lowBound=0, cat='Integer')
fruit_juice = LpVariable("FruitJuice", lowBound=0, cat='Integer')

model += 2 * lemonade + 1 * fruit_juice <= 100
model += 1 * lemonade <= 50
model += 1 * lemonade <= 30
model += 2 * fruit_juice <= 40

model += lemonade + fruit_juice

model.solve()

print(int(lemonade.varValue))
print(int(fruit_juice.varValue))
print(int(value(model.objective)))

