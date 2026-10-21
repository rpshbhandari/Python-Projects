from Books import Book
from Loan import Loan
from Member import Member
from datetime import date, timedelta

class Library:
    def __init__(self):
        self.books = []
        self.members = []
        self.loans = []
        self.default_return_date = 7
        self.max_loans = 5
        
    
    def add_book(self, book) -> str:
        if not isinstance(book, Book):
            return f"Should be instantance of class: {Book.__name__}"
        if book in self.books:
            return f"{book.title} is already in the library!"
        self.books.append(book)
        return f"{book.title} is added to the library!"
        
    def remove_book(self, book) -> str:
        if not isinstance(book, Book):
            return f"Should be instantance of class: {Book.__name__}"
        if not book in self.books:
            return f"{book.title} is not in the library to remove!"
        self.books.remove(book)
        return f"{book.title} is remove from the library!"

    def find_book(self, book):
        if not isinstance(book, Book):
            return f"Should be instantance of class: {Book.__name__}"
        for i in self.books:
            if book.title == i.title:
                return f"{book.title} found"
        
    def register_member(self, member):
        if not isinstance(member, Member):
            return f"Should be instantance of class: {Member.__name__}"
        if member in self.members:
            return f"{Member.name} is already in the library!"
        self.members.append(member)
        return f"{member.name} is added to the library!"
    
    def remove_member(self, member) -> str:
        if not isinstance(member, Member):
            return f"Should be instantance of class: {Member.__name__}"
        if not member in self.members:
            return f"{member.name} is not in the library to remove!"
        self.members.remove(member)
        return f"{member.name} is remove from the library!"
    
    def issue_book(self, book, member):
        if not isinstance(book, Book):
            return f"Should be instantance of class: {Book.__name__}"
        if not book in self.books:
            return f"{book.title} is not in the library!"
        
        if not isinstance(member, Member):
            return f"Should be instantance of class: {Member.__name__}"
        if not member in self.members:
            return f"{Member.name} is not a member of the library!"
        
        if not book.status:
            return f"The book is: {Book.status} at the moment"
        
         # Check if the member has reached the maximum loan limit
        if len([loan for loan in self.loans if loan.member == member]) >= self.members:
            return f"{member.name} has reached the maximum loan limit"
        
        book.set_status(False)
        loan = Loan(len(self.loans) + 1, book, member)
        loan.issue_book(issue_date = date.today(),due_date=date.today() + timedelta(days=self.default_return_date))
        self.loans.append(loan)
        return f"{loan.book.title} issued to {loan.member.name}"
    
    
    def return_book(self, book, member):
        if not isinstance(book, Book):
            return f"Should be instantance of class: {Book.__name__}"
        if not book in self.books:
            return f"{book.title} is not in the library!"
        
        if not isinstance(member, Member):
            return f"Should be instantance of class: {Member.__name__}"
        if not member in self.members:
            return f"{Member.name} is already in the library!"
        if book.status:
            return f"The book is: {book} available at the moment so can't be returned"
        
        # Find the corresponding loan and return the book
        for loan in self.loans:
            if loan.book == book and loan.member == member:
                book.set_status(True)
                loan.return_book(return_date=date.today())
                self.loans.remove(loan)
                return f"{book.title} returned by {member.name}"
        return f"The book {book.title} was not borrowed by {member.name}"
    
    
    def list_available_books(self):
        return [i.get_details() for i in self.books]
    
    def list_members(self):
        return [i.get_details() for i in self.members]
    
    def list_loans(self):
        return [
            loan.get_details()
            for loan in self.loans
        ]
    
    
Books1 = Book(123, 'asd', 'asfsf', 2017)
Books2 = Book(2312423, 'asd', 'asfsf', '2017')
Member1 = Member(1, 'Sam','a', 'asd', 'asd')
Member2 = Member(2, 'Ram','a', 'asd', 'asd')


Lib = Library()

Lib.add_book(Books1)
Lib.add_book(Books2)
Lib.register_member(Member1)
Lib.register_member(Member2)
Lib.issue_book(Books1, Member1)
Lib.issue_book(Books2, Member2)
Lib.return_book(Books1, Member1)
# print(Lib.find_book(Books1))
print(Lib.list_available_books())
print(Lib.list_members())
print(Lib.list_loans())
# print(Lib.find_book(Books1))
