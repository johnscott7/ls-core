frozen = frozenset([1, 2, 3, 4, 5])
frozen.add(6)
print(frozen)

# What will the above output?
# This will give an error since frozensets are immutable and
# also because add is a set method, not a frozenset method