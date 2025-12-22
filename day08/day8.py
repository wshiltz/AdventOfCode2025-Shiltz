import math

def main():
    with open("input.txt", "r") as file:
        data = [line.strip().split(",") for line in file.readlines()]
        
    for i in range(len(data)):
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]))
        
    junctionPairs = {}
    for i in range(len(data)):
        for j in range(len(data)):
            if data[i] != data[j] and (not (data[j], data[i]) in junctionPairs.keys()):
                junctionPairs[(data[i], data[j])] = math.dist(data[i], data[j])
    
    circuits = []
    for junction in data:
        circuits.append([junction])
    
    while(len(circuits) > 1):
        print(f"Current Length: {len(circuits)}")
        
        pairToAdd = min(junctionPairs, key=junctionPairs.get)
        circuit0 = None
        circuit1 = None
        
        for j in range(len(circuits)):
            if pairToAdd[0] in circuits[j] and (not pairToAdd[1] in circuits[j]):
                circuit0 = circuits[j]
                index0 = j
            elif pairToAdd[1] in circuits[j] and (not pairToAdd[0] in circuits[j]):
                circuit1 = circuits[j]
                index1 = j
                
        if circuit0 and circuit1:  
            circuit0 += circuit1
            circuits.remove(circuit1)
        elif circuit0:
            circuits[index0].append(pairToAdd[1])
        elif circuit1:
            circuits[index1].append(pairToAdd[0])
            
            
        junctionPairs[pairToAdd] = math.inf
        
    circuits = sorted(circuits, key=lambda x: len(x), reverse=True)

    print(f"Multipied X Coordinates of Last Connection: {pairToAdd[0][0] * pairToAdd[1][0]}")
    
if __name__ == "__main__":
    main()