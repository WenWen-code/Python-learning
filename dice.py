# 创建包含三个测量站点的列表，每个元素为字典
tel1 = {'ID': 'C001', 'coord': (32.1234, 118.7654), 'height': 45.6}
tel2 = {'ID': 'C003', 'coord': (25.1235, 130.2394), 'height': 50.3}
tel3 = {'ID': 'C004', 'coord': (30.2356, 892.2938), 'height': 80.8}
station = [tel1, tel2, tel3]

# 添加新增站点
dx = int(input("请输入新增站点的个数: "))
for y in range(dx):
    tel4 = {}
    for x in range(3):
        key = input("请输入键: ")
        if x == 1:
            value = input("请输入值: ")
            coords = value.split(',')
            if float(coords[0]) > 90.0 or float(coords[0]) < -90.0 or float(coords[1]) > 180.0 or float(coords[1]) < -180.0:
                print("坐标不符合标准")
                break
            tel4[key] = tuple(map(float, coords))
        elif x == 2:
            value = int(input("请输入值: "))
            tel4[key] = value
        else:
            value = input("请输入值: ")
            tel4[key] = value
    station.append(tel4)

# 检查是否有重复ID
ids = [s['ID'] for s in station]
if len(ids) == len(set(ids)):
    print("无重复ID")
else:
    print("有重复ID")

# 按高程升序排序
station.sort(key=lambda z: z['height'])

# 根据ID查询坐标（使用字典键值访问）
telx = input("请输入想要查询对象的ID: ")
for s in station:
    if telx == s['ID']:
        print(s)
        # 修改坐标或名称
        ds = input("输入0修改名称，输入1修改坐标: ")
        if ds == '0':
            s['ID'] = input("请输入新的ID: ")
        elif ds == '1':
            new_coords = input("请输入新的坐标: ").split(',')
            s['coord'] = tuple(map(float, new_coords))
        break

# 统计区域范围（找出最大最小经纬度坐标）
num1 = []
num2 = []
for s in station:
    num1.append(s['coord'][0])
    num2.append(s['coord'][1])
max_a1 = max(num1)
min_b1 = min(num1)
max_a2 = max(num2)
min_b2 = min(num2)
print("坐标最大和最小值为", max_a1, min_b1, max_a2, min_b2)

# 统计在指定范围内的坐标数量
num1 = float(input("请输入范围的小值: "))
num2 = float(input("请输入范围的大值: "))
dy = 0
for s in station:
    if num1 <= s['coord'][0] <= num2 and num1 <= s['coord'][1] <= num2:
        dy += 1
print("在范围内的坐标有", dy, "个")

# 根据ID删除列表中的元素
dID = input("输入想要删除的站点的ID: ")
for s in station:
    if dID == s['ID']:
        station.remove(s)
        break

# 在已创建的测量站点列表中给每个测量站点增加坐标信息
print("增加信息")
for s in station:
    key = 'crs'
    value = input("请输入值: ")
    s[key] = value

print(station)