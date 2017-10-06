"""
Apart from tuples being immutable there is also a semantic distinction that should guide their usage. Tuples are heterogeneous data structures (i.e., their entries have different meanings), while lists are homogeneous sequences. Tuples have structure, lists have order.

Using this distinction makes code more explicit and understandable.

One example would be pairs of page and line number to reference locations in a book, e.g.:

my_location = (42, 11)  # page number, line number
You can then use this as a key in a dictionary to store notes on locations. A list on the other hand could be used to store multiple locations. Naturally one might want to add or remove locations from the list, so it makes sense that lists are mutable. On the other hand it doesn't make sense to add or remove items from an existing location - hence tuples are immutable.

There might be situations where you want to change items within an existing location tuple, for example when iterating through the lines of a page. But tuple immutability forces you to create a new location tuple for each new value. This seems inconvenient on the face of it, but using immutable data like this is a cornerstone of value types and functional programming techniques, which can have substantial advantages.

There are some interesting articles on this issue, e.g. "Python Tuples are Not Just Constant Lists" or "Understanding tuples vs. lists in Python". The official Python documentation also mentions this ("Tuples are immutable, and usually contain an heterogeneous sequence ...").

In a statically typed language like Haskell the values in a tuple generally have different types and the length of the tuple must be fixed. In a list the values all have the same type and the length is not fixed. So the difference is very obvious.

Finally there is the namedtuple in Python, which makes sense because a tuple is already supposed to have structure. This underlines the idea that tuples are a light-weight alternative to classes and instances.


"""
