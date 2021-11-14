import numpy as np

def row_multiplying(coef, row): # 계수 만큼 요소 곱하기
    return   coef * row

def adding_rows(src, dst): # 두 행 합치기
    return  dst + src

def row_sort(mat): # pivot기준 오름 차순 정렬
    for i in range(len(mat)):
        src = find_pivot_col(mat[0]) # 시작점
        
        for j in range(1, len(mat)-i):
            dst= find_pivot_col(mat[j]) # 비교 대상
            if dst == -1 and src != -1: # src가 정상이고 dst가 0벡터면 옮기지 않음
                pass
            elif dst < src or src == -1: # 비교대상의 pivot이 더 작으면, 시작이 0 벡터이면  뒤로
                matrix[[j-1,j]] = matrix[[j,j-1]]
            src = dst
    return matrix
        
def find_pivot_col(row): # pivot 찾기
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return -1

n = int(input("n 입력: "))
arr = input("요소를 순서대로 입력(띄어쓰기로 구분): ")

matrix = np.array(list(map(int ,arr.split(" "))))
matrix = matrix.reshape((n,n))
matrix =matrix.astype("float32")

for i in range(n): # col (0 ~ n-1)
    matrix = row_sort(matrix)
    pivot_col  = find_pivot_col(matrix[i]) # j행의 pivot 찾기
    if pivot_col == -1: # pivot 못 찾았다면 그 행은 zero row 이므로
        continue # 다음 열로 넘어감
    
    for j in range(i+1, n): # row 별 operation 적용하기
        #print(matrix[j-1], pivot_col)
        
        #j행 pivot_col열 값 소거
        coef = -1.0*matrix[j][pivot_col] /matrix[i][pivot_col] # 계수 조절 (-해당 값/ 나누려는 값)
        test = row_multiplying(coef, matrix[i]) # 계수 곱
        matrix[j] =adding_rows(test, matrix[j]) # 덧셈
        
print(matrix)
