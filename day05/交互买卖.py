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
kc = 0
tqtk = 0

if 1 <= yhq <= 10:
    shop[7][1] = shop[7][1] / 600 * 300

else:
    shop[1][1] = shop[1][1] / 2

while True:
    for index,value in enumerate(shop):
        print(index,"    ",value)

    #�����빺�����Ʒ���
    num = input("������Ҫ�������Ʒ��ţ�")

    if num.isdigit():
        num = int(num)
        if 0 <= num < len(shop):
            if num == 7:
                kc = kc + 1
                if kc < 2:
                    if money >= shop[num][1]:
                        money = money - shop[num][1]
                        shopcar.append(shop[num])
                        print("����ɹ�������")
                        print("���ĵ�ǰ���Ϊ��",money)
                        shop[7][1] = shop[7][1] * 2
                    else:
                        print("�Բ��������ʽ��㣡����")
                # elif kc == 2:
                #     # shop[7][1] = shop[7][1] * 2
                #     if money >= shop[num][1]:
                #         money = money - shop[num][1]
                #         shopcar.append(shop[num])
                #
                #         print("����ɹ�������")
                #         print("���ĵ�ǰ���Ϊ��",money)
                #     else:
                #         print("�Բ��������ʽ��㣡����")

                else:
                    if money >= shop[num][1]:
                        money = money - shop[num][1]
                        shopcar.append(shop[num])
                        print("����ɹ�������")
                        print("���ĵ�ǰ���Ϊ��",money)
                    else:
                        print("�Բ��������ʽ��㣡����")
            elif num == 1:
                tqtk = tqtk + 1
                if tqtk < 2:
                    if money >= shop[num][1]:
                        money = money - shop[num][1]
                        shopcar.append(shop[num])
                        print("����ɹ�������")
                        print("���ĵ�ǰ���Ϊ��",money)
                        shop[1][1] = shop[1][1] * 2
                    else:
                        print("�Բ��������ʽ��㣡����")
                # elif tqtk == 2:
                #     # shop[1][1] = shop[1][1] * 2
                #     if money >= shop[num][1]:
                #         money = money - shop[num][1]
                #         shopcar.append(shop[num])
                #
                #         print("����ɹ�������")
                #         print("���ĵ�ǰ���Ϊ��",money)
                #     else:
                #         print("�Բ��������ʽ��㣡����")
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
            print("����Ʒ�����ڣ���������������")

    #����qQ�˳�
    elif num == "Q" or num == "q":
        print("�˳��̳ǣ�����")
        break
    else:
        print("����Ƿ���������\n����������")

#����������Ҫ���һ�¹����嵥
print("---------����СƱ����----------")
for index,value in enumerate(shopcar):
    print(index,"    ",value)
print("���ĵ�ǰ���Ϊ��",money)
print("�����������ۼƻ��֣�",(money1 - money)/10)
print("����ӭ�´ι��٣�������")
























