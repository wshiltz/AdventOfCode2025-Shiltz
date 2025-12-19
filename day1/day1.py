def main():
    DEBUG = False
    
    with open("input.txt", "r") as file:
        data = [line.strip() for line in file.readlines()]
        
    location = 50
    zeroCount = 0
    
    for line in data:
        steps = int(line[1:])
        direction = line[0]
        
        if DEBUG:
            print(f"START: {location}")
            print(f"STEPS: {steps}")
        
        if direction == "L":
            zeroCount += abs((location - steps) // 100)
            if location == 0:
                zeroCount -= 1
            location = (location - steps) % 100
            if location == 0:
                zeroCount += 1
            
        elif direction == "R":
            zeroCount += (location + steps) // 100
            location = (location + steps) % 100
            
        if DEBUG:
            print(f"ZERO PASSES: {zeroCount}")
            print(f"END: {location}\n")
            
    print(f"Final Zero Passes: {zeroCount}")
    
if __name__ == "__main__":
    main()