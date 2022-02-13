'''
수많은 마라톤 선수들이 마라톤에 참여하였습니다. 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다.
마라톤에 참여한 선수들의 이름이 담긴 배열 participant와 완주한 선수들의 이름이 담긴 배열 completion이 주어질 때, 완주하지 못한 선수의 이름을 return 하도록 solution 함수를 작성해주세요.

[제한사항]
마라톤 경기에 참여한 선수의 수는 1명 이상 100,000명 이하입니다.
completion의 길이는 participant의 길이보다 1 작습니다.
참가자의 이름은 1개 이상 20개 이하의 알파벳 소문자로 이루어져 있습니다.
참가자 중에는 동명이인이 있을 수 있습니다.
'''

# 시간 초과 코드
def solution(participant, completion): 
    answer = ''
    for comp in range(len(completion)): 
        if completion[comp] in participant: 
            participant.remove(completion[comp])
        else:
            answer = completion[comp]
    answer = participant[0]
    return answer


# 딕셔너리로 중복값 관리 
import collections # collections에 내장된 함수인 Counter()는 Dic과 같이 hash형 자료들의 값의 개수를 셀 때 사용

def solution(participant, completion): 
    answer = ''
    part = collections.Counter(participant)
    comp = collections.Counter(completion)

    collect = part - comp # type : collection.Counter
    answer = list(collect)[0]

    return answer

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
solution(participant, completion)