class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n =len(instructions) 
        visited = [0]* n
        i = 0 
        score = 0
        while 0<=i<n and not visited[i]:
            visited[i] = True
            if instructions[i] == 'add':
                score += values[i]
                i+=1
            elif instructions[i] == 'jump':
                i += values[i]
        return score

        