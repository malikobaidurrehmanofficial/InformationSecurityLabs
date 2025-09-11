import math

def calculate_perimeter(coordinates):
    """
    Calculate the perimeter of a polygon given a list of coordinate tuples.
    
    Args:
        coordinates: List of tuples representing polygon vertices in order [(x1, y1), (x2, y2), ...]
    
    Returns:
        float: The perimeter of the polygon
    """
    perimeter = 0.0
    n = len(coordinates)
    
  
    for i in range(n):
        x1, y1 = coordinates[i]
        x2, y2 = coordinates[(i + 1) % n]  
        
     
        side_length = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        perimeter += side_length
    
    return perimeter


if __name__ == "__main__":

    square = [(0, 0), (1, 0), (1, 1), (0, 1)]
    print(f"Square perimeter: {calculate_perimeter(square)}") 
    

    triangle = [(0, 0), (3, 0), (1.5, 2)]
    print(f"Triangle perimeter: {calculate_perimeter(triangle)}")
    

    hexagon = [(2, 3), (3, 5), (2, 4), (2, 5), (3, 2), (2, 2)]
    