import json

import sys
sys.path.append(r'/home/runner/work/problem-solving-alarm/problem-solving-alarm/src/lib')

import message

# 한번 요청으로 1만건의 메시지 발송이 가능합니다.
if __name__ == '__main__':
    data = {
        'messages': [
            {
                'to': '01050929241',
                'from': '01050929241',
                'text': '💌 just_junyan님이 문제를 푸셨습니다!'
                        + '- 시간: 오늘 17:25'
                        + '- 문제 티어: Silver 2'
                        + '- 문제 번호: 17287번'
                        + '- 문제 이름: The Deeper, The Better'
                        + '- 시도 횟수: 4회'
                        + '- 현재 등수: 3등 (로그인 필요...)'
            }
        ]
    }
    res = message.send_many(data)
    print(json.dumps(res.json(), indent=2, ensure_ascii=False))
