# 计算 π 的近似值（Chudnovsky 兄弟的加强鬼畜公式）

这个一行Python代码使用了Chudnovsky兄弟的公式来计算π值。这个公式使用无穷级数来表示1/π，并且收敛速度非常快。

## 代码解析

我们使用的公式为:

1 / π = 12 ∑ (−1)^k (6k)!(545140134k+13591409) / ((3k)!(k!)^3(640320)^(3k+3/2))

其中，k是从0开始的自然数，'∑'代表对k进行求和，'!'代表阶乘。

我们用Python的lambda匿名函数来实现这个公式，lambda函数的参数n是迭代次数。具体的实现如下:

```python
(lambda n: 12 * sum(((-1)**k * math.factorial(6*k) * (545140134*k+13591409)) / (math.factorial(3*k) * (math.factorial(k)**3) * ((640320)**(3*k + 3/2))) for k in range(n)))
```

我们使用sum函数来对k的各个值进行求和，使用math.factorial函数来计算阶乘，使用'**'运算符来进行乘方运算。

注意这个函数计算的是1/π，所以我们需要取其倒数来得到π的值。

## 如何使用

你可以直接在Python环境中输入这段代码，然后调用这个函数来得到π的近似值。这是一个例子：

```python
import math

calc_pi = (lambda n: 12 * sum(((-1)**k * math.factorial(6*k) * (545140134*k+13591409)) / (math.factorial(3*k) * (math.factorial(k)**3) * ((640320)**(3*k + 3/2))) for k in range(n)))

# 计算pi
pi = 1 / calc_pi(10)

print(pi)
```

这个例子中，我们首先导入了math库，然后定义了计算1/π的lambda函数。然后我们调用这个函数，参数n设为10，得到了1/π的近似值。最后我们取其倒数，得到了π的近似值。