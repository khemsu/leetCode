class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer=""
        temp = sorted(strs)
        first = temp[0]
        last = temp[-1]
        for i in range(min(len(first),len(last))):
            if(first[i]!=last[i]):
                return answer
            answer+=first[i]
        return answer



        