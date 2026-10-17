# -*- coding: utf-8 -*-
"""
Dramactor Scenario Group 3 (Genres 10 to 19: 10 genres x 4 cycles = 40 episodes)
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
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_batch3_scenarios():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [
            make_turn(t[0], t[1], t[2], t[3], t[4], t[5])
            for t in turns_data
        ]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # 10. CIA Covert Espionage
    data["CIA Covert Espionage"] = [
        mk_ep(
            "프라하 안전가옥 포위: 자정의 비상 탈출(Exfiltration)",
            "Station Chief Carrie (CIA Vienna Station)", "🕵️‍♂️",
            "동유럽 프라하의 극비 안전가옥. 현지 방첩 기관이 골목을 포위하기 시작했다. 변절 과학자와 함께 위조 여권으로 국경을 넘기 위한 5분간의 탈출 작전을 지휘해야 한다.",
            "initiate the emergency exfiltration protocol",
            "현지 첩보기관의 추적을 따돌리고 비밀 탈출 작전을 개시할 때 쓰는 CIA 전문 첩보 용어입니다.",
            [
                ("Surveillance vans on both ends of the alley. Thermal cameras active. We have four minutes before the strike team breaches. What's the escape vector?",
                 "골목 양쪽 끝에 감시 밴이 붙었어. 열화상 카메라 가동 중이야. 강습조가 진입하기까지 4분 남았네. 탈출 경로가 뭐야?",
                 "열화상 감시를 교란하기 위해 연막탄을 터뜨리고 지하 폐수로로 즉시 우회하자고 명령하세요.",
                 ("Pop smoke to blind their thermals and drop through the storm drain into the sewer grid immediately. Move!", "열화상 장비를 무력화할 연막탄을 터뜨리고 즉시 배수구를 통해 지하 하수관으로 진입하십시오. 움직여!", "‘pop smoke’와 ‘storm drain’은 전술 탈출 작전의 핵심 지휘 언어입니다."),
                 ("Let us wave white flags and ask them for peace.", "백기를 흔들며 평화를 요구합시다.", "첩보전에서 바로 체포되어 수용소로 직행하는 발언입니다."),
                 ("The car has bad spec so call the AS center.", "차가 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                ("We're in the tunnels. The asset is hyperventilating and dropped his flash drive containing the nuclear blueprints. Go back for it or keep moving?",
                 "하수도 안이야. 망명 과학자가 과호흡에 빠져 핵 설계도가 든 플래시 드라이브를 떨어뜨렸어. 주우러 돌아갈까, 계속 이동할까?",
                 "클라우드 1회성 원격 백업이 완료되었으니 지체 없이 국경 철도역으로 전진하라고 다그치세요.",
                 ("Leave it. I already mirrored the encrypted drive to Langley via quantum burst transmission. Keep moving to the rail yard!", "버려두십시오. 이미 양자 버스트 전송으로 랭글리 본부에 암호화 미러링을 마쳤습니다. 철도 조차장으로 계속 전진하세요!", "‘quantum burst transmission’은 첨단 첩보전의 극치를 보여주는 멋진 대처입니다."),
                 ("Wait ten minutes until he stops crying.", "그가 울음을 그칠 때까지 10분만 기다립시다.", "추격조에게 따라잡히는 안일한 행동입니다."),
                 ("Give him delicious candy for skinship.", "스킨십을 위해 맛있는 사탕을 줍시다.", "‘skinship’은 콩글리시입니다.")),
                ("Train cleared the Austrian border. The asset is safe under embassy protection. You brought him home without leaving a single fingerprint. Masterclass, officer.",
                 "기차가 오스트리아 국경을 통과했어. 망명자는 대사관 보호 아래 안전하네. 지문 하나 남기지 않고 구출에 성공했어. 특급 작전이었네, 요원.",
                 "우리의 이름은 역사에 남지 않지만 조국은 안전할 것이라고 묵직하게 화답하세요.",
                 ("We operate in the shadows so freedom can stand in the light. Job done, Carrie.", "자유가 빛 속에 서 있을 수 있도록 우리는 그림자 속에서 일할 뿐입니다. 임무 완료했습니다, 캐리 팀장님.", "CIA의 모토를 담은 최고의 피날레 대사입니다."),
                 ("I am glad we don't have to walk anymore.", "더 이상 안 걸어도 돼서 참 좋습니다.", "첩보 요원답지 못한 답변입니다."),
                 ("Let's do Dutch pay for the Vienna beer tonight.", "오늘 밤 비엔나 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "베를린 냉전 다리: 포로 교환(Bridge of Spies)",
            "Station Chief Carrie (CIA Vienna Station)", "🕵️‍♂️",
            "안개 자욱한 글리니케 다리 한가운데. 동서 진영의 최고 스파이를 맞교환하는 긴장의 순간. 적국 장교가 추가 정보 제공을 거부하며 협상 파기를 위협한다.",
            "execute the cold-war prisoner exchange at the bridge",
            "동서 냉전의 상징적인 다리 위에서 포로 교환을 성사시킬 때 쓰는 표현입니다.",
            [
                ("Their negotiator claims our pilot has brain trauma and refuses to release him without our deep-cover agent's cipher book. Do we blink?",
                 "상대 협상관이 우리 조종사가 뇌 손상을 입었다며 우리 잠입 요원의 암호책 없이는 석방할 수 없다고 버텨. 물러설까?",
                 "한 글자의 양보도 없으며 60초 안에 조종사를 인도하지 않으면 상대 장군을 영구 수감하겠다고 통보하세요.",
                 ("No deal. Tell them either our pilot walks across that bridge in sixty seconds, or their general rots in ADX Florence forever.", "타협은 없습니다. 60초 안에 우리 조종사가 저 다리를 건너오지 않으면, 그들의 장군은 연방 최고보안 교도소에서 평생 썩게 될 것이라 통보하십시오.", "‘ADX Florence’와 ‘walks across that bridge’는 상대의 허세를 꺾는 단호한 압박입니다."),
                 ("Let's give them all secret books so nobody gets mad.", "누구도 화나지 않게 비밀 책을 다 넘겨줍시다.", "국가 기밀을 헐값에 넘기는 굴욕입니다."),
                 ("The spy has a bad personality so let's claim to him.", "스파이가 성격이 나쁘니 그에게 클레임합시다.", "‘claim’은 콩글리시입니다.")),
                ("Their general is walking across. But our pilot collapsed halfway across the frost-covered planks. He's not moving.",
                 "상대 장군이 다리를 건너오고 있어. 그런데 우리 조종사가 서리 낀 나무판 중간에서 쓰러졌어. 움직이지 않아.",
                 "저격수 조준을 유지하며 현장 팀을 투입해 부축하고 교환선 너머로 신속히 견인하라고 명령하세요.",
                 ("Keep snipers trained on their perimeter. Tac-team, sprint to the midline, extract the pilot, and drag him across the chalk mark now!", "상대 외곽에 저격수 조준 유지하십시오. 전술팀, 중앙선으로 전력 질주해 조종사를 확보하고 지금 즉시 백색선 너머로 끌어당기세요!", "‘keep snipers trained’와 ‘extract the pilot’은 숨 막히는 현장 지휘의 정석입니다."),
                 ("Let's shout at the pilot to stand up quickly.", "조종사에게 빨리 일어나라고 소리나 지릅시다.", "무력하고 비전문적인 대처입니다."),
                 ("Check the handphone for the Russian weather app.", "러시아 날씨 앱을 보기 위해 핸드폰을 체크하세요.", "‘handphone’은 콩글리시입니다.")),
                ("Pilot across the line! Embassy transport secured. Both assets cleared. You just orchestrated the cleanest cold-war trade in three decades.",
                 "조종사 경계선 통과 완료! 대사관 호송 차량 탑승 완료. 30년 만에 가장 깔끔한 스파이 교환 작전을 완수했네.",
                 "우리는 단 한 명의 요원도 적진에 홀로 남겨두지 않는다고 자부심을 드러내세요.",
                 ("We never leave our people behind, Carrie. Not in the cold, not ever.", "우리는 결코 아군을 적진에 남겨두지 않습니다, 캐리. 추위 속에서도, 그 언제라도요.", "스파이 드라마의 감동을 완성하는 명대사입니다."),
                 ("I am happy we can go eat hot soup now.", "이제 따뜻한 수프를 먹으러 갈 수 있어서 기쁩니다.", "긴장의 여운을 깨뜨리는 가벼운 소감입니다."),
                 ("Let's do Dutch pay for the Berlin coffee.", "베를린 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "이중간첩의 덫: 모스크바 지부의 두더지(Mole) 색출",
            "Station Chief Carrie (CIA Vienna Station)", "🕵️‍♂️",
            "CIA 본부 극비 회의실. 모스크바 지부의 현장 첩보망 4개가 연쇄 붕괴되었다. 침투한 두더지를 잡기 위해 거짓 기밀을 흘리는 카나리아 함정(Canary Trap)을 가동해야 한다.",
            "plant the canary trap to expose the internal mole",
            "각 의심자에게 서로 다른 거짓 기밀을 유출해 스파이를 역추적할 때 쓰는 표현입니다.",
            [
                ("Four case officers executed in seventy-two hours. The mole sits inside our directorate. How do we smoke him out without tipping off the Kremlin?",
                 "72시간 만에 공작관 4명이 처형당했어. 두더지는 우리 본부 지휘부 안에 있어. 크렘린에 눈치채지 않게 그를 어떻게 유인해낼 텐가?",
                 "3명의 부국장에게 서로 다른 위조 작전 암호명을 전달해 유출된 암호명을 추적하자고 하세요.",
                 ("Seed three distinct counterfeit operational codenames to the suspects. Whichever codename flashes on Moscow's intercepted comms unmasks our traitor.", "용의자 세 명에게 각기 다른 위조 작전 암호명을 흘리십시오. 모스크바의 감청 통신에 걸려드는 암호명이 바로 배신자의 정체를 밝혀낼 것입니다.", "‘canary trap’의 작동 원리를 명쾌하게 적용한 천재적인 작전 지시입니다."),
                 ("Ask everyone in the office if they love Russia.", "사무실 사람들에게 러시아를 좋아하는지 물어봅시다.", "스파이에게 도망칠 기회를 주는 바보 같은 질문입니다."),
                 ("The mole has bad manner so let's punish him.", "두더지가 매너가 나쁘니 처벌합시다.", "‘manner’는 콩글리시입니다.")),
                ("The Kremlin just scrambled a submarine off Sevastopol matching document 'Blue-Echo'. That document was given exclusively to Deputy Director Vance.",
                 "크렘린이 방금 세바스토폴에서 '블루 에코' 문건에 일치하는 잠수함을 발진시켰어. 그 문건은 밴스 부국장에게만 단독 전달된 거야.",
                 "그의 공항 출국을 조용히 차단하고 본부 엘리베이터에서 연방수사국과 함께 현행범 체포하라고 지시하세요.",
                 ("Red-flag his diplomatic passport immediately. Trap him between floors in the executive elevator with an armed tactical team.", "그의 외교 여권을 즉시 출국 정지 조치하십시오. 본부 임원 엘리베이터를 층간 정지시키고 무장 전술팀으로 체포하십시오.", "‘red-flag passport’와 ‘trap between floors’는 스파이를 도주 없이 생포하는 냉혹한 작전입니다."),
                 ("Wait until he goes home and call his telephone.", "그가 집에 갈 때까지 기다렸다가 전화를 걸어봅시다.", "이미 비행기를 타고 모스크바로 망명할 것입니다."),
                 ("Send an SNS message asking Vance to surrender.", "밴스에게 항복하라는 SNS 메시지를 보냅시다.", "‘SNS’는 콩글리시입니다.")),
                ("Vance secured in federal detention! The entire foreign network is saved from execution. You cut out a cancer that ate at Langley for a decade.",
                 "밴스 체포 완료! 해외 공작원 전체가 처형 위기에서 구출되었어. 10년간 랭글리를 갉아먹던 암 덩어리를 자네가 도려냈네.",
                 "배신은 영원히 숨을 수 없으며 충성은 언제나 입증되는 법이라고 답하세요.",
                 ("Treason always leaves a trace, Carrie. The shadows protect the loyal, not the corrupt.", "반역은 언제나 흔적을 남깁니다, 캐리. 그림자는 충직한 자를 지킬 뿐, 부패한 자를 품어주지 않습니다.", "미드 명대사의 무게감을 선사하는 멋진 클로징입니다."),
                 ("I am happy we can go home early today.", "오늘 일찍 퇴근할 수 있어서 기쁩니다.", "국가 기밀 위기를 넘긴 순간에 어울리지 않는 말입니다."),
                 ("Let's do Dutch pay for the agency pizza.", "본부 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "사이버 블랙아웃: 적국 원자력 시설 스턱스넷 주입",
            "Station Chief Carrie (CIA Vienna Station)", "🕵️‍♂️",
            "중동 지하 원심분리기 시설 50미터 아래. 인터넷과 완전히 단절된 에어갭(Air-gap) 원자로를 무력화하기 위해 현장 엔지니어의 USB에 악성코드를 침투시켜야 한다.",
            "deliver the zero-day payload across the physical air-gap",
            "네트워크가 차단된 원자력 시설에 물리적 저장매체로 악성 페이로드를 전달할 때 쓰는 첩보 용어입니다.",
            [
                ("The facility is completely air-gapped. Zero wireless signals. The centrifuge control room is guarded by fifty armed commandos. How do we deliver the payload?",
                 "시설이 완전히 에어갭 격리되어 있어. 무선 신호 전무. 원심분리기 제어실은 무장 특수부대원 50명이 지키고 있어. 페이로드를 어떻게 주입할 건가?",
                 "납품 업체의 진동 계측기 펌웨어 업데이트 USB 드라이브를 가로채 변조 코드를 심자고 제안하세요.",
                 ("Intercept the third-party vibration contractor's diagnostic USB drive and inject our zero-day payload into the root kernel firmware.", "외부 진동 계측 업체의 진단용 USB 드라이브를 가로채 루트 커널 펌웨어에 우리의 제로데이 악성코드를 주입하십시오.", "‘zero-day payload’와 ‘root kernel firmware’는 스턱스넷 작전을 재현하는 초고난도 침투 기법입니다."),
                 ("Throw the USB drive over the high concrete wall.", "높은 콘크리트 벽 너머로 USB를 던져버립시다.", "초등학생 장난 수준의 황당한 대처입니다."),
                 ("The USB has bad spec so buy a new one.", "USB 스펙이 안 좋으니 새것을 사 오세요.", "‘spec’은 콩글리시입니다.")),
                ("Payload injected! The centrifuges are spinning ten times faster than design tolerance, but their monitors show normal green status! They have two minutes.",
                 "페이로드 주입 성공! 원심분리기가 허용 오차의 10배 속도로 회전하고 있어. 하지만 계기판엔 정상 초록 불이 들어와 있네! 2분 남았어.",
                 "열 폭주로 파괴되기 전에 현장 요원들에게 비상 철수 신호를 타전하라고 명령하세요.",
                 ("Issue the priority green-burst evacuation order to our undercover asset. The facility will self-destruct from rotor fatigue in ninety seconds.", "잠입 요원에게 최우선 비상 탈출 신호를 발신하십시오. 회전자 피로 파괴로 90초 안에 시설이 자체 파멸할 것입니다.", "‘priority evacuation order’와 ‘rotor fatigue’는 완벽한 파괴 공작의 종결 명령입니다."),
                 ("Tell the workers to run away quickly on foot.", "노동자들에게 걸어서 빨리 도망치라고 말하세요.", "현장 통제력이 없는 어설픈 외침입니다."),
                 ("Check the handphone for satellite images.", "위성 이미지를 보려고 핸드폰을 체크하세요.", "‘handphone’은 콩글리시입니다.")),
                ("Facility neutralized! Centrifuges shattered without a single civilian casualty. Their nuclear program is set back a decade. You pulled off a modern miracle.",
                 "시설 무력화 완료! 민간인 사상자 단 한 명 없이 원심분리기가 산산조각 났어. 핵 개발 프로그램이 10년 후퇴했네. 자네가 현대의 기적을 일궈냈어.",
                 "총알 한 발 쏘지 않고 조국의 안보를 수호한 것이 현대 첩보의 예술이라고 답하세요.",
                 ("True deterrence doesn't require dropping bombs, Carrie—it's executed with a whisper and a ghost in the machine.", "진정한 억제력은 폭탄을 투하하는 것이 아닙니다, 캐리. 속삭임과 기계 속의 유령으로 은밀하게 집행하는 것입니다.", "최고급 첩보 스릴러의 품격을 보여주는 마무리입니다."),
                 ("I am happy the work is finally done.", "일이 드디어 끝나서 참 기쁩니다.", "평범하고 감동이 덜한 반응입니다."),
                 ("Let's do Dutch pay for the agency dinner.", "본부 저녁 식사는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    # 11. Aviation Cockpit Emergency
    data["Aviation Cockpit Emergency"] = [
        mk_ep(
            "허드슨강의 기적: 3천 피트 양쪽 엔진 정지",
            "Captain Vance (Veteran Flight Captain)", "✈️",
            "뉴욕 라과디아 이륙 2분 후 3,200피트 상공. 거대 조류 떼와 정면충돌하며 에어버스 여객기 양쪽 제트 엔진이 동시에 폭발 정지했다. 155명의 승객을 태우고 활주로 복귀와 강 불시착 사이에서 생사의 결단을 내려야 한다.",
            "declare MAYDAY and commit to ditching on the river",
            "동력 상실 시 강 수면 불시착(Ditching)을 최종 결단하고 메이데이를 선포할 때 쓰는 항공 비상 전문 표현입니다.",
            [
                ("Dual engine flameout! Airspeed dropping through two hundred knots! LaGuardia tower says runway four is open! Can we make the runway?",
                 "양쪽 엔진 완전 정지! 대기속도 200노트 아래로 급락 중! 라과디아 관제탑은 4번 활주로가 열려있대! 활주로까지 닿을 수 있겠나?",
                 "활주로 복귀는 고도가 부족해 도심 추락을 부르므로 즉시 메이데이를 선포하고 허드슨강 불시착을 결단하세요.",
                 ("Negative on the runway! We don't have the glide ratio—we'd end up in the buildings. Declare MAYDAY; we are going into the Hudson!", "활주로 복귀 불가능합니다! 활공비가 안 나와 도심 빌딩가에 처박힙니다. 메이데이 선포하십시오. 우리는 허드슨강에 불시착합니다!", "‘We don't have the glide ratio’와 ‘going into the Hudson’은 기적을 만든 셜리 기장의 전설적인 결단입니다."),
                 ("Let's try to restart the engine for twenty minutes.", "20분 동안 엔진 재시동이나 시도해봅시다.", "고도가 수초 만에 바닥나 전원 사망하는 최악의 판단입니다."),
                 ("The airplane has bad spec so call the AS center.", "비행기 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                ("Altitude nine hundred feet! Sinking at a thousand feet per minute! The co-pilot is fighting severe turbulence. Do we deploy full flaps?",
                 "고도 900피트! 분당 1,000피트로 급강하 중! 부기장이 강한 난기류와 사투를 벌이고 있어. 플랩을 전개할까?",
                 "플랩 2단으로 항력을 최소화하고 충돌 10초 전 기수를 11도 들어올려 완충 착수를 준비하라고 명령하세요.",
                 ("Flaps two! Keep the nose up eleven degrees and wings level. Brace for impact on my count: three, two, one!", "플랩 2단계 유지! 기수 11도 들고 날개 수평 완벽히 유지하세요. 내 구호에 맞춰 충격에 대비하십시오. 셋, 둘, 하나!", "‘wings level’과 ‘brace for impact’는 수면 불시착 시 동체 두 동강을 막는 생사의 조종술입니다."),
                 ("Close your eyes and pray to heaven.", "눈을 감고 하늘에 기도나 합시다.", "조종간을 포기하는 무책임한 태도입니다."),
                 ("Check the handphone for family messages.", "가족 메시지를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Water landing successful! Both wings intact! Ferries are pulling alongside to evacuate passengers! All one hundred fifty-five souls accounted for!",
                 "착수 성공! 양쪽 날개 온전함! 통근 페리선들이 승객 구조를 위해 접안하고 있어! 탑승객 155명 전원 생존 확인!",
                 "하늘에서는 수첩의 규칙이 아니라 훈련된 본능과 승객을 향한 책임감이 생명을 구한다고 답하세요.",
                 ("A captain doesn't leave the aircraft until the last soul is safe. Outstanding cockpit discipline, Captain.", "마지막 한 영혼이 무사할 때까지 기장은 조종석을 떠나지 않습니다. 완벽한 칵핏 규율이었습니다, 기장님.", "항공 역사상 최고의 기적을 기리는 감동의 명대사입니다."),
                 ("I am glad I don't have to fly tomorrow.", "내일 비행 안 해도 돼서 참 좋습니다.", "영웅적 생환의 순간에 어울리지 않는 말입니다."),
                 ("Let's do Dutch pay for the Manhattan coffee.", "맨해튼 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "대서양 3만 피트 상공 급감압(Explosive Decompression)",
            "Captain Vance (Veteran Flight Captain)", "✈️",
            "보잉 777 여객기 야간 비행 중 화물칸 도어가 파손되며 기내 기압이 급격히 붕괴되었다. 조종사 산소마스크를 착용하고 30초 내 유효 의식을 유지하며 1만 피트로 비상 급강하해야 한다.",
            "execute emergency descent to ten thousand feet",
            "급감압 상황에서 승객들의 저산소증을 막기 위해 1만 피트 안전 고도로 급강하할 때 쓰는 조종 표현입니다.",
            [
                ("Cockpit window cracked! Cabin altitude horn blaring! Time of useful consciousness is under thirty seconds! What's the immediate memory item?",
                 "조종석 창문 균열! 객실 고도 경보음 폭음! 유효 의식 시간 30초 미만! 즉시 실행할 메모리 아이템이 뭐야?",
                 "산소마스크 100% 착용하고 오토파일럿 분리 후 스피드브레이크를 최대로 당겨 급강하하라고 외치세요.",
                 ("Masks on 100% emergency flow! Idle thrust, speedbrakes deploy! Emergency descent to ten thousand feet right now!", "산소마스크 100% 비상 모드 착용! 추력 아이들, 스피드브레이크 전개! 지금 즉시 1만 피트로 비상 급강하!", "‘masks on’과 ‘emergency descent’는 감압 비상 체크리스트의 절대적인 1순위 생존 공식입니다."),
                 ("Let's wait a minute to see if the air comes back.", "공기가 다시 돌아오는지 1분만 기다려봅시다.", "저산소증으로 전원 실신해 추락을 자초합니다."),
                 ("The cabin has bad spec so call the engineer.", "객실 스펙이 안 좋으니 엔지니어를 부릅시다.", "‘spec’은 콩글리시입니다.")),
                ("Leveling off at ten thousand feet. Oxygen levels stable. But the rudder trim is jammed from structural debris. Air traffic control asks our intention.",
                 "1만 피트 수평 비행 진입. 산소 수치 안정화. 하지만 파편으로 인해 방향타 트림이 고착되었어. 관제탑이 우리의 비행 의도를 묻고 있네.",
                 "비상사태를 유지하며 차동 추력(Differential Thrust)으로 방향을 잡고 인근 군 기지에 긴급 착륙을 요청하세요.",
                 ("Declare emergency. Steer using differential engine thrust and vector us for an immediate straight-in ILS approach to Shannon Air Base.", "비상사태 선포 유지. 좌우 엔진 차동 추력으로 기수를 선회하고 샤넌 공군기지 직선 계기착륙(ILS) 경로로 유도해주십시오.", "‘differential engine thrust’와 ‘straight-in ILS approach’는 유압 상실 비행기를 살려내는 베테랑의 기량입니다."),
                 ("Tell the passengers to jump with parachutes.", "승객들에게 낙하산 메고 뛰어내리라고 방송합시다.", "여객기에는 낙하산이 없으며 공황만 유발합니다."),
                 ("Let's have skinship with the purser.", "사무장과 스킨십을 나눕시다.", "‘skinship’은 콩글리시입니다.")),
                ("Touchdown confirmed! Tires smoked on the tarmac, emergency slides deployed, zero casualties! Boeing engineers said that flight was aerodynamically unsurvivable.",
                 "착륙 완료! 활주로에 타이어 연기를 뿜으며 비상 슬라이드 전개, 전원 무사 생환! 보잉사 엔지니어들은 이 기체가 공기역학적으로 생존 불가능했다고 말하네.",
                 "규율과 냉철한 판단이 공학적 한계를 뛰어넘어 기적을 만든다고 화답하세요.",
                 ("Steel and rivets may fail in the sky, Vance, but human training and iron discipline bring the metal home.", "하늘에서 철과 리벳은 부서질 수 있어도, 인간의 훈련과 강철 같은 규율은 기체를 끝내 지상으로 데려옵니다.", "비행 안전의 숭고한 본질을 짚어주는 명대사입니다."),
                 ("I am glad we don't have to fill out paperwork.", "서류 작업 안 해도 돼서 참 좋습니다.", "사고 조사 청문회가 남아있음을 모르는 철없는 소리입니다."),
                 ("Let's do Dutch pay for the hotel beer.", "호텔 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "카테고리 5 윈드시어: 뇌우 속 윈드터뷸런스 착륙 결단",
            "Captain Vance (Veteran Flight Captain)", "✈️",
            "시카고 오헤어 공항 최종 착륙 진입로. 거대 슈퍼셀 뇌우와 마이크로버스트(Microburst) 급변풍이 몰아치며 활주로 코앞에서 속도가 급변한다. 복행(Go-Around)을 결단해야 한다.",
            "execute an immediate go-around and escape windshear",
            "착륙 직전 급변풍 위험 감지 시 즉각 상승 복행 절차를 집행할 때 쓰는 전문 비행 표현입니다.",
            [
                ("Windshear alert blaring! Airspeed fluctuation plus thirty knots, then minus twenty! Ground proximity warning screams: 'PULL UP!' Do we force it down?",
                 "윈드시어 경보 울림! 대기속도 변동 폭 플러스 30노트에서 마이너스 20노트로 급락! 지상근접경고가 'PULL UP!'을 외치고 있어! 착륙을 강행할까?",
                 "지체 없이 최대 추력으로 복행하여 윈드시어 회피 기동을 단행하라고 소리치세요.",
                 ("Go-around! TOGA thrust! Flaps to approach, positive rate, gear up! Escape the windshear pocket immediately!", "복행! 최대 추력(TOGA)! 플랩 접근 위치, 상승률 확인, 착륙바퀴 올려! 즉시 윈드시어 포켓을 탈출한다!", "‘TOGA thrust’와 ‘escape the windshear’는 항공 참사를 막는 가장 완벽한 찰나의 결단입니다."),
                 ("Let's land anyway and step on the brakes hard.", "어쨌든 착륙해서 브레이크를 세게 밟읍시다.", "활주로 이탈 폭발 사고를 부르는 자살행위입니다."),
                 ("The cloud has bad spec so tell the controller.", "구름 스펙이 안 좋으니 관제사에게 항의합시다.", "‘spec’은 콩글리시입니다.")),
                ("Climbing out through turbulence. Fuel state is now down to thirty minutes. Alternate airport Milwaukee has severe fog. We need a diversion plan.",
                 "난기류를 뚫고 상승 중. 잔여 연료는 이제 30분 치뿐이야. 회항 공항인 밀워키는 짙은 안개가 끼어있어. 대체 회항 계획이 필요해.",
                 "연료 비상 선포(Mayday Fuel) 후 인근 공군 기지의 긴급 활주로 우선권을 요구하자고 하세요.",
                 ("Declare Mayday Fuel to Chicago Center. Divert to Rockford International; demand priority vectors for the long military runway.", "시카고 관제소에 '메이데이 퓨얼'을 선포하십시오. 록퍼드 국제공항으로 회항해 긴 군용 활주로 최우선 유도를 요구하세요.", "‘Mayday Fuel’과 ‘priority vectors’는 연료 고갈 직전 관제권을 독점하는 항공 비상 용어입니다."),
                 ("Let's circle around Chicago until the storm passes.", "폭풍이 지나갈 때까지 시카고 상공을 빙빙 돕시다.", "연료가 바닥나 공중 추락하는 위험한 생각입니다."),
                 ("Send an SNS message to passengers to keep quiet.", "승객들에게 조용히 하라는 SNS 메시지를 보냅시다.", "‘SNS’는 콩글리시입니다.")),
                ("Rockford runway cleared! Safe landing with four minutes of fuel remaining! The NTSB investigators commended our lightning-fast go-around decision.",
                 "록퍼드 활주로 개방 확인! 잔여 연료 4분 남기고 안전 착륙 성공! 연방교통안전위원회(NTSB) 조사관들이 번개 같은 복행 결정을 극찬했네.",
                 "착륙을 포기할 줄 아는 용기가 최고의 조종사를 만든다고 화답하세요.",
                 ("A good pilot has the skill to land, Captain, but a great pilot has the courage to go around. We brought everybody home.", "좋은 조종사는 착륙시키는 기술을 가졌지만, 위대한 조종사는 과감히 복행할 용기를 가졌습니다. 우리 모두를 무사히 집으로 데려왔습니다.", "항공인의 가슴을 울리는 진정한 명언입니다."),
                 ("I am glad we don't have to clean the airplane.", "비행기 청소 안 해도 돼서 참 좋습니다.", "위기 극복의 숭고함을 퇴색시키는 반응입니다."),
                 ("Let's do Dutch pay for the Rockford taxi.", "록퍼드 택시비는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "기장 흉통 실신: 부기장의 야간 계기착륙 단독 조종",
            "Captain Vance (Veteran Flight Captain)", "✈️",
            "대서양 횡단 야간 비행 중 기장이 급성 심근경색으로 의식을 잃었다. 부기장인 당신이 300명의 승객을 짊어지고 시정 100미터의 안개 낀 런던 히드로 공항에 단독 계기착륙을 완수해야 한다.",
            "assume solo command and execute autoland approach",
            "조종 불능 기장을 대신해 단독 지휘권을 인수하고 자동계기착륙을 집행할 때 쓰는 표현입니다.",
            [
                ("Captain is unresponsive! Pulse is weak! Purser is administering CPR in the jumpseat! You have full control of the aircraft! What is your protocol?",
                 "기장님이 의식을 잃었어! 맥박이 약해! 사무장이 보조석에서 심폐소생술 중이야! 자네가 기체 단독 조종권을 쥐었네! 매뉴얼 수순이 뭐야?",
                 "지휘권을 인수하고 즉시 의료 비상사태 선포 후 히드로 관제소에 앰뷸런스와 직선 접근을 요구하세요.",
                 ("I have controls. Declare a medical emergency to London Control. Request uninterrupted priority descent for Cat Three autoland on runway two-seven-right.", "내가 조종간을 인수합니다. 런던 관제소에 의료 비상사태를 선포하십시오. 27번 우측 활주로 카테고리 3 자동착륙을 위한 최우선 직선 강하를 요청하세요.", "‘I have controls’와 ‘Cat Three autoland’는 위기 상황에서 지휘권을 장악하는 완벽한 칵핏 콜아웃입니다."),
                 ("Let's cry loudly so passengers help us.", "승객들이 도와주도록 크게 울어봅시다.", "승객 공황만 유발하는 최악의 행동입니다."),
                 ("The captain has bad health spec so call his family.", "기장님 건강 스펙이 안 좋으니 가족에게 전화하세요.", "‘spec’은 콩글리시입니다.")),
                ("London reports thick pea-soup fog. Runway visual range is only seventy-five meters. Autopilot is tracking the localizer. Decision height is fifty feet.",
                 "런던에 짙은 완두콩 수프 안개가 꼈어. 활주로 가시거리는 75미터에 불과해. 오토파일럿이 로컬라이저를 추적 중이야. 결심 고도는 50피트네.",
                 "계기 수치를 교차 검증하며 50피트 결심 고도까지 흔들림 없이 접근을 유지하라고 자신을 다잡으세요.",
                 ("Tracking localizer and glideslope. System triple-channel redundant. Hands hovering on throttle; committing to autoland at decision height.", "로컬라이저와 글라이드슬로프 정대 확인. 3중 중복 시스템 정상. 스로틀 위에 손을 얹고 대기하며 결심 고도에서 자동착륙을 완수합니다.", "‘triple-channel redundant’와 ‘decision height’는 최고 등급 맹검 착륙을 이끄는 프로페셔널한 집중력입니다."),
                 ("Let's look out the window and guess where the ground is.", "창밖을 보면서 땅이 어디쯤인지 대충 짐작해봅시다.", "시계가 없는 상황에서 치명적인 충돌을 부릅니다."),
                 ("Check the handphone for London hotel reservation.", "런던 호텔 예약을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                ("Main gear on the centerline! Reverse thrust engaged! Rollout guidance brought the 777 to a complete halt! Paramedics boarded and saved the Captain's life!",
                 "메인 기어 중심선 터치다운! 역추력 전개! 활주 유도 장치가 777 기체를 완벽히 정지시켰어! 응급구조대가 탑승해 기장님의 목숨을 살려냈네!",
                 "진정한 비행사는 시련이 닥쳤을 때 두려움을 이기고 날개를 지켜낸다고 겸손히 화답하세요.",
                 ("The four stripes on your shoulders aren't just fabric, Vance—they represent the trust of every life behind that cockpit door. Mission accomplished.", "어깨 위의 네 줄 계급장은 단순한 천 조각이 아닙니다. 조종실 문 뒤에 있는 모든 생명의 신뢰를 의미합니다. 임무 완료했습니다.", "부기장에서 진정한 캡틴으로 거듭나는 감동의 순간입니다."),
                 ("I am glad I can drink beer at the pub now.", "이제 펍에서 맥주를 마실 수 있어서 기쁩니다.", "장엄한 순간의 가치를 떨어뜨립니다."),
                 ("Let's do Dutch pay for the London taxi.", "런던 택시비는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    return data
