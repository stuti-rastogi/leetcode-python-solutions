class hammingDistance {
public:
    int hammingDistance(int x, int y) {
        int result = x ^ y;
        int hammingDist = 0;     // count no. of ones in result
        
        while (result > 0) 
        {
            if ((result % 2) == 1)
                hammingDist = hammingDist + 1;
            result = result / 2;
        }
        return hammingDist;
    }
};