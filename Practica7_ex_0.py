# Read n 
n = 0
while (n < 2):
    try:
        n = int(input('n = '))
        if (n < 2):
            print('n must be an integer greater than 1')
    except:
        print('n must be an integer')

# Define array
# X = [None]*(n+1)  # An array with n+1 elements (all "None")
X = []              # An empty array

# Assign the value i in position i of the array
for i in range(n+1):
    # X[ii] = ii # if array already have elements
    X.append(i) # if start with an empty array

# Apply procedure
for i in range(2,int(n**(1/2))+1):
    if X[i]==0:
        jump = i*2
        while (jump <= n):
            X[jump] = 0
            jump+=i

# show results
print('[', end="")
for i in range(2,n+1):
    if X[i]:
        print(X[i], ' ',end="")
print(']')