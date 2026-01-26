class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.reviews = []

    def add_review(self, review):
        self.reviews.append(review)

    def count_reviews(self):
        return len(self.reviews)

    def display_reviews(self):
        if not self.reviews:
            print("No reviews available.")
            return

        print(f"Reviews for '{self.title}':")
        for idx, review in enumerate(self.reviews, start=1):
            print(f"{idx}. {review}")

    def get_info(self):
        print(f"The author of the book '{self.title}' is {self.author}.")
        print(f"Total Reviews: {self.count_reviews()}")
        print("Reviews:")
        self.display_reviews()


book1 = Book("shivuuBook", "shivam purve")
book1.add_review("Product is unique")
book1.add_review("Book is so costly still worth it!!")
book1.add_review("Book is really amazing, cool stuff contained")
book1.add_review("Hi, your product is glorious")

print("Printing info about different books\n")
book1.get_info()
