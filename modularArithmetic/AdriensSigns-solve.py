import crypty

a = 288260533169915
p = 1007621497415251
a_inv = crypty.getMultiplicativeInverse(a, p)

def readInput(filePath):
    l = []
    for line in open(filePath, "rt"):
        line = line.replace("\n", "").replace("[", "").replace("]", "")
        line = line.split(", ")
        l = line
        break
    
    for i in range(len(l)):
        l[i] = int(l[i])
    return l

def main():
    filePath = "AdriensSigns-output.txt"
    ciphertext = readInput(filePath)

if __name__ == "__main__":
    main()