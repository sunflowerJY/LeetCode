"""
Best answer is to created in to use hash table,such as{'a':12,'b':23,'c':13}which we can find the value by key.
Besides,the function of enumerate is awesome,which can return both of the index and content from the list.
"""
class Solution(object):
    def anagramMappings(self, A, B):
        D = {x: i for i, x in enumerate(B)}
        return [D[x] for x in A]