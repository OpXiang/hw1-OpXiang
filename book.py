class Book:

    def __init__(self,書名,作者,出版社,年份):
        self.書名="書名:"+書名
        self.作者="作者:"+作者
        self.出版社="出版社:"+出版社
        self.年份="年份:"+年份
       
    def info(self):        
        return "{}\n{}\n{}\n{}".format(self.書名,self.作者,self.出版社,self.年份)
        