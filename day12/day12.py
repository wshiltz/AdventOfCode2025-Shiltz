def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
    
    currentShape = 0
    sizes = []
    trees = []
    for line in data:
        if line == "":
            continue
        elif line[1] == ":":
            currentShape = int(line[0])
            sizes.append(0)
        elif line[0] == "#" or line[0] == ".":
            sizes[currentShape] += line.count("#")
        else:
            line = line.split()
            area = line[0].split("x")
            area = int(area[0]) * int(area[1][:-1])
            
            trees.append((line[1:], area))
    
    validTrees = 0
    for tree in trees:
        presentsArea = 0
        for i in range(len(tree[0])):
            presentsArea += sizes[i] * int(tree[0][i])
            
        if presentsArea <= tree[1]:
            validTrees += 1
            
    print("Note: The following solution takes advantage of the fact that the input does not require finding optimal shape placements and can be solved by just calculating the total optimal area of eachs shape.")
    print(f"Valid Trees: {validTrees}")
            
    
if __name__ == "__main__":
    main()