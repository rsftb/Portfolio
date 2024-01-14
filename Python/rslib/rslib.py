import re


# Static helpers
class Utilities:
    def __new__(*args, **kwargs) -> None: ...
    
    @classmethod
    def is_hex32(cls, string: str) -> bool:
        return re.fullmatch(r"^0x(([0-9A-F]){1,4})|(([0-9a-f]){1,4})$", string) is not None
        
    @classmethod
    def is_hex64(cls, string: str) -> bool: 
        return re.fullmatch(r"^0x(([0-9A-F]){1,8})|(([0-9a-f]){1,8})$", string) is not None
    
    # Doesn't seem to be any difference in the two methods below
    
    #@classmethod
    #def is_lambda(cls, cb) -> bool:
    #    return isinstance(cb, LambdaType)
    
    #@classmethod
    #def is_func(cls, cb) -> bool:
    #    return isinstance(cb, FunctionType)
    
    # Fairly useless function
    # Utilities.swap([1, 2, 3], 0, 2)
    @classmethod
    def swap(cls, container, i, j):
        container[i], container[j] = container[j], container[i]
    
    
print("===== Utilities =====")
hexnum = hex(30053)
print(hexnum)

print(Utilities.is_hex32("0x0000"))

print("=====================\n")



# Functor
class SortingAlgorithms:
    def __new__(self, container, algorithm, direction="ascending"):
      
        f = getattr(self, algorithm, None)
        if f is None: return False
        
        sorted_container = f(container, direction)
        return sorted_container
    
    # Modifies the list in-place (in the future)
    @classmethod
    def quicksort(self, container, direction="ascending"):
        
        if len(container) < 2:
            return container
    
        pivot = container[len(container) // 2]
        left = []
        middle = []
        right = []
    
        for i in container:
            if   i < pivot: left.append(i)
            elif i > pivot: right.append(i)
            else: middle.append(i)
    
        return self.quicksort(left) + middle + self.quicksort(right)
        

print("===== Sorting Algorithms =====")

foo = [4, 2, 8, 1, 4, 3]
print(foo, end=" > ")

foo_sorted = SortingAlgorithms([4, 2, 8, 1, 4, 3], "quicksort")
print(foo_sorted)


#bar = [2, 8, 1, 3, 2, 1]
#print(bar, end=" > ")

#bar_sorted = SortingAlgorithms.mergesort(bar)
#print(bar_sorted)

print("==============================\n")



class SizeError(Exception): ...


# List with a size limit
class SizedList:
    def __init__(self, max_size: int, from_container=None):
        self.sizedlist = list()
        
        if not isinstance(max_size, int):
            raise ValueError(f"max_length expects int, received {type(max_length)}")
        else:
            self._max_size = max_size
        
        if from_container:
            self.sizedlist.extend(from_container)

    @property
    def size(self):
        return len(self.sizedlist)
        
    @property
    def max_size(self):
        return self._max_size
    
    @max_size.setter
    def max_size(self, value):
        if value >= self.size:
            self._max_size = value
            return
        raise SizeError(f"New max_size ({value}) can't fit all objects currently in the sized list ({self.size}).")

    # inst.append(x)
    def append(self, item):
        if len(self.sizedlist) >= self.max_size:
            raise SizeError(f"Max length of '{self.max_length}' exceeded")
        else:
            self.sizedlist.append(item)
    
    # inst.pop(i)
    def pop(self, index):
        return self.sizedlist.pop(index)
    
    # print(inst)
    def __str__(self):
        return self.sizedlist.__str__()
    
    # print(inst.__repr__())
    def __repr__(self):
        return str(type(self))
    
    # inst[i]
    def __getitem__(self, index):
        return self.sizedlist[index]
    
    # len(inst)
    def __len__(self):
        return len(self.sizedlist)
    
    # inst_1 += inst_2
    def __iadd__(self, other):
        if isinstance(other, SizedList):
            self.sizedlist.extend(other.sizedlist)
        else:
            self.sizedlist.extend(other)
        return self


print("===== Sized List =====")
        
foo = SizedList(9, [73, 62, 21])
bar = SizedList(5, [1, 2, 3])

foo.append(59)
foo.append(20)

print(f"foo: {foo}")
print(f"foo.pop(1) > {foo.pop(1)}")
print(f"foo: {foo}")

print("\nfoo += bar")
foo += bar

print(f"foo: {foo}")
print(f"bar: {bar}")

print(f"\nfoo.size: {foo.size}")
print(f"foo.max_size: {foo.max_size}")

print("\ntry:")
try:
    print("    foo.max_size = 2")
    foo.max_size = 2
except Exception as err:
    print(f"Exception:\n    {err}")
    

print("======================\n")
      


# Returns the first item which yields True
def elect(container, cb):
        
    # Any callable
    if callable(cb):
        for c in container:
            if cb(c) is True: return c
        return None
    
    # String-name callable
    if isinstance(cb, str):
        if eval(f"callable({cb})"):
            for c in container:
                if eval(f"{cb}(c)"): return c
            return None
            
    return False


def blah(x: any):
    return len(x.__repr__()) > 1


print("===== elect() =====")

foo = elect([2, 6, 3, 4, 5], lambda n: n > 2 and n < 6)
print(foo)

foo = elect([1, 345, 5284], blah)
print(foo)

foo = elect([6, "aaa", 7], "blah")
print(foo)

foo = elect([1, 2, 3], range) # range is callable but doesn't yield the class True so function returns None, being able to evaluate range(1) >> 1 as True doesn't matter here
print(foo)

print("===================")


