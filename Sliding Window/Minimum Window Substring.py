"""
Given two strings, s and t, find the minimum window substring in s, which has the following properties:

It is the shortest substring of s that includes all of the characters present in t.
It must contain at least the same frequency of each character as in t.
The order of the characters does not matter here.
"""

def min_window(s, t):
    if t == "":
        return ""
    
    req_count = {}
    window = {}

    for c in t:
        req_count[c] = 1 + req_count.get(c, 0)
        window[c] = 0

    current, required = 0, len(req_count)
    
    res, res_len = [-1, -1], float("infinity")
    
    left = 0
    for right in range(len(s)):
        c = s[right]

        if c in t:
            window[c] = 1 + window.get(c, 0)

        if c in req_count and window[c] == req_count[c]:
            current += 1

        while current == required:
            if (right - left + 1) < res_len:
                res = [left, right]
                res_len = (right - left + 1)
            
            if s[left] in t:
                window[s[left]] -= 1

            if s[left] in req_count and window[s[left]] < req_count[s[left]]:
                current -= 1
            left += 1
    left, right = res

    return s[left:right+1] if res_len != float("infinity") else ""

print(min_window("ABCD" , "ABC"))