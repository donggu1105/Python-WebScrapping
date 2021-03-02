 # 주민등록번호
# 941105-1009920

import re
# abcd, book, desk
# ca?e

p = re.compile("ca.e") # 어떤 정규식을 컴파일할껀지 정하는거임

# . (ca.e) : 하나의 문자를 의미  ex] care, cafe, cave , case | caffe (X)
# ^ (^de) : 문자열의 시작  ex] desk , destination | fade (X)
# $ (se$) : 문자열의 끝 ex] case , base | face (X)



def print_match(m):
    if m:
        print("m.group() - " + m.group()) # 일치하는 문자열 반환
        print("m.string() - " + m.string) # 입력받은 문자열
        print("m.start() - ", m.start()) # 일치하는 문자열의 시작 index
        print("m.end() - " , m.end()) # 일치하는 문자열의 끝 index
        print("m.span() - " , m.span()) # 일치하는 문자열의 시작과 끝 index

    else:
        print("매칭되지 않았습니다.")


# m = p.match("careless")  # match : 주어진 문자열의 처음부터 일치하는지 확인
# print_match(m)

m = p.search("goodcare") # search : 주어진 문자열 중에 일치하는게 있는지 확인
print_match(m)

lst = p.findall("good care cafe case") # findall : 일치하는 모든 것을 리스트 형태로 반환
print(lst)


# 1. p = re.compile("원하는 형태") p는 pattern으로 보통 씀

# . (ca.e) : 하나의 문자를 의미  ex] care, cafe, cave , case | caffe (X)
# ^ (^de) : 문자열의 시작  ex] desk , destination | fade (X)
# $ (se$) : 문자열의 끝 ex] case , base | face (X)

# m = p.match()
# m = p.search()
# m = p.findall()