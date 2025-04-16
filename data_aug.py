# 라이브러리 임포트
import albumentations as A  # 이미지 증강용 메인 라이브러리
from albumentations.pytorch import ToTensorV2  # PyTorch 텐서로 변환
import cv2  # 이미지 입출력용 (OpenCV)
import matplotlib.pyplot as plt  # 시각화용 라이브러리
import os

# -------------------------------
# 💡 증강 파이프라인 정의
# -------------------------------
for i in range(1,601):
    transform = A.Compose([

    # 🔹 1. 블러/노이즈 중 하나 랜덤 적용
    A.OneOf([
        A.MotionBlur(p=0.3),  # 카메라 흔들림 효과
        A.MedianBlur(blur_limit=3, p=0.3),  # 중앙값 블러링
        A.GaussianBlur(p=0.3),  # 가우시안 블러
        A.GaussNoise(p=0.3),  # 가우시안 노이즈 추가
    ], p=0.5),  # 위 효과 중 하나를 50% 확률로 적용

    # 🔹 2. 밝기/대비/색상 변형 중 하나 랜덤 적용
    A.OneOf([
        A.RandomBrightnessContrast(p=0.5),  # 밝기와 대비 조절
        A.CLAHE(p=0.3),  # 어두운 부분 강조 (Histogram Equalization)
        A.HueSaturationValue(
            hue_shift_limit=(-100, 100), # 색상
            sat_shift_limit=(-100, 100),  # 채도
            val_shift_limit=(-100, 100),   # 밝기
            p=0.6
        )  # 색조/채도/명도 변화
    ], p=0.5),
        A.RGBShift(r_shift_limit=50, g_shift_limit=0, b_shift_limit=0, p=0.2),
        A.RGBShift(r_shift_limit=0, g_shift_limit=0, b_shift_limit=50, p=0.2),
        A.RGBShift(r_shift_limit=0, g_shift_limit=50, b_shift_limit=0, p=0.2),



    # 🔹 4. 그림자 효과 추가 (스캔 시 조명 대비 표현)
    # A.RandomShadow(p=0.3),  # 임의의 그림자 효과

    # 🔹 5. 이미지 사이즈 고정 (모델 입력용)
    # A.Resize(512, 256),  # 모든 이미지를 512x256으로 resize

    # 🔹 6. 정규화 (평균 0.5, 표준편차 0.5로 스케일링)
    A.Normalize(mean=(0.5,), std=(0.5,)),

    # 🔹 7. PyTorch 텐서로 변환
    ToTensorV2()
    ])

    # -------------------------------
    # 💡 실제 이미지 증강 예시
    # -------------------------------

    # 이미지 불러오기
    image = cv2.imread(f"C:/result/result_ratio{i}.png")  # OpenCV는 BGR로 읽음
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  # RGB로 변환 (matplotlib용)

    # 증강 적용
    augmented = transform(image=image)  # 증강된 결과 딕셔너리 반환
    aug_img = augmented['image'].permute(1, 2, 0).numpy()  # 텐서를 numpy로 변환 및 채널 순서 변환 (HWC)



    # -------------------------------
    # 💾 이미지 저장
    # -------------------------------
    # 정규화 복원 + uint8로 변환
    aug_img_np = (aug_img * 0.5 + 0.5) * 255
    aug_img_np = aug_img_np.astype("uint8")

    # RGB → BGR
    aug_img_bgr = cv2.cvtColor(aug_img_np, cv2.COLOR_RGB2BGR)

    # 저장 경로 지정
    save_path = f"C:/result/augmented6_check{i}.jpg"
    save_path1 = f"result/augmented6_check{i}.jpg"
    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cv2.imwrite(save_path, aug_img_bgr)
    print(f"✅ 이미지 저장 완료: {save_path}")


    # -------------------------------
    # 👀 시각화
    # -------------------------------
    plt.imshow(aug_img_np)
    plt.axis("off")

