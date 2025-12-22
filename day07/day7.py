def part1():
    with open("input.txt", "r") as file:
        data = [list(line.strip()) for line in file.readlines()]
        
    splits = 0
    for i in range(len(data)):
        for j in range(len(data[i])):
            if i != 0 and (data[i-1][j] == "S" or data[i-1][j] == "|"):
                if data[i][j] == '^':
                    if j-1 >= 0:
                        data[i][j-1] = '|'
                    if j+1 < len(data[i]):
                        data[i][j+1] = '|'
                        
                    splits += 1
                else:
                    data[i][j] = '|'
    
    print(f"Total Splits: {splits}")
    
def part2():
    with open("input.txt", "r") as file:
        data = [list(line.strip()) for line in file.readlines()]
        
    firstSplitter = None
    for i in range(len(data)):
        for j in range(len(data[i])):
            if data[i][j] == "S":
                for k in range(1, len(data)):
                    if data[i+k][j] == "^":
                        firstSplitter = (i+k, j)
                        break
    
    timelinesPerSplitter = {}
    for i in range(len(data)-1, 0, -1):
        for j in range(len(data[i])):
            if data[i][j] == "^":
                timelinesPerSplitter[(i, j)] = 0
                if j-1 >= 0:
                    k = 1
                    while(True):
                        if i+k >= len(data):
                            timelinesPerSplitter[(i, j)] += 1
                            break
                        if data[i+k][j-1] == "^":
                            timelinesPerSplitter[(i, j)] += timelinesPerSplitter[(i+k, j-1)]
                            break
                        k += 1
                if j+1 < len(data[i]):
                    k = 1
                    while(True):
                        if i+k >= len(data):
                            timelinesPerSplitter[(i, j)] += 1
                            break
                        if data[i+k][j+1] == "^":
                            timelinesPerSplitter[(i, j)] += timelinesPerSplitter[(i+k, j+1)]
                            break
                        k += 1

    print(f"Total Timelines: {timelinesPerSplitter[firstSplitter]}")
    
if __name__ == "__main__":
    part2()