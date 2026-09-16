from typing import List

def _delete_zeros(d: List[int]) -> List[int]:
    i = len(d) - 1
    while i > 0 and d[i] == 0:
        i -= 1
    return d[: i + 1]

class BigInt:
    def __init__(self, data = None):
        self.data = _delete_zeros(data if data else [0])
        self.base = 10000 #we have 1 nuber in 4 blocks(from 0 to 9999)
        self.digits_count = 4

    @staticmethod
    def from_str( s):
        if not s.isdigit():
            raise ValueError
        if s == "0":
            return BigInt([0])
        number = []
        i = len(s)
        while i > 0:
            j = max(0, i-4)
            number.append(int(s[j:i]))
            i=j
        return BigInt(number)

    def to_str(self):
        if len(self.data) == 1:
            return str(self.data[0])
        number_parts = [str(self.data[-1])]
        number_parts.extend(f"{x:0{self.digits_count}d}" for x in reversed(self.data[:-1]))
        return "".join(number_parts)

    def cmp(self, other):
        if len(self.data) != len(other.data):
            return -1 if len(self.data) < len(other.data) else 1
        for a, b in zip(reversed(self.data), reversed(other.data)):
            if a != b:
                return -1 if a < b else 1
        return 0

    def sum(self, other):
        a, b = self.data, other.data
        n = max(len(a), len(b))
        res = [0] * (n + 1)
        carry = 0
        for i in range(n):
            ai = a[i] if i < len(a) else 0
            bi = b[i] if i < len(b) else 0
            s = ai + bi + carry
            if s >= self.base:
                s -= self.base
                carry = 1
            else:
                carry = 0
            res[i] = s
        res[n] = carry
        return BigInt(_delete_zeros(res))

    def sub(self, other):
        if self.cmp(other) < 0:
            raise ValueError("negative result")
        a, b = self.data, other.data
        res = [0] * len(a)
        borrow = 0
        for i in range(len(a)):
            ai = a[i]
            bi = b[i] if i < len(b) else 0
            s = ai - bi - borrow
            if s < 0:
                s += self.base
                borrow = 1
            else:
                borrow = 0
            res[i] = s
        return BigInt(_delete_zeros(res))

    def mul(self, other):
        a, b = self.data, other.data
        res = [0] * (len(a) + len(b))
        for i in range(len(a)):
            carry = 0
            for j in range(len(b)):
                total = res[i + j] + a[i] * b[j] + carry
                res[i + j] = total % self.base
                carry = total // self.base
            res[i + len(b)] += carry
        return BigInt(_delete_zeros(res))

    def sqr(self):
        return self.mul(self)

    def mod(self, other):
        if other.data == [0]:
            raise ValueError("modulus = 0")
        rem = BigInt([0])
        ten = BigInt([10])
        for part in self.to_str():
            rem = rem.mul(ten).sum(BigInt([int(part)]))
            while rem.cmp(other) >= 0:
                rem = rem.sub(other)
        return rem

    def calculate(self, cmdline):
        parts = cmdline.strip().split()
        cmd = parts[0].lower()

        if cmd == "sum":
            A, B = self.from_str(parts[1]), self.from_str(parts[2])
            return A.sum(B).to_str()

        if cmd == "mul":
            A, B = self.from_str(parts[1]), self.from_str(parts[2])
            return A.mul(B).to_str()

        if cmd == "sqr":
            A = self.from_str(parts[1])
            return A.sqr().to_str()

        if cmd == "mod":
            A, M = self.from_str(parts[1]), self.from_str(parts[2])
            return A.mod(M).to_str()

        raise ValueError("unknown command")