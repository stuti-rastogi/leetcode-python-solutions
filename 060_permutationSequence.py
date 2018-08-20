class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        numbers = list(range(1, n+1))
        permutation = ''
        
        k = k - 1
        
        while n > 0:
            n = n - 1
            
            # get the index of current digit
            fact = math.factorial(n)
            index = k // fact
            k = k % fact
            
            permutation = permutation + str(numbers[index])
            
            # remove handled number
            numbers.remove(numbers[index])

        return permutation