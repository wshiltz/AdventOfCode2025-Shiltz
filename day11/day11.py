def findPathsDFS(servers, goal="out", path=["svr"], numPaths={}): 
    current = path[len(path)-1]
    paths = 0
    
    if current == goal:
        return 1
    
    if current in servers.keys():
        for next in servers[current]:
            if next not in numPaths.keys():
                numPaths[next] = findPathsDFS(servers, goal, path + [next], numPaths)
            paths += numPaths[next]
        
    return paths


def main():
    with open("input.txt", "r") as file:
        data = [line.strip().split() for line in file.readlines()]
        
    servers = {}
    for line in data:
        servers[line[0][:-1]] = line[1:]
    
    paths = findPathsDFS(servers, "dac", ["svr"], {}) * findPathsDFS(servers, "fft", ["dac"]) * findPathsDFS(servers, "out", ["fft"], {})
    paths += findPathsDFS(servers, "fft", ["svr"], {}) * findPathsDFS(servers, "dac", ["fft"], {}) * findPathsDFS(servers, "out", ["dac"], {})
    
    print(f"Total Paths: {paths}")
    
    
if __name__ == "__main__":
    main()