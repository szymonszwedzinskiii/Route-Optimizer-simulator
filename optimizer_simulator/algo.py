
def find_best_path(matrix,start = 0):
    n = len(matrix)
    visited = [False] * n
    path = [start]
    visited[start] = True
    current = start

    for _ in range(n-1):
        next_point = None
        min_dist = float('inf')

        for i in range(n):
            if not visited[i] and matrix[current][i] < min_dist:
                min_dist = matrix[current][i]
                next_point = i


        path.append(next_point)
        visited[next_point] = True
        current = next_point

    return path

