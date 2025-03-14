class Publication:
    def __init__(self, pub_type, name, chief_editor):
        self.name = name
        self.chief_editor= chief_editor
        self.pub_type = pub_type

    def print_information(self):
        print(f"{self.pub_type} - {self.name}")

class Magazine(Publication):
    def __init__(self,  name, chef_editor):
        super().__init__("Magazine", name)
        self.chef_editor = chef_editor

    def print_information(self):
        super().print_information()
        print(f"Editor: {self.chef_editor}")

class Book(Publication):
    def __init__(self, name, author, page_count):
        super().__init__("Book", name)
        self.author = author
        self.page_count = page_count
        self.type = type

    def print_information(self):
        super().print_information()
        print(f"Author: {self.author}")
        print(f"Page Count: {self.page_count}")


publication = Publication("Donald Duck", "Aki Hyyppä")
publication.print_information()

magazine = Magazine("book", "Aki Hyyppä")
magazine.print_information()

book1 = Book("Compartment No. 6", "Rosa Liksom", "192")
book2 = Book("Flatland", "Edwin", "96")
Book.print_information()

pub_list = [publication, magazine, book1, book2]
for item in pub_list:
    item.print_information()

