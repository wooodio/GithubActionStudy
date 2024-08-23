# import requests  # 웹 페이지 소스를 얻기 위한 패키지(기본 내장 패키지이다.)
# from bs4 import BeautifulSoup  #텍스트를 파싱해서 깔끔하게 만질수있음

# url='https://ridibooks.com/category/new-releases/2200'
# response = requests.get(url)
# response.encoding = 'utf-8'  # 한글이 깨지지 않게 utf-8로 인코딩
# html = response.text

# soup = BeautifulSoup(html, 'html.parser')
# bookservices = soup.select('.title_text')
# # for no, book in enumerate(bookservices, 1):
# #     print(no, book.text.strip())
# print(bookservices)
print('hello world')
