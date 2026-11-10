class Father:
    def father_hobby(self):
        print("Father's hobby is gardening")


class Mother:
    def mother_hobby(self):
        print("Mother's hobby is cooking")


class Child(Father, Mother):
    pass


c = Child()
c.father_hobby()
c.mother_hobby()