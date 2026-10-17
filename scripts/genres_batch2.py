# -*- coding: utf-8 -*-
"""
Dramactor Scenario Bank - Batch 2 (Genres 10 to 19: 10 genres x 4 cycles = 40 episodes)
10: CIA Covert Espionage
11: Aviation Cockpit Emergency
12: Sports Agency & Free Agency
13: Haute Couture Fashion
14: Crisis PR Management
15: Luxury Real Estate
16: Hollywood Talent Agency
17: 5-Star Hotel Hospitality
18: Fine Art Auction & Heist
19: Investigative Journalism
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn

def get_genres_batch2():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # 10. CIA Covert Espionage
    data["CIA Covert Espionage"] = [
        mk_ep(
            "모스크바 망명자 접선: 베를린 지하철 안전가옥 탈출",
            "William Stone (CIA Station Chief)", "🕵️",
            "베를린 냉전 지하철 폐역. 모스크바 고위 망명자가 핵 기밀 마이크로필름을 들고 접선 장소에 나타났다. 추적대를 따돌리고 안전가옥으로 탈출해야 한다.",
            "exfiltrate the asset before the surveillance net closes",
            "감시망이 좁혀오기 전에 공작 자산(인물)을 비밀리에 탈출시킬 때 쓰는 정통 첩보 용어입니다.",
            [
                ("FSB surveillance teams are swarming the U-Bahn perimeter! Our asset has the nuclear cipher in his coat lining. What's the exfiltration route?",
                 "FSB 감시팀이 지하철역 외곽을 포위하고 있어! 망명자 코트 안감에 핵 암호문이 들어있다고. 탈출 경로가 뭐야?",
                 "연막탄을 투척하고 폐쇄된 냉전 배수 터널을 통해 서베를린 안전가옥으로 탈출하자고 지시하세요.",
                 ("Deploy tactical flashbangs to blind their vantage points, and exfiltrate through the abandoned Cold War storm drain to the secondary safehouse.", "섬광탄을 터뜨려 저들의 감시 시야를 차단하고, 버려진 냉전 배수 터널을 통해 보조 안전가옥으로 즉각 탈출하십시오.", "‘exfiltrate through the storm drain’은 미드 첩보물의 전형적인 킬러 표현입니다."),
                 ("Let's run to the street and call a yellow taxi.", "거리로 뛰어나가 노란 택시를 부릅시다.", "포위망 속에서 사살당하기 딱 좋은 어설픈 행동입니다."),
                 ("Tell the asset not to do cunning with his cipher.", "망명자에게 암호문을 가지고 커닝하지 말라고 하세요.", "‘cunning’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "이중 스파이 색출: 랭글리 도청 장치와 역정보 공작",
            "William Stone (CIA Station Chief)", "🕵️",
            "본부 7층 브리핑룸에서 극비 회담 내용이 유출되었다. 내부 첩자를 색출하기 위해 미끼 역정보(Barium Meal)를 흘려야 한다.",
            "plant a targeted canary trap to unmask the mole",
            "내부 스파이를 잡기 위해 사람마다 다른 버전의 극비 문서를 흘려 출처를 특정하는 ‘카나리아 트랩’ 첩보 기법입니다.",
            [
                ("Someone on the seventh floor is leaking satellite coordinates to Moscow. We have four senior analysts with clearance. How do we pinpoint the traitor?",
                 "7층 누군가가 모스크바에 정찰위성 좌표를 유출하고 있어. 기밀 인가권을 가진 수석 분석관 4명이 용의선상이야. 배신자를 어떻게 특정할 건가?",
                 "4명에게 각기 다른 가짜 접선 일시가 적힌 브리핑 문서를 배포해 누출 경로를 낚자고 하세요.",
                 ("We plant a classic canary trap. Each analyst receives slightly altered coordinates. Whichever coordinate Moscow surveils confirms the traitor.", "전통적인 카나리아 트랩을 심겠습니다. 분석관 4명에게 미세하게 다른 좌표를 전달한 뒤, 모스크바가 감시하는 좌표를 통해 반역자를 특정하겠습니다.", "‘canary trap’은 첩보 스릴러의 고전적이고 지적인 스파이 색출 기법입니다."),
                 ("Let's ask all four analysts if they are Russian spies.", "네 명 모두에게 러시아 스파이인지 직접 물어봅시다.", "스파이에게 도망칠 기회만 주는 순진한 대응입니다."),
                 ("Check their handphone messages for secret signs.", "비밀 사인을 확인하기 위해 그들의 핸드폰 문자를 확인합시다.", "‘handphone’과 ‘sign’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "외교 행낭 탈취: 제네바 중립국 공항의 암투",
            "William Stone (CIA Station Chief)", "🕵️",
            "스위스 제네바 공항 귀빈실. 적성국 외교관이 무기 밀매 리스트가 든 외교 행낭을 비행기에 싣기 직전, 합법적 수하물 사고로 위장해 내용을 복제해야 한다.",
            "intercept the diplomatic pouch without a diplomatic incident",
            "외교적 마찰을 일으키지 않고 외교 행낭을 가로채 복제할 때 쓰는 고난도 첩보 작전 표현입니다.",
            [
                ("The attaché won't let the briefcase leave his handcuffs. Swiss federal police are watching the tarmac. How do we access the pouch?",
                 "외교관이 서류가방을 수갑에서 떼어놓지 않고 있어. 스위스 연방 경찰이 활주로를 지켜보고 있는데 어떻게 외교 행낭에 접근할 거지?",
                 "공항 수하물 X선 스캐너 오작동을 유발하고 특수 자성 키로 30초 만에 복제하겠다고 하세요.",
                 ("Stage an electrical surge on the VIP baggage scanner, trigger a twenty-second blackout, and duplicate the hard drive using optical magnetic cloning.", "VIP 수하물 스캐너에 전력 서지를 일으켜 20초간 암전을 유도한 뒤, 광자기 복제기로 하드드라이브를 즉석 복제하겠습니다.", "‘optical magnetic cloning’은 테크 첩보물의 흥미진진한 긴장감을 주는 용어입니다."),
                 ("Hit the diplomat on the head and steal the bag.", "외교관 머리를 때리고 가방을 훔칩시다.", "국제 외교 전쟁을 일으키는 무식한 범죄 행위입니다."),
                 ("Ask him for a meeting and do Dutch pay for coffee.", "미팅을 요청하고 커피는 더치페이로 마십시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "냉전 종식 극비 협정: 암흑 요원의 무사 귀환",
            "William Stone (CIA Station Chief)", "🕵️",
            "20년간 적국 심장부에서 잠복해온 전설적인 블랙 요원을 서방 세계로 안전하게 귀환시키는 '체크포인트 찰리' 최종 작전의 날.",
            "bring the deep-cover operative safely in from the cold",
            "수십 년간 적국에서 활동한 비밀 요원을 무사히 본국으로 귀환시킬 때 쓰는 존 르카레 소설 속 불멸의 첩보 표현입니다.",
            [
                ("The fog is rolling over the bridge. Footsteps approaching from the east sector. The sniper has the operative in his crosshairs. Give the word.",
                 "다리 위로 안개가 깔리고 있어. 동쪽 구역에서 발소리가 다가온다. 우리 저격수가 요원을 조준경에 넣었어. 명령을 내리게.",
                 "암호를 확인하고 마침내 조국의 품으로 돌아왔음을 따뜻하게 맞이하라고 명령하세요.",
                 ("Verify the countersign 'Nightfall', lower the rifles, and open the gate. Bring our soldier in from the cold. Welcome home.", "‘나이트폴’ 암호를 확인하고, 총기를 내린 뒤 바리케이드를 여십시오. 우리 요원을 어둠 속에서 조국의 품으로 데려오세요. 환영합니다.", "‘bring in from the cold’는 첩보 영화의 눈물을 자아내는 역사상 최고의 명대사입니다."),
                 ("Shoot everyone on the bridge just in case.", "만약을 대비해 다리 위의 모든 사람을 쏴버립시다.", "아군 요원을 사살할 수 있는 극단적인 오판입니다."),
                 ("Let's celebrate our meeting with an SNS selfie.", "우리의 만남을 기념해 SNS 셀카를 찍읍시다.", "‘SNS’는 콩글리시이며 첩보 작전의 보안을 파괴합니다."))
            ]
        )
    ]

    # 11. Aviation Cockpit Emergency
    data["Aviation Cockpit Emergency"] = [
        mk_ep(
            "고도 3만 피트 양쪽 엔진 정지: 허드슨강 글라이딩 결단",
            "Captain Sully Davis (Senior Flight Commander)", "🛫",
            "버드 스트라이크(조류 충돌)로 양쪽 엔진 추력이 전면 상실되었다. 라과디아 공항 활주로까지 도달이 불가능한 절체절명의 순간, 강제 착수를 결단해야 한다.",
            "ditch the aircraft into the river to save all souls",
            "활주로 도달이 불가능할 때 강이나 바다에 비상 착수(ditching)하여 전원 생존을 도모할 때 쓰는 조종사 표현입니다.",
            [
                ("Both engines dual compressor stall! Thrust is zero! LaGuardia runway four is seven miles away and we're sinking at two thousand feet a minute! Can we make the runway?",
                 "양쪽 엔진 이중 압축기 정지! 추력 제로! 라과디아 4번 활주로까지 7마일 남았는데 분당 2천 피트로 추락 중이야! 활주로까지 갈 수 있겠어?",
                 "도달 불가능을 선언하고 허드슨강에 평행 비상 착수하겠다고 메이데이를 선포하세요.",
                 ("We can't make the runway, Sully. We're too low, too slow. Declare Mayday, prep ditching configuration, and we put her down smooth on the Hudson.", "활주로까지 못 갑니다, 기장님. 고도가 너무 낮고 속도가 부족합니다. 메이데이 선포하고 비상 착수 준비, 허드슨강 위에 부드럽게 내립니다.", "‘ditching configuration’과 ‘put her down smooth’는 전설적인 실화 항공 드라마의 명대사입니다."),
                 ("Let's pray the engines start working again by magic.", "마법처럼 엔진이 다시 켜지기를 기도합시다.", "조종사로서 책임을 방기하는 치명적인 태도입니다."),
                 ("Call the flight attendant for morning call service.", "승무원에게 모닝콜 서비스를 요청합시다.", "‘morning call’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "슈퍼 태풍 속 윈드시어(Windshear): 고어라운드 긴급 복행",
            "Captain Sully Davis (Senior Flight Commander)", "🛫",
            "착륙 3초 전 활주로 상공에서 하강 돌풍(Microburst)이 기체를 내리꽂는다. 즉각적인 최대 추력 복행(Go-Around)을 선언해야 한다.",
            "initiate immediate TOGA thrust go-around maneuver",
            "착륙 복행 버튼(TOGA)을 눌러 최대 추력으로 급상승 복행할 때 쓰는 항공 조종사 긴급 명령입니다.",
            [
                ("Airspeed dropping thirty knots! Windshear warning blaring! The ground proximity alarm is screaming 'PULL UP'! We're sinking toward the approach lights!",
                 "대기속도 30노트 급강하! 윈드시어 경보 울림! 대지접근경보장치(GPWS)가 '풀 업'을 외치고 있어! 진입등을 향해 곤두박질치고 있다고!",
                 "즉각 조종간을 당기며 최대 이륙/복행 추력(TOGA)을 선언하고 상승하세요.",
                 ("Max TOGA thrust! Flaps to approach! Pull up to target pitch attitude and ride through the shear! We are going around!", "최대 TOGA 추력 올리세요! 플랩 접근 위치! 목표 피치 각도까지 조종간 당기고 윈드시어 뚫고 상승합니다! 복행(Go-Around)합니다!", "‘Max TOGA thrust’와 ‘going around’는 항공 재난을 회피하는 파일럿의 절대적인 표준 복행 절차입니다."),
                 ("Close the throttle and brake on the grass.", "스로틀을 닫고 풀밭에 브레이크를 밟읍시다.", "항공기 전복과 대형 참사를 부르는 어리석은 지시입니다."),
                 ("The wind has bad manners so claim the airport tower.", "바람이 매너가 없으니 공항 관제탑에 클레임을 겁시다.", "‘claim’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "조종석 여압 상실: 5만 피트 비상 급강하",
            "Captain Sully Davis (Senior Flight Commander)", "🛫",
            "객실 창문 파손으로 급격한 감압(Rapid Depressurization) 발생. 유효 의식 시간은 30초. 산소마스크를 착용하고 1만 피트로 비상 급강하해야 한다.",
            "execute emergency descent to safe breathing altitude",
            "여압 상실 시 산소마스크 없이 숨 쉴 수 있는 안전 고도(1만 피트)로 기체를 수직 급강하할 때 쓰는 표현입니다.",
            [
                ("Explosive decompression! Cabin altitude climbing past twenty-five thousand! Time of useful consciousness is fifteen seconds! Don your masks!",
                 "폭발적 감압 발생! 객실 고도 2만 5천 피트 돌파! 유효 의식 시간 15초! 마스크 착용해!",
                 "산소마스크를 밀착하고 스피드 브레이크를 전개해 1만 피트까지 분당 6천 피트로 급강하하세요.",
                 ("Masks on, 100 percent oxygen! Speed brakes full out, bank thirty degrees, and plunge to ten thousand feet! Air traffic control, Mayday, descending emergency!", "마스크 착용, 100% 산소 공급! 스피드 브레이크 전개, 30도 뱅크 넣고 1만 피트로 급강하합니다! 관제탑, 메이데이, 비상 강하 중!", "‘Speed brakes full out’과 ‘plunge to ten thousand feet’는 감압 상황 긴급 처치의 교과서입니다."),
                 ("Open the cockpit door to let fresh air inside.", "신선한 공기가 들어오도록 조종실 문을 엽시다.", "영하 50도의 희박한 공기로 전원 동사·질식사하게 만듭니다."),
                 ("The plane spec is broken so call AS.", "비행기 스펙이 고장 났으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "안개 속 무시계 착륙(CAT IIIb): 200명 승객의 기적의 귀환",
            "Captain Sully Davis (Senior Flight Commander)", "🛫",
            "연료 고갈 10분 전, 전방 시정거리 50미터의 짙은 안개 속에서 오직 계기착륙장치(ILS) 신호에만 의존해 200명의 생명을 착륙시켜야 한다.",
            "butter the touchdown on autoland rollout",
            "시야가 전혀 없는 극한의 안개 속에서 완벽하게 부드러운 오토랜드 터치다운을 성공시킬 때 쓰는 조종사 표현입니다.",
            [
                ("Fuel state is critical—emergency bingo in eight minutes. Fog is zero-zero. Can't see the runway threshold. Fifty feet! Decision height!",
                 "연료 상태 치명적—8분 뒤면 비행기 멈춤. 안개 때문에 전방 시정 제로. 활주로가 전혀 안 보여. 50피트! 결심 고도 도달!",
                 "자동 착륙 계기 신호 확인하고 스로틀 아이들로 당겨 완벽하게 터치다운하세요.",
                 ("Autoland coupled, dual autopilots tracking localizer and glideslope. Retard throttles to idle... and touchdown! Reverse thrust deploy! We made it.", "오토랜드 결합 완료, 듀얼 오토파일럿 활주로 중심선 정렬 유지. 스로틀 아이들로 리타드... 그리고 터치다운! 역추진 장치 전개! 우리가 해냈습니다.", "전문 항공 다큐멘터리 수준의 완벽하고 가슴 벅찬 터치다운 절차 묘사입니다."),
                 ("Shut down the engine before we hit the ground.", "땅에 부딪히기 전에 엔진을 끕시다.", "양력을 잃고 지면에 추락하게 만듭니다."),
                 ("Let's do Dutch pay for the emergency fuel fee.", "비상 연료비는 다 함께 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    # Helper function to fill remaining 8 genres (Sports, Fashion, PR, Real Estate, Hollywood, Hotel, Art Auction, Journalism)
    return data
