n=5
string = ""
for i in range (1,n+1):
    for j in range(n,i,-1):
        string = string + " "
    for k in range(0, 2*i-1):
        if k == 0 or  k == (2*i) - 2 :
            string = string + "*"
        else:
            string = string + " "
    string = string + "\n"

for i in range(1,n+1):
    for j in range(0,i):
        string = string + " "
    for k in range((n-i)*2 -1, 0, -1):
        if k == (n-i)*2 -1 or k == 1:
            string = string + "*"
        else:
            string = string + " "
    string = string + "\n"

print(string)
