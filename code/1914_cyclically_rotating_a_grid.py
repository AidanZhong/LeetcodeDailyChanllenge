# Problem: Cyclically Rotating a Grid
# Topic: Matrix
# Difficulty: Medium
'''
You are given an m x n integer matrix grid​​​, where m and n are both even integers, and an integer k.

The matrix is composed of several layers, which is shown in the below image, where each color is its own layer:



A cyclic rotation of the matrix is done by cyclically rotating each layer in the matrix. To cyclically rotate a layer once, each element in the layer will take the place of the adjacent element in the counter-clockwise direction. An example rotation is shown below:


Return the matrix after applying k cyclic rotations to it.
'''
from typing import List
from collections import deque


class Solution:
    def rotateGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        number_of_layers = min(m, n) // 2

        def get_layer_array_from_grid(layer_number: int) -> List[int]:
            ans = []
            # top row
            for j in range(layer_number, n - layer_number):
                ans.append(grid[layer_number][j])
            # right column
            for i in range(layer_number + 1, m - layer_number):
                ans.append(grid[i][n - layer_number - 1])
            # bottom row
            for j in range(n - layer_number - 2, layer_number - 1, -1):
                ans.append(grid[m - layer_number - 1][j])
            # left column
            for i in range(m - layer_number - 2, layer_number, -1):
                ans.append(grid[i][layer_number])
            return ans

        # get the array of each layers
        layer_arrays = []
        for layer in range(number_of_layers):
            array = get_layer_array_from_grid(layer)
            # rotate the array
            real_k = k % len(array)
            array = array[real_k:] + array[:real_k]
            layer_arrays.append(array)

        ans = [[0] * n for _ in range(m)]

        # refill the grid

        def refill_grid(grid: List[List[int]], layer_number: int, layer_array: deque) -> None:
            # top row
            for j in range(layer_number, n - layer_number):
                grid[layer_number][j] = layer_array.popleft()
            # right column
            for i in range(layer_number + 1, m - layer_number):
                grid[i][n - layer_number - 1] = layer_array.popleft()
            # bottom row
            for j in range(n - layer_number - 2, layer_number - 1, -1):
                grid[m - layer_number - 1][j] = layer_array.popleft()
            # left column
            for i in range(m - layer_number - 2, layer_number, -1):
                grid[i][layer_number] = layer_array.popleft()

        for layer_number, layer_array in enumerate(layer_arrays):
            refill_grid(ans, layer_number, deque(layer_array))
        return ans


print(Solution().rotateGrid(grid=[[40, 10], [30, 20]], k=1))
