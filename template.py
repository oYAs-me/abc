# inputの高速化などの定型句
import sys
input = sys.stdin.readline
def mapin(): return map(int, input().split())
def listin(): return list(map(int, input().split()))
def intin(): return int(input())
def strin(): return input().rstrip() # \nを除去
def printerr(*args, sep=' ', end='\n'): print(*args, sep=sep, end=end, file=sys.stderr) # 標準エラー出力
def printerr_f(*args, sep=' ', end='\n'): print(*[f"{arg=}" for arg in args], sep=sep, end=end, file=sys.stderr) # printerrをf文字列で{variable=}のようにする

# 再帰上限の変更
sys.setrecursionlimit(10**6)

# True/Falseの出力をYes/Noに変換する関数
def yn(b: bool): return 'Yes' if b else 'No'

# 便利な関数import
from math import gcd, lcm, ceil, floor, sqrt, factorial # 最大公約数, 最小公倍数, 切り上げ, 切り捨て, 平方根, 階乗
from itertools import permutations, combinations, product, accumulate # 順列, 組み合わせ, デカルト積, 累積和
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right # 二分探索
from heapq import heappop, heappush, heapify # ヒープqueue(優先度付きqueue)

# 定数等
ALPH = "abcdefghijklmnopqrstuvwxyz"
PI = 3.14159265358979323846264338

# 事前にAI等で作成したものは https://github.com/oYAs-me/abc に記載

