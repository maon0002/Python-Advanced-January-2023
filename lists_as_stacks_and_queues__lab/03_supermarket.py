from _collections import deque

person_deque = deque()

END_COMMAND = 'End'
PAID_COMMAND = 'Paid'

while True:
    command = input()

    if command == PAID_COMMAND:
        while person_deque:
            print(person_deque.popleft())
    elif command == END_COMMAND:
        print(f'{len(person_deque)} people remaining.')
        break
    else:
        person_deque.append(command)
