# L 557 Reverse Words in a String III
 
--- 
 
``` 
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        return ' '.join([word[::-1] for word in s.split(' ')])

 ```