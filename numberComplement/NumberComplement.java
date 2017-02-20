public class NumberComplement {
    public int findComplement(int num) {
        int mask = (Integer.highestOneBit(num) << 1) - 1;
        return ~num & mask;
    }
}