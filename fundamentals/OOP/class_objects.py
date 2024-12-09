import datetime as dt

# Creating a class
class News:

    # Class variable - common to all objects
    news_category = "Technology & Innovation"

    # Constructor to initialize object
    def __init__(self, headline, body):
        # Instance variables - unique to all objects
        self.headline = headline
        self.body = body
        self.date = dt.date.today()
    
    def display_news(self):
        """Displays News information"""
        news_block = f"""
        Headline: {self.headline}
        Body: {self.body}
        Date: {self.date}
        """
        print(news_block)

# Creating Objects
news1 = News("Elon Musk!","Elon Musk becomes richest person in the world")
news2 = News("Starship!!","Elon Musk's startship launch was successful")


# Calling object methods
print(f"\n\tNews Category: {News.news_category}") # Accessing class variable
news1.display_news()
news2.display_news()

