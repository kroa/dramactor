# -*- coding: utf-8 -*-
"""
Dramactor 100 Curated Master Database
Contains 92 authentic American drama scenario templates.
"""

# Dictionary of 92 distinct scenarios mapped to episode numbers 9..100
EPISODES_9_TO_100 = [
    # -------------------------------------------------------------
    # EP 9 ~ 20 (Batch 1: Genres 9 to 20)
    # -------------------------------------------------------------
    {
        "ep_num": 9,
        "title": "백악관 상황실: 자정의 미사일 요격 결단",
        "genre": "Politics",
        "speaker": "General Hayes (Chairman of Joint Chiefs)",
        "emoji": "🏛️",
        "synopsis": "워싱턴 D.C. 백악관 지하 상황실. 미확인 대륙간 탄도체가 레이더에 포착되고 국가안보보좌관인 당신에게 대통령 직보 직전의 군사 옵션 판단을 묻는다.",
        "turns": [
            {
                "dialogue": "Radar confirms the telemetry. We have six minutes before the warhead crosses the intercept vector. Do we scramble defensive batteries or initiate kinetic strike?",
                "korean": "레이더가 원격 측정 신호를 확인했습니다. 탄두가 요격 고도에 진입하기까지 6분 남았습니다. 방어 포대를 가동합니까, 아니면 즉각 타격에 나섭니까?",
                "hint": "합참의장이 6분 남은 상황에서 방어 요격과 선제 타격 중 결단을 촉구한다.",
                "choices": [
                    ("Authorize defensive interceptors immediately while keeping strike wings on standby.", "방어 요격 미사일을 즉각 승인하고, 타격 편대는 즉시 출격 대기 상태로 유지하십시오.", "native_killer", "'Authorize defensive interceptors'는 백악관 안보회의의 정석 브리핑 표현입니다."),
                    ("We should wait and see what happens first.", "먼저 무슨 일이 일어나는지 지켜봐야 합니다.", "wrong_konglish", "군사 위기 상황에서 'wait and see'는 돌이킬 수 없는 재앙을 초래합니다."),
                    ("Let us shoot it down right now.", "지금 당장 그것을 격추합시다.", "mediocre", "의미는 통하나 국가안보보좌관다운 격식 있는 군사 용어가 아닙니다.")
                ]
            },
            {
                "dialogue": "If the intercept fails, casualty estimates in the sector exceed forty thousand. Are you prepared to own that outcome before the President?",
                "korean": "만약 요격이 실패하면 해당 구역의 사상자 추정치가 4만을 넘어섭니다. 대통령 앞에서 그 결과에 책임을 질 준비가 되셨습니까?",
                "hint": "요격 실패 시 대규모 사상자가 발생할 수 있다며 책임을 감당할 수 있는지 묻는다.",
                "choices": [
                    ("I take full accountability. Stand by the President; I'll deliver the situational brief.", "제가 전적으로 책임지겠습니다. 대통령 곁을 지키십시오. 현장 브리핑은 제가 맡겠습니다.", "native_killer", "'take full accountability'와 'deliver the situational brief'는 정치 드라마 속 리더십의 표본입니다."),
                    ("It is not my fault if the weapon misses.", "무기가 빗나가면 그건 제 잘못이 아닙니다.", "wrong_konglish", "책임 회피는 백악관 핵심 참모로서 즉각 해임 사유입니다."),
                    ("Yes, I understand the danger very well.", "네, 그 위험을 아주 잘 알고 있습니다.", "mediocre", "수동적인 태도로 책임 있는 결단력이 돋보이지 않습니다.")
                ]
            },
            {
                "dialogue": "Direct hit confirmed over open ocean. Debris neutralized. Outstanding call, counselor.",
                "korean": "공해 상공에서 직격 성공 확인. 파편 무력화 완료. 훌륭한 판단이었습니다, 고문님.",
                "hint": "직격 격추에 성공해 위험이 제거되자 의장이 탁월한 판단이었다고 경의를 표한다.",
                "choices": [
                    ("Maintain DEFCON two until satellite arrays verify no second-wave telemetry.", "위성 감시망이 2차 발사 징후가 없음을 검증할 때까지 데프콘 2 단계를 유지하십시오.", "native_killer", "위기 해소 직후에도 방심하지 않는 'Maintain DEFCON two'는 최고의 카리스마 마무리입니다."),
                    ("Thank goodness, we can finally take a rest.", "다행이네요, 이제 좀 쉴 수 있겠습니다.", "wrong_konglish", "국가 비상 상황실에서 긴장을 너무 일찍 푸는 부적절한 태도입니다."),
                    ("Good job everyone, thank you very much.", "모두 수고하셨습니다, 대단히 감사합니다.", "mediocre", "평이한 인사말로 참모 본부의 긴장감을 이어가지 못합니다.")
                ]
            }
        ],
        "key_expr": "Authorize interceptors / Stand by",
        "key_note": "'Authorize interceptors'는 비상 요격 명령, 'Stand by'는 즉시 대기 태세를 뜻하는 정통 군사 안보 표현입니다."
    },
    {
        "ep_num": 10,
        "title": "미슐랭 3스타 주방: 헤드 셰프의 격노",
        "genre": "Culinary",
        "speaker": "Chef Marco (Executive Head Chef)",
        "emoji": "🔪",
        "synopsis": "시카고 최고급 파인다이닝 레스토랑의 피크타임 서비스. 미슐랭 암행 평가원이 VIP 4번 테이블에 앉은 순간, 소테 스테이션의 메인 수비드 양갈비 온도가 흔들린다.",
        "turns": [
            {
                "dialogue": "Table four is the Michelin inspector and your venison jus is splitting! Are you trying to burn my third star to the ground?!",
                "korean": "4번 테이블이 미슐랭 평가원인데 네 사슴고기 주(jus) 소스가 분리되고 있잖아! 내 세 번째 별을 통째로 불태워 없애버릴 셈이야?!",
                "hint": "헤드 셰프가 소스가 분리된 것을 보고 별을 날릴 셈이냐며 주방 전체를 뒤흔들며 소리친다.",
                "choices": [
                    ("Emulsifying a fresh reduction now. Service will not be delayed by a single second, chef!", "새 리덕션 즉시 유화 결합 중입니다. 단 1초도 서비스 지연되지 않습니다, 셰프!", "native_killer", "'The Bear' 스타일의 긴박하면서도 군더더기 없는 완벽한 주방 현장 전문 용어입니다."),
                    ("Sorry chef, I think the fire was too hot.", "죄송합니다 셰프님, 불이 너무 셌던 것 같습니다.", "wrong_konglish", "변명은 헤드 셰프를 더 분노하게 만듭니다."),
                    ("I will make it again as fast as possible.", "최대한 빨리 다시 만들겠습니다.", "mediocre", "의미는 맞지만 프로 파인다이닝의 정교한 언어가 아닙니다.")
                ]
            },
            {
                "dialogue": "You have forty-five seconds to plate, garnish, and wipe the rim. Hands up when ready!",
                "korean": "플레이팅하고 가니시 얹고 접시 테두리 닦기까지 45초 준다. 준비되면 두 손 들어!",
                "hint": "45초 안에 완성하고 테두리를 닦으라며 카운트다운을 시작한다.",
                "choices": [
                    ("Plated and pristine! Walking table four right behind you, chef!", "플레이팅 무결점 완료! 셰프님 바로 뒤에서 4번 테이블 서빙 들어갑니다!", "native_killer", "'Plated and pristine'과 'Walking table four'는 파인다이닝의 에이스 요리사 전용 표현입니다."),
                    ("Here is the dish, take it to the table.", "여기 요리 나왔으니 테이블로 가져가세요.", "wrong_konglish", "주방의 위계질서를 무시하고 홀 매니저에게 명령조로 들릴 수 있습니다."),
                    ("I am finished now, you can check it.", "이제 다 끝났으니 확인해보셔도 됩니다.", "mediocre", "다소 느슨하고 프로페셔널한 긴장감이 떨어집니다.")
                ]
            },
            {
                "dialogue": "The inspector just cleaned the plate. Not a crumb left. Good recovery on the line tonight.",
                "korean": "평가원이 접시를 싹 비웠더군. 부스러기 하나 안 남기고 말이야. 오늘 라인 복구 훌륭했어.",
                "hint": "평가원이 접시를 싹 비웠다며 셰프가 위기 대처 능력을 인정한다.",
                "choices": [
                    ("Standard never drops on my watch. Prep begins at five tomorrow, chef.", "제가 맡은 라인에선 기준이 무너지지 않습니다. 내일 프랩은 새벽 5시 시작입니다, 셰프.", "native_killer", "'Standard never drops on my watch'는 'The Bear'를 연상시키는 압도적인 장인정신 표현입니다."),
                    ("Thank you, can I leave early tonight?", "감사합니다, 오늘 좀 일찍 퇴근해도 될까요?", "wrong_konglish", "칭찬 직후 조기 퇴근을 요구하는 것은 주방 문화에서 감점 요인입니다."),
                    ("I am very happy that he liked it.", "그분이 좋아하셨다니 저도 참 기쁩니다.", "mediocre", "단순한 기쁨 표출로 프로 셰프의 단단함이 부족합니다.")
                ]
            }
        ],
        "key_expr": "On my watch / Plated and pristine",
        "key_note": "'On my watch'는 내가 책임지는 동안에, 'Pristine'은 흠잡을 데 없이 완벽한 상태를 뜻합니다."
    },
    {
        "ep_num": 11,
        "title": "랭글리 CIA 본부: 모스크바 망명자의 비밀 접선",
        "genre": "Espionage",
        "speaker": "Station Chief Carrie (CIA Langley)",
        "emoji": "🕵️",
        "synopsis": "버지니아주 랭글리 CIA 본부 특수작전실. 모스크바 고위 장교 출신 망명자가 미 대사관에 접촉해 왔으나 이중간첩 함정 가능성이 제기된다.",
        "turns": [
            {
                "dialogue": "The defector claims he has Kremlin cipher keys, but his dead-drop timing matches FSB counter-intel doctrine. Do we exfiltrate him or burn the asset?",
                "korean": "망명자가 크렘린 암호키를 쥐고 있다고 주장하지만, 접선 타이밍이 러시아 연방보안국(FSB)의 역정보 공작 패턴과 일치해. 탈출 작전을 감행할 텐가, 자산을 폐기할 텐가?",
                "hint": "망명자가 진짜인지 함정인지 판단하고 구출할지 폐기할지 결단을 묻는다.",
                "choices": [
                    ("Run a blind verification protocol through our Vienna station before committing any ground assets.", "지상 요원을 투입하기 전에 비엔나 지부를 통해 교차 블라인드 검증 프로토콜을 즉각 가동하십시오.", "native_killer", "'blind verification protocol'과 'ground assets'는 'Homeland' 스타일의 첩보 전문 용어입니다."),
                    ("Just bring him here and ask him questions.", "그냥 여기로 데려와서 질문해보면 됩니다.", "wrong_konglish", "적의 간첩을 본진으로 바로 들여보내는 치명적인 보안 위반입니다."),
                    ("We can trust him because he looked very scared.", "그가 매우 무서워 보였으니 믿어도 될 것 같습니다.", "mediocre", "주관적 감정에 의존하는 것은 정보 분석관의 실격 사유입니다.")
                ]
            },
            {
                "dialogue": "Vienna confirmed his handler was executed forty-eight hours ago. He's running for his life with a twenty-minute extraction window in Prague. Your call.",
                "korean": "비엔나에서 그의 직속 상관이 48시간 전 처형된 것을 확인했어. 그는 목숨을 걸고 도주 중이며 프라하에서 탈출 윈도우는 딱 20분 남았어. 자네 결정은?",
                "hint": "상관이 처형된 진짜 망명자로 확인되어 프라하 20분 탈출 작전을 승인할지 묻는다.",
                "choices": [
                    ("Greenlight the tactical team. Scrub all digital footprints and escort him across the Austrian border.", "전술팀에 그린라이트를 발령하십시오. 모든 디지털 흔적을 지우고 오스트리아 국경 너머로 에스코트하십시오.", "native_killer", "'Greenlight the tactical team'과 'Scrub digital footprints'는 박진감 넘치는 첩보 킬러 대사입니다."),
                    ("Tell him to take a normal train to Vienna.", "오스트리아로 가는 일반 기차를 타라고 그에게 전하세요.", "wrong_konglish", "추적당하는 망명자에게 대중교통을 타라는 것은 사형선고나 다름없습니다."),
                    ("I hope the mission goes well without accidents.", "사고 없이 작전이 잘 진행되길 바랍니다.", "mediocre", "명령권자로서 구체적인 전술 지시가 결여되어 있습니다.")
                ]
            },
            {
                "dialogue": "Asset is secured in our safehouse. Flash drive contains full naval nuclear coordinates. Outstanding tradecraft, officer.",
                "korean": "망명자 자산이 우리 안전가옥에 무사히 확보됐어. USB에는 해군 핵잠수함 전수 좌표가 담겨 있더군. 흠잡을 데 없는 공작술이었네, 요원.",
                "hint": "망명자 구출과 기밀 확보에 성공하자 지부장이 탁월한 공작술이었다고 치하한다.",
                "choices": [
                    ("Lock down the perimeter and transport the asset under diplomatic pouch protocol immediately.", "외곽 경계를 폐쇄하고 외교행낭 프로토콜에 따라 해당 자산을 즉시 본국으로 압송하십시오.", "native_killer", "'Lock down the perimeter'와 'diplomatic pouch protocol'은 최고 수준의 첩보 마무리 용어입니다."),
                    ("Great job everyone, let's go drink beer.", "모두 수고하셨습니다, 맥주나 마시러 갑시다.", "wrong_konglish", "국가 기밀 취급 현장에서 프로답지 못한 경솔한 발언입니다."),
                    ("I am glad that we succeeded in this difficult mission.", "이 어려운 미션을 성공해서 기쁩니다.", "mediocre", "단순 감상으로 긴장감 넘치는 요원의 단단함이 부족합니다.")
                ]
            }
        ],
        "key_expr": "Greenlight the team / Tradecraft",
        "key_note": "'Greenlight'는 공식 작전 승인, 'Tradecraft'는 정보기관 특유의 고도 공작 기술을 뜻합니다."
    },
    {
        "ep_num": 12,
        "title": "3만 피트 상공 비상: 콕핏 엔진 화재의 결단",
        "genre": "Aviation",
        "speaker": "Captain Sully (Senior Flight Captain)",
        "emoji": "✈️",
        "synopsis": "보스턴발 LA행 보잉 777 여객기 3만 피트 상공. 2번 엔진 폭발 화재 경보가 울리고 객실 여압이 급강하하며 280명의 승객의 목숨이 기장과 당신(부기장)의 15초 판단에 걸린다.",
        "turns": [
            {
                "dialogue": "Engine two fire handle illuminated! Dual hydraulic pressure dropping fast. Do we dump fuel and divert to Denver, or declare emergency and glide to nearest runway?",
                "korean": "2번 엔진 화재 경고등 점등! 듀얼 유압 압력이 급격히 떨어지고 있어. 연료를 방출하고 덴버로 우회할 텐가, 아니면 비상사태를 선포하고 최단거리 활주로로 활강할 텐가?",
                "hint": "기장이 유압 상실 위기에서 연료 방출 우회와 최단거리 활강 비상착륙 중 판단을 요구한다.",
                "choices": [
                    ("Declare Mayday now, initiate immediate descent checklist, and vector to runway three-zero left.", "지금 즉시 메이데이 선포하고 긴급 강하 체크리스트 가동 후 활주로 30 좌측으로 진입각 유도하십시오.", "native_killer", "'Declare Mayday', 'vector to runway'는 'Sully' 영화의 실전 콕핏 교신 전문 어휘입니다."),
                    ("Please don't panic, let us check the manual slowly.", "당황하지 마시고 천천히 매뉴얼을 찾아봅시다.", "wrong_konglish", "엔진 화재 상황에서 천천히 매뉴얼을 찾으면 공중 폭발 위험이 커집니다."),
                    ("I think we should land the airplane right away.", "당장 비행기를 착륙시켜야 한다고 생각합니다.", "mediocre", "의미는 통하나 콕핏의 표준 관제 용어가 아닙니다.")
                ]
            },
            {
                "dialogue": "Crosswinds at thirty-five knots on final approach and thrust is asymmetrical. Can you hold the centerline with manual rudder?",
                "korean": "최종 진입 구간에 35노트 측풍이 불고 있고 추력이 비대칭이야. 수동 러더 조작으로 활주로 중앙선을 유지할 수 있겠나?",
                "hint": "강한 측풍과 비대칭 추력 속에서 수동 조종으로 활주로를 지킬 수 있는지 기장이 묻는다.",
                "choices": [
                    ("On the controls, captain. Applying left cross-rudder; I will keep us glued to the centerline.", "조종간 잡았습니다, 기장님. 좌측 크로스 러더 적용해 활주로 중앙선에 칼같이 정렬시키겠습니다.", "native_killer", "'On the controls'와 'glued to the centerline'은 파일럿 특유의 압도적인 조종 신뢰감 표현입니다."),
                    ("I am not sure, it looks very scary outside.", "잘 모르겠습니다, 밖이 너무 무서워 보입니다.", "wrong_konglish", "기장 앞에서 공포를 드러내면 콕핏 통제권이 즉시 박탈됩니다."),
                    ("I will try my best to steer the plane straight.", "비행기를 똑바로 조종하도록 최선을 다하겠습니다.", "mediocre", "성실하나 항공 전문 조작 용어가 결여되어 있습니다.")
                ]
            },
            {
                "dialogue": "Main gear touched down smooth! Reverse thruster deployed, fire suppression foam standing by. Outstanding airmanship, first officer.",
                "korean": "메인 기어 부드럽게 접지 완료! 역추진 장치 전개, 소방 폼차 대기 중. 흠잡을 데 없는 비행 기량이었네, 부기장.",
                "hint": "기적적인 비상 착륙에 성공하자 기장이 탁월한 비행 기량(airmanship)에 경의를 표한다.",
                "choices": [
                    ("Engaging evacuation slides and clearing all two hundred eighty souls safely off the tarmac, sir.", "비상 탈출 슬라이드 전개하여 280명 승객 전원을 활주로 밖으로 안전하게 대피시키겠습니다, 기장님.", "native_killer", "'evacuation slides'와 'clearing all souls'는 안전 책임자의 완벽한 프로페셔널 마무리 대사입니다."),
                    ("We survived! God bless America!", "우리가 살아남았습니다! 신이여 미국을 축복하소서!", "wrong_konglish", "승객 대피가 남은 상황에서 환호성만 지르는 아마추어적 태도입니다."),
                    ("Thank you captain, good job to you too.", "감사합니다 기장님, 기장님도 수고하셨습니다.", "mediocre", "무난하지만 항공 비상 사후 프로토콜 실행이 빠져 있습니다.")
                ]
            }
        ],
        "key_expr": "Declare Mayday / Airmanship",
        "key_note": "'Declare Mayday'는 국제 표준 항공 비상 선포, 'Airmanship'은 조종사의 종합적인 전문 비행 기량을 뜻합니다."
    },
    {
        "ep_num": 13,
        "title": "메이저리그 FA 마감 5분 전: 3억 달러 초대형 계약",
        "genre": "Sports Management",
        "speaker": "Jerry Maguire (Super Agent)",
        "emoji": "🏈",
        "synopsis": "뉴욕 힐튼 호텔 프라이빗 스위트. 자정 FA 마감 5분을 앞두고 양키스와 다저스 단장이 사이영상 수상 특급 에이스 투수를 두고 3억 달러 비딩 전쟁을 벌인다.",
        "turns": [
            {
                "dialogue": "Yankees just offered eight years at two hundred eighty million with deferred money. Dodgers are offering seven at three hundred, fully guaranteed. Which contract protects our client?",
                "korean": "양키스가 지급 유예 조건으로 8년 2억 8천만을 제시했어. 다저스는 7년 3억 전액 보장이야. 어느 계약이 우리 선수를 지키는 딜인가?",
                "hint": "양키스의 장기 분할 지급과 다저스의 고액 전액 보장 중 선수를 위한 최적 계약을 선택해야 한다.",
                "choices": [
                    ("Take the Dodgers' fully guaranteed deal and demand a full no-trade clause with opt-out after year four.", "다저스의 전액 보장 계약을 택하고, 전 구단 트레이드 거부권과 4년 차 옵트아웃 조항을 추가 요구하십시오.", "native_killer", "'fully guaranteed deal', 'no-trade clause', 'opt-out'은 스포츠 에이전시의 3대 핵심 협상 카드입니다."),
                    ("We should ask for more money from both teams until midnight.", "자정까지 두 팀 모두에게 돈을 더 달라고 떼를 써봅시다.", "wrong_konglish", "시장 가치를 벗어난 무리한 요구는 두 팀 모두 테이블을 떠나게 만듭니다."),
                    ("Eight years is longer, so Yankees deal is better.", "8년이 더 기니까 양키스 제안이 더 좋아 보입니다.", "mediocre", "지급 유예(deferred)의 인플레이션 손실을 계산하지 못한 초보적 분석입니다.")
                ]
            },
            {
                "dialogue": "Dodgers GM says the opt-out is a dealbreaker. He gives us two minutes to sign or he pivots to the free-agent closer. Do we hold the line?",
                "korean": "다저스 단장이 옵트아웃은 절대 불가하대. 2분 안에 서명 안 하면 다른 FA 마무리 투수로 틀겠다고 배짱을 튕기고 있어. 버틸 텐가?",
                "hint": "단장이 옵트아웃 거부 블러핑을 치며 2분 카운트다운을 시작할 때 배짱으로 맞서야 한다.",
                "choices": [
                    ("Hold firm. He needs a playoff ace more than we need their cap space; call his bluff on speaker.", "스탠스 유지하십시오. 샐러리캡보다 가을야구 에이스가 절실한 건 저쪽입니다. 스피커폰으로 블러핑을 꺾으시죠.", "native_killer", "'Hold firm'과 'call his bluff'는 'Moneyball'과 'Jerry Maguire' 속 탑티어 에이전트의 시그니처 배짱입니다."),
                    ("We must remove the opt-out immediately so they don't leave.", "그들이 떠나지 않도록 옵트아웃 조항을 즉시 빼줘야 합니다.", "wrong_konglish", "상대의 첫 번째 압박에 굴복해 고객의 미래 가치를 날려버리는 패착입니다."),
                    ("Let's ask him politely for one more hour.", "정중하게 1시간만 더 달라고 부탁해봅시다.", "mediocre", "마감 직전 시간 끌기는 협상력을 급격히 약화시킵니다.")
                ]
            },
            {
                "dialogue": "He folded! Seven years, three hundred ten million, full no-trade, and year-four opt-out. We just broke the league record, partner!",
                "korean": "저쪽이 접었어! 7년 3억 1천만 달러, 전 구단 트레이드 거부권, 4년 차 옵트아웃 전부 승인됐네. 우리가 리그 신기록을 썼어, 파트너!",
                "hint": "협상에 완승을 거두고 리그 역대 최고액 신기록을 경신하자 파트너가 격하게 환호한다.",
                "choices": [
                    ("Draft the press release and notify the player's family. Tomorrow we show them the money!", "즉시 공식 보도자료 배포하고 선수 가족에게 알리십시오. 내일 세상에 진짜 가치를 증명합니다!", "native_killer", "'Jerry Maguire'의 전설적인 명대사 'Show me the money'를 고급스럽게 오마주한 최고의 승리 선언입니다."),
                    ("I am tired now, I will sleep first.", "이제 피곤하니 잠부터 자겠습니다.", "wrong_konglish", "역대급 딜 성사 직후 홍보와 언론 프레임을 놓치는 미숙한 반응입니다."),
                    ("That is a lot of money, thank you partner.", "정말 큰돈이네요, 감사합니다 파트너님.", "mediocre", "평범한 감사 인사로 승리의 카타르시스가 부족합니다.")
                ]
            }
        ],
        "key_expr": "Fully guaranteed / Call his bluff",
        "key_note": "'Fully guaranteed'는 전액 보장 계약, 'Call someone's bluff'는 상대의 허세를 꿰뚫고 맞받아치다를 뜻합니다."
    },
    {
        "ep_num": 14,
        "title": "파리 패션위크 백스테이지: 런웨이 드레스 파손 위기",
        "genre": "Haute Couture",
        "speaker": "Miranda Priestly (Vogue Editor-in-Chief)",
        "emoji": "👗",
        "synopsis": "파리 그랑 팔레 백스테이지. 오프닝 피날레 드레스의 실크 솔기가 찢어지며 패션계 거물 미란다 프리슬리가 얼음장 같은 눈빛으로 당신을 응시한다.",
        "turns": [
            {
                "dialogue": "The headliner dress is shredded thirty seconds before the overture. Tell me why I shouldn't replace your entire collection with Saint Laurent right now.",
                "korean": "오버추어 음악 시작 30초 전에 피날레 드레스 솔기가 찢어졌어. 지금 당장 네 컬렉션 전체를 생로랑으로 교체하지 말아야 할 이유를 대봐.",
                "hint": "편집장이 컬렉션 전체를 취소하겠다고 서늘하게 압박하며 이유를 묻는다.",
                "choices": [
                    ("We restructure the silhouette with raw deconstructed draping; it turns an accident into avant-garde genius.", "손상된 실크를 해체주의 드레이핑으로 재구조화하겠습니다. 단순한 사고가 아방가르드한 걸작으로 승화될 겁니다.", "native_killer", "'The Devil Wears Prada' 특유의 패션 감각과 위기 전환 능력을 보여주는 킬러 표현입니다."),
                    ("It was not my fault, the model was walking too fast.", "제 잘못이 아닙니다, 모델이 너무 빨리 걸어서 그렇습니다.", "wrong_konglish", "남 탓을 하는 것은 패션계 거물 앞에서 즉각 퇴출 사유입니다."),
                    ("I will try to sew it quickly with thread.", "실과 바늘로 빨리 꿰매보도록 하겠습니다.", "mediocre", "오트쿠튀르 무대의 품격에 맞지 않는 밋밋한 반응입니다.")
                ]
            },
            {
                "dialogue": "Avant-garde? If the buyers don't understand the vision, the showroom cancels six million in advance orders. Are you banking your career on this silhouette?",
                "korean": "아방가르드? 바이어들이 그 의도를 이해하지 못하면 쇼룸은 6백만 달러 선주문을 취소할 거야. 이 실루엣에 네 커리어를 걸 수 있겠어?",
                "hint": "수백만 달러 주문 취소 위험을 들며 자신의 커리어를 걸 수 있는지 묻는다.",
                "choices": [
                    ("Every stitch. Haute couture isn't about safety; it's about defining what the world wears tomorrow.", "한 땀 한 땀 전부 걸겠습니다. 오트쿠튀르는 안전함이 아닌, 내일 온 세상이 입을 유행을 정의하는 예술입니다.", "native_killer", "'Defining what the world wears tomorrow'는 미란다의 심미안을 완벽히 만족시키는 전설적 멘트입니다."),
                    ("If you think so, we can cancel the show.", "편집장님이 그렇게 생각하신다면 쇼를 취소해도 됩니다.", "wrong_konglish", "자신감 부족으로 프로 디자이너로서의 자격을 상실합니다."),
                    ("I think buyers will like it because it is pretty.", "예쁘니까 바이어들도 좋아할 것이라 생각합니다.", "mediocre", "설득력이 결여된 아마추어적 평가입니다.")
                ]
            },
            {
                "dialogue": "That was not entirely uninspired. The French press is already calling it a triumph. That's all.",
                "korean": "완전히 영감이 없진 않았어. 프랑스 언론들이 이미 위대한 승리라고 부르고 있더군. 이상이야.",
                "hint": "미란다 프리슬리가 그녀 특유의 극찬('That's all')을 남기며 컬렉션의 성공을 인정한다.",
                "choices": [
                    ("Honored, Miranda. The spring lookbook will be on your desk before Milan fashion week.", "영광입니다, 미란다. 밀라노 패션위크 전에 봄 룩북을 책상 위에 올려놓겠습니다.", "native_killer", "최고의 찬사를 담담하고 프로페셔널하게 받아넘기는 완벽한 어시스턴트 마무리입니다."),
                    ("Thank you so much! You are my hero!", "정말 감사합니다! 당신은 저의 영웅입니다!", "wrong_konglish", "과도한 아첨은 미란다의 냉소를 부릅니다."),
                    ("I am glad that French people liked my clothes.", "프랑스 사람들이 제 옷을 좋아해 주어서 다행입니다.", "mediocre", "패션 디렉터로서의 카리스마가 부족합니다.")
                ]
            }
        ],
        "key_expr": "Haute couture / That's all",
        "key_note": "'Haute couture'는 최고급 맞춤 패션, 'That's all'은 미란다 프리슬리의 시그니처 종결 표현입니다."
    },
    {
        "ep_num": 15,
        "title": "글로벌 제약사 리콜 사태: CEO 긴급 기자회견 리허설",
        "genre": "Crisis PR",
        "speaker": "Olivia Pope (Managing Crisis Director)",
        "emoji": "🎙️",
        "synopsis": "워싱턴 D.C. 위기관리 컨설팅 룸. 신약 부작용 사망 사건으로 주가가 40% 폭락한 포춘 100대 제약사 CEO에게 긴급 생방송 기자회견 직전의 스탠스를 훈련시킨다.",
        "turns": [
            {
                "dialogue": "The New York Times is leading with a leaked memo showing your safety chief flagged liver toxicity six months ago. How do you face the press in ten minutes?",
                "korean": "뉴욕타임스가 당신네 안전책임자가 6개월 전 간 독성을 경고했던 내부 유출 메모를 1면에 실었소. 10분 뒤에 기자들을 어떻게 대면할 거요?",
                "hint": "치명적인 내부 고발 메모 유출 앞에서 언론을 어떻게 상대할지 묻는다.",
                "choices": [
                    ("Take immediate moral ownership, announce a voluntary global recall, and pledge a fifty-million-dollar victims' fund.", "도덕적 책임을 즉각 인정하고, 전 세계 자발적 전량 리콜을 발표하며, 5천만 달러의 피해자 기금을 서약하십시오.", "native_killer", "'Take moral ownership', 'voluntary global recall'은 위기관리 PR의 바이블 같은 정석 대응입니다."),
                    ("Deny the memo and say the reporter is a liar.", "메모를 전면 부인하고 기자가 거짓말쟁이라고 말합시다.", "wrong_konglish", "은폐와 언론 공격은 회사를 즉각 파멸로 이끕니다."),
                    ("Say that we are investigating the facts calmly.", "차분하게 사실관계를 조사 중이라고 말합시다.", "mediocre", "사망자가 발생한 상황에서 지나치게 안이하고 미온적인 태도입니다.")
                ]
            },
            {
                "dialogue": "If you recall, our quarterly cash flow goes negative and the board will demand your resignation by market close. Are you prepared to step down?",
                "korean": "리콜을 단행하면 분기 현금흐름이 마이너스로 돌아서고 이사회는 장 마감 전까지 당신의 사임을 요구할 거요. 물러날 준비가 되었소?",
                "hint": "이사회 사임 압박과 현금흐름 악화 속에서도 원칙을 지킬 수 있는지 묻는다.",
                "choices": [
                    ("My reputation and human lives come before my title. Integrity is the only asset that restores market valuation.", "제 직함보다 사람 목숨과 기업의 평판이 먼저입니다. 진정성만이 시장의 신뢰를 되살릴 유일한 자산입니다.", "native_killer", "'Scandal'의 올리비아 포프를 전율케 하는 진정한 리더십과 가치관의 발현입니다."),
                    ("I want to keep my job no matter what happens.", "무슨 일이 있어도 제 일자리는 지키고 싶습니다.", "wrong_konglish", "자신의 안위만 챙기는 태도로 위기관리 전문가의 신뢰를 완전히 잃습니다."),
                    ("Can we ask the board to give me more time?", "이사회에 시간을 좀 더 달라고 부탁할 수 있을까요?", "mediocre", "수동적이고 우유부단하여 리더의 단호함이 결여되어 있습니다.")
                ]
            },
            {
                "dialogue": "Spoken like a true statesman. Deliver those words with that exact conviction, and we will win the courtroom of public opinion.",
                "korean": "진정한 지도자다운 답변이오. 그 확신 그대로 단상에서 발화한다면, 우리는 여론의 법정에서 반드시 승리할 거요.",
                "hint": "위기관리 전문가가 태도에 경의를 표하며 단상으로 나갈 것을 독려한다.",
                "choices": [
                    ("The cameras are live. Let's walk out together and set the record straight.", "생방송 카메라 켜졌습니다. 함께 걸어나가 진실을 바로잡고 신뢰를 회복합시다.", "native_killer", "'Set the record straight'는 왜곡된 사실을 바로잡을 때 쓰는 가장 품격 있는 영어 관용구입니다."),
                    ("I am very nervous, please hold my hand.", "너무 긴장되니 제 손 좀 잡아주세요.", "wrong_konglish", "국가적 기자회견 직전 CEO의 위엄을 깎아내리는 유약한 태도입니다."),
                    ("Thank you Olivia, I will go talk to reporters now.", "감사합니다 올리비아, 이제 기자들에게 말하러 가겠습니다.", "mediocre", "평이한 마무리로 긴장감 넘치는 결연함이 아쉽습니다.")
                ]
            }
        ],
        "key_expr": "Set the record straight / Moral ownership",
        "key_note": "'Set the record straight'는 오해나 왜곡을 바로잡다, 'Moral ownership'은 도덕적 책임을 통감하다를 뜻합니다."
    },
    {
        "ep_num": 16,
        "title": "맨해튼 억만장자 거리: 1억 달러 펜트하우스 비딩 전쟁",
        "genre": "Luxury Real Estate",
        "speaker": "Ryan Serhant (Managing Real Estate Broker)",
        "emoji": "🏙️",
        "synopsis": "맨해튼 57번가 초호화 빌리어네어스 로우 90층 펜트하우스. 1억 2천만 달러 올캐시 매수 희망자와 헤지펀드 거물이 동시 입찰에 뛰어들며 마감 10분 전 중개인의 최종 결단을 요구한다.",
        "turns": [
            {
                "dialogue": "We have two competing offers on the table: an all-cash wire from a European family office at ninety million, and a leveraged ninety-five from a tech titan. Which buyer do we present to the seller?",
                "korean": "테이블 위에 두 개의 입찰이 올라왔습니다. 유럽 패밀리 오피스의 9천만 달러 전액 현금 송금과 테크 거물의 레버리지 9천 5백만 달러 제안입니다. 매도인에게 어느 쪽을 올리시겠습니까?",
                "hint": "확실한 전액 현금 9천만 달러와 대출 조건부 9천 5백만 달러 중 매도인의 이익을 극대화할 전략을 선택한다.",
                "choices": [
                    ("Leverage the tech bid to force the European office into a non-contingent bidding war above one hundred million.", "테크 거물의 입찰가를 지렛대 삼아 유럽 오피스를 1억 달러 이상의 무조건부 비딩 전쟁으로 몰아넣으십시오.", "native_killer", "'non-contingent bidding war'는 맨해튼 하이엔드 부동산 중개업계의 최상급 수익 극대화 스킬입니다."),
                    ("Take the lower money because cash is always simple.", "현금이 항상 단순하니까 그냥 더 적은 돈을 받읍시다.", "wrong_konglish", "매도인에게 천만 달러 이상의 추가 마진을 안겨줄 협상 기회를 날려버립니다."),
                    ("Wait until next month to see if new buyers come.", "다음 달까지 새 구매자가 오는지 기다려봅시다.", "mediocre", "하이엔드 시장의 입찰 모멘텀을 죽이는 소극적 대처입니다.")
                ]
            },
            {
                "dialogue": "The European buyer refuses to budge past ninety-five, and the tech CEO wants an exclusive forty-eight-hour inspection contingency. How do we close the gap?",
                "korean": "유럽 매수인은 9천 5백만 달러에서 한 푼도 못 올리겠다고 버티고, 테크 CEO는 48시간 독점 실사 조건을 요구합니다. 격차를 어떻게 좁히겠습니까?",
                "hint": "두 매수인의 조건이 팽팽히 맞설 때 매도인을 완벽히 보호하는 계약 조건을 설계해야 한다.",
                "choices": [
                    ("Require a non-refundable ten percent hard deposit with a twenty-four-hour signing window, winner takes all.", "24시간 서명 기한과 함께 10%의 환불 불가 보증금을 요구해 승자독식으로 몰아붙이십시오.", "native_killer", "'non-refundable hard deposit'과 'winner takes all'은 럭셔리 부동산 브로커의 칼날 같은 승부수입니다."),
                    ("Give both buyers whatever discounts they ask for.", "두 매수인 모두에게 그들이 원하는 할인을 다 해줍시다.", "wrong_konglish", "수수료와 매도인의 자산 가치를 동시에 깎아먹는 최악의 판단입니다."),
                    ("Ask the seller to lower the price to be friendly.", "매도인에게 친절하게 가격을 깎아달라고 부탁합시다.", "mediocre", "고객의 대리인으로서 자격 미달인 굴종적인 태도입니다.")
                ]
            },
            {
                "dialogue": "Wire cleared! One hundred two million, zero contingencies, record price per square foot in Midtown history. You just orchestrated the deal of the decade.",
                "korean": "송금 완료 확인! 1억 2백만 달러, 무조건부 계약, 미드타운 역사상 평당 최고가 신기록입니다. 자네가 방금 10년 만의 최고의 딜을 성사시켰네.",
                "hint": "역대 최고가 기록을 경신하며 계약이 완결되자 파트너가 격찬을 보낸다.",
                "choices": [
                    ("Commission banked. Prepare the champagne and get the penthouse keys to the penthouse suite.", "수수료 입금 완료. 샴페인을 준비하고 펜트하우스 스위트 열쇠를 새 주인에게 전달합시다.", "native_killer", "'Commission banked'는 성공한 럭셔리 브로커의 당당하고 세련된 자축 인사입니다."),
                    ("I am shocked, I did not know it would sell.", "저도 깜짝 놀랐습니다, 팔릴 줄 몰랐어요.", "wrong_konglish", "자신의 능력을 깎아내리고 우연에 기대는 아마추어적인 발언입니다."),
                    ("Thank you Ryan, real estate is quite fun.", "감사합니다 라이언, 부동산은 참 재미있네요.", "mediocre", "밋밋한 소감으로 역사적 성취감의 깊이가 느껴지지 않습니다.")
                ]
            }
        ],
        "key_expr": "Hard deposit / Non-contingent",
        "key_note": "'Hard deposit'은 계약 파기 시 반환되지 않는 보증금, 'Non-contingent'는 단서 조건 없는 완결 계약을 뜻합니다."
    },
    {
        "ep_num": 17,
        "title": "비벌리힐스 에이전시: 오스카 캠페인 vs 3천만 불 블록버스터",
        "genre": "Hollywood Agency",
        "speaker": "Ari Gold (Top Hollywood Talent Agent)",
        "emoji": "🎬",
        "synopsis": "비벌리힐스 최고 연예 기획사 대표실. 오스카 노미네이트가 유력한 주연 배우에게 마블 스튜디오의 3천만 달러 3부작 계약과 명장 감독의 저예산 예술 영화 중 진로 결단을 압박한다.",
        "turns": [
            {
                "dialogue": "Marvel is offering thirty million upfront for a three-picture superhero franchise, but Nolan wants you for an indie drama that shoots in two weeks with zero backend. Which script are you signing?",
                "korean": "마블에서 3편 프랜차이즈에 계약금 3천만 달러를 불렀는데, 놀란 감독은 러닝개런티 전혀 없는 2주 뒤 크랭크인 저예산 드라마에 널 캐스팅하고 싶어 해. 어느 대본에 사인할 거야?",
                "hint": "막대한 상업적 부와 거장 감독과의 오스카 도전 중 배우의 장기적 커리어를 극대화할 전략을 제시한다.",
                "choices": [
                    ("We take Nolan for critical prestige, then leverage that Oscar buzz to renegotiate Marvel's franchise rate to forty million.", "놀란의 작품으로 평단의 극찬과 오스카를 챙기고, 그 오스카 열풍을 지렛대 삼아 마블 계약금을 4천만 달러로 재협상합니다.", "native_killer", "할리우드 탑 에이전트들이 사용하는 'Prestige first, cash in next'의 교과서적인 윈-윈 전략입니다."),
                    ("Just take the money, acting awards are useless anyway.", "그냥 돈이나 받으세요, 연기상 같은 건 어차피 쓸모없습니다.", "wrong_konglish", "배우의 예술적 야망을 짓밟고 에이전트와 배우의 관계를 파탄 냅니다."),
                    ("Let's do both films at the exact same time.", "두 영화를 완전히 같은 시기에 동시에 촬영합시다.", "mediocre", "스케줄 충돌로 두 프로덕션 모두에서 소송을 당할 수 있는 비현실적 대안입니다.")
                ]
            },
            {
                "dialogue": "Marvel says they won't wait for award season. They want your signature by 5 PM, or the role goes to Chalamet. Do we bluff, or do we blink?",
                "korean": "마블이 시상식 시즌까지 안 기다려준대. 오늘 오후 5시까지 서명 안 하면 역할 샬라메한테 넘어간단다. 블러핑 칠래, 아니면 꼬리 내릴래?",
                "hint": "제작사의 마감 압박과 라이벌 배우 대체 위협 앞에서 담대하게 응수한다.",
                "choices": [
                    ("Let them call Chalamet. His schedule is locked on Dune; Marvel's bluffing because our screen test blew the studio away.", "샬라메한테 연락해보라 하십시오. 걔 스케줄 듄에 묶여 있습니다. 우리 스크린 테스트가 압도적이었으니 저쪽의 허풍일 뿐입니다.", "native_killer", "상대의 카드와 업계 일정을 꿰뚫고 있는 탑티어 에이전트의 짜릿한 승부수입니다."),
                    ("I am scared! Please sign the Marvel paper right away!", "너무 무섭습니다! 제발 마블 서류에 지금 당장 사인해주세요!", "wrong_konglish", "상대의 위협에 패닉에 빠져 협상력을 바닥으로 떨어뜨립니다."),
                    ("Maybe we can ask them for a small extension?", "혹시 마블에 마감 연장을 정중히 요청해볼까요?", "mediocre", "단호한 결단력 없이 상대에게 끌려다니는 미온적 대응입니다.")
                ]
            },
            {
                "dialogue": "Boom! Marvel caved and pushed their principal photography to fit Nolan's shoot. You get the art and the bag. That's how we conquer this town!",
                "korean": "터졌다! 마블이 꼬리 내리고 놀란 스케줄에 맞춰 본촬영을 미루기로 했어. 예술과 돈 둘 다 거머쥔 거야. 이게 바로 이 바닥을 집어삼키는 법이지!",
                "hint": "두 편 모두 성사시키며 최고의 승리를 거둔 에이전트의 환호에 화답한다.",
                "choices": [
                    ("Book the studio screening room, Ari. We're taking Hollywood by storm, one masterpiece at a time.", "스튜디오 시사실 예약하시죠, 아리. 걸작 하나씩 찍으며 할리우드를 완전히 집어삼킬 차례입니다.", "native_killer", "'Entourage'의 아리 골드와 환상의 호흡을 맞추는 스타일리시하고 야망 넘치는 답변입니다."),
                    ("I am going home to take a nap now.", "전 이제 낮잠이나 자러 집에 가겠습니다.", "wrong_konglish", "할리우드 정점에 선 순간 분위기를 차갑게 식히는 무성의한 발언입니다."),
                    ("Thank you Ari, you are a very loud agent.", "감사합니다 아리, 참 목소리가 크신 에이전트군요.", "mediocre", "파트너십의 열정을 공유하지 못하는 어색한 코멘트입니다.")
                ]
            }
        ],
        "key_expr": "Take by storm / Leverage the buzz",
        "key_note": "'Take by storm'은 돌풍을 일으키며 장악하다, 'Leverage buzz'는 세간의 화제성을 협상 지렛대로 쓰다를 뜻합니다."
    },
    {
        "ep_num": 18,
        "title": "플라자 호텔 스위트: 외교 사절단 긴급 충돌",
        "genre": "5-Star Hotel",
        "speaker": "Monsieur Dupont (General Manager)",
        "emoji": "🏨",
        "synopsis": "센트럴파크 앞 전설적인 5성급 호텔 더 플라자. UN 총회 기간 국빈 방문 중인 중동 로열 패밀리와 미국 상원의원 일행 사이의 스위트룸 보안 충돌을 무마해야 한다.",
        "turns": [
            {
                "dialogue": "The Prime Minister's royal detail is demanding that we clear the entire presidential floor, but the Senior Senator from California refuses to vacate suite 1402. We have fifteen minutes before Secret Service intervenes.",
                "korean": "총리의 왕실 경호팀이 프레지덴셜 플로어 전 층 소개를 요구하고 있는데, 캘리포니아 중진 상원의원이 1402호 스위트 퇴거를 완강히 거부하고 있습니다. 비밀경호국이 개입하기까지 15분 남았습니다.",
                "hint": "외교적 특권과 자국 최고위 정치인의 자존심이 충돌할 때 우아한 외교적 해법을 모색한다.",
                "choices": [
                    ("Upgrade the Senator to the penthouse duplex with private elevator access, framed as an exclusive courtesy for his diplomatic seniority.", "상원의원을 단독 엘리베이터가 있는 펜트하우스 듀플렉스로 무료 업그레이드해드리고, 외교적 원로 예우 차원임을 정중히 브리핑하십시오.", "native_killer", "상대의 체면을 세워주면서 갈등을 즉시 해소하는 5성급 호텔 총지배인의 완벽한 기지입니다."),
                    ("Tell the royal guards to fight the Senator outside.", "왕실 경호원들에게 밖으로 나가 상원의원과 싸우라고 하십시오.", "wrong_konglish", "호텔을 외교적 참사의 전쟁터로 만드는 몰지각한 발언입니다."),
                    ("Call the police and kick everyone out of the lobby.", "경찰을 불러서 로비의 모든 사람을 쫓아냅시다.", "mediocre", "VIP 고객 전원을 적으로 돌리는 호텔리어로서의 자격 미달 행동입니다.")
                ]
            },
            {
                "dialogue": "The Senator agreed to the penthouse, but the Prince's advance team insists on installing their own surveillance jamming pods in the hallway, violating federal fire codes.",
                "korean": "상원의원은 펜트하우스로 옮기기로 동의했으나, 왕세자 선발대가 연방 소방법을 위반하며 복도에 자체 도청방지 전파방해기를 설치하겠다고 고집합니다.",
                "hint": "국제 외교 관례와 호텔 안전 법규 사이에서 타협 없는 보안 프로토콜을 관철한다.",
                "choices": [
                    ("Provide our certified military-grade encrypted routing suite and offer dedicated 24/7 Diplomatic Security Service oversight.", "호텔의 공인 군사등급 암호화 라우팅 스위트를 제공하고, 24시간 연방 외교안보국 전담 감독관 입회를 제안하십시오.", "native_killer", "법규 준수와 보안 요구를 모두 충족하는 정통 하이엔드 호텔 프로토콜 솔루션입니다."),
                    ("Just unplug their machines and run away.", "그냥 그들의 기계 플러그를 뽑고 도망치세요.", "wrong_konglish", "물리적 충돌과 즉각적인 외교 항의를 부르는 위험한 처신입니다."),
                    ("Ignore the fire code because they are very rich.", "그들이 엄청난 부자이니까 소방법을 무시합시다.", "mediocre", "화재 참사 시 법적 형사 책임을 져야 하는 무책임한 대처입니다.")
                ]
            },
            {
                "dialogue": "Both delegations are dining peacefully in the Grand Ballroom. The State Department just commended our discretion. Flawless hospitality under fire, colleague.",
                "korean": "양국 대표단 모두 그랜드 볼룸에서 평화롭게 만찬 중입니다. 국무부에서 우리 호텔의 신중한 기밀 유지와 대처에 감사를 표했습니다. 위기 속 완벽한 서비스였습니다, 동료여.",
                "hint": "외교 위기를 완벽하게 수습한 후 최고급 호텔리어의 품격으로 화답한다.",
                "choices": [
                    ("Discretion and grace are the hallmarks of The Plaza. Let us ensure their departure at dawn is equally seamless.", "신중함과 품격이야말로 플라자 호텔의 상징입니다. 새벽에 있을 귀국 의전까지 티끌 하나 없이 완벽하게 준비하겠습니다.", "native_killer", "세계 최고 럭셔리 호텔의 자부심과 프로페셔널리즘이 물씬 묻어나는 명대사입니다."),
                    ("I survived today, I want to quit this job.", "오늘 겨우 살아남았네요, 이 일 그만두고 싶습니다.", "wrong_konglish", "성공적인 수습 후 부정적 넋두리로 전문성을 깎아먹습니다."),
                    ("Thank you Monsieur Dupont, hotels are very stressful.", "감사합니다 뒤퐁 지배인님, 호텔 일은 정말 스트레스가 심하네요.", "mediocre", "일상적인 푸념으로 프로페셔널한 마무리가 아쉽습니다.")
                ]
            }
        ],
        "key_expr": "Hallmark of hospitality / Under fire",
        "key_note": "'Hallmark'는 최고의 품질을 보증하는 상징, 'Under fire'는 극심한 비난이나 압박을 받는 와중을 뜻합니다."
    },
    {
        "ep_num": 19,
        "title": "소더비 경매장: 1억 달러 레오나르도 다빈치 비공개 낙찰",
        "genre": "Fine Art Auction",
        "speaker": "Julian Vance (Senior Chief Auctioneer)",
        "emoji": "🎨",
        "synopsis": "소더비 뉴욕 본사 그랜드 갤러리. 500년간 실종되었던 르네상스 걸작 초상화가 출품되어 낙찰봉을 내리기 10초 전, 비밀 전화 입찰자와 객석의 수집가가 1억 달러 선에서 숨 막히는 호가 승부를 벌인다.",
        "turns": [
            {
                "dialogue": "The bid stands at ninety-eight million from the phone in Geneva. The gentleman in the third row is hesitating. Do we hammer the lot or coax the centenary record?",
                "korean": "제네바 전화 입찰에서 9천 8백만 달러를 불렀습니다. 3열의 신사분께서 망설이고 계십니다. 낙찰봉을 내리시겠습니까, 아니면 1억 달러 신기록을 유도하시겠습니까?",
                "hint": "9천 8백만 달러에서 낙찰봉을 내리기 직전, 역사적인 1억 달러 돌파를 위한 카리스마 있는 호가 유도를 주문한다.",
                "choices": [
                    ("Hold the gavel. Look him in the eye and remind the room that history does not come up for sale twice.", "낙찰봉을 잠시 멈추십시오. 그의 눈을 응시하며 역사는 두 번 다시 매물로 나오지 않는다는 점을 상기시키십시오.", "native_killer", "'History does not come up for sale twice'는 소더비·크리스티 수석 경매사들의 전설적인 클로징 멘트입니다."),
                    ("Bang the hammer fast so we can go home early.", "빨리 집에 갈 수 있게 낙찰봉을 당장 내려치세요.", "wrong_konglish", "수백만 달러의 경매 수수료와 역대급 기록을 스스로 걷어차는 경솔한 행위입니다."),
                    ("Shout at the gentleman to give us two more million.", "그 신사에게 2백만 달러만 더 내놓으라고 소리 지르세요.", "mediocre", "하이엔드 경매장의 품격을 완전히 무너뜨리는 천박한 방식입니다.")
                ]
            },
            {
                "dialogue": "He bit! One hundred million in the room! But Geneva is demanding a thirty-second pause to verify provenance documentation before countering. Can we grant the delay?",
                "korean": "넘어왔습니다! 객석에서 1억 달러 나왔습니다! 하지만 제네바 측에서 추가 호가 전 출처 검증 문서를 확인하겠다며 30초의 유예를 요구합니다. 유예를 허용할 수 있습니까?",
                "hint": "낙찰 열기가 식지 않도록 경매의 모멘텀을 유지하면서도 규정을 지킨다.",
                "choices": [
                    ("State firmly from the podium that provenance is fully certified by the Louvre curatorial board and ask for the final call.", "루브르 큐레이터 위원회가 출처를 공인했음을 단상에서 확언하고, 즉시 최종 호가를 진행하십시오.", "native_killer", "의구심을 단칼에 불식시키고 입찰자들의 긴장감을 최고조로 유지하는 명경매사의 결단입니다."),
                    ("Tell Geneva we don't know who painted this picture.", "제네바 쪽에 이 그림을 누가 그렸는지 우리도 모른다고 말하세요.", "wrong_konglish", "진품 논란을 스스로 자초하여 경매를 취소시키고 소송을 부르는 발언입니다."),
                    ("Wait five minutes in silence until Geneva is ready.", "제네바가 준비될 때까지 5분 동안 조용히 기다립시다.", "mediocre", "객석의 열기와 경쟁 심리를 차갑게 식혀버리는 미숙한 진행입니다.")
                ]
            },
            {
                "dialogue": "Fair warning... and sold for one hundred ten million dollars! The highest price for an Old Master in our house's two-hundred-year history!",
                "korean": "마지막 호가... 1억 1천만 달러에 낙찰되었습니다! 우리 경매소 200년 역사상 최고가 거장 걸작 기록입니다!",
                "hint": "역사적인 낙찰봉이 내려진 후 최고 경매 팀으로서 감격을 나눈다.",
                "choices": [
                    ("Down comes the gavel. Escort the buyer to the private vault for the provenance handover.", "낙찰봉이 떨어졌습니다. 매수인을 프라이빗 금고로 안내하여 진품 증서 이관 절차를 진행하십시오.", "native_killer", "'Down comes the gavel'은 경매의 결정적 승리를 선언하는 정통 클래식 표현입니다."),
                    ("Now I can buy a new car with my bonus!", "이제 보너스로 새 차를 살 수 있겠네요!", "wrong_konglish", "예술적 경외심과 고객 신뢰 대신 사리사욕을 드러내는 천박한 반응입니다."),
                    ("That was a good auction, I am satisfied.", "좋은 경매였습니다, 만족스럽네요.", "mediocre", "역대급 세계 신기록의 감격에 비해 지나치게 무미건조합니다.")
                ]
            }
        ],
        "key_expr": "Down comes the gavel / Fair warning",
        "key_note": "'Down comes the gavel'은 최종 낙찰봉이 내려치다, 'Fair warning'은 낙찰 직전 마지막 호가 경고를 뜻합니다."
    },
    {
        "ep_num": 20,
        "title": "워터게이트 지하 주차장: 한밤의 내부 고발자 접선",
        "genre": "Investigative Journalism",
        "speaker": "Deep Throat (Anonymous Senior Whistleblower)",
        "emoji": "📰",
        "synopsis": "새벽 2시 워싱턴 D.C. 외곽 지하 주차장. 거대 국방 군수기업의 전투기 결함 은폐 문서를 건네받으며 퓰리처상 탐사보도 기자의 목숨을 건 비밀 접선이 시작된다.",
        "turns": [
            {
                "dialogue": "You shouldn't have come. They tapped my phone lines this morning. The audit files inside this briefcase prove the Pentagon paid for defective flight control software.",
                "korean": "오지 말았어야 했소. 그자들이 오늘 아침 내 전화선을 도청했소. 이 서류 가방 안의 감사 파일들이 국방부가 결함투성이 비행 제어 소프트웨어 대금을 지불했다는 사실을 증명하오.",
                "hint": "생명의 위협을 느끼는 내부 고발자의 신뢰를 얻고 확실한 증거를 확보해야 한다.",
                "choices": [
                    ("Your courage will not be in vain. I will protect your identity under the First Amendment and cross-check every single serial number before printing.", "당신의 용기는 헛되지 않을 겁니다. 수정헌법 제1조에 따라 신원을 목숨 걸고 지킬 것이며, 보도 전 모든 일련번호를 교차 검증하겠습니다.", "native_killer", "'All the President's Men'과 'Spotlight' 속 정통 탐사보도 기자의 확고한 언론 윤리와 신뢰 형성 대사입니다."),
                    ("Give me the files quickly so I can post them on Twitter tonight.", "오늘 밤 트위터에 올릴 수 있게 서류나 빨리 넘기세요.", "wrong_konglish", "고발자의 신원을 위험에 빠뜨리고 확인되지 않은 지라시를 유포하는 사이비 언론 행태입니다."),
                    ("Are you sure this is not a fake paper?", "이거 가짜 서류 아닌 거 확실합니까?", "mediocre", "목숨 걸고 나온 고발자의 신뢰를 첫마디부터 꺾어버리는 무례한 질문입니다.")
                ]
            },
            {
                "dialogue": "The Department of Justice will file an emergency injunction at dawn to suppress your story under the Espionage Act. Can your paper withstand the pressure?",
                "korean": "법무부가 간첩법을 적용해 당신 기사의 보도를 금지하려고 새벽에 긴급 가처분 신청을 낼 거요. 당신 신문사가 그 압박을 견뎌낼 수 있겠소?",
                "hint": "국가 권력의 사전 검열 및 보도금지 가처분 압박에 맞서 헌법적 저널리즘 원칙을 천명한다.",
                "choices": [
                    ("Our publisher has seasoned constitutional litigators on retainer. We will publish on the front page and fight it all the way to the Supreme Court.", "우리 사주에겐 헌법 전문 베테랑 변호인단이 대기하고 있습니다. 1면에 당당히 싣고 연방 대법원까지 끝까지 싸울 겁니다.", "native_killer", "'The Post'의 캐서린 그레이엄 발행인을 연상시키는 위대한 언론 자유의 수호 선언입니다."),
                    ("If the government says no, we must stop writing immediately.", "정부가 안 된다고 하면 당장 기사 작성을 중단해야죠.", "wrong_konglish", "권력의 협박 앞에 무릎 꿇는 부끄러운 언론인의 굴복입니다."),
                    ("Maybe we can delete the sensitive names and make it gentle.", "민감한 이름들을 지우고 기사를 부드럽게 쓰면 어떨까요?", "mediocre", "진실을 희석하여 고발의 파급력을 무력화시키는 비겁한 타협입니다.")
                ]
            },
            {
                "dialogue": "Headlights! A black SUV just entered level B. Take the fire exit stairs and don't look back. Godspeed, reporter.",
                "korean": "헤드라이트 불빛이오! 검은 SUV가 지하 B층으로 진입했소. 비상계단으로 빠져나가고 절대 뒤돌아보지 마시오. 신의 가호가 있기를, 기자 양반.",
                "hint": "추격자가 들이닥친 일촉즉발의 탈출 순간에 마지막 인사를 나눈다.",
                "choices": [
                    ("Files secured. Stay low until the headlines hit the morning stands. The truth is going to break.", "서류 확보했습니다. 조간신문 1면에 헤드라인이 실릴 때까지 몸을 숨기십시오. 진실은 반드시 터져 나옵니다.", "native_killer", "긴박한 탈출 속에서도 취재원의 안전을 챙기며 진실의 힘을 믿는 최고의 마무리입니다."),
                    ("I am so scared of that black car, where is my mommy!", "저 검은 차가 너무 무서워요, 우리 엄마 어디 갔어!", "wrong_konglish", "목숨이 걸린 스릴러 상황을 우스꽝스럽게 망쳐버리는 유아적 대사입니다."),
                    ("Okay bye bye, see you next time.", "네 안녕히 가세요, 다음에 또 봐요.", "mediocre", "생사의 기로에 선 긴장감을 전혀 살리지 못한 가벼운 작별입니다.")
                ]
            }
        ],
        "key_expr": "Hit the morning stands / Stay low",
        "key_note": "'Hit the morning stands'는 아침 신문 가판대에 실려 배포되다, 'Stay low'는 위험이 가실 때까지 은신하다를 뜻합니다."
    }
]

print(f"Loaded {len(EPISODES_9_TO_100)} curated episodes.")

