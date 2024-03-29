"""
각도기

문제설명
각에서 0도 초과 90도 미만은 예각, 90도는 직각,
 90도 초과 180도 미만은 둔각 180도는 평각으로 분류합니다. 
 각 angle이 매개변수로 주어질 때 
 예각일 때 1, 직각일 때 2, 둔각일 때 3, 평각일 때 4를 return하도록 solution 함수를 완성해주세요.

"""

def solution(angle):
    if (angle > 0 and angle < 90) : 
        return 1
    elif angle == 90 :
        return 2
    elif (angle > 90 and angle < 180) :
        return 3
    elif angle == 180 : 
        return 4
    
"""
다른사람 풀이
def solution(angle):
    if angle<=90:
        return 1 if angle<90 else 2
    else:
        return 3 if angle<180 else 4

def solution(angle):
    return 2 if angle==90 else 1 if angle<90 else 4 if angle==180 else 3

더 간결하게 표현가능하다.
"""