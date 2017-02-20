public class hammingDistance 
{
    public int hammingDistance(int x, int y) 
    {  
        return Integer.bitCount(x ^ y);
    }
}