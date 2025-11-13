# 영화관 좌석 예약 프로그램
# 5행 5열(총 25석) 영화관 좌석
# 각 좌석은 처음에 모두 빈 자리('O')로 표시
# 예약된 좌석은 'X'로 표시되며,
# 이미 예약된 좌석은 예약 불가 메시지를 출력

# 좌석 초기화
# seats = [['O','O','O','O','O'],
#     ['O','O','O','O','O'],
#     ['O','O','O','O','O'],
#     ['O','O','O','O','O'],
#     ['O','O','O','O','O']]
seats = []

for j in range(5):
    row = []
    for i in range(5):
        row.append('O')
    seats.append(row)

# 좌석 현황 출력 후
result = '   1  2  3  4  5\n'
for j in range(5):
    result += f'{chr(65 + j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result += '\n'
print(result)

# 예약 여부 입력 받음
rsrv_row = input('좌석을 예약하시겠어요? 행(A~E): ').upper()
rsrv_col = input('좌석을 예약하시겠어요? 열(1~5): ')

# 좌석 예약 처리
posx = ord(rsrv_row) - 65
posy = int(rsrv_col) - 1
seats[posx][posy] = 'X'

# 예약 확인
result = '   1  2  3  4  5\n'
for j in range(5):
    result += f'{chr(65 + j):3s}'
    for i in range(5):
        result += f'{seats[j][i]:3s}'
    result += '\n'
print(f'\n{result}')

# 처리 완료 메세지 출력
print(f'{rsrv_row}{rsrv_col} 좌석이 예약되었습니다!')
