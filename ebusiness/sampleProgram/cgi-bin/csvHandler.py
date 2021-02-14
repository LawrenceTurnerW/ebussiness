import csv
from reviewItem import review

#open csv file with its absolute path
#def readCsv(address):
#    csv_file=open(address,"r",encoding="utf_8", errors="", newline="")
#    f=csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#    return f

#print out all rows from the parameter result, which is gotten from CSV file
def printCSV(result):
    i=0
    for row in result:
        i+=1
        print(row)
    print("rows:"+str(i)+"")

#csv should be the result which is get from csv_file
#use readCsv method for it
#word should be a string
def searchRevByWord(word,address):
    csv_file=open(address,"r",encoding="utf_8", errors="", newline="")
    f=csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    searchRe=[]
    for row in f:
        #for col in row:
        if word in row[5] or word in row[1]:
            #print(row[5])
            searchRe.append(row)
    #return of the list of rows whose review contains the word
    csv_file.close()
    return searchRe


def generateReviews(rows):
    list=[]
    for row in rows:
        reItem=review()
        reItem.userId=row[0]
        reItem.productId=row[1]
        reItem.userName=row[2]
        reItem.helpfulVotes=row[4]
        reItem.totalVotes=row[3]
        reItem.reviewText=row[5]
        reItem.rating=row[6]
        reItem.summary=row[7]
        reItem.reviewTime=row[8]
        list.append(reItem)
    return list
#wordで検索した結果から商品idの重複を取り除く
def searchName(searchRe):
    s=[]
    for r in searchRe:
        s.append(r[1])
    slist=set(s)
    return slist
#レビューの評価の再計算を行う
# def reviewHandler(name,address):
#     answerList=[]
#     csvlist=[]
#     csv_file=open(address,"r",encoding="utf-8", errors="", newline="")
#     f=csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
#     result2 = 0
#     helpfulvotes=0#役に立った人数
#     valuation=0#★1から★5の評価
#     #csvをリストに変換
#     for fd in f:
#         csvlist.append(fd)
#     for s in name:
#         result2 = 0
#         helpfulvotes=0
#         valuation=0
#         for c in csvlist:
#             #商品一致の判別
#             if s==c[1]:
#                 z=float(c[4])
#                 d=float(c[6])
#                 helpfulvotes=helpfulvotes+z
#                 valuation= valuation+(d*z)
#         result2= valuation/helpfulvotes
#         result3={
#             "kekka":result2,
#             "tableid":s
#         }
#         answerList.append(result3)
#     return answerList
def reviewHandler(name):
    answerList=[]
    zlist=[]
    with open(file="C:/Users/Takafumi/git/ebusiness/ebusiness/dataset/gameRating.csv", mode="r", encoding="utf_8") as rf:
        answerfile=csv.reader(rf)
        for af in answerfile:
            zlist.append(af)
        for n in name:
            for a in zlist:
                if n==a[0]:
                    answerList.append(a)
                    break
    return answerList
#address="D:\講義\R02\ebusiness\dataset\gameDataCSV.csv"
#result=readCsv(address)
#searchRe=searchRevByWord(result,"Sony")
#reList=generateReviews(searchRe)
#for re in reList:
#    print(re.userId+" , "+re.userName+" , "+re.productId+" , "+re.helpfulVotes+" , "+re.totalVotes+" , "+re.reviewText+" , "+re.summary)
#print(len(reList))
