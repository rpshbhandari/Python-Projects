from datetime import date

class Book:
    def __init__(self, title:str, author:str, isbn:str, publication_year: date):
        self.title = title
        self.author = author
        self.isbn = isbn
        self.publication_year = date(year=int(publication_year), day=1, month=1)
        self.status = True

    def get_details(self):
        return {
            "Title": self.title, 
            "Author": self.author, 
            "ISBN": self.isbn, 
            "Year": self.publication_year.strftime("%Y"), 
            "Status": self.status
            }

    def set_status(self, status: bool) -> bool:
        self.status = status
        return self.status
    
    def get_status(self) -> bool:
        return self.status
    

