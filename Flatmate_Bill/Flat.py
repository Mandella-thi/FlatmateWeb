class Bill:
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """ creates a flatmate person who lives in the
    flat and pays a share of the bill"""
    def __init__(self, name,days_in_house):
        self.name =name
        self.days_in_house =days_in_house

    def pays(self, bill, flatemate2):
        weigth= self.days_in_house/(self.days_in_house +
                                    flatemate2.days_in_house)
        to_pay = bill.amount*weigth
        return to_pay
