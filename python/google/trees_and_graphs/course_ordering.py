def is_halfway(current_course, prereqs_courses):

    graph = {}
    for pair in prereqs_courses:
        graph[pair[0]] = pair[1]

    visited = set()
    stack = []

    for node in graph.keys():
        if node not in visited:
            dfs(node, graph, stack, visited)
    topological_ordering = stack[::-1]
    total_count = len(topological_ordering)
    counter = 1
    for i in range(total_count):
        if current_course == stack[i]:
            break
        counter += 1

    return (counter / float(total_count)) >= 0.5

def dfs(node, graph, stack, visited):
    if node not in graph:
        stack.append(node)
        visited.add(node)
    else:
        if node not in visited:
            dfs(graph[node], graph, stack, visited)
            stack.append(node)
            visited.add(node)

prereqs_courses = [
    ["Data Structures", "Algorithms"],
    ["Foundations of Computer Science", "Operating Systems"],
    ["Computer Networks", "Computer Architecture"],
    ["Algorithms", "Foundations of Computer Science"],
    ["Computer Architecture", "Data Structures"],
    ["Software Design", "Computer Networks"]
]

print is_halfway("Data Structures", prereqs_courses)