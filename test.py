# 推理代码
from ultralytics import YOLO
yolo = YOLO("./yolov8n.pt", task="detect") # 也可以换为seg
result = yolo(source="./ultralytics/assets/bus.jpg", save=True) # save=False
