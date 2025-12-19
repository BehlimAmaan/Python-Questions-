# Python Interview Problems – Complete Solutions
# Author: ChatGPT (Interview-style solutions)
# Note: Each problem is numbered as per the question list

# ---------------- BASIC LEVEL ----------------

# 1. Reverse a string without built-in reverse
def reverse_string(s):
    rev = ""
    for ch in s:
        rev = ch + rev
    return rev

# 2. Check palindrome number
def is_palindrome(num):
    temp = num
    rev = 0
    while num > 0:
        rev = rev * 10 + num % 10
        num //= 10
    return temp == rev

# 3. Largest and smallest in list
def find_min_max(lst):
    minimum = maximum = lst[0]
    for i in lst:
        if i < minimum:
            minimum = i
        if i > maximum:
            maximum = i
    return minimum, maximum

# 4. Character frequency
def char_frequency(s):
    freq = {}
    for ch in s:
        freq[ch] = freq.get(ch, 0) + 1
    return freq

# 5. Swap without third variable
def swap(a, b):
    a, b = b, a
    return a, b

# 6. Prime check
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# 7. Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    series = []
    for _ in range(n):
        series.append(a)
        a, b = b, a + b
    return series

# 8. Sum of digits
def sum_of_digits(n):
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total

# 9. Remove duplicates from list
def remove_duplicates(lst):
    result = []
    for i in lst:
        if i not in result:
            result.append(i)
    return result

# 10. Second largest element
def second_largest(lst):
    first = second = float('-inf')
    for i in lst:
        if i > first:
            second = first
            first = i
        elif first > i > second:
            second = i
    return second

# ---------------- INTERMEDIATE LEVEL ----------------

# 11. Anagram check
def is_anagram(s1, s2):
    return sorted(s1) == sorted(s2)

# 12. Find duplicates in list
def find_duplicates(lst):
    seen = set()
    duplicates = set()
    for i in lst:
        if i in seen:
            duplicates.add(i)
        seen.add(i)
    return list(duplicates)

# 13. Word count
def word_count(sentence):
    words = sentence.split()
    count = {}
    for w in words:
        count[w] = count.get(w, 0) + 1
    return count

# 14. Merge dictionaries
def merge_dicts(d1, d2):
    result = d1.copy()
    for k, v in d2.items():
        result[k] = result.get(k, 0) + v
    return result

# 15. Flatten nested list
def flatten_list(lst):
    result = []
    for i in lst:
        if isinstance(i, list):
            result.extend(flatten_list(i))
        else:
            result.append(i)
    return result

# 16. First non-repeating character
def first_non_repeating(s):
    freq = char_frequency(s)
    for ch in s:
        if freq[ch] == 1:
            return ch
    return None

# 17. Rotate list by k
def rotate_list(lst, k):
    k = k % len(lst)
    return lst[k:] + lst[:k]

# 18. Missing numbers from 1 to n
def missing_numbers(lst, n):
    return [i for i in range(1, n + 1) if i not in lst]

# 19. Check if list is sorted
def is_sorted(lst):
    return lst == sorted(lst)

# 20. Reverse each word
def reverse_words(sentence):
    return " ".join(word[::-1] for word in sentence.split())

# ---------------- INTERMEDIATE–ADVANCED ----------------

# 21. Longest word
def longest_word(sentence):
    words = sentence.split()
    return max(words, key=len)

# 22. Longest substring without repeating characters
def longest_unique_substring(s):
    start = 0
    max_len = 0
    used = {}
    for i, ch in enumerate(s):
        if ch in used and start <= used[ch]:
            start = used[ch] + 1
        else:
            max_len = max(max_len, i - start + 1)
        used[ch] = i
    return max_len

# 23. Move zeros to end
def move_zeros(lst):
    non_zero = [i for i in lst if i != 0]
    zeros = [0] * (len(lst) - len(non_zero))
    return non_zero + zeros

# 24. Pair sum
def pair_sum(lst, target):
    seen = set()
    pairs = []
    for num in lst:
        diff = target - num
        if diff in seen:
            pairs.append((diff, num))
        seen.add(num)
    return pairs

# 25. Stack using list
class Stack:
    def __init__(self):
        self.items = []
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop() if self.items else None

