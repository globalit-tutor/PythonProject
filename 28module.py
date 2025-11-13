# 모듈
# 파이썬 코드가 포함된 파일
# 즉, 변수, 함수, 클래스등을 하나의 파일에 담은 것
# 따라서, 이미 만든 기능을 다른 파일에서 다시 사용 가능
# 코드를 기능별로 파일 단위로 나누면 관리가 수월함

# 파이썬 표준 모듈
# 파이썬에서 기본적으로 제공하는 모듈들
# math, random, datetime, os, sys 등등
# 파이썬 셸에서 dir(모듈명) 실행시 함수/상수 조회 가능


# 외부 모듈 - 3rd party
# pip install로 설치해야 사용가능


# 모듈 생성
# 패키지 디렉토리 아래에
# 기능을 의미하는 이름으로 py 파일 작성

# 모듈 가져하기 1
# import 모듈파일명
import zzyzzy.sayhello

# 모듈 기능 호출 1
# 모듈파일명.함수명, 모듈파일명.변수명
print(zzyzzy.sayhello.msg)
zzyzzy.sayhello.greeting()


# 모듈 가져하기 2
# import 모듈파일명 as 별칭
import zzyzzy.sayhello as sh

# 모듈 기능 호출 2
# 별칭.함수명, 별칭.변수명
print(sh.msg)
sh.greeting()


# 모듈 가져하기 2b
# import 모듈파일명 as 별칭
import zzyzzy.sayhello as sayhello

# 모듈 기능 호출 2b
# 별칭.함수명, 별칭.변수명
print(sayhello.msg)
sayhello.greeting()


# 모듈 가져하기 3 (추천!)
# from 패키지.모듈파일명 import 함수명/변수명
from zzyzzy.sayhello import greeting
from zzyzzy.sayhello import msg

# 모듈 기능 호출 3
# 함수명, 변수명
print(msg)
greeting()


# 모듈 가져하기 3b (비추!)
# from 패키지.모듈파일명 import 함수명, 변수명
from zzyzzy.sayhello import greeting, msg

# 모듈 기능 호출 3b
# 함수명, 변수명
greeting()






