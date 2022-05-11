import math
inp = input().split()

m = math.ceil(int(inp[0])/int(inp[-1]))
n = math.ceil(int(inp[1])/int(inp[-1]))
result = m * n
print(result)

