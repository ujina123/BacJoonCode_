'''
전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.
구조대 : 119
박준영 : 97 674 223
지영석 : 11 9552 4421
전화번호부에 적힌 전화번호를 담은 배열 phone_book 이 solution 함수의 매개변수로 주어질 때, 어떤 번호가 다른 번호의 접두어인 경우가 있으면 false를 그렇지 않으면 true를 return 하도록 solution 함수를 작성해주세요.

[제한 사항]
phone_book의 길이는 1 이상 1,000,000 이하입니다.
각 전화번호의 길이는 1 이상 20 이하입니다.
같은 전화번호가 중복해서 들어있지 않습니다.
'''

# 24개 test 중에서 하나 실패... 원인 모름 ㅠ
def solution(phone_book):
    answer = True
    
    phone_book.sort()
    
    for phone in range(len(phone_book)-1):
        if phone_book[phone+1].find(phone_book[phone]) != -1:
            answer = False
            break
            
    return answer

# .zip() 과 .startwith() 메서드 사용
'''
> zip은 함수 안의 각 리스트, 튜플, 문자열에 대하여 각 요소를 짝지어 주는 함수
> startwith()
    - str.startswith(str or tuple) 형식으로 사용
    - 대소문자를 구분하고 인자값에 있는 문자열이 string에 있으면 true, 없으면 false를 반환
    - list나 dict을 넣는다면  error
    - 
'''

def solution(phone_book):
    answer = True
    phone_book.sort()
    for zip1, zip2 in zip(phone_book, phone_book[1:]):
        if zip2.startswith(zip1):
            answer = False
    return answer

print(solution(	["123", "456", "789"]))