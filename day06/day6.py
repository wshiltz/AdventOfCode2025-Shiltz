import math

# Parts have seperate functions because of how different they are
def part1():
    with open("input.txt", "r") as file:
        data = [line.strip().split() for line in file.readlines()]
        
    finalSum = 0
    mathSymbols = data.pop()
    for i in range(len(mathSymbols)):
        if mathSymbols[i] == "+":
            result = 0
            for numbers in data:
                result += int(numbers[i])
        else:
            result = int(data[0][i])
            for j in range(1, len(data)):
                result *= int(data[j][i])  
                
        finalSum += result
        
    print(f"Final Result: {finalSum}")  
            
def part2():    
    with open("input.txt", "r") as file:
        data = [line.replace("\n", "") for line in file.readlines()]
    
    columns = []
    for i in range(len(data[0])):
        columns.append([])
        for j in range(len(data)):
            columns[i].append(data[j][i].strip())
    columns.append(["", "", "", "", ""])
    
    result = 0
    nums = []
    operation = ""
    for column in columns:
        if column == ['', '', '', '', '']:
            if operation == "*":
                result += math.prod(nums)
            else:
                result += sum(nums)
                
            operation = ""
            nums = []
        else:
            if (column[0] + column[1] + column[2] + column[3]) != "":
                nums.append(int(column[0] + column[1] + column[2] + column[3]))
            operation += column[4] 
            
    print(f"Final Result: {result}") 
    
        
if __name__ == "__main__":
    part2()