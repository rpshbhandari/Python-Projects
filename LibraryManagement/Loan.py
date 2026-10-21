from datetime import date, timedelta

class Loan:
    def __init__(self, loan_id: int, book, member) -> None:
        self.loan_id = loan_id
        self.book = book
        self.member = member
        self.issue_date = ''
        self.due_date = ''
        self.return_date = ''
    
    def issue_book(self, issue_date: date, due_date: date) -> None:
        self.issue_date = issue_date
        self.due_date = due_date
    
    def return_book(self, return_date: date) -> None:
        self.return_date = return_date
    
    def is_overdue(self) -> bool:
        if not self.return_date:
            today = date.today()
            return today > self.due_date
        return self.return_date > self.due_date
    
    def get_details(self):
        return {
            "Loan ID": self.loan_id,
            "Book ID": self.book.title,
            "Member ID": self.member.member_id,
            "Due Date": self.due_date,
            "Return Date": self.return_date
        }
