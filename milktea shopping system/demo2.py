cout_buy = 0
cust_list =[]
vip_list = [1,2,3,4,5]
for j in range(2):
    alter_num = "y"
    nc_list = [["原味奶茶",3,0,0],["香蕉冰奶茶",5,0,0],["草莓冰奶茶",5,0,0],["蒟蒻冰奶茶",7,0,0],["珍珠冰奶茶",7,0,0]]
    print("欢迎光临小象奶茶店，本店销售以下品种的奶茶：\n"
          "①原味奶茶    ￥3  ②香蕉冰奶茶    ￥5  "
          "③草莓冰奶茶    ￥5\n④蒟蒻冰奶茶  ￥7  "
          "⑤珍珠冰奶茶    ￥7")
    alter_input = input("您是会员不？y/n")
    if alter_input == "y":
        vip_input = int(input("请输入您的会员号："))
        for element in vip_list:
            if vip_input == element:
                print("欢迎回来")
                i = 1
    else:
        vip_new = int(input("请输入您想设置的会员号："))
        vip_list.append(vip_new)
        print("感谢您的加入，下次生效")
        i = 0
    while alter_num == "y":
        num_guest = int(input("请输入1-5来选择您所需要的奶茶："))
        if num_guest == 1 or num_guest == 2 or num_guest == 3 or num_guest == 4 or num_guest == 5:
            if num_guest == 1:
                nc_list[0][2] = int(input("请输入您所需要的数量："))
                nc_list[0][3] = nc_list[0][2]*nc_list[0][1]
            if num_guest == 2:
                nc_list[1][2] = int(input("请输入您所需要的数量："))
                nc_list[1][3] = nc_list[1][2]*nc_list[1][1]
            if num_guest == 3:
                nc_list[2][2] = int(input("请输入您所需要的数量："))
                nc_list[2][3] = nc_list[2][2] * nc_list[2][1]
            if num_guest == 4:
                nc_list[3][2] = int(input("请输入您所需要的数量："))
                nc_list[3][3] = nc_list[3][2]*nc_list[3][1]
            if num_guest == 5:
                nc_list[4][2] = int(input("请输入您所需要的数量："))
                nc_list[4][3] = nc_list[4][2]*nc_list[4][1]
        else:
            print("Woops! 我们只售卖以上五种奶茶哦!新口味敬请期待!")
        alter_num = input("您想继续选购吗?想的话请输入Y，不想的话请输入N：")
    for element in nc_list:
        cout_buy = cout_buy + int(element[3])
        i=+1
    if i == 1:
        print("您将享受九折优惠！")
        cout_buy = cout_buy*0.9
    else:
        print("您注册的会员下次生效")
    print("您的购物清单如下：")
    for element in nc_list:
        if element[3] == 0:
            continue
        print("奶茶名：{}，数量：{}，总价：{}".format(element[0],element[2],element[3]))
    print("本次您购物总金额为：{}".format(cout_buy))
    cust_list.append([j,nc_list[0][2],nc_list[1][2],nc_list[2][2],nc_list[3][2],nc_list[4][2]])
    import os
    #def c():
     #   os.system('cls')
for element in cust_list:
    print(element)