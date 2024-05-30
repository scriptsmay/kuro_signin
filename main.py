
import time
import datetime
import json
from package.bbs import getbbsforum, getpostdetail, likeposts,shareposts,getTotalGold,mingchaosignin,bbssignin
from package.serverjiang import sc_send
from package.notify_tg import send_notify

def sign_in():
    now = datetime.datetime.now()
    month = now.strftime("%m")

    # 从JSON文件中读取数据
    with open('config.json', encoding='utf-8') as f:
        data = json.load(f)

    # 从数据中获取用户数据列表
    users = data['users']

    # sckey
    sckey = data['sckey']

    # tg推送机器人key
    send_key = data['send_key']


    for user in users:
        wechattext=""
        name= user['name']
        roleId = user['roleId']
        tokenraw = user['tokenraw']
        userId = user['userId']
        devcode= user['devCode']

        
        
        #鸣潮签到
        

        print(now.strftime("%Y-%m-%d"))
        wechattext=wechattext+now.strftime("%Y-%m-%d")+" "+name+"鸣潮签到\n\n"
        print(name)
        print("=====================================")
        response0=mingchaosignin(tokenraw,roleId,userId,month)
        print(response0)
        wechattext=wechattext+str(response0)+"\n\n"
        print("=====================================")
        time.sleep(1)


        #库街区签到

        response1 = bbssignin(tokenraw)
        wechattext=wechattext+str(response1)+"\n\n"
        print(response1)
        print("=====================================")
        time.sleep(1)
        print("签到完毕，开始点赞帖子")
        wechattext=wechattext+"签到完毕，开始点赞帖子\n\n"

        idlist=getbbsforum(tokenraw,devcode)
        post_user_pairs = [(post["postId"], post["userId"]) for post in idlist["data"]["postList"]]
        i=0
        for postid, userid in post_user_pairs:
            getpostdetail(tokenraw,devcode,postid)
            time.sleep(5)
            print("第"+str((i+1))+"个帖子"+likeposts(tokenraw,devcode,postid,userid))
            wechattext=wechattext+"第"+str((i+1))+"个帖子"+str(likeposts(tokenraw,devcode,postid,userid))+"\n\n"
            time.sleep(3)
            i+=1
            if i>4:
                break
        print("=====================================")

        #转发帖子
        print("点赞完毕，开始转发帖子")
        wechattext=wechattext+"点赞完毕，开始转发帖子\n\n"
        print(shareposts(tokenraw,devcode))
        wechattext=wechattext+shareposts(tokenraw,devcode)+"\n\n"
        print("=====================================")


        #获取金币数量
        gold=getTotalGold(tokenraw,devcode)
        goldnum=gold["data"]["goldNum"]
        print("现在剩余："+str(goldnum)+"金币")
        wechattext=wechattext+"现在剩余："+str(goldnum)+"金币\n\n"
        print(name+"签到完毕")

        # 发送微信通知
        if sckey:
            print(sc_send(name+"签到",wechattext,key=sckey))

        # 发送tg推送
        if send_key:
            print(send_notify(name+"签到结果：", wechattext, send_key=send_key))

