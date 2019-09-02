# coding=utf-8
# 二维数组中，每行从左到右递增，每列从上到下递增，给出一个数，判断它是否在数组中
# 从左下角（或右上角）开始遍历数组


def find_integer(matrix, num):
    if not matrix:
        return False
    raws, cols = len(matrix), len(matrix[0])
    raw, col = raws - 1, 0
    while raw >= 0 and col <= cols - 1:
        if matrix[raw][col] == num:
            return True
        elif matrix[raw][col] > num:
            raw -= 1
        else:
            col += 1
    return False


if __name__ == '__main__':
    matrix = [[1, 2, 3],
              [2, 3, 6],
              [3, 6, 7]]
    num = 6
    print(find_integer(matrix, num))