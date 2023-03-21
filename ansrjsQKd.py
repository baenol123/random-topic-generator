import random

first_words = ["로봇", "인공", "자율", "스마트", "가상","미래","전기"]
second_words = ["도시", "산업", "환경", "교통", "보안","물리","화학","생명","의대","공학"]
third_words = ["과 인류의 발전","과 관련된 윤리문제",",과연 허용 가능한가"]

selected_first_word = random.choice(first_words)
selected_second_word = random.choice(second_words)
selected_third_word = random.choice(third_words)

new_topic = selected_first_word + " " + selected_second_word + "" + selected_third_word

print("당신의 발표 주제는 {} 입니다!".format(new_topic))
