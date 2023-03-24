import re

def solution(new_id):
	new_id = new_id.lower()                         # 소문자 변환
	new_id = re.sub("[^a-z0-9-_.]", "", new_id)  # 영문자, 숫자, -, _, .을 제외한 문자는 공백으로 치환
	new_id = re.sub("[.]{2,}", ".", new_id)           # .. 을 .으로 치환
	new_id = new_id.lstrip(".")                        # 왼쪽과 오른쪽 .제거
	new_id = new_id.rstrip(".")

	if not new_id:
		new_id = "a"                            # 빈 문자열일경우 a
		
	if len(new_id) > 15:                                 # 아이디의 길이가 15이상일 경우 15문자만 사용 및 오른쪽 .제거
		new_id = new_id[:15]
		new_id = new_id.rstrip(".")
	
	while len(new_id) < 3:                              # 아이디의 길이가 3보다 작을 경우 마지막 문자 반복 추가
		new_id = new_id + new_id[-1]
	
	res = new_id
	
	return res