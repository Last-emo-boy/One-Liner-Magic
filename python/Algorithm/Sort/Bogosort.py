sort = lambda a: a if all(a[i] <= a[i+1] for i in range(len(a)-1)) else sort(__import__('random').sample(a, len(a)))
