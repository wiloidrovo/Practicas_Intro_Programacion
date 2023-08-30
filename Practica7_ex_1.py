n = 0
while (n < 2):
    try:
        n = int(input('Enter the number of elements: '))
        if (n < 2):
            print('It must be an integer greater than 1')
    except:
        print('It must be an integer')
X = []
for i in range(n+1):
    y = int(input("Enter any integer number for the list: "))
    X.append(y)
print("Your initial list is:", X)
# Apply procedure
for k in range(n):
    max = X[0]
    id_max = 0
    for i in range((n+1) - k):
        if (X[i] > max):
            max = X[i]
            id_max = i
    for j in range(id_max + 1, ((n+1) - k)):
        X[j - 1] = X[j]
    X[n - k] = max
#X = X[:-1] #Adjust the len of the list
#print("max =", max)
#print("id_max =", id_max)
print("Your sorted list is:", X)