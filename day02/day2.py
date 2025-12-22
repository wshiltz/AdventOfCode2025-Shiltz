import re

def checkValid(codeString, increments):
    valid = True
    
    for increment in increments[len(codeString)]:
        splitString = [codeString[i:i+increment] for i in range(0, len(codeString), increment)]
        if splitString.count(splitString[0]) == len(splitString):
            valid = False
            
    return valid

def main():
    with open("input.txt", "r") as file:
        data = re.split(",", file.readline())
        
    codes = []
    for idRange in data:
        idRange = re.split("-", idRange)

        for num in range(int(idRange[0]), int(idRange[1])+1):
            codes.append(num)
            print()
            
    invalidCount = 0
    increments = {}
    for code in codes:
        codeString = str(code)
        if len(codeString) not in increments.keys():
            increments[len(codeString)] = []
            for increment in range(1, (len(codeString)//2)+1):
                if len(codeString) % increment == 0:
                    increments[len(codeString)].append(increment)
        
        if not checkValid(codeString, increments):
            invalidCount += code
                
    print(invalidCount)

if __name__ == "__main__":
    main()
import re

def checkValid(codeString, increments):
    valid = True
    
    for increment in increments[len(codeString)]:
        splitString = [codeString[i:i+increment] for i in range(0, len(codeString), increment)]
        if splitString.count(splitString[0]) == len(splitString):
            valid = False
            
    return valid

def main():
    with open("input.txt", "r") as file:
        data = re.split(",", file.readline())
        
    codes = []
    for idRange in data:
        idRange = re.split("-", idRange)

        for num in range(int(idRange[0]), int(idRange[1])+1):
            codes.append(num)
            
    invalidCount = 0
    increments = {}
    for code in codes:
        codeString = str(code)
        if len(codeString) not in increments.keys():
            increments[len(codeString)] = []
            for increment in range(1, (len(codeString)//2)+1):
                if len(codeString) % increment == 0:
                    increments[len(codeString)].append(increment)
        
        if not checkValid(codeString, increments):
            invalidCount += code
                
    print(invalidCount)

if __name__ == "__main__":
    main()