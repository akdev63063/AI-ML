class Book:
    count = 0
    def __init__(self,title,author_name):
        self.title = title
        self.author_name = author_name
        self.lor = []

    def add_new_reviews(self,reviews):
        self.lor.append(reviews)
        print("New Review Add Successful")
        

    def count_review(self):
        total_review = len(self.lor)
        print("Total Revies : ",total_review)

    def Show_reviews(self):
        if len(self.lor) == 0:
            print("No Review Available")
        else:
            print("Reviews: ")
            for reviews in self.lor:
                print(" ",reviews)  

b1 = Book("Programming Book","Akash Kumar")
b1.add_new_reviews("Very Nice Book")
b1.add_new_reviews("Very, Beautiful and  Nice Book")
b1.Show_reviews()
b1.count_review()



