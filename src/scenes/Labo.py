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
    yukio, misa = w.get("yukio"), w.get("misa")
    return w.scene('研究所の朝',
            w.cmd.change_camera("yukio"),
            w.cmd.change_stage("Labo"),
            w.cmd.change_time("midmorning"),
            w.cmd.change_date(9,28, 2020),
            w.plot_note("$yukioは研究所で$misaの助手をやっていた"),
            w.plot_note("最近の$misaは涙の研究にはまっていて、入室した途端に$yukioから涙を採取する"),
            w.plot_note("$misaは涙の種類について語る"),
            w.plot_note("感情が動いて流す涙と普段流している涙には明確な違いがあり、味も違うと言い出す"),
            "冒頭は滅多に無く$misaが泣いていたから。でもそれは実験の為だったという",
            "マンションの階段を登ってくる足音から",
            "女性の涙について考えている$yukio",
            "手にはタウン誌。その表紙に「都市伝説特集」",
            "見下ろすと「再開発反対」の幟が立っていて、おじさんが街頭演説をしている",
            yukio.come("#寝ぼけ眼で鍵を開けて入ってくる$S"),
            misa.be("#試験管を手に何かを作っている$S"),
            yukio.do("残暑、と呼ぶには既に肌寒く、それは昨日から降り続いている雨のせいだったけれども$full_yukioは真っ赤な女物の傘を手にその住宅街に入っていく",
                "目的の五階建てのマンションはベージュの外壁でその軒先から涙のように滴る雫が傘を外れて彼の肩を僅かに濡らした"),
            yukio.do("傘を畳み、エレベータで四階に上がる",
                "その間にコンビニに置いていた無料のタウン誌をぺらぺらと捲って見るが都市伝説特集とタイトルにあったのに記載されているのは大半がただの心霊スポットだった").omit(),
            misa.do("#泣いている$S"),
            yukio.talk("おはようございます"),
            yukio.do("と口から出してしまってから、スカートの上に白衣を着たすらりと長身の女性が目に涙を浮かべてこちらを凝視しているのに気づいて$Sはどう対処したものかと思考回路が一旦停止してしまう", "&"),
            yukio.do("部屋を間違えたのだろうか、とも思ったが遠心分離機や机の上に並ぶ試験管類、スチール棚には学術書と分厚いファイルが並ぶその見慣れた光景はどう考えても『$Labo』だ",
                "目の前の女性もその鋭い眼光ときゅっと結ばれた発色のいい唇、耳が隠れる程度のショートの茶髪という$Sが知る$full_misaそのものだった"),
            misa.talk("朝イチに出会った人間に対して見せる顔じゃないな"),
            yukio.talk("いや、鬼の目にも涙ってこういうことを言うんですね"),
            yukio.think("それは$Sが持ち合わせた語彙の中で一番無難な婉曲表現のはずだった"),
            misa.talk("$meだって涙の一つくらい持ち合わせいるわ",
                "そもそも人間というのは常日頃から泣いている生き物なのよ？",
                "さては金曜に渡した資料読んでないわね"),
            yukio.do("帰る直前に「あ、これ来週からの新しい研究課題だから目通しておいて」と渡されたままそのファイルは鞄の中に眠っている"),
            yukio.do("ただでさえ先週は九州の取引先企業とここを行ったり来たりしていたので土日は疲労困憊のまま睡魔と仲良くしてしまったので、",
                "$Sは「ああ、あれですね」と適当に誤魔化そうとして視線を天井の隅へと向ける",
                "五年前にリフォームしたといはいえ築四十年の住居はところどころに痛みの跡が見えた",
                "具体的には雨漏りの跡なのだが").omit(),
            misa.talk("人間の涙というのは眼球を保護する為に$meたちが意識しなくても常に流れているのよ",
                "交感神経と副交感神経という言葉は知っているわね？",
                "人間には自律神経があってこの二つの神経系がそれぞれ優位になることで様々な機能が調整されているの",
                "涙もその一種よ",
                "交感神経が優位になれば興奮して眼球の血流量が少なくなり涙が抑えられる",
                "逆に副交感神経が優位になれば涙の量が増えるわ"),
            yukio.talk("じゃあ悲しいときは副交感神経ですか？"),
            yukio.do("鞄を自分の仕事机の上に置き、肩が濡れた薄手のジャケットを脱いでハンガーを手に取る",
                "生憎と個人用ロッカーなどは存在しないのでベランダに干された白衣の隣にそれを掛けた"),
            yukio.do("雨はもう上がりそうだが吹き込むようなら仮眠室か浴室に移動した方がいいだろう").omit(),
            misa.talk("感情の昂りによって出る涙は普段眼球を保護しているそれとは違うのよ",
                "味が違うと言ったら分かるかしら"),
            yukio.talk("涙に味なんてあるんですか？"),
            misa.talk("味のないものなんて世の中に存在しないわ",
                "味覚が鈍感というなら別だけれど何かしらの成分を含んでいる訳だからそれに対する受容体はきちんと反応するわ",
                "舐めてみる？"),
            yukio.do("自身の目に溜まったそれを小型のスポイトで採取して、彼女は$Sの顔をまじまじと眺める"),
            "ここでこのマンションは大丈夫なんでしょうか、という疑問を再開発に絡めて",
            )


