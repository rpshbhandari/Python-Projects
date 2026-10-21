

class Member:
    def __init__(self, member_id: int, name: str, email: str, phone, member_since) -> None:
       self.member_id = member_id
       self.name = name
       self.email = email
       self.phone = phone
       self.member_since = member_since
    
    def get_details(self) -> dict:
        return {
            "Member ID": self.member_id,
            "Name": self.name,
            "Email": self.email,
            "Phone": self.phone,
            "Member Since": self.member_since,
        }
        
    def update_info(self, name, email, phone) -> str:
        self.name = name
        self.email = email
        self.phone = phone
        return f"upated details for {self.member_id}"