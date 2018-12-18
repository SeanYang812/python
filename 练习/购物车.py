

goods_list = [
    ['变形金刚','100'],
    ['钢铁侠','500'],
    ['蜘蛛侠','250'],
    ['浩克','666']
]
count = 0
total = 0
balance_price = 0
shopping_cart = {}
# while True:
print("-----请选择你的商品------\n",'商品编号 商品名称 商品价格')
for i, goods in enumerate(goods_list):
    # print(i+1,goods)
    print('\r', i + 1, '****', goods[0], '****', goods[1])
while True:
    for i,goods in enumerate(goods_list):
        inp = input("请输入你选择的商品编号：").strip()
        print(i)
        if inp.isdigit():
            inp = int(inp)
            if inp == i+1:
                goods_name = goods_list[inp-1][0]
                goods_price = int(goods_list[inp-1][1])
                print(goods_name,goods_price)
                if goods_name in shopping_cart:
                    shopping_cart[goods_name]['count'] += 1
                else:
                    shopping_cart[goods_name] = {'goods_price':goods_price,'count':1}
                balance_price += goods_price
                print('购物车列表：',shopping_cart)
                print('商品总价：',balance_price)
            else:
                print('输入编号不存在，请重新输入')
                continue
        else:
            print('请输入编号')
            continue



