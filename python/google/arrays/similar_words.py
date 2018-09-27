class Solution(object):
    def areSentencesSimilar(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        if len(words1) == 0 and len(words2) == 0:
            return True

        if len(words1) != len(words2):
            return False

        word_mapping = {}

        for pair in pairs:
            if pair[0] in word_mapping:
                word_mapping[pair[0]].append(pair[1])
            else:
                word_mapping[pair[0]] = [pair[1]]

        for i in range(len(words1)):
            if words1[i] == words2[i]:
                continue

            if words1[i] in word_mapping and words2[i] in word_mapping:
                if words2[i] in word_mapping[words1[i]] or words1[i] in word_mapping[words2[i]]:
                    continue
                else:
                    return False
            elif words1[i] in word_mapping:
                if words2[i] not in word_mapping[words1[i]]:
                    return False
            elif words2[i] in word_mapping:
                if words1[i] not in word_mapping[words2[i]]:
                    return False
            else:
                return False

        return True


solution = Solution()



words1 = ["this","summer","thomas","get","actually","actually","rich","and","possess","the","actually","great","and","fine","vehicle","every","morning","he","drives","one","nice","car","around","one","great","city","to","have","single","super","excellent","super","as","his","brunch","but","he","only","eat","single","few","fine","food","as","some","fruits","he","wants","to","eat","an","unique","and","actually","healthy","life"]
words2 = ["this","summer","thomas","get","very","very","rich","and","possess","the","very","fine","and","well","car","every","morning","he","drives","a","fine","car","around","unique","great","city","to","take","any","really","wonderful","fruits","as","his","breakfast","but","he","only","drink","an","few","excellent","breakfast","as","a","super","he","wants","to","drink","the","some","and","extremely","healthy","life"]
pairs = [["good","nice"],["good","excellent"],["good","well"],["good","great"],["fine","nice"],["fine","excellent"],["fine","well"],["fine","great"],["wonderful","nice"],["wonderful","excellent"],["wonderful","well"],["wonderful","great"],["extraordinary","nice"],["extraordinary","excellent"],["extraordinary","well"],["extraordinary","great"],["one","a"],["one","an"],["one","unique"],["one","any"],["single","a"],["single","an"],["single","unique"],["single","any"],["the","a"],["the","an"],["the","unique"],["the","any"],["some","a"],["some","an"],["some","unique"],["some","any"],["car","vehicle"],["car","automobile"],["car","truck"],["auto","vehicle"],["auto","automobile"],["auto","truck"],["wagon","vehicle"],["wagon","automobile"],["wagon","truck"],["have","take"],["have","drink"],["eat","take"],["eat","drink"],["entertain","take"],["entertain","drink"],["meal","lunch"],["meal","dinner"],["meal","breakfast"],["meal","fruits"],["super","lunch"],["super","dinner"],["super","breakfast"],["super","fruits"],["food","lunch"],["food","dinner"],["food","breakfast"],["food","fruits"],["brunch","lunch"],["brunch","dinner"],["brunch","breakfast"],["brunch","fruits"],["own","have"],["own","possess"],["keep","have"],["keep","possess"],["very","super"],["very","actually"],["really","super"],["really","actually"],["extremely","super"],["extremely","actually"]]

print solution.areSentencesSimilar(words1, words2, pairs)
