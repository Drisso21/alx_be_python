class Book:
    def __init__(self,title,autor,year):
        self.title = title
        self.autor = autor
        self.year = year
    def __del__(self):
        print(f'Deleting book {self.title}')
    def __repr__(self):
        return f"Book('{self.title}','{self.autor}',{self.year})"
    def __str__(self):
        return f"{self.title} by {self.autor} in {self.year}"