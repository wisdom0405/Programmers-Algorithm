"""
부분 문자열

문제설명
어떤 문자열 A가 다른 문자열 B안에 속하면 A를 B의 부분 문자열이라고 합니다. 예를 들어 문자열 "abc"는 문자열 "aabcc"의 부분 문자열입니다.

문자열 str1과 str2가 주어질 때, str1이 str2의 부분 문자열이라면 1을 부분 문자열이 아니라면 0을 return하도록 solution 함수를 완성해주세요.

"""
def solution(str1, str2):
    if str1 in str2 : 
        return 1
    else : 
        return 0

"""
+ 추가
.find() 메소드 통해서 부분문자열이 문자열에 존재하는지 확인가능

substring = "zz"
string = "hello world"
print(string.find(substring))

부분문자열이 문자열에 포함되어 있다면 부분문자열 가장 왼쪽의 인덱스를 반환하고,
포함되어 있지 않다면 -1을 반환합니다.
예제에서 결과값은 -1로, ‘zz’는 ‘hello world’에 포함되어 있지 않음을 의미합니다.
"""