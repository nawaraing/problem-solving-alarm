import json

import sys
sys.path.append(r'/Users/kangjunhyeon/python-test/MEMuV7qVBtT5Vb-24011618254387-coolsms-python/src/lib')

import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01050929241',
                'from': '01050929241',
                'text': '한글 45자, 영자 90자 이하 입력되면 자동으로 SMS타입의 메시지가 추가됩니다.'
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
