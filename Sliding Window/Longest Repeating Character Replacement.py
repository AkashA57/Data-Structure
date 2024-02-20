"""
Given a string, s, of lowercase English characters and an integer, k, return the length of the longest substring after replacing 
at most k characters with any other lowercase English character so that all the characters in the substring are the same.
"""

def longest_repeating_character_replacement(s, k):
    
    # Replace this placeholder return statement with your code
    len_word = len(s)
    start, end = 0, 1
    hashmap = {s[start]:1}
    result = 1
    max_freq = 1

    while end<len_word:
        if s[end] in hashmap:
            hashmap[s[end]] += 1
        else:
            hashmap[s[end]] = 1

        max_freq = max(max_freq, hashmap[s[end]])
        if max_freq+k>=end-start+1:
            if result<end-start+1:
                result = end-start+1
        else:
            hashmap[s[start]]-=1
            start +=1
        end+=1
    return result

print(longest_repeating_character_replacement("aaacbbbaabab" , 2))


        