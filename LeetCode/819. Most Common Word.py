class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        p = paragraph.replace("."," ").replace(","," ").replace("!"," ").replace("?"," ").replace("'"," ").replace(";"," ")
        p_new = p.replace("  "," ")
        print(p_new)
        lp = p_new.split(" ")
        if "" in lp:
            lp.remove("")
        print(lp)
        c = {}
        for i in lp:
            if i.lower() in c:
                c[i.lower()] += 1
            else:
                c[i.lower()] = 1

        for i in banned:
            if i in c:
                del c[i]

        print(c)
        #sort_c = sorted(c.values())
        sort_c = dict(sorted(c.items(), key=lambda item: item[1], reverse=True))
        return next(iter(sort_c))
      
            
        
