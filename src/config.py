# -*- coding: utf-8 -*-
'''
Story Config
============
'''

ASSET = {
        "PERSONS": (
            # (tag / name / full / age (birth) / job / call / info)
            ("yuri", "ユリ", "シラサギ,ユリ", 32,(1,1), "female", "会社員", "me:わたし"),
            ('misa', 'ミサ', 'アイジョウ,ミサ', 37,(1,1), 'female', '研究員', "me:私"),
            ("yukio", "ユキオ", "マキタ,ユキオ", 25,(1,1), "male", "助手", "me:僕"),
            ("akio", "アキオ", "イルマ,アキオ", 40,(1,1), "male", "会社員", "me:俺"),
            ),
        "STAGES": (
            # (tag / name / parent / (geometry) / info)
            ("Aichi", "愛知県", "Japan"),
            ("Nagoya", "名古屋市", "Aichi"),
            ("Station", "駅", "Nagoya"),
            ("Subway", "地下鉄", "Nagoya"),
            ("Cinema", "映画館", "Nagoya"),# 三越映画劇場モデル
            ("Manshion", "マンション", "Nagoya"),
            ("Labo", "研究所", "Nagoya"),
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
            ),
        "RUBIS": (
            # (origin / rubi / exclusions / always)
            ),
        }

