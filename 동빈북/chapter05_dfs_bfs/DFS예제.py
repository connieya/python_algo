# DFS 메서드 정의
def dfs(graph , start , visited):
    # 햔재 노드르 방문 처리
    visited[start] = True
    print(start, end =' ')
    # 현재 노드와 연결된 다른 노드르 재귀적으로 방문
    for i in graph[start]:
        if not visited[i]:
            dfs(graph,i,visited)

# 각 노드가 연결된 정보를 리스트 자료형으로 표현 (2차원 리스트)
graph = [
    [],
    [2,3,8],
    [1,7,8],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,7,8],
    [1,7]
]

# 각 노드가 방문된 정보를 리스트 자료형으로 표현 (1차원 리스트)
visited = [False] * 9

# 정의된 DFS 함수 호출
dfs(graph , 1, visited)