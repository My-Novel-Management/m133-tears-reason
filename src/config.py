# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("yuri", "悠里", "白鷺,悠里", 32,(1,1), "female", "会社員", "me:わたし"),
            ('misa', '美彩', '桂木,美彩', 37,(1,1), 'female', '研究員', "me:私:k_yukio:蒔田君"),
            ("yukio", "幸男", "蒔田,幸男", 25,(1,1), "male", "助手", "me:僕"),
            ("akio", "昭雄", "入間,昭雄", 40,(1,1), "male", "会社員", "me:俺"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Aichi", "愛知県", "Japan"),
            ("Nagoya", "名古屋市", "Aichi"),
            ("Station", "駅", "Nagoya"),
            ("Subway", "地下鉄", "Nagoya"),
            ("Cinema", "映画館", "Nagoya"),# 三越映画劇場モデル
            ("Cafe", "喫茶店", "Nagoya"),
            ("Manshion", "マンション", "Nagoya"),
            ("Labo", "桂木研究所", "Nagoya"),
            ("InTrain", "電車車内", "Nagoya"),
            ),
        "DAYS": (
            # (tag / name / month / day / year)
            ),
        "TIMES": (
            # (tag / name / hour / minute)
            ),
        "ITEMS": (
            # (tag / name / cate / info)
            ),
        "WORDS": (
            # (tag / name / cate / info)
            ("yakata", "泪館"),
            ("sns", "ＳＮＳ"),
            ("line", "ＬＩＮＥ"),
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ("桂木美彩", "桂木美彩《かつらぎみさ》"),
            ("白鷺悠里", "白鷺悠里《しらさぎゆり》"),
            ("蒔田幸男", "蒔田幸男《まきたゆきお》"),
            ("昭雄", "昭雄《あきお》"),
            ("滴る雫", "滴《したた》る雫《しずく》"),
            ("婉曲", "婉曲《えんきょく》"),
            ("昂り", "昂《たかぶ》り"),
            ("泪館", "泪館《なみだかん》"),
            ),
        }

