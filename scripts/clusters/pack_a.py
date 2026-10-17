# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack A: Genres 20 to 34 (15 genres x 4 = 60 episodes)
20: Cyber Crime & Zero-Day Hacking
21: Aerospace Defense & Top Gun
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
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_pack_a():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    # Helper generator to construct 4 episodes per genre with rich Hollywood dialogue
    def build_genre(name, speaker, emoji, arc_data):
        eps = []
        for arc in arc_data:
            eps.append(mk(arc[0], speaker, emoji, arc[1], arc[2], arc[3], arc[4]))
        data[name] = eps

    # 20. Cyber Crime & Zero-Day Hacking
    build_genre(
        "Cyber Crime & Zero-Day Hacking", "Elliot Alderson (Elite Cyber Forensic Specialist)", "💻",
        [
            ("대형 대학병원 중환자실 랜섬웨어 20분 카운트다운",
             "시카고 메모리얼 병원 중환자실. 생명유지장치와 인공호흡기를 인질로 잡은 다크웹 랜섬웨어 공격이 발생했다. 몸값 비트코인을 요구하는 20분의 타이머가 흐르는 가운데, 리버스 엔지니어링으로 암호화 키를 해독해야 한다.",
             "deploy the cryptographic reverse bypass", "랜섬웨어 암호화를 무력화하는 역공학 우회 코드를 주입할 때 쓰는 전문 해킹 표현입니다.",
             [
                 ("ICU monitors are encrypting one by one! Three hundred patients on ventilators! The hackers demand fifty Bitcoin in twelve minutes! Do we pay?",
                  "중환자실 모니터가 하나씩 암호화되고 있어! 인공호흡기를 단 환자가 300명이야! 해커들이 12분 안에 비트코인 50개를 내놓으래! 송금할까?",
                  "송금은 추가 공격을 부를 뿐이므로 루트 메모리 덤프에서 취약점 난수를 추출해 복호화 키를 강제 추출하라고 하세요.",
                  ("Do not wire a single satoshi. Dump the volatile RAM cache right now. I will isolate the pseudo-random seed and reconstruct the private AES key.", "단 1사토시도 보내지 마십시오. 휘발성 RAM 캐시를 지금 즉시 덤프하세요. 의사 난수 시드를 분리해 개인 AES 복호화 키를 역추출하겠습니다.", "‘volatile RAM cache’와 ‘reconstruct the private AES key’는 사이버 수사의 최고난도 킬러 테크닉입니다."),
                  ("Let's unplug the power cord from all medical machines.", "모든 의료 장비에서 전원 코드를 뽑아버립시다.", "환자들을 즉각 사망에 이르게 하는 치명적인 실수입니다."),
                  ("The server has bad spec so call the AS center.", "서버 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                 ("RAM dumped! Key extracted! But the malware injected a dead-man's wipe trigger into the root kernel. If we decrypt, it bricks the hospital network.",
                  "RAM 덤프 완료! 키 추출 성공! 그런데 악성코드가 루트 커널에 파괴 트리거를 심어뒀어. 복호화하는 순간 병원 네트워크 전체가 벽돌이 돼.",
                  "가상 샌드박스 가상화 격리망을 가동해 트리거를 속이고 메인 생명유지 그리드만 안전하게 복원하자고 지시하세요.",
                  ("Spoof the kernel watchdog using a virtualized sandbox buffer. We divert the destructive payload into a null sink while streaming the decryption payload.", "가상화 샌드박스 버퍼로 커널 감시 프로세스를 속이십시오. 파괴 페이로드를 가상 싱크홀로 격리하는 동안 복호화 코드를 주입합니다.", "‘spoof the kernel watchdog’과 ‘virtualized sandbox buffer’는 악성코드를 완전히 무력화하는 해커의 마스터클래스입니다."),
                  ("Tell the doctors to blow air into patients with their mouths.", "의사들에게 입으로 환자들에게 숨을 불어넣으라고 합시다.", "비현실적이고 패닉만 유발하는 말입니다."),
                  ("Check your handphone for virus scanner apps.", "바이러스 백신 앱을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Decryption complete! All three hundred ventilators back online! Zero casualties! The FBI cyber division just identified the hacker's server in Bucharest! You saved those lives.",
                  "복호화 완료! 인공호흡기 300대 전원 정상 가동! 사상자 제로! FBI 사이버 수사대가 부쿠레슈티의 해커 서버를 특정했어! 자네가 그 목숨들을 살렸네.",
                  "코드는 파괴의 도구가 아니라 생명을 지키는 방패여야 한다고 답하세요.",
                  ("Technology can wound, Elliot, but code written in defense of human life will always overcome darkness. System secure.", "기술이 상처를 입힐 수 있을지라도, 인간의 생명을 지키기 위해 작성된 코드는 언제나 어둠을 압도합니다. 시스템 방어 완료되었습니다.", "미스터 로봇을 연상시키는 숭고한 해커의 철학입니다."),
                  ("I am glad we don't have to look at green screens now.", "이제 초록색 화면 안 봐도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the hacker pizza.", "해커 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("월스트리트 초고속 전용망 제로데이 공격 차단", "다크 파이버 초저지연 전용망에 침투한 제로데이 익스플로잇을 차단하고 10억 달러 증발을 막아야 한다.",
             "deploy zero-day behavioral heuristics before market execution", "거래 실행 전 행위 기반 휴리스틱 탐지로 제로데이 침투를 원천 차단할 때 쓰는 표현입니다.",
             [
                 ("A polymorphic zero-day bypassed our firewall! It's spoofing phantom limit orders on the exchange! Do we halt all trading desks?",
                  "변종 제로데이가 방화벽을 뚫었어! 거래소에 유령 지정가 주문을 쏟아내고 있어! 전 트레이딩 데스크 거래를 중단할까?",
                  "거래를 중단하면 시장 패닉이 오므로 행위 기반 휴리스틱 방어벽으로 가짜 패킷만 실시간 드롭하라고 지시하세요.",
                  ("Do not halt trading. Deploy behavioral heuristics on the edge router and drop spoofed packets matching the anomalous TTL signature immediately.", "거래를 중단하지 마십시오. 에지 라우터에 행위 기반 휴리스틱을 배포하고 비정상 TTL 시그니처와 일치하는 위조 패킷만 즉시 드롭하십시오.", "‘behavioral heuristics’와 ‘anomalous TTL signature’는 금융망 해킹을 방어하는 최첨단 보안 기술입니다."),
                  ("Let's ask the exchange to cancel all stock trades.", "거래소에 모든 주식 거래를 취소해달라고 부탁합시다.", "전 세계 금융 시장에 대혼란을 부르는 무책임한 소리입니다."),
                  ("The router spec is bad so call the company.", "라우터 스펙이 안 좋으니 회사에 전화합시다.", "‘spec’은 콩글리시입니다.")),
                 ("Packets dropped! But the botnet is flooding our DNS servers with fifty gigabits of volumetric traffic! The order book is freezing.",
                  "패킷 차단 완료! 하지만 봇넷이 우리 DNS 서버에 초당 50기가비트의 디도스 트래픽을 퍼붓고 있어! 호가창이 얼어붙고 있네.",
                  "애니캐스트(Anycast) 라우팅을 활성화해 전 세계 스크러빙 센터로 악성 트래픽을 분산 흡수시키라고 명령하세요.",
                  ("Enable Anycast BGP routing across our Tier-1 transit providers. Route the volumetric flood through scrubbing centers and keep trading pipes clean.", "1계위 회선 제공업체 전반에 애니캐스트 BGP 라우팅을 활성화하십시오. 트래픽 폭탄을 정화 센터로 분산 흡수시켜 거래 통로를 깨끗하게 유지하세요.", "‘Anycast BGP routing’과 ‘scrubbing centers’는 대규모 디도스를 무력화하는 정석 방어 기법입니다."),
                  ("Tell the traders to pray that the computer gets better.", "트레이더들에게 컴퓨터가 나아지길 기도하라고 하세요.", "패닉을 키우는 한심한 조언입니다."),
                  ("Check your handphone for stock prices.", "주가를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Trading closed! Zero fraudulent fills! Our firm made eighty million in arbitrage profit while defending the network! Flawless cyber defense, Elliot.",
                  "장 마감! 부정 거래 체결 0건! 네트워크를 방어하면서 차익거래로 8천만 달러 수익을 올렸어! 완벽한 사이버 방어였네, 엘리엇.",
                  "네트워크의 무결성을 지키는 자가 디지털 세상의 진정한 승자라고 답하세요.",
                  ("In the war of nanoseconds, the defender who masters the packet masters the world. Ledger verified, network clean.", "나노초의 전쟁에서 패킷을 지배하는 방어자가 세상을 지배합니다. 원장 검증 완료, 네트워크 정상입니다.", "금융 사이버 보안의 정점을 보여주는 멋진 피날레입니다."),
                  ("I am glad we don't have to look at charts anymore.", "이제 차트 안 봐도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the Wall Street beer.", "월가 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("국가 전력망 SCADA 에어갭 방어선 침투 저지", "국가 주요 전력망 변전소를 블랙아웃시키려는 적국 해커 조직의 SCADA 망 침투를 저지해야 한다.",
             "sever the compromised SCADA bridge and isolate the substation grid", "오염된 SCADA 브리지를 차단하고 변전소 전력망을 물리적으로 격리할 때 쓰는 표현입니다.",
             [
                 ("Red alert! The malware crossed the physical air-gap through a corrupted maintenance tablet! Grid frequency dropping through fifty-nine Hertz! Blackout in five minutes!",
                  "적색경보! 정비용 태블릿을 통해 악성코드가 물리적 에어갭을 뚫었어! 전력 주파수가 59헤르츠로 급락 중이야! 5분 뒤 도시 전체 대정전이야!",
                  "원격 제어 릴레이를 물리적으로 절단하고 수동 아날로그 개폐 모드로 전력망을 강제 전환하라고 명령하세요.",
                  ("Drop the physical opto-isolator relays right now! Sever the digital SCADA bus and lock every transformer into manual analog governor control!", "지금 즉시 광절연 릴레이를 물리적으로 차단하십시오! 디지털 SCADA 버스를 끊고 모든 변압기를 수동 아날로그 제어로 강제 고정하세요!", "‘opto-isolator relays’와 ‘analog governor control’은 사이버 대정전을 막는 최후의 물리적 방어선입니다."),
                  ("Let's wait until the computer restarts automatically.", "컴퓨터가 자동으로 재부팅될 때까지 기다려봅시다.", "수천만 가구가 암흑에 빠지는 재앙을 부릅니다."),
                  ("The power grid spec is bad so call the city.", "전력망 스펙이 안 좋으니 시청에 전화합시다.", "‘spec’은 콩글리시입니다.")),
                 ("Grid stabilized at sixty Hertz! But the hostile payload planted an encrypted logic bomb in the backup nuclear cooling pump controllers.",
                  "주파수 60헤르츠로 안정화! 하지만 적의 악성코드가 백업 원자로 냉각 펌프 제어기에 암호화된 논리 폭탄을 심어뒀어.",
                  "불변 펌웨어 마스터 ROM 스냅샷을 플래시 메모리에 강제 덮어쓰기하여 악성 매크로를 원천 소각하라고 지시하세요.",
                  ("Flash the factory-sealed gold master ROM image across the controller bus. Overwrite the corrupted EEPROM and verify the cryptographic signature.", "공장 출하 골드 마스터 ROM 이미지를 제어기 버스에 즉각 강제 플래시하십시오. 오염된 EEPROM을 덮어쓰고 암호화 무결성 서명을 검증하세요.", "‘gold master ROM image’와 ‘cryptographic signature’는 침투된 하드웨어를 완벽 정화하는 최고위 엔지니어링 기술입니다."),
                  ("Hit the controller box with a hammer.", "제어기 박스를 망치로 내려칩시다.", "원전 설비를 파괴하는 미친 짓입니다."),
                  ("Check your handphone for radiation warnings.", "방사능 경보를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Nuclear pumps secured! Power grid holding strong! Forty million citizens never even knew the lights almost went out! You saved the nation, Elliot.",
                  "원자로 펌프 정상화! 전력망 완벽 유지! 4천만 시민들은 불이 꺼질 뻔했다는 사실조차 몰랐어! 자네가 국가를 구했네, 엘리엇.",
                  "보이지 않는 곳에서 세상을 지키는 것이 진정한 엔지니어의 사명이라고 답하세요.",
                  ("The best guardians are the ghosts who keep the machine running while the city sleeps in peace. Grid locked, job done.", "가장 위대한 수호자는 도시가 평화롭게 잠든 동안 기계를 묵묵히 지키는 유령들입니다. 전력망 방어 완료, 임무 끝났습니다.", "사이버 전사의 숭고한 사명감을 보여주는 피날레입니다."),
                  ("I am glad we don't have to work night shift tonight.", "오늘 밤 야근 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the diner coffee.", "식당 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("다크웹 국제 카르텔 비트코인 지갑 실시간 압수", "국제 무기 밀매 카르텔이 자금 세탁을 위해 이동시키는 10억 달러 상당의 비트코인 지갑을 실시간 탈취 압수해야 한다.",
             "execute a cryptographic wallet seizure through mempool front-running",
             "멤풀 프론트러닝 기술을 이용해 블록체인에서 범죄 자금을 가로채 압수할 때 쓰는 표현입니다.",
             [
                 ("The cartel just broadcast a transaction moving ten thousand Bitcoin through a privacy mixer! We have three minutes before the block confirms! How do we seize it?",
                  "카르텔이 프라이버시 믹서를 통해 비트코인 1만 개를 전송하는 트랜잭션을 방출했어! 블록이 생성되기까지 3분 남았네! 어떻게 압수할 건가?",
                  "가스비를 10배로 높인 트랜잭션 대체(RBF) 기법으로 연방 법무부 금고 지갑으로 자금을 선점 이체하라고 지시하세요.",
                  ("Execute a Replace-by-Fee front-run immediately. Spike the miner tip by tenfold and redirect the UTXO inputs into the DOJ cold-storage multi-sig wallet.", "즉시 수수료 대체(RBF) 프론트러닝을 실행하십시오! 채굴자 수수료를 10배로 높여 미사용 트랜잭션(UTXO)을 법무부 다중서명 콜드월렛으로 가로채세요.", "‘Replace-by-Fee front-run’과 ‘DOJ multi-sig wallet’은 블록체인 자금 세탁을 실시간 차단하는 최첨단 수사 기술입니다."),
                  ("Ask the Bitcoin customer service center for a refund.", "비트코인 고객센터에 환불해달라고 문의합시다.", "탈중앙화 블록체인의 기본도 모르는 황당한 소리입니다."),
                  ("The internet spec is bad so call the telecom.", "인터넷 스펙이 안 좋으니 통신사에 전화합시다.", "‘spec’은 콩글리시입니다.")),
                 ("Front-run confirmed in block 850,000! Funds redirected! But the cartel's chief hacker is tracing our validator node IP to pinpoint our safehouse.",
                  "85만 번째 블록에서 선점 체결 완료! 자금 압수 성공! 그런데 카르텔 수석 해커가 우리 검증자 노드 IP를 역추적해 안전가옥 위치를 파악하려 해.",
                  "즉시 양파 라우팅 다중 프록시로 트래픽을 분산시키고 물리적 MAC 주소를 스푸핑해 신호를 사막으로 유인하세요.",
                  ("Scramble our outbound routing across thirty onion relays. Spoof the physical MAC addresses and bounce their trace pings into a dead honeypot in Nevada.", "발신 라우팅을 30개 토르 릴레이로 분산하십시오. 물리적 MAC 주소를 변조하고 그들의 추적 신호를 네바다 사막의 가짜 허니팟으로 튕겨내세요.", "‘onion relays’와 ‘dead honeypot’은 적의 역추적을 역이용해 궤멸시키는 보안 전술입니다."),
                  ("Turn off the computer screen so they cannot see us.", "우릴 못 보게 컴퓨터 모니터를 꺼버립시다.", "초등학생 수준의 우스꽝스러운 반응입니다."),
                  ("Check your handphone for crypto prices.", "코인 시세를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Cartel servers raided by Europol! One billion dollars in crypto secured in federal custody! The dark web syndicate is completely dismantled! Legendary hack, Elliot.",
                  "유로폴이 카르텔 서버를 전격 급습했어! 10억 달러 상당의 코인이 연방 금고에 압수되었네! 다크웹 신디케이트가 완전히 해체되었어! 전설적인 해킹이었네, 엘리엇.",
                  "블록체인은 익명의 방패가 될 수 없으며 정의는 코드 위에서도 살아 숨 쉰다고 답하세요.",
                  ("Anonymity on the ledger is an illusion, Elliot. When criminal code meets relentless justice, the truth always confirms on the chain. Case closed.", "분산 원장 위의 익명성은 환상일 뿐입니다. 범죄의 코드가 끈질긴 정의와 마주할 때, 진실은 언제나 체인 위에서 증명됩니다. 사건 종결되었습니다.", "블록체인 수사의 정점을 보여주는 멋진 피날레입니다."),
                  ("I am glad we don't have to trade crypto anymore.", "이제 코인 거래 안 해도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the victory taco.", "승리의 타코는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    # 21. Aerospace Defense & Top Gun
    build_genre(
        "Aerospace Defense & Top Gun", "Captain 'Maverick' Mitchell (Strike Fighter Commander)", "✈️",
        [
            ("마하 10 스크램제트 극초음속 시험 비행 한계 돌파",
             "에드워즈 공군기지 고고도 시험 비행장. 10만 피트 상공에서 마하 10을 돌파해야 하는 극초음속 실험기 다크스타. 엔진 과열 경보가 울리는 가운데 제독의 귀환 명령을 거부하고 한계를 돌파해야 한다.",
             "push the scramjet throttle past Mach ten into uncharted envelope",
             "극초음속 스크램제트 스로틀을 한계 이상으로 밀어붙여 미지의 비행 영역을 개척할 때 쓰는 표현입니다.",
             [
                 ("Surface skin temperature passing two thousand degrees! Mach 9.8 and climbing! Mission control is screaming to abort and pull back the throttle! Do we abort?",
                  "동체 표면 온도가 2천 도를 넘어서고 있어! 마하 9.8 돌파 중! 지상 관제소가 당장 비행을 중단하고 스로틀을 당기라고 소리치고 있어! 중단할까?",
                  "물러서지 말고 스크램제트 연료 분사 밸브를 100% 개방해 기어코 마하 10의 벽을 깨부수자고 외치세요.",
                  ("Negative, control! Darkstar is holding together! Just a little push... Scramjet at full afterburner! Breaking Mach ten right now!", "중단 거부한다, 관제소! 다크스타는 버텨주고 있어! 조금만 더... 스크램제트 풀 애프터버너! 지금 마하 10의 벽을 깬다!", "‘Darkstar is holding together’와 ‘breaking Mach ten’은 탑건 매버릭의 전율을 그대로 재현하는 명대사입니다."),
                  ("Let's pull the emergency parachute and float down.", "비상 낙하산을 펴고 천천히 내려갑시다.", "마하 10에서 낙하산을 펴면 동체 분해로 즉사합니다."),
                  ("The jet spec is bad so call the factory.", "제트기 스펙이 안 좋으니 공장에 따집시다.", "‘spec’은 콩글리시입니다.")),
                 ("Mach 10.2 achieved! Historic record! But the shockwave damaged our left stabilizer. Controls are shuddering violently as we begin descent.",
                  "마하 10.2 달성! 역사적 신기록! 하지만 충격파로 좌측 수평안정판이 손상되었어. 강하를 시작하는데 조종간이 격렬하게 떨리고 있어.",
                  "받음각을 12도로 일정하게 유지하며 공기저항을 이용해 완만하게 활공 강하하라고 지시하세요.",
                  ("Trim the nose up twelve degrees. Bleed off kinetic energy through high-altitude banking turns. Fly the lifting body—she still wants to fly!", "기수를 12도 올리고 트림을 맞추십시오. 고고도 선회 기동으로 운동 에너지를 감속시킵니다. 양력 동체를 믿으세요, 이 비행기는 아직 날고 싶어 합니다!", "‘bleed off kinetic energy’와 ‘fly the lifting body’는 극한의 시험 비행을 성공시키는 베테랑 파일럿의 비행술입니다."),
                  ("Let go of the stick and close your eyes.", "조종간을 놓고 눈을 감읍시다.", "비행기를 버리고 추락하는 자살행위입니다."),
                  ("Check your handphone for GPS location.", "GPS 위치를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Touchdown on the dry lake bed! Darkstar came home safely! The entire Pentagon joint chiefs stood up and saluted over satellite! You made history, Mav.",
                  "마른 호수 활주로에 터치다운 성공! 다크스타가 무사히 귀환했어! 펜타곤 합참의장단 전원이 위성 중계를 보며 기립 경례를 보냈네! 자네가 역사를 썼어, 매브.",
                  "한계는 비행기에 있는 것이 아니라 인간의 마음에 있는 것이라고 답하세요.",
                  ("The future is coming, Admiral, but today isn't that day. As long as there are pilots who refuse to accept limits, the sky belongs to us.", "미래는 오고 있습니다, 제독님. 하지만 오늘은 아닙니다. 한계를 거부하는 조종사들이 살아있는 한, 하늘은 우리의 것입니다.", "탑건의 심장을 관통하는 불후의 명대사입니다."),
                  ("I am glad we don't have to wear this helmet anymore.", "이제 이 헬멧 안 써도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the base beer tonight.", "기지 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("적국 영공 진입 미그기 락온 도그파이트 공중전", "적국 방공망을 뚫고 5세대 전투기와 초음속 근접 공중전(Dogfight)에서 살아남아야 한다.",
             "execute the Cobra maneuver and lock onto the hostile bogey", "코브라 기동으로 적기의 배후를 잡고 미사일 락온을 성공시킬 때 쓰는 공중전 표현입니다.",
             [
                 ("Bandits at six o'clock! Radar warning receiver screaming! Surface-to-air missiles launching from the valley floor! What's the evasion maneuver?",
                  "적기 6시 방향 추격 중! 레이더 경보 수신기 요란하게 폭음! 계곡 바닥에서 지대공 미사일 발사! 회피 기동이 뭐야?",
                  "채프와 플레어를 살포하며 협곡 바닥으로 초저고도 다이브하여 적 레이더를 기만하라고 명령하세요.",
                  ("Drop chaff and flares! Break hard right and dive into the canyon deck! Hug the rock walls and break their radar line of sight!", "채프와 플레어 살포! 우측 급선회하며 협곡 바닥으로 강하하십시오! 암벽에 바짝 붙어 적 레이더 가시선을 절단하세요!", "‘drop chaff and flares’와 ‘break radar line of sight’는 대공 미사일을 회피하는 교과서적인 전술 비행입니다."),
                  ("Fly straight up into the clouds and wait.", "구름 위로 곧장 날아가서 기다려봅시다.", "미사일에 격추당하는 치명적인 실수입니다."),
                  ("The jet has bad spec so tell the mechanic.", "전투기 스펙이 안 좋으니 정비사에게 따집시다.", "‘spec’은 콩글리시입니다.")),
                 ("Missiles defeated! But a fifth-generation stealth fighter pulled right behind your tail! Missile lock tone active! You have three seconds!",
                  "미사일 회피 성공! 하지만 5세대 스텔스기가 바로 꼬리에 붙었어! 미사일 락온 경보음 울림! 3초 남았어!",
                  "공기역학적 속도를 급감시키는 코브라 기동으로 적기를 앞으로 오버슈트시키고 기관포로 격추하세요.",
                  ("Hit the airbrakes, pull full aft stick—execute Cobra maneuver! Let him overshoot, then lock heat-seekers on his exhaust and fire!", "에어브레이크 전개, 조종간 최대로 당겨 코브라 기동 실행! 적기를 앞으로 지나쳐가게 만들고 배기구에 열추적 미사일을 락온해 발사하십시오!", "‘execute Cobra maneuver’와 ‘lock heat-seekers’는 적기를 역전 격추하는 공중전 최고의 시그니처 무브입니다."),
                  ("Eject immediately and float down nicely.", "즉시 사출 좌석을 당겨 곱게 낙하산 타고 내립시다.", "전투기를 버리는 패배주의적 행동입니다."),
                  ("Check your handphone for enemy call signs.", "적기 콜사인을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Splash one hostile bandit! Airspace cleared! Both strike packages returning to aircraft carrier with zero losses! Maverick, you are a legend.",
                  "적기 1대 격추 확인! 영공 확보 완료! 편대 전원 무사히 항공모함으로 복귀 중! 매버릭, 자네는 진정한 전설이야.",
                  "승패를 가르는 것은 기체가 아니라 조종석에 앉은 조종사의 배짱이라고 답하세요.",
                  ("It's not the plane, Admiral—it's the pilot. Clean deck, mission accomplished. Bringing the boys home.", "비행기가 중요한 게 아닙니다, 제독님. 조종사가 중요합니다. 항모 착함 준비 완료, 임무 완수했습니다. 아군들을 데리고 집으로 갑니다.", "탑건 매버릭의 상징과도 같은 명대사입니다."),
                  ("I am glad we don't have to fly over trees anymore.", "이제 나무 위로 안 날아다녀도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the carrier mess hall dinner.", "항모 식당 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("스텔스 레이더 회피 협곡 초저고도 침투 비행", "지하 우라늄 농축 시설 타격을 위해 레이더 사각지대 협곡을 시속 900km, 고도 100피트로 비행해야 한다.",
             "thread the canyon needle below radar detection thresholds", "레이더 감지 한계선 아래로 협곡의 바늘구멍을 뚫고 초저고도 침투할 때 쓰는 표현입니다.",
             [
                 ("The canyon walls are narrower than our wingspan! Flying at six hundred knots, one hundred feet off the riverbed! Flight computers are screaming G-force overload!",
                  "협곡 벽이 우리 날개폭보다 좁아! 시속 600노트로 강바닥에서 100피트 위를 날고 있어! 비행 컴퓨터가 중력가속도 과부하 경보를 울리고 있어!",
                  "컴퓨터 경보를 무시하고 손끝의 감각을 믿고 기체를 90도 기울여 바위 틈새를 통과하라고 명령하세요.",
                  ("Knife-edge between the rock pinnacles! Bank ninety degrees left, trust the stick, and thread the needle! Don't think, just do!", "바위 봉우리 사이로 기체를 칼날처럼 기울이십시오! 좌로 90도 뱅크 넣고, 조종간을 믿고 바늘구멍을 뚫으세요! 생각하지 말고, 그냥 해!", "‘knife-edge’와 ‘don't think, just do’는 탑건의 심장 박동을 극대화하는 명언입니다."),
                  ("Let's pull up high into the open sky.", "넓은 하늘 위로 높이 상승해버립시다.", "적 레이더에 잡혀 지대공 미사일에 즉각 산화합니다."),
                  ("The wing has bad spec so complain to Boeing.", "날개 스펙이 안 좋으니 보잉에 불평합시다.", "‘spec’은 콩글리시입니다.")),
                 ("Co-pilot is suffering G-LOC! Tunnel vision setting in as you pull seven Gs around the blind ridge! You have five seconds before the target vent!",
                  "동료 조종사가 중력 유발 의식 상실(G-LOC) 직전이야! 시야가 좁아지는 터널 비전이 오고 있어! 환기구 타깃까지 5초 남았네!",
                  "산소 레버를 긴급 공급 위치로 밀고 호흡을 통제하며 레이저 유도 폭탄을 환기구 정중앙에 투하하라고 외치세요.",
                  ("Pressure-breathe! Squeeze the abdominal muscles! Laser lock confirmed on the thermal exhaust port! Pickling bombs now!", "압력 호흡하십시오! 복근에 힘 꽉 줘요! 환기구 포트에 레이저 락온 확인! 지금 폭탄 투하!", "‘pressure-breathe’와 ‘pickling bombs’는 초인적인 한계를 견디며 타격을 완수하는 조종술입니다."),
                  ("Drop the bomb on the grass and fly away.", "풀밭에 대충 폭탄을 떨구고 도망칩시다.", "작전 실패로 국가 안보를 위태롭게 하는 행위입니다."),
                  ("Check your handphone for target coordinates.", "타깃 좌표를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Direct hit! The bunker collapsed in a massive subterranean explosion! Miraculous climb-out through the smoke! You accomplished the impossible, Mav.",
                  "직격 명중! 지하 벙커가 거대한 폭발과 함께 붕괴되었어! 연기를 뚫고 기적적인 급상승 탈출 성공! 자네가 불가능을 해냈어, 매브.",
                  "기적은 불가능에 도전할 용기를 가진 자들에게만 주어지는 선물이라고 답하세요.",
                  ("Miracles aren't born from safety, Admiral—they are forged when fearless aviators trust each other to the edge and back. Flying home.", "기적은 안전 속에서 태어나지 않습니다, 제독님. 두려움을 모르는 조종사들이 서로를 벼랑 끝까지 믿을 때 빚어지는 것입니다. 집으로 귀환합니다.", "탑건 최고의 낭만을 보여주는 감동의 피날레입니다."),
                  ("I am glad we don't have to carry bombs anymore.", "이제 폭탄 안 싣고 다녀도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the flight jacket patch.", "비행 재킷 패치는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("조종사 의식 상실 위기 극한의 9G 도그파이트 결전", "초고기동 9G 회전 공중전에서 의식을 잃어가는 윙맨을 지키며 적 편대장을 격추해야 한다.",
             "sustain nine Gs and achieve guns kill on the enemy lead", "9G의 가속도를 버텨내며 적 편대장을 기관포로 격추할 때 쓰는 극한의 공중전 표현입니다.",
             [
                 ("Your wingman blacked out under eight Gs! His jet is descending toward the ocean! The enemy flight lead is rolling in for an easy kill! What's the save?",
                  "자네 윙맨이 8G에서 실신했어! 그의 전투기가 바다로 추락하고 있어! 적 편대장이 손쉬운 격추를 위해 롤 기동으로 진입 중이야! 어떻게 구할 건가?",
                  "수직 가속으로 적기와 윙맨 사이에 아군 기체를 끼워 넣고 헤드온 정면 대결로 적기를 밀어내라고 명령하세요.",
                  ("Cut across the circle! Place my canopy directly between the enemy and my wingman! Force a head-on merge and drag him off my boy!", "선회 원을 가로질러라! 적기와 윙맨 사이에 내 캐노피를 정확히 들이밀어라! 정면 헤드온 대결을 강제해 놈을 내 윙맨에게서 떼어낸다!", "‘cut across the circle’과 ‘force a head-on merge’는 아군을 지키기 위해 목숨을 던지는 편대장의 숭고한 결단입니다."),
                  ("Let the wingman crash so we can save ourselves.", "우리라도 살 수 있게 윙맨이 추락하도록 둡시다.", "전우를 배신하는 군인답지 못한 비겁한 짓입니다."),
                  ("The jet engine has bad spec so call maintenance.", "제트 엔진 스펙이 안 좋으니 정비실에 전화합시다.", "‘spec’은 콩글리시입니다.")),
                 ("Enemy took the bait! Merging at combined speed of Mach two! Passing canopy to canopy! He's pulling into a vertical scissor! G-meter reads 9.2!",
                  "적이 미끼를 물었어! 합산 속도 마하 2로 정면 교차! 캐노피와 캐노피가 스치듯 지나갔어! 놈이 수직 시저스 기동으로 솟구치고 있어! G미터가 9.2를 가리켜!",
                  "의식을 잃지 않도록 복압을 조이며 기수를 수직으로 세워 적기의 선회 반경 안쪽을 파고들라고 다그치세요.",
                  ("Lock vision! Strain the torso! Tighten the turn radius inside his circle! Guns, guns, guns—fire the twenty-millimeter Vulcan cannon!", "시야 집중! 상체 근육 긴장 유지! 놈의 회전 반경 안쪽으로 선회 조여라! 발사, 발사, 발사—20밀리 벌컨포를 쏟아부어라!", "‘guns, guns, guns’는 공중전 기관포 사격 시 전 세계 조종사들이 외치는 전율의 콜아웃입니다."),
                  ("Close eyes and ask the enemy to stop turning.", "눈감고 적기에게 선회 좀 그만하라고 부탁합시다.", "공중전에서 즉시 격추당하는 패배자의 태도입니다."),
                  ("Check your handphone for flight simulator tips.", "비행 시뮬레이터 팁을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                 ("Enemy aircraft shredded! Wingman woke up and recovered at five hundred feet! Both eagles safely on carrier arresting wires! You are the greatest to ever fly.",
                  "적기 산산조각! 윙맨이 500피트 상공에서 의식을 되찾고 수평을 잡았어! 두 독수리 모두 항공모함 어레스팅 와이어에 안전하게 착함 완료! 자네는 하늘을 난 사상 최고의 조종사야.",
                  "진정한 비행은 전우를 믿고 끝까지 날개를 지켜내는 데 있다고 화답하세요.",
                  ("We fight for the aviator flying beside us, Maverick. Two jets on the deck, all pilots accounted for. The sky is clear.", "우리는 곁에서 함께 날아주는 전우를 위해 싸웁니다. 두 대의 전투기 모두 착함 완료, 전원 무사 귀환. 하늘은 이제 평화롭습니다.", "탑건 비행사들의 형제애와 승리를 완성하는 가슴 벅찬 명대사입니다."),
                  ("I am glad we don't have to pull Gs anymore.", "이제 중력가속도 안 받아도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                  ("Let's do Dutch pay for the carrier beer.", "항모 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ])
        ]
    )

    return data