# 26. Queue using list
class Queue:
    def __init__(self):
        self.items = []
    def enqueue(self, item):
        self.items.append(item)
    def dequeue(self):
        return self.items.pop(0) if self.items else None

# 27. Balanced parentheses
def is_balanced(expr):
    stack = []
    pairs = {')': '(', ']': '[', '}': '{'}
    for ch in expr:
        if ch in '([{':
            stack.append(ch)
        elif ch in pairs:
            if not stack or stack.pop() != pairs[ch]:
                return False
    return not stack

# 28. Intersection of lists
def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))

# 29. List of tuples to dictionary
def tuples_to_dict(tuples):
    return dict(tuples)

# 30. Sort dictionary by values
def sort_dict_by_value(d):
    return dict(sorted(d.items(), key=lambda x: x[1]))

# ---------------- ADVANCED LEVEL ----------------

# 31. Binary search
def binary_search(lst, target):
    low, high = 0, len(lst) - 1
    while low <= high:
        mid = (low + high) // 2
        if lst[mid] == target:
            return mid
        elif lst[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1

# 32. Linear search
def linear_search(lst, target):
    for i, val in enumerate(lst):
        if val == target:
            return i
    return -1

# 33. Cycle detection in list
def has_cycle(lst):
    seen = set()
    for i in lst:
        if id(i) in seen:
            return True
        seen.add(id(i))
    return False

# 34. Simple LRU Cache
class LRUCache:
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
    def get(self, key):
        if key not in self.cache:
            return -1
        value = self.cache.pop(key)
        self.cache[key] = value
        return value
    def put(self, key, value):
        if key in self.cache:
            self.cache.pop(key)
        elif len(self.cache) >= self.capacity:
            self.cache.pop(next(iter(self.cache)))
        self.cache[key] = value

# 35. Most frequent element
def most_frequent(lst):
    freq = {}
    for i in lst:
        freq[i] = freq.get(i, 0) + 1
    return max(freq, key=freq.get)

# 36. Decorator for execution time
import time

def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end - start}")
        return result
    return wrapper

# 37. Generator for even numbers
def even_generator(n):
    for i in range(0, n + 1, 2):
        yield i

# 38. Read file line by line
def read_large_file(filename):
    with open(filename, 'r') as file:
        for line in file:
            print(line.strip())

# 39. Shallow vs Deep copy
import copy

def copy_example():
    a = [[1, 2], [3, 4]]
    shallow = copy.copy(a)
    deep = copy.deepcopy(a)
    return a, shallow, deep

# 40. Exception handling
def safe_input():
    try:
        num = int(input("Enter number: "))
        return num
    except ValueError:
        return "Invalid input"

# ---------------- VERY ADVANCED ----------------

# 41. Merge sort
def merge_sort(lst):
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i]); i += 1
        else:
            result.append(right[j]); j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

# 42. Quick sort
def quick_sort(lst):
    if len(lst) <= 1:
        return lst
    pivot = lst[0]
    left = [x for x in lst[1:] if x <= pivot]
    right = [x for x in lst[1:] if x > pivot]
    return quick_sort(left) + [pivot] + quick_sort(right)

# 43. Kth largest element
def kth_largest(lst, k):
    lst.sort(reverse=True)
    return lst[k - 1]

# 44. Multithreading example
import threading

def print_numbers():
    for i in range(5):
        print(i)

# 45. GIL explanation is conceptual – demo uses threading

# 46. Bank Account class
class BankAccount:
    def __init__(self, balance=0):
        self.__balance = balance
    def deposit(self, amount):
        self.__balance += amount
    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
    def get_balance(self):
        return self.__balance

# 47. Producer Consumer (basic)
from queue import Queue

def producer(q):
    for i in range(5):
        q.put(i)

def consumer(q):
    while not q.empty():
        print(q.get())

# 48. Loop optimization
def square_numbers(lst):
    return [i * i for i in lst]

# 49. Parse large JSON file
import json

def parse_json(filename):
    with open(filename) as f:
        data = json.load(f)
    return data

# 50. URL Shortener logic
import random
import string

def url_shortener(long_url):
    short = ''.join(random.choices(string.ascii_letters + string.digits, k=6))
    return f"short.ly/{short}"
