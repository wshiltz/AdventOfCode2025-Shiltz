def checkAccess(data, i, j):
    count = 0
    
    for iMod in [-1, 0, 1]:
        for jMod in [-1, 0, 1]:
            iValid = i + iMod >= 0 and i + iMod < len(data)
            jValid = j + jMod >= 0 and j + jMod < len(data[i])
            if not (iMod == 0 and jMod == 0) and iValid and jValid:
                if data[i+iMod][j+jMod] == "@":
                    count += 1
            if count >= 4:
                return False
    
    return True             

def main():
    with open("test.txt", "r") as file:
        data = [list(line.strip()) for line in file.readlines()]
        
    removedRolls = 0
    while True:
        accessableRolls = 0
        newData = data
        for i in range(len(data)):
            for j in range(len(data[i])):
                if data[i][j] == "@" and checkAccess(data, i, j):
                    accessableRolls += 1
                    removedRolls += 1
                    newData[i][j] = "."
        data = newData
        
        if accessableRolls == 0:
            break
    
    print(removedRolls)
    
if __name__ == "__main__":
    main()