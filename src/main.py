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
from scenes import Cafe
from scenes import Cinema
from scenes import InTrain
from scenes import Labo
from scenes import Station


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
TITLE = "悲しみの落ちる場所"
MAJOR, MINOR, MICRO = 0, 9, 0
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
RELEASED = (9, 27, 2020)


# Episodes
def ep_first_talk(w: World):
    return w.episode("最初の会話（映画館の噂）",
            Labo.every_morning(w),
            Labo.urban_legend(w),
            )

def ep_get_tears(w: World):
    return w.episode("涙の採取",
            Cinema.woman_tears(w),
            )

def ep_depart_story(w: World):
    return w.episode("別れた事情",
            Cafe.her_situation(w),
            InTrain.her_situation2(w).omit(),
            Station.many_people(w).omit(),
            )

def ep_truth(w: World):
    return w.episode("分析結果と真相と",
            Labo.acquaintaince(w),
            Labo.analyzed(w),
            Labo.lost_sadness(w),
            )


def ch_main(w: World):
    return w.chapter('main',
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
            ep_first_talk(w),
            ep_get_tears(w),
            ep_depart_story(w),
            ep_truth(w),
            w.symbol("（了）"),
            )


# Notes
def writer_note(w: World):
    return w.writer_note("覚書",
            "女性の涙というのは男性にとってはいつまでも神秘的でよく分からないものだ",
            "その中に何千もの嘘が紛れているのに、男は見抜けない",
            "しかし涙は感情により味が変わるという",
            "それは交感神経と副交感神経のバランスが変わり、普段目を潤している涙とは異なり、",
            "感情の発露としての涙だかららしい",
            "本作ではそんな女の涙の嘘を科学的に解明し、なおかつ、都市伝説や占いといった女性が好きそうな話題をからめることで、",
            "ミステリとしても楽しめるようにしたものである",
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

def chara_notes(w: World):
    return (chara_misa(w),
            chara_yuri(w),
            chara_yukio(w),
            chara_akio(w),
            )

def chara_yuri(w: World):
    return w.chara_note("$yuriの履歴書",
            "ホステスと土方の両親に下に生まれる",
            "場所は名古屋の栄、歓楽街",
            "母親は東南アジアの血が入っていてせっせと自分の兄弟のために仕送りをしていた",
            "父親は顔すら覚えておらず、入れ替わり立ち替わり、色々な男を連れ込んでは金をせびっていた",
            "その頃から男は利用するものだと刷り込まれた",
            "初恋は小学生の先生",
            "ロリコンでやたらとべたべた触ってくる気持ち悪い先生だったが、ちょっと優しくするとすぐに贔屓して成績もよくつけてくれた",
            "その頃にうそなきも覚えた",
            "中学の頃には男子たちにも評判になっていて、エキゾチックな顔立ちでよく持てた",
            "ただ真剣に恋をするような相手は現れず、いつも適当にかっこいい男子を捕まえては恋人のいない期間を造らなかった",
            "高校二年の時、当時やっていたバスケ部のマネージャーとしていった対抗試合の相手学校にいた男子に初恋に落ちる",
            "今までの自身から絶対に落ちると思って手を尽くしたものの、彼には将来を誓った女性までもがいて、始めて失恋してしまった",
            "失恋そのものもショックだったが、それ以上に自分が失恋したことを周囲に知られたくなくて、彼と一度だけデートにいった映画館に「ここで映画を一緒に見たカップルは別れる」というジンクスを言いふらした",
            "それが$yakataの所以である",
            "それから大学、社会人となり、相手と別れる度にそこにやってきては泣いていた",
            "それが$Sの別れの儀式となった",
            )

def chara_misa(w: World):
    return w.chara_note("$misaの履歴書",
            "父親は生まれる前に蒸発して行方不明なままで、結局七年経ってから失踪人になり死亡したことにされた",
            "母は泣かない女だった",
            "企業の研究室で成果を出し、同期の中でも出世頭として三十で室長を務めていた",
            "$Sはいつも一人でお留守番をしていることが多く、住まわせてもらっていたアパートの大家夫婦によくしてもらった",
            "小さな畑でいろいろと作っている人たちで、その頃から何かと探究心が強かった",
            "小学校で理科に出会い、実験器具を勝手に使ってはいろいろして壊して怒られた",
            "それでも当時の担任が理解ある人で、$Sの疑問に丁寧に答えてくれた",
            "中学に入ると一人でいろいろと実験をするようになる",
            "大学では大手を振って実験できると意気込んだものの、意外と規制が厳しく、思ったようにならなかった",
            "先生にも恵まれず、先輩のツテで企業の研究所に入り浸った",
            "就職もそこになったが、三十で独立",
            "自分の研究所を作り、そこでへんてこな研究をしては企業に売りつけて商売をしている",
            )

def chara_yukio(w: World):
    return w.chara_note("$yukioの履歴書",
            "岐阜県の小さな街に生まれる",
            "農家をやっている両親で、兄弟も男三人女三人と大家族だった",
            "次男である$Sは何かと板挟みの中でいいように使われる日々",
            "それは学生になっても変わらず、あれこれと頼まれてはパシリをするという毎日だった",
            "大学を出て精密機器を売る会社員（営業）になる",
            "ある日、汗を調べさせてほしいという不思議な女性（$misa）と出会い、そこから研究所にスカウトされた",
            )

def chara_akio(w: World):
    return w.chara_note("akioの履歴書",
            "奈良県の中規模都市で生まれる",
            "父親は関西人だが母親は関東人で、調子のいい父親と生真面目な母親はどこか合わない",
            "外面がよく金遣いの荒い父は、他人や異性にモテたが、母親からは酷く嫌われていた",
            "母はよく$Sに愚痴り、ああなってはいけない、という言葉が強く残る",
            "しかし顔面偏差値が高かった$Sは小学生、中学、高校とよくもて、父親は悪くないんだという思考になった",
            "大学時代に女遊びが開花すると、サークル仲間と女をはめては遊んでいた",
            "就職も面接官の人事課の女性課長に気に入ってもらい、女性用下着の会社に簡単に決まる",
            "それからも順風満帆に思えた",
            "しかしいつも女に本気にはなれず、ただの道具のように使い捨てる",
            "本気で恋をして結婚することはあるのだろうかと、どんどん結婚して身を固めていく友人たちを見て悩んでいた",
            "そんな時に出会ったのが$yuriだった",
            "結婚を前提に、という言葉を初めて口にした女性だったが、彼女はどうも本気ではないのが透けて見えた",
            "自分と同じ人種だと分かった",
            "やがて彼女から別れを切り出された。その理由は$S自身の人生の履歴だった",
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
            *chara_notes(w),
            stage_note(w),
            theme_note(w),
            motif_note(w),
            ch_main(w),
            )


if __name__ == '__main__':
    import sys
    sys.exit(main())

