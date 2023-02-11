million = list(range(1, 1_000_001))
#print(million)

print(min(million))
print(max(million))
print(sum(million))

odd_numbers = list(range(1, 21, 2))
print(odd_numbers)

threes = list(range(3, 31, 3))
print(threes)

cubes = []
for cube in range(1, 11):
    cubes.append(cube**3)
print(cubes)

cube_comprehension = [cube**3 for cube in range(1,11)]
print(cube_comprehension)