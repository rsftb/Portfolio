from types import FunctionType
import re
import cProfile
import dis


# TODO
#   * Utilities:
#       - more methods, maybe another profiling method
#   * SortingAlgorithms:
#       - add MergeSort
#       - add InsertionSort
#       - add BogoSort
#   * SizedList:
#       - see if there's relevant dunder methods missing
#   ~ Maths:
#       - create


# Static helpers in namespace Utilities
class Utilities:
    def __new__(*args, **kwargs) -> None: ...
    
    ## Boolean "is_something()" methods
    # Removed the methods is_func and is_lambda
    
    # Utilities.is_hex32("0xC2FF")
    @classmethod
    def is_hex32(cls, hexadecimal: str) -> bool:
        return re.fullmatch(r"^0x(([0-9A-F]){1,4})|(([0-9a-f]){1,4})$", hexadecimal) is not None
    
    # Utilities.is_hex64("0xdeadbeef")
    @classmethod
    def is_hex64(cls, hexadecimal: str) -> bool: 
        return re.fullmatch(r"^0x(([0-9A-F]){1,8})|(([0-9a-f]){1,8})$", hexadecimal) is not None


    ## Visual debugging tools
    
    # Utilities.quick_cProfile(myfunc, ("foo",), 50)
    @classmethod
    def quick_cProfile(cls, func: callable, arguments: tuple, calls=1):
        if calls == 1:
            pr = cProfile.Profile()
            pr.enable()
            func(*arguments)
            pr.disable()
            pr.print_stats()
        elif calls > 1:
            pr = cProfile.Profile()
            pr.enable()
            for i in range(calls): func(*arguments)
            pr.disable()
            pr.print_stats()
        else:
            return False
    
    # Utilities.disassemble_func(myfunc)
    @classmethod
    def disassemble_func(cls, func: FunctionType):
        bytecode = dis.dis(func)
        print(bytecode)
    
    
    ## Auxillary functions    
        
    # Utilities.elect([6, 3, 1, 4, 5], lambda n: n > 3 and n < 6)
    @classmethod
    def elect(cls, container, cb: callable) -> any:
        """Returns the first item which yields True"""
        
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
    
    # Fairly useless function
    # Utilities.swap([1, 2, 3], 0, 2)
    @classmethod
    def swap(cls, container, i, j):
        container[i], container[j] = container[j], container[i]



# Functor for sorting algorithms
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
            raise SizeError(f"Max size of '{self.max_size}' exceeded.")
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


