import cv2
import json
import matplotlib.pyplot as plt

# 경로
image_path = "C:/Users/Public/result_ratio546.png"

# transcription + points가 있는 json-like 문자열이 있는 .txt 파일을 따로 분리해서도 가능
json_data = '''
	[{"transcription": "지급지 상단", "points": [[140, 42], [210, 42], [210, 55], [140, 55]]},{"transcription": "지급지 하단", "points": [[140, 222], [210, 222], [210, 235], [140, 235]]},{"transcription": "주식회사 상단", "points": [[140, 65], [236, 65], [236, 78], [140, 78]]},{"transcription": "주식회사 하단", "points": [[140, 268], [236, 268], [236, 281], [140, 281]]},{"transcription": "원 기호", "points": [[219, 88], [245, 88], [245, 118], [219, 118]]},{"transcription": "앞", "points": [[508, 65], [525, 65], [525, 80], [508, 80]]},{"transcription": "시리얼번호", "points": [[535, 53], [710, 53], [710, 79], [535, 79]]},{"transcription": "년", "points": [[614, 153], [624, 153], [624, 166], [614, 166]]},{"transcription": "월", "points": [[667, 153], [677, 153], [677, 166], [667, 166]]},{"transcription": "일", "points": [[719, 153], [729, 153], [729, 166], [719, 166]]},{"transcription": "자기앞수표 제목", "points": [[333, 19], [552, 19], [552, 49], [333, 49]]},{"transcription": "micr글자 2개", "points": [[570, 333], [613, 333], [613, 352], [570, 352]]},{"transcription": "micr글자 3개", "points": [[228, 329], [280, 329], [280, 348], [228, 348]]},{"transcription": "micr글자 9개", "points": [[57, 325], [215, 325], [215, 344], [57, 344]]},{"transcription": "박스내부 글자 1", "points": [[746, 24], [851, 24], [851, 43], [746, 43]]},{"transcription": "박스내부 글자 2", "points": [[746, 44], [851, 44], [851, 63], [746, 63]]},{"transcription": "지역 ", "points": [[245, 218], [341, 218], [341, 240], [245, 240]]},{"transcription": "은행", "points": [[403, 235], [486, 235], [486, 256], [403, 256]]},{"transcription": "직급 글자1", "points": [[403, 256], [420, 256], [420, 278], [403, 278]]},{"transcription": "직급 글자2", "points": [[436, 256], [453, 256], [453, 278], [436, 278]]},{"transcription": "직급 글자3", "points": [[469, 256], [486, 256], [486, 278], [469, 278]]},{"transcription": "성명", "points": [[496, 235], [645, 235], [645, 273], [496, 273]]},{"transcription": "금액", "points": [[244, 82], [327, 82], [327, 120], [244, 120]]},{"transcription": "금액 한글", "points": [[243, 119], [374, 119], [374, 149], [243, 149]]},{"transcription": "은행명1", "points": [[246, 60], [408, 60], [408, 79], [246, 79]]},{"transcription": "은행명2", "points": [[244, 269], [406, 269], [406, 288], [244, 288]]},{"transcription": "금액아래 글자1", "points": [[199, 150], [475, 150], [475, 169], [199, 169]]},{"transcription": "금액아래 글자2", "points": [[200, 169], [340, 169], [340, 188], [200, 188]]},{"transcription": "micr코드 위 글자", "points": [[237, 285], [505, 285], [505, 304], [237, 304]]}]
'''  # 일단 일부만 넣음. 전체는 너가 위에 적은 거 다 쓰면 돼.

# 이미지 불러오기
img = cv2.imread(image_path)

# 오류 확인
if img is None:
    raise FileNotFoundError(f"이미지 경로를 확인하세요: {image_path}")

# 박스 그리기
data = json.loads(json_data)
for obj in data:
    points = obj["points"]
    pts = [(int(x), int(y)) for x, y in points]
    for i in range(4):
        cv2.line(img, pts[i], pts[(i + 1) % 4], (0, 0, 255), 2)

# OpenCV는 BGR, matplotlib는 RGB라서 변환 필요
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# matplotlib으로 출력
plt.figure(figsize=(10, 10))
plt.imshow(img_rgb)
plt.title("Boxed Image")
plt.axis("off")
plt.show()