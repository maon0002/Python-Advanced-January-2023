from collections import deque

seats = [x for x in input().split(", ")]
first_seq = deque(int(x) for x in input().split(", "))
second_seq = deque(int(x) for x in input().split(", "))
MATCHES_CONDITION = 3
ROTATION_CONDITION = 10
rotations = 0
seat_matches = 0
matched_seat_list = []

while rotations < ROTATION_CONDITION and seat_matches < MATCHES_CONDITION:
    first_n = first_seq.popleft()
    last_n = second_seq.pop()
    char = chr(first_n + last_n)
    seat_one = str(first_n) + char
    seat_two = str(last_n) + char
    rotations += 1
    if seat_one in seats:
        seats.remove(seat_one)
        matched_seat_list.append(seat_one)
        second_seq.appendleft(last_n)
        seat_matches += 1
    elif seat_two in seats:
        seats.remove(seat_two)
        matched_seat_list.append(seat_two)
        first_seq.append(first_n)
        seat_matches += 1
    else:
        first_seq.append(first_n)
        second_seq.appendleft(last_n)

print(f"Seat matches: {', '.join(matched_seat_list)}")
print(f"Rotations count: {rotations}")
