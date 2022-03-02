from sqlalchemy import null


def summaryRanges(nums):
    if len(nums) == 0: return []
    elif len(nums) == 0: return [str(nums[0])]
    index = 0
    b = None
    n = None
    res = []
    index = 1
    for r in range(len(nums)):
        if b != None:
            if nums[b] == nums[r] - index:
                n = r
                index += 1
            else:
                if n == None:
                    res.append(str(nums[b]))
                else:
                    res.append(str(nums[b]) + '->' + str(nums[n]))
                    n = None
                    index = 1
                b = r
        else:
            b = r
        if r == len(nums) - 1:
            if n == None:
                res.append(str(nums[b]))
            else:
                res.append(str(nums[b]) + '->' + str(nums[n]))
    return res