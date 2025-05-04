class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        score = 0
        visited = [0]*len(instructions)
        i=0
        while 0<=i<len(instructions) and visited[i] == 0:
            visited[i]+=1
            if instructions[i] == "add":
                score += values[i]
                i += 1
            elif instructions[i] == "jump":
                i += values[i]
        return score
            
            
