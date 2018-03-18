class Solution {
public:
    int hammingWeight(uint32_t n) {
        int nbits = 0;
        while (n) {
            nbits += 1;
            n &= n - 1;
        }
        return nbits;
    }
};
