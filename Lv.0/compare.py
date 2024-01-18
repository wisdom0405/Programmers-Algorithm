"""
숫자 비교하기

문제설명
정수 num1, num2가 매개변수로 주어질 때, 
num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.
"""
def solution(num1, num2):
    if num1 == num2 : 
        return 1
    else : 
        return -1
    
"""
다른사람의 풀이

def solution(num1, num2):
    return 1 if num1==num2 else -1

좀 더 간결하게 작성이 가능하다.
"""