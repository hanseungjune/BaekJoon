# 네오가 기억하는 멜로디는 음악의 끝부분과 처음부분이 이어서 재생된 멜로디일 수 있다
# 음악 제목, 재생이 시작되고 끝난 시각, 악보를 제공
# 멜로디 및 악보는 'C, C#, D, D#, E, F, F#, G, G#, A, A#, B' 12개
# 각 음은 1분에 1개씩 재생된다.
# 음악은 반드시 처음부터 재생
# 음악의 길이보다 재생된 시간이 길때는 처음부터 반복해서 재생
# 반대의 경우에는 재생시간만큼만 재생된다.
# 음악이 00:00을 넘겨서까지 재생되는일 없음
# 일치하는 음악이 여러개면 재생시간이 제일 긴 음악 제목을 반환
# 재생시간도 같으면 먼저 입력된 제목을 반환
# 일치하는 음악이 없으면 "(None)"을 반환한다.

def change(s):
    # 일단 초기화라고 생각하자
    s = s.replace('C#', 'c').replace('D#', 'd').replace('F#', 'f').replace('G#', 'g').replace('A#', 'a')
    return s


def solution(m, musicinfos):
    lst = []
    m = change(m)
    for i in musicinfos:
        i = i.split(',')
        lst.append([
            int(i[1][:2]) * 60 + int(i[1][3:]) - (int(i[0][:2]) * 60 + int(i[0][3:])),  # 재생시간(분)
            i[2],  # 노래제목
            change(i[3])  # 멜로디
        ])

    lst.sort(key=lambda x: (-x[0]))  # 재생시간 내림차순

    # 재생시간에 따라 생성된 악보
    for i in range(len(musicinfos)):
        a = lst[i][0] // len(lst[i][2])  # 몫
        b = lst[i][0] % len(lst[i][2])  # 나머지
        music = lst[i][2] * a + lst[i][2][:b]

        if m in music:
            return lst[i][1]
    else:
        return "(None)"