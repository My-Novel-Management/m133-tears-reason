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
def every_morning(w: World):
    return w.scene('研究所の朝',
            w.cmd.change_camera("yukio"),
            w.cmd.change_stage("Labo"),
            w.cmd.change_time("midmorning"),
            w.plot_note("$yukioは研究所で$misaの助手をやっていた"),
            w.plot_note("最近の$misaは涙の研究にはまっていて、入室した途端に$yukioから涙を採取する"),
            w.plot_note("$misaは涙の種類について語る"),
            w.plot_note("感情が動いて流す涙と普段流している涙には明確な違いがあり、味も違うと言い出す"),
            )


def urban_legend(w: World):
    return w.scene("都市伝説",
            w.cmd.change_stage("Labo"),
            w.plot_note("$yukioが$yakataの都市伝説について語る"),
            w.plot_note("$yakataで映画を見たカップルは別れるという噂だった"),
            w.plot_note("$misaはそこで泣いている女はどうせ利用しているだけで本物の涙を流す女はいないと断言する"),
            )


def acquaintaince(w: World):
    return w.scene("知人",
            w.cmd.change_stage("Labo"),
            w.plot_note("ラボにやってくると$misaと$yuriは険悪な雰囲気がかもしだされる"),
            w.plot_note("どうやら大学時代の知り合いらしく、$misaは$yuriの涙が全て嘘だと言い切った"),
            )


def analyzed(w: World):
    return w.scene("分析結果",
            w.cmd.change_stage("Labo"),
            w.plot_note("分析結果が出て、彼女の涙はほとんどが水だったという$misa"),
            w.plot_note("$yuriは本気の涙だったと力説するが、結果は覆らないという$misa"),
            w.plot_note("$misaは$yuriが今流している涙も分析し、それもほぼ涙で感情の涙ではないと説明する"),
            )


def lost_sadness(w: World):
    return w.scene("失われた悲しみ",
            w.cmd.change_stage("Labo"),
            w.plot_note("いつからか「悲しい」という感情が失われていた女"),
            w.plot_note("悲しいという「装置」だったと、あの$yakataについて話す"),
            w.plot_note("$yuriは最初で最後の涙を流したのが、あの$yakataだったと語った"),
            )
