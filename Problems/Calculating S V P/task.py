# put your python code here
length = int(input())
width = int(input())
height = int(input())
edges = 4 * (length + width + height)
surface = 2 * (length * width + width * height + length * height)
volume = length * width * height
print(edges)
print(surface)
print(volume)
