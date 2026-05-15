from typing import List
"""
nums = [2,7,11,15]
nums = [3,2,4]
nums = [3,3]

target = 9
target = 6
target = 6
"""

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        def = definir uma função 
        twoSum = nome da função 
        self = pq é uma função dentro de uma classe, ai precisa usar isso
        nums = Lista de inteiros dentro de num
        target = int
        List[int] = retorna uma Lista int
        Cria uma função twoSum que recebe uma lista de inteiros e tem um numero alvo que retorna outra lista de int
        """
        

        for i in range(len(nums)):
          # percorre cada posição da lista
            

            for j in range(i + 1, len(nums)):
                # i + 1 pra não se repetir tipo [2, 7] e [7, 2]

                if nums[i] + nums[j] == target:

                    return [i, j]