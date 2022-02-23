class Solution:
    def convert(self, s: str, numRows: int) -> str:
        def zigzagCoversion(s,numRows):
            res = []
            if((len(s) <= numRows) or (numRows == 1)):
                return s
            for r in range(numRows):
                res.append(s[r])
                pos1 = r + 1
                pos2 = 0
                while(True):

                    if((r != 0) and (r != numRows - 1)):
                        pos1 += (numRows - r - 1) * 2
                        pos2 = pos1 + 2 * r

                        if(pos1 <= len(s)):
                            res.append(s[pos1 - 1])
                            pos1 = pos2
                        else:
                            break
                        if(pos2 <= len(s)):
                            res.append(s[pos2 - 1])
                        else:
                            break
                    else:
                        pos1 += 2 * (numRows-1)
                        if(pos1 <= len(s)):
                            res.append(s[pos1 - 1])
                        else:
                            break
            sres = ''.join(res)
            return sres
        return zigzagCoversion(s,numRows)