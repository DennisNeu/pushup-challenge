from datetime import datetime, timedelta

class User:
    """Basic class for the user of the application, storing necessary data"""
    def __init__(self, name, pushup_goal):
        "Initialize object"
        self.name = name
        self.pushup_goal = pushup_goal
        self.pushup_amount = 0

        self.BEGIN_DATE = datetime.today()
        self.END_DATE = self.BEGIN_DATE + timedelta(days=365)

    def __str__(self) -> str:
        return f'name: {self.name}, goal: {self.pushup_goal}, current amount: {self.pushup_amount}, pushups left: {self.calc_remaining_pushups()}, begin date: {self.BEGIN_DATE.strftime("%d-%m-%y")}, end date: {self.END_DATE.strftime("%d-%m-%y")}, time left: {self.calc_days_left()}'

    def calc_days_left(self):
        """Calculate the time until the challenge ends"""
        today = datetime.today()
        days_left = (self.END_DATE - today).days
        
        # Return + 1 so the end date is inclusive
        return(days_left + 1)
    
    def add_pushups(self, amount):
        """Add specified amount of pushups"""
        if amount < 0:
            print("Please enter positive number")
            return
        
        self.pushup_amount += amount

    def calc_remaining_pushups(self):
        """Calculate remaining pushups"""
        return self.pushup_goal - self.pushup_amount
    
    def change_goal(self, new_goal):
        if new_goal < 0:
            print("Please enter positive number")
            return
        
        self.pushup_goal = new_goal

    
if __name__ == "__main__":
    testUser = User("Chris", 10_000)

    print(testUser)

    testUser.add_pushups(12)

    print(testUser)