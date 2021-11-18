# -*- coding: utf-8 -*-
"""
    @Time    : 2021/11/17 18:05
    @Author  : jiayou.liu
"""
import functools
import random
import time
from typing import List

print_arg = True


def log(description=None, print_args=print_arg, print_cost_time=True):
    """日志切面"""

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print(f"---{description}---")
            if print_args:
                print(f"args: {args}")
            start_time = int(time.time() * 1000)
            res = func(*args, **kwargs)
            end_time = int(time.time() * 1000)
            if print_args:
                print(f"return: {res}")
            if print_cost_time:
                print(f'cost: {end_time - start_time} ms')

        return wrapper

    return decorator


def swap(arr: List[int], i: int, j: int):
    """交换数组中两个下标的值"""
    temp = arr[i]
    arr[i] = arr[j]
    arr[j] = temp


@log(description="冒泡排序")
def bubble_sort(arr: List[int]):
    """冒泡排序
    思路：两两比较，第一轮会选出最大的数，第二轮选出次大的数，依此类推...进行N轮
    时间复杂度：O(N*N)
    """
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    for i in range(arr_len):
        for j in range(arr_len - 1 - i):
            if arr[j] > arr[j + 1]:
                # 两两比较交换
                swap(arr, j, j + 1)
    return arr


@log(description="选择排序")
def selection_sort(arr: List[int]):
    """选择排序
    思路：选择第0个值，跟剩下所有值比较。第一轮选出最小值跟第0位交换。选择第1个值，第二轮选出次小值跟第1位交换，以此类推...进行N轮
    时间复杂度：O(N*N)
    """
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    for i in range(arr_len):
        min_index = i
        for j in range(i + 1, arr_len):
            if arr[j] < arr[min_index]:
                min_index = j
        swap(arr, i, min_index)
    return arr


@log(description="插入排序")
def insert_sort(arr: List[int]):
    """插入排序
    思路：第一轮保证0-0有序，第二轮保证0-1有序，第三轮保证0-2有序，以此类推...进行N轮
    时间复杂度：O(N*N)
    """
    arr_len = len(arr)
    if arr_len <= 1:
        return arr
    for i in range(1, arr_len):
        current_index = i
        for j in range(i - 1, -1, -1):
            if arr[current_index] < arr[j]:
                swap(arr, current_index, j)
                current_index = j
    return arr


def init_random_array(size: int):
    """生成一个随机数组"""
    return [random.randint(-size, size) for i in range(size)]


def quick_sort_fun(arr: List[int], left: int, right: int):
    # 递归出口
    if left >= right:
        return
    i = left
    j = right
    base_val = arr[left]
    while left < right:
        # 从右往左选择一个比基准值小的数
        while left < right and arr[right] >= base_val:
            right = right - 1
        # 如果left和right没有相遇则交换，i++
        if left < right:
            swap(arr, left, right)
            left = left + 1
        # 从左往右选择一个比基准值大的数
        while left < right and arr[left] <= base_val:
            left = left + 1
        # 如果left和right没有相遇则交换，j--
        if left < right:
            swap(arr, left, right)
            right = right - 1
    # 分别对基准值左右两边进行二分递归
    quick_sort_fun(arr, i, left - 1)
    quick_sort_fun(arr, left + 1, j)
    return arr


@log(description="快速排序")
def quick_sort(arr: List[int]):
    """快速排序
    思路：
    1.取基准值arr[0]，i=0, j=len(arr)-1。
    2.从右往左遍历j--，找到比基准值大的数，将该数赋给arr[i]。
    3.从坐往右遍历i++，找到比基准值小的数，将该数赋给arr[j]。
    4.如果i<j，则继续。否则将基准值左右两边进行递归。当二分后i>=j时递归结束。
    时间复杂度：O(NlogN),最坏情况下O(N*N)
    """
    return quick_sort_fun(arr, 0, len(arr) - 1)


def merge_sort_fun(arr: List[int], start: int, end: int):
    # 只有一个元素一定是有序的
    if start == end:
        return
    # 分
    mid = int((end - start) / 2) + start
    left_start = start
    left_end = mid
    right_start = mid + 1
    right_end = end

    merge_sort_fun(arr, left_start, left_end)
    merge_sort_fun(arr, right_start, right_end)
    # 合
    new_arr = []
    # 依次升序排列
    while left_start <= left_end and right_start <= right_end:
        if arr[left_start] < arr[right_start]:
            new_arr.append(arr[left_start])
            left_start = left_start + 1
        else:
            new_arr.append(arr[right_start])
            right_start = right_start + 1
    # 左边数组未遍历完
    while left_start <= left_end:
        new_arr.append(arr[left_start])
        left_start = left_start + 1
    # 右边数组未遍历完
    while right_start <= right_end:
        new_arr.append(arr[right_start])
        right_start = right_start + 1
    # 将合并后的有序临时数组内容替换到原数组
    for i in range(end - start + 1):
        arr[i + start] = new_arr[i]
    return arr


@log(description="归并排序")
def merge_sort(arr: List[int]):
    """归并排序
    思路：
    1.将原数组进行二分，直到数组内只存在一个元素。
    2.将不能再分的数组进行合并，比较大小按顺序放入新数组。
    3.将有序的新数组数据同步到旧数组
    """

    return merge_sort_fun(arr, 0, len(arr) - 1)


if __name__ == '__main__':
    """算法数据结构学习
    算法可视化理解：
    1. https://www.cs.usfca.edu/~galles/visualization/Algorithms.html
    2. https://visualgo.net/en
    """
    data_size = 10
    bubble_sort(init_random_array(data_size))
    selection_sort(init_random_array(data_size))
    insert_sort(init_random_array(data_size))
    quick_sort(init_random_array(data_size))
    merge_sort(init_random_array(data_size))
