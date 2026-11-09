# 便利な関数import
from math import gcd, lcm, ceil, floor, sqrt, factorial, pi # 最大公約数, 最小公倍数, 切り上げ, 切り捨て, 平方根, 階乗
from itertools import permutations, combinations, product, accumulate # 順列, 組み合わせ, デカルト積, 累積和
from collections import deque, defaultdict, Counter
from bisect import bisect_left, bisect_right # 二分探索
from heapq import heappop, heappush, heapify, nlargest, nsmallest # ヒープqueue(優先度付きqueue)

# 型ヒントのためのimport
from collections.abc import Callable, Collection, Iterable
from typing import TypeVar, Any
TYPE = TypeVar('TYPE')
# Iterableの型ヒント
VectorLike_Iterable = Iterable[TYPE]
MatrixLike_Iterable = Iterable[Iterable[TYPE]]
# CollectionはIterableのサブクラスでlen()やin演算子などが使えるもの。
VectorLike_Collection = Collection[TYPE]
MatrixLike_Collection = Collection[Collection[TYPE]]

# inputの高速化などの定型句
import sys
input = sys.stdin.readline
def mapin(): return map(int, input().split())
def listin(): return list(map(int, input().split()))
def listin0indexed(): return [0] + list(map(int, input().split()))
def intin(): return int(input())
def strin(): return input().rstrip() # \nを除去
def printerr(*args, sep=' ', end='\n'): print(*args, sep=sep, end=end, file=sys.stderr) # 標準エラー出力

# 再帰上限の変更
sys.setrecursionlimit(10**6)

def yn(b: bool):
    """True/Falseの出力をYes/Noに変換する関数"""
    return 'Yes' if b else 'No'
def get_top_k_largest(arr: VectorLike_Iterable[TYPE], key_func: Callable[[TYPE], Any], top_k: int = 1) -> list[TYPE]:
    """Counterの中で、`key_func`に従ってソートしたときの値上位`top_k`個のkeyを返す\\
    (idx(昇順), val(降順))の`key_func`の例: `lambda x: (-x[0], x[1])`"""
    return nlargest(top_k, arr, key=key_func)
def get_top_k_smallest(arr: VectorLike_Iterable[TYPE], key_func: Callable[[TYPE], Any], top_k: int = 1) -> list[TYPE]:
    """Counterの中で、`key_func`に従ってソートしたときの値下位`top_k`個のkeyを返す\\
    (idx(昇順), val(降順))の`key_func`の例: `lambda x: (x[0], -x[1])`"""
    return nsmallest(top_k, arr, key=key_func)

# 定数等
ALPH = "abcdefghijklmnopqrstuvwxyz"

# 事前にAI等で作成したものは https://github.com/oYAs-me/abc に記載





