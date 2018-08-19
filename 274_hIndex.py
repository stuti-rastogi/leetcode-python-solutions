class Solution:
    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0
        
        n = len(citations)  
                   
        citations.sort()  
        citations.reverse()            
            
        h = 0 
            
        while (h < n) and (citations[h]-1 >= h):  
                h= h + 1                
        return h  
    