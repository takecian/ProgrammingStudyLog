#!/usr/bin/env python3
"""
Comprehensive tests for tree and graph patterns.
Run with: python test_trees_graphs.py
"""

import sys
import traceback

# Import the modules to test
from tree_traversal import (
    TreeNode, create_tree_from_list,
    preorder_recursive, inorder_recursive, postorder_recursive,
    preorder_iterative, inorder_iterative, postorder_iterative,
    level_order_traversal, zigzag_level_order,
    max_depth, min_depth, is_balanced, diameter_of_tree
)
from binary_search_tree import (
    is_valid_bst, search_bst, insert_into_bst, delete_node_bst,
    kth_smallest_bst, kth_largest_bst, range_sum_bst,
    closest_value_bst, sorted_array_to_bst, trim_bst
)
from graph_algorithms import (
    Graph, dfs_recursive, dfs_iterative, bfs,
    shortest_path_bfs, has_cycle_directed, has_cycle_undirected,
    topological_sort, connected_components, is_bipartite,
    course_schedule
)


def run_test(test_name, test_func):
    """Run a single test and report results."""
    try:
        test_func()
        print(f"✓ {test_name}")
        return True
    except Exception as e:
        print(f"✗ {test_name}: {str(e)}")
        traceback.print_exc()
        return False


def test_tree_traversal():
    """Test tree traversal algorithms."""
    # Create test tree:     1
    #                      / \
    #                     2   3
    #                    / \
    #                   4   5
    root = create_tree_from_list([1, 2, 3, 4, 5])
    
    # Test DFS traversals
    assert preorder_recursive(root) == [1, 2, 4, 5, 3]
    assert inorder_recursive(root) == [4, 2, 5, 1, 3]
    assert postorder_recursive(root) == [4, 5, 2, 3, 1]
    
    # Test iterative versions match recursive
    assert preorder_iterative(root) == preorder_recursive(root)
    assert inorder_iterative(root) == inorder_recursive(root)
    assert postorder_iterative(root) == postorder_recursive(root)
    
    # Test BFS
    assert level_order_traversal(root) == [[1], [2, 3], [4, 5]]
    assert zigzag_level_order(root) == [[1], [3, 2], [4, 5]]
    
    # Test tree analysis
    assert max_depth(root) == 3
    assert min_depth(root) == 2
    assert is_balanced(root) == True
    assert diameter_of_tree(root) == 3  # Path: 4-2-1-3 or 5-2-1-3
    
    # Test edge cases
    assert preorder_recursive(None) == []
    assert max_depth(None) == 0
    assert is_balanced(None) == True


def test_binary_search_tree():
    """Test BST operations."""
    # Create valid BST:     5
    #                      / \
    #                     3   8
    #                    / \ / \
    #                   2  4 7  9
    root = create_tree_from_list([5, 3, 8, 2, 4, 7, 9])
    
    # Test BST validation
    assert is_valid_bst(root) == True
    
    # Test search
    assert search_bst(root, 4).val == 4
    assert search_bst(root, 10) is None
    
    # Test insertion
    root = insert_into_bst(root, 6)
    assert search_bst(root, 6).val == 6
    
    # Test kth smallest/largest
    assert kth_smallest_bst(root, 1) == 2
    assert kth_smallest_bst(root, 4) == 5
    assert kth_largest_bst(root, 1) == 9
    assert kth_largest_bst(root, 3) == 7
    
    # Test range sum
    assert range_sum_bst(root, 3, 7) == 3 + 4 + 5 + 6 + 7  # 25
    
    # Test closest value
    assert closest_value_bst(root, 3.5) == 4
    assert closest_value_bst(root, 6.7) == 7
    
    # Test array to BST conversion
    arr = [1, 2, 3, 4, 5, 6, 7]
    bst_root = sorted_array_to_bst(arr)
    assert is_valid_bst(bst_root) == True
    assert inorder_recursive(bst_root) == arr
    
    # Test trimming
    trimmed = trim_bst(root, 4, 8)
    trimmed_values = inorder_recursive(trimmed)
    assert all(4 <= val <= 8 for val in trimmed_values)


def test_graph_traversal():
    """Test graph traversal algorithms."""
    # Create test graph: 0 - 1 - 2
    #                    |   |
    #                    3 - 4
    graph = {
        0: [(1, 1), (3, 1)],
        1: [(0, 1), (2, 1), (4, 1)],
        2: [(1, 1)],
        3: [(0, 1), (4, 1)],
        4: [(1, 1), (3, 1)]
    }
    
    # Test DFS
    dfs_result = dfs_recursive(graph, 0)
    assert len(dfs_result) == 5
    assert dfs_result[0] == 0  # Starts with 0
    
    # Test iterative DFS gives same vertices (order may differ)
    dfs_iter_result = dfs_iterative(graph, 0)
    assert set(dfs_result) == set(dfs_iter_result)
    
    # Test BFS
    bfs_result = bfs(graph, 0)
    assert len(bfs_result) == 5
    assert bfs_result[0] == 0
    assert bfs_result[1] in [1, 3]  # Level 1 neighbors
    
    # Test shortest path
    path = shortest_path_bfs(graph, 0, 2)
    assert path == [0, 1, 2]
    
    path = shortest_path_bfs(graph, 3, 2)
    assert len(path) == 4  # 3-0-1-2 or 3-4-1-2


