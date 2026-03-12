with open("results.txt", "w") as f:
    for num in range(2, 251):
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            f.write(str(num) + "\n")

print("Números primos guardados en results.txt")