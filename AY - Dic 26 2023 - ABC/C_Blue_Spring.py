def find_sum(nums, D, P):
    def backtrack(start, curr_nums):
        if len(curr_nums) == D and sum(curr_nums) > P:
            return curr_nums
        for i in range(start, len(nums)):
            curr_nums.append(nums[i])
            result = backtrack(i + 1, curr_nums)
            if result:
                return result
            curr_nums.pop()
        return None
    s=0
    nums.sort(reverse=True)
    while True:
        try:
            x = backtrack(0, [])
            s+=len(x)
            for xi in x:
                nums.pop(nums.index(xi))
        except:
            break
    return s
        

N,D,P = map(int, input().split())
Fi = list(map(int, input().split()))
Fi.sort(reverse=True)
x = find_sum(Fi, D, P)
print(x//D,sum(Fi))











