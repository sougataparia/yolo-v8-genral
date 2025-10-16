import os


# Now do the usual imports
from ultralytics import YOLO


os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

def main():
    model = YOLO("cbam_yolo11.yaml")
    # model.train(data="data_set.yaml", epochs=650, batch = 4, patience = 20)
    model.info()

if __name__ == "__main__":
    main()