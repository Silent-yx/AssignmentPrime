import sys
import pygame

class EventList:
    class eve:
        def __init__(self , image , text , choice_num , choice_text , resulttext):
            self.image = image
            self.text = text
            self.choice_num = choice_num
            self.choice_text = choice_text
            self.resulttext = resulttext
        
    #事件总数，每次加事件的时候记得改
    event_num = 10
    
    evelist = []
    #属性增减 饥饿值 口渴值 san值 智商 清洁值 时间(单位15min) (单个事件的时间不要超过37)
    effect = []
    #选选项的需求 最小值）无要求就是0 时间要求不计在此处
    limit = []
    #做出选择后在状态栏出现的信息
    message = []
    #刷出该事件的需求，无要求为0 最后两项为时间下限和上限 范围在32~88之间 无要求则同时为0
    refreshneed = []

    #! 有特殊影响的事件在dormitory中的specialeffect处添加！！！
    
    #时间对照: ( 8:00 -> 32 ) ( 22:00 -> 88 )
        
    #0
    evelist.append(eve("../res/image/要迟到了.png","早上睡迟了，要不要翘课呢",2 ,["翘！","不翘！"] , ["翘的好！","冲去上课，满身是汗"]))
    effect.append([[0,0,0,-1,0,4],[0,0,0,0,-1,4]])
    limit.append([[0,0,0,1,0],[0,0,0,0,0]])
    message.append(["翘课睡觉咯，智商-1","冲去上课，满身是汗，清洁值-1"])
    refreshneed.append([0,0,0,0,0,32,40])
    #1
    evelist.append(eve("../res/image/老坛酸菜.png","隔壁老铁送来老坛酸菜牛肉面，要不要吃捏",2 ,["吃","不吃！"] , ["就这味儿！干净又卫生！","..."]))
    effect.append([[+1,0,0,0,-1, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,1],[0,0,0,0,0]])
    message.append(["吃了老坛酸菜牛肉面，饥饿值+1，清洁值-1","谢绝了隔壁老铁的老坛酸菜牛肉面"])
    refreshneed.append([0,0,0,0,0,0,0])
    #2 test用 记得替换掉
    evelist.append(eve("../res/image/睡觉.png","小咪亿下",1 ,["睡！"] , ["zzZZZZZZZZ..."]))
    effect.append([[0,0,0,0,0,36]])
    limit.append([[0,0,0,0,0]])
    message.append(["小睡了亿下"])
    refreshneed.append([0,0,0,0,0,0,0])
    #3 test用 记得替换掉
    evelist.append(eve("../res/image/test事件.png","开挂！！！",1 ,["上上下下左右左右BA！"] , ["外挂已付费"]))
    effect.append([[10,10,10,10,10,0]])
    limit.append([[0,0,0,0,0]])
    message.append(["开个小挂 不过分吧 全属性回满 全物品+5"])
    refreshneed.append([0,0,0,0,0,0,0])
    #4 记得替换掉
    evelist.append(eve("../res/image/test事件.png","采购时间！",1 ,["出发！"] , ["物资补充了！"]))
    effect.append([[0,0,0,0,0,12]])
    limit.append([[0,0,0,0,0]])
    message.append(["去超市补充了物资"])
    refreshneed.append([0,0,0,0,0,48,60])
    #5 周常核酸检测
    evelist.append(eve("../res/image/核酸检测.png","核酸检测",2 ,["马上去做","叛逆！不去！"] , ["排了一条从图书馆到操场超长大队，终于做了核酸，嗓子好痛","在宿舍里边吃零食边卷卷，舒服了"]))
    effect.append([[0,0,0,0,0,24],[0,0,0,2,0,12]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["排了一条从图书馆到操场超长大队，终于做了核酸","在宿舍舒适地卷卷，智商+2"])
    refreshneed.append([0,0,0,0,0,56,88])
    #6 敲门 查卫生
    evelist.append(eve("../res/image/哐哐哐敲门.png","叮叮当,有人敲门", 2 ,["开门","一定有鬼,不开"] , ["宿管查卫生,寄！","..."]))
    effect.append([[0,0,-1,0,+1, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["┭┮﹏┭┮ 被迫整理 san值-1 清洁值+1","不开门好像不太好"])
    refreshneed.append([0,0,0,0,0,48,60])
    #7敲门 送六个核桃
    evelist.append(eve("../res/image/咚咚咚敲门.png","咚咚咚,有人敲门", 2 ,["开门","一定有鬼,不开"] , ["隔壁朋友送来六个核桃,提神醒脑","..."]))
    effect.append([[0,0,0,+1,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["喝了六个核桃 智商+1","不开门好像不太好"])
    refreshneed.append([0,0,0,0,0,48,88])
    #8砸门 恶作剧
    evelist.append(eve("../res/image/砸门.png","哐哐哐,有人砸门", 2 ,["战战兢兢开门","这回真滴一定有鬼,坚决不开"] , ["门口空无一人","..."]))
    effect.append([[0,0,-2,0,0, 1],[0,0,0,0,0, 1]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["没人。。。 san值-2","不应该开门"])
    refreshneed.append([0,0,0,0,0,48,88])
    #9二课读书 崩了
    evelist.append(eve("../res/image/二课.png","室友拉你去参加悦读二课", 2 ,["好耶","算了，万一二课又崩了"] , ["好书啊好书，不过二课果然崩了","还好没去，二课崩了"]))
    effect.append([[0,0,-1,+1,0, 8],[0,0,0,+1,0, 8]])
    limit.append([[0,0,0,0,0],[0,0,0,0,0]])
    message.append(["读书收获 智商+1 签到失败 san值-1","暗自庆幸 san值+1"])
    refreshneed.append([0,0,0,0,0,48,88])

