import sys; sys.stdin=open('input.txt','r')
import itertools
# 연산자가 3개일 경우는 6가지 조합
# 연산자가 2개일 경우는 2가지 조합
# 연산자랑 피연산자 분리부터
# 나머지는 주석을 읽으면서 설명가능

def solution(expression):
    # 연산자만
    cal = []
    # 연산자 피연산자 모두
    res = []
    # 피연산자만
    temp = []
    i = len(expression)
    # 연산자랑 피연산자 분리
    while i >= 0:
        # 뒤에서부터 꺼내면서 앞으로 넣으면 차곡차곡 쌓듯이 정리가 됨
        i -= 1
        # i번째 인덱스에 해당하는 문자열을 꺼내서
        elem = list(expression).pop(i)
        # i가 -1이 되면, 피연산자배열을 숫자로 병합변환해서 res 배열에 넣어주기(stack느낌) - 마무리(정리)(남은게 숫자 뿐일거라서)
        if i == -1:
            number = int(''.join(temp))
            res.insert(0, number)
            # 피연산자 배열 초기화
            temp = []
        # 피연산자인경우, 피연산자 배열에 차곡차곡 넣기
        elif elem not in '+*-':
            temp.insert(0, elem)
        # 연산자인경우, 연산자 배열에 넣고(나중에 검증용), 피연산자배열을 숫자로 병합변환해서 res 배열에 넣어주기(stack느낌)
        elif elem in '+*-':
            cal.append(elem)
            number = int(''.join(temp))
            # 피연산자 넣기
            res.insert(0, number)
            temp = []
            # 연산자 넣기
            res.insert(0, elem)

    # 연산자 경우의 수 뽑기
    # 연산자 중복제거
    lst = list(set(cal))
    ans = []
    # 문제에서 제시한 연산자의 갯수는 1~3개뿐이라서 순열의 경우는 밑에 3가지 방법이면 충분하다.
    if len(lst) == 3:
        ans = itertools.permutations(lst, 3)
    elif len(lst) == 2:
        ans = itertools.permutations(lst, 2)
    elif len(lst) == 1:
        ans = itertools.permutations(lst, 1)
    # 연산자 순열 배열로 따로 넣기(언패킹해서)
    ans = list(ans)

    # 연산자 갯수, 연산자 우선순위 순열
    # for c in cal:
    #     print(c)
    # for an in ans:
    #     print(an)

    # 최대값 초기화
    mx = 0
    # 연산자 순열 꺼내기
    for calculator in ans:
        # 연산자, 피연산자 배열 카피(1차원이라서 가능)
        result = res[::]
        # 연산자 우선순위대로 꺼내기(경우의 수)
        for sequence in calculator:
            # 식에서 꺼내서 계산
            i = -1
            while True:
                # i는 0부터 result-1 길이까지
                i += 1
                # i가 길이가 되면 break해서 다음 연산자 가져오기
                if i == len(result):
                    break
                # result[i]가 내가 찾는 연산자라면, 다음과 같이 계산해주기
                if sequence == result[i]:
                    if sequence == '+':
                        # 우선순위에 따른 계산
                        a = result[i-1] + result[i+1]
                    elif sequence == '-':
                        # 우선순위에 따른 계산
                        a = result[i-1]-result[i+1]
                    elif sequence == '*':
                        # 우선순위에 따른 계산
                        a = result[i-1] * result[i+1]
                    # 3번 없애면 (피연산자)+(연산자)+(피연산자)
                    del result[i-1]
                    del result[i-1]
                    del result[i-1]
                    # a 추가
                    result.insert(i-1, a)
                    # -1 해줘서 원래 자리에서 다시 계산해야함
                    i -= 1
                    # 1개가 되면
                    if len(result) == 1:
                        # 마지막 숫자 꺼내서
                        for element in result:
                            # 절댓값
                            answer = abs(element)
                            # 최대값 구하기
                            if mx < answer:
                                mx = answer
                            break

    return mx

print(solution(expression))