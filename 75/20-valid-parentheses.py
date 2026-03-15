# https://leetcode.com/problems/valid-parentheses/

class Solution:
    """
    1. brute force
    time: O(n^2)
    space: O(n)

    simple idea: valid parenheses must always appear in matching pair like () {} or []
    so if the string is valid we can repeatedly remove these matching pairs until nothing if left.
    after removing all, the string should be empty, otherwise string is invalid
    """
    def isValid(self, s: str) -> bool:
        while '()' in s or '{}' in s or '[]' in s: # time: O(n)
            s = s.replace('{}', '') # time: O(n), space: O(n)
            s = s.replace('()', '')
            s = s.replace('[]', '')
        return s == ''
    
    """
    2. stack
    time: O(n)
    space: O(n)


    we use stack to track opening brackets, whenever we see a closing bracket, we simply check whether
    it matches the most recent opening bracket on top of stack
    if match we remove that opening bracket
    if not -> invalid
    and the valid ends with empty stack.

    """
    def isValid(self, s: str) -> bool:
        st = []

        for c in s:
            if c == '(' or c == '[' or c == '{':
                st.append(c)
            else:
                if not st:
                    return False
                if c == ')':
                    if st.pop() != '(':
                        return False
                elif c == ']':
                    if st.pop() != '[':
                        return False
                elif c == '}':
                    if st.pop() != '{':
                        return False
        
        return not st