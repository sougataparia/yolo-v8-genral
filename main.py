from ultralytics import YOLO
import os
os.environ["KMP_DUPLICATE_LIB_OK"]="TRUE"

def main():
    # Train a new YOLO model from scratch
    model = YOLO("yolov8n.pt")
    # Train the model using the custom dataset for optimum epochs with early stopping
    results = model.train(data="config.yaml", epochs=650, batch=4, patience = 20)



if __name__ == '__main__':
    # Important to avoid multiprocessing RuntimeError on Windows
    main()