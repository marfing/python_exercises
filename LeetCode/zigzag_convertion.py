class Solution:
    def convert(self, s: str, numRows: int) -> str:
        new_string = ''
        count = 0
        while count*int(numRows*3/2) < len(s):
            new_string += s[count*int(numRows*3/2)] 
            count += 1
        print(f"New string: {new_string}")


if __name__ == "__main__":
    solution = Solution()
    solution.convert('PAYPALISHIRING',3)