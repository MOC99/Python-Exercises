UserPurchase_dict = {"原味奶茶":0,"香蕉冰奶茶":0,"草莓冰奶茶":0,"蒟蒻冰奶茶":0,"珍珠冰奶茶":0}
Naicha_Price = {"原味奶茶":3,"香蕉冰奶茶":5,"草莓冰奶茶":5,"蒟蒻冰奶茶":7,"珍珠冰奶茶":7}
Naicha_List = [["原味奶茶",1],["香蕉冰奶茶",2],["草莓冰奶茶",3],["蒟蒻冰奶茶",4],["珍珠冰奶茶",5]]
Vip_dict = {"151448511":1,"13256232":2}
UserPurchase_Naicha = {"VipNum":0,"NaichaNum":0,"BuyNum":0}
User_List =[]

i = 0
keyword = 0
cout_buy = 0

# Vip判断函数
def UserVip():
    Vip_key = int(input("请输入您的会员号："))
    UserPurchase_Naicha["VipNum"] = Vip_key
    for key in Vip_dict.keys():
        if Vip_key == Vip_dict[key]:
            print("您将享受九折优惠")
            keyword = 1
            return keyword
        else:
            print("木有找到哦")

def UserNotVip():
    Vip_num = input("请输入您要设置的会员号：")
    Vip_tel =input("请继续输入您的手机号：")
    UserPurchase_Naicha["VipNum"] = Vip_num
    Vip_dict[Vip_num] = Vip_tel
    print("Thanks!下次光临时生效")
    return keyword

# 输出函数
def UserPurchase_Print(i):
    print("您选购的奶茶如下")
    TotalPrice_User = 0
    for NaichaKind in UserPurchase_dict.keys():
        if UserPurchase_dict[NaichaKind]!=0:
            print("{}   {}".format(NaichaKind,UserPurchase_dict[NaichaKind]))
        TotalPrice_Naicha = UserPurchase_dict[NaichaKind]*Naicha_Price[NaichaKind]
        TotalPrice_User += TotalPrice_Naicha
    if i == 1:
        print("您本次消费总共{}".format(TotalPrice_User*0.9))
    else:
        print("您本次消费总共{}".format(TotalPrice_User))

#选择函数
def UserChoose_Naicha(i):
    UserPurchase_dict[Naicha_List[i][0]] = int(input("请输入您所需要的数量："))
    UserPurchase_Naicha["NaichaNum"] = Naicha_List[i][1]
    UserPurchase_Naicha["BuyNum"] = UserPurchase_dict[Naicha_List[i][0]]


#用户界面
def UserScreen():
    print("欢迎光临小象奶茶店，本店销售以下品种的奶茶：\n"
          "①原味奶茶    ￥3  ②香蕉冰奶茶    ￥5  "
          "③草莓冰奶茶    ￥5\n④蒟蒻冰奶茶  ￥7  "
          "⑤珍珠冰奶茶    ￥7")
    alter_num = "y"
    while alter_num == "y":
        num_guest = int(input("请输入1-5来选择您所需要的奶茶："))
        if num_guest == 1 or num_guest == 2 or num_guest == 3 or num_guest == 4 or num_guest == 5:
            UserChoose_Naicha(num_guest-1)
        else:
            print("Woops! 我们只售卖以上五种奶茶哦!新口味敬请期待!")
        alter_num = input("您想继续选购吗?想的话请输入Y，不想的话请输入N：")
        User_List.append(UserPurchase_Naicha)

#主函数main()
def main():
    for j in range(1,21):
        print("第{}位顾客您好！".format(j))
        UserScreen()
        vip = input("您是否为会员：(y/n)")
        if vip == "y":
            keyword = UserVip()
        else:
            keyword = UserNotVip()
        UserPurchase_Print(keyword)
        print("####$$$$##Terminal##$$$$####")
        print(User_List)
        print(Vip_dict)
        print("####$$$$##Terminal##$$$$####")

main()
