class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        numPossible = 0

        if len(flowerbed) == 0:
            numPossible = 0
        elif len(flowerbed) == 1:
            if flowerbed[0] == 0:
                numPossible = 1
            else:
                numPossible = 0
        else:
            for i in range(0, len(flowerbed)):
                if flowerbed[i] == 0:
                    if (i == 0) and (flowerbed[0] == 0) and (flowerbed[1] == 0):
                        flowerbed[i] = 1
                        numPossible += 1
                    elif (i == (len(flowerbed) - 1)):
                        if (flowerbed[i] == 0 and flowerbed[i-1] == 0):
                            flowerbed[i] = 1
                            numPossible += 1
                    elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0:
                        flowerbed[i] = 1
                        numPossible += 1

        return n <= numPossible

        

            
            
        