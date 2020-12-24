class Solution:
    def commonElements (self,A, B, C, n1, n2, n3):
        i = 0
        j = 0
        k = 0
        res = []

        while i < n1 and j < n2 and k < n3:
            min_element = min(A[i], B[j], C[k])

            if A[i] == B[j] == C[k]:
                res.append(A[i])
                i += 1
                j += 1
                k += 1

            else:
                if min_element == A[i]:
                    i += 1

                if min_element == B[j]:
                    j += 1

                if min_element == C[k]:
                    k += 1

        sorted(list(set(res)))
        return res