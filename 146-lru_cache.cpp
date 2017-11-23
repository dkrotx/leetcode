#include <list>
#include <unordered_map>

class LRUCache {
public:
    LRUCache(int capacity) : limit_(capacity) {}
    
    int get(int key) {
        unordered_map<int, value_ref_pair>::iterator it = hash_.find(key);
        if (it == hash_.end())
            return -1;
        
        update_ref(it->second);
        return it->second.value;
    }
    
    void put(int key, int value) {
        unordered_map<int, value_ref_pair>::iterator it = hash_.find(key);
        if (it == hash_.end())
            insert_value(key, value);
        else {
            it->second.value = value;
            update_ref(it->second);
        }
    }
    
private:
    struct value_ref_pair {
        int value;
        list<int>::iterator it;
    };
    
    list<int> key_list_;
    unordered_map<int, value_ref_pair> hash_;
    size_t limit_;
    
private:
    void update_ref(value_ref_pair &vr) {
        int value = *vr.it;
        key_list_.erase(vr.it);
        key_list_.push_front(value);
        vr.it = key_list_.begin();
    }
    
    void insert_value(int key, int value) {
        if (!limit_)
            return;
        
        if (hash_.size() == limit_) {
            hash_.erase(key_list_.back());
            key_list_.pop_back();
        }
        
        key_list_.push_front(key);
        value_ref_pair r = {value, key_list_.begin()};
        hash_.insert(make_pair(key, r));
    }
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */
