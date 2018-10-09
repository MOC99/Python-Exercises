UserPurchase_dict = {"原味奶茶":0,"香蕉冰奶茶":0,"草莓冰奶茶":0,"蒟蒻冰奶茶":0,"珍珠冰奶茶":0}
Naicha_Price = {"原味奶茶":3,"香蕉冰奶茶":5,"草莓冰奶茶":5,"蒟蒻冰奶茶":7,"珍珠冰奶茶":7}
Naicha_List = [["原味奶茶",1],["香蕉冰奶茶",2],["草莓冰奶茶",3],["蒟蒻冰奶茶",4],["珍珠冰奶茶",5]]
Vip_dict = {"tel1":1,"tel2":2}
UserPurchase_Naicha = {"VipNum":0,"NaichaNum":0,"BuyNum":0}
User_List =[]
NaichaNumSet_tmp = set()
NaichaNumSet_Intersection = set()
NaichaNumSet_list = []

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
        TotalPrice_Naicha = int(UserPurchase_dict[NaichaKind])*int(Naicha_Price[NaichaKind])
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
    NaichaNumSet_tmp.add(Naicha_List[i][1])

# 奶茶推荐函数
def UserApprove(j):
    NaichaNumSet_dict = {1,2,3,4,5}
    len_tmp = 0
    len_NumTmp = 0
    len2 = len(NaichaNumSet_tmp)
    for k in range(0,j):
        NaichaNumSet_Intersection = NaichaNumSet_list[k] & NaichaNumSet_tmp
        NaichaNumSet_list.append(NaichaNumSet_Intersection)
    for k in range(0,j):
        len1 = len(NaichaNumSet_list[k])
        len_next = len(NaichaNumSet_list[k+1])
        len_def = len1/len2
        len_def_next = len_next/len2
        if len_def_next>=len_def:
            len_NumTmp = k+1
        else:
            len_NumTmp = k
    NaichaNumSet_difference = NaichaNumSet_dict-NaichaNumSet_list[len_NumTmp]
    print("买了以上口味的其他顾客还喜欢{}号奶茶".format(max(NaichaNumSet_difference)))

#用户界面
def UserScreen():
    print("欢迎光临小象奶茶店，本店销售以下品种的奶茶：\n"
          "①原味奶茶    ￥3  ②香蕉冰奶茶    ￥5  "
          "③草莓冰奶茶    ￥5\n④蒟蒻冰奶茶  ￥7  "
          "⑤珍珠冰奶茶    ￥7\n本店爆款网红奶茶：蒟蒻冰奶茶")
    UserTmp = input("输入y立即购买(输入n即可跳过)：")
    if UserTmp == "y":
        UserPurchase_dict["蒟蒻冰奶茶"] = input("请输入您所需的数量：")
        NaichaNumSet_tmp.add(4)
    alter_num = input("您还想继续选购吗(y/n):")
    if alter_num == "y":
        while alter_num == "y":
            num_guest = int(input("请输入1-5来选择您所需要的奶茶："))
            if num_guest == 1 or num_guest == 2 or num_guest == 3 or num_guest == 4 or num_guest == 5:
                UserChoose_Naicha(num_guest-1)
            else:
                print("Woops! 我们只售卖以上五种奶茶哦!新口味敬请期待!")
            alter_num = input("您想继续选购吗?想的话请输入Y，不想的话请输入N：")
            User_List.append(UserPurchase_Naicha)
            NaichaNumSet_list.append(NaichaNumSet_tmp)

# Terminal界面
def Terminal():
    print("\n#####$$$$Terminal$$$$#####")
    NaichaNumSet_tmp.clear()
    print(NaichaNumSet_tmp)
    print(NaichaNumSet_list)
    print(User_List)
    print("#####$$$$Terminal$$$$#####\n")

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
        k = j-1
        if k != 0:
            UserApprove(j)
    Terminal()                          # 20位顾客招待完后自动显示

main()
