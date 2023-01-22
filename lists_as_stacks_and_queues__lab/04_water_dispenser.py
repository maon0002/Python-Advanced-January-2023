from _collections import deque

water_liters = int(input())
persons_que = deque()
START_COMMAND = 'Start'
END_COMMAND = 'End'

while True:
    command = input()
    if command == START_COMMAND:
        break
    else:
        name = command
        persons_que.append(name)

while True:
    second_command = input().split(' ')
    current_command = second_command[0]
    if current_command == END_COMMAND:
        print(f'{water_liters} liters left')
        break

    if current_command.isdigit():
        person_needed_liters = int(current_command)
        current_person = persons_que.popleft()
        if water_liters >= person_needed_liters:
            print(f'{current_person} got water')
            water_liters -= person_needed_liters
        else:
            print(f'{current_person} must wait')
    elif second_command[0] == 'refill':
        refill_with = int(second_command[1])
        water_liters += refill_with


