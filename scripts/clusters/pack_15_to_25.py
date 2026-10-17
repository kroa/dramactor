# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack: Genres 15 to 25 (11 genres x 4 = 44 episodes)
15: Luxury Real Estate
16: Hollywood Talent Agency
17: 5-Star Hotel Hospitality
18: Fine Art Auction & Heist
19: Investigative Journalism
20: Cyber Crime & Zero-Day Hacking
21: Aerospace Defense & Top Gun
22: Space Exploration & Sci-Fi
23: True Crime Detective Noir
24: Organized Crime Syndicate
25: Formula 1 Motor Racing
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_pack_15_to_25():
    data = {}
    def mk(title, speaker, emoji, synopsis, key_expr, key_note, turns):
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns])

    # 15. Luxury Real Estate
    data["Luxury Real Estate"] = [
        mk(
            "맨해튼 억만장자 거리 펜트하우스 비딩전", "Ryan Serhant (Ultra-Luxury Broker)", "🏙️",
            "센트럴파크 사우스 펜트하우스 1억 2천만 달러. 실리콘밸리 테크 억만장자와 월가 헤지펀드 거물이 동시에 전액 현금 비딩을 넣었다. 듀얼 에이전시 갈등을 조율하고 마감 전 에스크로를 체결해야 한다.",
            "secure an all-cash non-contingent escrow before the sunset clause", "일몰 시한 전에 전액 현금 무조건부 에스크로 계약을 체결할 때 쓰는 표현입니다.",
            [
                ("Two all-cash offers at 120 million on the table. The tech mogul refuses to waive inspection; the hedge fund titan wants the furniture included. How do we close?",
                 "1억 2천만 달러 전액 현금 제안 2건이 올라왔어. 테크 거물은 점검 면제를 거부하고, 헤지펀드 거물은 미술품 가구를 포함해 달래. 어떻게 클로징할 건가?",
                 "헤지펀드 거물에게 5백만 달러 추가 가구 프리미엄을 붙이고 오늘 정오까지 무조건부 에스크로 서명을 요구하라고 하세요.",
                 ("Tell the hedge fund titan he gets the custom staging for a five-million premium, provided he wires ten percent non-refundable earnest money by noon.", "헤지펀드 거물에게 5백만 달러 추가 프리미엄에 맞춤 가구를 넘기되, 오늘 정오까지 10% 몰취 계약금을 송금해야 한다는 조건을 붙이십시오.", "‘non-refundable earnest money’는 협상 주도권을 쥐는 부동산 전문 용어입니다."),
                 ("Let's ask them to play rock-paper-scissors for the penthouse.", "펜트하우스를 두고 가위바위보를 시켜봅시다.", "수천억 원대 딜을 장난으로 만드는 최악의 태도입니다."),
                 ("The house has bad spec so give them discount.", "집 스펙이 안 좋으니 할인해 줍시다.", "‘spec’은 콩글리시입니다.")),
                ("Hedge fund wired twelve million! But the penthouse building board is requesting tax returns from five foreign entities. They threaten to reject the buyer.",
                 "헤지펀드가 1,200만 달러를 송금했어! 그런데 입주자 대표위원회가 5개 해외 법인의 세무 내역을 요구하며 입주 승인을 거부하겠대.",
                 "대표위원회 의장에게 직접 연락해 구매자의 JP모건 무조건부 지급 보증서를 제시하고 오늘 중 특별 승인을 이끌어내세요.",
                 ("Present JP Morgan's unconditional liquidity guarantee directly to the board president. Remind them this sale sets a building record and boosts their own equity.", "입주자 대표 회장에게 JP모건의 무조건부 유동성 보증서를 제시하십시오. 이번 거래가 건물 최고가를 경신해 그들의 자산 가치도 끌어올린다는 점을 강조하세요.", "‘unconditional liquidity guarantee’는 까다로운 보드를 안심시키는 결정적 카드입니다."),
                 ("Tell the board members that they are very mean people.", "입주자 대표들에게 너무 못됐다고 불평합시다.", "입주 거절을 자초하는 유치한 반발입니다."),
                 ("Check the handphone for elevator codes.", "엘리베이터 코드를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Board approved unanimously! The deed is recorded in Manhattan registry! Twelve million dollar commission earned! You just conquered Billionaires' Row, Ryan.",
                 "입주자 대표 전원 만장일치 승인! 맨해튼 등기소에 소유권 이전 등록 완료! 중개 수수료 1,200만 달러 확보! 자네가 억만장자의 거리를 정복했네, 라이언.",
                 "부동산은 건물이 아니라 사람들의 야망과 신뢰를 파는 예술이라고 답하세요.",
                 ("We don't sell square footage, Ryan—we sell the pinnacle of human achievement. Deal closed.", "우리는 단순한 평수를 파는 것이 아닙니다, 라이언. 인간이 도달할 수 있는 성취의 정점을 파는 것입니다. 딜 종결되었습니다.", "밀리언달러 리스팅의 정수를 담은 명대사입니다."),
                 ("I am glad we don't have to show houses tomorrow.", "내일 집 안 보여줘도 돼서 참 좋습니다.", "프로 중개사답지 못한 안일한 소감입니다."),
                 ("Let's do Dutch pay for the Manhattan steak.", "맨해튼 스테이크는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk(
            "아스펜 스키 샬레: 1억 5천만 달러 랜드마크 딜", "Ryan Serhant (Ultra-Luxury Broker)", "🏙️",
            "콜로라도 아스펜 로키산맥 정상. 세계적 억만장자 가문이 소유한 스키 인/아웃 대저택 매각 현장. 비밀 구매자가 익명 유한책임회사(LLC)를 통해 파격적인 당일 현금 매수를 제안한다.",
            "execute a blind-trust purchase agreement with strict confidentiality",
            "비밀 신탁과 익명 법인을 통해 비밀을 유지하며 초고가 부동산을 매입할 때 쓰는 표현입니다.",
            [
                ("Buyer wants complete anonymity through a Delaware blind trust and demands forty-eight-hour closing. Seller wants ten million over asking. Do we bridge the gap?",
                 "매수자가 델라웨어 비밀 신탁을 통한 완전한 익명성과 48시간 내 클로징을 요구해. 매도자는 호가보다 1천만 달러를 더 원하고. 이 격차를 좁힐 수 있겠나?",
                 "48시간 즉시 클로징에 대한 프리미엄으로 매도자의 호가 1천만 증액을 전액 수용하고 비밀유지 협약을 묶으라고 하세요.",
                 ("Accept the premium. Tell the buyer a forty-eight-hour escrow for a trophy asset demands a ten-million convenience fee. Wire the funds to title right now.", "프리미엄을 수용하십시오. 트로피 자산을 48시간 만에 인수하려면 1천만 달러의 편의 수수료가 필요하다고 매수자에게 전하세요. 지금 즉시 권원보험 계좌로 자금을 쏘게 하십시오.", "‘trophy asset’과 ‘wire to title’은 초호화 부동산 거래의 격을 보여주는 언어입니다."),
                 ("Let's wait two months to see if prices drop.", "가격이 떨어지는지 두 달만 기다려봅시다.", "거래 기회를 완전히 날려버리는 우유부단함입니다."),
                 ("The chalet has bad spec so tell the ski patrol.", "샬레 스펙이 안 좋으니 스키 패트롤에 말합시다.", "‘spec’은 콩글리시입니다.")),
                ("Title received the funds! But the local county commissioner refuses to record the deed without a public hearing on scenic ridge easements.",
                 "권원보험사가 자금을 수령했어! 그런데 지역 군 행정관이 경관 보호 조례에 대한 공청회 없이는 등기 이전을 거부하겠다고 버텨.",
                 "해당 대지가 50년 전 취득된 기득권 보호 조항(Grandfathered Rights)을 보유하고 있음을 법적으로 입증해 공청회를 면제시키세요.",
                 ("Present the 1974 sovereign patent deed. The ridge easement is fully grandfathered under Colorado property law. Expedite recording before 5 PM.", "1974년 주정부 원초 등기부를 제시하십시오. 해당 능선 조례는 콜로라도 부동산법상 기득권 보호를 받습니다. 오늘 오후 5시 전까지 등기를 집행하십시오.", "‘grandfathered rights’와 ‘sovereign patent deed’는 행정 규제를 단칼에 돌파하는 부동산 법률 무기입니다."),
                 ("Tell the commissioner that skiing is very fun.", "행정관에게 스키 타는 건 재미있다고 말해봅시다.", "법적 공방에서 아무짝에도 쓸모없는 헛소리입니다."),
                 ("Check your handphone for snow forecasts.", "눈 예보를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Deed recorded! A hundred sixty million dollar historic sale in Aspen! The seller gifted you a vintage Patek Philippe! You own this mountain.",
                 "등기 완료! 아스펜 역사상 최고가인 1억 6천만 달러 매각 성사! 매도자가 자네에게 빈티지 파텍 필립을 선물했네! 자네가 이 산을 지배했어.",
                 "불가능을 가능하게 만드는 집념이 최고의 중개사를 증명한다고 화답하세요.",
                 ("When obstacles arise on the mountain, Ryan, you don't turn back—you carve your own trail to the summit. Deal closed.", "산에서 장애물을 만났을 때 돌아서는 것이 아니라, 정상으로 향하는 자신만의 길을 개척하는 것입니다. 딜 종결되었습니다.", "럭셔리 부동산의 정점에서 나누는 품격 있는 대화입니다."),
                 ("I am glad we can drink beer at the lodge now.", "이제 롯지에서 맥주를 마실 수 있어서 참 좋습니다.", "품격을 떨어뜨리는 소박한 소리입니다."),
                 ("Let's do Dutch pay for the ski lift ticket.", "스키 리프트권은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk(
            "마이애미 워터프론트 메가맨션 허리케인 에스크로", "Ryan Serhant (Ultra-Luxury Broker)", "🏙️",
            "플로리다 마이애미 스타 아일랜드. 카테고리 4 허리케인이 상륙하기 24시간 전. 8천만 달러 메가맨션의 클로징 당일 방파제 침식 위험이 감지되며 바이어가 계약 취소를 통보했다.",
            "negotiate an emergency escrow holdback for storm fortification",
            "자연재해 직전 방파제 보강을 위한 에스크로 유보금을 협상해 계약을 살려낼 때 쓰는 표현입니다.",
            [
                ("Category four hurricane is twenty hours out! Buyer is panicking about seawall failure and threatens to invoke the act of God clause to walk with his deposit!",
                 "카테고리 4 허리케인이 20시간 앞이야! 매수자가 방파제 붕괴를 걱정하며 불가항력(Act of God) 조항을 발동해 계약금을 빼서 나가겠대!",
                 "계약 취소 대신 2백만 달러의 에스크로 유보금을 걸고 폭풍 후 즉시 해양 방파제를 복구해 주는 조건으로 즉일 클로징을 설득하세요.",
                 ("Do not let him walk. Offer a two-million storm holdback in escrow. The seller warrants complete post-hurricane seawall restoration, and the title clears today.", "그를 그냥 보내지 마세요. 에스크로에 2백만 달러 폭풍 유보금을 예치하십시오. 매도자가 허리케인 후 방파제 복구를 보증하고 소유권은 오늘 이전합니다.", "‘storm holdback in escrow’는 취소 위기의 초호화 계약을 즉각 소생시키는 묘수입니다."),
                 ("Let's scream at the ocean to stop the waves.", "파도를 멈추라고 바다를 향해 고함을 지릅시다.", "황당하고 비이성적인 행동입니다."),
                 ("The seawall has bad spec so call the AS center.", "방파제 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                ("Buyer agreed to the holdback! But the marine insurance underwriter suspended binding new windstorm policies due to the approaching eye wall. We have two hours.",
                 "매수자가 유보금에 동의했어! 그런데 허리케인 눈이 다가오자 해상 보험사가 신규 풍수해 보험 인수 승인을 중단해버렸어. 2시간 남았어.",
                 "런던 로이즈(Lloyd's of London)의 글로벌 초과 손해 브로커를 긴급 동원해 특약 바인더를 즉시 발행받으라고 지시하세요.",
                 ("Patch through to Lloyd's of London syndicates immediately. Issue a specialty maritime surplus-lines binder before the storm coordinates hit the radar.", "즉시 런던 로이즈 신디케이트로 연결하십시오. 폭풍 좌표가 레이더에 찍히기 전에 특수 해상 잉여 보험 바인더를 발급받으세요.", "‘surplus-lines binder’와 ‘Lloyd's syndicates’는 위기 속에서 보험 인수를 관철하는 글로벌 금융 기술입니다."),
                 ("Tell the insurance agent he has bad manner.", "보험 설계사에게 매너가 나쁘다고 따집시다.", "‘manner’는 콩글리시입니다."),
                 ("Check the handphone for hurricane wind speeds.", "허리케인 풍속을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Insurance bound! Escrow funded! Title recorded! The hurricane passed with zero seawall damage, and the property value jumped ten million post-storm!",
                 "보험 체결 완료! 에스크로 펀딩 완료! 등기 완료! 허리케인이 방파제 손상 없이 지나갔고, 폭풍 후 자산 가치가 1천만 달러 뛰었어!",
                 "폭풍우 속에서도 흔들리지 않는 배짱이 최고의 자산을 지켜낸다고 답하세요.",
                 ("Real estate fortune isn't made in calm seas, Ryan—it's forged when you stand tall while everyone else runs for shelter. Another masterclass.", "부동산의 대박은 잔잔한 바다에서 나오지 않습니다, 라이언. 남들이 피난처로 달아날 때 우뚝 서서 자리를 지킬 때 빚어지는 것입니다. 또 한 번의 마스터클래스였습니다.", "압도적 배짱의 승리를 선언하는 피날레입니다."),
                 ("I am glad we don't have to clean the swimming pool.", "수영장 청소 안 해도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                 ("Let's do Dutch pay for the Miami mojito tonight.", "오늘 밤 마이애미 모히토는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk(
            "비벌리힐스 유서 깊은 대저택 조닝 변경과 전격 클로징", "Ryan Serhant (Ultra-Luxury Broker)", "🏙️",
            "캘리포니아 비벌리힐스 선셋 블러바드. 1920년대 할리우드 전설이 살던 유서 깊은 1억 달러 대저택. 역사 보존 위원회의 건축 제한 조례를 돌파하고 해외 테크 거물과의 매매를 완결해야 한다.",
            "secure a historic preservation variance for modern expansion",
            "역사 보존 구역 내에서 현대적 확장을 허용하는 특별 예외 승인을 쟁취할 때 쓰는 표현입니다.",
            [
                ("The Beverly Hills Historical Commission blocked the sale! They refuse to allow our buyer to install a sub-terrace private screening theater and art vault.",
                 "비벌리힐스 역사보존위원회가 매각을 가로막았어! 우리 매수자가 지하 프라이빗 상영관과 미술품 수장고를 짓는 것을 불허하겠대.",
                 "원래 외관을 100% 보존하면서 지하 구조물만을 비파괴 공법으로 증축하는 친환경 문화재 보존 계획안을 제출하세요.",
                 ("Submit our non-invasive structural blueprints. We preserve every stone of the 1928 facade while engineering an earthquake-rated subterranean vault. It's a win-win.", "비파괴 구조 설계도를 제출하십시오. 1928년 파사드의 돌 하나까지 완벽히 보존하면서 내진 설계 지하 수장고를 구축합니다. 완벽한 윈-윈입니다.", "‘non-invasive blueprints’와 ‘preserve the facade’는 보존위원회를 설득하는 세련된 건축 해법입니다."),
                 ("Let's threaten to tear down the historic house tonight.", "오늘 밤 유서 깊은 집을 불도저로 밀어버리겠다고 협박합시다.", "문화재 훼손 혐의로 형사 고발당하는 자멸수입니다."),
                 ("The old house has bad spec so tell the mayor.", "오래된 집 스펙이 안 좋으니 시장에게 따집시다.", "‘spec’은 콩글리시입니다.")),
                ("Commission granted the variance! But the seller's estranged ex-wife just placed a lis pendens on the title claiming unrecorded marital equity.",
                 "위원회가 조닝 예외를 승인했어! 그런데 매도자의 이혼한 전처가 미등기 부부 지분을 주장하며 소송 계속 통지서(Lis Pendens)를 등기부에 걸어버렸어.",
                 "법원에 긴급 담보 공탁을 신청해 등기부상의 권리 침해를 즉시 말소하고 매각 대금을 신탁 계좌에 묶자고 하세요.",
                 ("File for an expedited bond substitution to expunge the lis pendens immediately. Escrow deposits disputed equity into court trust while title conveys clean.", "소송 통지서를 즉시 말소하기 위한 긴급 보증 공탁을 신청하십시오. 분쟁 지분을 법원 신탁에 예치하고 소유권은 무결점으로 이전합니다.", "‘expunge the lis pendens’와 ‘bond substitution’은 등기 분쟁을 24시간 내 해결하는 최고급 부동산 법률 기술입니다."),
                 ("Tell the ex-wife to go away and cry.", "전처에게 저리 가서 울라고 하세요.", "법적 효력이 없는 무례한 처사입니다."),
                 ("Check the handphone for lawyer fees.", "변호사 비용을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Lis pendens expunged! One hundred ten million wired! Full escrow closed before Sunset Boulevard sunset! You wrote Hollywood history, Ryan.",
                 "소송 통지서 말소 완료! 1억 1천만 달러 송금 완료! 선셋 블러바드의 일몰 전에 에스크로 전면 클로징! 자네가 할리우드의 역사를 썼네, 라이언.",
                 "진정한 거물은 과거의 유산을 경외하면서도 미래의 가치를 조각해낸다고 답하세요.",
                 ("A historic estate isn't preserved by freezing in time, Ryan—it lives on when you connect its grand past to a visionary future. Deal done.", "역사적 저택은 시간에 얼어붙는다고 보존되는 것이 아닙니다. 웅장한 과거를 미래의 비전과 연결할 때 영원히 살아 숨 쉬는 것입니다. 딜 완료했습니다.", "비벌리힐스의 전설을 완성하는 완벽한 피날레입니다."),
                 ("I am glad we can sleep late tomorrow morning.", "내일 아침에 늦잠 잘 수 있어서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                 ("Let's do Dutch pay for the Sunset cocktail.", "선셋 칵테일은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    return data
