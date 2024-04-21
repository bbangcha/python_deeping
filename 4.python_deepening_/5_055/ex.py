import book as bk

myBookRepository = bk.BookRepository()

myBookRepository.registBook(bk.Book('pyton', 20000, 1234567890))
myBookRepository.registBook(bk.Book('java', 25000, 987654321))
myBookRepository.registBook(bk.Book('c/c++', 27000, 147852369))

myBookRepository.printBooksInfo()
print('-' * 50)
myBookRepository.printBookInfo(987654321)
myBookRepository.printBookInfo(1234567890)
print('-' * 50)
myBookRepository.removeBook(1234567890)
myBookRepository.printBooksInfo()
