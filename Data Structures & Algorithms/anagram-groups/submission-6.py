class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # act cat -> act
        # stop pots tops -> opst
        # { act: [act, cat], opst: [stop, pots, tops]}

        res = defaultdict(list)

        for s in strs:
            sortedS = ''.join(sorted(s))
            res[sortedS].append(s)

        return list(res.values())