#     4. Water Dispenser
# Write a program that keeps track of people getting water from a dispenser and the amount of water left at the end.
# On the first line, you will receive the starting quantity of water (integer) in a dispenser. Then, on the following lines, you will be given the names of some people who want to get water (each on a separate line) until you receive the command "Start". Add those people in a queue. Finally, you will receive some commands until the command "End":
#     • "{liters}" - litters (integer) that the current person in the queue wants to get. Check if there is enough water in the dispenser for that person.
#         ◦ If there is enough water, print "{person_name} got water" and remove him/her from the queue.
#         ◦ Otherwise, print "{person_name} must wait" and remove the person from the queue without reducing the water in the dispenser.
#     • "refill {liters}" - add the given litters in the dispenser.
# In the end, print how many liters of water have left in the format: "{left_liters} liters left".


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


