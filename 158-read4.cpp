#include <algorithm>
#include <stdlib>
using namespace std;

/*
 * The API: int read4(char *buf) reads 4 characters at a time from a file.
 * 
 * The return value is the actual number of characters read. For example, it returns 3 if there is only 3 characters left in the file.
 * 
 * By using the read4 API, implement the function int read(char *buf, int n) that reads n characters from the file.
 * 
 * Note:
 * The read function may be called multiple times.
 */


// Forward declaration of the read4 API.
int read4(char *buf);


class Solution {
    char extra_buf[4];
    int  extra_size;
    int  extra_offset;
public:
    Solution() {
        extra_size = 0;
        extra_offset = 0;
    }
    
    /**
     * @param buf Destination buffer
     * @param n   Maximum number of characters to read
     * @return    The number of characters read
     */
    int read(char *buf, int n) {
        int total = 0;
        
        // drain the extra_buf first
        if (extra_size - extra_offset > 0) {
            int ngot = extra_size - extra_offset;
            int need = min(n, ngot);
            
            memcpy(buf, &extra_buf[extra_offset], need);
            extra_offset += need;
            total += need;
            buf += need;
            n -= need;
        }
        
        // read by portions of 4 bytes
        while (n >= 4) {
            int nr = read4(buf);
            
            if (nr < 0)
                return nr;
            else if (nr == 0)
                break;
                
            buf += nr;
            n -= nr;
            total += nr;
        }
        
        // fill the remainder
        if (n) {
            int nr = read4(extra_buf);
            if (nr < 0)
                return nr;
            
            if (nr > 0) {
                extra_size = nr;
                
                int need = min(extra_size, n);
                memcpy(buf, extra_buf, need);
                total += need;
                extra_offset = need;
            }
        }
        
        return total;
    }
};
