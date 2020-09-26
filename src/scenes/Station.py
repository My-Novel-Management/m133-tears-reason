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
def many_people(w: World):
    yukio = w.get("yukio")
    yuri = w.get("yuri")
    return w.scene("たくさんのカップル",
            w.cmd.change_stage("Station"),
            yukio.come("中央駅前まで戻ってくる"),
            yuri.come(),
            "駅前の雑踏と、郷愁",
            "そこに出会いと別れと恋模様が散らばっている",
            "映画館なんて必要ない、と思わせるスマホで映画を見ている二人とか",
            yukio.do("沢山の人"),
            yukio.do("待ち合わせをしているカップルが抱き合って喜んでいる"),
            yuri.talk("あんな風に単純に出会ったことを喜べる間だけが、恋なのよ",
                "でもそれを過ぎたらもうあとはどうやって延命するか、あるいは結婚という形を手に入れるか",
                "そう思わない？"),
            yukio.talk("$meはその人たちの色々な姿があると思います",
                "結婚しなくても、一人でも、二人でも、あるいはもっと別の形でも、",
                "その人たちにとっての何らかの形があると",
                "それを幸せって呼ぶかどうかは分かりませんけど"),
            yuri.talk("あの、$meも一緒に連れていってもらえるかしら、その研究所に"),
            )
