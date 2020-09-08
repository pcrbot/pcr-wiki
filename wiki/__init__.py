import json
from hoshino import config, Service, priv
from hoshino.typing import CQEvent
from .. import chara
from .data import *

sv = Service('wiki', help_='''
[@bot简介ue] 角色简介
[@bot技能ue] 角色技能
[@bot专武ue] 角色专武
[@bot羁绊ue] 角色羁绊
'''.strip(), bundle='pcr查询')

def get_chara(name, types):
    id_ = chara.name2id(name)
    confi = 100
    if id_ == chara.UNKNOWN:
        id_, guess_name, confi = chara.guess_id(name)
    c = chara.fromid(id_)
    msg = ''
    is_npc = chara.is_npc(id_)
    if confi < 100:
        msg = f'兰德索尔似乎没有叫"{name}"的人...\n角色别称补全计划: github.com/Ice-Cirno/HoshinoBot/issues/5\n您有{confi}%的可能在找{guess_name}{c.icon.cqcode}'
    elif is_npc:
        msg = f'没有查询到{name}的wiki数据'
    else:
        msg = f'{c.icon.cqcode}'
        try:
            if types == 'introduce':
                msg += get_info(id_)
            elif types == 'skill':
                msg += get_skill(id_)
            elif types == 'uniquei':
                msg += get_uniquei(id_)
            elif types == 'kizuna':
                msg += get_kizuna(id_)
        except:
            msg += f'\n暂时没有更新{name}的数据'
    return msg

@sv.on_prefix(('简介','介绍'), only_to_me=True)
async def introduce(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"简介"+别称，如"简介ue"')
        return
    result = get_chara(name,'introduce')
    await bot.send(ev, result)

@sv.on_prefix(('技能'), only_to_me=True)
async def skill(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"技能"+别称，如"技能ue"')
        return
    result = get_chara(name,'skill')
    await bot.send(ev, result)

@sv.on_prefix(('专武'), only_to_me=True)
async def uniquei(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"专武"+别称，如"专武ue"')
        return
    result = get_chara(name,'uniquei')
    await bot.send(ev, result)

@sv.on_prefix(('羁绊'), only_to_me=True)
async def kizuna(bot, ev: CQEvent):
    name = ev.message.extract_plain_text().strip()
    if not name:
        await bot.send(ev, '请发送"羁绊"+别称，如"羁绊ue"')
        return
    result = get_chara(name,'kizuna')
    await bot.send(ev, result)

@sv.on_fullmatch(('更新wiki'))
async def update_wiki(bot, ev: CQEvent):
    if priv.get_user_priv(ev) < priv.SUPERUSER:
        return
    local_version = get_file_md5()
    download_addres = 'https://alphaone-my.sharepoint.cn/personal/yu_vip_tg/_layouts/15/download.aspx?UniqueId=90bc6f10-7493-45fd-90e9-9d3083fcc8c1&Translate=false&tempauth=eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJhdWQiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAvYWxwaGFvbmUtbXkuc2hhcmVwb2ludC5jbkAzYjFjODFiMS1kMTU2LTRhZjktYjE2OS1hZTA4MTI4YzAzOTYiLCJpc3MiOiIwMDAwMDAwMy0wMDAwLTBmZjEtY2UwMC0wMDAwMDAwMDAwMDAiLCJuYmYiOiIxNTk5NTMxMzU3IiwiZXhwIjoiMTU5OTUzNDk1NyIsImVuZHBvaW50dXJsIjoiK1M1LzlHRWJwYnFMV1pPN1M4TGcvc09QanRxVWJpZFE3R2tvb3hINnZIOD0iLCJlbmRwb2ludHVybExlbmd0aCI6IjE0MCIsImlzbG9vcGJhY2siOiJUcnVlIiwiY2lkIjoiWkRObFl6WXdNVEF0WTJJMFppMDBNMlUxTFRsbE1qVXRZV0k1TlRBek1XWmpaR1JsIiwidmVyIjoiaGFzaGVkcHJvb2Z0b2tlbiIsInNpdGVpZCI6Ik0ySTRNbU16WkRrdFpXWmlaUzAwWWpnekxUaGxaV1F0Tmprd09HVmxZbVJpTXpsbCIsImFwcF9kaXNwbGF5bmFtZSI6ImRyaXZlLm1pY2hpa2F3YWNoaW4uYXJ0Iiwic2lnbmluX3N0YXRlIjoiW1wia21zaVwiXSIsImFwcGlkIjoiODZkNzEzOGItMmFhYS00NzZlLTk4MDgtZDRkZGQ5NWIzZjNjIiwidGlkIjoiM2IxYzgxYjEtZDE1Ni00YWY5LWIxNjktYWUwODEyOGMwMzk2IiwidXBuIjoieXVAdmlwLnRnIiwicHVpZCI6IjEwMDMzMjMwQzU3N0FDOTgiLCJjYWNoZWtleSI6IjBoLmZ8bWVtYmVyc2hpcHwxMDAzMzIzMGM1NzdhYzk4QGxpdmUuY29tIiwic2NwIjoiYWxsZmlsZXMud3JpdGUiLCJ0dCI6IjIiLCJ1c2VQZXJzaXN0ZW50Q29va2llIjpudWxsfQ.WG5Oc3oyYkdOSVQ1TzI3T2hENW9remhGS1E0bWRtUFpWajhyUURjTXBRQT0&ApiVersion=2.0'
    f = requests.get(download_addres)
    with open(os.path.join(os.path.dirname(__file__), 'version.json'), "wb") as code:
        code.write(f.content)
    with open(os.path.join(os.path.dirname(__file__), 'version.json'), "rb") as file:
        version = json.load(file) 
    if version['hash'] == local_version:
        await bot.send(ev, f'已是最新版本，无需更新')
    else:
        db_request = requests.get(version['url'])
        with open(os.path.join(os.path.dirname(__file__), 'data.db'), "wb") as db:
            db.write(db_request.content)
        result = version['content']
        await bot.send(ev, f'{result}')