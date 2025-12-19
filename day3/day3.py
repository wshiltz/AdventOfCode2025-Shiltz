def main():
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
    
    totalJolts = 0
    for bank in data:
        batteries = []
        for battery in range(0, len(bank)):
            batteries.append(int(bank[battery]))
            
        numBatteries = 12
        selectedBatteries = []
        while(len(selectedBatteries) < numBatteries):
            if (numBatteries-len(selectedBatteries)-1) == 0:
                selectedBatteries.append(max(batteries))
            else:
                selectedBatteries.append(max(batteries[:-(numBatteries-len(selectedBatteries)-1)]))
            batteries = batteries[batteries.index(selectedBatteries[len(selectedBatteries)-1])+1:]
        
        joltage = ""
        for battery in selectedBatteries:
            joltage += str(battery)
        joltage = int(joltage)
        print(f"Bank: {bank}, Joltage: {joltage}")
        
        totalJolts += joltage
        
    print(f"Total Joltage: {totalJolts}")
    
if __name__ == "__main__":
    main()