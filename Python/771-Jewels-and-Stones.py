class Solution:
    def numJewelsInStones(self, J, S):
        """
        :type J: str
        :type S: str
        :rtype: int
        """
        return len([x for x in S if x in J ])
        



s = Solution()
examples = [
    { "inputJ": "aA", "inputS": "aAAbbbb", "output": 3},
    { "inputJ": "z", "inputS": "ZZ", "output": 0},
]
         
successfulSolution = True
for example in examples:
    if example["output"] != s.numJewelsInStones(example["inputJ"], example["inputS"]):
        successfulSolution = False
    

print("Succesful Solution:", successfulSolution)

    


