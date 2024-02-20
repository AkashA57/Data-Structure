"""
Given two strings, str1 and str2, find the shortest substring in str1 such that str2 is a subsequence of that substring.
str1 = “abbcb”
str2 = “ac”
output: “abbc”
"""

def min_window(str1, str2):
    
    # Replace this placeholder return statement with your code
    len_str1 = len(str1)
    len_str2 = len(str2)
    result = ""
    if len_str1<len_str2:
        return result

    for index in range(len_str2-1, len_str1):
        if str1[index]==str2[-1]:
            backtrack_index = index-1
            str2_index = len_str2-2
            while backtrack_index>-1 and str2_index>-1:
                if str1[backtrack_index]==str2[str2_index]:
                    str2_index -= 1
                backtrack_index -= 1
            if str2_index == -1 and (len(result)<1 or len(result)>index-backtrack_index):
                result = str1[backtrack_index+1:index+1]
    return result

print(min_window("afgegrwgwga", "aa"))

