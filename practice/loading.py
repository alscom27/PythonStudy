import time

# end="" 옵션 = 자동개행되던 print를 개행되지 않게 해줌
# flush=True 옵션 = 출력이 강제로 바로 날 수 있게 해줌


def loading():
    for num in range(3):
        print(".", end="", flush=True)
        time.sleep(0.5)


loading()
