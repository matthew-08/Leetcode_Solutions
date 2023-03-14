class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:

        string = str(num)
        l = 0
        strHold = ""
        result = 0

        for i in range(len(string)):
            strHold += string[i]
            if i >= k - 1:
                if(int(strHold) != 0):
                    if (num/int(strHold)).is_integer():
                        result += 1
                strHold = strHold[1:]
        return result
            
