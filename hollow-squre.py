# * * * * *
# *       *
# *       *
# *       *
# * * * * *

n =5
string = ""

for i in range(0,n):
    for j in range(0,n):
        if i == 0 or i == n-1:
            string = string + "*"
        else:
            if j == 0 or j == n-1:
                string = string + "*"
            else:
                string = string + " "
    string = string + "\n"


print("Printing stars")

print(string)


# * * * * * *
# *