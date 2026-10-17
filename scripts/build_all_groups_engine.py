# -*- coding: utf-8 -*-
"""
Dramactor Scenario Engine for Groups 2 to 10 (Genres 5 to 49: 45 genres x 4 cycles = 180 episodes)
Provides high-fidelity, Hollywood-grade drama scenarios with 3-turn dialogues,
killer idioms, mediocre replies, and realistic Konglish traps with educational feedback.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn

def get_remaining_scenarios():
    data = {}

    # Helper lambda to shorten building
    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [
            make_turn(t[0], t[1], t[2], t[3], t[4], t[5])
            for t in turns_data
        ]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # -------------------------------------------------------------
    # Group 2 (Genres 5 to 9)
    # -------------------------------------------------------------

    # 5. Wall Street Hedge Fund
    data["Wall Street Hedge Fund"] = [
        mk_ep(
            "0.1초의 플래시 크래시: 고빈도 알고리즘 셧다운 결단",
            "Gordon Sterling (Chief Investment Officer)", "📈",
            "초고빈도(HFT) 알고리즘 폭주로 3초 만에 2억 달러 손실이 발생했다. 헤지펀드 CIO와 함께 수동 킬스위치를 내리고 시장 반등에 숏스퀴즈를 걸어야 한다.",
            "pull the emergency kill-switch and reverse the book",
            "알고리즘 폭주 시 긴급 킬스위치를 작동하고 포지션을 역전시킬 때 쓰는 월가 전문 용어입니다.",
            [
                (
                    "Our latency arbitrage algorithm is caught in an infinite loop! We're losing two million a second on S&P futures! Do I pull the plug or let the model self-correct?",
                    "초저지연 차익거래 알고리즘이 무한 루프에 빠졌어! S&P 선물에서 초당 2백만 달러씩 날리고 있다고! 플러그를 뽑을까, 모델의 자동 보정을 믿을까?",
                    "즉시 킬스위치를 내리고 전 서버 거래를 수동 제어로 전환하라고 명령하세요.",
                    ("Pull the emergency kill-switch right now! Kill the API connections and liquidate all open futures contracts before we trigger circuit breakers!", "즉각 비상 킬스위치 내려요! API 연결 전면 차단하고 서킷 브레이커 걸리기 전에 오픈 선물 포지션 전부 청산하세요!", "‘kill-switch’와 ‘liquidate all open futures’는 금융 위기 영화의 숨 막히는 긴급 명령입니다."),
                    ("Please wait five minutes to see if the computer is okay.", "컴퓨터가 괜찮아지는지 5분만 기다려봅시다.", "수천억 원이 증발하는 순간에 안일한 태도로 회사를 파산시킵니다."),
                    ("The algorithm has a bad spec so let's call the engineer for AS.", "알고리즘 스펙이 안 좋으니 엔지니어에게 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")
                ),
                (
                    "Switch pulled. We stopped the bleeding, but we're down sixty million on the day. Investors are calling our desk demanding an emergency redemption meeting.",
                    "스위치 내렸어. 출혈은 멈췄지만 오늘 하루 6천만 달러 마이너스야. 투자자들의 긴급 환매 요구 전화가 빗발치고 있어.",
                    "패닉 매도세가 바닥을 쳤으니 저가 매수로 반등을 유도해 손실을 복구하자고 설득하세요.",
                    ("We don't panic. The market is oversold on a liquidity vacuum. We buy the dip with our dry powder and ride the mean-reversion wave back to black.", "패닉에 빠지지 마세요. 유동성 공백으로 인한 일시적 과매도입니다. 비축 현금으로 저가 매수해 평균 회귀 파도를 타고 흑자로 복귀합니다.", "‘buy the dip with dry powder’와 ‘mean-reversion wave’는 월가 헤지펀드 트레이더의 시그니처 화법입니다."),
                    ("Tell the investors that we are very sorry and will try harder tomorrow.", "투자자들에게 정말 죄송하고 내일 더 열심히 하겠다고 전하세요.", "아마추어 같은 변명으로 투자자들의 전액 인출 사태를 촉발합니다."),
                    ("Let's send an SNS message to investors for skinship.", "투자자들과 스킨십을 위해 SNS 메시지를 보냅시다.", "‘SNS’와 ‘skinship’은 콩글리시입니다.")
                ),
                (
                    "The rebound hit! We caught the exact bottom tick. We just clawed back forty million in forty-five minutes. You've got ice in your veins.",
                    "반등이 터졌어! 정확히 바닥 틱을 잡았다고. 45분 만에 4천만 달러를 되찾았네. 자네 심장엔 피 대신 얼음물이 흐르는군.",
                    "이것이 월스트리트의 법칙이라며 트레이딩 데스크의 수익 실현을 지시하세요.",
                    ("That's how we hunt in a flash crash, Gordon. Lock in the profits, hedge our delta, and wire the performance fees to our team.", "그것이 플래시 크래시에서 살아남는 사냥법입니다, 고든. 수익 실현하고 델타 헤지 걸고, 트레이딩 팀에 성과급 송금하세요.", "‘lock in profits’와 ‘hedge our delta’는 트레이딩의 정석을 보여주는 완벽한 마무리입니다."),
                    ("I am happy we did not lose all our money today.", "오늘 돈을 다 날리지 않아서 다행입니다.", "성공한 헤지펀드 트레이더다운 패기가 전혀 없는 표현입니다."),
                    ("Let's do Dutch pay for the trading room beer tonight.", "오늘 밤 트레이딩 룸 맥주값은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "원자재 선물 쇼크: 마진콜 5억 달러 결제 10분 전",
            "Gordon Sterling (Chief Investment Officer)", "📈",
            "중동 정세 급변으로 원유 선물이 폭등하며 청산소로부터 5억 달러 마진콜 통보를 받았다. 10분 안에 담보를 차환하고 파산을 막아야 한다.",
            "meet the margin call without triggering firesales",
            "자산 헐값 매각 없이 담보 부족액(마진콜)을 신속히 조달할 때 쓰는 금융 표현입니다.",
            [
                (
                    "Brent crude surged seventeen percent on the drone strikes! The clearinghouse demands five hundred million dollars in collateral by 3 PM or they liquidate our fund!",
                    "브렌트유가 드론 공습으로 17% 폭등했어! 청산소가 오후 3시까지 담보금 5억 달러를 입금하지 않으면 우리 펀드를 강제 청산하겠다고 통보했네!",
                    "보유 중인 미 국채를 레포(Repo) 시장에서 당일 환매조건부채권으로 할인 조달하자고 하세요.",
                    ("We pledge our overnight Treasury holdings into the tri-party Repo market. We secure five hundred million in cash liquidity within six minutes.", "보유 중인 미국 국채를 3자간 환매조건부채권(Repo) 시장에 담보로 제공하겠습니다. 6분 안에 5억 달러의 현금 유동성을 확보할 수 있습니다.", "‘tri-party Repo market’과 ‘cash liquidity’는 유동성 위기를 극복하는 최고급 금융 금융공학 용어입니다."),
                    ("Call my mother to ask if she has some extra money.", "어머니께 전화해서 여윳돈이 있는지 물어보겠습니다.", "수천억 원 마진콜 상황에서 비상식적인 황당한 답변입니다."),
                    ("Let's make a meeting with the bank for morning call.", "모닝콜을 위해 은행과 미팅을 잡읍시다.", "‘morning call’은 콩글리시입니다.")
                ),
                (
                    "Repo cash secured! Wire sent to the clearinghouse with two minutes to spare. But our short oil position is bleeding ten million every hour.",
                    "레포 현금 확보 완료! 2분 남기고 청산소 송금 완료했어. 하지만 우리 원유 숏 포지션에서 매시간 천만 달러씩 손실이 나고 있네.",
                    "사우디 비축유 방출 발표를 미리 예측하고 옵션 스프레드로 헤지하자고 제안하세요.",
                    ("The Strategic Petroleum Reserve release is imminent. We buy out-of-the-money put spreads to hedge the tail risk and turn this shock into pure profit.", "전략비축유 방출 발표가 임박했습니다. 외가격 풋 스프레드를 매수해 꼬리 위험을 헤지하고 이 충격을 순이익으로 전환시키겠습니다.", "‘out-of-the-money put spreads’와 ‘tail risk’는 파생상품 헤지의 극치를 보여주는 표현입니다."),
                    ("Let's pray the oil price comes down very soon.", "기름값이 빨리 떨어지길 기도합시다.", "운에 기대는 비전문적인 태도입니다."),
                    ("The oil market has bad manners so let's claim them.", "원유 시장이 매너가 없으니 클레임을 겁시다.", "‘claim’은 콩글리시입니다.")
                ),
                (
                    "White House just announced the reserve release! Crude crashed twenty dollars in two minutes! The puts exploded four hundred percent! You just saved this fund from extinction.",
                    "백악관이 전략비축유 방출을 발표했어! 원유가가 2분 만에 20달러 폭락했네! 풋옵션이 400% 폭등했다고! 자네가 이 펀드를 파멸에서 구원했어.",
                    "위기를 기회로 바꾸는 것이 월스트리트의 미학이라며 승리의 미소를 지으세요.",
                    ("Volatility is our greatest weapon, Gordon. We cashed in the puts, closed the short, and booked a net seventy-million-dollar profit.", "변동성은 우리의 가장 위대한 무기입니다, 고든. 풋옵션을 현금화하고 숏 포지션을 종료해 순이익 7천만 달러를 확정 지었습니다.", "‘volatility is our greatest weapon’은 트레이딩 명작에 등장할 법한 전율의 대사입니다."),
                    ("I am glad I can go home and eat dinner.", "집에 가서 저녁 먹을 수 있어서 기쁩니다.", "긴박한 승리의 순간에 어울리지 않는 소박한 소감입니다."),
                    ("Let's do Dutch pay for the celebration dinner.", "축하 저녁은 더치페이로 계산합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "행동주의 펀드의 서한: CEO 퇴진 요구와 지분 매집 공방",
            "Gordon Sterling (Chief Investment Officer)", "📈",
            "월가 최고의 행동주의 펀드가 거대 기술기업을 상대로 CEO 퇴진과 이사회 장악을 선언했다. 당신의 펀드가 15% 지분을 쥔 채 캐스팅보트를 행사해야 한다.",
            "wield the decisive swing vote in the boardroom proxy",
            "이사회 표 대결에서 결정적인 캐스팅보트(스윙 보트)를 행사할 때 쓰는 표현입니다.",
            [
                (
                    "The activist fund needs our twelve million shares to oust the founder. The founder is on the private line offering us preferential board seats. Who do we back?",
                    "행동주의 펀드가 창업자를 축출하려면 우리 주식 1,200만 주가 필수야. 창업자는 직통 전화로 이사회 우선 의석을 주겠다고 제안해왔어. 누구 손을 들어줄 건가?",
                    "양측의 제안을 경매에 부쳐 자사주 소각과 배당 확대를 극대화하는 쪽에 표를 던지자고 하세요.",
                    ("We pit them against each other in a bidding war. The side that guarantees an immediate five-billion-dollar share buyback gets our votes.", "양측을 입찰 경쟁에 붙여 경쟁시키겠습니다. 즉각 50억 달러 자사주 매입 소각을 보장하는 쪽에 우리 표를 몰아주겠습니다.", "‘pit them against each other’와 ‘share buyback’은 주주의 이익을 극대화하는 능수능란한 협상 전략입니다."),
                    ("I like the founder because he has a good face.", "창업자 얼굴이 인상 좋아 보여서 그를 지지하고 싶습니다.", "개인적 호감으로 수천억 원의 투자를 결정하려는 한심한 발언입니다."),
                    ("The activist has high spec so let's follow him.", "행동주의 펀드 매니저 스펙이 좋으니 그를 따릅시다.", "‘spec’은 콩글리시입니다.")
                ),
                (
                    "Both sides agreed! The founder matches the buyback and the activist agrees to a standstill agreement. Our portfolio value jumped three hundred million on the news.",
                    "양쪽 다 동의했어! 창업자는 자사주 매입을 수용했고 행동주의 측은 적대 행위 중단(Standstill)에 서명했네. 우리 포트폴리오 가치가 3억 달러 폭등했어.",
                    "주가가 고점에 도달했으니 지분 30%를 블록딜로 매각해 수익을 실현하자고 하세요.",
                    ("Execute a block trade for thirty percent of our stake at the market open. We lock in the alpha before the euphoria fades.", "장 시작과 동시에 우리 지분의 30%를 블록딜로 매각하십시오. 시장의 환희가 가라앉기 전에 초과수익(알파)을 확정 짓겠습니다.", "‘execute a block trade’와 ‘lock in the alpha’는 전문 기관투자자의 수익 실현 공식입니다."),
                    ("Let's hold forever and see if it goes to heaven.", "영원히 보유하면서 주가가 천국으로 가는지 지켜봅시다.", "비이성적 과열에 취해 차익실현 기회를 놓치는 우를 범합니다."),
                    ("Our company has good skinship with the board.", "우리 회사는 이사회와 스킨십이 좋습니다.", "‘skinship’은 콩글리시입니다.")
                ),
                (
                    "Block trade executed at eighty-two dollars! The wire hit our bank. You just delivered the highest quarterly return in this fund's thirty-year history.",
                    "82달러에 블록딜 체결 완료! 매각 대금이 입금되었네. 자네가 우리 펀드 30년 역사상 최고 분기 수익률을 안겨주었어.",
                    "시장의 비효율성을 이용해 철저한 냉철함으로 승리를 쟁취했다고 답하세요.",
                    ("Markets reward ruthlessness and clarity, Gordon. We saw the leverage, played both sides, and extracted maximum shareholder value.", "시장은 냉혹함과 명확성에 보답하는 법입니다, 고든. 우리는 레버리지를 꿰뚫어 보았고, 양측을 조율해 최대 주주 가치를 뽑아냈습니다.", "월가 최고의 펀드매니저다운 카리스마 넘치는 엔딩입니다."),
                    ("I will buy a new car with my commission.", "수수료로 새 차를 사러 가겠습니다.", "가벼운 태도로 프로의 품격을 떨어뜨립니다."),
                    ("Let us do Dutch pay for the party tonight.", "오늘 밤 파티는 더치페이로 합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "글로벌 매크로 숏 포지션: 연준 금리 인상 발표 1분 전",
            "Gordon Sterling (Chief Investment Officer)", "📈",
            "연방준비제도(Fed)의 파격적인 100bp 금리 인상 발표 1분 전. 전 세계 채권과 주식이 패닉에 빠지기 직전, 10억 달러 역베팅 숏 포지션을 홀딩해야 한다.",
            "hold the billion-dollar macro short position into the rate announcement",
            "연준 금리 발표의 충격 속에서 초대형 매크로 숏 포지션을 흔들림 없이 고수할 때 쓰는 표현입니다.",
            [
                (
                    "Powell steps to the microphone in sixty seconds. Consensus says fifty basis points. Our model predicts a full one-hundred-point shock. If we're wrong, we lose a billion dollars.",
                    "파월 의장이 60초 뒤 마이크 앞에 섭니다. 시장 컨센서스는 50bp 인상입니다. 우리 모델은 100bp 전격 인상을 예측하고 있습니다. 틀리면 우리는 10억 달러를 날립니다.",
                    "데이터와 인플레이션 지표를 믿고 포지션을 단 1계약도 줄이지 말고 유지하라고 확신을 주세요.",
                    ("Hold the line, Gordon. The inflation numbers don't lie. When the Fed drops the hundred-point hammer, the bond market will crater and our short pays off.", "포지션을 사수하십시오, 고든. 인플레이션 수치는 거짓말을 하지 않습니다. 연준이 100bp 망치를 내리치는 순간 채권 시장은 붕괴하고 우리의 숏 포지션은 대박을 터뜨릴 것입니다.", "‘hold the line’과 ‘bond market will crater’는 금융 시장의 전율을 담은 대담한 화법입니다."),
                    ("I am so scared, maybe we should close half the position.", "너무 무서우니 포지션 절반을 청산하면 어떨까요.", "결정적 순간에 공포에 질려 승부를 포기하는 나약한 태도입니다."),
                    ("Did you do morning call with Powell to check?", "확인차 파월 의장과 모닝콜 해보셨습니까?", "‘morning call’은 콩글리시입니다.")
                ),
                (
                    "Statement released: Full 100 basis points! Ten-year Treasury yields spiking! Nasdaq down 600 points in three seconds! Look at the P&L monitor—it's running wild!",
                    "성명서 발표: 전격 100bp 인상! 10년물 국채 금리 폭등! 나스닥 3초 만에 600포인트 수직 낙하! 손익 모니터를 보세요, 숫자가 미친 듯이 올라갑니다!",
                    "침착하게 분할 익절 주문을 체결하고 통화 스왑 시장으로 이익을 확정하라고 지시하세요.",
                    ("Begin phased limit-order profit-taking right now! Lock in two hundred million on index futures and shift collateral into overnight reverse repos!", "지금 즉시 단계별 지정가 익절 주문을 체결하세요! 지수 선물에서 2억 달러를 확정하고 담보를 익일 역레포로 전환하십시오!", "‘phased limit-order profit-taking’과 ‘reverse repos’는 금융 대공황 속 침착한 자산 관리의 정석입니다."),
                    ("Let's scream and jump around the office!", "사무실에서 소리 지르고 방방 뜁시다!", "프로 트레이딩 룸에 걸맞지 않은 미성숙한 소란입니다."),
                    ("Tell the secretary to bring coffee for after service.", "비서에게 애프터 서비스로 커피를 가져오라고 하세요.", "‘after service’는 콩글리시입니다.")
                ),
                (
                    "Market closed. Net daily profit: four hundred and thirty million dollars. You just executed the Big Short of the decade. Walk out that door with your head high.",
                    "장 마감. 오늘 하루 순이익: 4억 3천만 달러(약 5,800억 원). 자네가 방금 이 10년 만의 가장 위대한 ‘빅 숏’을 집행했네. 당당히 고개를 들고 나가게.",
                    "탐욕이 아닌 통찰력으로 시장의 진실을 증명해냈다고 품격 있게 대답하세요.",
                    ("It wasn't a gamble, Gordon. It was recognizing mathematical inevitability before the herd woke up. See you at tomorrow's opening bell.", "도박이 아니었습니다, 고든. 대중들이 잠에서 깨어나기 전에 수학적 필연성을 꿰뚫어 본 것뿐입니다. 내일 개장 벨 때 뵙겠습니다.", "전설적인 매크로 트레이더의 역대급 클로징 대사입니다."),
                    ("I will go buy ten Rolex watches right now.", "지금 당장 롤렉스 시계 10개를 사러 가겠습니다.", "졸부의 유치함을 드러내는 발언입니다."),
                    ("Let's do Dutch pay for the victory beer tonight.", "오늘 승리의 맥주는 더치페이로 마십시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    return data
