#include "Stack.h"

template <typename T>
stack<T>::stack()
{
	start = NULL;
}

template <typename T>
stack<T>::~stack()
{
	deleteStack();
}

template <typename T>
stack<T>::stack(const stack<T>& copy)
{
	copyStack(copy);
}

template <typename T>
stack<T>& stack<T>::operator=(const stack<T>& copy)
{
	if(this != &copy)
	{
		deleteStack();
		copyStack(copy);
	}
	return *this;
}

int main()
{
	return 0;
}