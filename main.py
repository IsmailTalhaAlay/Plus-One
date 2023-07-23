class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        self.a = ''
        self.List = []
        for i in digits:
            self.a = self.a + str(i)
        self.variable = int(self.a) + 1
        print(self.variable)
        for r in (str(self.variable)):
            self.List.append(int(r))
        return (self.List)