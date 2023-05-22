# Pancake Sort（煎饼排序） - Python 实现

这是一个使用 Python 实现的 Pancake Sort（煎饼排序）算法。该算法的思想是通过翻转操作将数组中的最大元素逐步移动到数组的最后位置，从而实现排序。该算法具有 O(nlogn) 的平均时间复杂度和 O(1) 的额外空间复杂度。

## 代码逻辑

代码使用递归的方式实现 Pancake Sort。以下是代码的逻辑解释：

1. 如果输入的数组长度小于 2，则直接返回该数组（基本情况）。
2. 否则，执行以下步骤：
   - 找到数组中的最大元素。
   - 将最大元素放到数组的最前面，即将其翻转到索引位置 0 处。
   - 然后，将整个数组进行翻转，使得最大元素移动到数组的末尾。
   - 递归调用 Pancake Sort 函数来处理剩余的子数组（除去最后一个元素）。
3. 返回经过排序的数组。

## 如何使用

以下是使用 Pancake Sort 算法的示例代码：

```python
# 导入 Pancake Sort 函数
pancake_sort = lambda arr: arr if len(arr) < 2 else [max(arr)] + pancake_sort(arr[:arr.index(max(arr))][::-1] + arr[arr.index(max(arr))+1:])

# 使用示例
my_list = [9, 1, 5, 2, 7]
sorted_list = pancake_sort(my_list)
print("排序完成的列表:", sorted_list)
```

上述代码中，我们首先导入了 Pancake Sort 函数。然后，我们定义了一个示例列表 `my_list`，其中包含待排序的元素。接下来，我们调用 `pancake_sort` 函数，将 `my_list` 作为参数传递给它，以获取排序后的结果。最后，我们打印出排序完成的列表。

运行以上代码，将会得到如下输出结果：

```
排序完成的列表: [9, 7, 5, 2, 1]
```

这是经过 Pancake Sort 排序后的列表。