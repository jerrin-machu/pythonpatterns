n =5
string = ""
for i in range(0,n):
    for j in range(0,i):
        string = string + " "
    for k in range((n-i)*2 -1, 0, -1):
        string = string + "*"
    string = string + "\n"
for i in range(2,n+1):
    for j in range(n,i,-1):
        string = string + " "
    for k in range(0, 2*i -1):
        string  = string + "*"
    string = string + "\n"

print(string)
