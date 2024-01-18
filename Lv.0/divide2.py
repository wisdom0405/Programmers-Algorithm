"""
두 수의 나눗셈

문제설명
정수 num1과 num2가 매개변수로 주어질 때, 
num1을 num2로 나눈 값에 1,000을 곱한 후 정수 부분을 return 하도록 soltuion 함수를 완성해주세요.
"""

def solution(num1, num2):
    answer = ((num1 / num2) * 1000)
    return int(answer)

"""
다른사람의 풀이
import math

def solution(num1, num2):
    return math.trunc(num1 / num2 * 1000) 

math.trunc(x)는 주어진 숫자 x의 소수 부분을 제거하고 정수 부분만을 반환하는 함수입니다. 
이 함수는 x를 소수점 이하에서 가장 가까운 정수 방향으로 버린 결과를 반환합니다.
즉, 양의 정수에 대해서는 내림을 하고, 음의 정수에 대해서는 올림을 수행합니다.

math.trunc를 사용할 수 있음을 알게됨.
간단한 문제더라도 단순하게 접근하지 않고
어떤 방법으로도 활용가능한지 다각도로 살펴봐야할 것 같음.
"""