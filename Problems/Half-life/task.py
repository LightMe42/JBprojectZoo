atoms = int(input())
final_q = int(input())
hf = 0
while atoms > final_q:
    atoms = atoms // 2
    hf += 12
print(hf)
