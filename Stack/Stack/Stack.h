template <typename T>
struct element
{
	T data;
	element* link;
};

template <typename T = int>
class stack 
{
public:
	stack();
	~stack();
	stack(const stack&);
	stack& operator=(const stack&);

	bool isEmpty() const;
	void push(const T&);
	void pop(T&);
	void top(T&) const;
	int lenght();
private:
	element<T> *start;
	void copyStack(const stack&);
	void deleteStack();
};

