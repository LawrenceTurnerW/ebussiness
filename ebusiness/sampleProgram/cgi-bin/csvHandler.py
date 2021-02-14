import csv
from reviewItem import review

#open csv file with its absolute path
def readCsv(address):
    csv_file=open(address,"r",encoding="utf_8", errors="", newline="")
    f=csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    return f

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
def searchRevByWord(csv, word):
    searchRe=[]
    for row in csv:
        #for col in row:
        if word in row[5] or word in row[1]:
            #print(row[5])
            searchRe.append(row)
    #return of the list of rows whose review contains the word
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

def searchName(searchRe):
    slist=[]
    for row in searchRe:
        slist.append(row[1])
    slist=set(slist)
    print("----------------------------")
    print(slist)
    print("----------------------------")
    return slist

def reviewHandler(result,name):
    answerList=[]
    for s in name:
        result2 = 0.0
        helpfulvotes=0.0
        valuation=0.0
        for c in result:
            if s==c[1]:
                helpfulvotes=helpfulvotes+c[4]
                valuation= valuation+(c[6]*c[4])
            result2= valuation/helpfulvotes
        result={
            "kekka":result2,
            "tableid":s
        }
        print(result)
        answerList.append(result)
    return answerList
#address="D:\講義\R02\ebusiness\dataset\gameDataCSV.csv"
#result=readCsv(address)
#searchRe=searchRevByWord(result,"Sony")
#reList=generateReviews(searchRe)
#for re in reList:
#    print(re.userId+" , "+re.userName+" , "+re.productId+" , "+re.helpfulVotes+" , "+re.totalVotes+" , "+re.reviewText+" , "+re.summary)
#print(len(reList))
