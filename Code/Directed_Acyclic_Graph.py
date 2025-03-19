#!/usr/bin/env python3


def sort_graph(unsorted_graph):
    sorted_graph = {}
    sorted_graph = {x: unsorted_graph[x] for x in sorted(unsorted_graph.keys())}
    sorted_graph = {x: sorted(sorted_graph[x]) for x in sorted_graph.keys()}
    result = sorted_graph
    return result


def sort_path(unsorted_path):
    sorted_path = []
    sorted_path = sorted(unsorted_path)
    result = sorted_path
    return result


def validate_input(input_graph, input_path):
    exception1 = "Path does not look correct"
    exception2 = "Should have 2 elements"
    exception3 = "Both elements should be part of graph keys"

    if len(input_path) != 2:
        raise Exception(f"{exception1} -> {exception2} ..")

    input_graph_keys = input_graph.keys()
    if not (
        (input_path[0] in input_graph_keys) and (input_path[1] in input_graph_keys)
    ):
        raise Exception(f"{exception1} -> {exception3} ..")


def find_paths(my_graph, my_path):
    print(f"Graph: {my_graph}")
    print(f"Path: {my_path}")

    start, end = my_path
    my_paths = []

    def dfs(current_node, path):
        # Add the current node to the path
        path.append(current_node)

        # If the current node is the end node, add the path to the result
        if current_node == end:
            my_paths.append(path.copy())
        else:
            # Recursively visit all adjacent nodes
            for neighbor in my_graph[current_node]:
                dfs(neighbor, path)

        # Backtrack: Remove the current node from the path
        path.pop()

    # Start DFS from the start node
    dfs(start, [])

    result = my_paths
    return result


if __name__ == "__main__":
    # pass
    # print("Test")

    graph = {0: [2, 1, 4], 2: [3], 1: [3], 3: [], 4: [3]}

    graph = sort_graph(graph)
    # print(my_graph)
    # for item, val in my_graph.items():
    #     print(item, val)

    path = [0, 3]
    path = sort_path(path)

    validate_input(graph, path)

    paths = find_paths(graph, path)
    print(f"Paths: {paths}")
