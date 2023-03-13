class Cricketer:
    def __init__(self, name, age, num_of_matches):
        self.name = name
        self.age = age
        self.num_of_matches = num_of_matches

    def getinfo(self):
        return f"Name= {self.name}\n" \
               f" Age= {self.age}\n" \
               f" Number of matches= {self.num_of_matches}\n"



class Batsman(Cricketer):
    def __init__(self, name, age, num_of_matches, runs, num_of_centuries):
        self.runs = runs
        self.num_of_centuries = num_of_centuries
        super().__init__(name, age, num_of_matches)

    def getinfo(self):
        super(Batsman, self).getinfo()
        return f" Runs= {self.runs}\n" \
               f" Number of centuries= {self.num_of_centuries}\n"


class Bowler(Cricketer):
    def __init__(self, name, age, num_of_matches, num_of_wickets):
        self.num_of_wickets = num_of_wickets
        super().__init__(name, age, num_of_matches)

    def getinfo(self):
        super(Bowler, self).getinfo()
        return f" Number of wickets= {self.num_of_wickets}\n"


Player1 = Cricketer('Ram', 24, 100)
print(Player1.getinfo())
