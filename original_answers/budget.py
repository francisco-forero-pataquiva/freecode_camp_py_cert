class Category:
    
    def __repr__(self):
        text = f'{self.name:*^30}\n'

        for element in self.ledger:
            d = element["description"]
            a = format((element["amount"]), ".2f")
            text+=f'{d[:29-len(a)]} {a.rjust(29-len(d))}\n'        
        text += f"Total: {self.total}"
        return text
    
    def __init__(self, name):
        self.name = name
        self.total = 0
        self.ledger = []
        
    def deposit(self,amount,description=""):
        self.total += amount
        self.ledger.append({"amount": amount, "description": description})
        
    def withdraw(self,amount,description=""):
        can_transfer = self.check_funds(amount)
        if can_transfer:
            self.total -= amount
            self.ledger.append({"amount": -amount, "description": description})
        return can_transfer
    
    def get_balance(self):
        return self.total
    
    def transfer(self,amount,init):
        can_transfer = self.check_funds(amount)
        if can_transfer:
            self.withdraw(amount,f"Transfer to {init.name}")
            init.deposit(amount,f"Transfer from {self.name}")
            return can_transfer
        return can_transfer
    
    def check_funds(self,amount):  
        if amount > self.total:
            return False
        return True


def create_spend_chart(categories):

    name_list = []
    size_list = []
    for category in categories:
        name_list.append(category.name)
        height = len(max(name_list, key=len))
        height_alig = [word.ljust(height) for word in name_list]
        
        global_total = 0
        for item in category.ledger:
            amount = item['amount']
            if amount < 0:
                global_total += amount 
        size_list.append(global_total)
    total = int(round(sum(size_list)))
    percentages = []
    for y in size_list:
        perc = y * 100/total
        perc = round(perc//10)*10
        percentages.append(perc)
        
    s = f"Percentage spent by category\n"
    for x in range(100,-10,-10):
        s += f"{str(x).rjust(3)}|"
        for percentage in percentages:
            if percentage >= x:
                s += " o "
            else:
                s += "   "
        s += " \n"
    s += f'{" "*4}{"-"*((len(name_list)+2)*2)}\n'            
    for name in zip(*height_alig):
        s += f'{" "*5}{"  ".join(name)}  \n'
    return s.rstrip("\n")