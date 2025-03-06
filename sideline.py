class sideline():
    def __init__(self,date,exchange_rate,number,sales,travel_expenses):
        self.date = date
        self.exchange_rate = exchange_rate  #汇率
        self.number = number #件数
        self.sales = sales #营业额
        self.travel_expenses = travel_expenses
        self.project_aliases = {
            "s": "offline",  # 扫街
            "n": "gachapon",  # 扭蛋
            "t": "online",  # 通贩
            "c": "market vendors"  # 場販 目前没写汇率
        }

    def cal_price(self,project):
        self.project = self.project_aliases.get(project, project)

        if self.project == "offline":
            if self.exchange_rate > 4.8 and self.sales > 10000:
                self.price = 0.06 * self.sales
            elif self.exchange_rate > 4.8 and self.sales < 10000:
                self.price = 0.062 * self.sales
            elif self.exchange_rate < 4.8 and self.sales > 10000:
                self.price = 0.058 * self.sales
            else:
                self.price = 0.06 * self.sales

        if self.project == "gachapon":
            if self.exchange_rate > 4.8 :
                self.price = 0.06 * self.sales
            elif self.exchange_rate < 4.8 :
                self.price = 0.055 * self.sales

        if self.project == "online":
            if self.exchange_rate > 4.8 :
                self.price = 0.053 * self.sales
            elif self.exchange_rate < 4.8 :
                self.price = 0.052 * self.sales

        self.summarize = self.price + self.travel_expenses

    def print_bill(self):
        print(f"日期:{self.date}\n"
              f"今日汇率(支付宝):{self.exchange_rate}\n"
              f"件数:{self.number}\n"
              f"总额(円):{self.sales}\n"
              f"车马(円):{self.travel_expenses}\n"
              f"收rmb:{self.summarize}")

project1 = sideline("2025/03/6",4.87,1,400,0)
project1.cal_price("n")
project1.print_bill()