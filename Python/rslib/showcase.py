from rslib import Utilities, SortingAlgorithms, SizedList


print("===== Utilities =====")

hexnum = hex(30053)
print(hexnum)

print(Utilities.is_hex32(hexnum))

#Utilities.quick_cProfile(Utilities.is_hex32, ("0xFFFF",), 1000000)

#Utilities.quick_cProfile(Utilities.is_hex32, ("0xFFFFFFFF",), 1000000)

#Utilities.disassemble_func(Utilities.is_hex32)


print("=====- collapse -====")
nested = [1, 2, [3, [4, 5], (6, 7), 8], 9]
collapsed = Utilities.collapse(nested)
print(f"{nested} > {list(collapsed)}")

print("======- elect -======")

def blah(x: any):
    return len(x.__repr__()) > 1

foo = Utilities.elect([2, 6, 3, 4, 5], lambda n: n > 2 and n < 6)
print(foo)

foo = Utilities.elect([1, 345, 5284], blah)
print(foo)

foo = Utilities.elect([6, "aaa", 7], "blah")
print(foo)

# range is callable but doesn't yield the class True so function returns None
# being able to evaluate range(1) >> 1 as True doesn't matter here
foo = Utilities.elect([1, 2, 3], range)
print(foo)

print("=====================\n")



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
      