def test_cycle_detection():
    """Test cycle detection algorithms."""
    # Directed graph with cycle: 0 -> 1 -> 2 -> 0
    directed_cycle = {
        0: [(1, 1)],
        1: [(2, 1)],
        2: [(0, 1)]
    }
    assert has_cycle_directed(directed_cycle) == True
    
    # Directed graph without cycle: 0 -> 1 -> 2
    directed_no_cycle = {
        0: [(1, 1)],
        1: [(2, 1)],
        2: []
    }
    assert has_cycle_directed(directed_no_cycle) == False
    
    # Undirected graph with cycle: 0 - 1 - 2 - 0
    undirected_cycle = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (2, 1)],
        2: [(0, 1), (1, 1)]
    }
    assert has_cycle_undirected(undirected_cycle) == True
    
    # Undirected graph without cycle: 0 - 1 - 2
    undirected_no_cycle = {
        0: [(1, 1)],
        1: [(0, 1), (2, 1)],
        2: [(1, 1)]
    }
    assert has_cycle_undirected(undirected_no_cycle) == False


def test_topological_sort():
    """Test topological sorting."""
    # DAG: 0 -> 1 -> 3
    #      |    |
    #      v    v
    #      2 -> 3
    dag = {
        0: [(1, 1), (2, 1)],
        1: [(3, 1)],
        2: [(3, 1)],
        3: []
    }
    
    topo_order = topological_sort(dag)
    assert topo_order is not None
    assert len(topo_order) == 4
    assert topo_order.index(0) < topo_order.index(1)
    assert topo_order.index(0) < topo_order.index(2)
    assert topo_order.index(1) < topo_order.index(3)
    assert topo_order.index(2) < topo_order.index(3)
    
    # Graph with cycle should return None
    cycle_graph = {
        0: [(1, 1)],
        1: [(2, 1)],
        2: [(0, 1)]
    }
    assert topological_sort(cycle_graph) is None


def test_connected_components():
    """Test connected components finding."""
    # Graph with 2 components: {0, 1, 2} and {3, 4}
    graph = {
        0: [(1, 1)],
        1: [(0, 1), (2, 1)],
        2: [(1, 1)],
        3: [(4, 1)],
        4: [(3, 1)]
    }
    
    components = connected_components(graph)
    assert len(components) == 2
    
    # Sort components by first element for consistent testing
    components.sort(key=lambda x: min(x))
    assert set(components[0]) == {0, 1, 2}
    assert set(components[1]) == {3, 4}


def test_bipartite():
    """Test bipartite graph detection."""
    # Bipartite graph: 0 - 1 - 2
    #                  |       |
    #                  3 - - - 4
    bipartite_graph = {
        0: [(1, 1), (3, 1)],
        1: [(0, 1), (2, 1)],
        2: [(1, 1), (4, 1)],
        3: [(0, 1), (4, 1)],
        4: [(2, 1), (3, 1)]
    }
    assert is_bipartite(bipartite_graph) == True
    
    # Non-bipartite graph (triangle): 0 - 1 - 2 - 0
    triangle_graph = {
        0: [(1, 1), (2, 1)],
        1: [(0, 1), (2, 1)],
        2: [(0, 1), (1, 1)]
    }
    assert is_bipartite(triangle_graph) == False


def test_course_schedule():
    """Test course scheduling problem."""
    # Can finish: 0 -> 1, 2 -> 3
    assert course_schedule(4, [[1, 0], [3, 2]]) == True
    
    # Cannot finish due to cycle: 0 -> 1 -> 0
    assert course_schedule(2, [[1, 0], [0, 1]]) == False
    
    # Single course
    assert course_schedule(1, []) == True


def test_edge_cases():
    """Test edge cases."""
    # Empty tree
    assert preorder_recursive(None) == []
    assert is_valid_bst(None) == True
    assert max_depth(None) == 0
    
    # Single node tree
    single = TreeNode(1)
    assert preorder_recursive(single) == [1]
    assert is_valid_bst(single) == True
    assert max_depth(single) == 1
    
    # Empty graph
    assert dfs_recursive({}, 0) == []
    assert connected_components({}) == []
    assert topological_sort({}) == []
    
    # Single vertex graph
    single_vertex = {0: []}
    assert dfs_recursive(single_vertex, 0) == [0]
    assert connected_components(single_vertex) == [[0]]


def main():
    """Run all tests."""
    print("Running Tree and Graph Pattern Tests...")
    print("=" * 50)
    
    tests = [
        ("Tree Traversal", test_tree_traversal),
        ("Binary Search Tree", test_binary_search_tree),
        ("Graph Traversal", test_graph_traversal),
        ("Cycle Detection", test_cycle_detection),
        ("Topological Sort", test_topological_sort),
        ("Connected Components", test_connected_components),
        ("Bipartite Detection", test_bipartite),
        ("Course Schedule", test_course_schedule),
        ("Edge Cases", test_edge_cases),
    ]
    
    passed = 0
    total = len(tests)
    
    for test_name, test_func in tests:
        if run_test(test_name, test_func):
            passed += 1
    
    print("=" * 50)
    print(f"Results: {passed}/{total} test suites passed")
    
    if passed == total:
        print("🎉 All tree and graph tests passed!")
        return 0
    else:
        print("❌ Some tests failed!")
        return 1


if __name__ == "__main__":
    sys.exit(main())