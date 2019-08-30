def mergeSortedArray(A, B):
    for num in B:
        A.append(num)
    nums_len = len(A)
    for i in range(0, nums_len):
        for j in range(i, nums_len):
            if A[j] < A[i]:
                mid = A[i]
                A[i] = A[j]
                A[j] = mid
    return A

if __name__ == '__main__':
    A = [1,2,5,7]
    B = [4,2,3,9,20,6]
    s = mergeSortedArray(A,B)
    print(s)