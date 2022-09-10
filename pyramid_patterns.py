n=5
string = ""
for i in range(1, n+1):
    for j in range(0,n-i+1):
        string = string + " "
    for k in range(0,(2*i) - 1):
        string = string + "*"
    string = string + "\n"

print(string)
