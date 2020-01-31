#! python3

# Functional programming is all about separation of concerns
# Each part concerns itself with the part it's really good at
# Unlike OOP where data and functionality is combined in properties and methods
# functional programming passes data through pure functions that do one thing really well
# But in the end the goals are the same as OOP and both ar not mutually exclusive

# 1   Clear & understandible
# 2   Extendable
# 3   Maintainable
# 4   Efficient
# 5   DRY

# Prime Pillar of Functional Programming is
# -------------- PURE FUNCTION ------------

# Pure function given same input will ALWAYS return same output
# Pure functions should NEVER produce any side-effects (does it interact with the outside world beyond the scope of the pure function)

# [1,2,3]   ->   Function   ->   [2,3,4]

def multiply_by2(li):
  new_list = []
  for item in li:
    new_list.append(item * 2)
  return new_list

print(multiply_by2([1,2,3]))