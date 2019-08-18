i=0
with open('gps_20161101') as f:
    for line1 in f:
        i = i+1 # 每行末尾会有一个换行符

print (i)
print (i*31*2)