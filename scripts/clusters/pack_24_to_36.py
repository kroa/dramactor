# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack: Genres 24 to 36 (13 genres x 4 = 52 episodes)
24: Organized Crime Syndicate
25: Formula 1 Motor Racing
26: Diplomatic Statecraft & Embassy
27: Bio-Hazard & Epidemiology
28: Forensic Pathology & CSI
29: High-Stakes Casino Poker
30: Private Military & Extraction
31: Environmental Justice & Crime
32: Antiquities & Treasure Hunting
33: Architectural Grand Design
34: VIP Protection & Counter-Terror
35: Superyacht Ocean Luxury
36: Music & Entertainment Business
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_pack_24_to_36():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    def add_g(name, spk, emo, arcs):
        data[name] = [mk(a[0], spk, emo, a[1], a[2], a[3], a[4]) for a in arcs]

    # 24. Organized Crime Syndicate
    add_g(
        "Organized Crime Syndicate", "Don Salvatore Falcone (Syndicate Boss)", "🍸",
        [
            ("패밀리 보스의 비밀 서재: 내부 배신자 색출",
             "리틀 이태리 고급 시가 클럽 지하. 패밀리 내부에서 FBI와 내통한 언더커버 스파이의 정황이 포착되었다. 보스의 날카로운 심문에 흔들림 없이 충성을 입증해야 한다.",
             "root out the rat inside the crime family", "조직 내부의 밀고자(배신자)를 색출하고 결백을 증명할 때 쓰는 표현입니다.",
             [
                 ("A wiretap transcript fell into my lap this morning. Someone in my inner circle has been singing like a canary to the Feds. Convince me it wasn't you.",
                  "오늘 아침 내 손에 도청 녹취록이 들어왔어. 내 최측근 중 누군가가 FBI에 카나리아처럼 지저귀고 있더군. 네가 아니라는 걸 증명해 봐라.",
                  "보스에게 목숨을 걸고 충성을 맹세하며 금융 계좌와 도청 내역을 대조해 진짜 배신자를 지목하겠다고 답하세요.",
                  ("I’ve bled for this family for fifteen years, Don Salvatore. Run my financials, check every call. But look at Sonny's offshore shell company—that's where your leak is coming from.",
                   "전 15년간 이 패밀리를 위해 피를 흘렸습니다, 살바토레 대부님. 제 금융 내역과 모든 통화를 털어보십시오. 하지만 소니의 역외 페이퍼컴퍼니를 보십시오. 정보는 거기서 새고 있습니다.",
                   "‘bled for this family’와 ‘singing like a canary’에 맞서는 냉철한 반격은 마피아 누아르의 정수입니다."),
                  ("I am innocent because I like Italian pasta and respect you.",
                   "저는 이탈리아 파스타를 좋아하고 대부님을 존경하므로 결백합니다.",
                   "유치하고 맹목적인 변명으로 보스의 의심만 키웁니다."),
                  ("Let's call the police AS center to check the wiretap.",
                   "도청 장치를 확인하기 위해 경찰 AS 센터를 부릅시다.",
                   "‘AS’는 콩글리시입니다."))
                 ,
                 ("Sonny's offshore account had three FBI wire transfers. You brought me the head of the serpent. But how do we silence him before the grand jury convenes tomorrow?",
                  "소니의 역외 계좌에 FBI 송금 내역이 3건 찍혀 있었어. 네가 뱀의 머리를 가져왔군. 하지만 내일 대배심이 소집되기 전에 놈의 입을 어떻게 막을 텐가?",
                  "법정 출석 전 시칠리아행 화물선에 태워 영구 추방하거나 법적 증언 능력을 무력화하자고 제안하세요.",
                  ("Put him on a midnight freighter to Palermo with zero passport. Strip him of every asset, make him a ghost. Dead men tell no tales, but living ghosts can't testify.",
                   "자정 팔레르모행 화물선에 여권도 없이 태워 보내시죠. 모든 자산을 박탈해 유령으로 만드십시오. 죽은 자는 말이 없지만, 살아있는 유령은 증언할 수 없습니다.",
                   "‘strip him of every asset’과 ‘dead men tell no tales’는 대부(Godfather) 스타일의 냉혈한 전략입니다."),
                  ("We can give him a scolding and tell him not to do it again.",
                   "그에게 따끔하게 잔소리를 하고 다시는 그러지 말라고 타이릅시다.",
                   "범죄 조직에서 용납될 수 없는 순진한 발언입니다."),
                  ("Check your handphone for shipping prices.",
                   "운송 가격을 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("It's done. Sonny is on the water, the Feds' subpoena is nullified, and the Falcone family controls the five boroughs. You're my new underboss.",
                  "끝났다. 소니는 바다 위에 있고 연방정부 소환장은 무효화되었으며, 팔코네 패밀리는 뉴욕 5개 자치구를 장악했다. 오늘부터 네가 내 새로운 언더보스다.",
                  "패밀리의 명예와 오메르타(침묵의 규율)를 목숨 바쳐 수호하겠다고 엄숙히 수락하세요.",
                  ("Our word is our bond, Don Salvatore. The omertà remains sacred. As long as I breathe, no Fed crosses our threshold.",
                   "우리의 맹세는 혈맹입니다, 살바토레 대부님. 오메르타의 규율은 여전히 신성합니다. 제가 숨 쉬는 한 어떤 연방요원도 우리 문턱을 넘지 못할 것입니다.",
                   "‘omertà remains sacred’는 조직의 최고위 간부다운 장엄한 충성 서약입니다."),
                  ("I am happy because now I can wear expensive suits.",
                   "이제 비싼 양복을 입을 수 있게 되어 기쁩니다.",
                   "가벼운 태도로 엄숙한 분위기를 망칩니다."),
                  ("Let's do Dutch pay for the celebration steak dinner.",
                   "축하 스테이크 저녁 식사는 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("항만 부두 밀수 컨테이너 연방 요원 급습 돌파",
             "브루클린 부두 자정. 1억 달러 상당의 다이아몬드 선적이 실린 컨테이너 하역 중 국토안보부와 세관 요원들이 항구를 전면 봉쇄했다. 포위망을 뚫고 물건을 반출해야 한다.",
             "evade the federal cordon and secure the contraband", "연방 수사망의 봉쇄를 뚫고 밀수품을 무사히 빼돌릴 때 쓰는 표현입니다.",
             [
                 ("Customs and DHS just cordoned off Gate 4! Searchlights everywhere, and K-9 units are sweeping Berth 12! Do we torch the cargo or fight our way out?",
                  "세관과 국토안보부가 4번 게이트를 봉쇄했어! 서치라이트가 깔리고 탐지견들이 12번 선석을 샅샅이 뒤지고 있다! 화물을 불태울까, 총격전을 벌여 뚫을까?",
                  "총을 쏘지 말고 항만 전력 변전소를 차단해 정전 속에서 바지선으로 우회 반출하자고 지시하세요.",
                  ("Kill the main breaker at the substation. Cut the harbor lights, drop smoke cannisters, and transfer the crate to the tugboat on the blind side. No gunfire, no heat.",
                   "변전소 메인 차단기를 내리십시오. 항만 조명을 끄고 연막탄을 투척한 뒤 사각지대에 대기 중인 예인선으로 상자를 옮기세요. 총성도, 수사망 추적도 없게 만듭니다.",
                   "‘kill the main breaker’와 ‘no gunfire, no heat’는 전문 밀수 작전의 정석입니다."),
                  ("Let's surrender to the police and ask for forgiveness.",
                   "경찰에게 투항하고 선처를 구합시다.",
                   "조직 전체를 파멸로 이끄는 나약한 선택입니다."),
                  ("The shipping container has bad spec so call AS.",
                   "선적 컨테이너 스펙이 안 좋으니 AS를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("Power is out! DHS is scrambling in the dark. But a Coast Guard cutter is moving to intercept the tugboat in the channel. What's the escape route?",
                  "정전됐다! 국토안보부가 어둠 속에서 우왕좌왕하고 있어. 하지만 해안경비대 순찰정이 수로에서 예인선을 나포하려 접근 중이야. 탈출로는?",
                  "가짜 조난 신호를 띄워 순찰정의 방향을 돌리고 퀸스 운하 수로로 잠입하자고 명령하세요.",
                  ("Broadcast a decoy distress beacon towards Staten Island. When the cutter diverts, slip the tug up the Newtown Creek inlet under radar shadow.",
                   "스태튼아일랜드 쪽으로 가짜 조난 신호를 송출하십시오. 순찰정이 회항하면 예인선을 레이더 사각지대인 뉴타운 크릭 수로로 몰래 진입시키세요.",
                   "‘decoy distress beacon’과 ‘radar shadow’는 군사 작전 수준의 도주 전략입니다."),
                  ("Wave a white towel and tell them we are fishermen.",
                   "흰 수건을 흔들며 고기잡이 어부라고 둘러댑시다.",
                   "어설픈 거짓말로 즉각 체포를 자초합니다."),
                  ("Check your handphone for coastal weather.",
                   "해안 날씨를 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("The diamonds are locked in our Manhattan vault! Zero arrests, zero shots fired, and the Feds are raiding an empty container! Masterclass, underboss.",
                  "다이아몬드가 맨해튼 금고에 안전하게 입고되었어! 체포 0명, 발포 0발, 연방요원들은 빈 깡통 컨테이너를 뒤지고 있네! 완벽한 마스터클래스였네, 언더보스.",
                  "밤의 어둠 속에서도 팔코네의 규칙만이 법이라고 답하세요.",
                  ("The law operates in daylight, Don Salvatore, but we own the shadows. The family's vault is full, and our honor is intact.",
                   "법은 대낮에 작동하지만, 그림자를 지배하는 건 우리입니다, 살바토레 대부님. 패밀리의 금고는 채워졌고 우리의 명예는 건재합니다.",
                   "조직의 카리스마를 각인시키는 누아르 대사입니다."),
                  ("I am glad we can eat midnight ramen now.",
                   "이제 야식으로 라면을 먹을 수 있어서 참 다행입니다.",
                   "가벼운 태도로 긴장감을 날려버립니다."),
                  ("Let's do Dutch pay for the tugboat fuel.",
                   "예인선 기름값은 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("라이벌 카르텔과의 평화 회담: 마약 구역 분할 담판",
             "브루클린 빈티지 와이너리. 뉴욕 전역을 피로 물들인 5대 패밀리 간의 영역 분쟁을 종식하기 위해 살인적인 긴장감 속에서 카르텔 보스들과의 종전 협상 테이블에 마주 앉았다.",
             "negotiate a bloodless truce and partition territories", "유혈 사태를 멈추고 구역 분할 평화 협정을 이끌어낼 때 쓰는 표현입니다.",
             [
                 ("Don Moretti pulled his Beretta under the table! He demands exclusive distribution in Manhattan or he turns Brooklyn into a warzone. How do you respond?",
                  "모레티 보스가 테이블 밑에서 베레타를 뽑았어! 맨해튼 독점 유통권을 넘기지 않으면 브루클린을 전쟁터로 만들겠다고 위협하고 있다. 어떻게 대응하겠나?",
                  "총구 앞에서도 눈 하나 깜빡하지 않고 모레티의 돈세탁 루트가 이미 우리 손안에 있음을 상기시키세요.",
                  ("Put the piece away, Moretti. Before you pull that trigger, remember who controls your offshore laundering channels in Zurich. You shoot me, your entire empire starves by morning.",
                   "총 집어넣어, 모레티. 그 방아쇠를 당기기 전에 취리히에 있는 네 해외 돈세탁 파이프라인을 누가 쥐고 있는지 기억해라. 날 쏘는 순간 네 제국은 내일 아침 굶어 죽는다.",
                   "‘put the piece away’와 ‘offshore laundering channels’는 상대의 물리적 위협을 금융 급소로 단칼에 제압하는 명대사입니다."),
                  ("Please don't shoot, let's play rock paper scissors.",
                   "제발 쏘지 마세요, 가위바위보로 결정합시다.",
                   "자폭에 가까운 우스꽝스러운 발언입니다."),
                  ("You have bad manner so say sorry to our Don.",
                   "매너가 안 좋으시니 우리 보스께 사과하세요.",
                   "‘manner’는 콩글리시입니다."))
                 ,
                 ("Moretti lowered his weapon. His hands are trembling. He asks what territorial split we offer if he backs down from Manhattan.",
                  "모레티가 총을 내렸어. 손을 떨고 있군. 맨해튼에서 물러난다면 어떤 구역 분할 조건을 제시할 것인지 묻고 있다.",
                  "뉴저지 항만 화물 운송권 40%를 양도하되 맨해튼 전역과 금융가는 건드리지 않는 불가침 조약을 맺으세요.",
                  ("We grant you forty percent of the New Jersey cargo freight, but Manhattan and the financial district remain strictly Falcone territory. Sign the accord or drown.",
                   "뉴저지 화물 운송 이권의 40%를 넘겨주지. 단, 맨해튼과 금융가는 철저히 팔코네의 불가침 구역이다. 협약에 서명하든가 파멸하든가 둘 중 하나를 골라라.",
                   "‘strictly Falcone territory’와 ‘sign the accord or drown’은 보스의 위엄을 극대화하는 최후통첩입니다."),
                  ("Take everything you want, we don't mind.",
                   "원하는 걸 다 가져가세요, 우린 상관없습니다.",
                   "패밀리의 이권을 거저 헌납하는 배임 행위입니다."),
                  ("Check your handphone for calculator.",
                   "계산기를 두드리려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("Moretti signed! The bloodbath is over, the peace treaty is sealed, and the syndicate is unified under our supreme banner. You brought peace through strength.",
                  "모레티가 서명했다! 유혈 사태는 끝났고 평화 협정이 체결되었으며 암흑가는 우리 깃발 아래 통합되었다. 자네가 힘을 통해 평화를 쟁취했네.",
                  "진정한 힘은 총탄을 쏘지 않고도 굴복시키는 장악력에 있다고 답하세요.",
                  ("True power isn't about spilling blood, Don Salvatore—it's about making our enemies understand that defying us is suicide. The city is ours.",
                   "진정한 권력은 피를 흘리는 데서 오는 것이 아닙니다, 살바토레 대부님. 우리에게 저항하는 것이 자살행위임을 깨닫게 하는 데서 나옵니다. 이 도시는 우리의 것입니다.",
                   "마피아 보스의 철학을 완성하는 웅장한 피날레입니다."),
                  ("I am glad we can have a party with loud music.",
                   "이제 시끄러운 음악 틀고 파티할 수 있어서 기쁩니다.",
                   "천박한 언행으로 품격을 떨어뜨립니다."),
                  ("Let's do Dutch pay for the treaty champagne.",
                   "평화 협정 샴페인은 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("배신자의 청문회 증언 저지: 비밀 장부 원본 탈환",
             "워싱턴 D.C. 연방 법원 근처 안전가옥. 내일 아침 의회 특별 청문회에서 마피아의 20년 치 범죄 장부를 제출하려는 전직 회계사의 은신처에 단독 침투해 증거를 회수해야 한다.",
             "retrieve the incrimination ledger before the congressional subpoena", "의회 소환 전 범죄 혐의가 담긴 핵심 비밀 장부를 회수할 때 쓰는 표현입니다.",
             [
                 ("Federal marshals have fortified the safehouse! The accountant is clutching the red hard-drive containing forty years of syndicate shell accounts. We have ten minutes.",
                  "연방 보안관들이 안전가옥을 요새화했어! 회계사가 40년 치 페이퍼컴퍼니 비밀 장부가 든 빨간 하드드라이브를 쥐고 있다. 10분 남았어.",
                  "보안 시스템 전원을 차단하고 소음기 장착 권총으로 경호팀을 신속 무력화한 뒤 회계사에게 면담을 요구하세요.",
                  ("Deploy the thermal bypass on their perimeter alarms. Subdue the exterior sentries cleanly, breach the panic room, and put me face-to-face with that accountant.",
                   "외곽 경보기에 열선 바이패스를 설치하십시오. 외부 보초들을 은밀히 제압하고 패닉룸을 돌파해 회계사를 내 앞에 마주 앉히세요.",
                   "‘thermal bypass’와 ‘breach the panic room’은 특수 타격 작전의 긴박감을 재현합니다."),
                  ("Knock on the front door and say we have pizza delivery.",
                   "현관문을 두드리고 피자 배달 왔다고 소리칩시다.",
                   "어설픈 장난으로 무장 경호팀의 사격을 유발합니다."),
                  ("The safehouse lock has bad spec so call AS.",
                   "안전가옥 자물쇠 스펙이 안 좋으니 AS를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("Panic room breached! The accountant is hyperventilating on the floor. He claims the hard-drive is encrypted with a dead-man's key to the FBI director.",
                  "패닉룸 돌파 완료! 회계사가 바닥에서 과호흡을 일으키고 있어. FBI 국장에게 자동 전송되는 데드맨 스위치 암호가 걸려 있다고 주장한다.",
                  "가족들의 안전 보장 각서와 카리브해 스위스 계좌 이전을 교환 조건으로 제시해 암호를 해제하게 만드세요.",
                  ("Hand over the decryption cipher right now. In return, I guarantee your family's boarding passes to Grand Cayman with clean passports. Refuse, and you face the void.",
                   "지금 당장 복호화 암호를 넘겨라. 그 대가로 그랜드케이먼행 가족 탑승권과 위조 없는 클린 여권을 보장해주지. 거부하면 네겐 오직 영원한 어둠뿐이다.",
                   "‘decryption cipher’와 ‘face the void’는 극도의 압박과 탈출구를 동시에 제시하는 심리 협상의 극치입니다."),
                  ("Please tell me the password because I forgot mine too.",
                   "저도 비밀번호를 자주 잊어버리니 제발 알려주세요.",
                   "어이없는 실언으로 주도권을 상실합니다."),
                  ("Check your handphone for password cracking apps.",
                   "비밀번호 해킹 앱을 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("The drive is wiped, the ledger is in ashes, and the accountant vanished to the islands! The Senate hearing collapsed with zero evidence! Salvatore Falcone is untouchable.",
                  "하드드라이브는 포맷되었고 장부는 재가 되었으며 회계사는 섬으로 증발했다! 상원 청문회는 증거 부족으로 와해되었네! 살바토레 팔코네는 불가침의 지배자다.",
                  "기록은 불타 없어졌지만 패밀리의 전설은 영원할 것이라고 화답하세요.",
                  ("Paper burns, Don Salvatore, and digital traces evaporate. But the empire we built on silence will outlive every prosecutor in Washington. Salute.",
                   "종이는 불타고 디지털 흔적은 증발합니다, 살바토레 대부님. 하지만 우리가 침묵 위에 세운 제국은 워싱턴의 모든 검사들보다 오래 살아남을 것입니다. 경의를 표합니다.",
                   "시리즈의 서사를 완결 짓는 불멸의 마피아 명대사입니다."),
                  ("I am glad we don't have to study law books.",
                   "이제 법률 공부 안 해도 돼서 참 좋습니다.",
                   "가벼운 잡담으로 품위를 해칩니다."),
                  ("Let's do Dutch pay for the celebration whisky.",
                   "축하 위스키는 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    # 25. Formula 1 Motor Racing
    add_g(
        "Formula 1 Motor Racing", "Toto Wolff (Mercedes Team Principal)", "🏎️",
        [
            ("모나코 그랑프리 빗속 타이어 교체 2.1초 피트스톱 결단",
             "모나코 몬테카를로 서킷. 랩 58에서 갑작스러운 국지성 폭우가 쏟아지는 가운데, 1위를 달리던 드라이버에게 슬릭 타이어를 버리고 인터미디어트로 교체할 것을 지시해야 한다.",
             "box for intermediate tires in sudden torrential rain", "갑작스러운 폭우 시 즉각 피트인하여 인터미디어트 타이어로 교체할 때 쓰는 표현입니다.",
             [
                 ("Rain is pelting down at Turn 3! Max is catching us by two seconds per lap on wet track! Our tires have zero grip! Do we stay out or box this lap?",
                  "3번 코너에 폭우가 쏟아져! 막스가 젖은 노면에서 랩당 2초씩 좁혀오고 있어! 우리 타이어는 접지력이 제로야! 이번 랩에 버틸까, 피트인할까?",
                  "지체 없이 박스 호출을 내리고 피트 크루 전원에게 2초 컷 인터미디어트 교체를 대기시키라고 무전하세요.",
                  ("Box, box, box! Confirming inters! We have an eight-second gap to Verstappen. Crew, green tires ready in pit lane! Two seconds flat, let's execute!",
                   "박스, 박스, 박스! 인터미디어트 확인! 베르스타펜과 8초 차이다. 피트 크루, 인터 타이어 피트 레인 대기! 2.0초 플랫으로 간다, 실행해!",
                   "‘Box, box, box’와 ‘confirming inters’는 실제 F1 팀 라디오의 긴박감을 그대로 재현한 명대사입니다."),
                  ("Drive slower so you don't slip on the rain puddles.",
                   "물웅덩이에서 미끄러지지 않게 그냥 천천히 달리세요.",
                   "F1의 스피드 경쟁을 완전히 포기하는 발언입니다."),
                  ("The race car spec is bad so call the pit AS center.",
                   "레이스 카 스펙이 안 좋으니 피트 AS 센터를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("Pit stop complete: 2.1 seconds! Incredible stop! But Verstappen stayed out on slicks and is aquaplaning! He's blocking the apex at Casino Square!",
                  "피트스톱 완료: 2.1초! 경이적인 스톱이었어! 하지만 베르스타펜이 슬릭 타이어로 버티다 수막현상으로 미끄러지고 있어! 카지노 스퀘어 에이펙스를 막고 있다!",
                  "젖은 연석을 피해 DRS 없이 언더컷 가속으로 터널 입구에서 아웃사이드 추월을 감행하라고 지시하세요.",
                  ("Do not lift through the tunnel! He has zero lateral grip on those cold slicks. Sell the dummy inside and take him on the outside into the chicane!",
                   "터널 통과할 때 가속 페달에서 발 떼지 마! 놈은 차가운 슬릭 때문에 횡접지력이 제로야. 안쪽으로 속임수를 주고 시케인 진입 직전 아웃사이드로 따돌려라!",
                   "‘sell the dummy’와 ‘outside into the chicane’은 초특급 레이싱 추월 전술입니다."),
                  ("Honk your horn loudly so he moves his car out of the way.",
                   "경적을 크게 울려서 차를 옆으로 비키라고 하세요.",
                   "F1 머신에는 경적이 없다는 상식도 모르는 망발입니다."),
                  ("Check your handphone for GPS navigation directions.",
                   "GPS 내비게이션 경로를 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("Chequered flag! Lewis crosses the line! Monaco Grand Prix victory! Fastest lap bonus point secured! The paddock is chanting your name, Toto!",
                  "체커드 플래그! 루이스가 결승선을 통과했다! 모나코 그랑프리 우승! 패스티스트 랩 보너스 포인트까지 획득! 패독이 당신 이름을 연호하고 있어, 토토!",
                  "완벽한 팀워크와 데이터 중심의 냉철한 판단이 만들어낸 승리라고 화답하세요.",
                  ("Absolute masterclass from the entire team. Cold data, fearless strategy, and sheer perfection in the pit lane. That is how champions race.",
                   "팀 전체가 일궈낸 완벽한 마스터클래스였습니다. 냉철한 데이터, 두려움 없는 전략, 피트 레인에서의 무결점 실행. 이것이 챔피언이 달리는 방식입니다.",
                   "토토 볼프의 완벽주의 리더십을 상징하는 명대사입니다."),
                  ("I am glad we don't have to change tires tomorrow.",
                   "내일은 타이어 교체 안 해도 돼서 참 다행입니다.",
                   "프로 스포츠의 치열함을 깎아내리는 실언입니다."),
                  ("Let's do Dutch pay for the podium champagne.",
                   "포디움 샴페인 값은 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("아부다비 최종전 챔피언십 결전: 오버컷 vs 언더컷 전략",
             "야스 마리나 서킷. 시즌 최종전 챔피언십 포인트 동점 상황. 라이벌 팀 레드불의 깜짝 피트스톱에 맞서 오버컷으로 트랙 포지션을 사수해야 한다.",
             "execute an overcut strategy to defend track position", "타이어 마모를 한계까지 버티며 랩타임을 유지해 역전 피트스톱을 달성할 때 쓰는 표현입니다.",
             [
                 ("Red Bull just pulled Max in for fresh softs on Lap 40! If we pit now, we emerge three seconds behind in heavy traffic! Do we overcut?",
                  "레드불이 40랩에 막스를 불러들여 소프트 타이어를 끼웠어! 지금 피트인하면 백마커 트래픽 속에 3초 뒤처져 나오게 돼! 오버컷으로 갈까?",
                  "타이어 잔여 수명을 극한까지 쥐어짜내며 3랩 동안 해머 타임으로 격차를 벌리라고 무전하세요.",
                  ("Stay out! Hammer time, Lewis! Empty track ahead. Give me qualifying laps for the next three stints. We overcut them in the pit window!",
                   "트랙에 머물러라! 해머 타임이다, 루이스! 앞이 뻥 뚫렸어. 다음 3랩 동안 예선 주행 모드로 한계를 뽑아내라. 피트 윈도우에서 오버컷으로 잡는다!",
                   "‘Hammer time’과 ‘qualifying laps’는 메르세데스 F1의 전설적인 무전 지령입니다."),
                  ("Turn off the engine to save gasoline.",
                   "휘발유를 아끼기 위해 시동을 끄세요.",
                   "레이스 중 엔진을 끄라는 어처구니없는 조언입니다."),
                  ("The steering wheel has bad spec so call AS.",
                   "스티어링 휠 스펙이 안 좋으니 AS를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("Gap is plus twenty-four seconds! Red Bull is stuck behind a Williams! Lewis is flying through sector two! Boxing this lap for the lead!",
                  "격차가 24초로 벌어졌어! 레드불이 윌리엄스 머신에 막혀 고전 중이야! 루이스가 2번 섹터를 날아다니고 있어! 선두 탈환을 위해 이번 랩에 들어온다!",
                  "미디엄 컴파운드로 신속 교체하고 피트 출구에서 블라인드 스팟을 방어하라고 지시하세요.",
                  ("Yellow medium compound fitted! Release him now! Defend the inside line at Turn 1 on cold tires! Track position is ours!",
                   "옐로우 미디엄 컴파운드 장착 완료! 지금 릴리스해! 차가운 타이어로 1번 코너 안쪽 라인을 필사적으로 방어해라! 트랙 포지션은 우리 것이다!",
                   "‘track position is ours’는 치열한 F1 피트 전쟁의 승리를 알리는 대사입니다."),
                  ("Let Max pass so nobody gets angry on track.",
                   "트랙에서 싸움 나지 않게 막스가 추월하도록 비켜줍시다.",
                   "챔피언십을 거저 넘겨주는 패배주의 발언입니다."),
                  ("Check your handphone for race standings.",
                   "레이스 순위를 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("World Drivers' Championship won! Lewis wins the eighth title! Pure strategic perfection under unbelievable pressure! Toto, history is rewritten!",
                  "드라이버 월드 챔피언십 우승! 루이스의 통산 8번째 월드 챔피언 등극! 믿을 수 없는 압박 속에서 이뤄낸 순수한 전략적 완벽성! 토토, 역사가 다시 쓰였어!",
                  "이 승리는 공학적 한계를 돌파한 수천 명의 브랙클리 공장 엔지니어들의 몫이라고 답하세요.",
                  ("This title wasn't won in forty laps—it was built in Brackley by a thousand souls pushing every micron of aerodynamic perfection. We reign supreme.",
                   "이 타이틀은 40랩 만에 얻은 것이 아닙니다. 브랙클리 공장에서 1마이크론의 공기역학적 완벽함을 위해 한계를 밀어붙인 천 명의 영혼들이 만든 것입니다. 우리는 최고입니다.",
                   "모터스포츠의 엔지니어링 미학을 노래하는 품격 있는 연설입니다."),
                  ("I am glad the loud engine sound stopped.",
                   "시끄러운 엔진 소리가 멈춰서 참 좋습니다.",
                   "모터스포츠 팬들의 열정을 무시하는 망언입니다."),
                  ("Let's do Dutch pay for the championship trophy.",
                   "챔피언십 트로피 제작비는 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("예선 Q3 마지막 1초: 몬차 서킷 슬립스트림 토우 작전",
             "이탈리아 몬차 국립 서킷. 템플 오브 스피드. 1/1000초 차이로 폴 포지션이 갈리는 Q3 세션 종료 40초 전, 두 드라이버의 공기역학적 슬립스트림 토우를 완벽히 정렬해야 한다.",
             "execute a synchronized slipstream tow down the straight", "직선 구간에서 앞차의 후류를 이용해 최고 속도를 끌어올리는 슬립스트림 작전을 펼칠 때 쓰는 표현입니다.",
             [
                 ("Forty seconds left on the clock! All ten cars are crawling out of the pit lane playing chicken! If we don't cross the start line before zero, no lap time!",
                  "세션 종료 40초 전! 10대 전원이 눈치싸움을 벌이며 피트 레인을 기어가고 있어! 0초 전에 결승선을 넘지 못하면 랩타임 측정도 못 해!",
                  "트래픽 큐를 즉시 추월해 조지와 루이스를 2초 간격으로 배치하고 파라볼리카 탈출 토우를 전개하라고 지시하세요.",
                  ("Jump the queue on the pit exit! George leads, Lewis tucks into his slipstream at three car lengths. Punch a hole in the air through the Curva Grande!",
                   "피트 출구에서 줄서기를 제치고 나가! 조지가 앞서고, 루이스는 3대 차체 간격으로 후류에 바짝 붙는다. 쿠르바 그란데에서 공기를 갈라 길을 열어줘라!",
                   "‘jump the queue’와 ‘punch a hole in the air’는 몬차 서킷의 전형적인 슬립스트림 전술입니다."),
                  ("Drive backwards to avoid touching other cars.",
                   "다른 차와 부딪히지 않게 후진해서 빠져나옵시다.",
                   "F1 규정을 어겨 실격당하는 상식 밖의 행동입니다."),
                  ("The telemetry spec has bad error so call AS.",
                   "원격 측정 스펙에 에러가 났으니 AS를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("Both cars crossed with one second to spare! George gave Lewis a massive aerodynamic tow! Lewis is up three-tenths in Sector 1! But tires are overheating in Parabolica!",
                  "두 차 모두 1초 남기고 결승선 통과! 조지가 루이스에게 엄청난 공기역학 토우를 주었어! 루이스가 1섹터에서 0.3초 앞서가고 있다! 하지만 파라볼리카에서 타이어가 과열 중이야!",
                  "스티어링 각도를 최소화하고 풀 파워 엔진 모드로 직선 가속에 모든 것을 걸라고 독려하세요.",
                  ("Unleash engine Mode 1! Minimum steering input through the apex, preserve the rear tires, and pin the throttle onto the main straight! Bring it home!",
                   "엔진 모드 1을 해제해라! 에이펙스에서 스티어링 꺾임을 최소화해 후륜 타이어를 살리고, 메인 직선에서 풀 스로틀을 꽂아 넣어라! 폴 포지션을 가져와!",
                   "‘unleash Mode 1’과 ‘pin the throttle’은 드라이버의 아드레날린을 폭발시키는 무전입니다."),
                  ("Close your eyes if you are scared of the speed.",
                   "스피드가 무서우면 그냥 눈을 감고 달리세요.",
                   "시속 350km에서 대형 참사를 부르는 자살행위입니다."),
                  ("Check your handphone for lap time alerts.",
                   "랩타임 알림을 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("Pole position! New Monza lap record! Front row lockout for Mercedes! The Tifosi are stunned in silence! What an engineering triumph!",
                  "폴 포지션! 몬차 서킷 랩 레코드 경신! 메르세데스의 프런트 로 독점! 티포시(페라리 팬들)가 충격에 빠져 침묵하고 있어! 경이적인 엔지니어링 승리다!",
                  "완벽한 팀워크와 공기역학의 조화가 불가능을 가능으로 만들었다고 자축하세요.",
                  ("When two drivers execute as one aerodynamic machine, physics bends to our will. Tomorrow, we turn this front row into a dominant one-two finish.",
                   "두 드라이버가 하나의 공기역학 머신처럼 움직일 때 물리학도 우리의 의지에 굴복합니다. 내일, 이 프런트 로를 압도적인 원투 피니시로 바꿔놓겠습니다.",
                   "F1 팀 수장의 카리스마 넘치는 인터뷰입니다."),
                  ("I am glad we don't have to drive fast until tomorrow.",
                   "내일까지는 빨리 안 달릴 수 있어서 다행입니다.",
                   "긴장감을 떨어뜨리는 무성의한 대답입니다."),
                  ("Let's do Dutch pay for the pit garage pizza.",
                   "피트 차고 피자는 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("비용 상한선 규정 위반 혐의 FIA 청문회 돌파",
             "파리 FIA(국제자동차연맹) 본부. 라이벌 팀들의 담합으로 제기된 500만 달러 비용 상한선(Cost Cap) 초과 혐의에 대해 풍동 실험실 및 탄소섬유 연구개발비 회계의 투명성을 입증해야 한다.",
             "defend cost cap compliance before the FIA tribunal", "FIA 조사위원회에서 재정 규정 준수와 합법적 R&D 회계를 입증할 때 쓰는 표현입니다.",
             [
                 ("Red Bull and Ferrari are demanding our disqualification! They claim our upgraded front wing exceeded the budget cap by four million pounds! The stewards are waiting.",
                  "레드불과 페라리가 우리 실격을 요구하고 있어! 신형 프런트 윙이 예산 상한선을 400만 파운드 초과했다고 주장한다! 심사위원들이 기다리고 있다.",
                  "독립 회계 감사 보고서와 풍동 시간 환산표를 제출하여 합법적인 파워트레인 R&D 비용임을 반박 불가능하게 증명하세요.",
                  ("Lay the forensic audit from Deloitte on the table. Every single pound spent on composite aero testing falls strictly under permitted power-unit R&D exclusions. We are compliant to the penny.",
                   "딜로이트 포렌식 감사 보고서를 테이블에 펼치십시오. 복합소재 공기역학 테스트에 쓰인 모든 파운드는 허용된 파워트레인 R&D 예외 조항에 완벽히 부합합니다. 우린 1페니까지 규정을 준수했습니다.",
                   "‘forensic audit’과 ‘compliant to the penny’는 FIA의 법적 공세를 완벽히 차단하는 기업 방어 논리입니다."),
                  ("Tell the judges that we are too famous to be punished.",
                   "심사위원들에게 우린 너무 유명해서 처벌받을 수 없다고 우깁시다.",
                   "오만한 태도로 가중 처벌을 받게 됩니다."),
                  ("The accounting spec has bad error so call AS.",
                   "회계 스펙에 에러가 났으니 AS를 부릅시다.",
                   "‘spec’과 ‘AS’는 콩글리시입니다."))
                 ,
                 ("The stewards cross-examined our chief aerodynamicist for three hours. The Ferrari delegation is trying to contest our wind tunnel sensor telemetry calibration.",
                  "심사위원들이 우리 공기역학 수석을 3시간 동안 교차 검증했어. 페라리 대표단이 풍동 센서 원격 계측 보정치를 문제 삼으려 하고 있다.",
                  "FIA 인증 봉인 장치와 실시간 클라우드 로그를 제시하여 측정 오차가 0%임을 쐐기 박으세요.",
                  ("Our wind tunnel sensors are cryptographically sealed and synced live to FIA servers. Any claim of discrepancy is willful ignorance. Dismiss the protest with prejudice.",
                   "우리 풍동 센서는 암호화 봉인되어 FIA 서버에 실시간 동기화됩니다. 불일치 주장은 고의적인 무지에 불과합니다. 상대의 이의 제기를 영구 기각하십시오.",
                   "‘cryptographically sealed’와 ‘dismiss the protest with prejudice’는 상대의 트집을 분쇄하는 결정타입니다."),
                  ("Cry loudly and beg the stewards for mercy.",
                   "크게 울면서 심사위원들에게 자비를 구합시다.",
                   "메르세데스의 명예를 실추시키는 부끄러운 행동입니다."),
                  ("Check your handphone for racing gossip blogs.",
                   "레이싱 가십 블로그를 보려고 핸드폰을 켜세요.",
                   "‘handphone’은 콩글리시입니다."))
                 ,
                 ("Full exoneration! The FIA dismissed all charges! Ferrari's protest rejected with legal penalties! Our technical integrity stands pristine across the sport!",
                  "완전 무혐의! FIA가 모든 혐의를 기각했다! 페라리의 항의는 기각되고 벌금형이 내려졌어! 우리 팀의 기술적 청렴성은 모터스포츠 전역에서 무결함이 입증되었네!",
                  "승리는 트랙 위에서뿐만 아니라 규정 준수의 정직함 속에서도 증명되는 것이라고 화답하세요.",
                  ("Integrity is non-negotiable. Our rivals can try to beat us with lawyers in boardrooms, but we will always answer them where it matters—on the racetrack.",
                   "청렴성은 타협할 수 없는 가치입니다. 라이벌들이 회의실에서 변호사들을 동원해 우리를 꺾으려 들겠지만, 우리는 언제나 가장 중요한 곳, 트랙 위에서 답할 것입니다.",
                   "F1 최고 수장의 품격 있는 종전 선언입니다."),
                  ("I am glad we don't have to read financial papers today.",
                   "오늘은 재무 서류 안 읽어도 돼서 참 좋습니다.",
                   "가벼운 농담으로 승리의 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the legal counsel coffee.",
                   "변호사 커피값은 더치페이합시다.",
                   "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    return data

