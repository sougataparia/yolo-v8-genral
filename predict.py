from ultralytics import YOLO
import os

# Optional: Fix OpenMP error (already in your main.py)
os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def main():
    # Load the model from the saved weights
    model = YOLO("runs/detect/train/weights/last.pt")  # or "best.pt"

    # Predict on a test image
    results = model.predict(source="C:/Users/souga/OneDrive/summerInternshipProject/Code/Other_YOLO/YOLOv8/insulator_defect_dataset/images/test", save=True, conf=0.25)

    # Print prediction results (optional)
    for r in results:
        print(r.names)       # class names
        print(r.boxes.xyxy)  # bounding box coordinates
        print(r.boxes.cls)   # class indices
        print(r.boxes.conf)  # confidence scores

if __name__ == "__main__":
    main()
