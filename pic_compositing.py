from PIL import Image
import os
import random
position = []
# 배경 이미지 불러오기
# open("C:/Users/김민석/Desktop/data_generator/result.txt", "w").close()
for i in range(1,501):
    decide_value = random.random()
    q=random.randint(1,5)
    bg = Image.open(f"C:/Users/김민석/Desktop/check{q}_removed_2.jpg").convert("RGBA")
    bg_width, bg_height = bg.size
    test_value = "short_bank_names"
    space = "short_space"
    if q==2:
        test_value, space  = "bank_names", "space"
    value=0
    if q!=3:
        value=0.03
    d_value=True
    # 텍스트 이미지 파일 경로들
    base_dir = "C:/Users/김민석/Desktop/data_generator/dataset"
    text_images = [
        os.path.join(base_dir, "3words", f"{random.randint(0, 99)}.png"),  # 지급지 상단
        os.path.join(base_dir, "3words", f"{random.randint(0, 99)}.png"),  # 지급지 하단
        os.path.join(base_dir, "symbols", f"{random.randint(0, 99)}.png"),  # 원 기호
        os.path.join(base_dir, "start_serial_numbers", f"{random.randint(0, 99)}.png"),  # 앞
        os.path.join(base_dir, "serial_numbers", f"{random.randint(0, 99)}.png"),  # 시리얼 번호
        os.path.join(base_dir, "year", f"{random.randint(0, 99)}.png"),  # 연
        os.path.join(base_dir, "month", f"{random.randint(0, 99)}.png"),  # 월
        os.path.join(base_dir, "day", f"{random.randint(0, 99)}.png"),  # 일
        os.path.join(base_dir, "title", f"{random.randint(0, 99)}.png"),  # 자기앞수표 표시
        os.path.join(base_dir, "micr2", f"{random.randint(0, 99)}.png"),  # micr 글자2개
        os.path.join(base_dir, "micr3", f"{random.randint(0, 99)}.png"),  # micr 글자3개

        os.path.join(base_dir, "micr5", f"{random.randint(0, 99)}.png"),  # micr 글자5개
        os.path.join(base_dir, "micr7", f"{random.randint(0, 99)}.png"),  # micr 글자7개
        os.path.join(base_dir, "micr9", f"{random.randint(0, 99)}.png"),  # micr 글자9개
        os.path.join(base_dir, "micr12", f"{random.randint(0, 99)}.png"),  # micr 글자12개
        os.path.join(base_dir, "box_stamp1", f"{random.randint(0, 99)}.png"),  # 박스내부 글자 1
        os.path.join(base_dir, "box_stamp2", f"{random.randint(0, 99)}.png"),  # 박스내부 글자 2
        os.path.join(base_dir, "region", f"{random.randint(0, 99)}.png"),  # 지역
        os.path.join(base_dir, "stamp1", f"{random.randint(0, 99)}.png"),  # 첫번째로 위에 있는 도장
        os.path.join(base_dir, "stamp2", f"{random.randint(0, 99)}.png"),  # 두번째로 위에 있는 도장
        os.path.join(base_dir, space, f"{random.randint(0, 99)}.png"),  # 은행 ex) 상호저축은행중앙회

        os.path.join(base_dir, "rank1", f"{random.randint(0, 99)}.png"),  # 직급1
        os.path.join(base_dir, "rank2", f"{random.randint(0, 99)}.png"),  # 직급2
        os.path.join(base_dir, "rank3", f"{random.randint(0, 99)}.png"),  # 직급3
        os.path.join(base_dir, "name", f"{random.randint(0, 99)}.png"),  # 상명
        os.path.join(base_dir, "4words", f"{random.randint(0, 99)}.png"),  # 주식회사 상단
        os.path.join(base_dir, "4words", f"{random.randint(0, 99)}.png"),  # 주식회사 하단
    ]




    positions_ratio = [
        (0.16, 0.11, 0.08, 0.035),  # 지급지 상단
        (0.16, 0.58, 0.08, 0.035),  # 지급지 하단
        (0.2, 0.23, 0.06, 0.11),    # 원 기호
        (0.579, 0.17, 0.02, 0.04),  # 앞
        (0.61, 0.14, 0.2, 0.07),    # 시리얼번호
        (0.7, 0.4, 0.0125, 0.035),  # 연
        (0.76, 0.4, 0.0125, 0.035), # 월
        (0.82, 0.4, 0.0125, 0.035), # 일
        (0.38, 0.02, 0.25, 0.08),   # 자기앞수표 제목
        (0.65, 0.87, 0.05, 0.05),   # micr 글자2개
        (0.26, 0.86, 0.06, 0.05),   # micr 글자3개

        (0.53, 0.85, 0.1, 0.045),   # micr 글자5개
        (0.35, 0.86, 0.14, 0.045),   # micr 글자7개
        (0.065, 0.85, 0.18, 0.05),   # micr 글자9개
        (0.72, 0.85, 0.25, 0.05),   # micr 글자12개
        (0.85, 0.065, 0.12, 0.05),  # 박스내부 글자 1
        (0.85, 0.115, 0.12, 0.05),  # 박스내부 글자 2
        (0.31, 0.5, 0.11, 0.06),  # 지역
        (0.47, 0.5, 0.31, 0.06),  # 첫번째로 위에 있는 도장
        (0.47, 0.55, 0.31, 0.06),  # 두번째로 위에 있는 도장
        (0.47, 0.63, 0.13, 0.04),  # 은행

        (0.47, 0.67, 0.02, 0.04),  # 직급1
    ]

    rank2 = (0.525, 0.67, 0.02, 0.04)
    if decide_value <= 0.16:
        rank2 = None
        del text_images[22]
    else:
        positions_ratio.append(rank2) # 직급2

    positions_ratio += [
        (0.58, 0.67, 0.02, 0.04),  # 직급3
        (0.61, 0.64, 0.17, 0.09),  # 성명
    ]
    if decide_value <= 0.16:
        del text_images[24]
        del text_images[24]
    else:
        positions_ratio += [
            (0.16, 0.17, 0.08, 0.035),  # 주식회사 상단
            (0.16, 0.68, 0.11, 0.035)  # 주식회사 하단
        ]

    # 각 텍스트 이미지를 위치에 맞게 붙이기
    for idx, (path, ratio) in enumerate(zip(text_images, positions_ratio)):
        if not path or not os.path.exists(path) or ratio is None:
            continue
        rx, ry, rw, rh = ratio
        fg=""
        fg = Image.open(path).convert("RGBA")
        x = int(bg_width * rx)+ random.randint(-1, 1)
        y = int(bg_height * ry)+ random.randint(-1, 1)

        # ✅ 은행명 위치 (idx 4, 5)는 높이 기준 비율 유지 리사이즈
        if idx in [4, 5]:
            target_height = int(bg_height * rh)
            orig_w, orig_h = fg.size
            target_width = int(target_height * (orig_w / orig_h))
        # ✅ 조건문이 발동된 주식회사 상단/하단에 은행명을 붙일 때는 확대
        elif idx in [2, 3]:
            scale = 1.3
            target_height = int(bg_height * rh * scale)
            orig_w, orig_h = fg.size
            target_width = int(target_height * (orig_w / orig_h))
        else:
            target_width = int(bg_width * rw)
            target_height = int(bg_height * rh)

        fg_resized = fg.resize((target_width, target_height), Image.LANCZOS)
        bg.paste(fg_resized, (x, y), fg_resized)


    count = random.randint(2,4)
    target_height = int(bg_height * 0.05)  # 기준 세로 비율
    amount_target_height = int(bg_height * 0.13)  # 기준 세로 비율
    amount_kor_target_height = int(bg_height * 0.08)  # 기준 세로 비율

    amount_img_path = os.path.join(base_dir, "amount" , f"{random.randint(0, 99)}.png")  # 금액
    amount_img = Image.open(amount_img_path).convert("RGBA")
    amount_width, amount_height = amount_img.size
    amount_ratio = amount_width/amount_height
    amount_target_width = int(amount_target_height * amount_ratio)
    amount_resized = amount_img.resize((amount_target_width, amount_target_height), Image.LANCZOS)
    amount_x= int(bg_width * 0.28)+ random.randint(-1, 1)
    amount_y= int(bg_height * 0.24)+ random.randint(-1, 1)
    bg.paste(amount_resized, (amount_x, amount_y), amount_resized)

    amount_kor_img_path = os.path.join(base_dir, "amountKo" , f"{random.randint(0, 99)}.png")  # 금액
    amount_kor_img = Image.open(amount_kor_img_path).convert("RGBA")
    amount_kor_width, amount_kor_height = amount_kor_img.size
    amount_kor_ratio = amount_kor_width/amount_kor_height
    amount_kor_target_width = int(amount_kor_target_height * amount_kor_ratio)
    amount_kor_resized = amount_kor_img.resize((amount_kor_target_width, amount_kor_target_height), Image.LANCZOS)
    amount_kor_x= amount_x + amount_target_width + 5 + random.randint(-1, 1)
    amount_kor_y= int(bg_height * 0.28)+ random.randint(-1, 1)
    bg.paste(amount_kor_resized, (amount_kor_x, amount_kor_y), amount_kor_resized)

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


    #금액아래 글자1
    sentences1_img_path = os.path.join(base_dir, "sentences1", f"{random.randint(0, 99)}.png")
    sentences1_img = Image.open(sentences1_img_path).convert("RGBA")

    # 비율 유지 리사이즈
    sentences1_width, sentences1_height = sentences1_img.size
    sentences1_ratio = sentences1_width / sentences1_height
    sentences1_target_height = int(bg_height * 0.05)  # 주식회사 단독 크기 비율
    sentences1_target_width = int(sentences1_target_height * sentences1_ratio)
    sentences1_resized = sentences1_img.resize((sentences1_target_width, sentences1_target_height),
                                               Image.LANCZOS)

    # 위치 (amount 기준 근처, 가령 왼쪽 위쪽 위치 지정)
    sentences1_x = int(bg_width * 0.2) + random.randint(-1, 1)
    sentences1_y = int(bg_height * 0.36) + random.randint(-1, 1)
    bg.paste(sentences1_resized, (sentences1_x, sentences1_y), sentences1_resized)

    # 좌표 저장
    sentences1_corners = [
        [sentences1_x, sentences1_y],
        [sentences1_x + sentences1_target_width, sentences1_y],
        [sentences1_x + sentences1_target_width, sentences1_y + sentences1_target_height],
        [sentences1_x, sentences1_y + sentences1_target_height],
    ]
    position.append(sentences1_corners)


    # 금액아래 글자2
    sentences2_img_path = os.path.join(base_dir, "sentences2", f"{random.randint(0, 99)}.png")
    sentences2_img = Image.open(sentences2_img_path).convert("RGBA")

    # 비율 유지 리사이즈
    sentences2_width, sentences2_height = sentences2_img.size
    sentences2_ratio = sentences2_width / sentences2_height
    sentences2_target_height = int(bg_height * 0.05)  # 주식회사 단독 크기 비율
    sentences2_target_width = int(sentences2_target_height * sentences2_ratio)
    sentences2_resized = sentences2_img.resize((sentences2_target_width, sentences2_target_height),
                                               Image.LANCZOS)

    # 위치 (amount 기준 근처, 가령 왼쪽 위쪽 위치 지정)
    sentences2_x = int(bg_width * 0.2) + random.randint(-1, 1)
    sentences2_y = int(bg_height * 0.41) + random.randint(-1, 1)
    bg.paste(sentences2_resized, (sentences2_x, sentences2_y), sentences2_resized)

    # 좌표 저장
    sentences2_corners = [
        [sentences2_x, sentences2_y],
        [sentences2_x + sentences2_target_width, sentences2_y],
        [sentences2_x + sentences2_target_width, sentences2_y + sentences2_target_height],
        [sentences2_x, sentences2_y + sentences2_target_height],
    ]
    position.append(sentences2_corners)


    # micr위 글자
    sentences3_img_path = os.path.join(base_dir, "sentences1", f"{random.randint(0, 99)}.png")
    sentences3_img = Image.open(sentences3_img_path).convert("RGBA")

    # 비율 유지 리사이즈
    sentences3_width, sentences3_height = sentences3_img.size
    sentences3_ratio = sentences3_width / sentences3_height
    sentences3_target_height = int(bg_height * 0.04)  # 주식회사 단독 크기 비율
    sentences3_target_width = int(sentences3_target_height * sentences3_ratio)
    sentences3_resized = sentences3_img.resize((sentences3_target_width, sentences3_target_height),
                                               Image.LANCZOS)

    # 위치 (amount 기준 근처, 가령 왼쪽 위쪽 위치 지정)
    sentences3_x = int(bg_width * 0.28) + random.randint(-1, 1)
    sentences3_y = int(bg_height * 0.73) + random.randint(-1, 1)
    bg.paste(sentences3_resized, (sentences3_x, sentences3_y), sentences3_resized)

    # 좌표 저장
    sentences3_corners = [
        [sentences3_x, sentences3_y],
        [sentences3_x + sentences3_target_width, sentences3_y],
        [sentences3_x + sentences3_target_width, sentences3_y + sentences3_target_height],
        [sentences3_x, sentences3_y + sentences3_target_height],
    ]
    position.append(sentences3_corners)


    #여기에 추가
    corporation1_img_path = os.path.join(base_dir, "bank_names", f"{random.randint(0, 99)}.png")
    corporation1_img = Image.open(corporation1_img_path).convert("RGBA")

    # 비율 유지 리사이즈
    corporation1_width, corporation1_height = corporation1_img.size
    corporation1_ratio = corporation1_width / corporation1_height
    corporation1_target_height = int(bg_height * 0.05)  # 주식회사 단독 크기 비율
    corporation1_target_width = int(corporation1_target_height * corporation1_ratio)
    corporation1_resized = corporation1_img.resize((corporation1_target_width, corporation1_target_height), Image.LANCZOS)

    # 위치 (amount 기준 근처, 가령 왼쪽 위쪽 위치 지정)
    if decide_value<=0.16:
        corporation1_x = int(bg_width * 0.16) + random.randint(-1, 1)
        corporation1_y = int(bg_height * 0.14) + random.randint(-1, 1)
    else:
        corporation1_x = int(bg_width * 0.28) + random.randint(-1, 1)
        corporation1_y = int(bg_height * 0.16) + random.randint(-1, 1)
    bg.paste(corporation1_resized, (corporation1_x, corporation1_y), corporation1_resized)

    # 좌표 저장
    corporation1_corners = [
        [corporation1_x, corporation1_y],
        [corporation1_x + corporation1_target_width, corporation1_y],
        [corporation1_x + corporation1_target_width, corporation1_y + corporation1_target_height],
        [corporation1_x, corporation1_y + corporation1_target_height],
    ]
    position.append(corporation1_corners)


    # 여기에 추가
    corporation2_img_path = os.path.join(base_dir, "bank_names", f"{random.randint(0, 99)}.png")
    corporation2_img = Image.open(corporation2_img_path).convert("RGBA")

    # 비율 유지 리사이즈
    corporation2_width, corporation2_height = corporation2_img.size
    corporation2_ratio = corporation2_width / corporation2_height
    corporation2_target_height = int(bg_height * 0.05)  # 주식회사 단독 크기 비율
    corporation2_target_width = int(corporation2_target_height * corporation2_ratio)
    corporation2_resized = corporation2_img.resize((corporation2_target_width, corporation2_target_height), Image.LANCZOS)

    # 위치 (amount 기준 근처, 가령 왼쪽 위쪽 위치 지정)
    if decide_value <= 0.16:
        corporation2_x = int(bg_width * 0.16) + random.randint(-1, 1)
        corporation2_y = int(bg_height * 0.61) + random.randint(-1, 1)
    else:
        corporation2_x = int(bg_width * 0.28) + random.randint(-1, 1)
        corporation2_y = int(bg_height * 0.68) + random.randint(-1, 1)
    bg.paste(corporation2_resized, (corporation2_x, corporation2_y), corporation2_resized)

    # 좌표 저장
    corporation2_corners = [
        [corporation2_x, corporation2_y],
        [corporation2_x + corporation2_target_width, corporation2_y],
        [corporation2_x + corporation2_target_width, corporation2_y + corporation2_target_height],
        [corporation2_x, corporation2_y + corporation2_target_height],
    ]
    position.append(corporation2_corners)


    transcription = ["지급지 상단", "지급지 하단","원 기호", "앞", "시리얼번호", "년", "월", "일","자기앞수표 제목",
                     "micr글자 2개", "micr글자 3개", "micr글자 5개", "micr글자 7개","micr글자 9개", "micr글자 12개","박스내부 글자 1",
                     "박스내부 글자 2", "지역 ", "첫 번째로 위에 있는 도장","두 번째로 위에 있는 도장", "은행", "직급 글자1"]
    if decide_value>0.16:
        transcription +=["직급 글자2"]
    transcription +=["직급 글자3", "성명"]
    if decide_value > 0.16:
        transcription += ["주식회사 상단", "주식회사 하단"]
    transcription+=["금액","한글 금액", "금액아래 글자1", "금액아래 글자2","micr위 글자"]

    transcription.append("은행명 상단")
    transcription.append("은행명 하단")

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


