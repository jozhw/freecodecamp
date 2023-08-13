import math


def create_spend_chart(categories):
    #determine the total amounts
    totals = get_total_withdrawl(categories)
    totals_each = []
    totals_names = []
    totals_percentage = []
    totals_circles = []
    for category in categories:
        totals_each.append(category.total_withdraw())
        totals_names.append(category.name)


    #calculations
    for value in totals_each:
        percentage = (math.floor(value * 10 / totals)) * 10
        totals_percentage.append(percentage)

    #developing the chart
    chart = 'Percentage spent by category\n'

    num_circles = list(map(lambda x: (x/10), totals_percentage))

    j = 100
    while j >= 0:
        space = " "
        chart += str(j).rjust(3) + "|" + space
        for circle in num_circles:
            if circle * 10 >= j:
                spaces = "o  "
            else:
                spaces ="   "
            chart += spaces
        chart += "\n"
        j-=10

    number_bars = (int(len(totals_names)) * 3) + 1
    bars = "    " + (int(number_bars) * "-" + "\n")
    chart += bars


    #getting the words vertically with the first letter being cap

    biggest_word = max(totals_names, key=len)
    max_letters = int(len(biggest_word))

    #function for appendingword
    def appendingword(word):
        split_word = list(word)
        new_word = []
        for character in split_word:
            new_word += character
        return new_word

    naming = []
    for word in totals_names:
        word.capitalize()
        if len(word) < max_letters:
            number_spaces = int(max_letters - len(word))
            word += (" " * number_spaces)
            naming.append(appendingword(word))

        else:
            naming.append(appendingword(word))


    new_name = list(item for item in zip(*naming))

    for t in new_name:
        add = "     "
        if t != new_name[-1]:
            for i in t:
                add += i + "  "
            chart += add + "\n"
        else:
            for i in t:
                add += i + "  "
            chart += add



    return chart








def get_total_withdrawl(categories):
    total = 0
    for category in categories:
        total += category.total_withdraw()
    return total







class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []


    def __str__(self):
        max_char = 30
        stars_length = int((max_char - (len(self.name)))/2)
        stars = '*' * stars_length
        title = stars + self.name + stars + "\n"
        description = []

        for item in self.ledger:
            descrip = item['description'][:23]
            descrip_amount = len(descrip)
            amouns = float(item['amount'])
            amoun = str("{:.2f}".format(amouns))
            len_amoun = (len(amoun))
            space_amoun = int(max_char - descrip_amount - len_amoun)
            list = (descrip + (" " * space_amoun) + amoun).ljust(max_char) + "\n"
            description.append(list)



        Total = ("Total: " + str(self.get_balance()))

        descriptions = "".join(description)

        final = title + descriptions + Total
        return final


    def deposit(self, amount, description = ""):
        self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description = ""):
        if self.check_funds(amount):
            self.ledger.append({"amount": -amount, "description": description})
            return True
        else:
            return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item["amount"]
        return balance


    def transfer(self, amount, category):
        if self.check_funds(amount):

            self.withdraw(amount, "Transfer to " + category.name)
            category.deposit(amount, "Transfer from " + self.name)
            return True
        else:
            return False


    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

    def total_withdraw(self):
        total = 0
        for item in self.ledger:
            value = item['amount']
            if value < 0:
                total += value
        return total
