import re
import pulp
    
def main():
    with open("input.txt", "r") as file:
        data = [line.strip().split(" ") for line in file.readlines()]
    
    allLights = []
    allButtons = []
    allJolts = []
    for line in data:
        allLights.append(list(line[0][1:-1]))
        
        tempJolts = line[len(line)-1].split(",")
        tempJolts[0] = tempJolts[0][1:]
        tempJolts[len(tempJolts)-1] = tempJolts[len(tempJolts)-1][:-1]
        tempJolts = [int(i) for i in tempJolts]
        
        allJolts.append(tempJolts)
        
        tempButtons = []
        for i in range(1, len(line)-1):
            tempButtons.append(re.findall("[0-9]", line[i]))
        
            tempButtons[i-1] = [int(j) for j in tempButtons[i-1]]
        
        allButtons.append(tempButtons)
        
    leastButtonsLights = []   
    leastButtonsJolts = [] 
    for i in range(len(data)):
        print(f"Progress: {i+1}/{len(data)}")
        
        lights = allLights[i]
        buttons = allButtons[i]
        jolts = allJolts[i]
        
        queue = []
        visited = []
        for action in buttons:
            result = ["." for j in range(len(lights))]
            for num in action:
                if result[num] != "#":
                    result[num] = "#"
                else:
                    result[num] = "."
            if result not in visited:
                queue.append((result.copy(), action, 1))
                visited.append(result)
                
        while(len(queue) > 0):
            current = queue.pop(0)
            
            if current[0] == lights:
                leastButtonsLights.append(current[2])
                break
            
            for action in buttons:
                if action != current[1]:
                    result = current[0].copy()
                    for num in action:
                        if result[num] != "#":
                            result[num] = "#"
                        else:
                            result[num] = "."
                    if result not in visited:
                        queue.append((result.copy(), action, current[2]+1))
                        visited.append(result)
        
        currentProblem = pulp.LpProblem(f"Problem {i+1}", pulp.LpMinimize)
        vars = pulp.LpVariable.dicts("button", [j for j in range(len(buttons))], lowBound=0, cat="Integer")
        
        for j in range(len(jolts)):
            expression = 0
            for k in range(len(buttons)):
                expression += (vars[k] * buttons[k].count(j))
                
            currentProblem += expression == jolts[j]
        
        objective = 0
        for j in range(len(buttons)):
            objective += vars[j]
            
        currentProblem += objective
        currentProblem.solve(pulp.PULP_CBC_CMD(msg=0))
        
        leastButtonsJolts.append(int(pulp.value(currentProblem.objective)))

    print(f"Sum of Fewest Button Presses for Lights: {sum(leastButtonsLights)}")
    print(f"Sum of Fewest Button Presses for Jolts: {sum(leastButtonsJolts)}")
    
if __name__ == "__main__":
    main()