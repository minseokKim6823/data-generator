from PIL import Image
import os
import random

# 배경 이미지 불러오기
# open("C:/Users/김민석/Desktop/data_generator/result6.txt", "w").close()
for i in range(501,601):
    bg = Image.open(f"C:/Users/김민석/Desktop/check6_removed_2.jpg").convert("RGBA")
    bg_width, bg_height = bg.size

    # 텍스트 이미지 파일 경로들
    base_dir = "C:/Users/김민석/Desktop/data_generator/dataset"
    text_images = [
        os.path.join(base_dir, "3words", f"{random.randint(0, 99)}.png"),  # 지급지 상단
        os.path.join(base_dir, "3words", f"{random.randint(0, 99)}.png"),  # 지급지 하단
        os.path.join(base_dir, "4words", f"{random.randint(0, 99)}.png"),  # 주식회사 상단
        os.path.join(base_dir, "4words", f"{random.randint(0, 99)}.png"),  # 주식회사 하단
        os.path.join(base_dir, "symbols", f"{random.randint(0, 99)}.png"),  # 원 기호
        os.path.join(base_dir, "start_serial_numbers", f"{random.randint(0, 99)}.png"),  # 앞
        os.path.join(base_dir, "serial_numbers", f"{random.randint(0, 99)}.png"),  # 시리얼 번호
        os.path.join(base_dir, "year", f"{random.randint(0, 99)}.png"),  # 연
        os.path.join(base_dir, "month", f"{random.randint(0, 99)}.png"),  # 월
        os.path.join(base_dir, "day", f"{random.randint(0, 99)}.png"),  # 일
        os.path.join(base_dir, "title", f"{random.randint(0, 99)}.png"),  # 자기앞수표 표시
        os.path.join(base_dir, "micr2", f"{random.randint(0, 99)}.png"),  # micr 글자2개
        os.path.join(base_dir, "micr3", f"{random.randint(0, 99)}.png"),  # micr 글자3개
        os.path.join(base_dir, "micr9", f"{random.randint(0, 99)}.png"),  # micr 글자9개

        os.path.join(base_dir, "box_stamp1", f"{random.randint(0, 99)}.png"),  # 박스내부 글자 1
        os.path.join(base_dir, "box_stamp2", f"{random.randint(0, 99)}.png"),  # 박스내부 글자 2
        os.path.join(base_dir, "region", f"{random.randint(0, 99)}.png"),  # 지역
        os.path.join(base_dir, "short_space", f"{random.randint(0, 99)}.png"),  # 은행 ex) 상호저축은행중앙회
        os.path.join(base_dir, "rank1", f"{random.randint(0, 99)}.png"),  # 직급
        os.path.join(base_dir, "rank2", f"{random.randint(0, 99)}.png"),  # 직급
        os.path.join(base_dir, "rank3", f"{random.randint(0, 99)}.png"),  # 직급

        os.path.join(base_dir, "name1", f"{random.randint(0, 99)}.png"),  # 상명
    ]

    positions_ratio = [
        (0.16, 0.11, 0.08, 0.035),  # 지급지 상단
        (0.16, 0.58, 0.08, 0.035),  # 지급지 하단
        (0.16, 0.17, 0.11, 0.035),  # 주식회사 상단
        (0.16, 0.7, 0.11, 0.035),  # 주식회사 하단
        (0.25, 0.23, 0.03, 0.08),    # 원 기호
        (0.579, 0.17, 0.02, 0.04),  # 앞
        (0.61, 0.14, 0.2, 0.07),    # 시리얼번호
        (0.7, 0.4, 0.0125, 0.035),  # 년
        (0.76, 0.4, 0.0125, 0.035), # 월
        (0.82, 0.4, 0.0125, 0.035), # 일
        (0.38, 0.05, 0.25, 0.08),   # 자기앞수표 제목
        (0.65, 0.87, 0.05, 0.05),   # micr 글자2개
        (0.26, 0.86, 0.06, 0.05),   # micr 글자3개
        (0.065, 0.85, 0.18, 0.05),   # micr 글자9개
        (0.85, 0.065, 0.12, 0.05),  # 박스내부 글자 1
        (0.85, 0.115, 0.12, 0.05),  # 박스내부 글자 2
        (0.28, 0.57, 0.11, 0.06),  # 지역

        (0.46, 0.615, 0.095, 0.055),  # 은행
        (0.46, 0.67, 0.02, 0.06),  # 직급
        (0.497, 0.67, 0.02, 0.06),  # 직급
        (0.535, 0.67, 0.02, 0.06),  # 직급

        (0.565, 0.615, 0.17, 0.1)  # 성명
    ]


    # 각 텍스트 이미지를 위치에 맞게 붙이기
    for idx, (path, (rx, ry, rw, rh)) in enumerate(zip(text_images, positions_ratio)):
        if not path or not os.path.exists(path):
            continue
        fg = Image.open(path).convert("RGBA")
        x = int(bg_width * rx)
        y = int(bg_height * ry)

        # ✅ 은행명 위치 (idx 4, 5)는 높이 기준 비율 유지 리사이즈
        if idx in [4, 5]:
            target_height = int(bg_height * rh)
            orig_w, orig_h = fg.size
            target_width = int(target_height * (orig_w / orig_h))
        else:
            target_width = int(bg_width * rw)
            target_height = int(bg_height * rh)

        fg_resized = fg.resize((target_width, target_height), Image.LANCZOS)
        bg.paste(fg_resized, (x, y), fg_resized)

    target_height = int(bg_height * 0.05)  # 기준 세로 비율
    amount_target_height = int(bg_height * 0.1)  # 기준 세로 비율
    amount_kor_target_height = int(bg_height * 0.08)  # 기준 세로 비율
    amount_img_path = os.path.join(base_dir, "amount" , f"{random.randint(0, 99)}.png")  # 금액
    amount_img = Image.open(amount_img_path).convert("RGBA")
    amount_width, amount_height = amount_img.size
    amount_ratio = amount_width/amount_height
    amount_target_width = int(amount_target_height * amount_ratio)
    amount_resized = amount_img.resize((amount_target_width, amount_target_height), Image.LANCZOS)
    amount_x= int(bg_width * 0.28)+ random.randint(-2, 2)
    amount_y= int(bg_height * 0.22)+ random.randint(-2, 2)
    bg.paste(amount_resized, (amount_x, amount_y), amount_resized)

    amount_kor_img_path = os.path.join(base_dir, "amountKo", f"{random.randint(0, 99)}.png")  # 금액
    amount_kor_img = Image.open(amount_kor_img_path).convert("RGBA")
    amount_kor_width, amount_kor_height = amount_kor_img.size
    amount_kor_ratio = amount_kor_width / amount_kor_height
    amount_kor_target_width = int(amount_kor_target_height * amount_kor_ratio)
    amount_kor_resized = amount_kor_img.resize((amount_kor_target_width, amount_kor_target_height), Image.LANCZOS)
    amount_kor_x = int(bg_width * 0.28) + random.randint(-2, 2)
    amount_kor_y = int(bg_height * 0.31) + random.randint(-2, 2)
    bg.paste(amount_kor_resized, (amount_kor_x, amount_kor_y), amount_kor_resized)

    bank_target_height = int(bg_height * 0.05)
    bank_img_path = os.path.join(base_dir, "short_bank_names", f"{random.randint(0, 99)}.png")  # 금액
    bank_img = Image.open(bank_img_path).convert("RGBA")
    bank_width,bank_height = bank_img.size
    bank_ratio =bank_width /bank_height
    bank_target_width = int(bank_height * bank_ratio)
    bank_resized = bank_img.resize((bank_target_width, bank_target_height), Image.LANCZOS)
    bank1_x = int(bg_width * 0.28) + random.randint(-2, 2)
    bank1_y = int(bg_height * 0.16) + random.randint(-2, 2)
    bg.paste(bank_resized, (bank1_x, bank1_y), bank_resized)

    bank2_x = int(bg_width * 0.28) + random.randint(-2, 2)
    bank2_y = int(bg_height * 0.7) + random.randint(-2, 2)
    bg.paste(bank_resized, (bank2_x, bank2_y), bank_resized)

    sentences_target_height = int(bg_height * 0.05)
    sentences1_img_path = os.path.join(base_dir, "sentences1", f"{random.randint(0, 99)}.png")  # 금액
    sentences1_img = Image.open(sentences1_img_path).convert("RGBA")
    sentences1_width, sentences1_height = sentences1_img.size
    sentences1_ratio = sentences1_width / sentences1_height
    sentences1_target_width = int(sentences_target_height * sentences1_ratio)
    sentences1_resized = sentences1_img.resize((sentences1_target_width, sentences_target_height), Image.LANCZOS)
    sentences1_x = int(bg_width * 0.23) + random.randint(-2, 2)
    sentences1_y = int(bg_height * 0.39) + random.randint(-2, 2)
    bg.paste(sentences1_resized, (sentences1_x, sentences1_y), sentences1_resized)

    sentences2_img_path = os.path.join(base_dir, "sentences2", f"{random.randint(0, 99)}.png")  # 금액
    sentences2_img = Image.open(sentences2_img_path).convert("RGBA")
    sentences2_width, sentences2_height = sentences2_img.size
    sentences2_ratio = sentences2_width / sentences2_height
    sentences2_target_width = int(sentences_target_height * sentences2_ratio)
    sentences2_resized = sentences2_img.resize((sentences2_target_width, sentences_target_height), Image.LANCZOS)
    sentences2_x = int(bg_width * 0.23) + random.randint(-2, 2)
    sentences2_y = int(bg_height * 0.44) + random.randint(-2, 2)
    bg.paste(sentences2_resized, (sentences2_x, sentences2_y), sentences2_resized)

    sentences3_img_path = os.path.join(base_dir, "sentences1", f"{random.randint(0, 99)}.png")  # 금액
    sentences3_img = Image.open(sentences3_img_path).convert("RGBA")
    sentences3_width, sentences3_height = sentences3_img.size
    sentences3_ratio = sentences3_width / sentences3_height
    sentences3_target_width = int(sentences_target_height * sentences3_ratio)
    sentences3_resized = sentences3_img.resize((sentences3_target_width, sentences_target_height), Image.LANCZOS)
    sentences3_x = int(bg_width * 0.27) + random.randint(-2, 2)
    sentences3_y = int(bg_height * 0.75) + random.randint(-2, 2)
    bg.paste(sentences3_resized, (sentences3_x, sentences3_y), sentences3_resized)

    # 예시 bg 크기 (예: 2480 x 3508)
    # print(f"배경 크기: {bg_width} x {bg_height}")

    position = []

    for rx, ry, rw, rh in positions_ratio:
        x = int(bg_width * rx)
        y = int(bg_height * ry)
        w = int(bg_width * rw)
        h = int(bg_height * rh)

        corners = [
            [x, y],
            [x + w, y],
            [x + w, y + h],
            [x, y + h],
        ]
        # print("position1", corners)
        position.append(corners)

    # 금액 위치 좌표 출력 추가
    amount_corners = [
        [amount_x, amount_y],
        [amount_x + amount_target_width, amount_y],
        [amount_x + amount_target_width, amount_y + amount_target_height],
        [amount_x, amount_y + amount_target_height],
    ]
    position.append(amount_corners)

    # 금액 한글 위치 좌표 출력 추가
    amount_kor_corners = [
        [amount_kor_x, amount_kor_y],
        [amount_kor_x + amount_kor_target_width, amount_kor_y],
        [amount_kor_x + amount_kor_target_width, amount_kor_y + amount_kor_target_height],
        [amount_kor_x, amount_kor_y + amount_kor_target_height],
    ]
    position.append(amount_kor_corners)

    bank1_corners = [
        [bank1_x, bank1_y],
        [bank1_x + bank_target_width, bank1_y],
        [bank1_x + bank_target_width, bank1_y + bank_target_height],
        [bank1_x, bank1_y + bank_target_height],
    ]
    position.append(bank1_corners)

    bank2_corners = [
        [bank2_x, bank2_y],
        [bank2_x + bank_target_width, bank2_y],
        [bank2_x + bank_target_width, bank2_y + bank_target_height],
        [bank2_x, bank2_y + bank_target_height],
    ]
    position.append(bank2_corners)

    sentences1_corners = [
        [sentences1_x, sentences1_y],
        [sentences1_x + sentences1_target_width, sentences1_y],
        [sentences1_x + sentences1_target_width, sentences1_y + sentences_target_height],
        [sentences1_x, sentences1_y + sentences_target_height],
    ]
    position.append(sentences1_corners)

    sentences2_corners = [
        [sentences2_x, sentences2_y],
        [sentences2_x + sentences2_target_width, sentences2_y],
        [sentences2_x + sentences2_target_width, sentences2_y + sentences_target_height],
        [sentences2_x, sentences2_y + sentences_target_height],
    ]
    position.append(sentences2_corners)

    sentences3_corners = [
        [sentences3_x, sentences3_y],
        [sentences3_x + sentences3_target_width, sentences3_y],
        [sentences3_x + sentences3_target_width, sentences3_y + sentences_target_height],
        [sentences3_x, sentences3_y + sentences_target_height],
    ]
    position.append(sentences3_corners)

    transcription = ["지급지 상단", "지급지 하단", "주식회사 상단", "주식회사 하단","원 기호", "앞", "시리얼번호",
                     "년", "월", "일", "자기앞수표 제목", "micr글자 2개","micr글자 3개", "micr글자 9개",
                     "박스내부 글자 1", "박스내부 글자 2", "지역 ", "은행","직급 글자1", "직급 글자2", "직급 글자3",
                     "성명", "금액", "금액 한글", "은행명1","은행명2","금액아래 글자1","금액아래 글자2", "micr코드 위 글자"]

    with open("C:/Users/김민석/Desktop/data_generator/result.txt", "a", encoding="utf-8") as f:
        image_path = f"result/result_ratio{i}.png"
        bg.save(f"C:/Users/김민석/Desktop/data_generator/{image_path}")
        f.write(f"{image_path}\t[")
        for j in range(len(transcription)):
            entry = {
                "transcription": transcription[j],
                "points": position[j]
            }
            # JSON처럼 문자열로 포맷팅
            f.write(f'{{"transcription": "{entry["transcription"]}", "points": {entry["points"]}}}')
            if j!=len(transcription)-1:
                f.write(f',')

        f.write("]\n")

#ch4_test_images/img_61.jpg    [{"transcription": "금액1", "points": [[310, 104], [416, 141], [418, 216], [312, 179]]}, {...}]


