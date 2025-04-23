#01
from keyword import kwlist
print(kwlist)

#02
# help()
# help>keywords

#03
from a import a
print(a)

#04
# Out of all the keywords, None, True, False are keywords whic are also used as data. And they are only keywords which start with a capital letter.

#05
# del keyword -> when you create a variable, you name it. This process happens in the namespace stack. But the actual object is created in the private heapspace or the dynamic memory and this means that the variable we created is just a reference to the actual object. del keyword deletes the reference variable from the stack namespace. While the actual object stays, this gets deleted by the memory manager's garbage collector. The when and how of the garbage collector is beyond our scope.  