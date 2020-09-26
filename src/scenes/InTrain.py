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
    yukio = w.get("yukio")
    yuri = w.get("yuri")
    return w.scene('$yuriの事情２',
            w.cmd.change_stage("InTrain"),
            w.cmd.change_time("noon"),
            w.plot_note("涙を採取し、分析に回そうとする$yukioに、一緒に研究所に行くという$yuri"),
            w.plot_note("移動する間も$yuriは別れた事情について話す"),
            w.plot_note("しかし付き合ううちに彼が女を道具としてしか見ていなかったことが分かった"),
            w.plot_note("そこに最初から最後まで恋愛感情がなかったことが分かり、別れた"),
            w.plot_note("聞いているとどう考えても泣くような話には、$yukioは思えなかった"),
            yukio.be(),
            yuri.be(),
            yukio.do("食べ終えるとまだ話の続きがあるというので中央駅まで地下鉄に乗りつつ、話の続きを聞いた"),
            yuri.talk("意外と悪くないかな、と最初の頃は思っていたわ",
                "女性の扱いも上手いしお金の使い方もよかった"),
            yuri.talk("でもね、ある時彼の$snsにあった大量の女性のアドレスコレクションを見つけてしまったの"),
            yuri.talk("彼は全てを告白したわ",
                "小さい頃からよくもてた自分にとっていつしか女性はカードのようにコレクションとして集めるだけの存在になってしまったって",
                "でもそこに愛も恋もまったくなく、つまらなく感じていたところに同じ価値観を持つ人間を見つけたんだって",
                "それが$me",
                "$meは男性をコレクションと考えたことはなかったけど、言いたいことは分かったわ"),
            yuri.talk("でも$meと彼には決定的な違いがあった",
                "それは彼が結婚という最終形を目指していたこと",
                "互いを利用し合う関係でよかったのに"),
            yuri.talk("こうして$meと彼の恋愛は終わったのよ",
                "$meにとっては永遠に終わらないことが大事だったの"),
            yukio.think("それを聞くとますます彼女が映画館で泣いていた理由がわからなくなった"),
            )