def urban_legend(w: World):
    yukio, misa = w.get("yukio"), w.get("misa")
    return w.scene("都市伝説",
            w.cmd.change_stage("Labo"),
            w.plot_note("$yukioが$yakataの都市伝説について語る"),
            w.plot_note("$yakataで映画を見たカップルは別れるという噂だった"),
            w.plot_note("$misaはそこで泣いている女はどうせ利用しているだけで本物の涙を流す女はいないと断言する"),
            yukio.talk("いえ結構です",
                "それよりこれ、どう思います？"),
            yukio.do("このままだとまたいつものように実験台にされかねないと手にしていたタウン誌で話題の変更を試みた"),
            misa.talk("オカルトは$meの研究の題材にはならないの、$k_yukioはよく知っているでしょう？"),
            yukio.talk("心霊スポットじゃなくてこっちを見て下さいよ"),
            yukio.do("$Sが指差したのはタウン誌の特集記事の隅っこに小さく掲載された『カップルが別れる映画館』というものだ"),
            misa.talk("却下"),
            yukio.talk("これ$meが高校の頃からある噂なんでちょっと懐かしいなって思ったんです",
                "聞いたことありません？　$yakataて"),
            yukio.think("全く恋愛に縁がなかったあの時代、それでも周囲には付き合っている男女を少し羨ましく眺めていたものだけれど、",
                "ある時女子生徒が集団で話しているときにこんな話をしていたのだ",
                "その映画館でカップルで映画を見たら必ず別れるから別れたくなったらそこにこっそり行けばいいのだと"),
            yukio.think("偶然別れたカップルがいたのがそういう噂話に発展したものだろうと思っていたけれど、意外とその噂は生き延びて今こうしてタウン誌にまで記載されている",
                "科学的では全然ないかも知れないけれどそういう謎にこそ$Sはロマンを感じることができた").omit(),
            misa.talk("へー、それで$k_yukioはその都市伝説を信じている訳？"),
            yukio.talk("信じる信じないって話じゃないです",
                "ただ学校の七不思議とかもそうですけどこの手の話って何かきっかけがあって生まれて、それがミームのように人の記憶を辿って受け継がれていくの、",
                "面白いなと思うんですよ"),
            misa.talk("分かった",
                "じゃあ早速そこに行って涙のサンプルを取ってきてくれるかしら",
                "できれば女性がいいわね", "それも一人で映画を見に来て泣いている女性が"),
            yukio.think("やけに限定的な指定に疑問符を沢山浮かべつつ曖昧な返事をすると$Sはその視線を一旦窓の外へと投げた",
                "&"),
            yukio.do("まだ雨は止まずにアスファルトを濡らし続けているがこの中に出ていくのをあと三十分どうやって引き延ばそうかと考え、$Sはこう提案した"),
            yukio.talk("ところで所長、コーヒー飲みたくありませんか？"),
            )


