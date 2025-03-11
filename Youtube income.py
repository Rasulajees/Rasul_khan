import random

class YoutubeEarnings:
    print("\nLEARN WITH RASUL\n")
    def __init__(self,likes,shares,subscribers): #Generating random likes,shares, and subscibers between 500 and 50000
        self.likes=random.randint(500,50000)
        self.shares=random.randint(500,50000)
        self.subscribers=random.randint(500,50000)
        self.earnings_per_1000_likes=75 #75 rupees per 1000 likes

    def calculate_earnings(self):
         if self.likes>=1000 and self.shares>=1000 and self.subscribers>=1000:
            earnings=(self.likes and self.shares and self.subscribers //1000)*self.earnings_per_1000_likes
            return (f"likes:{self.likes} \nshares:{self.shares} \nsubscribers:{self.subscribers}\n you are Earnings are ₹{earnings}")
         else:
            return( f"likes:{self.likes} \nshares:{self.shares} \nsubscribers:{self.subscribers}\n you needs at least 1000 likes,shares,and subcribers to start earning.")
    
#Example usage:
Youtube_earnings= YoutubeEarnings("likes","shares","subscribers")
print(Youtube_earnings.calculate_earnings())   