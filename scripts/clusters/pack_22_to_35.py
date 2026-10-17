# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack: Genres 22 to 35 (14 genres x 4 = 56 episodes)
22: Space Exploration & Sci-Fi
23: True Crime Detective Noir
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
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_pack_22_to_35():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    def add_g(name, spk, emo, arcs):
        data[name] = [mk(a[0], spk, emo, a[1], a[2], a[3], a[4]) for a in arcs]

    # 22. Space Exploration & Sci-Fi
    add_g(
        "Space Exploration & Sci-Fi", "Commander Miller (Deep Space Flight Director)", "🚀",
        [
            ("화성 거주 기지 초대형 태양 폭풍 긴급 쉘터 대피",
             "화성 올림푸스 기지. 메가톤급 태양 플레어가 기지를 덮치기 15분 전. 방사능 차폐 지하 쉘터로 승무원들을 대피시켜야 한다.",
             "seal the radiation shelter before the solar storm hits", "태양 폭풍 도달 전 방사능 차폐 구역을 밀폐하고 생명유지 시스템을 사수할 때 쓰는 표현입니다.",
             [
                 ("Class-X solar flare detected! Coronal mass ejection arriving in twelve minutes! Radiation shields at thirty percent! Do we evacuate the surface greenhouse?",
                  "X등급 태양 플레어 감지! 코로나 질량 방출 도달까지 12분! 방사능 차폐막이 30%뿐이야! 지상 온실 승무원들을 대피시킬까?",
                  "지상 온실을 즉시 포기하고 모든 대원을 지하 용암동굴 벙커로 10분 내 집결시키라고 명령하세요.",
                  ("Abandon surface greenhouse modules immediately! Lock the airlocks and herd all personnel into the subterranean lava tube shelter now!", "지상 온실 모듈을 즉시 포기하십시오! 에어로크를 폐쇄하고 전 대원을 지금 즉시 지하 용암동굴 쉘터로 대피시키세요!", "‘abandon surface modules’와 ‘subterranean lava tube shelter’는 우주 기지 비상 탈출의 정석 명령입니다."),
                  ("Let's look at the pretty solar storm through the glass window.", "유리창을 통해 예쁜 태양 폭풍을 구경합시다.", "치명적인 방사능 피폭으로 즉사하는 황당한 소리입니다."),
                  ("The spaceship has bad spec so call the AS center.", "우주선 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                 ("Shelter sealed! But the main power cable from the nuclear reactor severed under the magnetic pulse. Oxygen scrubbers have six minutes of battery.",
                  "쉘터 밀폐 완료! 하지만 자기장 펄스로 원자로 주 전력 케이블이 끊어졌어. 산소 발생기 배터리는 6분 남았네.",
                  "예비 초전도 수소 연료전지를 긴급 바이패스로 직결해 산소 공급 라인을 유지하라고 지시하세요.",
                  ("Bypass the primary relay and hotwire the auxiliary hydrogen fuel cell array directly to life support. We hold sixty percent oxygen flow.", "주 릴레이를 바이패스하고 비상 수소 연료전지 어레이를 생명유지 시스템에 직접 직결하십시오. 60% 산소 공급을 유지합니다.", "‘hotwire auxiliary fuel cell’과 ‘life support flow’는 우주 재난 영화의 긴박감을 극대화하는 엔지니어링 대처입니다."),
                  ("Tell the crew to hold their breath for thirty minutes.", "대원들에게 30분 동안 숨을 참으라고 하세요.", "인간의 한계를 모르는 무지한 조언입니다."),
                  ("Check your handphone for NASA weather forecasts.", "NASA 날씨 예보를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Solar storm passed! Radiation levels normalized! Life support stabilized! Mission Control in Houston confirmed zero casualties! You saved Mars base, Commander.",
                  "태양 폭풍 통과! 방사능 수치 정상화! 생명유지 시스템 안정화! 휴스턴 지상 관제소가 사상자 제로를 확인했어! 자네가 화성 기지를 구했네, 사령관.",
                  "우주의 냉혹함 앞에서도 인간의 불굴의 의지가 새로운 세계를 개척한다고 답하세요.",
                  ("Space is merciless, Miller, but human resilience is infinite. We held the frontier, and Mars is still ours. Stand down.", "우주는 냉혹하지만, 인간의 회복력은 무한합니다. 우리는 개척지를 지켜냈고 화성은 여전히 우리의 것입니다. 상황 종료.", "인터스텔라와 마션을 연상시키는 웅장한 피날레입니다."),
                  ("I am glad we don't have to clean the space suit now.", "이제 우주복 청소 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the freeze-dried space pizza.", "동결건조 우주 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("지구 궤도 도킹 슬러스터 폭발 충돌 회피 기동", "국제우주정거장(ISS) 도킹 직전 RCS 추진기 폭주로 충돌 궤도에 진입한 우주선을 수동 제어로 회피시켜야 한다.",
             "execute manual RCS retrograde burn to avoid orbital collision", "추진기 폭주 시 수동 역추진 분사로 궤도 충돌을 긴급 회피할 때 쓰는 표현입니다.",
             [
                 ("Stuck thruster on quad-two! Spacecraft spinning at fifteen degrees per second! We are on direct collision course with the solar array in forty seconds!",
                  "2번 쿼드 추진기 고착! 우주선이 초당 15도로 회전하고 있어! 40초 뒤 정거장 태양전지판과 정면충돌 궤도야!",
                  "오토파일럿을 즉시 분리하고 수동 수직 펄스 역분사로 회전 모멘텀을 상쇄하라고 명령하세요.",
                  ("Disengage autopilot! Kill thruster manifold two, switch to manual pulse control, and fire opposite yaw verniers to cancel rotational inertia!", "오토파일럿 즉각 해제! 2번 매니폴드 차단하고 수동 펄스 제어로 전환해 반대편 요(Yaw) 버니어 추진기를 분사해 회전 관성을 상쇄하세요!", "‘disengage autopilot’과 ‘cancel rotational inertia’는 우주 도킹 참사를 막는 베테랑 조종술입니다."),
                  ("Let's close our eyes and hope we bounce off.", "눈을 감고 튕겨 나가길 바랍시다.", "수억 달러 정거장을 파괴하고 전원 사망하는 자멸수입니다."),
                  ("The thruster spec is bad so call Boeing.", "추진기 스펙이 안 좋으니 보잉에 따집시다.", "‘spec’은 콩글리시입니다.")),
                 ("Spin arrested! But closing velocity is still six meters per second! Station commander says we have eight seconds before impact!",
                  "회전 정지 완료! 하지만 접근 속도가 여전히 초당 6미터야! 정거장 사령관이 충돌 8초 전이라고 외치고 있어!",
                  "비상 질소 추진제를 100% 분사해 정거장 상공 5미터 틈새로 회피 기동하라고 명령하세요.",
                  ("Fire emergency cold-gas nitrogen thrusters at full burst! Pitch up forty degrees and skim five meters over the solar truss!", "비상 질소 가스 추진제를 풀 버스트로 분사하십시오! 기수 40도 들고 태양전지판 트러스 상공 5미터로 스쳐 지나가세요!", "‘cold-gas nitrogen thrusters’와 ‘skim over the truss’는 찰나의 순간 충돌을 피하는 기적의 비행술입니다."),
                  ("Tell the station astronauts to duck their heads.", "정거장 우주비행사들에게 머리 숙이라고 하세요.", "황당하고 무력한 반응입니다."),
                  ("Check your handphone for orbital speed apps.", "궤도 속도 앱을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Clear of the station! Station commander confirmed zero contact! Safely re-aligned for soft dock on port three! You pulled off an impossible orbital save, Miller.",
                  "정거장 회피 완료! 정거장 사령관이 접촉 제로를 확인했어! 3번 도킹 포트에 부드러운 도킹 정대 완료! 불가능한 궤도 회피를 해냈네, 밀러.",
                  "침착함과 훈련된 반사신경이 우주에서 생사를 가른다고 답하세요.",
                  ("Panic has no place in the vacuum of space, Commander. We fly the profile, we trust our hands, and we bring the crew home.", "우주의 진공 속에서 패닉이 들어설 자리는 없습니다, 사령관님. 우리는 비행 매뉴얼을 따르고 손끝을 믿으며 대원들을 집으로 데려옵니다.", "우주 비행사의 진정한 위엄을 보여주는 피날레입니다."),
                  ("I am glad we don't have to float outside today.", "오늘 우주 유영 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the Houston coffee.", "휴스턴 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("우주정거장 산소 발생기 고장 15분 생명유지 사투", "산소 발생기 주 전원 보드가 타버려 이산화탄소가 치솟는 정거장에서 화학 산소 캔들을 긴급 점화해야 한다.",
             "ignite backup chemical oxygen candles to stabilize partial pressures", "산소 결핍 위기 시 비상 화학 산소 캔들을 점화해 분압을 정상화할 때 쓰는 표현입니다.",
             [
                 ("Elektron oxygen generator burned out! CO2 scrubbing failure! Carbon dioxide levels crossing four percent! Crew is experiencing cognitive confusion! What's the remedy?",
                  "일렉트론 산소 발생기 전소! 이산화탄소 흡착 실패! CO2 농도 4% 돌파 중! 승무원들이 인지 혼란을 겪고 있어! 처방이 뭐야?",
                  "리튬 수산화물 캐니스터를 전 모듈에 즉시 수동 장착하고 비상 화학 산소 캔들을 점화하라고 지시하세요.",
                  ("Distribute portable lithium hydroxide scrubbing canisters to all modules! Strike the backup sodium chlorate oxygen candles and restore partial pressure immediately!", "모든 모듈에 휴대용 수산화리튬 흡착 캐니스터를 배포하십시오! 비상 염소산나트륨 산소 캔들을 즉시 점화해 분압을 정상화하세요!", "‘lithium hydroxide canisters’와 ‘sodium chlorate oxygen candles’는 아폴로 13호의 위기를 극복한 역사적 생명유지 화학 공식입니다."),
                  ("Tell the crew to open the window for fresh air.", "신선한 공기를 위해 창문을 열라고 하세요.", "우주의 진공으로 빨려 나가 즉사하는 황당한 소리입니다."),
                  ("The air generator spec is bad so call AS.", "공기 발생기 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                 ("Oxygen candles burning! CO2 levels dropping! But the chemical reaction triggered a false thermal fire alarm in the Russian segment.",
                  "산소 캔들 점화 성공! CO2 농도 감소 중! 그런데 화학 반응열로 인해 러시아 모듈에 화재 오경보가 울렸어.",
                  "환기 덕트를 개방하고 적외선 분광기로 화재가 아닌 정상 열 방출임을 확인해 자동 소화 분말 분사를 차단하세요.",
                  ("Override the automatic halon fire suppression protocol. Verify thermal delta with handheld infrared spectrometer. It's clean oxygen generation, not an active fire.", "자동 하론 소화 약제 분사를 수동 오버라이드하십시오. 휴대용 적외선 분광기로 열 변화를 검증하세요. 정상 산소 생성이며 화재가 아닙니다.", "‘override fire suppression’과 ‘infrared spectrometer’는 2차 재앙을 차단하는 냉철한 판단입니다."),
                  ("Spray water on the chemical candles immediately.", "화학 캔들에 물을 뿌려버립시다.", "폭발성 반응을 부르는 치명적인 실수입니다."),
                  ("Check your handphone for oxygen levels.", "산소 수치를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Atmosphere stabilized! Normal 21% oxygen restored across all modules! The international crew cheered in relief! Houston flight directors applauded your cool head.",
                  "대기 상태 완벽 안정화! 전 모듈 정상 21% 산소 복원 완료! 다국적 승무원들이 환호했어! 휴스턴 비행 지휘관들이 자네의 침착함에 박수를 보냈네.",
                  "우주에서는 오직 지식과 흔들리지 않는 규율만이 숨 쉴 수 있는 공기를 만들어낸다고 답하세요.",
                  ("Breath is life, Miller. In orbit, physics forgives nothing, but disciplined minds conquer everything. We breathe easy tonight.", "호흡은 곧 생명입니다, 밀러. 궤도에서 물리학은 어떤 실수도 용서하지 않지만, 규율 잡힌 정신은 모든 것을 극복합니다. 오늘 밤 편히 숨 쉽니다.", "우주 생존 드라마의 정점을 찍는 명대사입니다."),
                  ("I am glad we don't have to choke anymore.", "더 이상 숨 안 막혀서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the orbital freeze-dried ice cream.", "궤도 동결건조 아이스크림은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("대기권 재진입 열차폐막 손상 마하 25 기적의 귀환", "대기권 재진입 5분 전 방열 타일 손상이 감지된 캡슐을 완벽한 진입 각도로 유도해 플라스마 지옥을 뚫어야 한다.",
             "steer through the atmospheric entry corridor with damaged heat tiles",
             "손상된 열차폐막을 보호하며 대기권 진입 각도를 미세 제어해 생환할 때 쓰는 표현입니다.",
             [
                 ("Tile loss on the starboard chine! If plasma penetrates during peak heating, the capsule disintegrates! Entry interface in four minutes! What's the entry profile?",
                  "우현 샤인 부위 방열 타일 탈락! 최고 가열 시 플라스마가 침투하면 캡슐이 공중 분해돼! 진입 인터페이스 4분 전이야! 진입 프로파일이 뭐야?",
                  "받음각을 40도로 정밀 고정하고 플라스마 열 부하가 손상되지 않은 좌현에 집중되도록 롤 기동 각도를 비대칭 보정하라고 지시하세요.",
                  ("Bank forty degrees to port! Shift the thermal stagnation point away from the damaged starboard tiles! Ride the plasma shockwave on the intact composite belly!", "좌측으로 40도 롤 기동하십시오! 열 정체점을 손상된 우현 타일에서 반대쪽으로 이동시키세요! 온전한 복합재 동체 하부로 플라스마 충격파를 타고 넘습니다!", "‘shift the stagnation point’와 ‘ride the plasma shockwave’는 우주왕복선 참사를 막는 궁극의 재진입 비행술입니다."),
                  ("Turn the capsule upside down and close eyes.", "캡슐을 거꾸로 뒤집고 눈을 감읍시다.", "공중 분해로 전원 사망하는 최악의 행동입니다."),
                  ("The thermal tile spec is bad so call NASA.", "방열 타일 스펙이 안 좋으니 NASA에 따집시다.", "‘spec’은 콩글리시입니다.")),
                 ("Communications blackout! Radio ionization barrier! G-meter passing six Gs! Cockpit temperature is one hundred twenty degrees! Hull sensors are glowing red!",
                  "통신 두절! 플라스마 이온화 전파 차단! G미터 6G 돌파! 조종석 온도가 섭씨 50도를 넘었어! 선체 센서가 새빨갛게 타오르고 있어!",
                  "통신이 두절되어도 미리 계산된 비상 롤 리버설 프로파일을 수동으로 유지하며 음속 돌파를 기다리라고 외치세요.",
                  ("Hold the roll reversal vector! Do not touch the thrusters! Let the atmospheric friction bleed our Mach number down! We break through in sixty seconds!", "롤 반전 벡터를 그대로 유지하십시오! 추진기를 건드리지 마세요! 대기 마찰이 마하 속도를 깎아내리도록 두세요! 60초 뒤 대기권을 뚫고 나갑니다!", "‘hold the roll reversal’과 ‘bleed Mach number down’은 암흑의 재진입 공포를 이겨내는 침착한 비행 지휘입니다."),
                  ("Open the door to let cool air in.", "시원한 공기를 넣게 문을 열어봅시다.", "플라스마가 쏟아져 들어와 즉사하는 황당한 발상입니다."),
                  ("Check your handphone for weather on Earth.", "지구 날씨를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Blackout broken! 'Houston, we have visual on three main parachutes!' Splashdown in the Pacific Ocean! All crew safe! You brought them through the fire, Miller.",
                  "통신 재개! '휴스턴, 메인 낙하산 3개 육안 확인!' 태평양 해상 착수 완료! 전 승무원 무사 생환! 자네가 그들을 불지옥에서 데리고 나왔네, 밀러.",
                  "하늘의 별을 향한 여정은 지구의 대지 위로 안전하게 발을 디딜 때 비로소 완성된다고 화답하세요.",
                  ("The journey to the stars is never easy, but bringing our pioneers home through the fire is why we dare to explore. Welcome back to Earth.", "별을 향한 여정은 결코 쉽지 않지만, 불길을 뚫고 우리 개척자들을 집으로 데려오는 것이야말로 우리가 탐험하는 이유입니다. 지구에 오신 것을 환영합니다.", "우주 탐사 역사에 기록될 감동적인 피날레입니다."),
                  ("I am glad we don't have to swim in the ocean.", "바다에서 수영 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the carrier recovery beer.", "구조 항모 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    # 23. True Crime Detective Noir
    add_g(
        "True Crime Detective Noir", "Detective Rust Cohle (Homicide Lead Investigator)", "🔍",
        [
            ("20년 전 미제 살인 사건 DNA 프로파일링 급반전",
             "루이지애나 주경찰 미제사건 전담반. 1995년 사탕수수밭에서 발생한 연쇄 살인 사건의 증거물에서 추출한 미량 DNA가 현직 유력 상원의원의 가문 족보와 일치했다. 권력의 압박 속에서 진실을 밝혀내야 한다.",
             "follow the genealogical DNA trail directly to the high-society suspect",
             "가계 족보 DNA 분석을 통해 성역으로 여겨지던 상류층 용의자를 특정할 때 쓰는 표현입니다.",
             [
                 ("The genealogical DNA hits a match in the Tuttle family registry! The governor just called the precinct captain demanding we incinerate the cold case box!",
                  "족보 DNA가 터틀 가문 족보와 일치했어! 주지사가 서장에게 직접 전화해 미제사건 증거 상자를 소각하라고 압박하고 있어!",
                  "외압에 굴하지 말고 연방 법무부 독립 데이터베이스에 디지털 해시를 즉시 공증 백업하라고 하세요.",
                  ("Do not burn a single scrap. Clone the DNA STR profile and upload the cryptographic hash to the federal civil rights repository. They can't un-ring this bell.", "단 한 조각의 종이도 태우지 마십시오. DNA 프로필을 복제하고 연방 민권국 저장소에 암호화 해시를 즉시 업로드하십시오. 저들은 엎질러진 물을 주워 담을 수 없습니다.", "‘cryptographic hash’와 ‘can't un-ring this bell’은 권력의 증거 인멸을 차단하는 냉혹한 수사관의 결단입니다."),
                  ("Let's apologize to the governor and say we made a mistake.", "주지사님께 우리가 실수했다고 사과합시다.", "경찰의 명예를 팔아먹고 살인마를 방조하는 행위입니다."),
                  ("The evidence box has bad spec so throw it away.", "증거 상자 스펙이 안 좋으니 버립시다.", "‘spec’은 콩글리시입니다.")),
                 ("The backup is secure! But the lead suspect has an alibi sworn by three judges from twenty years ago. The DA says no jury will convict.",
                  "백업은 안전해! 하지만 유력 용의자는 20년 전 판사 3명이 서명한 완벽한 알리바이를 갖고 있어. 검사장은 배심원이 유죄 평결을 안 내릴 거래.",
                  "판사들의 알리바이 서명 날짜에 찍힌 팩스 타임스탬프와 주립 은행 인출 기록의 시차 모순을 밝혀내 알리바이를 분쇄하세요.",
                  ("Subpoena the hotel phone records and the offshore wire transfers. The judges were in Bermuda; the suspect was in the swamp. We break their perjury wide open.", "호텔 통화 기록과 해외 송금 내역을 소환 압수하십시오. 판사들은 버뮤다에 있었고 용의자는 늪지대에 있었습니다. 그들의 위증을 완전히 박살 내겠습니다.", "‘break perjury wide open’은 거짓 알리바이를 무너뜨리는 형사의 날카로운 추리입니다."),
                  ("Tell the judges that lying is very bad manner.", "판사들에게 거짓말은 매너가 나쁜 짓이라고 타이릅시다.", "‘manner’는 콩글리시입니다."),
                  ("Check your handphone for news articles.", "뉴스 기사를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Suspect confessed in the interrogation room! All twenty-four cold case homicides solved! The senator was arrested on live television! Rust, you conquered the dark.",
                  "취조실에서 용의자 자백 완료! 미제 살인 사건 24건 전원 해결! 상원의원이 생방송 뉴스 도중 전격 체포되었어! 러스트, 자네가 어둠을 정복했네.",
                  "세상은 어둠으로 가득 차 보이지만 한 걸음씩 빛이 승리해나가는 것이라고 답하세요.",
                  ("Once there was only dark, Rust. If you ask me, the light's winning. Case closed.", "옛날엔 오직 어둠뿐이었습니다, 러스트. 내게 묻는다면, 빛이 이겨가고 있는 중입니다. 사건 종결.", "트루 디텍티브(True Detective) 시즌 1의 불멸의 명대사를 그대로 재현한 피날레입니다."),
                  ("I am glad we don't have to smell swamps anymore.", "이제 늪지대 냄새 안 맡아도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the diner whiskey.", "식당 위스키는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("비 내리는 뒷골목 마피아 청부 살인 현장 감식", "폭우가 쏟아지는 뉴올리언스 뒷골목. 마피아 보스의 최측근이 살해된 현장에서 감식반과 함께 지워져 가는 탄도 궤적을 복원해야 한다.",
             "reconstruct the bullet trajectory under pouring rain", "폭우 속에서도 레이저 탄도학으로 저격수의 은신 위치를 정밀 역추적할 때 쓰는 표현입니다.",
             [
                 ("Torrential rain is washing away blood evidence and powder residue! The mob family is surrounding the yellow tape with shotguns! Do we clear out?",
                  "폭우가 혈흔 증거와 화약 잔여물을 씻어내고 있어! 마피아 조직원들이 엽총을 들고 폴리스 라인을 에워싸고 있네! 철수할까?",
                  "물러서지 말고 방수 텐트를 치고 탄도학 레이저로 탄착군 각도를 측정해 저격수의 3층 창문을 즉시 특정하라고 명령하세요.",
                  ("Erect the forensic canopy immediately. Cast ballistic trajectory rods through the brick impact points. The shooter was forty yards out, elevated third floor.", "즉시 감식 텐트를 치십시오. 벽돌 탄착점에 탄도 막대를 꽂으세요. 저격수는 40야드 거리, 3층 높이에서 사격했습니다.", "‘ballistic trajectory rods’와 ‘forensic canopy’는 폭우 속에서도 현장을 보존하는 노련한 수사관의 지휘입니다."),
                  ("Run away quickly before the mob shoots us.", "마피아가 쏘기 전에 빨리 도망칩시다.", "경찰의 위엄을 버리고 도망치는 비겁한 행동입니다."),
                  ("The rain spec is bad so call the weather station.", "비 스펙이 안 좋으니 기상청에 따집시다.", "‘spec’은 콩글리시입니다.")),
                 ("Third floor window raided! We found the spent casing. But it's an untraceable polymer shell without rifling grooves. The mob captain is smirking.",
                  "3층 창문 급습 완료! 탄피를 찾았어. 하지만 강선 흔적이 없는 추적 불가의 폴리머 탄피야. 마피아 두목이 비웃고 있네.",
                  "탄피 림에 남은 뇌관 타격 핀의 미세 현미경 마모흔을 추출해 특정 총기 개조 장인의 시그니처를 밝혀내세요.",
                  ("Microscopic firing pin impressions are unique as fingerprints. Scan the striation marks against our underground gunsmith registry. We have his signature.", "공이 자국 현미경 흔적은 지문만큼 고유합니다. 암시장 총기 개조 장인 데이터베이스와 대조 스캔하십시오. 놈의 고유 시그니처를 잡았습니다.", "‘firing pin impressions’와 ‘striation marks’는 과학 수사로 암흑가를 굴복시키는 결정적 단서입니다."),
                  ("Tell the mob boss to confess or we get angry.", "마피아 보스에게 자백 안 하면 화낼 거라고 으름장을 놓읍시다.", "조롱만 당하는 유치한 태도입니다."),
                  ("Check your handphone for gun prices.", "총기 가격을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Gunsmith broke and gave up the contract hit order! Hitman arrested at the airport! The mob family surrendered their territory! Justice in the rain.",
                  "총기상이 입을 열고 청부 살인 의뢰서를 불었어! 저격범이 공항에서 체포되었네! 마피아 조직이 구역을 포기하고 퇴각했어! 빗속의 정의구현이었네.",
                  "비가 아무리 쏟아져도 피 흘린 자들의 침묵의 외침은 지워지지 않는다고 답하세요.",
                  ("Rain washes the streets, Rust, but it never washes away the ledger of blood. The truth always remains. Another one for the books.", "비가 거리를 씻어낼 순 있어도, 피의 기록까지 씻어낼 수는 없습니다. 진실은 언제나 남습니다. 또 하나의 사건을 매듭지었습니다.", "하드보일드 누아르의 진수를 보여주는 명대사입니다."),
                  ("I am glad we can change into dry socks now.", "이제 마른 양말로 갈아신을 수 있어서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the gumbo stew.", "검보 스튜는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("부패한 서장과의 대면: 비밀 녹취록 폭로", "경찰서장 집무실. 마약 카르텔로부터 매달 뇌물을 받으며 수사를 방해해온 부패한 경찰서장에게 비밀 녹취록을 들이밀고 배지를 반납하게 해야 한다.",
             "confront the corrupt precinct captain with undeniable wiretap tapes",
             "부패한 경찰 고위층을 반박 불가능한 도청 녹취록으로 압박해 사임시킬 때 쓰는 표현입니다.",
             [
                 ("Captain locked the office door! He put his service weapon on the mahogany desk. He warns that if you step out of line, you'll be found dead in a ditch.",
                  "서장이 집무실 문을 잠갔어! 마호가니 책상 위에 권총을 올려놓았네. 선을 넘으면 도랑에서 변사체로 발견될 거라고 경고하고 있어.",
                  "녹음기를 테이블 위에 올려놓고 연방 검찰청 특수수사부가 건물 밖에서 실시간 감청 중임을 통보하세요.",
                  ("I don't cross lines, Captain—I draw them. Federal prosecutors are listening through my wire in the van outside. Take your hand off that Glock.", "난 선을 넘지 않습니다, 서장님. 선을 그을 뿐이지. 연방 검사들이 건물 밖 밴에서 도청 장치로 실시간 청취 중입니다. 권총에서 손 떼시죠.", "‘I don't cross lines, I draw them’은 부패한 상관을 단칼에 압도하는 불후의 명대사입니다."),
                  ("Cry loudly and ask the captain not to shoot.", "크게 울면서 서장님께 쏘지 말아 달라고 빕시다.", "경찰의 자존심을 팽개치는 굴욕적인 처사입니다."),
                  ("The captain has bad manner so let's scold him.", "서장님이 매너가 나쁘니 혼냅시다.", "‘manner’는 콩글리시입니다.")),
                 ("Captain blanched! He backed away from the desk. But he offers five hundred thousand in cash from his safe to burn the tapes and walk away.",
                  "서장의 얼굴이 하얗게 질렸어! 책상에서 물러섰네. 하지만 금고에서 현금 50만 달러를 꺼내며 녹취록을 불태우고 모른 척 넘어가재.",
                  "돈으로 살 수 없는 것이 형사의 영혼이며 즉시 배지와 권총을 테이블 위에 반납하라고 최후통첩을 보내세요.",
                  ("My badge isn't for sale, Captain. Put your gold shield and your service weapon on this desk, and put your hands behind your back.", "내 배지는 팔지 않습니다, 서장님. 금색 배지와 총을 책상 위에 내려놓고, 손을 등 뒤로 돌리십시오.", "‘my badge isn't for sale’은 부패 척결의 숭고한 결의를 보여주는 대사입니다."),
                  ("Take the five hundred thousand and buy a nice car.", "50만 달러를 받아서 멋진 차나 삽시다.", "동료 경찰을 배신하는 범죄 행위입니다."),
                  ("Check your handphone for banking apps.", "은행 앱을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Internal affairs entered and cuffed the Captain! The corrupt precinct syndicate is smashed! The entire department stood up and saluted you!",
                  "내사과 요원들이 진입해 서장에게 수갑을 채웠어! 부패한 경찰서 조직이 일망타진되었네! 부서 전원이 자네에게 기립 경례를 보냈어!",
                  "배지의 무게는 타협하지 않는 양심에서 나온다고 답하세요.",
                  ("A badge is just tin, Rust, unless it's backed by a heart that refuses to bend. Today, the law lives again.", "배지는 타협을 거부하는 심장이 뒷받침되지 않는다면 그저 양철 조각에 불과합니다. 오늘, 법이 다시 살아 숨 쉽니다.", "정의로운 경찰의 표상을 보여주는 감동적인 피날레입니다."),
                  ("I am glad we don't have to salute the captain.", "이제 서장한테 경례 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the precinct coffee.", "경찰서 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("최후의 탄도학 증거: 범인의 총기 시그니처 입증", "지방법원 배심원 재판. 피고인 측 변호인이 총기 감식 오류를 주장하며 무죄 평결을 노리는 가운데, 특수 탄도학 증언으로 범행을 쐐기 박아야 한다.",
             "demonstrate unassailable ballistic striation matching on the stand",
             "법정 증인석에서 탄도학 홈 일치를 완벽히 시연해 배심원 유죄 평결을 이끌어낼 때 쓰는 표현입니다.",
             [
                 ("Defense attorney is confusing the jury with pseudo-scientific doubt! He claims barrel wear makes striation matching impossible! You have five minutes on the stand.",
                  "변호인이 유사 과학적 의혹으로 배심원들을 혼란에 빠뜨리고 있어! 총열 마모 때문에 탄도 홈 일치가 불가능하다고 주장해! 증인석에서 5분 남았어.",
                  "현미경 비교 모니터를 배심원단 앞에 직접 띄우고 12개 고유 강선 홈과 뇌관 자국의 일치율을 육안으로 확인시키세요.",
                  ("Project the split-screen comparison microscope directly to the jury box. Point out the twelve distinct micro-striae land marks. The science does not lie.", "분할 화면 비교 현미경 영상을 배심원석에 직접 투사하십시오. 12개의 뚜렷한 미세 강선 랜드마크를 짚어주세요. 과학은 거짓말을 하지 않습니다.", "‘split-screen comparison microscope’와 ‘science does not lie’는 배심원의 의구심을 단칼에 날리는 압도적 법정 증언입니다."),
                  ("Tell the jury that the defendant looks like a bad guy.", "배심원들에게 피고인이 나쁜 놈처럼 생겼다고 말합시다.", "증거에 기반하지 않은 인신공격으로 즉각 제지당합니다."),
                  ("The microscope has bad spec so buy a new lens.", "현미경 스펙이 안 좋으니 새 렌즈를 사 옵시다.", "‘spec’은 콩글리시입니다.")),
                 ("The jury is leaning forward. The defense attorney is trying to provoke an emotional argument over chain of custody.",
                  "배심원들이 몸을 앞으로 기울이고 있어. 변호인이 증거물 보관 연속성(Chain of Custody)을 트집 잡으며 감정적 논쟁을 유도하고 있어.",
                  "냉정하고 객관적인 어조로 법의학 봉인 번호와 서명 기록 원장을 낭독해 절차적 완벽성을 증명하세요.",
                  ("Every transfer, from crime scene to ballistic tank, carries an immutable tamper-evident seal and double-verified signatures. The chain is unbroken.", "범죄 현장부터 탄도 수조까지 모든 이전 과정은 훼손 방지 봉인과 이중 검증 서명으로 기록되었습니다. 증거의 연속성은 완벽합니다.", "‘immutable tamper-evident seal’과 ‘chain unbroken’은 법정 기술자들의 공격을 무력화하는 정석 증언입니다."),
                  ("Tell the lawyer to stop being rude to a police officer.", "변호사에게 경찰관한테 무례하게 굴지 말라고 화를 냅시다.", "감정을 주체하지 못해 신빙성을 잃는 하책입니다."),
                  ("Check your handphone for jury verdict notifications.", "배심원 평결 알림을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Guilty on all counts! First-degree murder conviction! The victim's family wept with relief! The courtroom erupted in applause for your unimpeachable testimony.",
                  "모든 혐의 유죄 평결! 1급 살인 유죄 확정! 피해자 유족들이 안도의 눈물을 흘렸어! 자네의 흠잡을 데 없는 증언에 법정이 박수로 가득 찼네.",
                  "어둠에 묻힌 희생자들의 목소리를 법정에서 대변하는 것이 형사의 마지막 사명이라고 답하세요.",
                  ("We give voice to the silenced, Rust. When the evidence speaks with truth and honor, justice is finally served. Case closed.", "우리는 침묵당한 자들의 목소리를 대변할 뿐입니다, 러스트. 증거가 진실과 명예로 말할 때, 정의는 마침내 실현됩니다. 사건 종결.", "법정 형사물의 깊은 감동을 완성하는 피날레입니다."),
                  ("I am glad we don't have to wear this tie anymore.", "이제 이 넥타이 안 매도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the court dinner.", "법원 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    return data
