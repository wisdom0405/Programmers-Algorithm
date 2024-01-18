"""
배열의 평균값

정수 배열 numbers가 매개변수로 주어집니다. 
numbers의 원소의 평균값을 return하도록 solution 함수를 완성해주세요.

"""

def solution(numbers):
    answer = 0
    array_sum = 0
    for i in range(len(numbers)) :
        array_sum += numbers[i]
    
    answer = array_sum / len(numbers)
    
    return answer

"""
다른사람의 풀이

import numpy as np
def solution(numbers):
    return np.mean(numbers)

    
def solution(numbers):
    return sum(numbers) / len(numbers)

numpy라이브러리 사용을 하거나 sum을 이용하면 더 간편해진다
"""