class Solution:
    def myAtoi(self, s: str) -> int:
        res_s = ''
        begin_sort = False
        negative = False
        res = 0
        digit_num = 0
        for r in s:
            if (ord(r) >= ord('A') and ord(r) <= ord('Z')) or (ord(r) >= ord('a') and ord(r) <= ord('z')) or r == '.':
                break
            if begin_sort and ((ord(r) >= ord('A') and ord(r) <= ord('Z')) or (ord(r) >= ord('a') and ord(r) <= ord('z')) or r == '.' or r == ' ' or r == '+' or r == '-'):
                break
            if ord(r) <= ord('9') and ord(r) >= ord('0'):
                res_s+=r
                begin_sort = True
            elif r == '+' or r == '-':
                if r == '-':
                    negative = True
                begin_sort = True
        if res_s != '':
            res = -1 * int(res_s) if negative else int(res_s)
        if res > 2**31 - 1:
            res = 2**31 - 1
        elif res < -2**31:
            res = -2**31
        return res
