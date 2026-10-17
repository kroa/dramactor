# -*- coding: utf-8 -*-
"""
Builder for scripts/clusters/group_c.py
Generates Genres 12 to 21 (10 genres x 4 = 40 episodes)
"""
import sys
import os

content = '''# -*- coding: utf-8 -*-
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_group_c_scenarios():
    data = {}
    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # 12. Sports Agency & Free Agency
    data["Sports Agency & Free Agency"] = [
        mk_ep(
            "메이저리그 FA 마감 5분 전: 3억 달러 초대형 계약", "Jerry Maguire (Super Agent)", "🏈",
            "윈터 미팅 마감 직전 호텔 스위트룸. 올스타 홈런 타자의 몸값을 두고 뉴욕 양키스와 LA 다저스가 전면 입찰 경쟁을 벌인다. 전구단 트레이드 거부권을 관철해야 한다.",
            "secure a full no-trade clause in the mega-deal", "초대형 FA 계약에서 구단의 일방적 트레이드를 차단하는 전구단 거부권을 쟁취할 때 쓰는 표현입니다.",
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
            "슈퍼볼 MVP 라커룸 불화: 프랜차이즈 태그 거부", "Jerry Maguire (Super Agent)", "🏈",
            "NFL 프리시즌 트레이닝 캠프. 슈퍼볼 MVP 쿼터백이 구단의 일방적인 프랜차이즈 태그 지정에 반발하며 훈련 보이콧을 선언했다. 구단주와 담판을 벌여 다년 연장 계약을 이끌어내야 한다.",
            "demand a record-breaking long-term contract extension", "선수의 프랜차이즈 가치를 인정받아 역대 최고액 다년 연장 계약을 쟁취할 때 쓰는 표현입니다.",
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
            "NBA 맥스 계약 담판: 신발 브랜드 스폰서십 전쟁", "Jerry Maguire (Super Agent)", "🏈",
            "나이키 글로벌 본사 이사회실. NBA 신인왕 가드의 맥스 연장 계약과 함께 1억 달러 규모 시그니처 농구화 라인 론칭을 두고 나이키와 아디다스가 입찰 전쟁을 벌인다.",
            "negotiate an unprecedented signature shoe equity stake", "단순 후원을 넘어 신발 매출 지분을 포함한 전례 없는 시그니처 라인 계약을 이끌어낼 때 쓰는 표현입니다.",
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
            "유럽 축구 슈퍼스타 이적 마감일: 자정의 팩스 등록", "Jerry Maguire (Super Agent)", "🏈",
            "런던 프리미어리그 본부. 유럽 축구 이적 시장 마감 15분 전, 레알 마드리드와 맨체스터 유나이티드 사이의 1억 2천만 유로 이적 팩스가 통신 오류로 지연되고 있다. 마감 전 승인을 완료해야 한다.",
            "push through the transfer registration before the deadline window closes", "이적 시장 마감 시한 직전 팩스 등록과 승인 절차를 긴급 완수할 때 쓰는 표현입니다.",
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

    # 13. Haute Couture Fashion
    data["Haute Couture Fashion"] = [
        mk_ep(
            "파리 패션위크 런웨이 드레스 파손 위기", "Miranda Priestly (Editor-in-Chief)", "👗",
            "파리 그랑팔레 백스테이지. 런웨이 시작 3분 전 메인 피날레 오트 쿠튀르 실크 드레스가 찢어졌다. 미란다 프리슬리의 날카로운 시선 앞에서 즉석 바이어스 컷 드레이핑으로 기적을 일으켜야 한다.",
            "drape the silk bias cut under extreme backstage pressure", "극도의 백스테이지 압박 속에서 원단을 바이어스 재단으로 즉석 드레이핑해 예술품으로 승화시킬 때 쓰는 패션 전문 표현입니다.",
            [
                ("Three minutes until the finale march! The zipper tore right through the vintage chantilly lace! Miranda is glaring at the curtain! Do we pull the look or fix it?",
                 "피날레 행진까지 3분! 지퍼가 빈티지 샹티이 레이스를 찢고 튀어나왔어! 미란다가 커튼 너머로 매섭게 노려보고 있어! 룩을 뺄까, 고칠까?",
                 "룩을 빼지 말고 남은 실크 태피터를 바이어스 방향으로 즉석 핀 드레이핑해 아방가르드 비대칭 룩으로 재탄생시키라고 지시하세요.",
                 ("Do not pull the look! Grab the emerald silk taffeta and drape it on the bias with hidden pearl pins. We turn a tear into couture asymmetry!", "룩을 빼지 마세요! 에메랄드 실크 태피터를 가져와 진주 핀으로 바이어스 방향 드레이핑하십시오. 찢어진 흠을 쿠튀르 비대칭의 미학으로 바꿉니다!", "‘drape on the bias’와 ‘couture asymmetry’는 패션계의 위기를 천재성으로 승화시키는 언어입니다."),
                 ("Let's use glue to stick the dress together quickly.", "풀을 써서 드레스를 대충 붙여봅시다.", "런웨이 조명 아래서 옷이 떨어져 나가 국제적 망신을 부릅니다."),
                 ("The dress has bad spec so call the factory.", "드레스 스펙이 안 좋으니 공장에 전화합시다.", "‘spec’은 콩글리시입니다.")),
                ("The drape holds! But the supermodel refuses to step out without a matching headpiece. The house music is fading. You have fifteen seconds.",
                 "드레이핑이 버텨줬어! 하지만 톱모델이 어울리는 헤드피스 없이는 런웨이에 안 나가겠다고 버텨. 하우스 음악이 잦아들고 있어. 15초 남았네.",
                 "무대 조화 장식에서 흑장미를 꺾어 즉석에서 그녀의 올림머리에 꽂아 치명적인 드라마를 완성하세요.",
                 ("Snap the midnight rose from the floral centerpiece. Pin it into her chignon. Tell her she's not a model tonight—she's an empress claiming her crown.", "화훼 센터피스에서 흑장미를 꺾어 그녀의 시뇽 헤어에 꽂으십시오. 오늘 밤 모델이 아니라 왕관을 되찾는 여제처럼 걸으라고 하세요.", "‘chignon’과 ‘empress claiming her crown’은 모델의 런웨이 카리스마를 폭발시키는 연출입니다."),
                 ("Tell the model that crying makes her face ugly.", "모델에게 울면 얼굴 못생겨진다고 타일러봅시다.", "긴장한 모델을 더 패닉에 빠뜨리는 말입니다."),
                 ("Let's give her a candy for skinship.", "스킨십을 위해 사탕을 하나 쥐여줍시다.", "‘skinship’은 콩글리시입니다.")),
                ("Standing ovation from the front row! Anna Wintour smiled, and Miranda nodded once—which means you just conquered Paris. The collection is sold out.",
                 "프런트 로 전원 기립박수! 애나 윈투어가 미소를 지었고, 미란다가 고개를 한 번 끄덕였어. 이건 자네가 파리를 정복했다는 뜻이야. 전 컬렉션 완판이야.",
                 "진정한 쿠튀르는 완벽함이 아니라 치명적인 흠결조차 예술로 바꾸는 용기에서 탄생한다고 답하세요.",
                 ("Haute couture isn't about rigid perfection, Miranda—it's breathing life into fabric when disaster strikes. That's fashion.", "오트 쿠튀르는 경직된 완벽함이 아닙니다, 미란다. 재앙이 닥쳤을 때조차 원단에 생명을 불어넣는 용기입니다. 그것이 패션입니다.", "악마는 프라다를 입는다의 정점을 찍는 명대사입니다."),
                 ("I am glad we can take off our high heels now.", "이제 하이힐을 벗을 수 있어서 참 좋습니다.", "위대한 승리의 품격을 깎아먹는 소리입니다."),
                 ("Let's do Dutch pay for the Paris champagne.", "파리 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "밀라노 아틀리에: 적대적 명품 그룹 인수 거부", "Miranda Priestly (Editor-in-Chief)", "👗",
            "밀라노 유서 깊은 패션 하우스 본점. 프랑스 거대 럭셔리 복합 기업이 브랜드 인수를 시도하며 크리에이티브 디렉터 교체를 요구한다. 가문의 장인 정신과 독립성을 사수해야 한다.",
            "reject the hostile luxury buyout and protect creative autonomy", "상업적 거대 자본의 적대적 인수를 거부하고 크리에이티브 자율성을 지켜낼 때 쓰는 표현입니다.",
            [
                ("The French conglomerate bought forty-nine percent of our stock. Their CEO is at our showroom door demanding we fire our master tailors and offshore production to cut costs.",
                 "프랑스 명품 그룹이 우리 지분 49%를 사들였어. 그들의 CEO가 쇼룸 문앞에 서서 원가 절감을 위해 장인들을 해고하고 해외 공장으로 이전하라고 요구하고 있네.",
                 "타협 없는 수작업 장인정신이 우리 브랜드의 무형자산이자 유일한 가치임을 선언하며 제안을 일축하세요.",
                 ("Inform them our valuation rests entirely on handmade artisanal integrity. We do not dilute sixty years of heritage to please quarterly balance sheets.", "우리 브랜드의 기업 가치는 오직 장인들의 수작업 진실성에 기반한다고 전하십시오. 분기별 재무제표를 맞추기 위해 60년의 헤리티지를 희석할 생각은 추호도 없습니다.", "‘artisanal integrity’와 ‘dilute sixty years of heritage’는 자본주의의 횡포를 제압하는 패션 철학입니다."),
                 ("Let us agree to fire half the workers to be nice.", "좋은 게 좋은 거니 노동자 절반만 해고하는 데 동의합시다.", "브랜드의 정체성을 파괴하고 영혼을 파는 행위입니다."),
                 ("The CEO has bad manner so let's claim to him.", "CEO가 매너가 나쁘니 그에게 클레임합시다.", "‘manner’와 ‘claim’은 콩글리시입니다.")),
                ("They're threatening a hostile tender offer to cross fifty percent. They brought three billionaire private equity bankers to force our board's signature.",
                 "그들이 50%를 넘기기 위해 적대적 공개매수를 협박하고 있어. 이사회 서명을 강요하기 위해 억만장자 사모펀드 금융가 3명을 대동했네.",
                 "이탈리아 장인 보존 국립 재단과 백기사 동맹을 결성해 문화유산 보호법으로 지분을 동결시키자고 제안하세요.",
                 ("Activate the poison pill clause and partner with the Italian Cultural Heritage Trust. We designate our atelier a national treasure and freeze their voting rights.", "포이즌 필 조항을 가동하고 이탈리아 문화유산 신탁과 제휴하십시오. 우리 아틀리에를 국가 문화재로 지정해 그들의 의결권을 전면 동결시킵니다.", "‘poison pill clause’와 ‘cultural heritage trust’는 거대 자본의 인수를 차단하는 완벽한 법적 방패입니다."),
                 ("Tell the bankers to go away because we are tired.", "우리가 피곤하니 은행가들에게 그냥 가라고 하세요.", "기업 경영권 분쟁에서 아무런 효력이 없는 말입니다."),
                 ("Please check your handphone for stock prices.", "주가를 보려고 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")),
                ("Tender offer collapsed! Conglomerate surrendered and sold their stake back at a discount! Our master tailors are weeping with joy! You saved the soul of Milan.",
                 "공개매수 무산! 명품 그룹이 굴복하고 보유 지분을 할인 매각하고 철수했어! 우리 장인들이 기쁨의 눈물을 흘리고 있네! 자네가 밀라노의 영혼을 구했어.",
                 "진정한 럭셔리는 돈으로 살 수 없는 장인의 영혼에 깃들어 있다고 당당히 선언하세요.",
                 ("Luxury is not mass-produced in a spreadsheet, Miranda—it is carved by human hands that revere the craft. Our heritage stands unconquered.", "럭셔리는 엑셀 파일에서 대량 생산되지 않습니다, 미란다. 장인정신을 경외하는 인간의 손끝에서 조각되는 것입니다. 우리의 헤리티지는 꺾이지 않았습니다.", "명품 하우스의 존엄을 지켜낸 감동적인 피날레입니다."),
                 ("I am glad we don't have to work on weekends.", "주말에 일 안 해도 돼서 참 좋습니다.", "숭고한 승리의 여운을 반감시키는 답변입니다."),
                 ("Let's do Dutch pay for the Milanese risotto.", "밀라노 리소토는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "멧 갈라 레드카펫: 세기의 커스텀 드레스 독점 공개", "Miranda Priestly (Editor-in-Chief)", "👗",
            "뉴욕 메트로폴리탄 미술관 계단 앞. 전 세계 카메라가 집중된 멧 갈라 레드카펫. 톱 여배우가 입기로 한 드레스의 3미터 트레인이 리무진 문에 걸려 찢어지는 사고가 발생했다. 즉각적인 재단으로 스포트라이트를 되찾아야 한다.",
            "transform the ruined train into an architectural masterpiece on the stairs", "망가진 드레스 트레인을 현장에서 즉시 잘라내어 계단 위 조형적 걸작으로 재탄생시킬 때 쓰는 표현입니다.",
            [
                ("The limousine door crushed the organza train! Shredded beyond repair! The red carpet coordinator is counting down twenty seconds until her walk! What's the call?",
                 "리무진 문이 오간자 트레인을 짓이겨버렸어! 복구 불가능하게 찢어졌어! 레드카펫 코디네이터가 입장 20초 카운트다운을 세고 있어! 결단은?",
                 "가위를 들어 찢어진 3미터 트레인을 과감히 잘라내고 건축학적 미니드레스와 드라마틱 베일로 즉석 전환하라고 명령하세요.",
                 ("Hand me the shears! Sever the train at the hip and balloon the under-skirt with structural tulle. We turn a ruined gown into the boldest architectural silhouette on that carpet!", "가위 이리 주세요! 골반 선에서 트레인을 단칼에 잘라내고 구조적 튤로 언더스커트를 부풀리십시오. 망가진 드레스를 오늘 밤 레드카펫 최고의 조형적 실루엣으로 바꿉니다!", "‘sever the train’과 ‘architectural silhouette’은 패션계의 대담한 결단을 보여주는 프로페셔널한 지시입니다."),
                 ("Let's tell her to crawl on the stairs so no one sees it.", "아무도 못 보게 계단을 기어가라고 여배우에게 말합시다.", "스타의 커리어를 끝장내는 끔찍한 조언입니다."),
                 ("The fabric has bad spec so tell the driver.", "원단 스펙이 안 좋으니 운전기사에게 따집시다.", "‘spec’은 콩글리시입니다.")),
                ("She stepped onto the carpet! Flashbulbs exploding! But the fashion critics on live television are debating whether the raw hem was intentional. They're waiting for her quote.",
                 "여배우가 카펫에 올랐어! 플래시가 폭발하고 있어! 하지만 생방송 패션 비평가들이 거친 밑단이 의도된 연출인지 논쟁하고 있어. 그녀의 인터뷰 한마디를 기다려.",
                 "원초적 해체주의와 자유의 선언이라는 완벽한 인터뷰 멘트를 여배우의 인이어로 속삭여주세요.",
                 ("Feed this line to her earpiece: 'True glamour doesn't conform to hem lines—it liberates the woman within.' Watch every camera zoom in.", "인이어로 이 대사를 넣어주십시오: '진정한 글래머는 밑단 규칙에 갇히지 않습니다. 그 안의 여성을 해방할 뿐입니다.' 모든 카메라가 줌인하는 것을 보게 될 것입니다.", "‘liberates the woman within’은 전 세계 패션 매거진 1면을 장식할 전설적인 인터뷰 워딩입니다."),
                 ("Tell her to say the dress was very cheap.", "드레스가 아주 싼 거였다고 말하라고 하세요.", "모든 스폰서 브랜드를 파멸시키는 자폭 발언입니다."),
                 ("Let's send an SNS post to explain the mistake.", "실수를 해명하기 위해 SNS 글을 올립시다.", "‘SNS’는 콩글리시입니다.")),
                ("Vogue declared her Best Dressed of the decade! The internet crashed with ten million shares in sixty minutes! Miranda looked at you and didn't scoff—you made history.",
                 "보그가 그녀를 지난 10년 통틀어 베스트 드레서로 선정했어! 60분 만에 1,000만 회 공유되며 인터넷이 마비되었네! 미란다가 자네를 보고 비웃지 않았어. 자네가 역사를 쓴 거야.",
                 "위대한 패션은 두려움 없는 도전 속에서만 불멸의 빛을 발한다고 답하세요.",
                 ("Glamour is nothing without boldness, Miranda. When you dare to break the mold on the world's biggest stage, eternity remembers.", "대담함이 결여된 글래머는 아무것도 아닙니다, 미란다. 세계 최대의 무대에서 틀을 깨뜨릴 용기가 있을 때, 영원은 그 이름을 기억합니다.", "패션 제국의 정점에서 나누는 완벽한 대화입니다."),
                 ("I am glad we don't have to carry scissors anymore.", "이제 가위 안 들고 다녀도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                 ("Let's do Dutch pay for the after-party martini.", "애프터 파티 마티니는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "보그 9월호 커버 모델 교체: 패션 제국의 왕좌 승계", "Miranda Priestly (Editor-in-Chief)", "👗",
            "보그 본사 편집장 오피스. 패션계 1년 중 가장 중요한 9월호 인쇄 마감 24시간 전. 예정된 할리우드 톱스타가 스캔들에 휩싸이자, 미란다가 커버 사진을 전면 폐기하고 무명의 신예로 교체할 것을 제안한다.",
            "gamble the entire September Issue on an unknown visionary face", "보그 9월호라는 패션계 최고 권력의 커버를 파격적인 신예로 승부수를 띄울 때 쓰는 표현입니다.",
            [
                ("The publisher is on the phone screaming! Pulling the A-list actress will cost us four million in prepaid luxury ad pages! Do we publish her anyway or pull the trigger?",
                 "발행인이 전화로 고함을 지르고 있어! A급 여배우를 빼면 선지급된 4백만 달러 명품 광고가 날아간다고! 그녀를 그대로 인쇄할까, 아니면 교체를 단행할까?",
                 "안전한 타협은 보그의 사망 선고이므로 무명의 아프리카 신예 모델을 세워 패션의 미래를 선도하자고 미란다를 설득하세요.",
                 ("Publishing a tainted starlet turns Vogue into a supermarket tabloid. We pull the cover and put the Sudanese refugee prodigy on the front. We don't follow culture—we decree it.", "오점을 남긴 스타를 싣는 순간 보그는 슈퍼마켓 타블로이드 찌라시로 전락합니다. 표지를 전면 폐기하고 수단 난민 출신의 천재 모델을 올리십시오. 우리는 유행을 따르지 않고, 유행을 선포합니다.", "‘We decree culture’는 보그 편집장다운 절대 권력의 카리스마입니다."),
                 ("Let's print with no picture on the cover to save money.", "돈을 아끼기 위해 표지에 사진 없이 인쇄합시다.", "잡지 유통을 포기하는 황당한 발상입니다."),
                 ("The model has bad spec so let's call AS.", "모델 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                ("The advertisers are boycotting. Cartier and Chanel pulled their center spreads. The printer is holding the presses for precisely twelve minutes. What's the countermove?",
                 "광고주들이 보이콧을 선언했어. 까르띠에와 샤넬이 중앙 전면 광고를 철회했네. 인쇄소가 정확히 12분간 윤전기를 멈추고 대기 중이야. 반격 카드는?",
                 "단독 비하인드 다큐멘터리 클립을 틱톡과 인스타그램에 엠바고 해제해 1억 뷰 바이럴을 일으키고 광고주들이 다시 줄 서게 만들자고 하세요.",
                 ("Leak our thirty-second studio darkroom teaser to social media right now. When ten million people see her eyes, Cartier will offer double to buy back their spreads.", "30초 암실 스튜디오 티저를 소셜 미디어에 지금 즉시 유출하십시오. 1,000만 명이 그녀의 눈동자를 보는 순간, 까르띠에는 광고 지면을 되찾기 위해 2배를 부를 것입니다.", "‘studio darkroom teaser’와 ‘offer double to buy back’은 광고주를 무릎 꿇리는 천재적 언론 플레이입니다."),
                 ("We can cry and apologize to Cartier president.", "까르띠에 사장님께 울면서 사과합시다.", "패션 제국의 위엄을 땅에 떨어뜨리는 비굴한 태도입니다."),
                 ("Check the handphone for printer ink levels.", "인쇄소 잉크 잔량을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Presses rolling! The issue broke every newsstand record in eighty years! Cartier just begged for the back cover! Miranda just handed you the keys to her office.",
                 "윤전기 가동! 이번 9월호가 80년 보그 역사상 모든 가판대 판매 기록을 갈아치웠어! 까르띠에가 뒷표지를 달라고 애원했네! 미란다가 방금 자네에게 편집장실 열쇠를 건넸어.",
                 "패션은 옷이 아니라 시대를 꿰뚫어 보는 안목의 권력이라고 담담히 수락하세요.",
                 ("Fashion is not about dresses, Miranda—it is the ruthless art of anticipating what the world craves before it even knows it. Thank you for the kingdom.", "패션은 옷에 관한 것이 아닙니다, 미란다. 세상이 무엇을 갈망하는지 세상 스스로 알기 전에 냉혹하게 꿰뚫어 보는 예술입니다. 제국을 물려주셔서 감사합니다.", "미란다 프리슬리의 왕좌를 완벽히 계승하는 전율의 피날레입니다."),
                 ("I am happy I can buy many handbags now.", "이제 핸드백을 많이 살 수 있어서 참 기쁩니다.", "역사적 왕좌 승계의 무게를 모르는 철없는 소리입니다."),
                 ("Let's do Dutch pay for the editorial lunch.", "편집국 점심은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    return data
'''

with open("scripts/clusters/group_c.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Created group_c.py successfully.")
