input_line = input()
l = input_line.split()
sum = 0
for i in range(len(l)):
    sum += int(l[i])
print(sum)
