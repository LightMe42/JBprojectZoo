# put your python code here
group1 = int(input())
group2 = int(input())
group3 = int(input())
desks = group1 // 2 + group2 // 2 + group3 // 2
desks += group1 % 2 + group2 % 2 + group3 % 2
print(desks)
