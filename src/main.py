#!/usr/bin/env python3
# -*- coding: utf-8 -*-
'''
Story: "title"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World
from storybuilder.assets import basic
from storybuilder.assets import common_rubi
from config import ASSET
# import scenes
# from scenes import xxx


################################################################
#
#   1. Initialize
#   2. Story memo
#   3. Structure    - 1/8: 1K
#   4. Spec
#   5. Plot         - 1/4: 2K
#   6. Scenes
#   7. Conte        - 1/2: 4K
#   8. Layout
#   9. Draft        - 1/1: 8K
#
################################################################

# Constant
TITLE = "彼女の涙の理由はね"
MAJOR, MINOR, MICRO = 0, 3, 0
COPY = "その涙の本当の理由は、違っていた"
ONELINE = "映画館で一人泣いていた女の涙を採取したいと、謎の女が話しかけた"
OUTLINE = "約8000字の短編。映画館で泣いていた女性に謎の女が「あなたの涙を調べさせて」と言ってきた。その女は涙の研究をしていると説明した"
THEME = "女が流す涙の理由"
GENRE = "恋愛／ミステリ"
TARGET = "20-50years"
SIZE = "8K"
CONTEST_INFO = "妄想コンテスト「私が泣いた理由」"
CAUTION = ""
NOTE = ""
SITES = ["エブリスタ", "小説家になろう", "ノベルアッププラス", "カクヨム"]
TAGS = ["恋愛", "ミステリ", "失恋"]
RELEASED = (9, 20, 2020)


# Episodes
def ch_main(w: World):
    return w.chapter('main',
            "冒頭は$misaと$yukioの会話",
            "泪館の噂から",
            "それを聞いてそこで泣いてる女の涙を採取してきてという。あることを証明したいと",
            "いつも無理難題を言われる$yukio",
            w.plot_setup("$yukioは研究所で働いている"),
            w.plot_setup("$yakataという、そこで映画を見ると別れるという都市伝説のある映画館の噂を話す"),
            w.plot_turnpoint("$misaに命じられてそこで泣いている女の涙のサンプルを取ってくることになる"),
            w.plot_develop("$yuriが$yakataで一人泣きながらアクション映画を見ていた"),
            w.plot_develop("$yukioは調べさせてほしいとお願いする"),
            w.plot_develop("事情を聞き、$yuriは分析結果が聞きたいとついてくる"),
            w.plot_develop("$yuriはいかに$akioが酷い男だったか語る"),
            w.plot_turnpoint("分析結果が出て$misaは$yuriに「悲しんでなどいない」と突きつける"),
            w.plot_resolve("$yuriの涙はただ自分を可哀想な女に見せたいだけの偽物だった"),
            w.plot_resolve("その上、その噂を流したのは$yuriだと看破する"),
            "構造がちょい単調かも。どんでん返しがないとただの「本気で泣いてたんじゃないやん」で終わる",
            "研究者である$misaを主人公にする？",
            "いや助手役を主人公にするか。その方が採取のときが面白いし、共感者となる",
            "泪館という都市伝説のある映画館がある、と聞いて調査にやってきた、のではないと",
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            )

def plot_note(w: World):
    return w.writer_note("プロットメモ",
            "話の３本ライン",
            "１．＜現代性＞涙の味？",
            "２．＜社会性＞都市伝説（涙館）",
            "３．＜個人性＞別れの儀式",
            "映画を見て、一人泣いている女がいる",
            "彼女に近づいて、涙を分けて欲しいと頼む",
            "女は涙の研究をしていた",
            "涙の分析を終えて、彼女に言う",
            "失恋が悲しくて泣いていたんじゃないのねと",
            "女の涙の本当の理由は失恋して悲しい自分にひたっていただけだった",
            "分析する価値もない涙だと吐き捨てた",
            "視点は泣いている女側で",
            )

def chara_note(w: World):
    return w.writer_note("人物メモ",
            "・映画館で泣く女",
            "涙館は別れた女が泣きに来る場所",
            "ここで一人で映画を見ている女は周囲からすれば失恋後なのだと分かる",
            "その都市伝説を作った元凶の女",
            "・涙調査官",
            "・助手",
            )

def stage_note(w: World):
    return w.writer_note("舞台メモ",
            "映画館",
            "女が一人で泣きながら見ている映画が、全然泣ける映画じゃないのがいい",
            "研究所",
            "すごく怪しげなマンションの一室がいいかな。その方が「何この人感」が強まる",
            "- 三越映画劇場",
            "席数68／駐車場1200台／一般1400円／市営地下鉄・東山線・星ヶ丘駅",
            )

def theme_note(w: World):
    return w.writer_note("テーマメモ",
            "泣くのは誰のためなのか？",
            "涙を流すというのは",
            "涙の味が違う。感情の涙と普段流す涙では味が異なる（成分が異なる）",
            "泪橋という、別れの名所があった江戸",
            "この映画館は通称泪館。そこで映画を見ると別れると言われている",
            "そういう場所も使って「別れ」を計画した",
            "だからそこには別れた後の女性が涙を流すために映画を見るという噂話があった",
            "でもそれは学生時代の彼女が流した噂が、そのまま残って都市伝説になってしまったものだった",
            )

def motif_note(w: World):
    return w.writer_note("モチーフ",
            # main
            "涙", "涙の味", "涙の研究をしている謎の女",
            "都市伝説",
            # subs
            "噂",
            "研究",
            )

# Main
def main(): # pragma: no cover
    w = World.create_world(f"{TITLE}")
    w.config.set_version(MAJOR, MINOR, MICRO)
    w.db.set_from_asset(basic.ASSET)
    w.db.set_from_asset(common_rubi.ASSET)
    w.db.set_from_asset(ASSET)
    # spec
    w.config.set_copy(f"{COPY}")
    w.config.set_oneline(f"{ONELINE}")
    w.config.set_outline(f"{OUTLINE}")
    w.config.set_theme(f"{THEME}")
    w.config.set_genre(f"{GENRE}")
    w.config.set_target(f"{TARGET}")
    w.config.set_size(f"{SIZE}")
    w.config.set_contest_info(f"{CONTEST_INFO}")
    w.config.set_caution(f"{CAUTION}")
    w.config.set_note(f"{NOTE}")
    w.config.set_sites(*SITES)
    w.config.set_taginfos(*TAGS)
    w.config.set_released(*RELEASED)
    return w.run(
            writer_note(w),
            plot_note(w),
            chara_note(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

