import math


def solve_max_gap():
    # 读取输入文件
    try:
        with open('input.txt', 'r') as fin:
            data = fin.read().split()
    except FileNotFoundError:
        print("找不到 input.txt 文件")
        return

    if not data:
        return

    n = int(data[0])
    nums = [float(x) for x in data[1:1 + n]]

    # 处理边界情况
    if n < 2:
        with open('output.txt', 'w') as fout:
            fout.write("0\n")
        return

    global_min = min(nums)
    global_max = max(nums)

    # 如果所有数都相同，最大间隙为0
    if global_min == global_max:
        with open('output.txt', 'w') as fout:
            fout.write("0\n")
        return

    # 初始化 n-1 个桶
    bucket_count = n - 1
    # 分别记录桶内的最小值和最大值，初始化为正负无穷
    bucket_min = [float('inf')] * bucket_count
    bucket_max = [float('-inf')] * bucket_count

    # 计算每个桶的区间长度
    bucket_len = (global_max - global_min) / bucket_count

    # 将每个数放入对应的桶中
    for num in nums:
        # 计算当前数应该放入的桶的索引
        idx = int((num - global_min) / bucket_len)

        # 如果是最大值，它会被分到最后一个桶（索引为n-1），需要将其放回第n-2个桶
        if idx == bucket_count:
            idx = bucket_count - 1

        # 更新当前桶的极值
        if num < bucket_min[idx]:
            bucket_min[idx] = num
        if num > bucket_max[idx]:
            bucket_max[idx] = num

    # 遍历所有桶，计算相邻非空桶之间的最大间隙
    max_gap = 0.0
    prev_max = global_min  # 前一个非空桶的最大值

    for i in range(bucket_count):
        # 如果桶内有数据（非空桶）
        if bucket_min[i] != float('inf'):
            # 当前桶的最小值减去前一个非空桶的最大值
            gap = bucket_min[i] - prev_max
            if gap > max_gap:
                max_gap = gap
            # 更新前一个非空桶的最大值
            prev_max = bucket_max[i]

    # 输出结果到文件（保留2位小数）
    with open('output.txt', 'w') as fout:
        fout.write(f"{max_gap:.2f}\n")


if __name__ == '__main__':
    solve_max_gap()