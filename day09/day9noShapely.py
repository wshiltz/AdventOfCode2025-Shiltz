### THIS FILE IS UNFINISHED ###

# My initial attempt at day 9 involved manually calculating where the boundaries
# of the shape are and attempting to use the bounds to verify if a certain rectangle
# is valid. After many unsuccessful attempts, I discovered the Shapely library 
# and used that to solve day 9, but wanted to archive my original attempt
# so that I could possibly finish it in the future.

def isValid(point, tiles, xyDict, yxDict):
    if point in tiles: 
        return True
    else:
        condition1, condition2, condition3, condition4 = False, False, False, False
        
        condition1 = point[0] in xyDict.keys() and min(xyDict[point[0]]) < point[1]
        condition2 = point[0] in xyDict.keys() and max(xyDict[point[0]]) > point[1]
        condition3 = point[1] in yxDict.keys() and min(yxDict[point[1]]) < point[0]
        condition4 = point[1] in yxDict.keys() and max(yxDict[point[1]]) > point[0]
        
        # for tile in tiles:
        #     if tile[0] == point[0] and tile[1] > point[1]:
        #         condition1 = True
        #     elif tile[0] == point[0] and tile[1] < point[1]:
        #         condition2 = True
        #     elif tile[1] == point[1] and tile[0] > point[0]:
        #         condition3 = True
        #     elif tile[1] == point[1] and tile[0] < point[0]:
        #         condition4 = True
                
        if condition1 and condition2 and condition3 and condition4:
            return True
            
    return False

def main():
    with open("test.txt", "r") as file:
        data = [line.strip().split(",") for line in file.readlines()]
        
    redTiles = []
    for point in data:
        redTiles.append((int(point[0]), int(point[1])))
       
    # Create green tiles between red tiles  
    greenTiles = []
    for i in range(len(redTiles)):
        point = redTiles[i]
        if i+1 >= len(redTiles):
            nextPoint = redTiles[0]
        else:
            nextPoint = redTiles[i+1]
            
        if point[0] == nextPoint[0]:
            if point[1] > nextPoint[1]:
                for j in range(nextPoint[1]+1, point[1]):
                    greenTiles.append((point[0], j))
            else:
                for j in range(point[1]+1, nextPoint[1]):
                    greenTiles.append((point[0], j))
        else:
            if point[0] > nextPoint[0]:
                for j in range(nextPoint[0]+1, point[0]):
                    greenTiles.append((j, point[1]))
            else:
                for j in range(point[0]+1, nextPoint[0]):
                    greenTiles.append((j, point[1]))
                    
    # Add green tiles between other green tiles
    xyDict = {}
    for point in (redTiles + greenTiles):
        if point[0] in xyDict.keys():
            xyDict[point[0]].append(point[1])
        else:
            xyDict[point[0]] = [point[1]]
            
    yxDict = {}
    for point in (redTiles + greenTiles):
        if point[1] in yxDict.keys():
            yxDict[point[1]].append(point[0])
        else:
            yxDict[point[1]] = [point[0]]
        
    areas = []
    count = 0
    for point1 in redTiles:
        for point2 in redTiles: 
            count += 1
            
            xdist = abs(point2[0] - point1[0]) + 1
            ydist = abs(point2[1] - point1[1]) + 1
            
            if len(areas) <= 1 or (xdist * ydist) > max(areas):
                if isValid((point1[0], point2[1]), (greenTiles+redTiles), xyDict, yxDict) and isValid((point2[0], point1[1]), (greenTiles+redTiles), xyDict, yxDict):
                    areas.append(xdist * ydist)
          
    print(f"Max Area: {max(areas)}")
    
if __name__ == "__main__":
    main()