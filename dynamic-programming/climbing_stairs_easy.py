# Climbing Stairs - Easy
# Count ways to climb n stairs (1 or 2 steps at a time)

def climb_stairs(n):
    if n <= 2:
        return n
    a, b = 1, 2
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b