def acquaintaince(w: World):
    yukio, misa = w.get("yukio"), w.get("misa")
    yuri = w.get("yuri")
    return w.scene("知人",
            w.cmd.change_stage("Labo"),
            w.cmd.change_time("afternoon"),
            w.plot_note("ラボにやってくると$misaと$yuriは険悪な雰囲気がかもしだされる"),
            w.plot_note("どうやら大学時代の知り合いらしく、$misaは$yuriの涙が全て嘘だと言い切った"),
            "ここからは特に$yuriと$misaの表情や仕草に注意して描写。二人の関係性や違いが分かるように",
            yukio.come("#$yuriを連れて戻ってくる"),
            yukio.talk("ただいま戻りました"),
            misa.be("#何かよくわからない実験をしていた"),
            yuri.come(),
            yukio.do("研究所という名のマンションの一室に戻ると$misaはパソコンの前に座って数枚のグラフを見比べていた",
                "英数字が並ぶそれが何なのかは$Sには分からなかったが自分に関係のないものならいいなと思いつつ、",
                "一緒に入室してきた女性を簡単に紹介する"),
            yukio.talk("あの所長、こちらは今回涙の採取に協力して下さった$ln_yuriさんです"),
            yuri.talk("失礼します", "マンションの一室なんですね", "&"),
            yuri.talk("研究所というからもっと立派なものを想像してしまったけれどそれこそ健康食品や美容食品を扱っていてもおかしくないんじゃないかしら",
                "それで、そちらが上司の"),
            misa.talk("$ln_misa", "ご協力いただいたみたいでどうも",
                "けれどわざわざここまで出向いてくるなんて、ちょっと神経を疑うわね"),
            misa.do("$Sは$yuriの発言を遮って名乗ると険しい視線を投げつける"),
            yukio.talk("すみません", "この人いつもこんな調子なもので"),
            yukio.do("険悪になりそうなところに割って入り$yuriに応接用パイプ椅子に座るように促すが、",
                "$misaの方はお茶を用意しようとしている$Sに掌を見せてサンプルの提出を催促してくる"),
            misa.talk("その女にお茶なんて出す必要ないわ"),
            yukio.do("$Sが鞄から取り出したサンプルを毟り取って分析器にセットしながら明らかにいつもより苛立った声でそう告げる",
                "$yuriの方も当然機嫌は損なわれていて小さな溜息で$misaから視線を逸らすと、テーブルの上のタウン誌を手にして眺め始めた"),
            )


def analyzed(w: World):
    yukio, misa = w.get("yukio"), w.get("misa")
    yuri = w.get("yuri")
    return w.scene("分析結果",
            w.cmd.change_stage("Labo"),
            w.plot_note("分析結果が出て、彼女の涙はほとんどが水だったという$misa"),
            w.plot_note("$yuriは本気の涙だったと力説するが、結果は覆らないという$misa"),
            w.plot_note("$misaは$yuriが今流している涙も分析し、それもほぼ涙で感情の涙ではないと説明する"),
            yukio.be(),
            misa.be(),
            yuri.be(),
            yukio.do("それから三十分が沈黙のまま経過した",
                "空気は時間経過で質量を増やしているのかと思うほどに重く、分析器の小さなモータ音と$yuriがページを捲る音、$Sがコップから烏龍茶を飲む音だけが定期的に静寂を打ち破った"),
            misa.talk("結果が出た"),
            yukio.do("$misaがそれだけ口にしてパソコンに向かう",
                "三枚あるうちの二つのモニタにはそれぞれ棒グラフが表示され、片方は緑色、片方は赤いもので一部似たような長さだったが赤い方が全体的に短くなっている",
                "下部に表示されているアルファベットのいくつかはナトリウムやカリウムだと思われたが全部は$Sには分からなかった"),
            misa.talk("この意味が理解できる？"),
            yukio.do("どちらに対しての質問だったのだろう",
                "$Sは一応考える素振りを見せたが何か口にするより先に$yuriが質問を返した"),
            yuri.talk("どちらが$meの涙？"),
            yukio.do("検体ＡとＢがあり、おそらくＢの方が彼女のものなのだろうが$misaは何も答えないままマウスをクリックする",
                "両方のグラフの上に折れ線グラフが表示され、それが重ねられた"),
            yuri.talk("だから何なの？"),
            yukio.talk("あ、えっとですね、この折れ線グラフは各成分の平均値を繋いだものです"),
            yukio.do("$misaが説明を始めようとしないので$Sが分かる範囲で口を出した"),
            yukio.talk("涙というのは水以外にミネラル分を含んでいます",
                "よく塩辛いとか言いますけどあれはナトリウムが含まれているからですね",
                "こちらのグラフにはその成分がどれくらい含まれていたかを示したもので"),
            yuri.talk("平均値よりどちらも低いみたいだけれど、低い、つまり含まれた成分が少ないというのはほぼ水だと言ってしまっていいってことかしら？",
                "これを調べて一体何が分かるの？"),
            misa.talk("涙は自然に出るものと感情で出るものがある"),
            yukio.do("腕組みをした$misaがようやく口を開く"),
            misa.talk("感情によって出す涙には個人差があるし何より出る状況が全然違うわ",
                "$meが興味あるのは涙の分析からその人間の本質を見極めることよ",
                "このグラフの片方は$meが小指をわざとぶつけて刺激によって流した涙で、",
                "もう片方があなたのものよ",
                "$meが言っている意味、理解できる？"),
            yukio.do("$Sが説明するまでもないことだった",
                "それは$yuriの表情を見ても明らかで彼女は$misaが言いたいことを理解した上で目元を強張らせた"),
            yuri.talk("$meが悲しんでいない、とでも言うの？"),
            misa.talk("そうよ"),
            )


