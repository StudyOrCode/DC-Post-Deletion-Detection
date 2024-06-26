import json
import datetime
import re
import time

def OpenJson(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

def SaveJSON(filename, data):
    with open(filename, "w", encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)


def CurrentTime():
    dt = datetime.datetime.now()
    
    if dt.hour < 12:
        meridiem = "오전"

    else:
        meridiem = "오후"
    
    hour = dt.hour % 12
    if hour == 0:
        hour = 12
    
    return dt.strftime(f"%Y/%m/%d {meridiem} {hour}:%M:%S")



# 쿼리 제거
def gall_id(url):
    # '?' 를 기준으로 URL을 분리하여 쿼리 파라미터 부분을 얻는다
    query_str = url.split('?')[-1]

    # '&'를 기준으로 각 쿼리 파라미터를 분리한다
    query_params = query_str.split('&')

    # 각 쿼리 파라미터를 순회하며 'id' 파라미터의 값을 찾는다
    id_value = None
    for param in query_params:
        if param.startswith('id='):
            id_value = param.split('=')[-1]
            break

    return id_value



# 불필요한 텍스트 삭제
def OnlyTEXT(text):
    return re.sub(r'[^a-zA-Z0-9가-힣]', '', text)

# IP 괄호는 지우고 마침표는 유지
def RemoveBrackets(text):
    if text is not None:
        return re.sub(r'\(|\)', '', text)

    return None

def URLCheck(URL):
    OriginalURL = URL.split('/')
    return f"https://gall.dcinside.com/mgallery/board/view?id={OriginalURL[3]}&no={OriginalURL[4]}"