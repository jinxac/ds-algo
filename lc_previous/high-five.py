class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        result = []
        temp_map = {}
        
        for row in items:
            student_id = row[0]
            student_score = row[1]
            
            if student_id in temp_map:
                temp_map[student_id].append(student_score)
            else:
                temp_map[student_id] = [student_score]
        
        for key, val in temp_map.items():
            temp = []
            val.sort(reverse=True) 
            temp.append(key)
            total = 0
            count = 0
            for i in range(0, len(val)):
                if i == 5:
                    break
                total += val[i]
                count += 1
            avg = total//count
            temp.append(avg)
            result.append(temp)
        
        return result
            
