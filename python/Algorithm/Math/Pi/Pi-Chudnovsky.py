calc_pi = (lambda n: 12 * sum(((-1)**k * math.factorial(6*k) * (545140134*k+13591409)) / (math.factorial(3*k) * (math.factorial(k)**3) * ((640320)**(3*k + 3/2))) for k in range(n)))
