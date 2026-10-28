def row_correct(sudoku: list, row_no: int):
    for num in sudoku[row_no]:
        if sudoku[row_no].count(num) > 1 and num != 0:
            return False
    
    return True

if __name__ == "__main__":
    pass