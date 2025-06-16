class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        if strs == [""]:
            return [[""]]
        
        my_dict = {}
        for word in strs:
            chars = ''.join(sorted(word))

            if chars not in my_dict:
                my_dict[chars] = []

            my_dict[chars].append(word)

        return list(my_dict.values())

