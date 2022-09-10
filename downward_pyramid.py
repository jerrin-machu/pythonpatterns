n =6
string = ""

for i in range(1,n+1):
    for j in range(0,i):
        string = string + " "
    for k in range(0,(2*(n-i))-1):
        string = string + "*"
    string = string + "\n"
print(string)