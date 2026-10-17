class CombinationIterator:
    def __init__(self, characters: str, combinationLength: int):
        def gen(i=0, data=[]):
            if len(data) == combinationLength:
                yield ''.join(data)
            elif i < len(characters):
                data.append(characters[i])
                yield from gen(i+1)
                data.pop()
                yield from gen(i+1)
        
        self.gen = gen()
        self.nextt = next(self.gen, None)


    def next(self) -> str:
        result, self.nextt = self.nextt, next(self.gen, None)
        return result
        

    def hasNext(self) -> bool:
        return bool(self.nextt)
        


# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()