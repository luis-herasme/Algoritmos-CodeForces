from collections import defaultdict
import sys
input = sys.stdin.readline


t = int(input())
tasks_list = [None] * t

for i in range(t):
    input() # n
    tasks_list[i] = input() 
    
for tasks in tasks_list:
    prev_solved_task = "0"
    task_solved = defaultdict(lambda: 0)
    valid = True

    for task in tasks:
        if task != prev_solved_task:
            prev_solved_task = task
            
            if task_solved[task]:
                print("NO")
                valid = False
                break
            else:
                task_solved[task] = 1
        
    if valid:
        print("YES")
    
