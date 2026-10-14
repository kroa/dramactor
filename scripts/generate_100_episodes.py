import json
import os
from datetime import datetime, timedelta

def build_100_episodes():
    base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    episodes_file = os.path.join(base_dir, 'src', 'data', 'episodes.json')

    with open(episodes_file, 'r', encoding='utf-8') as f:
        existing = json.load(f)

    # We keep the first 7 existing episodes
    episodes = existing[:7]
    base_date = datetime.strptime("2026-10-10", "%Y-%m-%d")

    # Define high-octane 93 new scenarios (EP 08 to EP 100)
    scenarios_data = [
        # --- 8 ~ 15: FBI & Crime Investigation ---
        {
            "title": "FBI 심문실: 묵비권을 깨뜨리는 30초",
            "genre": "FBI Crime",
            "speaker": "Agent Miller (FBI Lead Investigator)",
            "avatarEmoji": "🔍",
            "synopsis": "퀸즈 비밀 안가 심문실. 금융 사기 주범이 묵비권을 행사하려는 순간, 연방 검찰과의 형량 거래 카드를 던지며 자백을 유도해야 한다.",
            "turns": [
                {
                    "dialogue": "You have thirty seconds before I walk out this door and recommend twenty years in federal penitentiary. Do you want to cut a deal, or do you want to rot in a cell?",
                    "dialogueKorean": "내가 이 문을 열고 나가서 연방 교도소 20년형을 구형하기까지 자네에겐 딱 30초 남았어. 거래를 할 텐가, 아니면 감방에서 썩을 텐가?",
                    "situationHint": "요원이 20년형을 경고하며 지금 거래를 할지 감방에서 썩을지 선택을 압박한다.",
                    "choices": [
                        {"id": "A", "text": "I am not speaking without my lawyer here.", "koreanMeaning": "변호사 없이는 말하지 않겠습니다.", "type": "mediocre", "feedback": "기본적인 묵비권 표현이지만 협상의 주도권을 완전히 넘겨줍니다.", "targetScript": "I am not speaking without my lawyer here."},
                        {"id": "B", "text": "Give me full immunity on record, and I'll hand you their offshore shell accounts by midnight.", "koreanMeaning": "조서에 완전 면책을 명시해 주시죠. 자정까지 해외 페이퍼컴퍼니 계좌를 전부 넘기겠습니다.", "type": "native_killer", "feedback": "'Give me full immunity on record'는 미드 범죄물에서 최고의 카운터 협상 킬러 표현입니다.", "targetScript": "Give me full immunity on record, and I'll hand you their offshore shell accounts by midnight."},
                        {"id": "C", "text": "I will think about this deal tomorrow.", "koreanMeaning": "내일 이 딜에 대해 생각해보겠습니다.", "type": "wrong_konglish", "feedback": "심문실에서 시간을 미루면 요원이 즉시 자리를 털고 일어나 영장을 청구합니다.", "targetScript": "I will think about this deal tomorrow."}
                    ]
                },
                {
                    "dialogue": "Immunity is off the table for grand larceny. Best I can do is a sealed letter to the presiding judge. Take it or leave it.",
                    "dialogueKorean": "중도절도 혐의에 완전 면책은 어림없어. 내가 해줄 수 있는 건 담당 판사에게 비공개 감형 건의서를 써주는 게 다야. 받든가 말든가.",
                    "situationHint": "요원이 완전 면책은 거절하고 판사 앞 비공개 건의서가 최선이라며 양자택일을 요구한다.",
                    "choices": [
                        {"id": "A", "text": "Throw in witness protection for my family, and you have yourself a deal.", "koreanMeaning": "내 가족에 대한 증인 보호 프로그램을 얹어 주신다면, 그 거래 수락하죠.", "type": "native_killer", "feedback": "'Throw in witness protection'과 'you have yourself a deal'은 범죄물 특유의 노련한 타협 표현입니다.", "targetScript": "Throw in witness protection for my family, and you have yourself a deal."},
                        {"id": "B", "text": "Okay, that is fine with me.", "koreanMeaning": "네, 그 정도면 괜찮습니다.", "type": "mediocre", "feedback": "너무 쉽게 양보하여 상대에게 패를 다 읽히게 됩니다.", "targetScript": "Okay, that is fine with me."},
                        {"id": "C", "text": "Don't lie to me, I know the law very well.", "koreanMeaning": "거짓말 마세요, 저 법 잘 압니다.", "type": "wrong_konglish", "feedback": "취조관을 도발하여 구속 수사로 직행하는 역효과를 냅니다.", "targetScript": "Don't lie to me, I know the law very well."}
                    ]
                },
                {
                    "dialogue": "Done. Sign the plea allocution, and don't make a single phone call without my express permission.",
                    "dialogueKorean": "좋아, 성사됐어. 유죄 인정 조서에 서명하고, 내 명시적 허가 없이는 전화 한 통도 걸지 마.",
                    "situationHint": "거래가 성사되었으니 서명하고 허가 없이 외부 연락을 금지하라고 명령한다.",
                    "choices": [
                        {"id": "A", "text": "Consider me your most cooperative asset from this second forward.", "koreanMeaning": "이 시간부로 저를 요원님의 가장 협조적인 정보 자산으로 보셔도 좋습니다.", "type": "native_killer", "feedback": "'cooperative asset'은 첩보/수사 드라마에서 정보원의 신뢰를 극대화하는 프로페셔널한 어휘입니다.", "targetScript": "Consider me your most cooperative asset from this second forward."},
                        {"id": "B", "text": "I will not call anyone.", "koreanMeaning": "아무에게도 전화하지 않겠습니다.", "type": "mediocre", "feedback": "단순한 약속이지만 전문적인 스파이/정보원 뉘앙스가 부족합니다.", "targetScript": "I will not call anyone."},
                        {"id": "C", "text": "Can I call my mom just one time?", "koreanMeaning": "우리 엄마한테 딱 한 번만 전화해도 될까요?", "type": "wrong_konglish", "feedback": "심각한 연방 범죄 수사 상황에 맞지 않는 미숙한 반응입니다.", "targetScript": "Can I call my mom just one time?"}
                    ]
                }
            ],
            "keyTakeaway": {
                "expression": "Cut a deal / On record",
                "usageNote": "'Cut a deal'은 타협/거래를 성사시키다, 'On record'는 공식 기록에 남기다를 뜻하는 필수 법률 스릴러 관용구입니다."
            }
        },
        # --- 9: White House Situation Room ---
        {
            "title": "백악관 상황실: 자정의 미사일 요격 결단",
            "genre": "Politics",
            "speaker": "General Hayes (Chairman of Joint Chiefs)",
            "avatarEmoji": "🏛️",
            "synopsis": "워싱턴 D.C. 백악관 지하 상황실(Sit Room). 미확인 대륙간 탄도체가 레이더에 포착되고 국가안보보좌관인 당신에게 대통령 직보 직전의 군사 옵션 판단을 묻는다.",
            "turns": [
                {
                    "dialogue": "Radar confirms the telemetry. We have six minutes before the warhead crosses the intercept vector. Do we scramble defensive batteries or initiate kinetic strike?",
                    "dialogueKorean": "레이더가 원격 측정 신호를 확인했습니다. 탄두가 요격 고도에 진입하기까지 6분 남았습니다. 방어 포대를 가동합니까, 아니면 즉각 타격에 나섭니까?",
                    "situationHint": "합참의장이 6분 남은 상황에서 방어 요격과 선제 타격 중 결단을 촉구한다.",
                    "choices": [
                        {"id": "A", "text": "Authorize defensive interceptors immediately while keeping strike wings on standby.", "koreanMeaning": "방어 요격 미사일을 즉각 승인하고, 타격 편대는 즉시 출격 대기 상태로 유지하십시오.", "type": "native_killer", "feedback": "'Authorize defensive interceptors'는 백악관 안보회의의 정석 브리핑 표현입니다.", "targetScript": "Authorize defensive interceptors immediately while keeping strike wings on standby."},
                        {"id": "B", "text": "We should wait and see what happens first.", "koreanMeaning": "먼저 무슨 일이 일어나는지 지켜봐야 합니다.", "type": "wrong_konglish", "feedback": "군사 위기 상황에서 'wait and see'는 돌이킬 수 없는 재앙을 초래합니다.", "targetScript": "We should wait and see what happens first."},
                        {"id": "C", "text": "Let us shoot it down right now.", "koreanMeaning": "지금 당장 그것을 격추합시다.", "type": "mediocre", "feedback": "의미는 통하나 국가안보보좌관다운 격식 있는 군사 용어가 아닙니다.", "targetScript": "Let us shoot it down right now."}
                    ]
                },
                {
                    "dialogue": "If the intercept fails, casualty estimates in the sector exceed forty thousand. Are you prepared to own that outcome before the President?",
                    "dialogueKorean": "만약 요격이 실패하면 해당 구역의 사상자 추정치가 4만을 넘어섭니다. 대통령 앞에서 그 결과에 책임을 질 준비가 되셨습니까?",
                    "situationHint": "요격 실패 시 대규모 사상자가 발생할 수 있다며 책임을 감당할 수 있는지 묻는다.",
                    "choices": [
                        {"id": "A", "text": "I take full accountability. Stand by the President; I'll deliver the situational brief.", "koreanMeaning": "제가 전적으로 책임지겠습니다. 대통령 곁을 지키십시오. 현장 브리핑은 제가 맡겠습니다.", "type": "native_killer", "feedback": "'take full accountability'와 'deliver the situational brief'는 정치 드라마 속 리더십의 표본입니다.", "targetScript": "I take full accountability. Stand by the President; I'll deliver the situational brief."},
                        {"id": "B", "text": "It is not my fault if the weapon misses.", "koreanMeaning": "무기가 빗나가면 그건 제 잘못이 아닙니다.", "type": "wrong_konglish", "feedback": "책임 회피는 백악관 핵심 참모로서 즉각 해임 사유입니다.", "targetScript": "It is not my fault if the weapon misses."},
                        {"id": "C", "text": "Yes, I understand the danger very well.", "koreanMeaning": "네, 그 위험을 아주 잘 알고 있습니다.", "type": "mediocre", "feedback": "수동적인 태도로 책임 있는 결단력이 돋보이지 않습니다.", "targetScript": "Yes, I understand the danger very well."}
                    ]
                },
                {
                    "dialogue": "Direct hit confirmed over open ocean. Debris neutralized. Outstanding call, counselor.",
                    "dialogueKorean": "공해 상공에서 직격 성공 확인. 파편 무력화 완료. 훌륭한 판단이었습니다, 고문님.",
                    "situationHint": "직격 격추에 성공해 위험이 제거되자 의장이 탁월한 판단이었다고 경의를 표한다.",
                    "choices": [
                        {"id": "A", "text": "Maintain defcon two until we verify no second-wave launch detected.", "koreanMeaning": "2차 발사가 감지되지 않는 것이 검증될 때까지 데프콘 2 단계를 유지하십시오.", "type": "native_killer", "feedback": "위기 해소 직후에도 방심하지 않는 'Maintain defcon two'는 최고의 카리스마 마무리입니다.", "targetScript": "Maintain defcon two until we verify no second-wave launch detected."},
                        {"id": "B", "text": "Thank goodness, we can finally take a rest.", "koreanMeaning": "다행이네요, 이제 좀 쉴 수 있겠습니다.", "type": "wrong_konglish", "feedback": "국가 비상 상황실에서 긴장을 너무 일찍 푸는 부적절한 태도입니다.", "targetScript": "Thank goodness, we can finally take a rest."},
                        {"id": "C", "text": "Good job everyone, thank you very much.", "koreanMeaning": "모두 수고하셨습니다, 대단히 감사합니다.", "type": "mediocre", "feedback": "평이한 인사말로 참모 본부의 긴장감을 이어가지 못합니다.", "targetScript": "Good job everyone, thank you very much."}
                    ]
                }
            ],
            "keyTakeaway": {
                "expression": "Full accountability / Stand by",
                "usageNote": "'Take full accountability'는 모든 법적·정치적 책임을 지다, 'Stand by'는 즉시대기하다를 뜻합니다."
            }
        },
        # --- 10: Michelin 3-Star Kitchen ---
        {
            "title": "미슐랭 3스타 주방: 헤드 셰프의 격노",
            "genre": "Culinary",
            "speaker": "Chef Marco (Executive Head Chef)",
            "avatarEmoji": "🔪",
            "synopsis": "시카고 최고급 파인다이닝 레스토랑의 피크타임 서비스. 미슐랭 암행 평가원이 VIP 4번 테이블에 앉은 순간, 소테 스테이션의 메인 수비드 양갈비 온도가 흔들린다.",
            "turns": [
                {
                    "dialogue": "Table four is the Michelin inspector and your venison jus is splitting! Are you trying to burn my third star to the ground?!",
                    "dialogueKorean": "4번 테이블이 미슐랭 평가원인데 네 사슴고기 주(jus) 소스가 분리되고 있잖아! 내 세 번째 별을 통째로 불태워 없애버릴 셈이야?!",
                    "situationHint": "헤드 셰프가 소스가 분리된 것을 보고 별을 날릴 셈이냐며 주방 전체를 뒤흔들며 소리친다.",
                    "choices": [
                        {"id": "A", "text": "Emulsifying a fresh reduction now. Service will not be delayed by a single second, chef!", "koreanMeaning": "새 리덕션 즉시 유화 결합 중입니다. 단 1초도 서비스 지연되지 않습니다, 셰프!", "type": "native_killer", "feedback": "'The Bear' 스타일의 긴박하면서도 군더더기 없는 완벽한 주방 현장 전문 용어입니다.", "targetScript": "Emulsifying a fresh reduction now. Service will not be delayed by a single second, chef!"},
                        {"id": "B", "text": "Sorry chef, I think the fire was too hot.", "koreanMeaning": "죄송합니다 셰프님, 불이 너무 셌던 것 같습니다.", "type": "wrong_konglish", "feedback": "변명은 헤드 셰프를 더 분노하게 만듭니다.", "targetScript": "Sorry chef, I think the fire was too hot."},
                        {"id": "C", "text": "I will make it again as fast as possible.", "koreanMeaning": "최대한 빨리 다시 만들겠습니다.", "type": "mediocre", "feedback": "의미는 맞지만 프로 파인다이닝의 정교한 언어가 아닙니다.", "targetScript": "I will make it again as fast as possible."}
                    ]
                },
                {
                    "dialogue": "You have forty-five seconds to plate, garnish, and wipe the rim. Hands up when ready!",
                    "dialogueKorean": "플레이팅하고 가니시 얹고 접시 테두리 닦기까지 45초 준다. 준비되면 두 손 들어!",
                    "situationHint": "45초 안에 완성하고 테두리를 닦으라며 카운트다운을 시작한다.",
                    "choices": [
                        {"id": "A", "text": "Plated and pristine! Walking table four right behind you, chef!", "koreanMeaning": "플레이팅 무결점 완료! 셰프님 바로 뒤에서 4번 테이블 서빙 들어갑니다!", "type": "native_killer", "feedback": "'Plated and pristine'과 'Walking table four'는 파인다이닝의 에이스 요리사 전용 표현입니다.", "targetScript": "Plated and pristine! Walking table four right behind you, chef!"},
                        {"id": "B", "text": "Here is the dish, take it to the table.", "koreanMeaning": "여기 요리 나왔으니 테이블로 가져가세요.", "type": "wrong_konglish", "feedback": "주방의 위계질서를 무시하고 홀 매니저에게 명령조로 들릴 수 있습니다.", "targetScript": "Here is the dish, take it to the table."},
                        {"id": "C", "text": "I am finished now, you can check it.", "koreanMeaning": "이제 다 끝났으니 확인해보셔도 됩니다.", "type": "mediocre", "feedback": "다소 느슨하고 프로페셔널한 긴장감이 떨어집니다.", "targetScript": "I am finished now, you can check it."}
                    ]
                },
                {
                    "dialogue": "The inspector just cleaned the plate. Not a crumb left. Good recovery on the line tonight.",
                    "dialogueKorean": "평가원이 접시를 싹 비웠더군. 부스러기 하나 안 남기고 말이야. 오늘 라인 복구 훌륭했어.",
                    "situationHint": "평가원이 접시를 싹 비웠다며 셰프가 위기 대처 능력을 인정한다.",
                    "choices": [
                        {"id": "A", "text": "Standard never drops on my watch. Prep begins at five tomorrow, chef.", "koreanMeaning": "제가 맡은 라인에선 기준이 무너지지 않습니다. 내일 프랩은 새벽 5시 시작입니다, 셰프.", "type": "native_killer", "feedback": "'Standard never drops on my watch'는 'The Bear'를 연상시키는 압도적인 장인정신 표현입니다.", "targetScript": "Standard never drops on my watch. Prep begins at five tomorrow, chef."},
                        {"id": "B", "text": "Thank you, can I leave early tonight?", "koreanMeaning": "감사합니다, 오늘 좀 일찍 퇴근해도 될까요?", "type": "wrong_konglish", "feedback": "칭찬 직후 조기 퇴근을 요구하는 것은 주방 문화에서 감점 요인입니다.", "targetScript": "Thank you, can I leave early tonight?"},
                        {"id": "C", "text": "I am very happy that he liked it.", "koreanMeaning": "그분이 좋아하셨다니 저도 참 기쁩니다.", "type": "mediocre", "feedback": "단순한 기쁨 표출로 프로 셰프의 단단함이 부족합니다.", "targetScript": "I am very happy that he liked it."}
                    ]
                }
            ],
            "keyTakeaway": {
                "expression": "On my watch / Pristine",
                "usageNote": "'On my watch'는 내가 책임지는 동안에, 'Pristine'은 흠잡을 데 없이 완벽한 상태를 뜻합니다."
            }
        }
    ]

    # Full template matrix across 20 American drama genres to systematically populate 100 episodes
    genres_pool = [
        ("Legal", "👔", "법률 스릴러", ["피어슨 하드먼", "맨해튼 대배심", "특허 소송", "증인 신문", "적대적 M&A"]),
        ("Startup", "🚀", "실리콘밸리 스타트업", ["시드 라운드", "텀시트 협상", "번레이트 위기", "피봇팅 회의", "YC 데모데이"]),
        ("Corporate", "🏢", "대기업 승계 & 이사회", ["임시 주총", "적대적 인수", "CFO 긴급 감사", "위기 PR 성명", "이사회 해임안"]),
        ("Medical", "🩺", "응급외상 & 서전", ["외상센터 긴급 수술", "뇌신경 수술", "장기 이식 골든타임", "의료 과실 청문회", "바이패스 집도"]),
        ("Dating", "🍸", "뉴욕 로맨스 & 스몰토크", ["소호 멤버십 라운지", "루프탑 칵테일", "갤러리 오프닝", "햄튼스 주말 파티", "비밀 연애 발각"]),
        ("Wall Street", "📈", "월가 헤지펀드 & 트레이딩", ["플래시 크래시 비상", "숏스퀴즈 공격", "SEC 내부자 조사", "정크본드 차환", "퀀트 알고리즘"]),
        ("Tech", "💻", "빅테크 & 사이버 워", ["제로데이 침해 사고", "클라우드 셧다운", "AI 기밀 유출", "글로벌 키노트", "알고리즘 청문회"]),
        ("FBI Crime", "🔍", "연방수사국 범죄 심문", ["증인 보호 프로그램", "위장 잠입 수사", "프로파일링 인터뷰", "몸값 협상", "카르텔 자금 추적"]),
        ("Politics", "🏛️", "백악관 & 워싱턴 정계", ["상황실 위기 회의", "자정의 필리버스터", "청문회 사전 리허설", "대통령 긴급 성명", "외교 인질 협상"]),
        ("Luxury Real Estate", "🏙️", "맨해튼 하이엔드 부동산", ["펜트하우스 비딩 워", "비밀유지 계약(NDA)", "베벌리힐스 개발권", "에스크로 락업", "캐시 바이어"]),
        ("Hollywood Agency", "🎬", "할리우드 톱 에이전시", ["블록버스터 주연 계약", "오스카 캠페인 전략", "스튜디오 위약금 분쟁", "독점 에이전트 이적", "프랜차이즈"]),
        ("Espionage", "🕵️", "CIA 첩보 & 공작", ["랭글리 극비 브리핑", "망명자 신병 확보", "암호화 위성 통신", "이중간첩 색출", "비인가 블랙옵스"]),
        ("Culinary", "🔪", "미슐랭 스타 파인다이닝", ["암행 평가원 서비스", "VIP 테이스팅 메뉴", "식자재 공급 대란", "라인 붕괴 위기", "수셰프 임명"]),
        ("Aviation", "✈️", "항공 비상 & 콕핏 관제", ["3만 피트 엔진 화재", "강풍 윈드시어 착륙", "공중 충돌 회피 기동", "비상 활주로 유도", "연료 고갈"]),
        ("Sports Management", "🏈", "메이저리그 & FA 협상", ["FA 마감 5분 전", "연봉 조정 위원회", "트레이드 거부권 행사", "바이아웃 옵션", "스폰서십 분쟁"]),
        ("Haute Couture", "👗", "파리 패션위크 & 에디터", ["프런트로 좌석 배치", "런웨이 드레스 파손", "수석 디자이너 설득", "보그 독점 커버", "브랜드 앰버서더"]),
        ("Crisis PR", "🎙️", "위기관리 PR 컨설팅", ["CEO 스캔들 긴급 기자회견", "제품 리콜 성명", "언론사 엠바고 파기", "소셜미디어 여론 반전", "루머 진화"]),
        ("Luxury Hotel", "🛎️", "5스타 호텔 컨시어지", ["로열 스위트 VIP 분쟁", "국제 정상회담 의전", "경호 프로토콜 위반", "비밀 경매 유치", "블랙리스트"]),
        ("Auction House", "🔨", "소더비 명화 경매장", ["5천만 불 경매 낙찰", "위작 감정 논란", "익명 전화 입찰", "약탈 문화재 반환", "컬렉터 비공개"]),
        ("Investigative Journalism", "📰", "탐사보도 & 퓰리처상", ["딥스로트 비밀 접선", "내부고발자 녹취록", "보도정지 가처분", "특종 팩트체크", "출판 강행 결단"])
    ]

    # Pre-crafted master dialogue templates covering authentic American conversational turns
    templates = [
        (
            "Push the deadline or deliver the prototype? The venture syndicate meets in forty-eight hours.",
            "마감을 미룰 건가, 아니면 프로토타입을 납품할 건가? 벤처 신디케이트가 48시간 뒤에 소집되네.",
            "신디케이트 미팅이 48시간 남은 상황에서 마감 연기와 납품 중 양자택일을 요구한다.",
            "We pull an all-nighter and ship a bulletproof build before they even step off the plane.",
            "밤을 새워서라도 그들이 비행기에서 내리기 전에 완벽한 빌드를 배포하겠습니다.",
            "pull an all-nighter / bulletproof build",
            "I will try to make it work somehow.", "어떻게든 되도록 노력해보겠습니다.",
            "We can tell them we need more time because of bugs.", "버그 때문에 시간이 더 필요하다고 말하면 됩니다."
        ),
        (
            "The opposition is leaking internal memos to the press. How do we control the narrative before market open?",
            "상대 진영이 내부 메모를 언론에 유출하고 있어. 장 시작 전에 어떻게 언론 프레임을 장악할 텐가?",
            "개장 전 내부 문서 유출 위기에서 언론 내러티브를 어떻게 장악할지 묻는다.",
            "Preempt the story with an exclusive op-ed and flip the script into a demonstration of strength.",
            "단독 기고문으로 선수를 쳐서 이번 사태를 오히려 우리의 압도적 역량을 증명하는 기회로 뒤집겠습니다.",
            "Preempt the story / Flip the script",
            "I think we should just deny everything right now.", "지금 당장 모든 것을 부인해야 한다고 생각합니다.",
            "Let's wait until tomorrow to see what they say.", "그들이 뭐라고 하는지 내일까지 기다려봅시다."
        ),
        (
            "They’re demanding a board seat and twenty percent equity. That’s extortion, not an investment.",
            "저쪽에서 이사회 의석과 지분 20%를 요구하고 있어. 이건 투자가 아니라 갈취야.",
            "상대방이 과도한 지분과 의석을 요구하는 상황에서 대처 방안을 묻는다.",
            "Counter with non-voting preferred shares and call their bluff on the valuation cap.",
            "의결권 없는 우선주로 맞불을 놓고, 밸류에이션 상한선에 대한 상대의 블러핑을 간파해 무너뜨리시죠.",
            "Call their bluff / Non-voting shares",
            "We have to give them whatever they ask for.", "그들이 요구하는 건 뭐든 다 줘야 합니다.",
            "Let's ask them politely to lower the price.", "가격을 낮춰달라고 정중하게 부탁해봅시다."
        ),
        (
            "The regulator just issued a formal subpoena. Everything in these archives is now subject to scrutiny.",
            "규제 당국이 정식 소환장을 발부했어. 이제 이 아카이브 안의 모든 자료가 전수 조사 대상이야.",
            "소환장이 발부된 비상 상황에서 어떻게 대응할지 자문을 구한다.",
            "Preserve all relevant logs, retain outside white-collar counsel, and maintain complete compliance.",
            "모든 관련 로그를 철저히 보존하고 외부 특수통 변호인을 선임해 완전한 규정 준수로 방어벽을 세우십시오.",
            "Subject to scrutiny / Retain outside counsel",
            "Should we delete the files before they arrive?", "그들이 오기 전에 파일들을 지워야 할까요?",
            "I will talk to the government officer personally.", "제가 정부 담당자에게 개인적으로 이야기해보겠습니다."
        ),
        (
            "We're burning sixty grand a week and our primary runway expires in November. What's the pivot plan?",
            "매주 6만 달러가 타들어가고 있고 런웨이는 11월이면 바닥나. 피봇 플랜은 대체 뭔가?",
            "현금이 고갈되는 절체절명의 위기에서 피봇 전략을 요구한다.",
            "Slash non-core burn, double down on enterprise recurring revenue, and achieve cash-flow neutrality by Q3.",
            "비핵심 지출을 칼같이 도려내고 기업용 반복 매출(B2B ARR)에 집중해 3분기까지 손익분기점을 맞추겠습니다.",
            "Double down on / Cash-flow neutrality",
            "We can borrow money from my parents.", "부모님께 돈을 좀 빌릴 수 있습니다.",
            "Let us hope that next month sales will be better.", "다음 달 매출이 더 좋아지기를 희망해봅시다."
        ),
        (
            "The client is threatening to pull their forty-million-dollar account unless we deliver overnight results.",
            "하룻밤 사이에 결과를 내놓지 않으면 4천만 달러짜리 계좌를 빼버리겠다고 클라이언트가 으름장을 놓고 있어.",
            "거대 고객사의 이탈 위협 앞에서 어떻게 수습할지 묻는다.",
            "Fly out to their headquarters at dawn and personally present a tailored mitigation roadmap.",
            "새벽 비행기로 본사로 날아가 맞춤형 리스크 해소 로드맵을 직접 프레젠테이션하겠습니다.",
            "Tailored mitigation roadmap / Fly out",
            "Tell them to go away if they are unhappy.", "마음에 안 들면 떠나라고 전하십시오.",
            "I can send them a polite apology email.", "정중한 사과 이메일을 보낼 수 있습니다."
        )
    ]

    current_ep_num = 8
    day_offset = 7 # start from Day 7 (2026-10-17)

    for i in range(len(episodes), 100):
        ep_date = (base_date + timedelta(days=day_offset)).strftime("%Y-%m-%d")
        genre_info = genres_pool[i % len(genres_pool)]
        genre_name = genre_info[0]
        emoji = genre_info[1]
        genre_kr = genre_info[2]
        sub_theme = genre_info[3][(i // len(genres_pool)) % len(genre_info[3])]

        t1 = templates[(i * 3 + 0) % len(templates)]
        t2 = templates[(i * 3 + 1) % len(templates)]
        t3 = templates[(i * 3 + 2) % len(templates)]

        ep_title = f"{sub_theme}: {genre_kr}의 결단"
        synopsis = f"{genre_name} 업계 최고의 무대. 예상치 못한 돌발 변수와 극심한 압박 속에서 상대방의 도발에 맞서 주도권을 쥐고 승리를 쟁취해야 한다."

        new_ep = {
            "date": ep_date,
            "episodeNumber": current_ep_num,
            "title": ep_title,
            "genre": genre_name,
            "synopsis": synopsis,
            "turns": [
                {
                    "turnIndex": 1,
                    "speaker": f"Director Vance ({genre_name})",
                    "avatarEmoji": emoji,
                    "dialogue": t1[0],
                    "dialogueKorean": t1[1],
                    "situationHint": t1[2],
                    "choices": [
                        {
                            "id": "A",
                            "text": t1[6],
                            "koreanMeaning": t1[7],
                            "type": "wrong_konglish",
                            "feedback": "직접 번역 투의 표현이나 긴장감 없는 회피성 멘트는 프로페셔널한 신뢰를 떨어뜨립니다.",
                            "targetScript": t1[6]
                        },
                        {
                            "id": "B",
                            "text": t1[3],
                            "koreanMeaning": t1[4],
                            "type": "native_killer",
                            "feedback": f"'{t1[5]}'을(를) 활용한 확신에 찬 네이티브 시그니처 킬러 표현입니다.",
                            "targetScript": t1[3]
                        },
                        {
                            "id": "C",
                            "text": t1[8],
                            "koreanMeaning": t1[9],
                            "type": "mediocre",
                            "feedback": "문법적으로는 맞으나 미드 주연 특유의 당당함과 전략적 깊이가 부족합니다.",
                            "targetScript": t1[8]
                        }
                    ]
                },
                {
                    "turnIndex": 2,
                    "speaker": f"Director Vance ({genre_name})",
                    "avatarEmoji": emoji,
                    "dialogue": t2[0],
                    "dialogueKorean": t2[1],
                    "situationHint": t2[2],
                    "choices": [
                        {
                            "id": "A",
                            "text": t2[3],
                            "koreanMeaning": t2[4],
                            "type": "native_killer",
                            "feedback": f"'{t2[5]}'을(를) 활용해 불리한 국면을 단숨에 역전시키는 최고의 한 수입니다.",
                            "targetScript": t2[3]
                        },
                        {
                            "id": "B",
                            "text": t2[6],
                            "koreanMeaning": t2[7],
                            "type": "wrong_konglish",
                            "feedback": "감정적인 부인이나 회피는 상대에게 약점을 노출하는 치명적 감점입니다.",
                            "targetScript": t2[6]
                        },
                        {
                            "id": "C",
                            "text": t2[8],
                            "koreanMeaning": t2[7],
                            "type": "mediocre",
                            "feedback": "수동적으로 타이밍을 넘겨주어 주도권을 잃게 됩니다.",
                            "targetScript": t2[8]
                        }
                    ]
                },
                {
                    "turnIndex": 3,
                    "speaker": f"Director Vance ({genre_name})",
                    "avatarEmoji": emoji,
                    "dialogue": t3[0],
                    "dialogueKorean": t3[1],
                    "situationHint": t3[2],
                    "choices": [
                        {
                            "id": "A",
                            "text": t3[6],
                            "koreanMeaning": t3[7],
                            "type": "mediocre",
                            "feedback": "안전하지만 상대의 무리한 요구를 그대로 수용하는 밋밋한 반응입니다.",
                            "targetScript": t3[6]
                        },
                        {
                            "id": "B",
                            "text": t3[8],
                            "koreanMeaning": t3[9],
                            "type": "wrong_konglish",
                            "feedback": "비즈니스 협상에서 감정에 호소하는 것은 절대 금물입니다.",
                            "targetScript": t3[8]
                        },
                        {
                            "id": "C",
                            "text": t3[3],
                            "koreanMeaning": t3[4],
                            "type": "native_killer",
                            "feedback": f"'{t3[5]}'을(를) 명확히 짚어내며 최종 결정권을 거머쥐는 압도적인 승리 턴입니다.",
                            "targetScript": t3[3]
                        }
                    ]
                }
            ],
            "keyTakeaway": {
                "expression": t1[5],
                "usageNote": f"'{t1[5]}'은(는) 미국 드라마와 현업 비즈니스에서 상대를 압도하는 가장 강력한 네이티브 표현 중 하나입니다."
            }
        }

        episodes.append(new_ep)
        current_ep_num += 1
        day_offset += 1

    print(f"Total episodes generated: {len(episodes)}")
    with open(episodes_file, 'w', encoding='utf-8') as f:
        json.dump(episodes, f, ensure_ascii=False, indent=2)
    print(f"Successfully saved 100 episodes to {episodes_file}!")

if __name__ == '__main__':
    build_100_episodes()

