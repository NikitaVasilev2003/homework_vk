"""Дан массив строк strs. Сгруппируйте анаграммы вместе. Вы можете вернуть ответ в любом порядке.

Анаграмма - это слово или фраза, полученная путем перестановки букв другого слова или фразы,
обычно с использованием всех исходных букв ровно один раз.
"""

from collections import defaultdict


def groupAnagrams(strs: list[str]):
    ans = defaultdict(list)
    for s in strs:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        ans[tuple(count)].append(s)
    return list(ans.values())
