'''公主连接Re:dive的游戏数据'''


'''角色名称

遵照格式： id: [台服官译简体, 日文原名, 英文名(罗马音), B服官译, 常见别称, 带错别字的别称等] （<-依此顺序）
若暂无台服官译则用日文原名占位，台日用全角括号，英文用半角括号
'''
CHARA_NAME = {
    1000: ["未知角色", "未知キャラ", "Unknown"],
    1001: ["日和", "ヒヨリ", "Hiyori", "日和莉", "猫拳", "🐱👊"],
    1002: ["优衣", "ユイ", "Yui", "种田", "普田", "由衣", "结衣", "ue", "↗↘↗↘"],
    1003: ["怜", "レイ", "Rei", "剑圣", "普怜", "伶", "早见"],
    1004: ["禊", "ミソギ", "Misogi", "未奏希", "炸弹", "炸弹人", "💣"],
    1005: ["茉莉", "マツリ", "Matsuri", "跳跳虎", "老虎", "虎", "🐅"],
    1006: ["茜里", "アカリ", "Akari", "妹法", "妹妹法"],
    1007: ["宫子", "ミヤコ", "Miyako", "布丁", "布", "🍮"],
    1008: ["雪", "ユキ", "Yuki", "小雪", "镜子", "镜法", "伪娘", "男孩子", "男孩纸", "雪哥"],
    1009: ["杏奈", "アンナ", "Anna", "中二", "煤气罐"],
    1010: ["真步", "マホ", "Maho", "狐狸", "真扎", "咕噜灵波", "真布", "🦊"],
    1011: ["璃乃", "リノ", "Rino", "妹弓"],
    1012: ["初音", "ハツネ", "Hatsune", "hego", "星法", "星星法", "⭐法", "睡法"],
    1013: ["七七香", "ナナカ", "Nanaka", "娜娜卡", "77k", "77香"],
    1014: ["霞", "カスミ", "Kasumi", "香澄", "侦探", "杜宾犬", "驴", "驴子", "🔍"],
    1015: ["美里", "ミサト", "Misato", "圣母"],
    1016: ["铃奈", "スズナ", "Suzuna", "暴击弓", "暴弓", "爆击弓", "爆弓", "政委"],
    1017: ["香织", "カオリ", "Kaori", "琉球犬", "狗子", "狗", "狗拳", "🐶", "🐕", "🐶👊🏻", "🐶👊"],
    1018: ["伊绪", "イオ", "Io", "老师", "魅魔"],

    1020: ["美美", "ミミ", "Mimi", "兔子", "兔兔", "兔剑", "萝卜霸断剑", "人参霸断剑", "天兔霸断剑", "🐇", "🐰"],
    1021: ["胡桃", "クルミ", "Kurumi", "铃铛", "🔔"],
    1022: ["依里", "ヨリ", "Yori", "姐法", "姐姐法"],
    1023: ["绫音", "アヤネ", "Ayane", "熊锤", "🐻🔨", "🐻"],

    1025: ["铃莓", "スズメ", "Suzume", "女仆", "妹抖"],
    1026: ["铃", "リン", "Rin", "松鼠", "🐿", "🐿️"],
    1027: ["惠理子", "エリコ", "Eriko", "病娇"],
    1028: ["咲恋", "サレン", "Saren", "充电宝", "青梅竹马", "幼驯染", "院长", "园长", "🔋", "普电"],
    1029: ["望", "ノゾミ", "Nozomi", "偶像", "小望", "🎤"],
    1030: ["妮诺", "ニノン", "Ninon", "妮侬", "扇子"],
    1031: ["忍", "シノブ", "Shinobu", "普忍", "鬼父", "💀"],
    1032: ["秋乃", "アキノ", "Akino", "哈哈剑"],
    1033: ["真阳", "マヒル", "Mahiru", "奶牛", "🐄", "🐮", "真☀"],
    1034: ["优花梨", "ユカリ", "Yukari", "由加莉", "黄骑", "酒鬼", "奶骑", "圣骑", "🍺", "🍺👻"],

    1036: ["镜华", "キョウカ", "Kyouka", "小仓唯", "xcw", "小苍唯", "8岁", "八岁", "喷水萝", "八岁喷水萝", "8岁喷水萝"],
    1037: ["智", "トモ", "Tomo", "卜毛"],
    1038: ["栞", "シオリ", "Shiori", "tp弓", "小栞", "白虎弓", "白虎妹"],

    1040: ["碧", "アオイ", "Aoi", "香菜", "香菜弓", "绿毛弓", "毒弓", "绿帽弓", "绿帽"],

    1042: ["千歌", "チカ", "Chika", "绿毛奶"],
    1043: ["真琴", "マコト", "Makoto", "狼", "🐺", "月月", "朋", "狼姐"],
    1044: ["伊莉亚", "イリヤ", "Iriya", "伊利亚", "伊莉雅", "伊利雅", "yly", "吸血鬼", "那个女人"],
    1045: ["空花", "クウカ", "Kuuka", "抖m", "抖"],
    1046: ["珠希", "タマキ", "Tamaki", "猫剑", "🐱剑", "🐱🗡️"],
    1047: ["纯", "ジュン", "Jun", "黑骑", "saber"],
    1048: ["美冬", "ミフユ", "Mifuyu", "子龙", "赵子龙"],
    1049: ["静流", "シズル", "Shizuru", "姐姐"],
    1050: ["美咲", "ミサキ", "Misaki", "大眼", "👀", "👁️", "👁"],
    1051: ["深月", "ミツキ", "Mitsuki", "眼罩", "抖s", "医生"],
    1052: ["莉玛", "リマ", "Rima", "Lima", "草泥马", "羊驼", "🦙", "🐐"],
    1053: ["莫妮卡", "モニカ", "Monika", "毛二力"],
    1054: ["纺希", "ツムギ", "Tsumugi", "裁缝", "蜘蛛侠", "🕷️", "🕸️"],
    1055: ["步未", "アユミ", "Ayumi", "步美", "路人", "路人妹"],
    1056: ["流夏", "ルカ", "Ruka", "大姐", "大姐头", "儿力", "luka", "刘夏"],
    1057: ["吉塔", "ジータ", "Jiita", "姬塔", "团长", "吉他", "🎸", "骑空士", "qks"],
    1058: ["贪吃佩可", "ペコリーヌ", "Pecoriinu", "佩可莉姆", "吃货", "佩可", "公主", "饭团", "🍙"],
    1059: ["可可萝", "コッコロ", "Kokkoro", "可可罗", "妈", "普白"],
    1060: ["凯留", "キャル", "Kyaru", "凯露", "百地希留耶", "希留耶", "Kiruya", "黑猫", "臭鼬", "普黑", "接头霸王", "街头霸王"],
    1061: ["矛依未", "ムイミ", "Muimi", "诺维姆", "Noemu", "夏娜", "511", "无意义", "天楼霸断剑", "姆咪", "母咪"],

    1063: ["亚里莎", "アリサ", "Arisa", "鸭梨瞎", "瞎子", "亚里沙", "鸭梨傻", "亚丽莎", "亚莉莎", "瞎子弓", "🍐🦐", "yls"],
    1064: ["雪菲", "シェフィ", "冰狼"],
    1065: ["嘉夜", "カヤ", "Kaya", "憨憨龙", "龙拳", "🐲👊🏻", "🐉👊🏻", "接龙笨比", "鬼道嘉夜"],
    1066: ["祈梨", "イノリ", "Inori", "梨老八", "李老八", "龙锤", "🐲🔨"],
    1067: ["穗希", "ホマレ", "Homare"],
    1068: ["拉比林斯达", "ラビリスタ", "Rabirisuta", "迷宫女王", "模索路晶", "模索路", "晶"],
    1069: ["真那", "マナ", "Mana", "霸瞳皇帝", "千里真那", "千里", "霸瞳", "霸铜"],
    1070: ["似似花", "ネネカ", "Neneka", "变貌大妃", "现士实似似花", "現士実似々花", "現士実", "现士实", "nnk", "448", "捏捏卡", "变貌", "大妃"],
    1071: ["克莉丝提娜", "クリスティーナ", "Kurisutiina", "誓约女君", "克莉丝提娜·摩根", "Christina", "Cristina", "克总", "女帝", "克", "摩根"],
    1072: ["可萝爹", "長老", "Chourou", "岳父", "爷爷"],
    1073: ["拉基拉基", "ラジニカーント", "Rajinigaanto", "跳跃王", "Rajiraji", "Lajilaji", "垃圾垃圾", "教授"],

    1075: ["贪吃佩可(夏日)", "ペコリーヌ(サマー)", "Pekoriinu(Summer)", "佩可莉姆(夏日)", "水吃", "水饭", "水吃货", "水佩可", "水公主", "水饭团", "水🍙", "泳吃", "泳饭", "泳吃货", "泳佩可", "泳公主", "泳饭团", "泳🍙", "泳装吃货", "泳装公主", "泳装饭团", "泳装🍙", "佩可(夏日)", "🥡", "👙🍙", "泼妇"],
    1076: ["可可萝(夏日)", "コッコロ(サマー)", "Kokkoro(Summer)", "水白", "水妈", "水可", "水可可", "水可可萝", "水可可罗", "泳装妈", "泳装可可萝", "泳装可可罗"],
    1077: ["铃莓(夏日)", "スズメ(サマー)", "Suzume(Summer)", "水女仆", "水妹抖"],
    1078: ["凯留(夏日)", "キャル(サマー)", "Kyaru(Summer)", "凯露(夏日)", "水黑", "水黑猫", "水臭鼬", "泳装黑猫", "泳装臭鼬", "潶", "溴", "💧黑"],
    1079: ["珠希(夏日)", "タマキ(サマー)", "Tamaki(Summer)", "水猫剑", "水猫", "渵", "💧🐱🗡️", "水🐱🗡️"],
    1080: ["美冬(夏日)", "ミフユ(サマー)", "Mifuyu(Summer)", "水子龙", "水美冬"],
    1081: ["忍(万圣节)", "シノブ(ハロウィン)", "Shinobu(Halloween)", "万圣忍", "瓜忍", "🎃忍", "🎃💀"],
    1082: ["宫子(万圣节)", "ミヤコ(ハロウィン)", "Miyako(Halloween)", "万圣宫子", "万圣布丁", "狼丁", "狼布丁", "万圣🍮", "🐺🍮", "🎃🍮", "👻🍮"],
    1083: ["美咲(万圣节)", "ミサキ(ハロウィン)", "Misaki(Halloween)", "万圣美咲", "万圣大眼", "瓜眼", "🎃眼", "🎃👀", "🎃👁️", "🎃👁"],
    1084: ["千歌(圣诞节)", "チカ(クリスマス)", "Chika(Xmas)", "圣诞千歌", "圣千", "蛋鸽", "🎄💰🎶", "🎄千🎶", "🎄1000🎶"],
    1085: ["胡桃(圣诞节)", "クルミ(クリスマス)", "Kurumi(Xmas)", "圣诞胡桃", "圣诞铃铛"],
    1086: ["绫音(圣诞节)", "アヤネ(クリスマス)", "Ayane(Xmas)", "圣诞熊锤", "蛋锤", "圣锤", "🎄🐻🔨", "🎄🐻"],
    1087: ["日和(新年)", "ヒヨリ(ニューイヤー)", "Hiyori(NewYear)", "新年日和", "春猫", "👘🐱"],
    1088: ["优衣(新年)", "ユイ(ニューイヤー)", "Yui(NewYear)", "新年优衣", "春田", "新年由衣"],
    1089: ["怜(新年)", "レイ(ニューイヤー)", "Rei(NewYear)", "春剑", "春怜", "春伶", "新春剑圣", "新年怜", "新年剑圣"],
    1090: ["惠理子(情人节)", "エリコ(バレンタイン)", "Eriko(Valentine)", "情人节病娇", "恋病", "情病", "恋病娇", "情病娇", "青椒"],
    1091: ["静流(情人节)", "シズル(バレンタイン)", "Shizuru(Valentine)", "情人节静流", "情姐", "情人节姐姐"],
    1092: ["安", "アン", "An", "胖安", "55kg"],
    1093: ["露", "ルゥ", "Ruu", "逃课女王"],
    1094: ["古蕾娅", "グレア", "Gurea", "龙姬", "古雷娅", "古蕾亚", "古雷亚", "古蕾雅", "🐲🐔", "🐉🐔"],
    1095: ["空花(大江户)", "クウカ(オーエド)", "Kuuka(Ooedo)", "江户空花", "江户抖m", "江m", "花m", "江花"],
    1096: ["妮诺(大江户)", "ニノン(オーエド)", "Ninon(Ooedo)", "江户扇子", "忍扇"],
    1097: ["雷姆", "レム", "Remu", "蕾姆"],
    1098: ["拉姆", "ラム", "Ramu"],
    1099: ["爱蜜莉雅", "エミリア", "Emiria", "艾米莉亚", "emt"],
    1100: ["铃奈(夏日)", "スズナ(サマー)", "Suzuna(Summer)", "瀑击弓", "水爆", "水爆弓", "水暴", "瀑", "水暴弓", "瀑弓", "泳装暴弓", "泳装爆弓"],
    1101: ["伊绪(夏日)", "イオ(サマー)", "Io(Summer)", "水魅魔", "水老师", "泳装魅魔", "泳装老师"],
    1102: ["美咲(夏日)", "ミサキ(サマー)", "Misaki(Summer)", "水大眼", "泳装大眼"],
    1103: ["咲恋(夏日)", "サレン(サマー)", "Saren(Summer)", "水电", "泳装充电宝", "泳装咲恋", "水着咲恋", "水电站", "水电宝", "水充", "👙🔋"],
    1104: ["真琴(夏日)", "マコト(サマー)", "Makoto(Summer)", "水狼", "浪", "水🐺", "泳狼", "泳月", "泳月月", "泳朋", "水月", "水月月", "水朋", "👙🐺"],
    1105: ["香织(夏日)", "カオリ(サマー)", "Kaori(Summer)", "水狗", "泃", "水🐶", "水🐕", "泳狗"],
    1106: ["真步(夏日)", "マホ(サマー)", "Maho(Summer)", "水狐狸", "水狐", "水壶", "水真步", "水maho", "氵🦊", "水🦊", "💧🦊"],
    1107: ["碧(插班生)", "アオイ(編入生)", "Aoi(Hennyuusei)", "生菜", "插班碧"],
    1108: ["克萝依", "クロエ", "Kuroe", "华哥", "黑江", "黑江花子", "花子"],
    1109: ["琪爱儿", "チエル", "Chieru", "切露", "茄露", "茄噜", "切噜"],
    1110: ["优妮", "ユニ", "Yuni", "真行寺由仁", "由仁", "优尼", "u2", "优妮辈先", "辈先", "书记", "uni", "先辈", "仙贝", "油腻", "优妮先辈", "学姐", "18岁黑丝学姐"],
    1111: ["镜华(万圣节)", "キョウカ(ハロウィン)", "Kyouka(Halloween)", "万圣镜华", "万圣小仓唯", "万圣xcw", "猫仓唯", "黑猫仓唯", "mcw", "猫唯", "猫仓", "喵唯"],
    1112: ["禊(万圣节)", "ミソギ(ハロウィン)", "Misogi(Halloween)", "万圣禊", "万圣炸弹人", "瓜炸弹人", "万圣炸弹", "万圣炸", "瓜炸", "南瓜炸", "🎃💣"],
    1113: ["美美(万圣节)", "ミミ(ハロウィン)", "Mimi(Halloween)", "万圣兔", "万圣兔子", "万圣兔兔", "绷带兔", "绷带兔子", "万圣美美", "绷带美美", "万圣🐰", "绷带🐰", "🎃🐰", "万圣🐇", "绷带🐇", "🎃🐇"],
    1114: ["露娜", "ルナ", "Runa", "Luna", "露仓唯", "露cw"],
    1115: ["克莉丝提娜(圣诞节)", "クリスティーナ(クリスマス)", "Kurisutiina(Xmas)", "Christina(Xmas)", "Cristina(Xmas)", "圣诞克", "圣诞克总", "圣诞女帝", "蛋克", "圣克", "必胜客"],
    1116: ["望(圣诞节)", "ノゾミ(クリスマス)", "Nozomi(Xmas)", "圣诞望", "圣诞偶像", "蛋偶像", "蛋望"],
    1117: ["伊莉亚(圣诞节)", "イリヤ(クリスマス)", "Iriya(Xmas)", "圣诞伊莉亚", "圣诞伊利亚", "圣诞伊莉雅", "圣诞伊利雅", "圣诞yly", "圣诞吸血鬼", "圣伊", "圣yly"],
    1118: ["贪吃佩可(新年)", "ペコリーヌ(ニューイヤー)", "Pecoriinu(NewYear)", "新年吃货", "新年佩可", "春吃", "新春吃货", "新春佩可", "年货"],
    1119: ["可可萝(新年)", "コッコロ(ニューイヤー)", "Kokkoro(NewYear)", "春可可", "春白", "新年妈", "春妈"],
    1120: ["凯留(新年)", "キャル(ニューイヤー)", "Kyaru(NewYear)", "凯露(新年)", "春凯留", "春黑猫", "春黑", "春臭鼬", "新年凯留", "新年黑猫", "新年臭鼬", "唯一神"],
    1121: ["铃莓(新年)", "スズメ(ニューイヤー)", "Suzume(NewYear)", "春铃莓", "春女仆", "春妹抖", "新年铃莓", "新年女仆", "新年妹抖"],
    1122: ["霞(魔法少女)", "カスミ(マジカル)", "Kasumi(MagiGirl)", "魔法少女霞", "魔法侦探", "魔法杜宾犬", "魔法驴", "魔法驴子", "魔驴", "魔法霞", "魔法少驴"],
    1123: ["栞(魔法少女)", "シオリ(マジカル)", "Shiori(MagiGirl)", "魔法少女栞", "魔法tp弓", "魔法小栞", "魔法白虎弓", "魔法白虎妹", "魔法白虎", "魔栞"],
    1124: ["卯月(NGs)", "ウヅキ(デレマス)", "Udsuki(DEREM@S)", "卯月", "卵用", "Udsuki(DEREMAS)", "岛村卯月"],
    1125: ["凛(NGs)", "リン(デレマス)", "Rin(DEREM@S)", "凛", "Rin(DEREMAS)", "涩谷凛", "西部凛"],
    1126: ["未央(NGs)", "ミオ(デレマス)", "Mio(DEREM@S)", "未央", "Mio(DEREMAS)", "本田未央"],
    1127: ["铃(游侠)", "リン(レンジャー)", "Rin(Ranger)", "骑兵松鼠", "游侠松鼠", "游骑兵松鼠", "护林员松鼠", "护林松鼠", "游侠🐿️", "武松"],
    1128: ["真阳(游侠)", "マヒル(レンジャー)", "Mahiru(Ranger)", "骑兵奶牛", "游侠奶牛", "游骑兵奶牛", "护林员奶牛", "护林奶牛", "游侠🐄", "游侠🐮", "牛叉"],
    1129: ["璃乃(奇幻)", "リノ(ワンダー)", "Rino(Wonder)", "璃乃(奇境)", "璃乃(仙境)", "爽弓", "爱丽丝弓", "爱弓", "兔弓", "奇境妹弓", "奇幻妹弓", "奇幻璃乃", "仙境妹弓", "白丝妹弓", "爱丽丝妹弓"],
    1130: ["步未(奇幻)", "アユミ(ワンダー)", "Ayumi(Wonder)", "步未(奇境)", "步未(仙境)", "路人兔", "兔人妹", "爱丽丝路人", "奇境路人", "奇幻路人", "奇幻步未", "仙境路人", "爱丽丝路人妹"],
    1131: ["流夏(夏日)", "ルカ(サマー)", "Ruka(Summer)", "泳装流夏", "水流夏", "泳装刘夏", "水刘夏", "泳装大姐", "泳装大姐头", "水大姐", "水大姐头", "水儿力", "泳装儿力", "水流"],
    1132: ["杏奈(夏日)", "アンナ(サマー)", "Anna(Summer)", "泳装中二", "泳装煤气罐", "水中二", "水煤气罐", "冲", "冲二"],
    1133: ["七七香(夏日)", "ナナカ(サマー)", "Nanaka(Summer)", "泳装娜娜卡", "泳装77k", "泳装77香", "水娜娜卡", "水77k", "水77香", "水七七香", "泳装七七香", "水七七"],
    1134: ["初音(夏日)", "ハツネ(サマー)", "Hatsune(Summer)", "水星", "海星", "水hego", "水星法", "泳装星法", "水⭐法", "水睡法", "湦", "水初音", "泳装初音"],
    1135: ["美里(夏日)", "ミサト(サマー)", "Misato(Summer)", "水母", "泳装圣母", "水圣母"],
    1136: ["纯(夏日)", "ジュン(サマー)", "Jun(Summer)", "泳装黑骑", "水黑骑", "泳装纯", "水纯", "小次郎"],
    1137: ["茜里(天使)", "アカリ(エンジェル)", "Akari(Angel)", "天使妹法", "天使茜里", "丘比特妹法"],
    1138: ["依里(天使)", "ヨリ(エンジェル)", "Yori(Angel)", "天使姐法", "天使依里", "丘比特姐法"],
    1139: ["纺希(万圣节)", "ツムギ(ハロウィン)", "Tsumugi(Halloween)", "万圣裁缝", "万圣蜘蛛侠", "🎃🕷️", "🎃🕸️", "万裁", "瓜裁", "鬼裁", "鬼才"],
    1140: ["怜(万圣节)", "レイ(ハロウィン)", "Rei(Halloween)", "万圣剑圣", "万剑", "瓜剑", "瓜怜", "万圣怜", "鬼剑"],
    1141: ["茉莉(万圣节)", "マツリ(ハロウィン)", "Matsuri(Halloween)", "万圣跳跳虎", "万圣老虎", "瓜虎", "🎃🐅"],
    1142: ["莫妮卡(魔法少女)", "モニカ(マジカル)", "Monika(MagiGirl)", "魔法少女毛二力", "魔法少女莫妮卡", "魔法毛二力", "魔二力"],
    1143: ["智(魔法少女)", "トモ(マジカル)", "Tomo(MagiGirl)", "魔法少女卜毛", "魔法少女智", "魔法智", "魔智", "琪露诺", "阿库娅", "⑨"],
    1144: ["秋乃(圣诞节)", "アキノ(クリスマス)", "Akino(Xmas)", "圣诞哈哈剑", "圣哈"],
    1145: ["咲恋(圣诞节)", "サレン(クリスマス)", "Saren(Xmas)", "圣诞充电宝", "圣诞咲恋", "圣冲", "圣充"],
    1146: ["优花梨(圣诞节)", "ユカリ(クリスマス)", "Yukari(Xmas)", "圣诞由加莉", "圣诞黄骑", "圣诞酒鬼", "圣诞奶骑"],
    1147: ["矛依未(新年)", "ムイミ(ニューイヤー)", "Muimi(NewYear)", "新春诺维姆", "新春夏娜", "新春511", "新年511", "春511", "新511"],


    1150: ["似似花(新年)", "ネネカ(ニューイヤー)", "Neneka(NewYear)", "新春nnk", "新年nnk", "新春似似花", "春似似花", "新年似似花", "春nnk", "春花", "新花"],
    1155: ["可可萝(礼服)", "コッコロ(儀装束)", "Kokkoro(FullDress)", "礼服妈", "礼服可可萝", "礼白", "礼妈"],
    1156: ["优衣(礼服)", "ユイ(儀装束)", "Yui(FullDress)", "礼服ue", "礼衣", "礼服优衣"],
    1157: ["霞(夏日)", "カスミ(サマー)", "Kasumi(Summer)", "水香澄", "水侦探", "水驴"],
    1158: ["莉玛(灰姑娘)", "リマ(シンデレラ)", "Rima(Cinderella)", "灰姑娘草泥马", "灰姑娘羊驼", "美羊羊"],
    1159: ["真琴(灰姑娘)", "マコト(シンデレラ)", "Makoto(Cinderella)", "灰狼", "大灰狼", "灰太狼"],
    1160: ["真步(灰姑娘)", "マホ(シンデレラ)", "Maho(Cinderella)", "灰狐狸", "灰狐", "灰姑娘狐狸", "灰姑娘真步"],

    1162: ["克萝依(学园祭)", "クロエ(聖学祭)", "学园祭华哥", "学园祭黑江", "学园祭花子"],
    1163: ["琪爱儿(学园祭)", "チエル(聖学祭)", "学园祭切露", "圣学祭切噜", "学园祭切噜"],

    1165: ["祈梨(时间旅行)", "イノリ(タイムトラベル)", "Inori(time travel)"],

    # =================================== #
    1701: ["环奈", "カンナ", "Kanna", "桥本环奈", "红二力", "毛大力", "毛小力", "毛六力", "可大萝", "大可萝", "缝合怪"],
    1702: ["环奈(振袖)", "カンナ(ニューイヤー)", "Kanna(NewYear)", "新春桥本环奈", "新春环奈", "春环", "二环", "环奈振袖", "振袖环奈", "春奈"],








    # =================================== #
    1801: ["日和(公主)", "ヒヨリ(プリンセス)", "Hiyori(Princess)", "公主日和莉", "公主猫拳", "公主🐱👊", "公主日和", "火猫"],
    1802: ["优衣(公主)", "ユイ(プリンセス)", "Yui(Princess)", "公主优衣", "公主yui", "公主种田", "公主田", "公主ue", "掉毛优衣", "掉毛yui", "掉毛ue", "掉毛", "飞翼优衣", "飞翼ue", "飞翼", "飞翼高达", "飞田", "毛衣"],

    1804: ["贪吃佩可(公主)", "ペコリーヌ(プリンセス)", "Pekoriinu(Princess)", "公主吃", "公主饭", "公主吃货", "公主佩可", "公主饭团", "公主🍙", "命运高达", "高达", "命运公主", "高达公主", "命吃", "春哥高达", "🤖🍙", "🤖"],
    1805: ["可可萝(公主)", "コッコロ（プリンセス）", "Kokkoro(Princess)", "公主妈", "月光妈", "蝶妈", "蝴蝶妈", "月光蝶妈", "公主可", "公主可萝", "公主可可萝", "月光可", "月光可萝", "月光可可萝", "蝶可", "蝶可萝", "蝶可可萝"],
    1806: ["凯留(公主)", "キャル(プリンセス)", "Kyaru(Princess)", "凯露(公主)", "公主猫", "公主猫猫", "公主猫猫头", "公主黑猫", "公主臭鼬"],


    # =================================== #
    1900: ["爱梅斯", "アメス", "Amesu", "菲欧", "フィオ", "Fio"],






    1907: ["大古", "タイゴ", "Taigo", "大吾", "鬼道大吾"],
    1908: ["花凛", "カリン", "Karin", "绿毛恶魔"],
    1909: ["涅比亚", "ネビア", "Nevia", "Nebia"],
    1910: ["真崎", "マサキ", "Masaki"],
    1911: ["米涅尔β", "ミネルβ", "MineruBeta", "米涅尔", "ミネル", "Mineru"],


    1914: ["豪绅", "ゴウシン", "Goushin"],
    1915: ["克里吉塔", "クレジック", "Kurejikku"],
    1916: ["基洛", "キイロ", "Kiiro"],
    1917: ["善", "ゼーン", "Seen"],
    1918: ["兰法", "ランファ", "Ranfa"],
    1919: ["阿佐尔德", "アンゾールド", "Anzoorudo"],
    1920: ["美空", "ミソラ", "Misora"],









    # =================================== #
    4031: ["骷髅", "髑髏", "Dokuro", "骷髅老爹", "老爹"],
 
    9000: ["祐树", "ユウキ", "Yuuki", "骑士", "骑士君"],
}

