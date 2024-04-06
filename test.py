def print_spiral(matrix):
    top = left = 0
    bottom = len(matrix) - 1
    right = len(matrix[0]) - 1
    
    while left <= right and top <= bottom:
        for i in range(left, right + 1):
            print('\n', matrix[top][i], end=" ")
            print('--', top, i, end=" ")
        top += 1
        
        for i in range(top, bottom + 1):
            print('\n', matrix[i][right], end=" ")
            print('--', i, right, end=" ")
        right -= 1
        
        if top <= bottom:
            for i in range(right, left - 1, -1):
                print('\n', matrix[bottom][i], end=" ")
                print('--', bottom, i, end=" ")
            bottom -= 1
        
        if left <= right:
            for i in range(bottom, top - 1, -1):
                print('\n', matrix[i][left], end=" ")
                print('--', i, left, end=" ")
            left += 1

m = [[0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7],
     [1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7],
     [2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7],
     [3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7],
     [4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7],
     [5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7],
     [6.1, 6.2, 6.3, 6.4, 6.5, 6.6, 6.7],
     [7.1, 7.2, 7.3, 7.4, 7.5, 7.6, 7.7]]

print_spiral(m)