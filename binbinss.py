import pymysql

db = pymysql.connect("binbinss.pro", "root", "ZhfsjtJHfiZhRsYB", "sspanel", charset='utf8')
cursor = db.cursor()


def num_to_string(num):
    numbers = {
        '1': 'id',
        '2': "money",
        '3': "node_speedlimit",
        '4': "node_connector"
    }
    return numbers.get(num)


def update(user_id, item, value):
    sql = "UPDATE user SET %s = %s WHERE id = %s " % (item, value, user_id)
    print(sql)
    return sql


def select(username):

    sql = "SELECT * FROM user WHERE email like '%s'" %username
    return sql


def find():
    user = input("请输入您要查询的email(支持模糊查找):")
    fin_user = "%" + user + "%"
    cursor.execute(select(fin_user))
    results = cursor.fetchall()
    for row in results:
        user_id = str(row[0])
        user_name = str(row[1])
        email = str(row[2])
        money = row[19]
        transfer_enable = row[9]/1024/1024/1024
        transfer_usage = (row[6]+row[7])/1024/1024/1024
        transfer_shengyu = transfer_enable - transfer_usage
        user_class = str(row[32])
        speed_limit = str(row[25])
        connector_limit = str(row[26])

        print("用户id = %s, 用户名 = %s, Email = %s, 余额 = %.2f, 总流量 = %.2f, 已用流量 = %.2f, 剩余流量 = %.2f, 用户等级 = %s, 限速 = %s, 节点连接数 = %s" \
          % (user_id, user_name, email, money, transfer_enable, transfer_usage, transfer_shengyu, user_class, speed_limit, connector_limit))


flag = 'y'

print("+------------------------------+\n+项目名：Binbinss数据库管理工具+\n+运行环境：Pyhon3              +\n+作者：binbin6106              +\n+------------------------------+")
while flag == 'y':
    switch_num = input("1.查询\n2.更改\n请输入您希望的操作：")
    if switch_num == '1':
        find()
    elif switch_num == '2':
        change_user_id = input("请输入需要更改的用户id：")
        change_user_num = input("1.用户名\n2.金额\n3.限速\n4.节点连接数\n请输入要修改的字段：")
        change_user_item = num_to_string(change_user_num)
        change_user_value = input("请输入要修改的内容：")
        cursor.execute(update(change_user_id, change_user_item, change_user_value))
        db.commit()
    else:
        print("您的输入有误")
    flag = input("是否继续？(y/n)")

db.close()
