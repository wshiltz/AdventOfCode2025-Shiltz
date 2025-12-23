import math

def main():
    with open("input.txt", "r") as file:
        data = [line.strip().split(",") for line in file.readlines()]
        
    for i in range(len(data)):
        data[i] = (int(data[i][0]), int(data[i][1]), int(data[i][2]))
        
    junctionPairs = []
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            if data[i] != data[j]:
                junctionPairs.append(((data[i], data[j]), math.dist(data[i], data[j])))
    junctionPairs = sorted(junctionPairs, key=lambda x: x[1], reverse = True)
    
    circuits = []
    for junction in data:
        circuits.append([junction])
    
    while(len(circuits) > 1):
        pairToAdd = junctionPairs.pop()[0]
        circuit0 = None
        circuit1 = None
        
        for j in range(len(circuits)):
            if pairToAdd[0] in circuits[j] and (not pairToAdd[1] in circuits[j]):
                circuit0 = circuits[j]
            elif pairToAdd[1] in circuits[j] and (not pairToAdd[0] in circuits[j]):
                circuit1 = circuits[j]
                
            if circuit0 and circuit1: 
                break
                
        if circuit0 != circuit1:
            circuit0 += circuit1
            circuits.remove(circuit1)

    print(f"Multipied X Coordinates of Last Connection: {pairToAdd[0][0] * pairToAdd[1][0]}")
    
if __name__ == "__main__":
    main()