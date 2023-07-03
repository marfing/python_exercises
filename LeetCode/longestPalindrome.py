class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 1:
            return s
        groups = []
        back_groups = []

        print(f"Grouping: {s}")
        for index,c in enumerate(s):
            if len(groups) == 0:
                groups.append(c)
            else:
                groups = [g for g in groups if len(g) > 1] + [g+c for g in groups[-index:]]
                groups.append(c)
        
        #print(f"Grouping: {s[::-1]}")
        for index,c in enumerate(s[::-1]):
            if len(back_groups) == 0:
                back_groups.append(c)
            else:
                back_groups = [g for g in back_groups if len(g) > 1] + [g+c for g in back_groups[-index:]]
                back_groups.append(c)
        
        groups = set(groups[:-1])
        back_groups = set(back_groups[:-1])

        palindromes = groups.intersection(back_groups)

        print(f"groups: {groups}")
        print(f"back_groups: {back_groups}")
        print(f"palindromes: {palindromes}")
        if len(palindromes) > 0:
            print(f"longest palindromes: {max(list(palindromes),key=len)}")
            return max(list(palindromes),key=len)
        else:
            return s[0]

    def longestPalindrome2(self, s: str) -> str:
        if len(s) == 1:
            return s
        groups = {}
        back_groups = {}

        #print(f"Grouping: {s}")
        for index,c in enumerate(s):
            if len(groups) == 0:
                groups[c]=index
            else:
                temp = {key+c:value for (key,value) in groups.items()}
                groups = {key:value for (key,value) in groups.items() if len(key) > 1 and value > index}
                groups.update(temp)
                groups[c] = index
        
        print(f"Groups: {groups}")
        #print(f"Grouping: {s[::-1]}")
        # for index,c in enumerate(s[::-1]):
        #     if len(back_groups) == 0:
        #         back_groups.append(c)
        #     else:
        #         back_groups = [g for g in back_groups if len(g) > 1] + [g+c for g in back_groups[-index:]]
        #         back_groups.append(c)
        
        # groups = set(groups[:-1])
        # back_groups = set(back_groups[:-1])

        # palindromes = groups.intersection(back_groups)

        # print(f"groups: {groups}")
        # print(f"back_groups: {back_groups}")
        # print(f"palindromes: {palindromes}")
        # if len(palindromes) > 0:
        #     print(f"longest palindromes: {max(list(palindromes),key=len)}")
        #     return max(list(palindromes),key=len)
        # else:
        #     return s[0]

    def longestPalindrome3(self, s: str) -> str:
        pal = s[0]
        if len(s) == 1:
            return pal
        for index,c in enumerate(s):
            temp = c
            for c2 in s[index+1:]:
                temp = temp + c2
                if temp == temp[::-1]:
                    if len(temp) > len(pal):
                        pal = temp
        return pal

if __name__ == "__main__":
    solution = Solution()
    # solution.longestPalindrome('abcd')
    solution.longestPalindrome3('babad')
    solution.longestPalindrome3('aacabdkacaa')
    solution.longestPalindrome3('abcd')