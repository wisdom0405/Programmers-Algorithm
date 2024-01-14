""" 
문제설명 
정수 num1, num2가 매개변수 주어집니다. num1과 num2를 곱한 값을 return 하도록 solution 함수를 완성해주세요.

제한사항
0 ≤ num1 ≤ 100
0 ≤ num2 ≤ 100

 """

# solution
def solution(num1, num2):
    if(num1 >= 0  and num1 <= 100) and (num2 >= 0 and num2 < 100):
        answer = num1 * num2
    
    else:
        answer = False
        
    return answer

print(solution(3,4)) # 12
print(solution(27,19)) # 513