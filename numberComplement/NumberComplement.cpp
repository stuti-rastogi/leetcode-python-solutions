class NumberComplement {
public:
    int findComplement(int num) {
        int mask = ~0;          // 0xFFFF FFFF
        while (num & mask)
            mask = mask << 1;   //gives 0s in the places of the actual number
        return ~mask ^ num;
    }
};