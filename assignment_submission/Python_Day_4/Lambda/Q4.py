def display_args(*args):
    print("Arguments:", args)

display_args(1, 2, 3, "hello", [4, 5])

display_lambda = lambda *args: print("Arguments:", args)

display_lambda('a', 'b', 10, 20)