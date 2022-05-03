import os
import re
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from datetime import datetime
from Fetch import fetch
from data import *

UnavailableChara = {
    1000,   # 未知角色
    1067,   # 穗希
    1069,   # 霸瞳
    1072,   # 可萝爹
    1073,   # 拉基拉基
    1102,   # 泳装大眼
    1908,
    4031,
    9000,
    9401,
}

start = datetime.now()

opt = Options()
opt.add_argument('--headless')
opt.add_argument(f"--disk-cache-dir={os.path.join(os.path.dirname(__file__), 'cache')}")#此处更改为你想存放缓存的地址
opt.add_argument('–disk-cache-size=134217728')#缓存最大128Mb
opt.add_argument('--disable-javascript')
opt.add_argument('--disable-images')
opt.add_argument('--disable-plugins')
opt.add_argument('--ignore-certificate-errors') #忽略证书错误
opt.add_argument('--ignore-ssl-errors') #忽略证书错误
driver = webdriver.Chrome(service=Service(ChromeDriverManager(url="https://cdn.npmmirror.com/binaries/chromedriver", latest_release_url="https://cdn.npmmirror.com/binaries/chromedriver/LATEST_RELEASE").install()), options=opt)

try:
    driver.get('https://pcredivewiki.tw/Character')
    anm_boxes = driver.find_elements_by_class_name('anm-float')
    chara_list = []
    for anm in anm_boxes:
        anm_img = anm.find_elements_by_class_name('img-fluid')[0]
        src = anm_img.get_attribute('src')
        matches = re.match(r'.*icon_unit_(\d+)\.', src)
        idx = int(matches.group(1)[0:4])
        name = anm.find_elements_by_class_name('card-footer')[0].text
        chara_list.append(dict({
            'idx': idx,
            'name': name
        }))

    for chara in chara_list:
        idx = chara.get('idx')
        name = chara.get('name')
        if idx > 0 and idx not in UnavailableChara:# 批量更新，自行替换为更新范围
        # if idx == 1156 and idx not in UnavailableChara:# 单条更新，此处数字更改为想要爬取的角色id
            driver.get(f'https://pcredivewiki.tw/Character/Detail/{name}')

            print(driver.title)

            info = fetch(driver)

            Info.replace(
                id=idx,
                name=info['info']['name'],
                guild = info['info']['guild'],
                birthday = info['info']['birthday'],
                age = info['info']['age'],
                height = info['info']['height'],
                weight = info['info']['weight'],
                blood_type = info['info']['blood_type'],
                race = info['info']['race'],
                hobby = info['info']['hobby'],
                cv = info['info']['cv'],
                introduce = info['info']['introduce'],
                start = ','.join(info['pattern']['start']),
                loop = ','.join(info['pattern']['loop']),
            ).execute()

            for skill in info['skill']:
                Skill.replace(
                    id=idx,
                    name = skill['skill_name'],
                    type = skill['skill_type'],
                    description = skill['description'],
                    num = skill['skill_num'],
                    effect = skill['skill_effect'],
                ).execute()
            
            Kizuna.delete().where(Kizuna.id == idx).execute()
            for i in info['kizuna']:
                for j in info['kizuna'][i]:
                    Kizuna.replace(
                        id=idx,
                        name = i,
                        episode = j,
                        effect = info['kizuna'][i][j],
                    ).execute()

            if('uniquei' in info.keys()):
                Uniquei.delete().where(Uniquei.id == idx).execute()
                Uniquei.replace(
                    id = idx,
                    name = info['uniquei']['name'],
                    num = info['uniquei']['weapon_num'],
                    description = info['uniquei']['description'],
                ).execute()

                for prop in info['uniquei']['props']:
                    Props.replace(
                        id = idx,
                        property = prop['property'],
                        base_value = prop['base_value'],
                        max_value = prop['max_value'],
                    ).execute()

            time = datetime.now()
            t = time - start
            print(f'用时：{t}，已更新编号{idx}{name}角色数据')
        # else:
            # print('跳过npc角色')
except Exception as ex:
    print(ex)
    print('更新出错')
finally:
    driver.quit()