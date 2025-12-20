import shapely

def main():
    with open("input.txt", "r") as file:
        data = [line.strip().split(",") for line in file.readlines()]
        
    redTiles = []
    for point in data:
        redTiles.append((int(point[0]), int(point[1])))
    
    boundaryShape = shapely.Polygon((redTiles + [redTiles[0]]))
        
    areas = []
    for point1 in redTiles:
        for point2 in redTiles:
            xdist = abs(point2[0] - point1[0]) + 1
            ydist = abs(point2[1] - point1[1]) + 1
            
            areas.append(([point1, point2], xdist * ydist))
          
    areas = sorted(areas, key=lambda x: x[1], reverse=True)
    
    print(f"Checking Area Validity...")
    
    largestValidArea = 0
    for i in range(len(areas)):
        corners = [areas[i][0][0], areas[i][0][1], [areas[i][0][0][0], areas[i][0][1][1]], [areas[i][0][1][0], areas[i][0][0][1]], areas[i][0][0]]
        rectangle = shapely.LineString(corners)
        
        if boundaryShape.covers(rectangle):
            largestValidArea = areas[i][1]
            break
        
    print(f"Max Area: {largestValidArea}")
    
if __name__ == "__main__":
    main()