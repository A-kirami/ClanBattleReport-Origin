import json
import sqlite3
from PIL import Image,ImageFont,ImageDraw
import os


def get_db_path():
    if not (os.path.isfile(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                                        "yobot/yobot/src/client/yobot_data/yobotdata.db"))) or os.access(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                                                                                                                                      "yobot/yobot/src/client/yobot_data/yobotdata.db")), os.R_OK)):
        raise OSError
    db_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                               "yobot/yobot/src/client/yobot_data/yobotdata.db"))
    return db_path

def get_web_address():
    if not (os.path.isfile(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                                        "yobot/yobot/src/client/yobot_data/yobotdata.db"))) or os.access(os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                                                                                                                                      "yobot/yobot/src/client/yobot_data/yobotdata.db")), os.R_OK)):
        raise OSError
    config_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../"
                                                   "yobot/yobot/src/client/yobot_data/yobot_config.json"))
    with open(f'{config_path}', 'r', encoding='utf8')as fp:
        yobot_config = json.load(fp)
        public_address = str(yobot_config["public_address"])
        if str(yobot_config["public_address"]).endswith("/"):
            public_address = str(yobot_config["public_address"])[:-1]
        web_address = public_address + ":" + str(yobot_config["port"])
        return web_address

font_path = os.path.join(os.path.dirname(__file__), 'RZYCY.ttf')

try:
    db_path = get_db_path()
except OSError:
    db_path = '' # 若非yobot插件版，请在此处配置数据库路径


def add_text(img: Image,text:str,textsize:int,font=font_path,textfill='white',position:tuple=(0,0)):
    #textsize 文字大小
    #font 字体，默认微软雅黑
    #textfill 文字颜色，默认黑色
    #position 文字偏移（0,0）位置，图片左上角为起点
    img_font = ImageFont.truetype(font=font,size=textsize)
    draw = ImageDraw.Draw(img)
    draw.text(xy=position,text=text,font=img_font,fill=textfill)
    return img

def add_text1(img: Image,text:str,textsize:int,font=font_path,textfill='white',position:tuple=(0,0)):
    #textsize 文字大小
    #font 字体，默认微软雅黑
    #textfill 文字颜色，默认黑色
    #position 文字偏移（0,0）位置，图片左上角为起点
    img_font = ImageFont.truetype(font=font,size=textsize)
    draw = ImageDraw.Draw(img)
    draw.text(xy=position,text=text,font=img_font,fill=textfill)
    return img
    
def get_apikey(gid: int) -> str:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f'select apikey from clan_group where group_id={gid}')
    apikey = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return apikey 
    
def get_GmServer(gid: int) -> str:
    conn = sqlite3.connect(db_path)
    cur = conn.cursor()
    cur.execute(f'select game_server from clan_group where group_id={gid}')
    game_server = cur.fetchall()[0][0]
    cur.close()
    conn.close()
    return game_server


#print(db_path)
#print(get_web_address())
