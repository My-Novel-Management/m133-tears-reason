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
def her_situation(w: World):
    yukio = w.get("yukio")
    yuri = w.get("yuri")
    return w.scene("$yuriの事情１",
            w.cmd.change_stage("Cafe"),
            w.cmd.change_time("midmorning"),
            w.plot_note("$yuriは自分が泣いている理由について語り始める"),
            w.plot_note("$yuriは下着メーカーに勤めていた男性$akioと恋愛関係になった"),
            w.plot_note("彼女からすると嫌な男としか感じなかったらしい"),
            w.plot_note("それでも男のステータスと金払いの良さなどに魅力を感じて、徐々に関係が深まった"),
            w.plot_note("語っている間に映画が終わってしまった"),
            "場所移動したことを冒頭で説明的に描写",
            "映画が終わり、二人で近くの喫茶店に入った",
            yukio.come(),
            yuri.come(),
            yukio.do("近くの喫茶店に入る"),
            yukio.do("昼前だからか人が賑わっている"),
            yukio.talk("ここでも大丈夫ですか？"),
            yuri.talk("構いませんよ", "賑やかな方がむしろ紛れますから"),
            yukio.do("二人とも注文を終わらせると彼女から語り始めた"),
            yuri.do("$full_yuriと名乗った女性は「失恋がどういうものか、あなたは知っている？」と始めた"),
            yuri.talk("誰でも恋の一つや二つはしたことがあると思う"),
            yukio.think("その話しぶりはどこか$misaを思わせた"),
            yuri.talk("$akioはキラキラとして傍目には幸せに溢れているように見えた"),
            yukio.do("別れた男性について語る彼女"),
            yuri.talk("女性にはずっと不自由してこなかったんだと思えるルックスと人当たりの良さ"),
            yuri.talk("けれど何故か彼の周囲にはエアポケットのような時間があった"),
            yuri.talk("それが気になって、少しだけ話しかけたの"),
            yuri.talk("向こうも最初は$meのことをあまりいけすかない奴だと思ってたらしいわ"),
            yuri.talk("これでも普段はね、もっとちゃんと化粧も髪のセットも、服や香水にだって気を遣うわ"),
            yuri.talk("でも泣きたい日くらいは少し手を抜いたっていいでしょう"),
            yuri.talk("ここが$yakataって都市伝説の場所なのは知っている？"),
            yuri.talk("あなたが聞いたのは”ここで映画を見たカップルは別れる”というものでしょう？",
                "けどね、それは正確じゃないの",
                "別れたいと思っているカップルがここを訪れるのよ",
                "そうすればどちらの所為でもなく映画館の所為にして別れることができる",
                "誰にとっても一番良い結果になるわけよね"),
            yukio.talk("それじゃあどうしてあなたは一人でここに？"),
            yuri.talk("その前に食べましょうか"),
            yukio.do("目の前には温かいスープとクリームが大盛りの小倉パンケーキが持ってこられた"),
            )
