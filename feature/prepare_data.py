import os
import cv2
import numpy as np
import tensorflow as tf

# ضبط مسارات البيانات
emotion_path = "frame_datasets"
sport_path = "frame_sport"

# تصنيفات المشاعر والحركات
emotion_classes = ["colere", "Degout", "Fatigue", "Joie", "peur", "Suprise", "tristesse"]
sport_classes = ["course", "kick", "punch", "sout"]

# حجم الصور الموحد للنموذج
IMG_SIZE = (224, 224)


def load_images_from_folder(folder_path, classes):
    images = []
    labels = []

    for label, category in enumerate(classes):
        class_path = os.path.join(folder_path, category)

        if not os.path.exists(class_path):
            print(f"⚠ المجلد {category} غير موجود! يتم تخطيه...")
            continue

        for img_name in os.listdir(class_path):
            img_path = os.path.join(class_path, img_name)
            img = cv2.imread(img_path)

            if img is None:
                print(f"❌ فشل تحميل الصورة: {img_path}")
                continue

            # تغيير الحجم إلى 224x224 وتحويل BGR إلى RGB
            img = cv2.resize(img, IMG_SIZE)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            images.append(img)
            labels.append(label)

    return np.array(images), np.array(labels)


# تحميل بيانات المشاعر
print("🔍 تحميل بيانات المشاعر...")
emotion_images, emotion_labels = load_images_from_folder(emotion_path, emotion_classes)

# تحميل بيانات الحركات الرياضية
print("🔍 تحميل بيانات الحركات الرياضية...")
sport_images, sport_labels = load_images_from_folder(sport_path, sport_classes)

# حفظ البيانات بتنسيق NumPy لاستخدامها في التدريب لاحقًا
np.save("emotion_images.npy", emotion_images)
np.save("emotion_labels.npy", emotion_labels)
np.save("sport_images.npy", sport_images)
np.save("sport_labels.npy", sport_labels)

print("✅ تم تجهيز البيانات بنجاح!")