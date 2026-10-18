# -*- coding: utf-8 -*-
"""
Generator for scripts/clusters/cluster_c.py (Genres 12 to 20: 9 genres x 4 = 36 episodes)
"""
import os

content = '''# -*- coding: utf-8 -*-
"""
Dramactor Scenario Cluster C (Genres 12 to 20: 9 genres x 4 cycles = 36 episodes)
12: Sports Agency & Free Agency
13: Haute Couture Fashion
14: Crisis PR Management
15: Luxury Real Estate
16: Hollywood Talent Agency
17: 5-Star Hotel Hospitality
18: Fine Art Auction & Heist
19: Investigative Journalism
20: Cyber Crime & Zero-Day Hacking
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_cluster_c_scenarios():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # 12. Sports Agency & Free Agency
    data["Sports Agency & Free Agency"] = [
        mk_ep(
            "메이저리그 FA 마감 5분 전: 3억 달러 초대형 계약",
            "Jerry Maguire (Super Agent)", "🏈",
            "윈터 미팅 마감 직전 호텔 스위트룸. 올스타 홈런 타자의 몸값을 두고 뉴욕 양키스와 LA 다저스가 전면 입찰 경쟁을 벌인다. 전구단 트레이드 거부권을 관철해야 한다.",
            "secure a full no-trade clause in the mega-deal",
            "초대형 FA 계약에서 구단의 일방적 트레이드를 차단하는 전구단 거부권을 쟁취할 때 쓰는 표현입니다.",
            [
                ("Yankees offer ten years at three hundred million, but they refuse the full no-trade clause. Dodgers offer 290 with opt-outs. Deadline in three minutes. What's the play?",
                 "양키스가 10년 3억 달러를 불렀지만 전구단 트레이드 거부권은 못 주겠대. 다저스는 옵트아웃 포함 2억 9천을 불렀어. 마감 3분 전이야. 결정은?",
                 "다저스의 옵트아웃 카드로 양키스를 압박해 전구단 트레이드 거부권을 최종 관철하자고 하세요.",
                 ("Call Cashman back. Tell him the Dodgers just sweetened their signing bonus. Either he gives us the full no-trade clause right now, or my client signs in LA.", "캐시먼 단장에게 전화 거세요. 다저스가 계약금을 올렸다고 전하십시오. 지금 당장 전구단 트레이드 거부권을 주지 않으면 내 의뢰인은 LA와 도장 찍습니다.", "‘full no-trade clause’와 ‘signs in LA’는 양키스를 굴복시키는 최고의 에이전트 화법입니다."),
                 ("Let's sign for less money so everyone is friendly.", "모두가 친해지도록 돈을 덜 받고 서명합시다.", "선수의 시장 가치를 헐값에 넘기는 프로답지 못한 태도입니다."),
                 ("The contract has bad spec so let's call AS.", "계약서 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                ("Yankees caved! Full no-trade clause granted! But now their team doctor is flagging my client's right shoulder MRI from three years ago. They want a discount.",
                 "양키스가 굴복했어! 트레이드 거부권 승인! 그런데 구단 의사가 3년 전 오른쪽 어깨 MRI를 문제 삼으며 몸값 할인을 요구하고 있어.",
                 "독립 전문의의 무결점 완치 소견서를 테이블에 던지며 단 1달러의 삭감도 없음을 못 박으세요.",
                 ("Throw Dr. Andrews' independent clearance on the table. My client pitched two hundred innings with zero pain. The three hundred million is fully guaranteed, non-negotiable.", "앤드루스 박사의 독립 소견서를 테이블에 던지십시오. 내 의뢰인은 무통증으로 200이닝을 던졌습니다. 3억 달러 전액 보장이며 타협은 없습니다.", "‘fully guaranteed’와 ‘non-negotiable’은 메이저리그 연봉 협상의 절대 원칙입니다."),
                 ("We can give them fifty percent discount for safety.", "안전을 위해 50% 할인해 줄 수도 있습니다.", "치명적인 손실을 부르는 무능한 협상입니다."),
                 ("Let's send an SNS post to shame the doctor.", "의사를 망신주기 위해 SNS 글을 올립시다.", "‘SNS’는 콩글리시입니다.")),
                ("Contract signed! Breaking news flashes on ESPN: Three hundred million fully guaranteed! You just reset the entire sports market, Jerry.",
                 "계약 체결! ESPN 속보 타전: 3억 달러 전액 보장! 자네가 메이저리그 스포츠 시장의 판도를 완전히 바꿨네, 제리.",
                 "선수의 가치를 믿고 끝까지 싸우는 것이 에이전트의 사명이라고 답하세요.",
                 ("Show me the money isn't just about cash, Jerry—it's about demanding every ounce of respect your athlete bled for. Deal done.", "‘Show me the money’는 단순한 돈이 아닙니다. 내 선수가 흘린 피와 땀에 걸맞은 모든 존중을 요구하는 것입니다. 계약 완료했습니다.", "영화 제리 맥과이어의 명대사를 승화시킨 최고의 피날레입니다."),
                 ("I am glad we don't have to talk to the coach.", "감독과 이야기 안 해도 돼서 참 좋습니다.", "선수와 구단 간의 신뢰를 무시하는 발언입니다."),
                 ("Let's do Dutch pay for the steak dinner tonight.", "오늘 밤 스테이크는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "슈퍼볼 MVP 라커룸 불화: 프랜차이즈 태그 거부",
            "Jerry Maguire (Super Agent)", "🏈",
            "NFL 프리시즌 트레이닝 캠프. 슈퍼볼 MVP 쿼터백이 구단의 일방적인 프랜차이즈 태그 지정에 반발하며 훈련 보이콧을 선언했다. 구단주와 담판을 벌여 다년 연장 계약을 이끌어내야 한다.",
            "demand a record-breaking long-term contract extension",
            "선수의 프랜차이즈 가치를 인정받아 역대 최고액 다년 연장 계약을 쟁취할 때 쓰는 표현입니다.",
            [
                ("Owner says if my quarterback doesn't report to camp tomorrow morning, he fines him fifty thousand a day and activates the backup. Do we report?",
                 "구단주는 내 쿼터백이 내일 아침 캠프에 불참하면 하루 5만 달러 벌금을 물리고 백업을 주전으로 올리겠대. 캠프에 들어갈까?",
                 "벌금 협박에 굴하지 말고 백업 쿼터백으로는 개막전 전패라는 냉혹한 현실을 각인시키세요.",
                 ("Stay home. Remind the owner that without our MVP under center, their opening month is zero and four and their season tickets will crater.", "집에 머무르십시오. 우리 MVP 쿼터백 없이 센터에 서면 개막 첫 달 4연패로 시즌권 판매가 바닥칠 거라는 현실을 상기시키세요.", "‘under center’와 ‘season tickets will crater’는 구단주의 급소를 찌르는 강력한 레버리지입니다."),
                 ("Tell the quarterback to say sorry to the owner.", "쿼터백에게 구단주에게 사과하라고 하세요.", "선수의 협상력을 완전히 말아먹는 굴욕적인 처사입니다."),
                 ("The quarterback has bad manner so let's scold him.", "쿼터백이 매너가 나쁘니 혼냅시다.", "‘manner’는 콩글리시입니다.")),
                ("Owner is sweating. He called a private meeting at his yacht. He offers four years at two hundred million, but only half is guaranteed. What's the counter?",
                 "구단주가 식은땀을 흘리며 요트에서 비밀 회동을 제안했어. 4년 2억 달러를 제안했지만 보장액은 절반뿐이야. 반격 제안은?",
                 "첫 3년 전액 1억 6천만 달러 보장과 부상 면책 특약을 넣지 않으면 계약서에 사인하지 않겠다고 못 박으세요.",
                 ("One hundred sixty million fully guaranteed over the first three years, plus injury protection. Take it or watch your stadium sit empty on opening Sunday.", "첫 3년 동안 1억 6천만 달러 전액 보장과 부상 보호 특약을 넣으십시오. 받든지, 아니면 개막전 일요일 텅 빈 경기장을 보시든지요.", "‘injury protection’과 ‘empty stadium’은 구단주의 고집을 꺾는 승부수입니다."),
                 ("Half guarantee is okay, maybe we can buy nice cars.", "절반 보장도 괜찮으니 멋진 차나 살 수 있겠네요.", "프로 스포츠의 냉혹한 부상 위험을 간과한 무책임한 생각입니다."),
                 ("Check the handphone for the owner's message.", "구단주 메시지를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Owner signed the papers! One hundred sixty million guaranteed! My quarterback just showed up to practice in a helicopter! The city is going wild!",
                 "구단주가 계약서에 서명했어! 1억 6천만 달러 전액 보장! 내 쿼터백이 방금 헬기를 타고 훈련장에 나타났네! 온 도시가 열광하고 있어!",
                 "챔피언에게 걸맞은 대우를 쟁취해냈으니 이제 슈퍼볼 트로피로 증명하자고 화답하세요.",
                 ("We got the bag, Jerry; now let's go deliver the Lombardi Trophy. Respect earned, deal sealed.", "원하는 대우를 쟁취했습니다, 제리. 이제 빈스 롬바디 트로피를 가져올 시간입니다. 존중을 얻었고, 계약은 성사되었습니다.", "NFL 에이전트의 승리를 상징하는 통쾌한 피날레입니다."),
                 ("I am glad we don't have to watch football now.", "이제 미식축구 안 봐도 돼서 참 좋습니다.", "스포츠 에이전트의 열정이 전혀 느껴지지 않는 답변입니다."),
                 ("Let's do Dutch pay for the tailgate beer.", "경기장 파티 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "NBA 맥스 계약 담판: 신발 브랜드 스폰서십 전쟁",
            "Jerry Maguire (Super Agent)", "🏈",
            "나이키 글로벌 본사 이사회실. NBA 신인왕 가드의 맥스 연장 계약과 함께 1억 달러 규모 시그니처 농구화 라인 론칭을 두고 나이키와 아디다스가 입찰 전쟁을 벌인다.",
            "negotiate an unprecedented signature shoe equity stake",
            "단순 후원을 넘어 신발 매출 지분을 포함한 전례 없는 시그니처 라인 계약을 이끌어낼 때 쓰는 표현입니다.",
            [
                ("Nike offers eighty million over five years, but zero equity in the shoe line. Adidas offers ninety with five percent royalties. Nike wants an answer in ten minutes.",
                 "나이키가 5년 8천만 달러를 제안했지만 브랜드 지분은 0%래. 아디다스는 5% 로열티 포함 9천만을 불렀어. 나이키가 10분 내 답변을 요구하네.",
                 "나이키에 아디다스의 로열티 조항을 제시하며 조던 브랜드 수준의 독립 서브 라벨 지분을 요구하세요.",
                 ("Match Adidas's five percent royalty and grant him his own standalone apparel imprint, or we walk into the German headquarters tomorrow morning.", "아디다스의 5% 로열티를 맞추고 그에게 독자적인 의류 서브 레이블을 부여하십시오. 그렇지 않으면 내일 아침 아디다스 독일 본사로 걸어 들어갑니다.", "‘standalone apparel imprint’와 ‘or we walk’는 나이키의 독점을 깨부수는 강력한 압박입니다."),
                 ("Just sign whatever Nike gives us because the swoosh is cool.", "스우시 로고가 멋있으니 나이키가 주는 대로 그냥 사인합시다.", "선수의 브랜드 가치를 수천억 원 날려먹는 무지한 처사입니다."),
                 ("The shoe has bad spec so tell the designer.", "신발 스펙이 안 좋으니 디자이너에게 말합시다.", "‘spec’은 콩글리시입니다.")),
                ("Nike matched the royalty and gave him the imprint! But they're demanding a twenty-game minimum clause to trigger the bonus. What's our response?",
                 "나이키가 로열티를 맞추고 독자 레이블까지 줬어! 그런데 보너스 발동 조건으로 최소 20경기 출전 조항을 요구하고 있어.",
                 "출전 경기 수 대신 올스타 투표 및 소셜 미디어 임팩트 지표로 대체하자고 협상하세요.",
                 ("No injury penalties. Tie the incentives to All-NBA team honors and global jersey sales, not mechanical games-played thresholds.", "부상에 따른 불이익 조항은 거부합니다. 인센티브를 단순 경기 수가 아니라 올-NBA 팀 선정과 글로벌 유니폼 판매량에 연동하십시오.", "‘All-NBA honors’와 ‘jersey sales’는 선수의 부상 위험을 방어하는 영리한 조항 설계입니다."),
                 ("Tell Nike we will never play basketball if they are mean.", "나이키가 짓궂게 굴면 농구 절대 안 하겠다고 전하세요.", "프로답지 못한 어린아이 투정입니다."),
                 ("Please check your handphone for shoe photos.", "신발 사진을 보려고 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")),
                ("Deal signed! One hundred million plus signature royalties! The billboard in Times Square just lit up with his face! You created a global icon, Jerry.",
                 "계약 체결! 1억 달러에 시그니처 로열티까지! 타임스퀘어 전광판에 선수의 얼굴이 환하게 켜졌네! 자네가 글로벌 아이콘을 탄생시켰어, 제리.",
                 "위대한 선수는 경기장에서 뛰지만, 전설은 역사와 브랜드 속에서 영원히 산다고 답하세요.",
                 ("Athletes play the game, Jerry, but legends transcend the culture. We just etched his name in sneaker history.", "선수는 경기를 뛰지만, 전설은 문화를 초월합니다, 제리. 우리는 방금 그의 이름을 스니커즈 역사에 새겨 넣었습니다.", "글로벌 비즈니스의 정점에 선 에이전트의 찬사입니다."),
                 ("I am happy we can get some free shoes now.", "이제 공짜 신발을 좀 얻을 수 있어서 기쁩니다.", "1억 달러 딜의 무게감을 떨어뜨리는 소박한 소리입니다."),
                 ("Let's do Dutch pay for the victory dinner.", "축하 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "유럽 축구 슈퍼스타 이적 마감일: 자정의 팩스 등록",
            "Jerry Maguire (Super Agent)", "🏈",
            "런던 프리미어리그 본부. 유럽 축구 이적 시장 마감 15분 전, 레알 마드리드와 맨체스터 유나이티드 사이의 1억 2천만 유로 이적 팩스가 통신 오류로 지연되고 있다. 마감 전 승인을 완료해야 한다.",
            "push through the transfer registration before the deadline window closes",
            "이적 시장 마감 시한 직전 팩스 등록과 승인 절차를 긴급 완수할 때 쓰는 표현입니다.",
            [
                ("Fifteen minutes until midnight! The international transfer matching system is lagging! Real Madrid says their paperwork hasn't registered in Madrid. What do we do?",
                 "자정까지 15분! 국제 이적 승인 시스템(TMS) 서버가 버벅거리고 있어! 레알 마드리드는 마드리드 협회에 서류가 안 떴다고 난리야. 어떻게 하지?",
                 "FIFA 긴급 핫라인을 통해 거래 타결 확인서(Deal Sheet)를 제출해 2시간 연장 승인을 확보하라고 지시하세요.",
                 ("File the signed Premier League Deal Sheet immediately! That grants an automatic two-hour extension while we manually push the TMS clearance through FIFA.", "서명된 프리미어리그 '딜 시트'를 즉시 제출하십시오! 그러면 수동으로 FIFA 승인을 받는 동안 2시간의 자동 연장 효력이 발생합니다.", "‘Deal Sheet’와 ‘TMS clearance’는 유럽 축구 이적 마감일의 생사를 가르는 절대 규정입니다."),
                 ("Let's cry and ask FIFA to change the rule.", "울면서 FIFA에 규칙을 바꿔달라고 애원합시다.", "아무런 효력이 없는 어리석은 태도입니다."),
                 ("The computer has bad spec so buy a new one.", "컴퓨터 스펙이 안 좋으니 새것을 사 오세요.", "‘spec’은 콩글리시입니다.")),
                ("Deal Sheet accepted! We have the two-hour window. But the player's previous club is refusing to release his image rights without a five-million payoff.",
                 "딜 시트 접수 완료! 2시간의 여유를 벌었어. 그런데 선수의 전 소속팀이 5백만 유로의 초상권 정산금을 주지 않으면 서명을 거부하겠대.",
                 "구매 구단과 판매 구단의 이적료 정산 조항에서 차감 처리하도록 중재안을 내놓아 분쟁을 즉시 종결시키세요.",
                 ("Offset the five million against their future sell-on clause. Neither side loses cash tonight, and the transfer clears within five minutes.", "그 5백만을 향후 재판매(Sell-on) 지분 조항에서 상계 처리하십시오. 오늘 밤 누구도 현금을 잃지 않고 5분 안에 이적이 성사됩니다.", "‘sell-on clause’와 ‘offset’은 복잡한 이적료 분쟁을 단칼에 정리하는 명쾌한 솔루션입니다."),
                 ("Tell the player to fight with his old club on the street.", "선수에게 길거리에서 전 소속팀과 싸우라고 하세요.", "선수의 품위를 깎아내리는 유치한 발언입니다."),
                 ("Let's send an SNS post to shame the club president.", "구단주를 망신주기 위해 SNS 글을 올립시다.", "‘SNS’는 콩글리시입니다.")),
                ("FIFA approved the transfer! White smoke from the Bernabéu! One hundred twenty million euro transfer complete! He's the new number ten in Madrid!",
                 "FIFA 이적 최종 승인! 베르나베우에 백색 연기가 피어올랐어! 1억 2천만 유로 이적 완료! 그가 마드리드의 새로운 10번이야!",
                 "마감 1초 전까지 포기하지 않는 열정이 불가능한 이적을 기적으로 만든다고 답하세요.",
                 ("A transfer window isn't won with polite emails, Jerry—it's seized in the dying seconds through sheer relentless will. Welcome to Madrid.", "이적 시장은 정중한 이메일로 이기는 것이 아닙니다. 끈질긴 의지로 마지막 1초에 낚아채는 것입니다. 마드리드에 오신 것을 환영합니다.", "유럽 축구 드라마의 정수를 보여주는 멋진 피날레입니다."),
                 ("I am glad we can sleep until noon tomorrow.", "내일 정오까지 잘 수 있어서 참 좋습니다.", "세계적 이적 성공의 순간에 긴장을 너무 일찍 풉니다."),
                 ("Let's do Dutch pay for the tapas beer tonight.", "오늘 밤 타파스 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    return data
'''

with open("scripts/clusters/cluster_c.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Created cluster_c.py successfully.")

