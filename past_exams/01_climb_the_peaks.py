from collections import deque

food_qty = list(int(x) for x in input().split(", "))
stamina_qty = deque(int(x) for x in input().split(", "))
peaks_dict = {
    0: ['Vihren', 80, 0],
    1: ['Kutelo', 90, 0],
    2: ['Banski Suhodol', 100, 0],
    3: ['Polezhan', 60, 0],
    4: ['Kamenitza', 70, 0],
}
days = -7
peak_number = 0
all_climbed = None

# all_not_climbed = all([False if peak[2] else True for peak in peaks_dict.values()])
# while food_qty and stamina_qty and days and not all_climbed:
while days and not all_climbed:
    days += 1
    curr_food = food_qty.pop()
    curr_stamina = stamina_qty.popleft()
    curr_strength = curr_stamina + curr_food
    curr_peak_difficulty = peaks_dict[peak_number][1]

    if curr_strength >= curr_peak_difficulty:
        peaks_dict[peak_number][2] = 1
        peak_number += 1

    elif curr_strength < curr_peak_difficulty:
        continue

    all_climbed = all([True if peak[2] else False for peak in peaks_dict.values()])

any_climbed = any([True if peak[2] else False for peak in peaks_dict.values()])
# print(food_qty)
# print(stamina_qty)
# print(peaks_dict)
# print(all_climbed)
# # print(all_not_climbed)
# print(any_climbed)

if all_climbed:
    print("Alex did it! He climbed all top five Pirin peaks in one week -> @FIVEinAWEEK")
else:
    print("Alex failed! He has to organize his journey better next time -> @PIRINWINS")

if any_climbed:
    print("Conquered peaks:")
    for vals in peaks_dict.values():
        if vals[2] == 1:
            peak_name = vals[0]
            print(peak_name)
