# mod2.py
PI = 3.141592


class Math:
    # self 는 자기 자신
    def solv(self, r):
        return PI * (r**2)


###클래스 정의 끝


# 이건 클래스와 상관 없음
def sum(a, b):
    return a + b


#  파일을 집접 실행(main으로 실행) 시에는 실행하고
# import 시에는 실행하지 않는 조건
if __name__ == "__main__":  # 안쓰면 라이브러리고 모듈 가져다 쓸때 실행이됨
    print(PI)
    a = Math()
    print(a.solv(2))
    print(sum(PI, 4.4))

# ###############3
# cmd
# python
# import sys
# sys.path
# sys.append()
# sys.path.remove(os.getcwd())
