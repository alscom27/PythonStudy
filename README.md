## 🔗 모델 파일 다운로드

GitHub의 파일 크기 제한(100MB)으로 인해 일부 사전학습 모델은 별도로 제공됩니다.

아래 링크에서 각 모델을 다운로드한 뒤, 해당 경로에 파일을 배치해주세요:

| 모델 이름 | 다운로드 링크 | 저장 위치 |
|-----------|----------------|------------|
| YOLOv3 Weights | [Google Drive](https://drive.google.com/uc?id=YOUR_FILE_ID) | `opencv-4/yolo_v3/yolov3.weights` |
| EAST Text Detection Model | [Dropbox](https://www.dropbox.com/s/r2png0l3zt8hxs/frozen_east_text_detection.tar.gz?dl=1) | `opencv-4/EAST/frozen_east_text_detection.pb` |
| Mask R-CNN Model (TensorFlow) | [HuggingFace](https://huggingface.co/USERNAME/MODEL_NAME) | `opencv-4/mask_rcnn/frozen_inference_graph.pb` |
| Mask R-CNN Config (.pbtxt) | [OpenCV GitHub](https://github.com/opencv/opencv_extra/blob/master/testdata/dnn/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt) | `opencv-4/mask_rcnn/mask_rcnn_inception_v2_coco_2018_01_28.pbtxt` |
| COCO Class Names | [COCO Labels](https://raw.githubusercontent.com/amikelive/coco-labels/master/coco-labels-paper.txt) | `opencv-4/mask_rcnn/coco_90.names` |

> 📦 압축 파일의 경우, 압축을 해제한 뒤 `.pb`만 사용해 주세요.

