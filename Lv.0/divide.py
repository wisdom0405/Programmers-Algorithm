"""
몫 구하기

문제설명
정수 num1, num2가 매개변수로 주어질 때, 
num1을 num2로 나눈 몫을 return 하도록 solution 함수를 완성해주세요.

"""

def solution(num1, num2):
    answer = num1 // num2
    return answer

"""
다른사람의 풀이1
def solution(num1, num2):
    return divmod(num1, num2)[0]

 divmod는 목과 나머지를 구할 수 있다.
 [0]이 몫, [1]이 나머지   

다른사람의 풀이2
def solution(num1, num2):
    answer = int(num1/num2)
    return answer

int를 사용하여 소수점을 날린다.
"""