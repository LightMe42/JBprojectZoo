deposit = int(input())
counter = 0
while deposit < 700000:
    deposit = deposit * 0.071 + deposit
    counter += 1
print(counter)
