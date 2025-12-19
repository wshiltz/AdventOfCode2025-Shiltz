import re

def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
        
    fresh = []
    ingredients = []
    for line in data:
        if "-" in line:
            fresh.append(re.split("-", line))
        elif line != "":
            ingredients.append(int(line))
            
        fresh = [(int(x[0]), int(x[1])) for x in fresh]
        fresh = sorted(fresh, key=(lambda x: x[0]))
        
    newFreshRange = []
    i = 0
    while(i < len(fresh)-1):
        start = fresh[i][0]
        end = fresh[i][1]
        
        while(i+1 < len(fresh) and fresh[i+1][0] <= end+1):
            if fresh[i+1][1] > end:
                end = fresh[i+1][1]
            i += 1
        
        newFreshRange.append((start, end))
        i += 1

    freshIds = 0
    for freshRange in newFreshRange:
        freshIds += (freshRange[1] - freshRange[0] + 1)
        
               
    freshIngredients = 0
    for ingredient in ingredients:
        for freshRange in fresh: 
            if ingredient >= freshRange[0] and ingredient <= freshRange[1]:
                freshIngredients += 1
                break
            
    print(f"Fresh Ingredients: {freshIngredients}")
    print(f"Total Unique Fresh IDs: {freshIds}")
    
if __name__ == "__main__":
    main()