CHARA_PROFILE = {
    1001: {"名字": "日和", "公会": "破晓之星", "生日": "8月27日", "年龄": "16", "身高": "155cm", "体重": "44kg", "血型": "A", "种族": "兽人族", "喜好": "助人、打气加油", "声优": "东山奈央", "口头禅和座右铭": "放不下心"},
    1002: {"名字": "优衣", "公会": "破晓之星", "生日": "4月5日", "年龄": "17", "身高": "158cm", "体重": "47kg", "血型": "O", "种族": "人族", "喜好": "料理、观察人类", "声优": "种田梨沙", "特技": "全体治愈", "儿时玩伴": "真琴"},
    1003: {"名字": "怜", "公会": "破晓之星", "生日": "1月12日", "年龄": "18", "身高": "163cm", "体重": "46kg", "血型": "B", "种族": "魔族", "喜好": "读书、骑马、茶", "声优": "早见沙织", "隐藏特技": "骑马"},
    1004: {"名字": "禊", "公会": "小小甜心", "生日": "8月10日", "年龄": "9", "身高": "128cm", "体重": "27kg", "血型": "O", "种族": "人族", "喜好": "恶作剧、探险", "声优": "诸星堇", "无人能出其右的技巧": "捣蛋鬼"},
    1005: {"名字": "茉莉", "公会": "王宫骑士团", "生日": "11月25日", "年龄": "12", "身高": "146cm", "体重": "40kg", "血型": "O", "种族": "兽人族", "喜好": "英雄扮演游戏", "声优": "下田麻美", "称号": "见习英雄"},
    1006: {"名字": "茜里", "公会": "恶魔伪王国军", "生日": "11月22日", "年龄": "13", "身高": "150cm", "体重": "42kg", "血型": "O", "种族": "魔族", "喜好": "萨克斯风", "声优": "浅仓杏美", "称号": "小恶魔", "姊姊": "依里"},
    1007: {"名字": "宫子", "公会": "恶魔伪王国军", "生日": "1月23日", "年龄": "14", "身高": "130cm", "体重": "32kg", "血型": "B", "种族": "魔族", "喜好": "吃布丁", "声优": "雨宫天"},
    1008: {"名字": "雪", "公会": "纯白之翼兰德索尔分部", "生日": "10月10日", "年龄": "14", "身高": "150cm", "体重": "40kg", "血型": "AB", "种族": "精灵族", "喜好": "欣赏镜中的自己", "声优": "大空直美", "罪过": "美丽的自己", "癖好": "自恋"},
    1009: {"名字": "杏奈", "公会": "暮光流星群", "生日": "7月5日", "年龄": "17", "身高": "159cm", "体重": "45kg", "血型": "A", "种族": "魔族", "喜好": "写小说", "声优": "高野麻美", "称号": "疾风之冥姬"},
    1010: {"名字": "真步", "公会": "自卫团", "生日": "9月22日", "年龄": "16", "身高": "155cm", "体重": "42kg", "血型": "O", "种族": "兽人族", "喜好": "幻想、收集玩偶", "声优": "内田真礼", "身份": "某谜之国度的公主"},
    1011: {"名字": "璃乃", "公会": "拉比林斯", "生日": "8月25日", "年龄": "15", "身高": "156cm", "体重": "44kg", "血型": "A", "种族": "人族", "喜好": "裁缝", "声优": "阿澄佳奈", "自称": "妹妹", "称号": "小笨蛋"},
    1012: {"名字": "初音", "公会": "森林守卫", "生日": "12月24日", "年龄": "17", "身高": "156cm", "体重": "46kg", "血型": "A", "种族": "精灵族", "喜好": "和妹妹一起玩、回笼觉、午睡、早睡", "声优": "大桥彩香", "称号": "超能力少女", "妹妹": "小栞"},
    1013: {"名字": "七七香", "公会": "暮光流星群", "生日": "8月21日", "年龄": "18", "身高": "166cm", "体重": "55kg", "血型": "O", "种族": "魔族", "喜好": "读书、魔法", "声优": "佳村遥", "称号": "魔法少女"},
    1014: {"名字": "霞", "公会": "自卫团", "生日": "11月3日", "年龄": "15", "身高": "152cm", "体重": "41kg", "血型": "AB", "种族": "兽人族", "喜好": "读书、推理", "声优": "水濑祈", "称号": "名侦探"},
    1015: {"名字": "美里", "公会": "森林守卫", "生日": "9月5日", "年龄": "21", "身高": "165cm", "体重": "54kg", "血型": "O", "种族": "精灵族", "喜好": "制作绘本", "声优": "国府田麻理子", "工作": "幼稚园的老师"},
    1016: {"名字": "铃奈", "公会": "月光学院", "生日": "4月10日", "年龄": "18", "身高": "167cm", "体重": "48kg", "血型": "O", "种族": "魔族", "喜好": "时尚", "声优": "上坂堇", "工作": "超级名模", "称号": "辣妹"},
    1017: {"名字": "香织", "公会": "自卫团", "生日": "7月7日", "年龄": "19", "身高": "158cm", "体重": "53kg", "血型": "A", "种族": "兽人族", "喜好": "跳舞、空手道", "声优": "高森奈津美", "绝技": "琉球空手道", "问候的方式": "嗨——呵"},
    1018: {"名字": "伊绪", "公会": "月光学院", "生日": "8月14日", "年龄": "23", "身高": "162cm", "体重": "52kg", "血型": "B", "种族": "魔族", "喜好": "看恋爱小说、恋爱剧、恋爱漫画", "声优": "伊藤静", "工作": "新来的老师"},
    1020: {"名字": "美美", "公会": "小小甜心", "生日": "4月3日", "年龄": "10", "身高": "117cm", "体重": "21kg", "血型": "O", "种族": "兽人族", "喜好": "收集可爱的东西", "声优": "日高里菜", "最喜欢": "兔子先生"},
    1021: {"名字": "胡桃", "公会": "咲恋救济院", "生日": "6月9日", "年龄": "12", "身高": "150cm", "体重": "40kg", "血型": "B", "种族": "人族", "喜好": "看戏、扮家家酒", "声优": "植田佳奈", "称号": "知名女演员"},
    1022: {"名字": "依里", "公会": "恶魔伪王国军", "生日": "11月22日", "年龄": "13", "身高": "150cm", "体重": "40kg", "血型": "O", "种族": "魔族", "喜好": "所有游戏", "声优": "原纱友里", "妹妹": "茜里", "性格": "害羞", "称号": "天才玩家"},
    1023: {"名字": "绫音", "公会": "咲恋救济院", "生日": "5月10日", "年龄": "14", "身高": "148cm", "体重": "38kg", "血型": "B", "种族": "人族", "喜好": "能在房间里玩的游戏", "声优": "芹泽优", "伙伴": "噗吉"},
    1025: {"名字": "铃莓", "公会": "咲恋救济院", "生日": "12月12日", "年龄": "15", "身高": "154cm", "体重": "43kg", "血型": "O", "种族": "人族", "喜好": "服侍", "声优": "悠木碧", "特点": "冒冒失失"},
    1026: {"名字": "铃", "公会": "伊丽莎白牧场", "生日": "1月1日", "年龄": "17", "身高": "144cm", "体重": "42kg", "血型": "B", "种族": "兽人族", "喜好": "红豆面包", "声优": "小岩井小鸟", "性格": "懒散"},
    1027: {"名字": "惠理子", "公会": "暮光流星群", "生日": "7月30日", "年龄": "16", "身高": "154cm", "体重": "43kg", "血型": "B", "种族": "魔族", "喜好": "实验、裁缝、料理", "声优": "桥本千波", "称号": "破坏者"},
    1028: {"名字": "咲恋", "公会": "咲恋救济院", "生日": "10月4日", "年龄": "17", "身高": "156cm", "体重": "43kg", "血型": "A", "种族": "精灵族", "喜好": "经营、茶会", "声优": "堀江由衣", "称号": "妈妈"},
    1029: {"名字": "望", "公会": "慈乐之音", "生日": "1月24日", "年龄": "17", "身高": "157cm", "体重": "40kg", "血型": "B", "种族": "人族", "喜好": "看舞台剧、跳舞", "声优": "日笠阳子", "称号": "超人气偶像"},
    1030: {"名字": "妮诺", "公会": "纯白之翼兰德索尔分部", "生日": "8月31日", "年龄": "16", "身高": "163cm", "体重": "51kg", "血型": "O", "种族": "人族", "喜好": "忍术开发", "声优": "佐藤聪美", "憧憬的地方": "东国", "称号": "冒牌忍者", "爱读的书": "《武士道》"},
    1031: {"名字": "忍", "公会": "恶魔伪王国军", "生日": "12月22日", "年龄": "18", "身高": "157cm", "体重": "42kg", "血型": "AB", "种族": "魔族", "喜好": "占卜", "声优": "大坪由佳", "称号": "占卜师"},
    1032: {"名字": "秋乃", "公会": "墨丘利财团", "生日": "3月12日", "年龄": "18", "身高": "157cm", "体重": "45kg", "血型": "AB", "种族": "人族", "喜好": "慈善事业", "声优": "松嵜丽", "称号": "大小姐"},
    1033: {"名字": "真阳", "公会": "伊丽莎白牧场", "生日": "3月3日", "年龄": "20", "身高": "142cm", "体重": "35kg", "血型": "B", "种族": "人族", "喜好": "相声", "声优": "新田惠海", "工作": "牧场主人", "职业道路": "搞笑艺人之路"},
    1034: {"名字": "优花梨", "公会": "墨丘利财团", "生日": "3月16日", "年龄": "22", "身高": "164cm", "体重": "55kg", "血型": "A", "种族": "精灵族", "喜好": "随意逛街", "声优": "今井麻美", "称号": "女中酒豪"},
    1036: {"名字": "镜华", "公会": "小小甜心", "生日": "2月2日", "年龄": "8", "身高": "118cm", "体重": "21kg", "血型": "A", "种族": "精灵族", "喜好": "读书", "声优": "小仓唯", "称号": "资优生"},
    1037: {"名字": "智", "公会": "王宫骑士团", "生日": "8月11日", "年龄": "13", "身高": "149cm", "体重": "43kg", "血型": "A", "种族": "人族", "喜好": "剑术、戏弄长者", "声优": "茅原实里", "家传剑技": "御久间流", "家传剑技的奥义": "阿修罗"},
    1038: {"名字": "栞", "公会": "伊丽莎白牧场", "生日": "11月3日", "年龄": "14", "身高": "153cm", "体重": "40kg", "血型": "A", "种族": "兽人族", "喜好": "读书、散步", "声优": "小清水亚美", "姊姊": "初音"},
    1040: {"名字": "碧", "公会": "森林守卫", "生日": "6月6日", "年龄": "13", "身高": "158cm", "体重": "44kg", "血型": "AB", "种族": "精灵族", "喜好": "交朋友的想象训练", "声优": "花泽香菜", "称号": "边缘人"},
    1042: {"名字": "千歌", "公会": "慈乐之音", "生日": "6月3日", "年龄": "17", "身高": "163cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "各种乐器", "声优": "福原绫香", "工作": "唱唤师", "称号": "歌姬"},
    1043: {"名字": "真琴", "公会": "自卫团", "生日": "8月9日", "年龄": "17", "身高": "168cm", "体重": "54kg", "血型": "O", "种族": "兽人族", "喜好": "做点心", "声优": "小松未可子", "儿时玩伴": "优衣"},
    1044: {"名字": "伊莉亚", "公会": "恶魔伪王国军", "生日": "5月5日", "年龄": "？？？", "身高": "172cm", "体重": "50kg", "血型": "A", "种族": "魔族", "喜好": "征服世界", "声优": "丹下樱", "称号": "传说的吸血鬼", "工作": "统领黑夜"},
    1045: {"名字": "空花", "公会": "纯白之翼兰德索尔分部", "生日": "11月19日", "年龄": "18", "身高": "157cm", "体重": "49kg", "血型": "AB", "种族": "人族", "喜好": "阅读小说", "声优": "长妻树里", "称号": "被虐狂"},
    1046: {"名字": "珠希", "公会": "墨丘利财团", "生日": "3月1日", "年龄": "18", "身高": "158cm", "体重": "48kg", "血型": "AB", "种族": "兽人族", "喜好": "与猫咪玩耍", "声优": "沼仓爱美", "外表": "猫娘", "称号": "幻影猫"},
    1047: {"名字": "纯", "公会": "王宫骑士团", "生日": "10月25日", "年龄": "25", "身高": "171cm", "体重": "50kg", "血型": "A", "种族": "人族", "喜好": "格斗技、入浴", "声优": "川澄绫子", "职位": "团长"},
    1048: {"名字": "美冬", "公会": "墨丘利财团", "生日": "11月11日", "年龄": "20", "身高": "163cm", "体重": "49kg", "血型": "O", "种族": "人族", "喜好": "佣兵等等的打工", "声优": "田所梓", "信条": "效率至上"},
    1049: {"名字": "静流", "公会": "拉比林斯", "生日": "10月24日", "年龄": "18", "身高": "168cm", "体重": "54kg", "血型": "O", "种族": "人族", "喜好": "所有家事", "声优": "天生目仁美", "自称": "姐姐"},
    1050: {"名字": "美咲", "公会": "月光学院", "生日": "1月3日", "年龄": "11", "身高": "120cm", "体重": "22kg", "血型": "A", "种族": "魔族", "喜好": "阅读流行杂志、搜集化妆品", "声优": "久野美咲", "自称": "成熟的淑女"},
    1051: {"名字": "深月", "公会": "暮光流星群", "生日": "3月7日", "年龄": "27", "身高": "166cm", "体重": "53kg", "血型": "A", "种族": "人族", "喜好": "研究、实验", "声优": "三石琴乃", "工作": "疯狂科学家", "称号": "独眼恶魔"},
    1052: {"名字": "莉玛", "公会": "伊丽莎白牧场", "生日": "3月14日", "年龄": "18", "身高": "150cm", "体重": "100kg", "血型": "A", "种族": "兽人族", "喜好": "理毛、聊天", "声优": "德井青空", "特点": "毛茸茸"},
    1053: {"名字": "莫妮卡", "公会": "纯白之翼兰德索尔分部", "生日": "7月28日", "年龄": "18", "身高": "140cm", "体重": "33kg", "血型": "A", "种族": "人族", "喜好": "逛糖果店", "声优": "辻亚由美", "称号": "小鬼头"},
    1054: {"名字": "纺希", "公会": "慈乐之音", "生日": "9月7日", "年龄": "14", "身高": "153cm", "体重": "45kg", "血型": "AB", "种族": "人族", "喜好": "裁缝", "声优": "木户衣吹", "创办的组织": "怜大人粉丝俱乐部"},
    1055: {"名字": "步未", "公会": "纯白之翼兰德索尔分部", "生日": "4月7日", "年龄": "16", "身高": "155cm", "体重": "43kg", "血型": "O", "种族": "精灵族", "喜好": "观察", "声优": "大关英里", "称号": "跟踪狂"},
    1056: {"名字": "流夏", "公会": "暮光流星群", "生日": "7月11日", "年龄": "25", "身高": "167cm", "体重": "54kg", "血型": "B", "种族": "人族", "喜好": "钓鱼", "声优": "佐藤利奈", "称号": "大姐头"},
    1057: {"名字": "吉塔", "公会": "？？？", "生日": "3月10日", "年龄": "17", "身高": "156cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "冒险、聊天", "声优": "金元寿子", "称号": "苍空的骑空士"},
    1058: {"名字": "贪吃佩可", "公会": "美食殿堂", "生日": "3月31日", "年龄": "17", "身高": "156cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "边走边吃、料理", "声优": "M·A·O", "口头禅": "太赞了吧☆", "装备": "皇家装备", "身份": "阿斯特赖亚王家的王女"},
    1059: {"名字": "可可萝", "公会": "美食殿堂", "生日": "5月11日", "年龄": "11", "身高": "140cm", "体重": "35kg", "血型": "B", "种族": "精灵族", "喜好": "冥想、养育动植物", "声优": "伊藤美来", "职责": "向导", "工作": "巫女"},
    1060: {"名字": "凯留", "公会": "美食殿堂", "生日": "9月2日", "年龄": "14", "身高": "152cm", "体重": "39kg", "血型": "A", "种族": "兽人族", "喜好": "和猫咪玩耍", "声优": "立花理香", "性格特点": "傲娇"},
    1061: {"名字": "矛依未", "公会": "？？？", "生日": "8月11日", "年龄": "16", "身高": "148cm", "体重": "40kg", "血型": "O", "种族": "人族", "喜好": "冒险、回忆故事", "声优": "潘惠美", "真正的名字": "诺维姆"},
    1063: {"名字": "亚里莎", "公会": "？？？", "生日": "6月17日", "年龄": "15", "身高": "155cm", "体重": "42kg", "血型": "O", "种族": "精灵族", "喜好": "搜集漂亮的叶子", "声优": "优木加奈", "称号": "见习森林守卫"},
    1065: {"名字": "嘉夜", "公会": "龙族巢穴", "生日": "6月25日", "年龄": "16", "身高": "156cm", "体重": "？？？kg", "血型": "B", "种族": "龙人族", "喜好": "格斗技", "声优": "小市真琴", "称号": "笨蛋打架狂"},
    1066: {"名字": "祈梨", "公会": "龙族巢穴", "生日": "9月29日", "年龄": "13", "身高": "145cm", "体重": "？？？kg", "血型": "AB", "种族": "龙人族", "喜好": "游戏", "声优": "藤田茜", "特技": "龙之吐息", "职位": "干部"},
    1070: {"名字": "似似花", "公会": "？？？", "生日": "3月24日", "年龄": "24", "身高": "149cm", "体重": "？？？kg", "血型": "O", "种族": "精灵族", "喜好": "模仿、艺术欣赏", "声优": "井口裕香", "称号": "变貌大妃", "特技": "分身"},
    1071: {"名字": "克莉丝提娜", "公会": "王宫骑士团", "生日": "2月7日", "年龄": "27", "身高": "165cm", "体重": "？？？kg", "血型": "O", "种族": "人族", "喜好": "和强敌之间的竞争", "声优": "高桥智秋", "称号": "誓约女君", "职位": "副团长"},
    1092: {"名字": "安", "公会": "？？？", "生日": "12月1日", "年龄": "17", "身高": "156cm", "体重": "55kg", "血型": "AB", "种族": "人族", "喜好": "读书", "声优": "日笠阳子"},
    1093: {"名字": "露", "公会": "？？？", "生日": "2月4日", "年龄": "15", "身高": "144cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "吃饭、睡觉", "声优": "古山贵实子"},
    1094: {"名字": "古蕾娅", "公会": "？？？", "生日": "11月3日", "年龄": "17", "身高": "167cm", "体重": "67kg", "血型": "B", "种族": "半人半龙", "喜好": "钢琴", "声优": "福原绫香"},
    1097: {"名字": "雷姆", "公会": "？？？", "生日": "2月2日", "年龄": "17", "身高": "154cm", "体重": "？？？kg", "血型": "？？？", "种族": "鬼族", "喜好": "戏剧欣赏、诗和散文", "声优": "水濑祈"},
    1098: {"名字": "拉姆", "公会": "？？？", "生日": "2月2日", "年龄": "17", "身高": "154cm", "体重": "？？？kg", "血型": "？？？", "种族": "鬼族", "喜好": "读书", "声优": "村川梨衣"},
    1099: {"名字": "爱蜜莉雅", "公会": "？？？", "生日": "9月23日", "年龄": "114", "身高": "164cm", "体重": "？？？kg", "血型": "？？？", "种族": "半精灵族", "喜好": "帮帕克梳理毛发、念书", "声优": "高桥李依"},
    1108: {"名字": "克萝依", "公会": "圣特蕾莎女子学院（好朋友社）", "生日": "8月7日", "年龄": "17", "身高": "154cm", "体重": "42kg", "血型": "O", "种族": "精灵族", "喜好": "飞镖", "声优": "种崎敦美", "性格特点": "阴暗系", "称号": "圣德蕾女的狂人"},
    1109: {"名字": "琪爱儿", "公会": "圣特蕾莎女子学院（好朋友社）", "生日": "9月15日", "年龄": "16", "身高": "156cm", "体重": "46kg", "血型": "O", "种族": "人族", "喜好": "跳舞、卡拉OK", "声优": "佐仓绫音", "切嚕唎咧咧囉唎囉唎囉": "咧切嚕切嚕啵啪嗶", "称号": "圣德蕾女的狂人"},
    1110: {"名字": "优妮", "公会": "圣特蕾莎女子学院（好朋友社）", "生日": "2月28日", "年龄": "18", "身高": "142cm", "体重": "36kg", "血型": "O", "种族": "人族", "喜好": "读书", "声优": "小原好美", "生活习惯": "茧居族", "称号": "圣德蕾女的狂人"},
    1114: {"名字": "露娜", "公会": "？？？", "生日": "？？？", "年龄": "？？？", "身高": "142cm", "体重": "28kg", "血型": "？？？", "种族": "人族", "喜好": "找「朋友」之事", "声优": "小仓唯"},
    1124: {"名字": "卯月", "公会": "NewGeneration", "生日": "4月24日", "年龄": "17", "身高": "159cm", "体重": "45kg", "血型": "O", "种族": "人族", "喜好": "和朋友打长电话", "声优": "大桥彩香"},
    1125: {"名字": "凛", "公会": "NewGeneration", "生日": "8月10日", "年龄": "15", "身高": "165cm", "体重": "44kg", "血型": "B", "种族": "人族", "喜好": "带狗散步", "声优": "福原绫香"},
    1126: {"名字": "未央", "公会": "NewGeneration", "生日": "12月1日", "年龄": "15", "身高": "161cm", "体重": "46kg", "血型": "B", "种族": "人族", "喜好": "购物", "声优": "原纱友里"},
}
