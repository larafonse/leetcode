class Solution:
    def romanToInt(self, s: str) -> int:
        # iterate through string
        i = 0
        result = 0

        while i < len(s):
            if s[i] == 'I':
                if i == len(s)-1:
                    result+=1
                elif s[i+1] == 'V':
                    result+=4
                    i+=1
                elif s[i+1] == 'X':
                    result+=9
                    i+=1
                else:
                    result +=1
            elif s[i] == 'V':
                result+=5
            elif s[i] == 'X':
                if i == len(s)-1:
                    result+=10
                elif s[i+1] == 'L':
                    result+=40
                    i+=1
                elif s[i+1] == 'C':
                    result+=90
                    i+=1
                else:
                    result +=10
            elif s[i] == 'L':
                result+=50
            elif s[i] == 'C':
                if i == len(s)-1:
                    result+=100
                elif s[i+1] == 'D':
                    result+=400
                    i+=1
                elif s[i+1] == 'M':
                    result+=900
                    i+=1
                else:
                    result +=100
            elif s[i] == 'D':
                result+=500
            else:
                result+=1000
            i+=1
        return result

# Using map
class Solution:
    def romanToInt(self, s: str) -> int:
        romanToNum = {
            'I':1,
            'V':5,
            'X':10,
            'L':50,
            'C':100,
            'D':500,
            'M':1000,
            'IV':4,
            'IX':9,
            'XL':40,
            'XC':90,
            'CD':400,
            'CM':900,
        }
        i = 0
        result = 0

        while i<len(s):
            if i == len(s)-1:
                result += romanToNum[s[i]]
            elif (s[i]+s[i+1]) in romanToNum:
                result+=romanToNum[s[i]+s[i+1]]
                i+=1
            else:
                result+=romanToNum[s[i]]
            i+=1
        return result