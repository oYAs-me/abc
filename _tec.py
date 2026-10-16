# 定数等
ALPH = "abcdefghijklmnopqrstuvwxyz"
PI = 3.14159265358979323846264338

# 複数行にまたがるものをlistとして管理
a = list(map(int, input().split()))

# listのsort
a.sort() # 変数がそのままsortされる。
a.sort(reverse=True) # 降順ソート


# 文字列が一致するか検討する cf. ABC049-c
s = input().rstrip()
def solve_match_str(s: str):
    """文字列の最初から順に部分文字列の合成で記述できるかを解く"""
    # 最長一致などのときは順序に注意
    candidates = ["dream", "dreamer", "erase", "eraser"] # matchを検証する文字リスト
    i, N = 0, len(s) # 文字列上の確認のためのポインタ管理
    while i <= N:
        is_matched = False
        for c in candidates:
            if s.startswith(c, i): # ◆最初の文字が一致するかどうかを確認するメソッド◆ ※iは開始位置
                i += len(c) # 一致した文字数分だけポインタを進める
                is_matched = True # flagを立てる
                break # for loopから離脱
        if not is_matched:
            return "No"
    return "Yes"
def solve_match_str_from_last(s: str):
    """文字列の最後から順に部分文字列の合成で記述できるかを解く"""
    # 最長一致などのときは順序に注意
    candidates = ["dream", "dreamer", "erase", "eraser"] # matchを検証する文字リスト
    while s: # s == ""のときループから外れる
        is_matched = False
        for c in candidates:
            if s.endswith(c): # ◆最後の文字が一致するかどうかを確認するメソッド◆
                s = s[:-len(c)] # 一致した文字分削除
                is_matched = True # flagを立てる
                break # for loopから離脱
        if not is_matched:
            return "No"
    return "Yes"


def dijkstra(n: int, mat: list[list[int]]):
    """1-indexed な Dijkstra 法による最短経路計算"""

    max_int = 10**18 # 十分大きい数を定数として管理する
    leng = [max_int] * (n+1) # 頂点数分の距離を管理するリスト
    v = [False] * (n+1) # 頂点数分の訪問管理リスト

    leng[1] = 0 # 始点の距離は0
    
    flag = True
    for i in range(1, n+1):
        min_leng = max_int # 最小距離を管理する変数
        for j in range(1, n+1):
            if not v[j] and leng[j] < min_leng: # 未訪問かつ最小距離より小さいとき
                p = j # 最小距離の頂点を管理する変数
                min_leng = leng[j] # 最小距離を更新する
        v[p] = True # 最小距離の頂点を訪問済みにする

        if min_leng == max_int: # 最小距離が更新されないときは、全ての頂点を訪問したことになる
            flag = False
            break

        # pから行ける頂点を更新する
        for j in range(1, n+1):
            if leng[p] + mat[p][j] < leng[j]: # pからjへの距離が、これまでの距離より小さいとき
                leng[j] = leng[p] + mat[p][j] # 距離を更新する
        
    if flag:
        return leng[1:] # 1-indexedなので、0番目は除いて返す

# 左からの累積和を求める
def cumsum(a: list[int]) -> list[int]:
    """左からの累積和を求める"""
    n = len(a)
    s = [0] * (n+1) # 0番目は0で初期化する
    for i in range(n):
        s[i+1] = s[i] + a[i]
    return s

# 右からの累積和を求める
def cumsum_right(a: list[int]) -> list[int]:
    """右からの累積和を求める"""
    n = len(a)
    s = [0] * (n+1) # 0番目は0で初期化する
    for i in range(n):
        s[i+1] = s[i] + a[n-1-i]
    return s