// Below is the interface for Iterator, which is already defined for you.
// **DO NOT** modify the interface for Iterator.
class Iterator {
    struct Data;
    Data* data;
public:
    Iterator(const vector<int>& nums);
    Iterator(const Iterator& iter);
    virtual ~Iterator();
    // Returns the next element in the iteration.
    int next();
    // Returns true if the iteration has more elements.
    bool hasNext() const;
};

// std::optional requires C++17, so simple analog
namespace utils
{
    template<class T>
    class optional {
    public:
        optional() : empty_(true) {}
        optional<T>& operator=(const T& val) {
            value_ = val;
            empty_ = false;
            return *this;
        }
        
        void reset() {
            empty_ = true;
        }
        
        bool has_value() const { return !empty_; }
        
        const T& value() const {
            return value_;
        }
        
    private:
        T value_;
        bool empty_;
    };
}


class PeekingIterator : public Iterator {
public:
    PeekingIterator(const vector<int>& nums) : Iterator(nums) {
        // Initialize any member here.
        // **DO NOT** save a copy of nums and manipulate it directly.
        // You should only use the Iterator interface methods.
        updateNext();
    }

    // Returns the next element in the iteration without advancing the iterator.
    int peek() {
        return next_value_.value();
    }

    // hasNext() and next() should behave the same as in the Iterator interface.
    // Override them if needed.
    int next() {
        int ret = next_value_.value();
        updateNext();
        return ret;
    }

    bool hasNext() const {
        return next_value_.has_value();
    }
    
private:
    utils::optional<int> next_value_;
    
    void updateNext() {
        if (Iterator::hasNext())
            next_value_ = Iterator::next();
        else
            next_value_.reset();
    }
};
