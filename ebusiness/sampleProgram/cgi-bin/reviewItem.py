class review:
    #parameters and setter, getter

    @property
    def userId(self):
        return self._userId

    @userId.setter
    def userId(self,value):
        self._userId=value

    @property
    def productId(self):
        return self._productId

    @productId.setter
    def productId(self,value):
        self._productId=value

    @property
    def userName(self):
        return self._userName
    @userName.setter
    def userName(self,value):
        self._userName=value

    @property
    def totalVotes(self):
        return self._totalVotes
    @totalVotes.setter
    def totalVotes(self,value):
        self._totalVotes=value

    @property
    def helpfulVotes(self):
        return self._helpfulVotes
    @helpfulVotes.setter
    def helpfulVotes(self,value):
        self._helpfulVotes=value

    @property
    def reviewText(self):
        return self._reviewText

    @reviewText.setter
    def reviewText(self,value):
        self._reviewText=value

    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self,value):
        self._rating=value

    @property
    def summary(self):
        return self._summary
    @summary.setter
    def summary(self,value):
        self._summary=value

    @property
    def reviewTime(self):
        return self._reviewTime
    @reviewTime.setter
    def reviewTime(self,value):
        self._reviewTime=value

#obj=review()
#obj.userId="abc"
#obj.productId="bca"
#obj.userName="Nin"
#print(obj.userId+obj.productId+obj.userName)
