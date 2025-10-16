from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def main():
    # Replace with your trained model path
    model = YOLO("runs/detect/train2/weights/best.pt") # by default it is, but if you train more than once, then it will change the path

    # Run evaluation on test set
    model.val(data="config.yaml", split="test")


if __name__ == "__main__":
    main()
