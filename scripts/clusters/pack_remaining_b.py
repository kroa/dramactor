# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack Remaining B: Genres 18 to 27 (10 genres x 4 = 40 episodes)
18: Fine Art Auction & Heist
19: Investigative Journalism
20: Cyber Crime & Zero-Day Hacking
21: Aerospace Defense & Top Gun
22: Space Exploration & Sci-Fi
23: True Crime Detective Noir
24: Organized Crime Syndicate
25: Formula 1 Motor Racing
26: Diplomatic Statecraft & Embassy
27: Bio-Hazard & Epidemiology
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_pack_remaining_b():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    # 18. Fine Art Auction & Heist
    data["Fine Art Auction & Heist"] = [
        mk("소더비 이브닝 세일 8천만 달러 모네 위작 논란", "Julian Vance (Senior Restitution Officer)", "🎨",
           "런던 소더비 경매장. 모네의 '수련' 진품 경매 시작 10분 전, 프랑스 화학 감정팀이 유채 안료에서 1950년대 합성 바륨이 검출되었다는 보고서를 보내왔다. 경매를 취소할지 진위를 규명할지 결단해야 한다.",
           "verify the provenance chain through archival forensics", "기록물 감식을 통해 예술품의 출처와 소장 이력을 엄밀히 검증할 때 쓰는 표현입니다.",
           [
               ("Chemical spectrometry shows trace synthetic barium in the blue glaze! If we hammer this for eighty million, Sotheby's reputation is destroyed! What's the protocol?",
                "화학 분광 분석 결과 파란색 유약에서 미량의 합성 바륨이 검출되었어! 이대로 8천만 달러에 낙찰시키면 소더비의 명성은 끝장이야! 규정이 뭐야?",
                "표면 바니시의 1960년대 보존 복원 처리 기록을 확인하고 모네의 원본 캔버스 섬유 탄소 연대 측정을 제시하라고 하세요.",
                ("Do not cancel the lot. That barium is from the 1964 National Gallery varnish conservation. Pull the provenance ledger and prove the canvas weave is 1908 Normandy linen.", "출품을 취소하지 마십시오. 그 바륨은 1964년 내셔널 갤러리의 바니시 복원 흔적입니다. 출처 원장을 제시해 캔버스가 1908년 노르망디 아마포 원본임을 입증하세요.", "‘provenance ledger’와 ‘canvas weave’는 미술품 감정의 절대적 전문성을 보여주는 언어입니다."),
                ("Let's throw the painting into the trash can.", "그림을 쓰레기통에 던져버립시다.", "8천만 달러짜리 국보급 명화를 파괴하는 황당한 발상입니다."),
                ("The paint has bad spec so tell the artist.", "물감 스펙이 안 좋으니 화가에게 따집시다.", "‘spec’은 콩글리시입니다.")),
               ("The restoration records confirmed your theory! But the anonymous bidder on line four demands a twenty-million discount or he withdraws his guarantee.",
                "복원 기록이 자네 이론을 증명했어! 하지만 4번 전화선 익명 응찰자가 2천만 달러 할인을 안 해주면 보증 입찰을 철회하겠대.",
                "도쿄와 뉴욕의 서면 응찰자 3명이 대기 중임을 상기시키며 정가 낙찰을 단호하게 고수하세요.",
                ("Tell line four there are three international museum syndicates on the books. He pays the reserve price, or he watches the hammer fall to Tokyo.", "4번 응찰자에게 국제 미술관 컨소시엄 세 곳이 대기 중이라고 전하십시오. 최저 낙찰가를 지불하든지, 아니면 도쿄로 망치가 떨어지는 걸 지켜보라고 하세요.", "‘reserve price’와 ‘hammer fall’은 경매장 주도권을 놓치지 않는 명쾌한 화법입니다."),
                ("Give him fifty percent discount so he buys it.", "그가 사도록 50%나 깎아줍시다.", "경매사의 신뢰도를 바닥에 떨어뜨리는 짓입니다."),
                ("Check the handphone for auction bids.", "경매 입찰을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Hammer fell! Sold for ninety-four million dollars, an all-time record for impressionism! The art world bowed to your forensic eye, Julian.",
                "망치가 떨어졌어! 인상파 역대 최고가인 9,400만 달러에 낙찰! 전 세계 미술계가 자네의 감식안에 경의를 표했네, 줄리안.",
                "위대한 예술은 시대의 의심을 견뎌내고 영원히 빛난다고 답하세요.",
                ("A masterpiece does not fear the scrutiny of science, Julian—it welcomes the light. Sold to the gentleman on line two.", "걸작은 과학의 엄격한 검증을 두려워하지 않습니다. 오히려 진실의 빛을 환영할 뿐입니다. 2번 응찰자에게 낙찰되었습니다.", "예술 경매의 품격을 완성하는 환상적인 피날레입니다."),
                ("I am glad we don't have to carry the frame.", "액자 안 날라도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the London martini.", "런던 마티니는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("나치 약탈 클림트 황금 명화 반환 극비 합의", "Julian Vance (Senior Restitution Officer)", "🎨",
           "빈 벨베데레 궁전 비밀 협상실. 2차 대전 나치에게 약탈당한 구스타프 클림트의 황금 초상화를 원소유자 유족에게 반환하는 세기의 재판 선고 전야. 국가적 손실을 막으려는 오스트리아 문화부와 유족 사이의 담판을 이끌어야 한다.",
           "execute the restitution settlement under the Washington Principles",
           "워싱턴 원칙에 따라 약탈 예술품을 유족에게 정당하게 반환하고 합의를 도출할 때 쓰는 표현입니다.",
           [
               ("The Austrian minister offers five million euros in compensation if the family leaves the portrait in Vienna. The family's lawyer refuses. Arbitration deadline is midnight.",
                "오스트리아 장관이 초상화를 빈에 남겨두면 5백만 유로 보상금을 주겠대. 유족 변호사는 거부하고 있고. 중재 시한은 자정이야.",
                "돈으로 역사의 상처를 덮을 수 없으므로 무조건적 소유권 반환 후 3년간의 순회 전시 대여 협약으로 타협안을 제시하세요.",
                ("Restitution of title is non-negotiable under the Washington Principles. Return full ownership to the heirs, then lease the portrait back for a three-year international tour.", "워싱턴 원칙에 따라 소유권 반환은 타협할 수 없습니다. 유족에게 전면 소유권을 반환하되, 3년간의 국제 순회 전시 대여 협약을 맺는 것이 명예로운 타협입니다.", "‘restitution of title’과 ‘Washington Principles’는 약탈 미술품 분쟁 해결의 국제적 기준입니다."),
                ("Tell the family that five million is a lot of money.", "유족에게 5백만 유로는 큰돈이라고 타이릅시다.", "역사적 비극의 상처를 모욕하는 몰상식한 발언입니다."),
                ("The picture has bad spec so tell the museum.", "그림 스펙이 안 좋으니 박물관에 말합시다.", "‘spec’은 콩글리시입니다.")),
               ("The minister agreed to return the title! But the museum director locked the gallery vault and refuses to surrender the golden canvas without a court bailiff.",
                "장관이 소유권 반환에 동의했어! 그런데 박물관장이 수장고 문을 걸어 잠그고 법원 집행관 없이는 황금 캔버스를 넘기지 않겠다고 저항하고 있어.",
                "국제 박물관 협의회 영구 제명과 연방 압수수색 영장 집행을 통보해 저항을 무력화하세요.",
                ("Present the federal court enforcement warrant. Remind the director that obstructing restitution results in personal contempt charges and international museum blacklisting.", "연방 법원 강제집행 영장을 제시하십시오. 반환을 방해하면 개인 법정모독죄 처벌과 국제 박물관 협의회 영구 제명이 뒤따른다는 점을 똑똑히 알리세요.", "‘enforcement warrant’와 ‘international blacklisting’은 불법 점거를 단칼에 해제시키는 법적 조치입니다."),
                ("Let's cry in front of the locked door.", "잠긴 문앞에서 울어봅시다.", "아무런 효력이 없는 무기력한 태도입니다."),
                ("Check the handphone for train tickets to Zurich.", "취리히 기차표를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Vault opened! The Golden Portrait is safely crated in climate-controlled containers! The heirs wept with gratitude! You restored justice to history.",
                "수장고가 열렸어! 황금빛 초상화가 항온 항습 상자에 안전하게 포장되었어! 유족들이 감사의 눈물을 흘렸네! 자네가 역사에 정의를 되돌려주었어.",
                "빼앗긴 예술을 제자리로 돌려놓는 것이야말로 인류 양심의 승리라고 답하세요.",
                ("Art plundered in darkness must always be returned in the light. Today, memory triumphs over tyranny. The portrait is going home.", "어둠 속에서 약탈당한 예술은 반드시 빛 속으로 돌아와야 합니다. 오늘, 기억이 폭정을 이겼습니다. 초상화는 집으로 갑니다.", "영화 우먼 인 골드를 연상시키는 가슴 벅찬 피날레입니다."),
                ("I am glad we don't have to carry heavy boxes now.", "이제 무거운 상자 안 날라도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Viennese coffee.", "빈 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("베니스 비엔날레 도난 설치작품 암시장 추적", "Julian Vance (Senior Restitution Officer)", "🎨",
           "이탈리아 베니스 대운하. 비엔날레 최고 영예인 황금사자상 수상 조각품이 전시장에서 사라졌다. 48시간 내 스위스 비밀 항구로 밀수출되기 전 수상 경찰과 공조해 회수해야 한다.",
           "intercept the illicit art trafficking corridor across the lagoon",
           "해상 밀수 경로를 차단하고 도난 미술품을 긴급 회수할 때 쓰는 표현입니다.",
           [
               ("The bronze sculpture was smuggled out via a motorized gondola! Interpol tracked encrypted radio chatter to a cargo barge near the Lido! What's our tactical approach?",
                "청동 조각품이 모터 곤돌라로 빼돌려졌어! 인터폴이 리도섬 근처 화물 바지선으로 향하는 암호 무전을 감청했네! 전술적 접근법이 뭐야?",
                "베니스 수상 경찰의 고속 순찰정으로 대운하 해상 통로를 전면 차단하고 잠수부를 투입해 수색하라고 명령하세요.",
                ("Deploy the Carabinieri marine interdiction team immediately. Seal the harbor exits and intercept the barge before it clears international waters.", "이탈리아 헌병대 해상 차단팀을 즉시 급파하십시오. 항구 출구를 전면 봉쇄하고 공해상으로 빠져나가기 전에 바지선을 나포해야 합니다.", "‘marine interdiction team’과 ‘seal harbor exits’는 밀수 선박을 틀어막는 해상 작전 지휘입니다."),
                ("Ask the gondola driver politely where the art is.", "곤돌라 사공에게 예술품이 어디 있는지 공손히 물어봅시다.", "도주 기회만 주는 순진한 소리입니다."),
                ("The boat has bad spec so buy a faster engine.", "보트 스펙이 안 좋으니 더 빠른 엔진을 사 옵시다.", "‘spec’은 콩글리시입니다.")),
               ("Barge boarded! The smugglers are cornered. But their leader is threatening to drop the irreplaceable bronze masterpiece into the deep canal waters!",
                "바지선 진입 성공! 밀수범들이 코너에 몰렸어. 그런데 두목이 둘도 없는 청동 걸작을 깊은 운하 물속에 빠뜨려버리겠다고 위협하고 있어!",
                "수중 음파 소나와 유압 크레인이 이미 선체 하부에 대기 중임을 알리고 즉각 무기를 버리라고 최후통첩을 보내세요.",
                ("Tell him our underwater recovery divers and hydraulic netting are already positioned beneath his hull. Drop the piece, and you face life imprisonment.", "선체 바로 밑에 수중 다이버들과 유압 그물망이 이미 대기 중이라고 알리십시오. 물건을 떨어뜨리는 순간 종신형에 처해질 것입니다.", "‘hydraulic netting’과 ‘life imprisonment’는 인질극을 벌이는 범인을 굴복시키는 단호한 대처입니다."),
                ("Tell the thief that bronze melts in water.", "도둑에게 청동은 물에 녹는다고 거짓말해봅시다.", "어설픈 거짓말로 조롱만 당합니다."),
                ("Check the handphone for water temperature.", "수온을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Sculpture secured without a scratch! Smugglers in handcuffs! The Venice Biennale jury presented you with the grand preservation medal! Magnifico!",
                "조각품 흠집 하나 없이 확보 완료! 밀수범 전원 체포! 베니스 비엔날레 심사위원단이 자네에게 문화재 보존 특별 메달을 수여했네! 훌륭했어!",
                "예술을 지키는 것은 인류의 보편적 영혼을 지키는 숭고한 사명이라고 화답하세요.",
                ("Art belongs to the world, Julian, not to the shadows of thieves. The Golden Lion shines once more over Venice.", "예술은 도둑의 그림자가 아니라 온 세상의 것입니다, 줄리안. 황금사자상이 베니스 위에서 다시 한번 빛을 발합니다.", "베니스의 낭만과 승리를 완벽히 조화시킨 피날레입니다."),
                ("I am glad we don't have to swim in the canal.", "운하에서 수영 안 해도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Venetian gelato.", "베니스 젤라토는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("루브르 큐레이터 다빈치 미공개 스케치 진위 판정", "Julian Vance (Senior Restitution Officer)", "🎨",
           "파리 루브르 박물관 지하 비밀 수장고. 500년간 봉인되었던 레오나르도 다빈치의 미공개 스케치 원본이 발견되었다. 적외선 다분광 분석을 통해 위작의 함정을 걸러내고 진품을 공표해야 한다.",
           "authenticate the Renaissance sketch through multispectral infrared imaging",
           "다분광 적외선 영상 분석을 통해 르네상스 원작의 필치를 과학적으로 감정할 때 쓰는 표현입니다.",
           [
               ("The sketch shows Leonardo's iconic sfumato crosshatching. But two Oxford professors claim it's an eighteenth-century pastiche. Press conference in thirty minutes.",
                "스케치에 레오나르도 특유의 스푸마토 음영 기법이 보여. 하지만 옥스퍼드 교수 두 명이 18세기 모작이라고 주장하고 있어. 기자회견까지 30분 남았네.",
                "적외선 투과 분광기로 밑그림의 은필선(Silverpoint)과 왼손잡이 특유의 사선 획 방향성을 제시하라고 지시하세요.",
                ("Run multispectral infrared scanning on the underdrawing. Prove the left-handed hatching strokes and walnut ink chemistry date precisely to 1503 Milan.", "밑그림에 다분광 적외선 스캔을 가동하십시오. 왼손잡이 특유의 빗금 획 방향과 호두 잉크의 화학 성분이 정확히 1503년 밀라노 산임을 증명하세요.", "‘multispectral infrared scanning’과 ‘left-handed hatching strokes’는 학계의 논란을 일거에 종식시키는 결정적 과학 감정입니다."),
                ("Let's ask the tourists in the museum if it looks pretty.", "박물관 관광객들에게 예뻐 보이는지 물어봅시다.", "학술적 권위를 스스로 시궁창에 버리는 짓입니다."),
                ("The paper spec is bad so buy new parchment.", "종이 스펙이 안 좋으니 새 양피지를 사 옵시다.", "‘spec’은 콩글리시입니다.")),
               ("The strokes confirm left-handed mastery! But a private collector claims he bought this drawing fifty years ago and threatens an international ownership freeze.",
                "획의 방향이 왼손잡이 거장의 진품임을 확인했어! 그런데 한 개인 수집가가 50년 전 자기가 산 그림이라며 국제 소유권 동결 소송을 걸겠다고 협박해.",
                "프랑스 국립 문서고의 1793년 왕립 컬렉션 등록 장부를 제시해 국가 소유의 불가침성을 법적으로 쐐기 박으세요.",
                ("Present the 1793 French Royal Collection accession ledger. State ownership of cultural patrimony is imprescriptible and immune to private claim.", "1793년 프랑스 왕립 컬렉션 등록 원장을 제시하십시오. 국가 문화유산의 소유권은 시효로 소멸하지 않으며 개인의 청구권으로부터 면책됩니다.", "‘imprescriptible ownership’과 ‘cultural patrimony’는 개인의 소유권 주장을 원천 봉쇄하는 국제법적 방패입니다."),
                ("Tell the collector to go home and cry.", "수집가에게 집에 가서 울라고 하세요.", "법적 분쟁에서 아무런 효력이 없는 무례한 언사입니다."),
                ("Check the handphone for museum opening hours.", "박물관 개관 시간을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Authenticity confirmed by Louvre board! The world media erupted! Da Vinci's lost masterpiece is unveiled under the glass pyramid! You uncovered history, Julian.",
                "루브르 이사회 진품 최종 공인! 전 세계 언론 폭발! 다빈치의 잃어버린 걸작이 유리 피라미드 아래서 공개되었어! 자네가 역사를 발굴했네, 줄리안.",
                "진정한 예술은 수백 년의 세월을 뛰어넘어 인간의 영혼과 영원을 잇는 다리라고 답하세요.",
                ("Five centuries of silence, Julian, broken by a single stroke of genius. Leonardo smiles across the ages. The masterpiece belongs to eternity.", "500년의 침묵이 거장의 단 한 번의 붓질로 깨어났습니다, 줄리안. 레오나르도가 시대를 뛰어넘어 미소 짓고 있습니다. 이 걸작은 영원의 것입니다.", "다빈치 명작 발견의 경외감을 완성하는 숭고한 피날레입니다."),
                ("I am glad we can eat lunch now.", "이제 점심을 먹을 수 있어서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the Parisian croissant.", "파리 크루아상은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    return data

