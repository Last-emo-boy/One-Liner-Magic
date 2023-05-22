counting_sort = lambda a: [x for i in range(min(a), max(a) + 1) for x in [i] * a.count(i)]
