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
    return w.scene('泣く女',
            w.cmd.change_stage("Cinema"),
            w.plot_note("$misaに言われ$yakataにやってくる$yukio"),
            w.plot_note("そこでアクション映画にもかかわらず泣いている女がいた"),
            w.plot_note("$yukioは$yuriに涙を調べさせてほしいと頼み込む"),
            w.plot_note("最初こそ不審に思われたが$yuriは別れた事情を聞くという約束と引き換えに承諾してくれた"),
            )


def her_situation(w: World):
    return w.scene("$yuriの事情１",
            w.cmd.change_stage("Cinema"),
            w.plot_note("$yuriは自分が泣いている理由について語り始める"),
            w.plot_note("$yuriは下着メーカーに勤めていた男性$akioと恋愛関係になった"),
            w.plot_note("彼女からすると嫌な男としか感じなかったらしい"),
            w.plot_note("それでも男のステータスと金払いの良さなどに魅力を感じて、徐々に関係が深まった"),
            w.plot_note("語っている間に映画が終わってしまった"),
            )
