# Python : nは64bitで表す事ができる自然数とし、1以下の整数もしくは合成数ならFalse、素数ならTrueを返す
import math

BASE_32 = (2, 7, 61)
BASE_64 = (2, 325, 9375, 28178, 450775, 9780504, 1795265022)
SMALL_PRIMES = (3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47)
PRODUCT_OF_SMALL_PRIMES = 614889782588491410  # 3から47までの素数の積

def miller_rabin(n: int) -> bool:
    if n < 2:
        return False
    if (n & 1) == 0:
        return n == 2

    # 小素数を用いた前処理（約85%以上の合成数を即座に除外）
    if math.gcd(n, PRODUCT_OF_SMALL_PRIMES) > 1:
        return n in SMALL_PRIMES

    if n < 4294967296:  # 2 ** 32
        bases = BASE_32
    elif n < 18446744073709551616:  # 2 ** 64
        bases = BASE_64
    else:
        raise ValueError("input integer is larger than 2 ** 64")

    n1 = n - 1
    lsb = n1 & -n1
    s = lsb.bit_length() - 1
    d = n1 >> s

    for a in bases:
        if a % n == 0:
            continue
        t = pow(a, d, n)
        if t == 1 or t == n1:
            continue
        for _ in range(s - 1):
            t = (t * t) % n
            if t == n1:
                break
        else:
            return False
    return True

def eratosthenes_sieve(n: int) -> tuple[list[int], bytearray]:
    """エラトステネスの篩による素数列挙\n
    list[int] : 素数のリスト
    bytearray : 素数フラグの配列 (0: 合成数, 1: 素数)
     -> bytearray[i] == 1 のとき i は素数
    """
    if n < 2:
        return []

    # 1バイトの配列で素数フラグを管理 (0: 合成数, 1: 素数)
    is_prime = bytearray([1]) * (n + 1)
    is_prime[0] = is_prime[1] = 0

    # sqrt(n) までの走査で十分
    limit = int(n**0.5)
    for i in range(2, limit + 1):
        if is_prime[i]:
            # C言語層でのスライス代入によりループ処理を高速化
            is_prime[i * i : n + 1 : i] = bytearray((n - i * i) // i + 1)

    return [i for i, prime in enumerate(is_prime) if prime], is_prime

if __name__ == "__main__":
    n = int(input('input integer: '))
    if miller_rabin(n):
        print(f"{n} is prime")
    else:
        print(f"{n} is not prime")
