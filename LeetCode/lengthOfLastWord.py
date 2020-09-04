
class Solution(object):  # 最后一个单词的长度
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.strip()
        if len(s) == 0:
            return 0
        if s.find(' ') < 0:
            return len(s)

        node = s.split(' ')
        return len(node[-1])


if __name__ == '__main__':
    print(Solution.lengthOfLastWord(Solution.__class__, '11'))
