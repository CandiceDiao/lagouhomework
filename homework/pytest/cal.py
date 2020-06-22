class calculate:

    def add(self,a,b):
        return a+b

    def sub(self,a,b):
        return a-b

    def mul(self,a,b):
        return a*b

    def div(self,a,b):

        try:
            div=a/b
        except ZeroDivisionError:
            print("异常")
        else:
            return div



