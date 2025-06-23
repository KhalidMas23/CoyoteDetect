import os, random, shutil

SRC_IMG_DIR = "dataset/images/all"
SRC_LBL_DIR = "dataset/labels/all"
TRAIN_IMG_DIR = "dataset/images/train"
VAL_IMG_DIR = "dataset/images/val"
TRAIN_LBL_DIR = "dataset/labels/train"
VAL_LBL_DIR = "dataset/labels/val"
VAL_SPLIT = 0.2

os.makedirs(TRAIN_IMG_DIR, exist_ok=True)
os.makedirs(VAL_IMG_DIR, exist_ok=True)
os.makedirs(TRAIN_LBL_DIR, exist_ok=True)
os.makedirs(VAL_LBL_DIR, exist_ok=True)

images = [f for f in os.listdir(SRC_IMG_DIR) if f.endswith((".jpg", ".png"))]
random.shuffle(images)
val_count = int(len(images) * VAL_SPLIT)

for i, img_name in enumerate(images):
    base = os.path.splitext(img_name)[0]
    label_name = base + ".txt"

    img_src = os.path.join(SRC_IMG_DIR, img_name)
    lbl_src = os.path.join(SRC_LBL_DIR, label_name)

    if not os.path.exists(lbl_src):
        continue  # skip if label missing

    if i < val_count:
        shutil.copy(img_src, VAL_IMG_DIR)
        shutil.copy(lbl_src, VAL_LBL_DIR)
    else:
        shutil.copy(img_src, TRAIN_IMG_DIR)
        shutil.copy(lbl_src, TRAIN_LBL_DIR)

print("✅ Dataset split complete.")
