# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack A: Genres 17 to 27 (11 genres x 4 = 44 episodes)
17: 5-Star Hotel Hospitality
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

def get_gen_pack_a():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    # 17. 5-Star Hotel Hospitality
    data["5-Star Hotel Hospitality"] = [
        mk("사우디 왕실 외교단 프레지덴셜 스위트 철통 보안 봉쇄", "Monsieur Dupont (Grand Hotelier & GM)", "🏨",
           "파리 리츠 호텔. 사우디 왕실 외교단이 전 층을 대관한 가운데, 의문의 파파라치 드론 침투와 도청 의혹이 제기되었다. 총지배인으로서 완벽한 의전과 보안을 지켜내야 한다.",
           "uphold the discreet discretion of royal diplomatic protocol", "왕실 외교 의전의 철통 보안과 품격을 유지할 때 쓰는 호텔리어 전문 표현입니다.",
           [
               ("A surveillance drone crashed onto the royal suite balcony! The prince's security detail is threatening to pull the entire delegation! What's our immediate action?",
                "감시 드론이 왕실 스위트 발코니에 추락했어! 왕자의 경호팀이 대표단 전원 철수를 위협하고 있네! 즉각적인 조치가 뭐야?",
                "해당 층의 주파수 재밍 돔을 즉각 가동하고 현지 대사관 보안팀과 협력해 즉각 전 층을 격리 봉쇄하라고 명령하세요.",
                ("Activate the hotel's RF anti-drone jamming shield immediately. Escort the royal delegation to the armored sub-penthouse while our forensic team traces the drone serial.", "호텔의 무선 주파수 안티드론 재밍 쉴드를 즉시 가동하십시오. 왕실 대표단을 방탄 서브 펜트하우스로 정중히 모시고, 감식팀이 드론 시리얼을 추적하게 하세요.", "‘anti-drone jamming shield’와 ‘armored sub-penthouse’는 5성급 호텔 총지배인의 완벽한 위기 대처입니다."),
                ("Tell the prince that drones are harmless toys.", "왕자님에게 드론은 무해한 장난감이라고 둘러대봅시다.", "국제 외교 참사를 부르는 어리석은 발언입니다."),
                ("The balcony has bad spec so call the AS center.", "발코니 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
               ("The prince is safely moved. But the royal chef refuses to cook without fresh white truffles from Alba by 7 PM. The supplier's truck broke down.",
                "왕자는 안전하게 이동했어. 하지만 왕실 셰프가 저녁 7시까지 알바산 백트러플이 오지 않으면 만찬 조리를 거부하겠대. 납품 트럭이 고장 났어.",
                "호텔 전용 헬기를 이탈리아 피에몬테로 급파해 트러플을 3시간 내 직송해 오라고 지시하세요.",
                ("Scramble the hotel's private charter helicopter to Alba immediately. White-glove courier brings the fresh truffles straight into the royal prep kitchen by 1800 hours.", "호텔 전용 전세 헬기를 즉시 알바로 급파하십시오. 특급 전담 배송원이 저녁 6시까지 왕실 조리실로 백트러플을 직송할 것입니다.", "‘white-glove courier’는 5성급 럭셔리 호텔의 불가능을 모르는 최상급 의전 서비스입니다."),
                ("Tell the prince to eat regular mushrooms today.", "왕자님에게 오늘은 일반 버섯이나 드시라고 권합시다.", "호텔의 성급을 하루아침에 박탈당하는 무례한 행동입니다."),
                ("Check the handphone for delivery updates.", "배송 상태를 보려고 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")),
               ("Royal gala concluded flawlessly! The crown prince presented you with the royal medal of honor and booked the presidential floor for the next five years! Masterful hospitality.",
                "왕실 갈라 만찬 완벽 성료! 왕세자가 자네에게 왕실 명예 훈장을 수여하고 향후 5년간 프레지덴셜 층 전체를 예약했어! 압도적 호스피탈리티였네.",
                "진정한 호텔리어는 손님의 기대치를 뛰어넘어 평생의 안식처를 선사하는 존재라고 답하세요.",
                ("True luxury isn't marble and gold, Dupont—it's crafting an impenetrable sanctuary where emperors feel entirely at peace. Service perfected.", "진정한 럭셔리는 대리석과 황금이 아닙니다, 뒤퐁. 제왕들이 완전한 평온을 느끼는 난공불락의 안식처를 빚어내는 것입니다. 완벽한 서비스였습니다.", "세계 최고 호텔리어의 숭고한 철학을 보여주는 피날레입니다."),
                ("I am glad we don't have to carry heavy bags today.", "오늘 무거운 짐 안 날라도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Parisian wine tonight.", "오늘 밤 파리 와인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("세계 억만장자 결혼식 도난 다이아몬드 목걸이 수색", "Monsieur Dupont (Grand Hotelier & GM)", "🏨",
           "뉴욕 플라자 호텔 그랜드 볼룸. 세계적 금융 가문의 세기의 결혼식 피로연 직전, 신부의 1,000만 달러 해리 윈스턴 다이아몬드 티아라가 스위트룸에서 사라졌다. 경찰 출동 전 은밀히 티아라를 회수해야 한다.",
           "execute a discreet forensic room sweep without alarming high-society guests",
           "상류층 하객들을 동요시키지 않고 은밀한 감식 수색으로 보석을 회수할 때 쓰는 표현입니다.",
           [
               ("The bride is in tears! Ten-million dollar diamond tiara missing from safe! Her father threatens to call the FBI and shut down the ballroom! What's our strategy?",
                "신부가 울음을 터뜨렸어! 금고에서 1,000만 달러 다이아몬드 티아라가 사라졌어! 신부 아버지는 FBI를 불러 볼룸을 폐쇄하겠대! 전략이 뭐야?",
                "공개 수사는 가문의 스캔들을 부르므로 호텔 보안팀의 폐쇄회로 디지털 동선 역추적으로 20분 내 은밀히 해결하겠다고 설득하세요.",
                ("A public FBI raid turns this wedding into a tabloid circus, sir. Give my team twenty minutes. Our forensic biometrics will pinpoint the tiara without a single guest noticing.", "공개 FBI 출동은 이 결혼식을 타블로이드 찌라시 서커스로 만듭니다. 제 팀에 20분만 주십시오. 생체 감식망으로 하객 누구도 눈치채지 못하게 티아라를 찾아내겠습니다.", "‘tabloid circus’와 ‘forensic biometrics’는 혼란을 막고 호텔의 통제력을 입증하는 설득입니다."),
                ("Let's frisk every single wedding guest at the door.", "문앞에서 모든 하객의 몸을 일일이 수색합시다.", "상류층 하객들의 거센 반발과 집단 소송을 부릅니다."),
                ("The safe has bad spec so call the locksmith.", "금고 스펙이 안 좋으니 열쇠공을 부릅시다.", "‘spec’은 콩글리시입니다.")),
               ("Camera logs show the maid's cart entered the suite. But she claims she never touched the jewelry box. She's shivering with fear.",
                "CCTV 기록상 메이드 카트가 스위트에 들어갔어. 하지만 그녀는 보석함을 건드린 적이 없다고 결백을 주장해. 공포에 떨고 있네.",
                "하우스키핑 세탁물 수거 자루를 특수 금속 탐지기로 비파괴 스캔해 린넨 사이에 엉켜 들어간 티아라를 신속히 찾아내세요.",
                ("Scan the laundry collection hampers with non-destructive thermal sensors. The tiara accidentally snagged on the discarded lace duvet during room refresh.", "세탁물 수거함을 비파괴 열감지 센서로 스캔하십시오. 객실 정리 중 폐기된 레이스 이불에 티아라가 우연히 걸려 들어간 것입니다.", "‘non-destructive thermal sensors’는 무고한 직원을 지키고 물건을 찾는 지혜로운 해결책입니다."),
                ("Fire the maid immediately and throw her out.", "메이드를 즉시 해고하고 쫓아내버립시다.", "진실을 밝히지 못하고 호텔 명예만 실추시키는 악수입니다."),
                ("Check the handphone for diamond serial codes.", "다이아몬드 시리얼 코드를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Tiara recovered completely intact! Placed on the bride's head before the organ played! The father wrote a half-million dollar staff bonus check! You saved the day.",
                "티아라 무사 회수 완료! 파이프오르간이 울리기 전 신부의 머리에 씌워졌어! 신부 아버지가 직원들을 위해 50만 달러 보너스 수표를 끊어줬네! 자네가 결혼식을 살렸어.",
                "진정한 호텔리어는 눈에 보이지 않는 기적을 매일 만들어내는 수호자라고 답하세요.",
                ("Discretion, composure, and razor-sharp precision—that is the invisible magic of the grand hotel, Dupont. The bride walks down the aisle.", "신중함, 침착함, 그리고 면도날 같은 정밀함. 그것이 그랜드 호텔의 보이지 않는 마법입니다. 신부가 버진 로드를 걸어갑니다.", "호텔리어의 자부심을 드높이는 감동적인 피날레입니다."),
                ("I am glad we don't have to clean the ballroom floor.", "볼룸 바닥 청소 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the wedding champagne.", "결혼식 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("자선 갈라 자정 정전 사태와 비상 발전기 가동", "Monsieur Dupont (Grand Hotelier & GM)", "🏨",
           "런던 메이페어 5성급 호텔. 영국 총리와 글로벌 억만장자 500명이 참석한 자선 갈라 도중 도심 변전소 폭발로 호텔 전체가 암흑에 휩싸였다. 60초 내 패닉을 막고 행사를 정상화해야 한다.",
           "command uninterrupted emergency transition to secondary generators",
           "정전 시 60초 내 2차 보조 발전기로 무중단 전력 전환을 지휘할 때 쓰는 표현입니다.",
           [
               ("Main grid failed! The ballroom is pitch black! Five hundred VIPs are screaming! The Prime Minister's security is drawing weapons! What's the protocol?",
                "메인 전력망 붕괴! 볼룸이 칠흑 같은 암흑이야! 500명의 VIP가 비명을 지르고 있어! 총리 경호팀이 무기를 꺼내 들고 있네! 매뉴얼이 뭐야?",
                "침착하게 무대 마이크를 잡고 안내 방송을 하며 30초 내 보조 디젤 터빈 발전기를 가동하라고 엔지니어링 룸에 명령하세요.",
                ("Engineering, synchronize auxiliary diesel turbine immediately! Banquet staff, illuminate sterling silver candelabras! I address the room on battery mic.", "기관실, 보조 디젤 터빈 즉시 동기화하십시오! 연회팀, 은식기 촛대에 즉각 불을 밝히세요! 내가 배터리 마이크로 장내를 안정시키겠습니다.", "‘synchronize auxiliary diesel turbine’과 ‘illuminate candelabras’는 암흑의 패닉을 로맨틱한 촛불 파티로 바꾸는 천재적 기지입니다."),
                ("Run outside and yell for the police.", "밖으로 뛰어나가 경찰을 부르며 소리칩시다.", "호텔 총지배인으로서 직무유기이자 공황을 키우는 짓입니다."),
                ("The electricity has bad spec so call the power plant.", "전기 스펙이 안 좋으니 발전소에 전화합시다.", "‘spec’은 콩글리시입니다.")),
               ("Power restored in forty-two seconds! Candelabras gave it a magical ambiance! But the kitchen refrigeration tripped and chilled dessert is melting.",
                "42초 만에 전력 복구 완료! 은촛대가 환상적인 분위기를 연출했어! 하지만 주방 냉동고 차단기가 내려가며 차가운 수플레 디저트가 녹고 있어.",
                "액체 질소를 투입해 영하 196도로 급속 냉동하고 분자 요리 시연으로 포장해 테이블로 서비스하라고 셰프에게 지시하세요.",
                ("Infuse liquid nitrogen across pastry station! Frame the melting soufflé as an avant-garde tableside molecular culinary performance!", "페이스트리 스테이션에 액체 질소를 즉각 분사하십시오! 녹아내리는 수플레를 아방가르드 즉석 분자 요리 퍼포먼스로 프레이밍해 테이블에 서빙하세요!", "‘liquid nitrogen’과 ‘tableside molecular performance’는 위기를 최고의 미식 쇼로 전환하는 위대한 기지입니다."),
                ("Tell the guests that there is no dessert today.", "손님들에게 오늘은 디저트가 없다고 통보합시다.", "만찬의 피날레를 망치는 무성의한 태도입니다."),
                ("Check the handphone for electrician telephone numbers.", "전기기사 전화번호를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("The Prime Minister applauded! The gala raised sixty million dollars, breaking all charity records! The board voted to name the grand ballroom after you!",
                "총리가 기립박수를 보냈어! 갈라 모금액이 6천만 달러를 돌파하며 역사상 모든 자선 기록을 갈아치웠네! 이사회가 그랜드 볼룸에 자네 이름을 헌정하기로 결의했어!",
                "시련이 닥쳤을 때 품격을 잃지 않는 것이 바로 그랜드 호텔의 영혼이라고 답하세요.",
                ("Darkness tests our walls, Dupont, but our grace keeps the light burning within. A magnificent evening for the history books.", "어둠이 우리의 벽을 시험할지라도, 우리의 품격은 내면의 빛을 언제나 밝혀둡니다. 역사에 기록될 장엄한 밤이었습니다.", "5성급 호텔 총지배인의 고결한 승리를 보여주는 피날레입니다."),
                ("I am glad the light bulb is working now.", "전구가 이제 켜져서 참 다행입니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the hotel cocktail tonight.", "오늘 밤 호텔 칵테일은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("세계경제포럼 다보스 VIP 정상회담 미슐랭 룸서비스", "Monsieur Dupont (Grand Hotelier & GM)", "🏨",
           "스위스 알프스 다보스 특급 호텔. 세계 최강대국 정상과 글로벌 테크 총수들의 비공개 심야 회담. 분쟁을 중재할 완벽한 스위스-프랑스 퓨전 코스를 15분 내 조율해야 한다.",
           "deliver impeccable diplomatic catering under high-security lockdown",
           "철통 보안 속에서 국가 정상들의 까다로운 의전과 식단을 완벽히 조율할 때 쓰는 표현입니다.",
           [
               ("The bilateral talks stalled! Both delegations are exhausted and hungry at 2 AM. One president is vegan, the other strictly kosher! Can we feed them in fifteen minutes?",
                "양자 회담이 결렬 위기야! 새벽 2시에 양국 대표단이 지치고 배고파하고 있어. 한쪽 대통령은 비건이고, 상대국 정상은 엄격한 코셔(Kosher) 식단이야! 15분 만에 맞춤식을 낼 수 있겠나?",
                "알프스 야생 버섯 콘소메와 비건 트러플 뇨끼를 코셔 인증 전용 조리기구로 조리해 중립의 맛을 전하라고 지시하세요.",
                ("Prepare our reserve foraged chanterelle consommé with kosher-certified black truffle gnocchi. Neutral, exquisite, and unifying in a single bowl.", "예비 보관된 알프스 야생 꾀꼬리버섯 콘소메에 코셔 인증 흑트러플 뇨끼를 즉시 준비하십시오. 중립적이면서도 정교하며 두 정상을 하나로 묶어줄 것입니다.", "‘kosher-certified black truffle gnocchi’는 까다로운 종교적·외교적 식단을 완벽히 일치시키는 천재적 기획입니다."),
                ("Just order some cheap fast food delivery outside.", "밖에서 싼 패스트푸드 배달이나 시킵시다.", "국가 원수들에 대한 모욕으로 외교 결렬을 부릅니다."),
                ("The chef has bad spec so scold him.", "셰프 스펙이 안 좋으니 혼냅시다.", "‘spec’은 콩글리시입니다.")),
               ("The dishes were served! Tensions dissolved over the broth. But the secret treaty document on the table just had red wine spilled across the signature page!",
                "요리가 나갔어! 따뜻한 국물에 긴장이 풀렸어. 그런데 테이블 위의 비밀 평화 조약 조인서에 레드와인이 쏟아지는 대참사가 발생했어!",
                "호텔 서예 복원 전문가를 즉각 투입해 무수분 펄프 건조기로 3분 만에 조약 문건을 원상 복구하라고 명령하세요.",
                ("Dispatch our master archivist with moisture-free blotting tools and cryogenic restoration pens. Erase the stain and preserve the parchment without a smudge.", "무수분 흡수지와 극저온 복원 펜을 든 수석 고문서 복원사를 즉시 투입하십시오. 얼룩을 완벽히 제거하고 양피지 원본을 흠집 없이 복구하세요.", "‘cryogenic restoration pens’와 ‘preserve the parchment’는 사소한 사고로 조약이 파기되는 것을 막는 호텔의 숨은 저력입니다."),
                ("Tell the presidents to write on a paper napkin.", "대통령들에게 종이 냅킨에 사인하라고 하세요.", "국가 조약의 권위를 땅바닥에 내팽개치는 짓입니다."),
                ("Check the handphone for wine cleaning tips.", "와인 지우는 법을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Parchment restored! The treaty was signed! The two leaders announced a historic peace agreement from our lobby staircase! You served world peace tonight, Dupont.",
                "문건 완벽 복구! 평화 조약 체결 완료! 두 정상이 우리 호텔 로비 계단에서 역사적인 평화 선언을 발표했어! 자네가 오늘 밤 세계 평화를 받들어 모셨네, 뒤퐁.",
                "테이블 위의 환대야말로 전장의 포성을 멈추게 하는 가장 위대한 힘이라고 답하세요.",
                ("The table is where humanity rediscovers common ground, Monsieur Dupont. We simply provided the warmth for peace to take root. Impeccable service.", "테이블이야말로 인류가 공통의 연대감을 재발견하는 곳입니다, 뒤퐁 총지배인. 우리는 평화가 뿌리내릴 수 있도록 따스한 온기를 건넸을 뿐입니다. 완벽한 서비스였습니다.", "5성급 호텔리어의 사명을 역사적 차원으로 승화시키는 웅장한 피날레입니다."),
                ("I am glad we don't have to serve soup anymore.", "이제 수프 서빙 안 해도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Swiss chocolate.", "스위스 초콜릿은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    return data

