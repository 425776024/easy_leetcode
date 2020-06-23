class Solution(object):

    def minWindow(self, s, t):
        # http://articles.leetcode.com/finding-minimum-window-in-s-which/
        ls_s, ls_t = len(s), len(t)
        need_to_find = [0] * 256
        has_found = [0] * 256
        min_begin, min_end = 0, -1
        min_window = 100000000000000
        for index in range(ls_t):
            need_to_find[ord(t[index])] += 1
        count, begin = 0, 0
        for end in range(ls_s):
            end_index = ord(s[end])
            if need_to_find[end_index] == 0:
                continue
            has_found[end_index] += 1
            if has_found[end_index] <= need_to_find[end_index]:
                count += 1
            if count == ls_t:
                begin_index = ord(s[begin])
                while need_to_find[begin_index] == 0 or\
                    has_found[begin_index] > need_to_find[begin_index]:
                    if has_found[begin_index] > need_to_find[begin_index]:
                        has_found[begin_index] -= 1
                    begin += 1
                    begin_index = ord(s[begin])
                window_ls = end - begin + 1
                if window_ls < min_window:
                    min_begin = begin
                    min_end = end
                    min_window = window_ls
        # print min_begin, min_end
        if count == ls_t:
            return s[min_begin: min_end + 1]
        else:
            return ''


if __name__ == '__main__':
    s = Solution()
    print s.minWindow('a', 'a')

