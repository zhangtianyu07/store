# coding=gbk
#��Ʒ
shop = [
    ["��ӥս��",1500], #0
    ["����̹��",3000], #1
    ["��Ǳͧ",2000],
    ["����ս��",1000],
    ["�Ա�����",1500],
    ["��Ӷ��",200],
    ["��Ȯ",100],
    ["�ɿ�",1300],
    ["�ֲ�������",500],
    ["����",800],     #9
]

#�ʽ�
money = input("�����������ʽ�")
money = int(money)

#���ﳵ
shopcar = []

while True:
    for index,value in enumerate(shop):
        print(index,"    ",value)

    #�����빺�����Ʒ���
    num = input("������Ҫ�������Ʒ��ţ�")

    if num.isdigit():
        num = int(num)
        if 0 <= num < len(shop):
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
print("����ӭ�´ι��٣�������")
























