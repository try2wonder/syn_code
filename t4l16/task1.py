class Kassa():
    balance = 0

    def top_up(self, x):
        self.balance += x

    def count_1000(self):
        res = self.balance // 1000
        print(res)

    def take_away(self, x):
        if self.balance >= x:
            self.balance -= x
        else:
            print('Error, not enough cash')

magnt = Kassa()
magnt.top_up(123456)
print(magnt.balance)
magnt.count_1000()
print(magnt.balance)
magnt.take_away(10000)
print(magnt.balance)