# coding=gbk
import random
#��Ʒ
shop = [
    ["��ӥս��",1500], #0
    ["����̹��",3000], #1
    ["��Ǳͧ",2000],
    ["����ս��",1000],
    ["�Ա�����",1500],
    ["��Ӷ��",200],
    ["��Ȯ",100],
    ["�ɿ�",1200],
    ["�ֲ�������",500],
    ["����",800],     #9
]
shop1 = [shop[1][0],shop[1][1] / 2]
shop2 = [shop[7][0],shop[7][1] / 600 * 300]

#�ʽ�
money = input("�����������ʽ�")
money = int(money)
money1 = money
#���ﳵ
shopcar = []
yhq = random.randint(1,31)
print(yhq)
print("---------�Ż�ȯ����---------")
print("1~10�� 10�Ųɿ��Ż�ȯ����600��300\n11~30�� 20������̹���Ż�ȯ������˦��")
print("---------------------------")

if 1 <= yhq <= 10:
    print("��ϲ�����鵽1�Ųɿ��Ż�ȯ����600��300")
    be2 = 0
    be1 = 1
else:
    print("��ϲ�����鵽1������̹���Ż�ȯ������˦��")
    be1 = 0
    be2 = 1

while True:
    for index,value in enumerate(shop):
        print(index,"    ",value)

    #�����빺�����Ʒ���
    num = input("������Ҫ�������Ʒ��ţ�")

    if num.isdigit():
        num = int(num)
        if 0 <= num < len(shop):
            #��������̹�����
            if num == 1:
                #�����Ż�ȯ�ж�
                if be1 == 0:
                    print("�����Ż�ȯ�Ƿ�ʹ�á�������1���ǡ���2����")
                    kc = int(input(":"))
                    #�Ƿ�ʹ���Ż�ȯ�ж�
                    if kc == 1:
                        be1 = be1 + 1
                        if money >= shop[num][1]:
                            money = money - shop1[1]
                            shopcar.append(shop1)
                            print("����ɹ�������")
                            print("���ĵ�ǰ���Ϊ��",money)
                        else:
                            print("�Բ��������ʽ��㣡����")
                        # else:
                        #     print("��ʹ�ù��Ż�ȯ�������Ż�ȯ������")
                    elif kc == 2:
                        if money >= shop[num][1]:
                            money = money - shop[num][1]
                            shopcar.append(shop[num])
                            print("����ɹ�������")
                            print("���ĵ�ǰ���Ϊ��",money)
                        else:
                            print("�Բ��������ʽ��㣡����")

                    else:
                        print("����Ƿ�������")
                else:
                    if money >= shop[num][1]:
                        money = money - shop[num][1]
                        shopcar.append(shop[num])
                        print("����ɹ�������")
                        print("���ĵ�ǰ���Ϊ��",money)
                    else:
                        print("�Բ��������ʽ��㣡����")




            #����ɿ����
            elif num == 7:
                #�����Ż�ȯ�ж�
                if be2 == 0:
                    print("�����Ż�ȯ�Ƿ�ʹ�á�������1���ǡ���2����")
                    tqtk = int(input(":"))
                    #�Ƿ�ʹ���Ż�ȯ�ж�
                    if tqtk == 1:
                        be2 = be2 + 1
                        if money >= shop[num][1]:
                            money = money - shop2[1]
                            shopcar.append(shop2)
                            print("����ɹ�������")
                            print("���ĵ�ǰ���Ϊ��",money)
                        else:
                            print("�Բ��������ʽ��㣡����")
                    # else:
                    #     print("��ʹ�ù��Ż�ȯ�������Ż�ȯ������")
                    elif tqtk == 2:
                        if money >= shop[num][1]:
                            money = money - shop[num][1]
                            shopcar.append(shop[num])
                            print("����ɹ�������")
                            print("���ĵ�ǰ���Ϊ��",money)
                        else:
                            print("�Բ��������ʽ��㣡����")

                    else:
                        print("����Ƿ�������")
                else:
                    if money >= shop[num][1]:
                        money = money - shop[num][1]
                        shopcar.append(shop[num])
                        print("����ɹ�������")
                        print("���ĵ�ǰ���Ϊ��",money)
                    else:
                        print("�Բ��������ʽ��㣡����")


            else:
                if money >= shop[num][1]:
                    money = money - shop[num][1]
                    shopcar.append(shop[num])
                    print("����ɹ�������")
                    print("���ĵ�ǰ���Ϊ��",money)
                else:
                    print("�Բ��������ʽ��㣡����")
        else:
            print("����Ʒ�����ڣ���������")

    elif num == "Q" or num == "q":
        print("�˳��̳ǣ�����")
        break

    else:
        print("����Ƿ�����������")

#����������Ҫ���һ�¹����嵥
print("---------����СƱ����----------")
for index,value in enumerate(shopcar):
    print(index,"    ",value)
print("���ĵ�ǰ���Ϊ��",money)
print("�����������ۼƻ��֣�",(money1 - money)/10)
print("����ӭ�´ι��٣�������")
