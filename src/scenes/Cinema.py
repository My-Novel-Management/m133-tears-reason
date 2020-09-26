# -*- coding: utf-8 -*-
'''
Stage: "stage name"
'''
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
sys.path.append('storybuilder')
from storybuilder.builder.world import World


## scenes
def woman_tears(w: World):
    yukio = w.get("yukio")
    yuri = w.get("yuri")
    return w.scene('泣く女',
            w.cmd.change_stage("Cinema"),
            w.plot_note("$misaに言われ$yakataにやってくる$yukio"),
            w.plot_note("そこでアクション映画にもかかわらず泣いている女がいた"),
            w.plot_note("$yukioは$yuriに涙を調べさせてほしいと頼み込む"),
            w.plot_note("最初こそ不審に思われたが$yuriは別れた事情を聞くという約束と引き換えに承諾してくれた"),
            "ざっくり映画館の周辺の様子を描写",
            "入り口には寄付を求める小箱設置",
            "客は少ない",
            "場末感を",
            yukio.come("映画館にやってくる"),
            yukio.do("地下鉄を乗り継ぎ、駅から少し徒歩で、路地に入ると雑居ビルに入っている"),
            yukio.do("どこにも$yakataとは書いてないが、女性の一人客がちらほら入っていくのが見える"),
            yukio.do("平日だからほとんど客はいない"),
            yukio.do("映画は古いアクション映画だ"),
            yukio.do("全体が見渡せるように端の席に座る"),
            yuri.be(),
            "映画の途中で入ってきた$yukio",
            yukio.do("自分のすぐ上の席に座り、$yuriが映画を見ている"),
            "彼女の様子、雰囲気、容姿を丁寧に描写。あまり目立つタイプではないのに何故か目が惹かれる感じ",
            yukio.do("特に悲しい場面でもないのに彼女は涙を流し始めた"),
            yukio.do("$Sはそっと席を移動し、彼女がよく見える位置に陣取る"),
            yukio.do("注意深く彼女を観察する"),
            yukio.do("年齢は三十前後、髪にはパーマを当てて化粧は薄めだがしっかりしている"),
            yukio.do("服装は地味だが小物が決まっている"),
            yukio.do("ネイルが薬指だけ取れている"),
            yukio.do("ハンカチを取り出していたが、それはブランドもの、それも男ものだ"),
            yukio.do("彼女の表情は動かないものの、涙だけがするすると落ちる"),
            yukio.do("$Sは彼女にターゲットを決めて近づいた"),
            yukio.talk("あの、すみません", "涙を採取してもよろしいでしょうか"),
            yuri.do("一瞬びっくりして見たが"),
            yuri.talk("$meの涙に何か価値がおありですか？"),
            yukio.do("上司が涙の研究をしていると告げると"),
            yuri.talk("目薬の会社か何かですか？"),
            yukio.talk("まあ、その下請けというか、似たようなものです"),
            yukio.think("さすがに趣味で研究しているとは言い難く、そう誤魔化す"),
            yuri.talk("いいですよ"),
            yukio.do("持ってきたサンプラにスポイトで採取した涙を入れる"),
            yuri.talk("その変わり、少しお話に付き合っていただけます？"),
            )


