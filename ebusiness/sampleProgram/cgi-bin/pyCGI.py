# -*- coding: utf-8 -*-
import cgi
import sys
import io
import csvHandler

#from reviewItem import review

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
form = cgi.FieldStorage()
word = form.getvalue('word','')
print(word)
address="C:/Users/Takafumi/git/ebusiness/ebusiness/dataset/gameDataCSV.csv"
#result=csvHandler.readCsv(address)
searchRe=csvHandler.searchRevByWord(word,address)
reList=csvHandler.generateReviews(searchRe)
name=csvHandler.searchName(searchRe)
omomi=csvHandler.reviewHandler(name)

print('Content-Type: text/html; charset=UTF-8\n')
html_body_prev = """
<!DOCTYPE html>
<html>
<head>
<link href="https://stackpath.bootstrapcdn.com/font-awesome/4.7.0/css/font-awesome.min.css" rel="stylesheet">
<title>Document</title>
<style>
.contact{/*背景*/
  display: flex;
  flex-direction: column;
	background-color: #003344;
  margin-top:80px;
}
.header{/*ヘッダー*/
  background-color:#131921;
  display:inline-block;
  width: 100%;
  position: fixed;
    top: 0px;
	   left: 0px;
  text-align: left;
  z-index: 3;
}
.header h2{/*AmazonReviw serch*/
  display: inline-block;
}
.orange{/*AmazonReviw serch*/
  color:#e47911;
  padding-left:40px;
}
.white{/*AmazonReviw serch*/
  color:#FFFFFF;
  padding-right:40px;
}
form{/*再検索窓*/
  display: inline-block;
}
.search_container{
  box-sizing: border-box;
}
.search_container input[type="text"]{
  border: none;
  height: 35px;
  width:400px;
  border-radius:4px 0 0 4px;
}
.search_container input[type="text"]:focus{
  outline: 0px;
}
.search_container input[type="submit"]{
  font-family: FontAwesome;
  cursor: pointer;
  border: none;
  background: #febd69;
  color: #fff;
  outline : none;
  width: 3.0em;
  height: 37px;
  border-radius:0 4px 4px 0;
}
h1{
  margin-left:50px;
}
@font-face {
font-family: 'NotoSansJP';
  src: url('../CSS/font/NotoSansJP-Regular.otf') format('opentype');
}
body{
  margin:0px;
  background-color:#0f171e;
  color:#FFFFFF;
  font-family: "NotoSansJP";
}
.kekka{
    background-color: #131921;
    text-align:center;
    margin:2% 8%;
    display:table;
    position: relative;
}
.title p{
	font-weight: bold;
}
.username p{
  font-size: 10%;
  width:80px;
  text-align:center
  margin:auto;
  position:absolute;
  top:120px;left:35px;
}

.rating_date p{
  font-size: 13px;
  display: inline-block;
  text-align: center;
  margin:0 0 0 10px;
}
.left{/*左右分割のためのクラス*/
  text-align: left;
}

.img{
  position:absolute;
    top:30px; left:35px;
}
.img img{
  object-fit:cover;
  border-radius:50%;
  width:80px;
  height:80px;
}

.grad-btn {
  box-sizing: border-box;
  position: absolute;
  bottom: 0;
  left: 150px;
  z-index: 1;
}
.grad-btn::before {
  content: "▼続きを読む"
}
.grad-item {
  position: relative;
  overflow: hidden;
  height: 70px; /*隠した状態の高さ*/
  padding:0 15px 30px 0;
}
.grad-item::before {
  display: block;
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;
  height:80px;
  background: -webkit-linear-gradient(top, rgba(19,25,33,1) 40%, rgba(255,255,255,0) 100%);
  background: linear-gradient(to top, rgba(19,25,33,1) 40%, rgba(255,255,255,0) 100%);
  content: "";
}
.grad-trigger {
  display: none; /*チェックボックス非表示*/
}
.grad-trigger:checked ~ .grad-btn::before {
  content: "▲閉じる" /*チェックされていたら、文言を変更する*/
}
.grad-trigger:checked ~ .grad-item {
  height: auto; /*チェックされていたら、高さを戻す*/
}
.grad-trigger:checked ~ .grad-item::before {
  display: none; /*チェックされていたら、grad-itemのbeforeを非表示にする*/
}

.star5_rating{
    position: relative;
    z-index: 0;
    display: inline-block;
    white-space: nowrap;
    color: #CCCCCC; /* グレーカラー 自由に設定化 */
    /*font-size: 30px; フォントサイズ 自由に設定化 */
}

.star5_rating:before, .star5_rating:after{
    content: '★★★★★';
}

.star5_rating:after{
    position: absolute;
    z-index: 1;
    top: 0;
    left: 0;
    overflow: hidden;
    white-space: nowrap;
    color: #ffcf32; /* イエローカラー 自由に設定化 */
}

.star5_rating[data-rate="5"]:after{ width: 5em; } /* 星5 */
.star5_rating[data-rate="4"]:after{ width: 4em; } /* 星4 */
.star5_rating[data-rate="3"]:after{ width: 3em; } /* 星3 */
.star5_rating[data-rate="2"]:after{ width: 2em; } /* 星2 */
.star5_rating[data-rate="1"]:after{ width: 1em; } /* 星1 */
.star5_rating[data-rate="0"]:after{ width: 0%; } /* 星0 */

/*タブ切り替え全体のスタイル*/
.tabs {
  background-color: #fff;
}

/*タブのスタイル*/
.tab_item {
  width: 200px;
  height: 40px;
  background-color: #d9d9d9;
  text-align: center;
  color: #565656;
  display: block;
  float: left;
}
.tab_item p{
margin-top:8px;
}
.tab_review{
  position:fixed;
    top:21px;
    left:850px;
  z-index:4;
}
.tab_gametitle{
  position:fixed;
    top:21px;
    left:1050px;
  z-index:4;
}
@media screen and (min-width: 1400px) {
  .tab_review{
    position:fixed;
      top:21px;
      left:1250px;
    z-index:4;
  }
  .tab_gametitle{
    position:fixed;
      top:21px;
      left:1450px;
    z-index:4;
  }
}
.tab_item:hover {
  opacity: 0.75;
}
/*ラジオボタンを全て消す*/
input[name="tab_item"] {
  display: none;
}
/*タブ切り替えの中身のスタイル*/
.tab_content {
  display: none;
  background-color: #003344;
}

/*選択されているタブのコンテンツのみを表示*/
#review:checked ~ #review_content,
#gametitle:checked ~ #gametitle_content{
  display: block;
}

/*選択されているタブのスタイルを変える*/
.tabs input:checked + .tab_item {
  font-weight: bold;
  background-color: #febd69;
  color: #fff;
}
.gametitle_base{
  margin-top:50px;
}
.sanretu{
  float:left;
  width:33.3333333%;
  background-color: #003344;

}
.game_score_box{
    width:300px;
    background-color: #131921;
    text-align:center;
    margin-top:10px;
    display:table;
    position: relative;
    margin:10px auto;
}
.gameimg{
  padding-top:30px;
  width:100px;
  height:150px;
}
.background{
  background-color: #003344;
}
</style>
</head>
<body>
<div class="header">
  <h2 class="orange">Amazon</h2><h2 class="white">Review search</h2>
  <form action="pyCGI.py" method="post"class="search_container">
    <input type="text" id ="word" name="word"size="25"><input class="button1" name="submit" type="submit"value="&#xf002">
  </form>
</div>

<div class="tabs">
  <input id="review" type="radio" name="tab_item" checked>
  <label class="tab_item tab_review" for="review"><p>レビュー</p></label>
  <input id="gametitle" type="radio" name="tab_item">
  <label class="tab_item tab_gametitle" for="gametitle"><p>ゲームデータ</p></label>
  <div class="tab_content" id="review_content">
    <div class="tab_content_description">
      <p class="c-txtsp">なんか知らんけどここに文字がないと動かない！見つけた人はラッキーだよ！</p>
      <div class="parent">
        <div class="contact">

        <h1>[ """+word+""" ]に関して """+str(len(reList))+""" 件のレビューが見つかりました！</h1>

"""
html_body_result="""
"""
for rev in reList:
    html_body_rev="""
<table border="0">
	<div class = "kekka">
    <div style="display:table-cell;width:150px;position:static;">
      <div class="img">
        <img src="../CSS/img/img"""+rev.rating+""".jpg">
      </div>
      <div class="username">
        <p>"""+rev.userName.replace('"', '')+"""</p>
      </div>
    </div>
    <div class="left" style="display:table-cell;">
      <div class="title">
        <p>"""+rev.summary+"""</p>
      </div>
      <div class="rating_date">
        <span class="star5_rating" data-rate="""+rev.rating+"""></span><p>"""+rev.reviewTime+"""</p>
      </div>
      <div class="gametitle">
        <p>GameTitle : """+rev.productId+"""</p>
      </div>
      <div class="grad-wrap">
        <input id="trigger"""+rev.summary+"""" class="grad-trigger" type="checkbox">
        <label class="grad-btn" for="trigger"""+rev.summary+""""></label>
        <div class="grad-item">"""+rev.reviewText+"""</div>
        </div>
      </div>
    </div>
</table>"""
    html_body_result+=html_body_rev

html_body_after="""
</div>
</div>
</div>
</div>
<div class="tab_content" id="gametitle_content">
  <div class="tab_content_description">
    <p class="c-txtsp">ここにも文字無いと動かないわ、なんだこれ</p>
    <div class="gametitle_base">"""

html_gamedata_result="""
<h1>[ """+word+""" ]に関連した商品のスコアを表示します！</h1>
<div class="background">
"""
for o in omomi:
    html_gamedata_rev="""
<table border="0">
  <div class="sanretu">
	<div class = "game_score_box">
    <img class="gameimg"src="../CSS/img/game_img"""+o[1][2:3]+""".jpg">
      <div class="gametitle">
        <p>ゲームタイトル:"""+o[0]+"""</p>
      </div>
      <div class="score">
        <p>score:"""+o[1][:4]+"""</p>
      </div>
    </div>
    </div>
</table>"""
    html_gamedata_result+=html_gamedata_rev

html_body_after_tow="""
    </div>
  </div>
</div>
</div>
</div>
</body>
</html>"""


print(html_body_prev+html_body_result+html_body_after+html_gamedata_result+html_body_after_tow)
