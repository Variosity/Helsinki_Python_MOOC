def matrix_sum():
    with open('matrix.txt') as matrix:
        element_list = []
        int_list = []
        i = 0
        for element in matrix:
            element = element.replace(',', ' ')
            element_list.append(element)
            int_list += [int(num) for num in element_list[i].split()]
            i += 1
    sum_of_matrix = sum(int_list)
    return sum_of_matrix

def matrix_max():
    with open('matrix.txt') as matrix:
        element_list = []
        int_list = []
        i = 0
        for element in matrix:
            element = element.replace(',', ' ')
            element_list.append(element)
            int_list += [int(num) for num in element_list[i].split()]
            i += 1
    max_of_matrix = max(int_list)
    return max_of_matrix

def row_sums():
    with open('matrix.txt') as matrix:
        element_list = []
        int_list = []
        row_sum = []
        i = 0
        for element in matrix:
            element = element.replace(',', ' ')
            element_list.append(element)
            int_list = [int(num) for num in element_list[i].split()]
            sums = sum(int_list)
            row_sum.append(sums)
            i += 1
    #sum_of_rows = int_list
    return row_sum

if __name__ == "__main__":

    print(matrix_sum())
    print(matrix_max())
    print(row_sums())
    #matrix_access()

    '''with open('matrix.txt') as matrix:
    element_list = []
    for element in matrix:
        element_list.append(element)
        '''

    '''def matrix_access():
    with open('matrix.txt') as matrix:
        element_list = []
        int_list = []
        i = 0
        for element in matrix:
            element = element.replace(',', ' ')
            element_list.append(element)
            int_list += [int(num) for num in element_list[i].split()]
    print(element_list)'''