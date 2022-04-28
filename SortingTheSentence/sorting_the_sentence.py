class Solution:
    def sortSentence(self, s: str) -> str:
        new_list = s.split()
        answer = ''
        
        for index in range(1,len(new_list)+1):
            for word in new_list:
                if int(word[-1]) == index:
                    answer += " "
                    answer += word[:len(word)-1]
                    
                    
        return answer[1:]
        