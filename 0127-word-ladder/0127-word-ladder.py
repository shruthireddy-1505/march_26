class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        st = set(wordList)
        if endWord not in st:
            return 0
        q = [(beginWord,1)]
        while q:
            word,step = q.pop(0)
            if word == endWord:
                return step
            for i in range(len(word)):
                org = word[i]
                for ch in range(ord('a'),ord('z')+1):
                    word = word[:i]+chr(ch)+word[i+1:]
                    if word in st:
                        st.remove(word)
                        q.append((word,step+1))
                word = word[:i]+org+word[i+1:]
            
        return 0

    