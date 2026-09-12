# Problem: Longest Substring of One Repeating Character
# Topic: Array
# Difficulty: Hard
from typing import List
from sortedcontainers import SortedList
import bisect


class Solution:
    def longestRepeating(self, s: str, queryCharacters: str, queryIndices: List[int]) -> List[int]:
        # convert the string into a list of (end_index, char) runs and a SortedList of run lengths
        n = len(s)
        if n == 0:
            return []

        arr = []  # list of (end_index, char)
        lengths = SortedList()

        # build runs
        character = s[0]
        count = 1
        for i in range(1, n):
            if s[i] == character:
                count += 1
            else:
                lengths.add(count)
                arr.append((i - 1, character))
                character = s[i]
                count = 1
        # last run
        lengths.add(count)
        arr.append((n - 1, character))

        def bin_search_index(idx):
            l, r = 0, len(arr) - 1
            while l <= r:
                mid = (l + r) // 2
                if arr[mid][0] < idx:
                    l = mid + 1
                elif arr[mid][0] > idx:
                    r = mid - 1
                else:
                    return mid
            return l

        ans = []
        s_list = list(s)

        for q_char, q_index in zip(queryCharacters, queryIndices):
            # find current run containing q_index
            pos = bin_search_index(q_index)
            cur_end, cur_char = arr[pos]
            prev_end, prev_char = arr[pos - 1] if pos - 1 >= 0 else (-1, '')
            next_end, next_char = arr[pos + 1] if pos + 1 < len(arr) else (n, '')

            if s_list[q_index] == q_char:
                ans.append(lengths[-1])
                continue

            # remove current run length
            cur_len = cur_end - prev_end
            lengths.remove(cur_len)

            # compute left/new/right lengths
            left_len = q_index - (prev_end + 1)
            right_len = cur_end - q_index

            # remove current run from arr
            arr.pop(pos)

            insert_at = pos
            # left part
            if left_len > 0:
                arr.insert(insert_at, (q_index - 1, cur_char))
                lengths.add(left_len)
                insert_at += 1

            # insert new single-char run
            arr.insert(insert_at, (q_index, q_char))
            lengths.add(1)
            insert_at += 1

            # right part
            if right_len > 0:
                arr.insert(insert_at, (cur_end, cur_char))
                lengths.add(right_len)

            # try merge with left neighbor
            left_idx = pos - 1 if left_len > 0 else pos - 1
            # find actual index of the new run (it may have shifted)
            # new_run_idx is where arr has end == q_index
            # scan around pos for safety (runs are small)
            new_run_idx = None
            for k in range(max(0, pos - 1), min(len(arr), pos + 3)):
                if arr[k][0] == q_index:
                    new_run_idx = k
                    break

            # merge left
            if new_run_idx is not None and new_run_idx - 1 >= 0 and arr[new_run_idx - 1][1] == q_char:
                left_e, left_c = arr[new_run_idx - 1]
                left_start = (arr[new_run_idx - 2][0] + 1) if new_run_idx - 2 >= 0 else 0
                left_len_actual = left_e - (left_start - 1) if False else None  # placeholder not used
                # compute left length from ends
                prev_prev_end = arr[new_run_idx - 2][0] if new_run_idx - 2 >= 0 else -1
                left_length = left_e - prev_prev_end
                # remove left and new lengths
                lengths.remove(left_length)
                lengths.remove(1)
                # update merged run end to q_index
                arr[new_run_idx - 1] = (q_index, q_char)
                lengths.add(left_length + 1)
                # remove the new run entry
                arr.pop(new_run_idx)
                new_run_idx = new_run_idx - 1

            # merge right
            if new_run_idx is not None and new_run_idx + 1 < len(arr) and arr[new_run_idx + 1][1] == q_char:
                right_e, right_c = arr[new_run_idx + 1]
                next_prev_end = arr[new_run_idx - 1][0] if new_run_idx - 1 >= 0 else -1
                right_length = right_e - (arr[new_run_idx][0])
                # remove current and right lengths
                lengths.remove(arr[new_run_idx][0] - (arr[new_run_idx - 1][0] if new_run_idx - 1 >= 0 else -1))
                lengths.remove(right_length)
                # extend current run end to right_e
                arr[new_run_idx] = (right_e, q_char)
                lengths.add((arr[new_run_idx][0] - (arr[new_run_idx - 1][0] if new_run_idx - 1 >= 0 else -1)))
                # remove right run entry
                arr.pop(new_run_idx + 1)

            # update s_list
            s_list[q_index] = q_char

            ans.append(lengths[-1])

        return ans


if __name__ == '__main__':
    print(Solution().longestRepeating("babacc", "bcb", [1, 3, 3]))  # Output: [3, 3, 4]
