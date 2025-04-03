from ultralytics import YOLO

# 모델 불러오기
model = YOLO("yolo11n.pt")  # 사전 학습된 YOLO11n 모델

# 이미지 목록에 대해 배치 추론 실행
# 디렉토리(워크스페이스)에 사진 있어야함
results = model(["truck.jpg", "bus.jpg"])  # Results 객체의 리스트 반환
# results = model(["image1.jpg"])

# 결과 리스트 처리
for result in results:
    boxes = result.boxes  # 경계 상자 출력에 대한 Boxes 객체
    masks = result.masks  # 세분화 마스크 출력에 대한 Masks 객체
    keypoints = result.keypoints  # 포즈 출력에 대한 keypoints 객체
    probs = result.probs  # 분류 출력에 대한 Probs 객체
    obb = result.obb  # OBB 출력에 대한 Oriented boxes 객체
    result.show()  # 화면에 표시
    result.save(filename="result.jpg")  # 디스크에 저장

# cmd에서 python ./실행파일명
