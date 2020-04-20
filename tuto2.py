import requests
from bs4 import BeautifulSoup

req = requests.get("https://movie.naver.com/movie/running/current.nhn")
if req.status_code !=200:
    print("failed", req.status_code)


html=req.text
bs= BeautifulSoup(html,"html.parser")

box= bs.find_all("dl",class_="lst_dsc" )

print(box)

title=[]
ratio=[]
reserve=[]

for b in box:
    title.append(b.find("dt", class_="tit").find("a").text)
    ratio.append(b.find("div", class_="star_t1").find("span",class_="num").text
    if b.find("div",class_="star_t1 b_star" ) !=None :
        reserve.append(b.find("div", class_="star_t1 b_star" ).find("span",class_="num" ).text )
    else: 
        reserve.append("0")    

movieInfo=[]
for i in range(len(box)) :
    movie=[]
    movie.append(title[i])
    movie.append(ratio[i])
    movie.append(reserve[i])
    movieInfo.append(movie)

    for i in movieInfo:
        print(i)



# file = open("tuto 3.csv", "a", newline="")
# wr = csv.writer(file)
# wr.writerow(["Title", "ratio", "reserve"])

# for i in range(len(box)) :
# wr.writerow([title[i],ratio[i],reserve[i]])git

# file.close()




# tuto ="4/20"
# git init
# git remote add origin https://github.com/cauinse/cauinse.git 
# git fetch origin
# git merge orgin/master

# git add
# git commit -m "tuto commit"
# git push origin master
