import os, random, shutil

def split_and_copy(src_img, src_lbl, dst_img_train, dst_img_val, dst_lbl_train, dst_lbl_val, val_split=0.2):
    os.makedirs(dst_img_train, exist_ok=True)
    os.makedirs(dst_img_val, exist_ok=True)
    os.makedirs(dst_lbl_train, exist_ok=True)
    os.makedirs(dst_lbl_val, exist_ok=True)

    images = [f for f in os.listdir(src_img) if f.lower().endswith(('.jpg', '.jpeg', '.png'))]
    random.shuffle(images)
    val_count = int(len(images) * val_split)

    for i, img in enumerate(images):
        base = os.path.splitext(img)[0]
        label = base + ".txt"
        img_src = os.path.join(src_img, img)
        lbl_src = os.path.join(src_lbl, label)

        if not os.path.exists(lbl_src):
            print(f"⚠️  Missing label for {img}, skipping.")
            continue

        if i < val_count:
            shutil.copy(img_src, dst_img_val)
            shutil.copy(lbl_src, dst_lbl_val)
        else:
            shutil.copy(img_src, dst_img_train)
            shutil.copy(lbl_src, dst_lbl_train)

# ✅ CORRECTED PATHS — use the /all subfolders
split_and_copy(
    "dataset/day/images/all", "dataset/day/labels/all",
    "dataset/day/images/train", "dataset/day/images/val",
    "dataset/day/labels/train", "dataset/day/labels/val"
)

split_and_copy(
    "dataset/night/images/all", "dataset/night/labels/all",
    "dataset/night/images/train", "dataset/night/images/val",
    "dataset/night/labels/train", "dataset/night/labels/val"
)

print("✅ Day and night datasets split.")
