class Solution:
    def countBits(num):
        """
        :type num: int
        :rtype: List[int]
        """
        num += 1
        res = [0, 1]
        while (len(res) < num):
            res += [i+1 for i in res]
            print (res)
        return res[:num]
    
        # return [bin(i).count('1') for i in range(num+1)]

    if __name__ == "__main__":
        n = 10
        print (countBits(n))