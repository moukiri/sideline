class sideline():
    def __init__(self,date,exchange_rate,sales,travel_expenses):
        self.date = date
        self.exchange_rate = exchange_rate  #汇率
        self.sales = sales #营业额
        self.travel_expenses = travel_expenses

    def cal_price(self,project):
        self.project = project

        if self.project == "offline": #扫街
            if self.exchange_rate > 4.8 and self.sales > 10000:
                self.price = 0.06 * self.sales
            if self.exchange_rate > 4.8 and self.sales < 10000:
                self.price = 0.062 * self.sales
            if self.exchange_rate < 4.8 and self.sales > 10000:
                self.price = 0.058 * self.sales
            if self.exchange_rate < 4.8 and self.sales < 10000:
                self.price = 0.06 * self.sales

        if self.project == "gachapon": #扭蛋
            if self.exchange_rate > 4.8 :
                self.price = 0.06 * self.sales
            if self.exchange_rate < 4.8 :
                self.price = 0.055 * self.sales

        if self.project == "online": #通贩
            if self.exchange_rate > 4.8 :
                self.price = 0.053 * self.sales
            if self.exchange_rate < 4.8 :
                self.price = 0.052 * self.sales

        self.summarize = self.price + self.travel_expenses

    def print_bill(self):
        print(f"扫街日期:{self.date}\n"
              f"今日汇率:{self.exchange_rate}\n"
              f"扫街总额(円):{self.sales}\n"
              f"收rmb:{self.summarize}")

project1 = sideline("2025/03/5",4.85,8000,10)
project1.cal_price("gachapon")
project1.print_bill()
