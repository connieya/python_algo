def maxSubArraySum(pnl, k):
    n = len(pnl)
    max_sum = -float('inf')
    current_sum = 0
    left = 0

    for right in range(n):
        current_sum += pnl[right]

        # 연속된 서브 배열의 길이가 k를 초과하면 왼쪽 포인터를 이동
        while (right - left + 1) >= k:
            current_sum -= pnl[left]
            left += 1

        max_sum = max(max_sum, current_sum)

    return max_sum

pnl = [-7,-5,-8,-6,-7]
k = 3
result = maxSubArraySum(pnl, k)
print(result)  # 결과는 8