#!/usr/bin/python
#coding=utf8


class Node(object):
    def __init__(self, count = 0, num = 0):
        self.count = count
        self.num = num

class  DigitDp(object):
    def __init__(self, bitlength, mod, k):
        self.dp = [[Node(-1, -1) for i in range(20 * bitlength)] for j in range(bitlength)]
        self.mod = mod
        self.k = k
        self.bit = 0

    def calc(self, num):
        self.num = num
        sum = 0
        count = 0
        flag = True
        for i in xrange(len(num), 0, -1):
            self.bit = i
            tmp = self._dfs(i, self.k, flag)
            flag = False
            sum += tmp.num
            count += tmp.count
            sum %= self.mod
            count %= self.mod

        return sum

    def _dfs(self, bit, target, is_start):
        if not bit:
            return Node(0+(not target), 0)
        start = 1 if bit == self.bit else 0
        end = int(self.num[-bit]) + 1 if is_start else 10
        result = Node()

        tmp = self.dp[bit - 1][200 + target]
        if not is_start and start == 0 and tmp.count != -1:
            return  tmp
        else:
            for i in xrange(start, end):
                tmp = self._dfs(bit - 1, i - target, is_start and i == int(self.num[-bit]))
                if tmp.count:
                    result.num += (((10**(bit - 1)%self.mod) * i)%self.mod * tmp.count)%self.mod + tmp.num
                    result.count += tmp.count
                    result.num %= self.mod
                    result.count %= self.mod

            if not is_start and not start:
                self.dp[bit - 1][200 + target] = result

        return result


if __name__ == '__main__':
        (dmin, dmax, strk) = (x for x in raw_input().split())
        # dmin = raw_input()
        # dmax = raw_input()
        # k = input()
        k = int(strk)
        mod = int(10**9+7)
        import pudb; pudb.set_trace()  # XXX BREAKPOINT
        ddp = DigitDp(20, mod, k)
        rmin = ddp.calc(str(int(dmin) - (int(dmin) > 0)))
        rmax = ddp.calc(dmax)
        print(int(rmax - rmin)%mod)

