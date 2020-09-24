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
def her_situation2(w: World):
    return w.scene('$yuriの事情２',
            w.cmd.change_stage("InTrain"),
            w.plot_note("涙を採取し、分析に回そうとする$yukioに、一緒に研究所に行くという$yuri"),
            w.plot_note("移動する間も$yuriは別れた事情について話す"),
            w.plot_note("しかし付き合ううちに彼が女を道具としてしか見ていなかったことが分かった"),
            w.plot_note("そこに最初から最後まで恋愛感情がなかったことが分かり、別れた"),
            w.plot_note("聞いているとどう考えても泣くような話には、$yukioは思えなかった"),
            )

