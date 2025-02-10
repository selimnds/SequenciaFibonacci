num = int(input("Quantas vezes você deseja que a sequência se repita? "))
fnacci = [1 , 1]

for n in range(num):
    fnacci.append(fnacci[-2] + fnacci[-1])
print(fnacci)
