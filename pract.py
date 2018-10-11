s=[['1','2'],[' 2','3']]

for i in range(0,2):
    for j in range(0,2):
        s[i][j]=int(s[i][j])

print(s)
print(s[0][0]+s[1][0])
print(len(s))