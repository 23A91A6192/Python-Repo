def addition(A,B):
    return [[A[i][j]+B[i][j] for j in range(len(A[0]))] for i in range(len(A))]
def Transpose(matrix):
    return [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
def Multiplication(A,B):
    result=[[0]*len(B[0]) for _ in range(len(A))]
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(A)):
                result[i][j]+=A[i][k]*B[k][j]
    return result
def main():
    A=[[1,2],[4,5]]
    B=[[7,8],[10,11]]
    add=addition(A,B)
    print("Addition: ")
    for row in add:
        print(row)
    print("Transpose")
    Trans=Transpose(A)
    for row in Trans:
        print(row)
    print("Multiplication")
    mul=Multiplication(A,B)
    for row in mul:
        print(row)
if __name__=="__main__":
    main()