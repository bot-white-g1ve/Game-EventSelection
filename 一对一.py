import json
import random
import base64

#######
# 设置参数
己方随机选择 = True
#######

with open('武器.json', 'r', encoding="utf-8") as file:
    武器 = json.load(file)
if 己方随机选择:
    选取武器名称, 选取武器属性 = random.choice(list(武器.items()))
else: 
    选取武器名称 = '诅咒之钉' # 设置参数
    选取武器属性 = 武器[选取武器名称]
敌人武器名称, 敌人武器属性 = random.choice(list(武器.items()))

with open('防具.json', 'r', encoding="utf-8") as file:
    防具 = json.load(file)
if 己方随机选择:
    选取防具名称, 选取防具属性 = random.choice(list(防具.items()))
else:
    选取防具名称 = '染血玩偶服' # 设置参数
    选取防具属性 = 防具[选取防具名称]
敌人防具名称, 敌人防具属性 = random.choice(list(防具.items()))

print(f"你选取的武器是{选取武器名称}，你选取的防具为{选取防具名称}")
print(f"敌人选取的武器是{敌人武器名称}，你选取的防具为{敌人防具名称}")
print(f"========")

def 计算点数(武器属性, 防具属性):
    总点数 = 0
    for 属性名称, 武器属性数值范围 in 武器属性.items():
        武器属性数值 = random.randint(武器属性数值范围[0], 武器属性数值范围[1])
        if 属性名称 in 防具属性:
            temp点数 = 武器属性数值*防具属性[属性名称]
            print(f"在{属性名称}属性上，投出{武器属性数值}，对方防具使攻击效果变成{防具属性[属性名称]}，最后点数为{temp点数}")
            总点数 += temp点数
        else:
            print(f"在{属性名称}属性上，投出{武器属性数值}，对方防具使攻击效果变成1，最后点数为{武器属性数值}")
            总点数 += 武器属性数值
    return 总点数

print("你发起攻击")
print(f"你的点数为{计算点数(选取武器属性, 敌人防具属性)}")
print("========")
print(f"敌人发起攻击")
print(f"敌人的点数为{计算点数(敌人武器属性, 选取防具属性)}")