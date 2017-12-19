#include <cmath>
#include <vector>
#include <algorithm>

class Solution {
public:
    int countPrimes(int n) 
    {
        if (n < 2)
            return 0;
        
        vector<bool> primes(n);
        int limit = static_cast<int>(sqrt(n));

        for (int p = 2; p <= limit; p++) {
            if (!primes[p]) {
                for (int j = p*p; j < n; j += p)
                    primes[j] = true;
            }
        }

        return count(primes.begin() + 2, primes.end(), false);
    }
};
