import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.daum.net/premovie/released")
if req.status_code !=200:
    print("failed", req.status_code)


html=req.text
bs= BeautifulSoup(html,"html.parser")

box= bs.find_all("div",class_="wrap_movie" )

print(box)

title=[]
ratio=[]
reserve=[]

for b in box:
    title.append(b.find("div", class_="name_movie").text)
    ratio.append(b.find("span", class_="info_grade").find("span",class_="wrap_grade grade_netizen").text)
    reserve.append(b.find("span", class_="info_state" ).find("span",class_="txt_dot" ).text )


movieInfo = []
for i in range(len(box)) :
    movie=[]
    movie.append(title[i])
    movie.append(ratio[i])
    movie.append(reserve[i])
    movieInfo.append(movie)

    for i in movieInfo:
        print(i)

# 다음 영화에서 제목 , 평점, 예매율(0% 존재하지 않음) 기준으로 크롤링 하였습니다
