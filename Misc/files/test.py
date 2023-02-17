from collections import deque

q = deque()

for i in range(0,10):
    q.append(1)

print(q)
q.append(7)
q.popleft()
print(q)
print(sum(q))
