from collections import deque
#NOT SOLVED
elf_energy = deque(int(x) for x in input().split())
num_of_materials = deque(int(x) for x in input().split())
toys = 0
times_counter = 0
THIRD_DAYS = 2
FIFTH_DAYS = None
used_energy = 0

while elf_energy and num_of_materials:
    curr_energy = elf_energy.popleft()
    curr_material = num_of_materials.pop()
    times_counter += 1

    if curr_energy < 5:
        num_of_materials.appendleft(curr_material)
        continue

    if times_counter % 3 == 0:
        if curr_energy >= curr_material * 2:
            toys += 2
            curr_energy -= curr_material
            used_energy -= curr_material
            curr_energy += 1
            elf_energy.append(curr_energy)
            if times_counter % 5 == 0:
                toys -= 2
        elif curr_energy < curr_material * 2:
            curr_energy *= 2
            elf_energy.append(curr_energy)
            num_of_materials.appendleft(curr_material)
        continue

    if times_counter % 5 == 0:
        if curr_energy >= curr_material:
            curr_energy -= curr_material
            used_energy -= curr_material
            elf_energy.append(curr_energy)
        elif curr_energy < curr_material:
            curr_energy *= 2
            elf_energy.append(curr_energy)
            num_of_materials.appendleft(curr_material)
        continue



    if times_counter % 3 != 0 and times_counter % 5 != 0 and curr_energy >= curr_material:
        toys += 1
        curr_energy -= curr_material
        used_energy -= curr_material
        curr_energy += 1
        elf_energy.append(curr_energy)

    elif curr_energy < curr_material:
        curr_energy *= 2
        elf_energy.append(curr_energy)
        num_of_materials.appendleft(curr_material)




print(f"Toys: {toys}")
print(f"Energy: {abs(used_energy)}")
print(f"Elves left: {elf_energy}")

