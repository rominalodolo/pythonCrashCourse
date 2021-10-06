#Passing an Arbitrary Number of Arguments

def make_pizza(*toppings):
"""Print the list of toppings that have been requested."""
print(toppings)
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

('pepperoni',)
('mushrooms', 'green peppers', 'extra cheese')

def make_pizza(*toppings):
"""Summarize the pizza we are about to make."""
print("\nMaking a pizza with the following toppings:")
for topping in toppings:
print(f"- {topping}")
make_pizza('pepperoni')
make_pizza('mushrooms', 'green peppers', 'extra cheese')

# Making a 16-inch pizza with the following toppings:
# - pepperoni
# Making a 12-inch pizza with the following toppings:
# - mushrooms
# - green peppers
# - extra cheese

