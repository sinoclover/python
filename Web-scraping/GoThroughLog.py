import requests

# # 提交一个基本表单
# userdata = {'firstname': 'a', 'lastname': 'b'}
# r1 = requests.post('http://pythonscraping.com/files/processing.php', data=userdata)
# print(r1.text)

# # 提交文件或图像
# files = {'uploadFile': open('pic/logo.jpg', 'rb')}
# r2 = requests.post('http://pythonscraping.com/files/processing2.php', files=files)
# print(r2.text)
#
# # 跟踪cookie
# params = {'username': 'Ryan', 'password': 'password'}
# r = requests.post('http://pythonscraping.com/pages/cookies/welcome.php', params)
# print(r.text)
# print('Cookie is set to: {}'.format(r.cookies.get_dict()))
# print('--------')
# print('Going to profile page...')
# r3 = requests.get('http://pythonscraping.com/pages/cookies/profile.php', cookies=r.cookies)
# print(r3.text)
#
# # 通过session持续跟踪会话信息
# session = requests.Session()
# params2 = {'username': 'Ryan', 'password': 'password'}
# s = session.post('http://pythonscraping.com/pages/cookies/welcome.php', params2)
# print(s.text)
# print('Cookie is set to: {}'.format(s.cookies.get_dict()))
# print('--------')
# print('Going to profile page...')
# s = requests.get('http://pythonscraping.com/pages/cookies/profile.php')
# print(s.text)
#
# # http基本接入认证
# from requests.auth import HTTPBasicAuth
#
# auth = HTTPBasicAuth('ryan', 'password')
# a = requests.post(url='http://pythonscraping.com/pages/auth/login.php', auth=auth)
# print(a.text)
