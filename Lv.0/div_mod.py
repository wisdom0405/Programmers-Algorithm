""" 
문제설명
정수 num1, num2가 매개변수로 주어질 때, num1를 num2로 나눈 나머지를 return 하도록 solution 함수를 완성해주세요.  

제한사항
0 < num1 ≤ 100
0 < num2 ≤ 100
"""

# solution
def solution(num1, num2):
    if (num1 > 0 and num1 <= 100) and (num2 > 0 and num2 <=100):
        answer = num1 % num2
        
    else :  
        answer = False
    
    return answer

print(solution(3,2))
print(solution(10,5))