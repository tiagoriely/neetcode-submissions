class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        ans = []
        countMap = {}

        for num in nums:
            countMap[num] = 1 + countMap.get(num, 0)
        
        sorted_map = dict(sorted(countMap.items(), key=lambda item: item[1], reverse=True))

        count = k
        for key, value in sorted_map.items():
            if count == 0:
                break;
            ans.append(key)
            count -= 1
                        
        sorted_ans = sorted(ans)
        return sorted_ans