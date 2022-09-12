n=5
string = ""
for i in range(1, n+1):
    for j in range(1,n-i+1):
        string = string + " "
    for k in range(0,2*i -1):
        if i == 1 or i == n :
            string = string + "*"
        else:
            if k == 0 or k == 2*i - 2:
                string = string + "*"
            else:
                string = string + " "
    string = string + "\n"


print(string)
