class Dog(object):             # declaration

    def __init__(self, age):   # constructor
       self.age = age          # attribute
       self.hates_cats = True

    def fetch(self, stick):    # method
        if self.age > 5:
            return "No take, only throw"
        else:
            return stick
