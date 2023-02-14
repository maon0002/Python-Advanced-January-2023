from collections import deque

eggs = deque(int(x) for x in input().split(", "))
paper = list(int(x) for x in input().split(", "))

BOX = 50
wrapped_eggs = 0
while eggs and paper:
    first_egg = eggs.popleft()
    last_paper = paper.pop()
    if first_egg == 13:
        paper.append(last_paper)
        paper[0], paper[-1] = paper[-1], paper[0]
        continue
    elif first_egg <= 0:
        paper.append(last_paper)
        continue
    if last_paper + first_egg <= BOX:
        wrapped_eggs += 1
        continue

if wrapped_eggs:
    print(f"Great! You filled {wrapped_eggs} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join(str(e) for e in eggs)}')
if paper:
    print(f'Pieces of paper left: {", ".join(str(p) for p in paper)}')