import book
# Book物件內初始化參數順序：Book('書名','作者','出版社','年份')
ds_book = book.Book('Python資料結構', '黃建庭', '全華圖書', '2021') 
book_info = ds_book.info()  # 注意!! info() 方法的回傳值，型態必須是str(字串)
print(book_info)
