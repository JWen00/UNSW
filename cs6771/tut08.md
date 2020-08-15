# Tutorial 8 

## Summary
1) Iterator Invalidation

Iterator invalidation occurs when a mutable operation changes the state of a container in such a
way that any previous iterators for the container are no longer valid. This may occur simply
because the object no longer exists (eg. std::set::erase), because the iterator was stored
internally as a pointer and the object has been moved (eg. std::vector), or for some other
reason.

## Tutorial Exercises

### Write the iterator class for `rope_user`

```c++
#include <range/v3/iterator.hpp>


class rope {
public:
	explicit rope(std::vector<std::string> rope)
	: rope_{std::move(rope)} {}

	class iterator {
        using outer_iterator = std::vector<std::string>::const_iterator; 
        using inner_iterator = std::string::const_iterator; 
	public:
        iterator() = default;
        iterator(const& std::vector<std::string> pointee,
                 outer_iterator outer, 
                 inner_iterator inner)
        : pointee_{&pointee}, 
          outer_{outer}, 
          inner_{inner} {}

        auto operator*() const -> char { 
            return *inner_; 
        }

        auto operator* () -> &char { 
            return *inner_;
        }

		auto operator++() -> iterator { 
            if (inner_ == outer_->end()) { 
                if (outer_ == pointee_->end()) { 
                    return pointee_->end(); 
                }
                ++outer_; 
                inner_ = outer_->begin();
                return *this;
            }
            ++inner_; 
            return *this; 
        }

        auto operator--() -> iterator { 
            if (inner_ == outer_->begin()) { 
                if (outer_ == pointee_->begin()) { 
                    return *this; 
                }
                outer_--;
                inner_ = outer_->end(); 
            }
            --inner_; 
            return *this;
        }

	private:
        outer_iterator outer_; 
        inner_iterator inner_; 
        std::vector<std::string> const* pointee_ = nullptr;
	};

	// TODO(tutorial): add member functions here to make this a range.

private:
	std::vector<std::string> rope_;
};


``
