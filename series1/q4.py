#assertion :An assert statement checks whether a condition is true. If a condition evaluates to True, a program will keep running. If a condition is false, the program will return an AssertionError. At this point, the program will stop executing.
x = "hello"

#if condition returns False, AssertionError is raised:
assert x == "goodbye", "x should be 'hello'"