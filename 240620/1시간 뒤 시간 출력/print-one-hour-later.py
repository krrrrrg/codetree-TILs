# 입력 받기
a = input()

# 시간과 분을 분리
h, m = a.split(':')

# 정수로 변환
h = int(h)
m = int(m)

# 1시간 뒤 계산
h += 1
if h == 24:
    h = 0

# 형식에 맞추어 출력
print(f"{h}:{m:02}")