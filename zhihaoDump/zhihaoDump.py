"""
Dump exams from www.zhihao.com

 @Author : Merack
 @E-Mail : merack@qq.com
 @URL : https://github.com/Merack/MKScript/zhihaoDump
"""

import requests
import os
from bs4 import BeautifulSoup

copyright = '''====================
@Author : Merack
@E-Mail : merack@qq.com
@URL : https://github.com/Merack/MKScript/zhihaoDump
====================
'''

session = requests.session()

baseURL = ''

header = {
    'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.77 Safari/537.36 Edg/91.0.864.37",
    'Origin': 'http://www.zhihao.com',
    'Host': 'www.zhihao.com'
}


def getCookie():
    data = {
        'key': 'yzhjrwjs'
    }
    return session.post('http://www.zhihao.com/jrw/check.asp', data=data).cookies


cookie = getCookie()


def login():
    data = {
        'myclass': '2',
        'myname': 'merack'
    }

    session.post(baseURL + 'login.asp', data=data, cookies=cookie)


def doExam(URL):
    res = session.get(URL, headers=header, cookies=cookie)
    res.encoding = 'gb2312'
    soup = BeautifulSoup(res.text, 'lxml')
    question = soup.find('form').text.strip()
    checkURL = soup.find('form').attrs['action']
    opArray = ['A', 'B', 'C', 'D']
    answer = ''
    nextURL = ''
    completeFlag = False
    for i in range(4):
        answer = opArray[i]
        datas = {
            "answer1": answer
        }
        header['Referer'] = URL
        checkRes = session.post(checkURL, data=datas, headers=header,
                                cookies=cookie)
        checkRes.encoding = 'gb2312'
        # print(checkRes.text)
        if "答案正确" in checkRes.text:
            nextURL = baseURL + BeautifulSoup(checkRes.text, 'lxml').find('a').attrs['href']
            # print(nextURL)
            break
        if "全部正确" in checkRes.text:
            # print('exam done!')
            completeFlag = True
            break

    return question, answer, nextURL, completeFlag


def main():
    os.mkdir('zhihao')
    os.chdir('zhihao')
    for i in range(1, 13):
        global baseURL
        baseURL = 'http://www.zhihao.com/jrwtest{:02d}/'.format(i)
        # print(baseURL)
        f = open('text{:02d}.txt'.format(i), 'w+', encoding='utf-8')
        f.write(copyright)
        f.write('\n')
        URL = baseURL + 'test01.htm'
        login()
        question, answer, URL, flag = doExam(URL)
        f.write(question)
        f.write('\n')
        f.write('answer: ' + answer)
        f.write('\n')
        f.write('\n')
        f.write('\n')
        while not flag:
            question, answer, URL, flag = doExam(URL)
            f.write(question)
            f.write('\n')
            f.write('answer: ' + answer)
            f.write('\n')
            f.write('\n')
        f.close()
        print('dump exam{:02d} done!'.format(i))

    print('all done, thanks for using')


if __name__ == '__main__':
    main()