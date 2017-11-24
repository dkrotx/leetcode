#include <list>
#include <iterator>
#include <unordered_map>
using namespace std;

class LFUCache {
public:
    LFUCache(int capacity) : capacity_(capacity) {
    }
    
    int get(int key)
    {
        table_t::iterator it = table_.find(key);
        if (it == table_.end())
            return -1;
        
        update_ref(it->second);
        return it->second.value;
    }
    
    void put(int key, int value) {
        table_t::iterator it = table_.find(key);
        
        if (it == table_.end())
            insertNew(key, value);
        else {
            it->second.value = value;
            update_ref(it->second);
        }
    }
    
private:
    struct freq_level;
    struct item {
        int key;
        int value;
        list<freq_level>::iterator it_level;
        list<int>::iterator it_within_level;
    };
    
    struct freq_level {
        int freq;
        list<int> keys;
        freq_level(int f) : freq(f) {}
    };
    
    size_t capacity_;
    list<freq_level> levels_;
    
    typedef unordered_map<int, item> table_t;
    table_t table_;
    
private:    
    void update_ref(item& x)
    {
        // to update reference we move item to next level
        int new_freq = x.it_level->freq + 1;
        list<freq_level>::iterator level = std::next(x.it_level);
        
        x.it_level->keys.erase(x.it_within_level);
        if (x.it_level->keys.empty())
            levels_.erase(x.it_level);
        
        if (level == levels_.end() || level->freq > new_freq)
            level = levels_.emplace(level, new_freq);
        
        level->keys.emplace_front(x.key);
        x.it_level = level;
        x.it_within_level = level->keys.begin();
    }
    
    void evict()
    {
        freq_level &least_level = levels_.front();
        int least_key = least_level.keys.back();
        table_.erase(least_key);
        
        least_level.keys.pop_back();
        if (least_level.keys.empty())
            levels_.pop_front();
    }
    
    void insertNew(int key, int value)
    {
        if (!capacity_)
            return;
        
        if (table_.size() == capacity_)
            evict();
        
        if (levels_.front().freq != 1)
            levels_.emplace_front(1);
        
        levels_.front().keys.emplace_front(key);
        item elem = { key, value, levels_.begin(), levels_.front().keys.begin() };
        table_.insert(make_pair(key, elem));
    }
};

/**
 * Your LFUCache object will be instantiated and called as such:
 * LFUCache obj = new LFUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
