/*
 * Follow up:
 * As an added challenge, try to code it using only iterators in C++ or iterators in Java.
 */

class Vector2D {
public:
    Vector2D(vector<vector<int>>& vec2d) : vec2d_(vec2d) 
    {
        seekFirst();
    }

    int next() {
        int ret = *it_one_;
        seekNext();
        return ret;
    }

    bool hasNext() {
        return it_vecs_ != vec2d_.end();
    }
    
private:
    const vector<vector<int>>& vec2d_;
    vector<vector<int>>::const_iterator it_vecs_;
    vector<int>::const_iterator it_one_;
    
    void seekNext(bool shift = true) {
        if (shift)
            ++it_one_;
        
        while (it_vecs_ != vec2d_.end() && it_one_ == it_vecs_->end()) {
            it_vecs_++;
            it_one_ = it_vecs_->begin();
        }
    }
    
    void seekFirst() {
        it_vecs_ = vec2d_.begin();
        if (it_vecs_ != vec2d_.end())
            it_one_ = it_vecs_->begin();
        
        seekNext(false);
    }
};

/**
 * Your Vector2D object will be instantiated and called as such:
 * Vector2D i(vec2d);
 * while (i.hasNext()) cout << i.next();
 */
