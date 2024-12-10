import datetime as dt

# Parent Class
class News:

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


# Child class inherits from Parent Class: News
class ShortNews(News):
    def __init__(self, headline):
        # Initializing parent class constructor from child class
        super().__init__(headline, body = None) # Excluding body for short_news

    # Method overriding - rewriting parent class method for alternate functionality
    def display_news(self):
        short_news_block = f"""
        Headline: {self.headline}
        Date: {self.date}
        """
        print(short_news_block)
        

# Creating Parent Class objects
news1 = News("Elon Musk!","Elon Musk becomes richest person in the world")
news2 = News("Starship!!","Elon Musk's startship launch was successful")

# Creating Child Class Objects
short_news1 = ShortNews("Nvidia is releasing a new graphics card")
short_news2 = ShortNews("Intel losing it's edge")

print("\t----------------")

# Calling Parent and Child Object methods
print(f"\n\tFull News:")
news1.display_news()
news2.display_news()

print("\t----------------")

print(f"\n\tShort News (without body):")
short_news1.display_news() # Calls overriden method
short_news2.display_news() # Calls overriden method

print("\t----------------")

 