def lost_sadness(w: World):
    yukio, misa = w.get("yukio"), w.get("misa")
    yuri = w.get("yuri")
    return w.scene("失われた悲しみ",
            w.cmd.change_stage("Labo"),
            w.plot_note("いつからか「悲しい」という感情が失われていた女"),
            w.plot_note("悲しいという「装置」だったと、あの$yakataについて話す"),
            w.plot_note("$yuriは最初で最後の涙を流したのが、あの$yakataだったと語った"),
            yukio.be(),
            misa.be(),
            yuri.be(),
            misa.do("$Sはいつもの調子で断言した"),
            misa.talk("学生時代からあなたはそうだった",
                "地味な外見で男性に近づいて安心させておいて利用するだけ利用しては次の男に乗り換える",
                "同期生の女友達にはこう言ってたらしいじゃない",
                "男性は本能的に騙されたがっているから自分はそれに応じているだけだって"),
            yukio.talk("同期って、同じ大学だったんですか？"),
            yukio.do("驚きの声を上げた$Sをひと睨みすると$misaはそのまま言葉を続けた"),
            misa.talk("あなたの母親は男性を利用するものだと教えた",
                "でも根が真面目なあなたは利用しながらもそれが恋という形なのだと思い込もうとした", "&"),
            misa.talk("あなたでしょ？", "$yakataの噂を流したのは"),
            yukio.talk("え？"),
            yuri.talk("そうよ", "付き合うのに理由は必要なくても別れるには何かしら理由が必要だったから",
                "$meはあそこで映画を見たから別れた、という理由を作るために噂を流したのよ",
                "でも最初だけよ？",
                "あとは勝手に都市伝説になっただけだわ"),
            misa.talk("そんなごまかしが通用すると思ってるの？"),
            yukio.do("$misaはテーブルの上のタウン誌を手に取り、あるページを広げて見せた"),
            misa.talk("この写真の後ろ姿、あなたよね？", "一度だけじゃなく何度も補強して完全にあの映画館を別れの場所にしたがった",
                "あなたにとってあそこが必要だったからよ"),
            yuri.talk("だったら何？"),
            misa.talk("あなた自身は失恋して悲しいという感情がない",
                "それはどういう事情なのか分からないわ",
                "でもね、悲しいという感情を味わいたいという気持ちまでは失われていないの",
                "あなたにとって涙に悲しいという感情を与える場所が、あそこだった",
                "だからあの場所がなくならないように都市伝説を流したのよ",
                "あなたの悲しみを、また失わないために"),
            yuri.do("その言葉に、$Sの両目からすうっと涙が落ちた"),
            yuri.talk("いつからかこんな風に何も考えなくても自然と涙を流すことができるようになったわ",
                "小さい頃はがんばって演技をしたというのにね、大嫌いな母親や、かつて父親だった人の前で"),
            yuri.do("$Sは自分の瞳から落ちる雫を掌ですくい取り、それを$misaに差し出すとこう尋ねた"),
            yuri.talk("この涙も分析して下さる？"),
            misa.do("けれど彼女は首を振り「熱いコーヒーでも飲まないか？」と笑顔を返した"),
            )
