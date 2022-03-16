#Minimize :  Z = 3x + 5y
#Subject to the constraints: 
#2x + 3y >= 12
#-x + y <= 3
#x >= 4
#y <= 3
#x, y >= 0

# import the library pulp as p
import pulp as p

# Create a LP Minimization problem
Lp_prob = p.LpProblem('Problem', p.LpMinimize)

# Create problem Variables
x = p.LpVariable("x", lowBound = 0) # Create a variable x >= 0
y = p.LpVariable("y", lowBound = 0) # Create a variable y >= 0

# Objective Function
Lp_prob += 3 * x + 5 * y

# Constraints:
Lp_prob += 2 * x + 3 * y >= 12
Lp_prob += -x + y <= 3
Lp_prob += x >= 4
Lp_prob += y <= 3

# Display the problem
print(Lp_prob)

status = Lp_prob.solve() # Solver
print(p.LpStatus[status]) # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))

# Display the problem
print(Lp_prob)

status = Lp_prob.solve() # Solver
print(p.LpStatus[status]) # The solution status

# Printing the final solution
print(p.value(x), p.value(y), p.value(Lp_prob.objective))


#: First import the library pulp as p.
#: Define the problem by giving a suitable name to your problem, here I have given the name ‘Problem’. Also, specify your aim for the objective function of whether to Maximize or Minimize.
#: Define LpVariable to hold the variables of the objective functions. The next argument specifies the lower bound of the defined variable, i.e. 0, and the upper bound is none by default. You can specify the upper bound too.
#: Denotes the objective function in terms of defined variables.
#: These are the constraints on the variables.
#: This will show you the problem in the output screen.
#: This is the problem solver.
#: Will display the status of the problem.
#: Will print the value for x and y and the minimum value for the objective function.

