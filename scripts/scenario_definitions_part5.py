# -*- coding: utf-8 -*-
"""
Dramactor Curated Master Database - Part 5 (Episodes 81 to 100)
Grand Finale & Immortal Legacy across 20 American drama genres.
"""

EPISODES_81_TO_100 = [
    # -------------------------------------------------------------
    # EP 81: Legal (최후의 평결: 미국 헌법을 바꾼 랜드마크 재판)
    # -------------------------------------------------------------
    {
        "ep_num": 81,
        "title": "최후의 평결: 미국 헌법을 바꾼 랜드마크 재판",
        "genre": "Legal",
        "speaker": "Harvey Specter (Managing Senior Partner)",
        "emoji": "⚖️",
        "synopsis": "뉴욕 연방법원 중앙 대법정. 5년간 이어진 사상 최대의 국가 권력 남용 및 시민 자유 침해 집단 소송 최종 변론. 12명의 배심원단이 평결을 위해 퇴장하기 3분 전, 헌법의 불멸의 가치를 증명하는 클로징을 마쳐야 한다.",
        "turns": [
            {
                "dialogue": "This is it. Five years of sleepless nights, corrupt judges, and death threats come down to your final three minutes before this jury. Are you going to quote statutes, or are you going to move their souls?",
                "korean": "드디어 이 순간이군. 5년간의 뜬눈으로 지새운 밤, 부패한 판사들, 살해 협박까지 이 모든 것이 배심원 앞 자네의 마지막 3분에 달렸어. 조문이나 읊어댈 텐가, 아니면 저들의 영혼을 뒤흔들 텐가?",
                "hint": "딱딱한 법 조문 나열을 넘어, 평범한 시민들의 존엄성과 헌법이 약속한 정의의 본질을 호소한다.",
                "choices": [
                    ("Look each juror in the eye: remind them that laws are not dead ink on parchment, but a living covenant protecting the powerless against the tyrant.", "배심원 한 사람 한 사람의 눈을 맞추십시오: 법은 양피지 위의 죽은 활자가 아니라, 폭군에 맞서 힘없는 약자를 지켜주는 살아 숨 쉬는 약속임을 상기시키십시오.", "native_killer", "'Suits'의 하비 스펙터를 전율케 하는 진정한 전설적인 법정 최후 변론의 극치입니다."),
                    ("Tell the jurors that you want to go home early so please vote quickly.", "배심원들에게 일찍 퇴근하고 싶으니 빨리 대충 투표해달라고 조릅시다.", "wrong_konglish", "배심원단을 모욕하고 5년간의 소송을 한순간에 망쳐버리는 경망스러운 발언입니다."),
                    ("Recite the federal tax code numbers from page one to fifty.", "연방 세법 조항 번호를 1페이지부터 50페이지까지 달달 낭독합시다.", "mediocre", "배심원들을 지루하게 만들어 집중력을 흩뜨리는 무미건조한 변론입니다.")
                ]
            },
            {
                "dialogue": "The jury foreman looked down and wiped a tear. The opposing counsel is sweating through his thousand-dollar suit. What is your final punchline before you step away from the podium?",
                "korean": "배심원 대표가 고개를 떨구고 눈물을 훔쳤어. 상대 변호사는 수천 달러짜리 양복이 땀에 젖고 있네. 단상에서 물러서기 전 마지막 펀치라인이 뭔가?",
                "hint": "정의는 결코 침묵하지 않는다는 숭고한 헌법적 확신으로 쐐기를 박는다.",
                "choices": [
                    ("Let your verdict echo through generations: that in this Republic, no corporation is above the law, and no citizen is beneath its shelter. The defense rests.", "여러분의 평결이 후대에 메아리치게 해주십시오: 이 공화국에서 어떤 거대 기업도 법 위에 군림할 수 없으며, 어떤 시민도 법의 보호 아래 소외되지 않는다고. 변호인 변론을 마칩니다.", "native_killer", "'To Kill a Mockingbird'와 'A Few Good Men'의 계보를 잇는 불멸의 명대사입니다."),
                    ("If you don't vote for us, I will haunt your dreams forever.", "우리 편 안 들어주면 내가 평생 꿈에 나타나서 괴롭힐 겁니다.", "wrong_konglish", "배심원 협박죄로 즉각 법정 구속을 부르는 정신 나간 폭언입니다."),
                    ("I guess that is all I have to say, have a nice weekend.", "제가 할 말은 대충 이게 전부인 것 같네요, 좋은 주말 보내세요.", "mediocre", "역사적인 랜드마크 재판의 결말치고는 너무 무기력합니다.")
                ]
            },
            {
                "dialogue": "Unanimous verdict! Five billion dollars in punitive damages! The entire courtroom rose to applaud! You didn't just win a lawsuit, partner; you rewrote American jurisprudence.",
                "korean": "배심원 전원일치 평결! 징벌적 손해배상 50억 달러 인용! 법정 전체가 기립 박수를 보냈어! 자네는 단순한 승소가 아니라 미국의 법 철학을 새로 썼네, 파트너.",
                "hint": "법조인으로서 최고의 정점에 선 변호사의 가슴 벅찬 자부심.",
                "choices": [
                    ("Justice delivered, Harvey. Pearson Specter now stands on the highest peak of American law. Let us walk out into the sunlight together.", "정의가 실현되었습니다, 하비. 이제 피어슨 스펙터는 미국 법조계의 가장 높은 봉우리에 우뚝 섰습니다. 함께 햇살 속으로 걸어나가시죠.", "native_killer", "'Suits'의 모든 여정을 완벽하게 매듭짓는 찬란하고 감동적인 피날레입니다."),
                    ("I am the greatest lawyer on planet Earth, everyone bow down!", "내가 지구상에서 가장 위대한 변호사다, 다들 내 앞에 무릎 꿇어라!", "wrong_konglish", "숭고한 승리 직후 오만방자함으로 동료들의 눈살을 찌푸리게 하는 언사입니다."),
                    ("Thank you Harvey, five years was a very long time.", "감사합니다 하비, 5년은 참 긴 시간이었네요.", "mediocre", "역사에 남을 대법정 승리의 감격에 비해 너무 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Living covenant / Defense rests",
        "key_note": "'Living covenant'는 살아 숨 쉬는 약속으로서의 법, 'The defense rests'는 변호인의 모든 변론이 완결되었음을 알리는 법정 종결 선언입니다."
    },
    # -------------------------------------------------------------
    # EP 82: Startup (데카콘 화성 탐사선 로켓 테크 합병)
    # -------------------------------------------------------------
    {
        "ep_num": 82,
        "title": "화성 탐사 우주 테크: 1,000억 달러 초대형 합병",
        "genre": "Startup",
        "speaker": "Elon Musk (Spaceflight & Tech Visionary)",
        "emoji": "🚀",
        "synopsis": "텍사스 보카치카 스타베이스 발사 통제 센터. 인류 최초의 민간 화성 유인 착륙선 발사 30분 전, 글로벌 딥테크 양대 산맥인 우주 로켓 기업과 인공지능 위성 기업의 1,000억 달러 합병 서명이 카운트다운과 함께 진행된다.",
        "turns": [
            {
                "dialogue": "T-minus thirty minutes to Mars Starship ignition! But Wall Street investment bankers are warning that combining autonomous AI navigation with rocket manufacturing creates unprecedented regulatory monopoly risks. Do we sign before launch or postpone?",
                "korean": "화성 스타쉽 점화까지 30분 전! 하지만 월가 투자은행들은 자율 AI 항법과 로켓 제조의 결합이 전례 없는 독점 규제 리스크를 부를 거라며 경고하고 있어. 발사 전에 서명할 텐가, 연기할 텐가?",
                "hint": "독점 논란을 넘어 다행성 문명(Multi-planetary species) 개척이라는 인류사적 비전으로 규제 당국과 시장을 설득한다.",
                "choices": [
                    ("Sign immediately. Multi-planetary civilization requires radical vertical integration; no fragmented supply chain can land humans on Mars. Let the future judge our audacity.", "즉시 서명하십시오. 다행성 문명 개척은 급진적인 수직 통합을 필요로 합니다; 파편화된 공급망으로는 화성에 인류를 착륙시킬 수 없습니다. 미래가 우리의 담대함을 심판하게 하십시오.", "native_killer", "일론 머스크의 우주 개척 철학을 완벽히 대변하는 'Multi-planetary radical vertical integration' 선언입니다."),
                    ("Cancel the Mars flight and give the rocket to NASA for free.", "화성 비행을 취소하고 로켓을 NASA에 공짜로 줘버립시다.", "wrong_konglish", "수십 년간의 기술 혁신과 창업의 꿈을 허무하게 포기하는 한심한 소리입니다."),
                    ("Wait until aliens land on Earth to make our decision.", "외계인이 지구에 착륙할 때까지 결정을 미루고 기다려봅시다.", "wrong_konglish", "역사적인 우주 발사 카운트다운 앞에서 비현실적인 농담을 늘어놓는 태도입니다.")
                ]
            },
            {
                "dialogue": "Merger agreement executed! T-minus two minutes! But telemetry indicates a thermal pressure fluctuation in booster engine three. Scrub the launch, or trust the autonomous telemetry?",
                "korean": "합병 계약 체결 완료! 2분 전! 하지만 3번 부스터 엔진에서 미세한 열 압력 변동이 원격 측정에 잡혔어. 발사를 중단할 텐가, 자율 원격 측정 알고리즘을 신뢰할 텐가?",
                "hint": "초당 수천 번의 실시간 캘리브레이션을 수행하는 AI 신경망 추력 분배 시스템을 확신하고 발사를 승인한다.",
                "choices": [
                    ("Trust the neural flight avionics: dynamic throttle reallocation will compensate in three milliseconds. All systems are green; authorize final launch sequence.", "신경망 항공 전자 시스템을 신뢰하십시오: 동적 추력 재분배가 3밀리초 만에 오차를 보정할 것입니다. 전 계통 정상; 최종 발사 시퀀스를 승인하십시오.", "native_killer", "최첨단 항공우주 공학의 정밀함과 위대한 개척자의 확신을 보여주는 완벽한 발사 승인입니다."),
                    ("Let's go outside and kick the rocket booster with our boots.", "밖으로 뛰어나가 발로 로켓 부스터를 툭툭 차봅시다.", "wrong_konglish", "극저온 액체 메탄 추진체가 가득 찬 로켓 앞에서 자살을 시도하는 미친 짓입니다."),
                    ("Close your eyes and hope the rocket doesn't blow up.", "눈을 감고 로켓이 안 터지기만을 요행으로 기도합시다.", "mediocre", "과학적 데이터 분석을 망각한 무책임한 처신입니다.")
                ]
            },
            {
                "dialogue": "Ignition! Liftoff! Super Heavy cleared the tower and Starship entered trans-Mars injection trajectory! Market valuation: one hundred twenty billion dollars! You made humanity multi-planetary today.",
                "korean": "점화! 이륙! 슈퍼 헤비가 발사대를 박차고 날아올라 스타쉽이 화성 전이 궤도에 진입했어! 기업가치 1,200억 달러 돌파! 자네가 오늘 인류를 다행성 종족으로 만들었네.",
                "hint": "우주 시대의 개막을 알리는 위대한 테크 창업자의 웅장한 피날레.",
                "choices": [
                    ("The stars are no longer distant dreams, Elon; they are our destination. Let us track the telemetry all the way to the red planet.", "별들은 더 이상 아득한 꿈이 아닙니다, 일론; 우리의 목적지입니다. 붉은 행성에 착륙할 때까지 원격 측정 데이터를 끝까지 추적합시다.", "native_killer", "인류 우주 탐사의 새 역사를 쓴 테크 리더의 가장 벅찬 영광의 순간입니다."),
                    ("Now I want to buy a ticket to Mars and never come back to Earth!", "이제 화성행 티켓 끊어서 지구로 영원히 안 돌아올래요!", "wrong_konglish", "위대한 과학적 도약 직후 현실 도피성 발언을 일삼는 가벼운 태도입니다."),
                    ("Thank you Elon, watching rockets is very loud.", "감사합니다 일론, 로켓 발사는 참 시끄럽네요.", "mediocre", "인류사적 우주 개척의 감격을 단순 소음으로 치부하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Multi-planetary civilization / Trans-Mars injection",
        "key_note": "'Multi-planetary'는 여러 행성에 인류 문명을 확장하는 비전, 'Trans-Mars injection'은 지구 궤도를 벗어나 화성으로 향하는 전이 궤적을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 83: Corporate (불멸의 미디어 제국 완성 주주들의 영구 신임)
    # -------------------------------------------------------------
    {
        "ep_num": 83,
        "title": "불멸의 미디어 제국 완성: 주주들의 영구 신임",
        "genre": "Corporate",
        "speaker": "Logan Roy (Eternal Chairman & Founder)",
        "emoji": "🏢",
        "synopsis": "웨이스타 로이코 본사 꼭대기 헤븐리 가든. 50년간의 정복 끝에 글로벌 미디어, 테크, 통신을 아우르는 3,000억 달러 단일 지주회사 통합을 완료하고, 전 세계 주주총회에서 영구 단독 회장으로 추대되는 역사적 대관식이 거행된다.",
        "turns": [
            {
                "dialogue": "Every competitor is crushed, every vulture fund is bought out, and the proxy battles are history. Three hundred billion dollars under one roof. Tell me: did we build an empire, or did we build a monument?",
                "korean": "모든 경쟁자는 박살 났고, 모든 하이에나 펀드는 흡수되었으며, 위임장 대결은 역사가 되었어. 한 지붕 아래 3천억 달러야. 내게 말해보게: 우리가 제국을 세운 건가, 아니면 불멸의 기념비를 세운 건가?",
                "hint": "단순한 기업의 크기를 넘어, 시대를 지배하고 여론의 향방을 결정하는 불가침의 문명적 영향력을 선언한다.",
                "choices": [
                    ("We built something far greater than money, Logan: an untouchable media dynasty that shapes human culture and dictates truth to power forever.", "우리는 돈보다 훨씬 위대한 것을 세웠습니다, 로건: 인류 문화를 형성하고 권력에 진실을 강제하는 불가침의 미디어 왕조를 완성했습니다.", "native_killer", "'Succession'의 로건 로이를 완전히 매료시키는 제국 완성의 가장 압도적인 헌사입니다."),
                    ("We built a giant pile of cash so we can buy more candy.", "사탕을 더 많이 사 먹을 수 있는 거대한 돈더미를 만들었죠.", "wrong_konglish", "3천억 달러 제국의 완성을 유치원생 장난으로 격하시키는 어처구니없는 소리입니다."),
                    ("I think we should donate the whole company to charity tomorrow.", "내일 회사 전체를 자선단체에 전액 기부해버립시다.", "wrong_konglish", "평생을 바쳐 제국을 일군 총수의 면전에서 모욕을 퍼붓는 자살골입니다.")
                ]
            },
            {
                "dialogue": "Untouchable dynasty. I like the sound of that. But the market opens in five minutes and Wall Street is waiting for our ten-year strategic guidance. What do you tell the world?",
                "korean": "불가침의 왕조라. 듣기 좋은 말이군. 하지만 5분 뒤 시장이 열리고 월스트리트는 우리의 향후 10년 전략 가이던스를 기다리고 있어. 세상에 뭐라고 공표할 텐가?",
                "hint": "안주하지 않고 차세대 양자 컴퓨팅 미디어와 우주 통신망까지 장악하겠다는 영원한 정복의 비전을 밝힌다.",
                "choices": [
                    ("Tell them we don't follow the market; the market follows us. Reinvest fifty billion into orbital communications and let the world know our dominance has only just begun.", "우리는 시장을 따르지 않으며 시장이 우리를 따른다고 선언하십시오. 500억 달러를 궤도 위성 통신망에 재투자하여 우리의 지배는 이제 겨우 시작되었음을 알리십시오.", "native_killer", "절대 권력을 쥔 제국의 수장이 구사하는 거침없는 선언입니다."),
                    ("Tell them we are tired and we will take a long nap until next year.", "너무 피곤하니 내년까지 긴 낮잠이나 자겠다고 공지합시다.", "wrong_konglish", "시장에 충격을 주고 주가를 대폭락시키는 나약한 발언입니다."),
                    ("Ask the investors to please send us love letters.", "투자자들에게 우리 회사로 연애편지나 보내달라고 부탁합시다.", "mediocre", "상장 대기업의 품격을 떨어뜨리는 기괴한 요청입니다.")
                ]
            },
            {
                "dialogue": "The market bell rang! Stock surged twenty percent! A three-hundred-sixty-billion-dollar valuation! You are no longer my successor; you are the architect of the future. Take the chair.",
                "korean": "개장 벨이 울렸어! 주가가 20% 폭등했네! 기업가치 3,600억 달러 돌파! 자넨 이제 단순한 후계자가 아니야; 미래의 설계자일세. 이 의자에 앉게.",
                "hint": "제국의 왕좌를 물려받은 최고 사령관의 위엄 있고 차분한 대관.",
                "choices": [
                    ("The throne is honored, Logan. Together, we built an empire that outlives time itself. Let the board commence.", "왕좌를 영광으로 받들겠습니다, 로건. 우리는 시간 자체를 초월해 영원히 살아남을 제국을 완성했습니다. 이사회를 개회하십시오.", "native_killer", "'Succession'의 대서사시를 가장 완벽하고 품격 있게 완결 짓는 불멸의 명대사입니다."),
                    ("I am going to dance on this boardroom table with my shoes off!", "신발 벗고 이사회 테이블 위에서 막춤이나 춰야지!", "wrong_konglish", "세계 최고 총수의 의자에 앉자마자 미치광이 행동을 일삼는 언사입니다."),
                    ("Thank you Logan, running an empire gives me back pain.", "감사합니다 로건, 제국 경영은 허리가 참 아프네요.", "mediocre", "역사적인 왕좌 승계의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Untouchable dynasty / Empire outlives time",
        "key_note": "'Untouchable dynasty'는 누구도 넘볼 수 없는 절대적 왕조, 'Outlive time'은 세대를 초월해 영원히 지속됨을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 84: Medical (샴쌍둥이 뇌 분리 수술 28시간 기적)
    # -------------------------------------------------------------
    {
        "ep_num": 84,
        "title": "샴쌍둥이 뇌 분리 수술: 28시간 기적의 집도",
        "genre": "Medical",
        "speaker": "Dr. Derek Shepherd (Chief of Pediatric Neurosurgery)",
        "emoji": "🏥",
        "synopsis": "존스 홉킨스 병원 본관 제1신경외과 수술실. 머리가 붙은 채 태어난 생후 6개월 샴쌍둥이의 공유 상시상정맥동(Superior Sagittal Sinus) 혈관 분리 수술 27시간째. 두 아이 모두에게 독립된 뇌혈류를 확보하며 생명을 살려내는 마지막 1시간의 기적에 도전한다.",
        "turns": [
            {
                "dialogue": "Hour twenty-seven. The shared sagittal venous sinus is bifurcated, but twin B's cerebral venous pressure is dropping fast! If we don't reconstruct the sinus wall with autologous pericardium in eight minutes, twin B suffers irreversible stroke! What is your micro-vascular reconstruction strategy?!",
                "korean": "27시간째 집도 중. 공유 상시상정맥동은 분리되었으나 쌍둥이 B의 뇌정맥압이 급락하고 있어! 8분 안에 자가 심낭 조직으로 정맥동 벽을 재건하지 못하면 B는 비가역적 뇌경색에 빠져! 미세혈관 재건 술기가 뭔가?!",
                "hint": "미세 10-0 나일론 봉합사로 자가 심낭 패치를 덧대어 협착 없이 완벽한 혈류 통로를 성형한다.",
                "choices": [
                    ("Harvest autologous pericardial patch immediately, fashion a triangular venous conduit under high magnification, and run continuous 10-0 monofilament sutures to restore laminar outflow.", "자가 심낭 패치를 즉시 채취해 고배율 현미경 하에서 삼각형 정맥관을 성형하고, 10-0 단섬유 연속 봉합으로 층류 혈류를 복원하십시오.", "native_killer", "'Autologous pericardial patch'와 '10-0 monofilament sutures'는 세계 최고 뇌혈관 외과의의 완벽한 미세 수술 술기입니다."),
                    ("Use household super glue to stick the veins together quickly.", "집에서 쓰는 순간접착제로 혈관을 대충 붙여버립시다.", "wrong_konglish", "혈관 내 혈전을 유발해 1분 만에 환아를 사망시키는 끔찍한 의료 범죄입니다."),
                    ("Give up on twin B and only save twin A to save time.", "시간을 아끼기 위해 쌍둥이 B는 포기하고 A만 살립시다.", "wrong_konglish", "의사의 윤리를 버리고 어린 생명을 살해 방조하는 극악무도한 망언입니다.")
                ]
            },
            {
                "dialogue": "Micro-suture completed! Venous doppler confirms robust biphasic flow in twin B! But twin A's core body temperature is dropping to thirty-three degrees. Hypothermia risk! How do you stabilize the core?",
                "korean": "미세 봉합 완료! 정맥 도플러 초음파상 쌍둥이 B에게서 강력한 2상성 혈류 확인! 하지만 쌍둥이 A의 심부 체온이 33도까지 떨어지고 있어. 저체온증 위험이야! 심부 체온을 어떻게 안정시킬 텐가?",
                "hint": "가온 관류액과 강제 온풍 담요를 가동하고 수혈 팩을 체온과 동일하게 가온 주입한다.",
                "choices": [
                    ("Initiate active internal rewarming: warm irrigation fluid into the craniotomy field, deploy forced-air warming blankets, and run all blood products through inline heaters.", "능동적 내적 재가온을 시작하십시오: 개두술 부위에 따뜻한 관류액을 주입하고, 강제 온풍 담요를 전개하며 모든 혈액 제제를 인라인 히터로 체온에 맞춰 주입하십시오.", "native_killer", "저체온증으로 인한 응고장애를 원천 차단하는 소아 수술 마취 집중치료의 정석입니다."),
                    ("Pour boiling hot water directly onto the baby's open skull.", "아기의 열린 두개골 위에 펄펄 끓는 뜨거운 물을 들이부읍시다.", "wrong_konglish", "뇌 조직을 화상으로 완전히 삶아버리는 엽기적인 살인 행위입니다."),
                    ("Turn on the room air conditioner to freeze the room completely.", "방을 완전히 얼려버리게 에어컨을 강풍으로 틀어버립시다.", "wrong_konglish", "저체온증을 더욱 악화시켜 심정지를 유발하는 자멸적 처신입니다.")
                ]
            },
            {
                "dialogue": "Core temperature thirty-seven! Both craniotomies closed! Both twins are breathing spontaneously on separate gurneys! Twenty-eight hours on our feet, and two separate lives begin today. You did it, Derek.",
                "korean": "심부 체온 37도 정상 회복! 두 아이 모두 두개골 봉합 완료! 두 쌍둥이가 각자의 이동 침대 위에서 자발호흡 중이야! 28시간 동안 서서 수술한 끝에, 오늘 두 개의 독립된 생명이 시작되었네. 자네가 해냈어, 데릭.",
                "hint": "생명 탄생의 기적을 일궈낸 외과의로서의 숭고한 눈물과 경외감.",
                "choices": [
                    ("Two separate cribs, two bright futures. Thank you to every nurse, anesthesiologist, and surgeon on this team. Let us walk out and give two healthy babies back to their mother.", "두 개의 침대, 두 개의 눈부신 미래. 이 팀의 모든 간호사, 마취과 의사, 외과의들에게 경의를 표합니다. 이제 밖으로 나가 두 건강한 아기를 어머니 품에 안겨드립시다.", "native_killer", "'Grey's Anatomy' 역사상 가장 아름다운 구명의 순간을 완성하는 최고의 감동입니다."),
                    ("I want to go to a bar and drink until I pass out on the floor!", "이제 술집 가서 바닥에 대자로 뻗을 때까지 만취해야지!", "wrong_konglish", "숭고한 28시간 수술 직후 프로 의식 없는 방탕함을 드러내는 언사입니다."),
                    ("Thank you Derek, standing for 28 hours gave me swollen feet.", "감사합니다 데릭, 28시간 서 있었더니 발이 퉁퉁 부었네요.", "mediocre", "의학사에 길이 남을 기적의 감격치고는 너무 시시한 육체적 불평입니다.")
                ]
            }
        ],
        "key_expr": "Autologous pericardium / Two bright futures",
        "key_note": "'Autologous pericardium'은 환자 자신의 심낭 조직을 이용한 무거부 반응 재건, 'Two bright futures'는 두 생명의 독립된 미래를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 85: Dating (멧 갈라 레드카펫 세기의 프러포즈)
    # -------------------------------------------------------------
    {
        "ep_num": 85,
        "title": "멧 갈라 레드카펫: 전 세계 생중계 세기의 프러포즈",
        "genre": "Dating",
        "speaker": "Chuck Bass (Billionaire Real Estate Tycoon)",
        "emoji": "🥂",
        "synopsis": "뉴욕 메트로폴리탄 미술관 멧 갈라 계단 레드카펫. 전 세계 5억 명이 시청하는 글로벌 패션 행사 라이브 카메라 앞에서, 10년간의 엇갈림 끝에 뉴욕 사교계의 제왕이 해리 윈스턴 30캐럿 에메랄드 컷 다이아몬드 반지를 들고 한쪽 무릎을 꿇는다.",
        "turns": [
            {
                "dialogue": "Five hundred cameras flashing, every monarch and movie star in the world watching. Ten years of running, fighting, and losing each other ends right here on these stairs. Blair Waldorf, are you going to keep conquering the world alone, or conquer it with me?",
                "korean": "500대의 카메라가 터지고, 세상의 모든 왕족과 영화배우가 지켜보고 있어. 10년간 도망치고 싸우고 서로를 잃어버렸던 시간은 바로 이 계단 위에서 끝나는 거야. 블레어 월도프, 앞으로도 세상을 혼자 정복할 텐가, 아니면 나와 함께 정복할 텐가?",
                "hint": "화려한 스포트라이트 속에서도 두 사람만의 깊은 영혼의 서사를 확인하며 화답한다.",
                "choices": [
                    ("Conquering the world was always meaningless without you beside me, Chuck. You are my home, my equal, and my only destiny. Yes, a thousand times yes.", "당신이 곁에 없다면 세상을 정복하는 것도 언제나 무의미했어, 척. 당신은 내 안식처이자 내 대등한 짝이며 내 유일한 운명이야. 백 번이고 천 번이고, 예스야.", "native_killer", "'Gossip Girl'의 척과 블레어의 10년 대서사를 영원한 승리로 장식하는 완벽한 눈물의 프러포즈 수락입니다."),
                    ("Give me the diamond ring first so I can test if it's real with a knife.", "진짜 다이아인지 칼로 긁어보게 반지부터 내 손에 쥐여줘 봐요.", "wrong_konglish", "전 세계 생중계 앞에서 속물적인 천박함을 드러내는 최악의 반응입니다."),
                    ("I am embarrassed, please stand up and don't make a scene.", "창피하니까 제발 일어나서 소란 좀 피우지 마세요.", "mediocre", "세기의 로맨틱한 순간에 찬물을 끼얹는 무미건조한 거절입니다.")
                ]
            },
            {
                "dialogue": "The crowd gasped, then roared into cheers! The ring is on your finger, flawless and eternal. But the Met Gala security chief whispers that the paparazzi barricade is collapsing under the mob. How do we make our grand exit?",
                "korean": "관중들이 숨을 죽이더니, 우레와 같은 환호성을 터뜨렸어! 완벽하고 영원한 반지가 당신 손가락에 끼워졌네. 하지만 멧 갈라 보안 책임자가 군중에 파파라치 바리케이드가 무너지고 있다고 귓속말해. 어떻게 위대한 퇴장을 할 텐가?",
                "hint": "혼란에 휩쓸리지 않고, 클래식 롤스로이스와 전용 헬기를 연계한 영화 같은 퇴장으로 전설을 완성한다.",
                "choices": [
                    ("Take my hand, Chuck. We walk down the grand steps through the spotlight, into the vintage Rolls-Royce, and take off into the Manhattan skyline.", "내 손을 잡아요, 척. 스포트라이트를 받으며 저 웅장한 계단을 함께 걸어 내려가 클래식 롤스로이스를 타고 맨해튼 스카이라인 속으로 날아오릅시다.", "native_killer", "할리우드 영화의 엔딩 크레디트를 장식하는 가장 스타일리시하고 눈부신 퇴장 연출입니다."),
                    ("Crawl on your hands and knees through the bushes to hide.", "수풀 속으로 네 발로 기어서 몰래 숨어서 도망칩시다.", "wrong_konglish", "드레스를 찢어먹고 멧 갈라의 여왕에서 노숙자 꼴로 전락하는 추태입니다."),
                    ("Throw the shoes at the photographers and scream angrily.", "사진기자들을 향해 하이힐을 집어던지며 꽥꽥 소리를 지릅시다.", "wrong_konglish", "세계적인 패션 축제에서 폭력 사태를 일으키는 상스러운 행동입니다.")
                ]
            },
            {
                "dialogue": "The Rolls-Royce door closed! Manhattan fireworks erupted over Central Park! The headlines are already printed: 'The Royal Wedding of New York.' We own eternity, my queen.",
                "korean": "롤스로이스 문이 닫혔어! 센트럴파크 상공으로 맨해튼 축하 불꽃놀이가 터졌네! 조간 헤드라인이 이미 인쇄되었어: '뉴욕의 세기의 로열 웨딩.' 우리는 영원을 거머쥐었소, 나의 여왕이여.",
                "hint": "영원한 사랑과 왕좌를 동시에 차지한 뉴욕 최고의 여왕다운 클로징.",
                "choices": [
                    ("You and me against the world, Chuck. Always have been, always will be. Drive into the dawn.", "세상에 맞서는 당신과 나, 척. 언제나 그래왔고, 앞으로도 영원히 그럴 거야. 새벽을 향해 달려요.", "native_killer", "'Gossip Girl'의 영원한 불멸의 엔딩을 선사하는 가장 가슴 벅찬 마침표입니다."),
                    ("I want to sleep for three days straight, wake me up next week.", "나 사흘 내리 잠만 잘 테니까 다음 주에 깨워줘요.", "wrong_konglish", "환상적인 로맨스의 여운을 잠투정으로 날려버리는 아쉬운 소리입니다."),
                    ("Thank you Chuck, that was quite a loud party.", "감사합니다 척, 참 시끄러운 파티였네요.", "mediocre", "세기의 로맨스 결말치고는 감정이 결여된 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "You and me against the world / Royal Wedding",
        "key_note": "'You and me against the world'는 세상 모든 역경에 맞서는 불멸의 연인, 'Royal Wedding'은 사교계 최고의 결혼식을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 86: Wall Street (세기의 공매도 100년 만의 글로벌 금융위기 예견)
    # -------------------------------------------------------------
    {
        "ep_num": 86,
        "title": "세기의 공매도: 100년 만의 글로벌 금융위기 예측",
        "genre": "Wall Street",
        "speaker": "Bobby Axelrod (Macro Trading Titan)",
        "emoji": "📈",
        "synopsis": "뉴욕 월스트리트 최상층 펜트하우스 트레이딩 룸. 서브프라임 모기지 채권 붕괴와 리만 브라더스 파산을 앞둔 2008년 전야. 전 세계 투자은행들이 호황에 취해 있을 때, 금융 시스템의 전면적 파멸을 내다보고 20억 달러 신용부도스왑(CDS) 쇼트 포지션을 걸어놓은 결전의 날이 밝아온다.",
        "turns": [
            {
                "dialogue": "The rating agencies are still giving triple-A ratings to subprime junk! Our carrying cost on the credit default swaps is burning five million dollars a day! The partners want to close the position and cut our losses. Do we pull out or hold the short?!",
                "korean": "신용평가사들은 여전히 서브프라임 쓰레기 채권에 AAA 등급을 매기고 있어! 신용부도스왑(CDS) 유지 프리미엄 비용으로 하루에 5백만 달러씩 타들어가고 있네! 파트너들은 포지션을 정리하고 손절하자고 난리야. 뺄 텐가, 쇼트를 버틸 텐가?!",
                "hint": "신용평가사들의 사기와 모기지 연체율의 기하급수적 폭증 데이터를 제시하며 포지션을 오히려 확대한다.",
                "choices": [
                    ("Hold the short and double down. The sixty-day delinquency rate just breached eight percent; the AAA ratings are a fraudulent facade and the entire domino falls in forty-eight hours.", "쇼트 포지션을 유지하고 2배로 포지션을 늘리십시오. 60일 연체율이 방금 8%를 돌파했습니다; AAA 등급은 사기성 가면일 뿐이며 48시간 안에 도미노 전체가 무너집니다.", "native_killer", "'The Big Short'의 마이클 버리와 마크 바움을 능가하는 완벽한 매크로 분석과 강철 심장의 베팅입니다."),
                    ("Sell everything and apologize to the banks for betting against America.", "전부 매도하고 미국 경제를 상대로 내기를 걸어 죄송하다고 은행에 사과합시다.", "wrong_konglish", "월가의 시스템적 사기를 간파하고도 스스로 굴복하는 비참한 패착입니다."),
                    ("Call a fortune teller to see if the stock market will crash.", "주식 시장이 폭락할지 점쟁이한테 전화해서 물어봅시다.", "wrong_konglish", "월가 최정상 헤지펀드에서 미신을 들먹이는 어처구니없는 발언입니다.")
                ]
            },
            {
                "dialogue": "Lehman Brothers just declared Chapter 11 bankruptcy! Credit freeze across the globe! Investment bank shares are down ninety percent! The counterparties are begging to settle our CDS for pennies on the dollar. How do you cash out?",
                "korean": "리만 브라더스가 연방 파산법 제11조 파산을 선언했어! 전 세계 신용 경색 발발! 투자은행 주가가 90% 폭락했네! 거래 상대방 은행들이 우리 CDS를 헐값에 합의해달라고 애걸복걸하고 있어. 어떻게 현금화할 텐가?",
                "hint": "금융 붕괴 속에서 연방준비제도(Fed) 보증을 요구하며 액면가 100% 전액 현금 청산을 관철한다.",
                "choices": [
                    ("No discounts. Demand full par-value settlement backed by Federal Reserve emergency discount window liquidity, or we seize their prime commercial real estate collateral.", "한 푼의 할인도 없습니다. 연방준비제도 긴급 할인창구 유동성이 보증하는 액면가 100% 전액 청산을 요구하고, 불응 시 프라임 상업용 부동산 담보를 압류하십시오.", "native_killer", "'The Big Short'의 마크 바움이 월가의 탐욕스러운 은행들을 응징할 때 보여주는 냉혹한 카운터펀치입니다."),
                    ("Forgive all their debts because bankers look so sad today.", "은행원들이 오늘 너무 슬퍼 보이니까 그들의 빚을 전액 탕감해 줍시다.", "wrong_konglish", "수조 원의 합법적 수익을 감상주의로 헌납하는 자선사업가 흉내입니다."),
                    ("Accept payment in Monopoly paper money instead of real cash.", "진짜 현금 대신 부루마블 게임 머니로 받겠다고 합시다.", "wrong_konglish", "금융의 기본을 모르는 유아적이고 황당무계한 소리입니다.")
                ]
            },
            {
                "dialogue": "Settlement cleared! Four billion seven hundred million dollars wired into our treasury! The biggest macro short in the history of Wall Street! You foresaw the crash that blinded the world.",
                "korean": "청산 완료! 국고 계좌로 47억 달러 전액 송금 확인! 월스트리트 역사상 최대 규모의 매크로 공매도 성공! 전 세계가 눈먼 금융위기를 자네 홀로 예견했네.",
                "hint": "거대한 승리 앞에서도 금융 시스템 붕괴로 고통받을 서민들을 기억하는 지적인 무게감.",
                "choices": [
                    ("We were right, Bobby, but remember: ordinary families will pay the price for Wall Street's greed. Do not dance. Secure our liquidity and prepare to rebuild.", "우리가 옳았습니다, 바비. 하지만 기억하십시오: 월가의 탐욕에 대한 대가는 평범한 서민들이 치르게 될 것입니다. 춤추지 마십시오. 유동성을 지키고 재건을 준비합시다.", "native_killer", "'The Big Short'의 브래드 피트의 명대사 'Just don't dance'를 오마주한 가장 깊이 있고 도덕적인 월가 피날레입니다."),
                    ("Let's dance in the street and throw champagne at poor people!", "길거리에서 춤추며 가난한 사람들한테 샴페인이나 뿌리자!", "wrong_konglish", "역사적 비극 앞에서 악마적 오만함을 드러내는 최악의 망동입니다."),
                    ("Thank you Bobby, shorting stocks is very exciting.", "감사합니다 바비, 공매도는 참 짜릿하네요.", "mediocre", "세계 금융위기의 비극과 무게감을 전혀 담아내지 못한 가벼운 소감입니다.")
                ]
            }
        ],
        "key_expr": "Credit default swap / Just don't dance",
        "key_note": "'Credit default swap (CDS)'는 채무 불이행 위험을 거래하는 파생상품, 'Just don't dance'는 타인의 불행으로 번 돈 앞에서 춤추지 말라는 금융 윤리입니다."
    },
    # -------------------------------------------------------------
    # EP 87: Tech (전 인류 뉴럴 인터페이스 공개 키노트)
    # -------------------------------------------------------------
    {
        "ep_num": 87,
        "title": "전 인류 뉴럴 인터페이스: 스티브 잡스 스타일 역사적 키노트",
        "genre": "Tech",
        "speaker": "Steve Jobs (Iconic Tech Visionary)",
        "emoji": "💻",
        "synopsis": "샌프란시스코 모스콘 센터 메인 강당. 전 세계 10억 명이 시청하는 애플 스페셜 이벤트 무대. 휠체어에 앉은 마비 환자가 생각만으로 피아노를 연주하는 차세대 비침습 뉴럴 인터페이스 '뉴로링크 원'의 실시간 시연을 3분 앞두고 마지막 키노트 리허설을 마친다.",
        "turns": [
            {
                "dialogue": "Every once in a while, a revolutionary product comes along that changes everything. Mac in 1984, iPhone in 2007. Tonight, we introduce direct thought synthesis. Are you going to read bullet points on slides, or are you going to show them magic?",
                "korean": "이따금 모든 것을 바꾸어놓는 혁명적인 제품이 세상에 나옵니다. 1984년의 매킨토시, 2007년의 아이폰처럼 말입니다. 오늘 밤, 우리는 생각 직결 합성 기술을 선보입니다. 슬라이드의 글머리 기호나 읽을 텐가, 아니면 저들에게 마법을 보여줄 텐가?",
                "hint": "복잡한 하드웨어 스펙 나열 대신, 기술이 인간의 한계를 극복하고 인간성을 회복시키는 마법 같은 감동의 순간을 연출한다.",
                "choices": [
                    ("No slides, Steve. Bring Sarah to the center stage in silence, turn off the podium monitors, and let her mind compose Beethoven's Moonlight Sonata in real time.", "슬라이드는 치우십시오, 스티브. 사라를 무대 중앙으로 조용히 모시고 강연대 모니터를 끈 채, 오직 그녀의 생각만으로 베토벤 월광 소나타를 실시간 연주하게 하십시오.", "native_killer", "스티브 잡스의 전설적인 무대 연출 미니멀리즘과 감동의 정수를 담아낸 최고의 키노트 디렉팅입니다."),
                    ("Read a 500-page engineering manual out loud for two hours.", "두 시간 동안 500페이지짜리 엔지니어링 설명서를 큰 소리로 낭독합시다.", "wrong_konglish", "관객 전원을 지루하게 만들어 잠들게 하는 최악의 키노트 프레젠테이션입니다."),
                    ("Tell the audience that the machine doesn't work so go home.", "기계가 고장 났으니 다들 집에 가라고 관객들을 쫓아냅시다.", "wrong_konglish", "세계적인 신제품 발표회를 사기극으로 파탄 내는 무책임한 짓입니다.")
                ]
            },
            {
                "dialogue": "The Moonlight Sonata echoed through the hall! Ten thousand journalists are on their feet crying! But the telecom giants are complaining backstage that thought synthesis bypasses cellular billing. What is our closing 'One More Thing'?",
                "korean": "월광 소나타가 강당에 울려 퍼졌어! 1만 명의 기자들이 기립해 눈물을 흘리고 있네! 하지만 통신 재벌들이 생각 통신이 이동통신 요금제를 우회한다며 백스테이지에서 항의하고 있어. 우리의 마지막 '원 모어 씽(One More Thing)'이 뭔가?",
                "hint": "모든 통신 장벽을 허물고 전 인류에게 오픈 메쉬 뉴럴 프로토콜을 무료로 개방하는 파격적 선언을 한다.",
                "choices": [
                    ("One More Thing: The neural protocol is permanently royalty-free and open to every paralyzed human being on Earth. Technology is nothing without humanity.", "원 모어 씽: 이 뉴럴 프로토콜은 영구히 로열티가 없으며 지구상의 모든 마비 환자들에게 전면 무료 개방됩니다. 인간성이 결여된 기술은 아무것도 아닙니다.", "native_killer", "스티브 잡스의 'One More Thing' 역사상 가장 숭고하고 위대한 박수를 이끌어낼 세기의 명선언입니다."),
                    ("One More Thing: We are charging everyone five thousand dollars a month!", "원 모어 씽: 앞으로 모든 사람에게 매달 500만 원씩 요금을 뜯어낼 겁니다!", "wrong_konglish", "감동의 무대를 천박한 바가지요금 발표로 망쳐버리는 언사입니다."),
                    ("One More Thing: I forgot what I wanted to say, goodbye.", "원 모어 씽: 내가 무슨 말 하려 했는지 까먹었네요, 안녕히 계세요.", "wrong_konglish", "역사적인 키노트의 클라이맥스를 코미디로 끝장내는 어이없는 소리입니다.")
                ]
            },
            {
                "dialogue": "A five-minute standing ovation! Front page of every newspaper on Earth! You didn't just launch a gadget; you restored human connection. Stay hungry, stay foolish, my friend.",
                "korean": "5분간의 기립 박수 갈채! 지구상 모든 신문의 1면을 도배했어! 자네는 단순한 전자기기를 출시한 게 아니야; 인간의 영혼을 연결했네. 늘 갈망하고, 늘 우직하게 살아가게, 친구여.",
                "hint": "스티브 잡스의 불멸의 유산과 함께 기술의 미래를 축복하는 피날레.",
                "choices": [
                    ("We put a dent in the universe tonight, Steve. The magic lives on in every heart that learns to speak again. Thank you.", "오늘 밤 우리는 우주에 지울 수 없는 흔적(Dent in the universe)을 남겼습니다, 스티브. 다시 말을 건네게 된 모든 이들의 심장 속에 마법은 영원할 것입니다. 감사합니다.", "native_killer", "'Put a dent in the universe'와 잡스의 영혼을 기리는 가장 완벽한 테크 드라마의 결말입니다."),
                    ("Now I want to sign autographs and become a movie star!", "이제 사인회 열고 할리우드 영화배우나 해야지!", "wrong_konglish", "위대한 혁명적 키노트 직후 연예인 병에 걸려 체면을 구기는 언사입니다."),
                    ("Thank you Steve, speaking on stage gives me sore feet.", "감사합니다 스티브, 무대에서 말하느라 발바닥이 참 아프네요.", "mediocre", "우주에 흔적을 남긴 세기의 키노트치고는 너무 시시한 반응입니다.")
                ]
            }
        ],
        "key_expr": "Dent in the universe / One More Thing",
        "key_note": "'Dent in the universe'는 우주에 지울 수 없는 혁신의 흔적을 남기다, 'One More Thing'은 스티브 잡스의 시그니처 깜짝 발표입니다."
    },
    # -------------------------------------------------------------
    # EP 88: FBI (세기의 체포 작전: FBI 10대 지명수배 총책 검거)
    # -------------------------------------------------------------
    {
        "ep_num": 88,
        "title": "세기의 체포 작전: FBI 10대 지명수배 총책 검거",
        "genre": "FBI",
        "speaker": "Agent Miller (FBI Supervisory Special Agent)",
        "emoji": "🔍",
        "synopsis": "마이애미 비스케인 만 초호화 요트 하버. 20년간 수사망을 피해 온 FBI 10대 지명수배 1순위 국제 무기 밀매 신디케이트 총책이 전용 헬기로 남미 탈출을 시도하는 카운트다운 10분 전, 육해공 입체 작전으로 생포해야 한다.",
        "turns": [
            {
                "dialogue": "Helicopter blades are spinning on the yacht's helipad! The target has fifty heavily armed mercenaries and three surface-to-air stingers! Hostage Rescue Team is four nautical miles out. Do we wait for gunboats or assault immediately?",
                "korean": "요트 헬리패드에서 헬기 로터가 돌기 시작했어! 타깃은 중무장 용병 50명과 스팅어 지대공 미사일 3기를 보유하고 있네! 해상 인질구출팀은 4해리 밖에 있어. 경비정을 기다릴 텐가, 즉각 강습할 텐가?",
                "hint": "헬기 이륙 시 영구 탈출하므로, 저격팀으로 헬기 테일 로터를 무력화하고 해상 침투조를 투입한다.",
                "choices": [
                    ("Take the shot: have our sniper disable the helicopter tail-rotor gearbox with a .50-caliber anti-material round, then board via high-speed interceptor ribs under cover of darkness.", "저격을 승인하십시오: 50구경 대물저격총으로 헬기 테일 로터 기어박스를 즉각 무력화한 뒤, 칠흑 같은 어둠을 틈타 고속 단정으로 선체에 강습 승선하십시오.", "native_killer", "'Anti-material round'와 해상 특수작전 기동은 타깃의 도주를 완벽히 봉쇄하는 FBI HRT의 최고봉 전술입니다."),
                    ("Wave your flashlight at the helicopter and ask them to wait for us.", "헬기를 향해 손전등을 흔들며 우리 올 때까지 기다려달라고 부탁합시다.", "wrong_konglish", "적 용병들에게 기관총 표적을 제공하고 몰살당하는 어리석은 짓입니다."),
                    ("Jump into the ocean and try to swim four miles by hand.", "바다로 뛰어들어 맨몸으로 4마일을 헤엄쳐 가봅시다.", "wrong_konglish", "상어 밥이 되거나 익사하여 임무를 완전히 망치는 미련한 행동입니다.")
                ]
            },
            {
                "dialogue": "Helicopter disabled! Assault team breached the main deck! But the kingpin retreated to the titanium panic room with a dead-man's switch detonator wired to forty pounds of C-4! He gives us sixty seconds to disarm or he sinks the yacht!",
                "korean": "헬기 무력화 완료! 강습팀 메인 갑판 진입! 하지만 보스가 C-4 폭약 40파운드와 연결된 데드맨 스위치를 쥐고 티타늄 패닉룸으로 후퇴했어! 60초 안에 무장해제하지 않으면 요트를 자폭 침몰시키겠대!",
                "hint": "데드맨 스위치 수신 주파수를 휴대용 RF 전파방해기로 즉각 교란 차단한 뒤 기습 섬광 돌입한다.",
                "choices": [
                    ("Jam the radio detonator frequency with our portable military ECM jammer, then breach the hydraulic door with thermal breaching tape to subdue him non-lethally.", "휴대용 군용 전파방해기(ECM)로 기폭 무선 주파수를 즉각 차단하고, 열선 브리칭 테이프로 유압 도어를 절단해 비살상 제압하십시오.", "native_killer", "자폭 테러 스위치를 과학적으로 무력화하고 타깃을 생포하는 최정예 대테러 수칙입니다."),
                    ("Tell him to go ahead and blow everyone up right now.", "어디 한번 다 같이 날아가게 지금 당장 스위치 눌러보라고 배짱부립시다.", "wrong_konglish", "요트 폭발로 팀원 전체를 순직시키는 최악의 무모함입니다."),
                    ("Run back to the boat and leave the hostages behind.", "요트에서 뛰어내려 인질들을 버려두고 혼자 도망칩시다.", "wrong_konglish", "FBI 요원의 명예를 시궁창에 버리는 비겁한 직무 유기입니다.")
                ]
            },
            {
                "dialogue": "Detonator jammed! Suspect pinned to the deck in zip-ties! All fifty mercenaries disarmed! The Top Ten Most Wanted syndicate is officially dismantled! Miller salutes you, agent. You wrote FBI history.",
                "korean": "기폭 장치 교란 차단 성공! 용의자 갑판에 포박 제압 완료! 용병 50명 전원 무장해제! FBI 10대 지명수배 카르텔이 공식 해체되었네! 밀러 요원이 자네에게 경례하네. 자네가 FBI의 역사를 썼어.",
                "hint": "20년간의 추적을 완수한 전설적인 수사관의 명예로운 보고.",
                "choices": [
                    ("Fidelity, Bravery, Integrity. The fugitive is in federal custody; justice never forgets and never sleeps. Notify the Director: case closed.", "충성, 용기, 진실(FBI 모토). 도망자는 연방 구금 하에 있습니다; 정의는 결코 잊지 않으며 잠들지 않습니다. 국장님께 보고하십시오: 사건 종결.", "native_killer", "FBI의 공식 모토와 수사의 완결을 선언하는 가장 품격 있고 감동적인 피날레입니다."),
                    ("Now I want to take a selfie with the handcuffs and post it online!", "수갑 찬 보스랑 셀카 찍어서 인스타그램에 올려야지!", "wrong_konglish", "연방 수사관의 보안 수칙과 품위를 망치는 철없는 언사입니다."),
                    ("Thank you Agent Miller, chasing criminals is very tiring.", "감사합니다 밀러 요원님, 범인 쫓기는 참 피곤하네요.", "mediocre", "세기의 범죄 조직을 소탕한 영웅의 소감치고는 너무 무미건조합니다.")
                ]
            }
        ],
        "key_expr": "Dead-man's switch / Case closed",
        "key_note": "'Dead-man's switch'는 사망 시 자동으로 폭발하는 스위치, 'Case closed'는 수사가 완벽히 종결되었음을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 89: Politics (국정연설 State of the Union 최종 퇴고)
    # -------------------------------------------------------------
    {
        "ep_num": 89,
        "title": "국정연설(State of the Union): 역사에 남을 마지막 퇴고",
        "genre": "Politics",
        "speaker": "President of the United States (POTUS)",
        "emoji": "🏛️",
        "synopsis": "워싱턴 D.C. 국회의사당 하원 의장실 뒤 비밀 대기실. 상하원 합동회의 및 전 세계 생중계 국정연설(State of the Union) 입장 15분 전, 국가적 경제 위기와 해외 전쟁 위협 속에서 국민을 하나로 결집할 마지막 결론 문단을 두고 대통령과 수석 연설문 작성관이 고뇌한다.",
        "turns": [
            {
                "dialogue": "Ten minutes before I walk down that aisle and face the joint session of Congress. The partisan knives are sharpened on both sides. Do we deliver a laundry list of policy bills, or do we summon the soul of the nation?",
                "korean": "본회의장 중앙 통로로 걸어나가 의회 합동회의를 대면하기까지 10분 남았소. 양당의 정쟁 칼날이 시퍼렇게 갈려 있소. 정책 법안들의 빨랫줄 목록이나 읽어줄 거요, 아니면 국가의 영혼을 일깨울 거요?",
                "hint": "당리당략에 치우친 정책 나열을 과감히 쳐내고, 위기 속에서 분열을 치유할 위대한 건국 정신과 희망을 설파한다.",
                "choices": [
                    ("Summon the soul, Mr. President. Delete the policy bullet points. Remind America that our union is strong not because we have no challenges, but because we refuse to let fear define our destiny.", "영혼을 일깨우십시오, 대통령님. 정책 조항들은 과감히 삭제하십시오. 우리의 연방이 강대한 이유는 도전이 없어서가 아니라, 공포가 우리의 운명을 규정하도록 결코 용납하지 않기 때문임을 상기시키십시오.", "native_killer", "'State of the Union is strong'의 정수를 꿰뚫는 백악관 수석 연설문 작가의 위대한 문장입니다."),
                    ("Tell the congressmen that they are all useless and throw the speech away.", "의원들에게 당신들은 다 쓸모없는 자들이라고 욕하고 원고를 찢어버립시다.", "wrong_konglish", "의회 합동회의에서 탄핵을 자초하고 국정을 파탄 내는 최악의 망동입니다."),
                    ("Talk about how delicious the White House chef's soup was today.", "오늘 백악관 주방장이 끓여준 수프가 얼마나 맛있었는지 자랑합시다.", "wrong_konglish", "국가 지도자의 국정연설을 일기장 수다로 격하시키는 어처구니없는 발언입니다.")
                ]
            },
            {
                "dialogue": "Five minutes! The Sergeant at Arms is preparing to announce: 'Mr. Speaker, the President of the United States!' What is the final line you want me to leave in the history books tonight?",
                "korean": "5분 전! 의회 경위관이 문을 두드리며 선포할 준비를 하고 있소: '하원의장님, 미합중국 대통령이 입장하십니다!' 오늘 밤 역사책에 영원히 남길 마지막 문장이 뭐요?",
                "hint": "자유와 번영의 횃불이 다음 세대로 영원히 타오를 것임을 선포한다.",
                "choices": [
                    ("Let history record: in the crucible of our doubts, we did not falter, we did not surrender, and the beacon of American liberty burned brighter than ever before. God bless America.", "역사에 기록되게 하십시오: 의구심의 도가니 속에서도 우리는 흔들리지 않았고, 굴복하지 않았으며, 미국의 자유의 횃불은 그 어느 때보다 찬란하게 타올랐다고. 신이여 미국을 축복하소서.", "native_killer", "의회 전체의 기립 박수를 이끌어낼 세기의 연설 클로징입니다."),
                    ("I am tired now, so everyone go home and drink beer.", "이제 피곤하니까 다들 집에 가서 맥주나 마십시다.", "wrong_konglish", "국정연설의 엄중함을 술주정으로 끝장내는 황당한 소리입니다."),
                    ("Vote for my party next year so I can keep this nice house.", "이 좋은 백악관에 계속 살 수 있게 내년에 우리 당에 표나 주세요.", "wrong_konglish", "국정연설을 사적 정쟁 선거운동으로 전락시키는 부끄러운 언사입니다.")
                ]
            },
            {
                "dialogue": "The chamber erupted into a five-minute standing ovation from both sides of the aisle! The Speaker gave a nod of respect. You didn't just write a speech, my friend; you united a fractured nation.",
                "korean": "본회의장 양당 의원석 전체에서 5분간의 기립 박수가 터져 나왔소! 하원의장도 경의의 고개를 끄덕였소. 자네는 단순한 연설을 쓴 게 아니야; 분열된 국가를 하나로 묶어냈네.",
                "hint": "국민과 역사를 섬긴 연설문 작성관의 깊은 긍지와 겸손.",
                "choices": [
                    ("The words belong to the people, Mr. President. It is an honor to serve the Republic and give voice to its highest ideals. May our union endure forever.", "그 말씀들은 국민의 것입니다, 대통령님. 공화국을 섬기고 그 가장 고귀한 이상에 목소리를 부여할 수 있어 영광이었습니다. 우리 연방이 영원히 번영하기를.", "native_killer", "'The West Wing'의 토비 지글러를 연상시키는 가장 품격 있고 감동적인 백악관 피날레입니다."),
                    ("Now I want to run for President myself and kick you out!", "이제 내가 직접 대통령에 출마해서 당신을 쫓아내야지!", "wrong_konglish", "국가적 승리 직후 오만방자하게 선을 넘는 배신자의 언사입니다."),
                    ("Thank you Mr. President, typing speeches gives me finger cramps.", "감사합니다 대통령님, 연설문 치느라 손가락에 쥐가 났네요.", "mediocre", "역사에 남을 국정연설의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "State of the Union / Beacon of liberty",
        "key_note": "'State of the Union'은 미합중국 대통령의 연두 국정연설, 'Beacon of liberty'는 자유의 횃불을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 90: Culinary (월드 베스트 50 레스토랑 1위 등극과 미슐랭 3스타)
    # -------------------------------------------------------------
    {
        "ep_num": 90,
        "title": "미식의 정점: 월드 베스트 1위 등극과 미슐랭 3스타",
        "genre": "Culinary",
        "speaker": "Chef Marco (World's Best Master Chef)",
        "emoji": "🔪",
        "synopsis": "스페인 발렌시아 월드 베스트 50 레스토랑 갈라 어워즈. 전 세계 최고의 스타 셰프 1,000명이 지켜보는 가운데, 세계 1위 레스토랑 트로피 수락 연설을 위해 무대로 올라가기 직전, 거친 주방의 흉터와 땀방울을 되돌아본다.",
        "turns": [
            {
                "dialogue": "They called our name! Number one in the world! Ten years ago we were scrubbing burnt pots in a windowless basement with thirty dollars in our bank account. What do you say to the culinary world tonight, chef?",
                "korean": "우리 이름이 불렸어! 세계 1위! 10년 전 우린 통장에 30달러를 두고 창문도 없는 지하실에서 탄 냄비를 박박 닦고 있었지. 오늘 밤 전 세계 요리계를 향해 뭐라고 말할 텐가, 셰프?",
                "hint": "화려한 명예에 도취되지 않고, 매일 밤 뜨거운 불과 칼 앞에서 묵묵히 땀 흘리는 전 세계 모든 주방 노동자들에게 영광을 돌린다.",
                "choices": [
                    ("Dedicate this trophy to every dishwasher, line cook, and apprentice who burns their hands in the shadows so others can taste magic. Cooking is an act of pure service.", "이 트로피를 어둠 속에서 손을 데어가며 남들에게 마법을 선사하는 전 세계 모든 설거지 담당, 라인 쿡, 견습생들에게 바칩니다. 요리는 순수한 헌신의 행위입니다.", "native_killer", "'The Bear'의 카르미와 앤서니 부르댕의 정신을 잇는 가장 진솔하고 눈물겨운 셰프의 수상 소감입니다."),
                    ("I am a culinary god and all other chefs are trash amateurs!", "난 요리의 신이고 다른 셰프들은 전부 쓰레기 아마추어들이다!", "wrong_konglish", "세계 미식계의 축제에서 오만방자함으로 조롱과 야유를 자초하는 망발입니다."),
                    ("Give me the gold trophy quickly so I can melt it down for cash.", "돈으로 바꾸게 황금 트로피나 빨리 내놓으라고 소리 지릅시다.", "wrong_konglish", "미식계 최고 영예의 무대에서 천박한 탐욕을 드러내는 추태입니다.")
                ]
            },
            {
                "dialogue": "The auditorium rose in tears and applause! Ferran Adrià and Thomas Keller are embracing you! The French press wants our definition of the future of gastronomy. What is your manifesto?",
                "korean": "강당 전체가 눈물과 기립 박수로 화답했어! 페란 아드리아와 토마스 켈러가 자넬 끌어안고 있네! 프랑스 언론이 미식의 미래에 대한 우리 철학을 묻고 있어. 자네의 매니페스토가 뭔가?",
                "hint": "사치와 과시의 파인다이닝을 넘어, 지속 가능한 대지와의 조화와 인간성의 치유를 선언한다.",
                "choices": [
                    ("The future of food is not luxury caviar; it is harmony with our soil, biodiversity, and gathering humanity around the table to heal our broken world.", "미식의 미래는 사치스러운 캐비어가 아닙니다; 그것은 흙과의 조화, 생물다양성 보존, 그리고 식탁 주위에 둘러앉아 상처 입은 세상을 치유하는 것입니다.", "native_killer", "21세기 미식 철학의 가장 높은 지평을 여는 숭고한 매니페스토입니다."),
                    ("The future of food is pill capsules so we never have to cook again.", "요리의 미래는 알약 캡슐이니 다신 요리 안 해도 되는 세상입니다.", "wrong_konglish", "요리사로서 자신의 직업과 음식의 문화를 스스로 부정하는 어리석은 소리입니다."),
                    ("I don't care about the future, I just like eating expensive meat.", "미래 따윈 관심 없고 난 그냥 비싼 고기 처먹는 게 좋습니다.", "wrong_konglish", "세계 1위 셰프의 자격을 의심케 하는 저급한 언사입니다.")
                ]
            },
            {
                "dialogue": "Flashbulbs blinding! Three Michelin stars reaffirmed, World Number One secured! Tonight, you stand on top of Mount Olympus. What is our first order of business tomorrow?",
                "korean": "플래시가 눈부시게 터지고 있어! 미슐랭 3스타 재확인, 월드 넘버원 확정! 오늘 밤, 자네가 올림포스산의 정상에 우뚝 섰네. 내일 아침 우리의 첫 번째 업무가 뭔가?",
                "hint": "영광에 취해 안주하지 않고, 내일 아침 다시 앞치마를 두르고 기본으로 돌아가는 장인 정신.",
                "choices": [
                    ("Sharpen the knives, prep the morning stock, and open our kitchen with the same humility as day one. Let us cook with love. Yes, Chef!", "칼을 갈고 아침 육수를 우리며 첫날의 그 겸손함 그대로 주방 문을 엽시다. 사랑을 담아 요리합시다. 예, 셰프!", "native_killer", "세계 정점에 오른 셰프가 보여주는 최고의 장인 정신과 불멸의 겸손함입니다."),
                    ("I will close the restaurant for five years and party in Ibiza!", "식당 5년 동안 문 닫고 이비자 섬에서 파티나 즐길래요!", "wrong_konglish", "세계 최고 레스토랑의 책임을 저버리고 방탕으로 전락하는 태도입니다."),
                    ("Thank you Marco, holding heavy trophies makes my wrist hurt.", "감사합니다 마르코, 무거운 트로피를 들었더니 손목이 시큰거리네요.", "mediocre", "세계 최고 셰프 등극의 감격치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "Harmony with soil / Mount Olympus",
        "key_note": "'Harmony with soil'은 자연과 공존하는 생태 미식 철학, 'Mount Olympus'는 해당 분야의 최고 정점을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 91: Espionage (세계 평화 협정 비준 극비 망명 완결)
    # -------------------------------------------------------------
    {
        "ep_num": 91,
        "title": "세계 평화 협정 비준: 극비 망명 공작 완결",
        "genre": "Espionage",
        "speaker": "Director of National Intelligence (DNI)",
        "emoji": "🕵️‍♂️",
        "synopsis": "아이슬란드 레이캬비크 호프디 하우스. 신냉전 종식을 선언하는 역사적 핵감축 평화 협정 조인식 당일, 적국 반체제 최고위 관료의 가족을 시베리아 감시망에서 북극해 쇄빙선을 거쳐 서방으로 무사히 구출해내는 CIA 역사상 최대의 엑스필(Exfil) 작전 최종 단계를 지휘한다.",
        "turns": [
            {
                "dialogue": "The defector's family is aboard the submarine off Svalbard, but hostile attack submarines are pinging active sonar twenty nautical miles out! If a torpedo fires, the summit collapses into World War Three. Do we surface under diplomatic escort, or run silent?",
                "korean": "망명자 가족이 스발바르 앞바다 잠수함에 탑승했으나, 적국 공격 원잠이 20해리 밖에서 능동 소나를 쏘며 좁혀오고 있어! 어뢰 한 발이라도 발사되면 정상회담은 제3차 세계대전으로 폭발해. 외교 호위 하에 부상할 텐가, 무소음 잠항할 텐가?",
                "hint": "수온 약층(Thermocline) 아래로 깊이 잠항해 소나를 회피하고 평화 조약 체결 순간까지 적을 기만한다.",
                "choices": [
                    ("Dive beneath the arctic thermocline layer and rig for ultra-quiet running: use bottom topography to ghost their sonar until the peace treaty is formally signed.", "북극 수온 약층 아래로 심도 잠항하고 초무소음 태세로 전환하십시오: 평화 조약이 공식 조인될 때까지 해저 지형을 이용해 적 소나를 유령처럼 따돌려야 합니다.", "native_killer", "'Hunt for Red October'의 정수를 담은 잠수함 음향학적 은폐 기동의 최고봉입니다."),
                    ("Fire all sixteen torpedoes at the enemy submarines immediately.", "적 잠수함을 향해 즉각 16발의 어뢰를 전량 발사합시다.", "wrong_konglish", "평화 회담을 날려버리고 전면 핵전쟁을 일으키는 미친 짓입니다."),
                    ("Surface and wave white flags out of the submarine hatch.", "수면 위로 부상해서 해치 밖으로 백기를 흔들며 항복합시다.", "wrong_konglish", "적에게 나포당하고 망명자 가족을 처형대로 보내는 수치스러운 굴복입니다.")
                ]
            },
            {
                "dialogue": "Sonar ghosted! But the opposing hardliners staged a coup in the capital and are attempting to assassinate their own Premier before he signs the treaty! Our sniper team is on the roof across Hofdi House. Order to protect the Premier?",
                "korean": "소나 따돌리기 성공! 하지만 적국 강경파가 쿠데타를 일으켜 총리가 조약에 서명하기 전에 암살하려 시도 중이야! 우리 저격팀이 회담장 맞은편 지붕에 배치되어 있네. 적국 총리를 보호하기 위해 사격 승인을 내릴 텐가?",
                "hint": "비치사성 교란 사격으로 암살범을 제압하여 타국의 정상과 평화 조약의 역사를 수호한다.",
                "choices": [
                    ("Authorize sniper green light: neutralize the rogue assassin before he breaches the terrace, preserving the Premier's life and the peace of the world.", "저격 승인 그린라이트: 암살범이 테라스를 침투하기 전에 즉각 사살 제압하여, 총리의 목숨과 인류 평화를 지켜내십시오.", "native_killer", "사적인 적대감을 초월해 세계 평화를 수호하는 정예 비밀 요원의 숭고한 결단입니다."),
                    ("Let the Premier be assassinated because he was our enemy anyway.", "어차피 우리 적이었으니 총리가 암살당하게 내버려 둡시다.", "wrong_konglish", "평화 조약을 파기시키고 전 세계를 핵전쟁 참화로 밀어 넣는 최악의 판단입니다."),
                    ("Run onto the stage and steal the golden pen from the table.", "무대로 뛰어나가 테이블 위의 금색 서명 펜을 훔쳐 달아납시다.", "wrong_konglish", "역사적인 평화 협정 현장에서 유치한 절도를 저지르는 정신 나간 짓입니다.")
                ]
            },
            {
                "dialogue": "Assassin down! The pen hit the parchment! Treaty ratified! Nuclear arsenals reduced by eighty percent! The submarine surfaced safely in Reykjavik harbor! You prevented Armageddon, director.",
                "korean": "암살범 제압 완료! 펜이 양피지에 서명되었어! 조약 비준 완료! 핵무기 80% 감축 확정! 잠수함도 레이캬비크 항에 안전하게 부상했네! 자네가 아마겟돈을 막았어, 국장.",
                "hint": "보이지 않는 곳에서 인류를 멸망의 벼랑 끝에서 구출해낸 정보 책임자의 숙연한 자부심.",
                "choices": [
                    ("The greatest intelligence triumph is the war that never happened. Secure the defector, thank our silent operators, and close the mission dossier.", "정보 공작의 가장 위대한 승리는 결코 일어나지 않은 전쟁입니다. 망명자를 안전 보호하고 보이지 않는 요원들에게 감사를 전하며 임무 서류를 종결하십시오.", "native_killer", "'The greatest triumph is the war that never happened'는 첩보 문학의 금자탑을 장식하는 불멸의 명언입니다."),
                    ("Now I want to write a tell-all book and make fifty million dollars!", "이제 폭로 자서전 써서 500억 땡겨야지!", "wrong_konglish", "국가 1급 기밀을 팔아먹는 배신자가 되어 감옥으로 향하는 패착입니다."),
                    ("Thank you Director, submarine operations make me seasick.", "감사합니다 국장님, 잠수함 작전은 뱃멀미가 참 심하네요.", "mediocre", "인류를 구원해낸 숭고한 감격치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "Thermocline stealth / War that never happened",
        "key_note": "'Thermocline'은 음파를 굴절시키는 해수 수온 약층, 'War that never happened'는 전쟁을 미연에 방지한 첩보 요원의 최고 영예를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 92: Aviation (상업 우주선 대기권 재진입 비상사태 생환)
    # -------------------------------------------------------------
    {
        "ep_num": 92,
        "title": "상업 우주선 대기권 재진입: 마하 25 기적의 귀환",
        "genre": "Aviation",
        "speaker": "Commander 'Sully' Miller (Veteran Astronaut)",
        "emoji": "✈️",
        "synopsis": "고도 400km 지구 저궤도에서 귀환 중인 민간 상업 우주선. 대기권 재진입 15분 전, 우측 날개 하부 열 차폐 타일 4장이 우주 쓰레기 충돌로 탈락하며, 섭씨 1,600도의 플라즈마 화염 속에서 기체 붕괴를 막고 모하비 활주로로 무사 생환해야 한다.",
        "turns": [
            {
                "dialogue": "Entry interface in twelve minutes! Plasma heat shield sensor shows thermal tile loss on the right elevon! At Mach twenty-five, atmospheric friction will burn through the aluminum spar! How do you adjust the re-entry angle of attack to survive?!",
                "korean": "12분 뒤 대기권 진입 개시! 플라즈마 열 차폐 센서상 우측 승강타 타일 손실 감지! 마하 25에서 대기 마찰열이 알루미늄 프레임을 녹여버릴 거야! 살아남기 위해 진입 받음각(AoA)을 어떻게 조절할 텐가?!",
                "hint": "손상된 우측 날개를 열기류에서 숨기기 위해 편요각(Yaw)과 롤 뱅크를 반대 방향으로 조작해 플라즈마 바람 그늘을 만든다.",
                "choices": [
                    ("Fly a thirty-eight-degree cross-bank angle of attack: bias our hypersonic roll maneuvers to the port side, shielding the damaged right wing in the aerodynamic wake.", "38도 크로스 뱅크 받음각으로 비행하십시오: 극초음속 롤 기동을 좌측으로 편향시켜 공기역학적 후류 그늘 속에 손상된 우측 날개를 숨겨야 합니다.", "native_killer", "컬럼비아호 참사의 교훈을 극복하는 우주비행사의 최고 난도 극초음속 비행 기동술입니다."),
                    ("Turn the spacecraft around and fly backward into the atmosphere.", "우주선을 180도 뒤집어서 거꾸로 대기권에 처박힙시다.", "wrong_konglish", "우주선이 공기 저항으로 0.1초 만에 산산조각 공중분해 되는 미친 짓입니다."),
                    ("Open the spacecraft emergency window to feel how hot it is.", "얼마나 뜨거운지 손으로 느껴보게 우주선 창문을 열어봅시다.", "wrong_konglish", "진공과 섭씨 1,600도 플라즈마로 즉각 재가 되어 소멸하는 황당한 소리입니다.")
                ]
            },
            {
                "dialogue": "Peak plasma heating survived! But blackout has ended and our automated glide navigation computer fried from electromagnetic ionization! Mojave runway is eighty miles out and we're a fifty-ton glider with zero engines! Can you land her deadstick, Commander?!",
                "korean": "최대 열 플라즈마 구간 돌파! 하지만 통신 두절이 끝났고 자동 활공 항법 컴퓨터가 전자기 이온화로 타버렸어! 모하비 활주로는 80마일 밖이고 우리는 엔진 없는 50톤짜리 글라이더야! 무동력 활공으로 불시착시킬 수 있겠나, 사령관?!",
                "hint": "에너지 관리 기동(HAC) 원을 수동 비행으로 그리며 활주로 중심선에 완벽한 무동력 착륙을 전개한다.",
                "choices": [
                    ("Take manual control of the flight stick. Fly the Heading Alignment Circle visually, manage kinetic energy with speedbrakes, and touch down at two hundred knots on the numbers.", "조종간을 수동 제어로 잡겠습니다. 방위정렬선회원(HAC)을 육안으로 비행하며 스피드브레이크로 운동 에너지를 관리하고, 활주로 번호 위 200노트로 접지하겠습니다.", "native_killer", "우주왕복선 파일럿의 전설적인 무동력 활공 착륙(Deadstick landing)의 진수를 완벽히 구현한 대사입니다."),
                    ("Eject all crew members without parachutes into the desert.", "사막 한가운데로 낙하산도 없이 승무원 전원을 사출시킵시다.", "wrong_konglish", "동료들을 전원 추락사시키는 엽기적이고 패륜적인 행동입니다."),
                    ("Wait until the spaceship stops by itself in the sky.", "우주선이 하늘에서 저절로 멈출 때까지 가만히 기다려봅시다.", "mediocre", "중력과 양력의 물리 법칙을 모르는 초등학생 수준의 발언입니다.")
                ]
            },
            {
                "dialogue": "Wheels down! Main gear touchdown... nose gear down! Drag chute deployed! Stopped on the Mojave runway centerline! All six commercial astronauts alive! You piloted an angel home from orbit, Sully.",
                "korean": "바퀴 접지! 메인 기어 접지... 노즈 기어 접지! 드래그 낙하산 전개! 모하비 활주로 중앙선에 완전 정지! 민간 우주비행사 6명 전원 생환! 자네가 궤도에서 천사를 살려 집으로 데려왔네, 설리.",
                "hint": "우주와 지구를 오가는 비행의 극한에서 인류를 구원한 전설적 파일럿의 긍지.",
                "choices": [
                    ("The vehicle held, the crew is home, and the sky is no longer the limit. Wheel stop confirmed. Let us debrief mission control and hug our families.", "기체는 버텼고, 승무원은 귀환했으며, 하늘은 더 이상 우리의 한계가 아닙니다. 휠 스탑 완료. 관제탑을 디브리핑하고 가족들을 안아줍시다.", "native_killer", "'The sky is no longer the limit'은 우주 항공 드라마의 불멸의 피날레를 장식하는 명문장입니다."),
                    ("Now I am going to sell pieces of the burned spaceship on eBay!", "불탄 우주선 파편 떼어내서 이베이에 팔아서 돈이나 벌어야지!", "wrong_konglish", "기적의 생환 직후 파렴치한 고물 장사꾼 흉내를 내는 언사입니다."),
                    ("Thank you Sully, space travel makes my stomach upside down.", "감사합니다 설리 사령관님, 우주여행은 멀미가 참 심하네요.", "mediocre", "기적의 우주 귀환의 감격을 단순 멀미 투정으로 깎아먹는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Heading Alignment Circle / Deadstick landing",
        "key_note": "'Heading Alignment Circle'은 우주선이 활주로 고도와 속도를 맞추는 나선 선회원, 'Deadstick landing'은 무동력 활공 비상착륙을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 93: Sports Management (명예의 전당 헌액식과 에이전시 계승)
    # -------------------------------------------------------------
    {
        "ep_num": 93,
        "title": "스포츠의 전설: 명예의 전당 헌액과 에이전시의 위대한 계승",
        "genre": "Sports Management",
        "speaker": "Jerry Maguire (Hall of Fame Super-Agent & Founder)",
        "emoji": "🏈",
        "synopsis": "오하이오주 캔턴 프로풋볼 명예의 전당(Pro Football Hall of Fame) 야외 대극장. 30년간 함께 울고 웃었던 선수가 명예의 전당 헌액 수락 연설을 마치고 황금 재킷을 입은 순간, 에이전시의 지휘봉을 차세대 파트너에게 공식 계승하는 감동의 밤이 펼쳐진다.",
        "turns": [
            {
                "dialogue": "Thirty years ago, people laughed when I wrote my mission statement about fewer clients and more personal caring. Tonight, four of our athletes are wearing Hall of Fame gold jackets. Tell me: did we change sports, or did sports change us?",
                "korean": "30년 전, 고객 수를 줄이고 선수 한 명 한 명을 진심으로 보살피자는 선언문을 썼을 때 사람들은 날 비웃었지. 오늘 밤, 우리 선수 4명이 명예의 전당 골드 재킷을 입고 있네. 내게 말해주게: 우리가 스포츠를 바꾼 건가, 아니면 스포츠가 우릴 바꾼 건가?",
                "hint": "단순한 비즈니스 계약 관계를 넘어, 선수의 영혼을 돌보는 진정한 파트너십이 스포츠의 정의를 바꾸었음을 증언한다.",
                "choices": [
                    ("We proved that an agent's greatest contract is written on the human heart, Jerry. You didn't just manage careers; you protected their dignity when the world only saw jerseys.", "에이전트의 가장 위대한 계약서는 인간의 심장 위에 새겨진다는 것을 우리가 증명했습니다, 제리. 당신은 단순히 커리어를 관리한 것이 아니라 세상이 유니폼만 볼 때 그들의 존엄성을 지켜주었습니다.", "native_killer", "'Jerry Maguire'의 철학을 완성하는 눈물겹고 숭고한 최고의 헌사입니다."),
                    ("We made a hundred million dollars, so who cares about feelings?", "우리가 돈을 수천억 벌었는데 마음 따위가 무슨 상관입니까?", "wrong_konglish", "영화 '제리 맥과이어'의 모든 숭고한 메시지를 쓰레기통에 처박는 천박한 언사입니다."),
                    ("I think sports are too violent and people should play chess instead.", "스포츠는 너무 폭력적이니 다들 체스나 둬야 한다고 생각합니다.", "mediocre", "명예의 전당 헌액식 현장에서 찬물을 끼얹는 엉뚱한 발언입니다.")
                ]
            },
            {
                "dialogue": "The athlete points to you from the stage: 'He was my agent, but he was my brother. He showed me the meaning of family.' Jerry tears up and hands you the agency's gold signet ring. 'The firm is yours now, partner. What is your promise to the next generation?'",
                "korean": "선수가 무대에서 자넬 가리켰어: '그는 내 에이전트였지만 내 형제였습니다. 내게 가족의 의미를 가르쳐주었습니다.' 제리가 눈물을 흘리며 에이전시의 황금 인장 반지를 건네네. '이제 이 회사는 자네 거야, 파트너. 다음 세대에게 무엇을 약속할 텐가?'",
                "hint": "돈보다 선수의 인간적 성장과 영혼을 먼저 생각하는 에이전시의 불멸의 원칙을 계승한다.",
                "choices": [
                    ("I promise that no athlete will ever walk alone. We will fight for their contracts, but we will fight twice as hard for their souls. The mission statement endures.", "어떤 선수도 결코 혼자 걷게 하지 않겠다고 약속합니다. 우리는 계약금을 위해 싸우겠지만, 그들의 영혼을 위해 두 배로 치열하게 싸울 것입니다. 우리의 선언문은 영원할 것입니다.", "native_killer", "'Jerry Maguire'의 시그니처 사명 선언문을 완벽하게 계승하는 감동의 피날레입니다."),
                    ("I promise to charge thirty percent commission and become super rich!", "앞으로 수수료 30% 떼어가며 초대형 부자가 되겠다고 약속합니다!", "wrong_konglish", "황금 인장 반지를 받자마자 악덕 에이전트로 흑화하는 부끄러운 언사입니다."),
                    ("I will sell the agency to the highest bidder tomorrow morning.", "내일 아침에 제일 돈 많이 주는 놈한테 회사를 팔아치우겠습니다.", "wrong_konglish", "30년의 위대한 유산을 돈 몇 푼에 팔아넘기려는 배은망덕한 태도입니다.")
                ]
            },
            {
                "dialogue": "The crowd gave a roaring ovation! Fireworks illuminated the Ohio sky! Jerry hugged you tightly. You carried the torch and elevated an entire industry. Show them the heart, champion.",
                "korean": "관중들이 우레와 같은 환호성을 보냈어! 불꽃놀이가 오하이오의 밤하늘을 수놓았네! 제리가 자넬 꼭 껴안았어. 자네가 횃불을 이어받아 스포츠 산업 전체를 한 단계 끌어올렸네. 심장을 보여주게, 챔피언.",
                "hint": "스포츠 에이전트 드라마의 완벽하고 영원한 감동의 피날레.",
                "choices": [
                    ("You had me at hello, Jerry. Let us toast to the legends of yesterday, and welcome the champions of tomorrow. Show them the heart!", "당신을 처음 본 순간부터 난 당신 편이었습니다, 제리(You had me at hello). 어제의 전설들을 위해 축배를 들고 내일의 챔피언들을 맞이합시다. 심장을 보여줘라!", "native_killer", "영화 'Jerry Maguire' 역사상 가장 로맨틱하고 상징적인 불멸의 명대사를 오마주한 최고의 클로징입니다."),
                    ("I want to eat a hot dog now because speeches make me hungry.", "연설 들었더니 배고프니까 핫도그나 사 먹으러 가야지.", "wrong_konglish", "명예의 전당 역사적 감동의 순간을 핫도그로 날려버리는 경박한 태도입니다."),
                    ("Thank you Jerry, football jackets look very heavy.", "감사합니다 제리, 풋볼 재킷은 참 무거워 보이네요.", "mediocre", "명예의 전당 헌액식의 숭고한 감격치고는 너무 시시한 소감입니다.")
                ]
            }
        ],
        "key_expr": "You had me at hello / Written on human heart",
        "key_note": "'You had me at hello'는 첫마디를 건넨 순간부터 당신을 사랑했다는 불멸의 명대사, 'Written on the heart'는 영혼에 새겨진 진정한 계약을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 94: Haute Couture (메트로폴리탄 미술관 회고전 불멸의 레거시)
    # -------------------------------------------------------------
    {
        "ep_num": 94,
        "title": "메트로폴리탄 미술관 회고전: 불멸의 패션 레거시",
        "genre": "Haute Couture",
        "speaker": "Miranda Priestly (Editor-in-Chief & Fashion Icon)",
        "emoji": "👠",
        "synopsis": "뉴욕 메트로폴리탄 미술관 코스튬 인스티튜트 그랜드 오프닝 갈라. 50년간의 패션 역사를 집대성한 당신의 오뜨 꾸뛰르 회고전 '불멸의 실크(Immortal Silk)' 테이프 커팅식 10분 전, 수석 큐레이터실에서 전설적인 패션 여왕과 와인 잔을 기울인다.",
        "turns": [
            {
                "dialogue": "Every design you ever dared to stitch is hanging under these museum lights. Alexander McQueen, Yves Saint Laurent, and now you. Tell me, do you finally feel you have conquered this town, or does the girl who came to interview in cerulean blue still hunger for more?",
                "korean": "자네가 감히 바느질했던 모든 디자인이 이 미술관 조명 아래 걸려 있네. 알렉산더 맥퀸, 이브 생 로랑, 그리고 이제 자네야. 솔직히 말해봐, 드디어 이 도시를 정복한 기분인가, 아니면 세룰리안 블루 스웨터를 입고 면접 보러 왔던 그 소녀는 여전히 더 큰 것을 갈망하는가?",
                "hint": "'악마는 프라다를 입는다'의 세룰리안 블루 스웨터의 초심을 기억하며 진정한 예술적 완성에 대해 답한다.",
                "choices": [
                    ("Conquering is temporary, Miranda; inspiring is eternal. That cerulean sweater taught me that every thread connects to the human heart. Tonight is for every dreamer who sees poetry in fabric.", "정복은 일시적이지만, 영감을 주는 것은 영원합니다, 미란다. 그 세룰리안 스웨터는 모든 실 한 올이 인간의 심장과 연결되어 있음을 제게 가르쳐주었죠. 오늘 밤은 원단 속에서 시를 발견하는 모든 몽상가들을 위한 것입니다.", "native_killer", "'The Devil Wears Prada'의 세룰리안 블루 명장면을 완벽히 오마주하며 예술적 영혼을 찬양하는 최고의 명대사입니다."),
                    ("I conquered this town, now everyone must worship my shoes!", "내가 이 도시를 정복했으니 이제 다들 내 구두를 숭배해야 합니다!", "wrong_konglish", "위대한 회고전의 품격을 저급한 교만으로 짓밟는 언사입니다."),
                    ("Cerulean blue is an ugly color, I hate that old sweater.", "세룰리안 블루는 촌스러운 색이라 그 옛날 스웨터 찢어버리고 싶네요.", "wrong_konglish", "자신의 위대한 커리어의 뿌리를 스스로 부정하는 배은망덕한 소리입니다.")
                ]
            },
            {
                "dialogue": "Miranda paused, and for the first time in thirty years, a gentle tear formed in her eye. She whispered: 'That's not entirely terrible.' The doors are opening to five thousand international dignitaries. What is your ribbon-cutting statement?",
                "korean": "미란다가 말을 멈추더니, 30년 만에 처음으로 눈에 부드러운 눈물이 맺혔네. 그녀가 속삭였어: '완전히 형편없진 않군.' 세계 각국 귀빈 5천 명을 향해 문이 열리고 있어. 자네의 테이프 커팅 기념사가 뭔가?",
                "hint": "패션이란 껍데기가 아닌 인간의 존엄과 용기를 입는 행위임을 선언한다.",
                "choices": [
                    ("Clothes do not simply clothe the body; they armor the spirit. May this exhibition remind us that courage, elegance, and vision can never go out of style.", "옷은 단순히 몸을 가리는 것이 아니라, 영혼을 무장시키는 갑옷입니다. 용기와 우아함, 그리고 비전은 결코 유행을 타지 않는다는 것을 이 회고전이 증명하기를.", "native_killer", "'Vision never goes out of style'은 세계 패션사에 영원히 기록될 명문장입니다."),
                    ("Buy my clothes so I can buy another private island in Hawaii!", "하와이에 개인 섬 하나 더 사게 내 옷이나 많이들 사 입으세요!", "wrong_konglish", "예술 전시회를 저급한 호객 행위로 전락시키는 부끄러운 언사입니다."),
                    ("Cut the ribbon fast because standing on high heels hurts.", "하이힐 신고 서 있기 발 아프니까 테이프나 빨리 자릅시다.", "mediocre", "역사적인 회고전의 숭고함을 단순 발 통증 투정으로 깎아먹는 평범한 소감입니다.")
                ]
            },
            {
                "dialogue": "Scissors clicked, ribbon fell, and applause shook the glass ceilings of The Met! Miranda looked back one last time, nodded respectfully, and whispered: 'That's all.' You are an immortal legend, designer.",
                "korean": "가위가 잘리고, 리본이 떨어지며, 박수갈채가 메트로폴리탄 미술관의 유리 천장을 흔들었어! 미란다가 마지막으로 뒤돌아보며 정중히 고개를 끄덕이고 속삭였네: '이상이야(That's all).' 자네는 불멸의 전설이야, 디자이너.",
                "hint": "미란다 프리슬리의 시그니처 작별 대사를 가슴에 품으며 패션의 전당에 영원히 새겨지는 피날레.",
                "choices": [
                    ("That's all, Miranda. Thank you for showing me that excellence demands our entire soul. The legacy lives on forever.", "이상입니다, 미란다. 탁월함이란 우리 영혼 전체를 바쳐야 하는 것임을 가르쳐주셔서 감사합니다. 우리의 유산은 영원히 살아 숨 쉴 것입니다.", "native_killer", "'That's all'을 미란다에게 되돌려주며 사제지간의 위대한 여정을 완결 짓는 궁극의 피날레입니다."),
                    ("Now I want to eat pizza in my ballgown and get grease on it!", "이제 무도회 드레스 입은 채로 피자 먹고 기름이나 묻혀야지!", "wrong_konglish", "불멸의 전설로 등극한 직후 체면을 완전히 구기는 경박한 행동입니다."),
                    ("Thank you Miranda, making dresses takes too much fabric.", "감사합니다 미란다, 드레스 만드느라 원단이 너무 많이 들었네요.", "mediocre", "세계 미술관에 영구 등재된 감격치고는 너무 시시한 푸념입니다.")
                ]
            }
        ],
        "key_expr": "That's all / Armor the spirit",
        "key_note": "'That's all'은 미란다 프리슬리의 전설적인 종결 명대사, 'Armor the spirit'은 영혼을 무장시키는 패션의 본질을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 95: Crisis PR (글로벌 평화 정상회담 인질 긴급 해제 브리핑)
    # -------------------------------------------------------------
    {
        "ep_num": 95,
        "title": "글로벌 평화 정상회담: 인질 극적 해제와 전 세계 브리핑",
        "genre": "Crisis PR",
        "speaker": "Olivia Pope (World's Premier Crisis Director)",
        "emoji": "🎙️",
        "synopsis": "스위스 제네바 UN 본부 그랜드 프레스 룸. 평화 정상회담장 진입로에서 다국적 테러 단체에 의해 억류되었던 국제 외교 사절단 40명이 무혈 평화 협상으로 전원 구출된 직후, 전 세계 150개국 생방송 카메라 앞에서 역사적 사태 종결 브리핑을 진행한다.",
        "turns": [
            {
                "dialogue": "Forty ambassadors safe, zero shots fired, and the hostile cell surrendered their arms peacefully. The global press corps has been screaming for twelve hours. The red broadcast light is blinking. How do you frame this triumph for history?",
                "korean": "대사 40명 전원 무사 생환, 총성 0발, 무장 테러 조직이 평화롭게 무기를 내려놓았어. 전 세계 기자단이 12시간 내내 비명을 지르며 대기 중이야. 빨간 생방송 등이 깜빡이고 있네. 역사를 위해 이 위대한 승리를 어떻게 브리핑할 텐가?",
                "hint": "단순한 물리적 승리가 아니라, 대화와 인간에 대한 신뢰가 폭력을 이겼음을 천명한다.",
                "choices": [
                    ("Step to the microphones with calm authority: declare that tonight, reason conquered terror, humanity disarmed hatred, and every single soul is coming home to their families.", "침착한 권위로 마이크 앞에 서십시오: 오늘 밤 이성이 공포를 이겼고, 인류애가 증오를 무장해제시켰으며, 모든 영혼들이 가족의 품으로 무사히 돌아가고 있음을 선포하십시오.", "native_killer", "'Scandal'의 올리비아 포프를 전율케 하는 진정한 국가급 위기관리 브리핑의 극치입니다."),
                    ("Call the reporters stupid monkeys and laugh in their faces.", "기자들에게 멍청한 원숭이들이라고 욕하며 얼굴에 대고 비웃읍시다.", "wrong_konglish", "전 세계 생중계에서 전대미문의 언론 폭언을 저지르는 미친 짓입니다."),
                    ("Tell everyone that negotiations are easy and anyone could do it.", "협상이란 건 식은 죽 먹기라 아무나 다 할 수 있는 일이라고 떠벌립시다.", "mediocre", "사투를 벌인 협상가들과 특수요원들의 피땀을 모욕하는 경솔한 태도입니다.")
                ]
            },
            {
                "dialogue": "The briefing stunned the world into silence, then applause broke out in the press gallery! But a hostile reporter shouts: 'Who authorized the backchannel concessions?' What is your ironclad rebuttal?",
                "korean": "브리핑이 전 세계를 숨죽이게 하더니, 기자실에서 박수가 터져 나왔어! 하지만 적대적 기자가 고함을 지르네: '누가 뒷거래 양보를 승인했습니까?' 자네의 철벽같은 반박이 뭔가?",
                "hint": "어떤 불법적 양보도 없었으며, 오직 인간의 존엄성과 도덕적 확신으로 굴복시켰음을 단호히 밝힌다.",
                "choices": [
                    ("Look directly at the reporter: not a single dollar was paid, not a single principle was compromised. We offered them justice under international law, and they accepted our resolve.", "기자를 정면 응시하십시오: 단 1달러도 지급되지 않았고, 단 하나의 원칙도 타협하지 않았습니다. 우리는 국제법에 따른 공정한 사법 정의를 제시했고, 저들은 우리의 단호한 결의에 굴복한 것입니다.", "native_killer", "어떤 음모론도 단칼에 베어버리는 완벽한 팩트와 카리스마의 방패입니다."),
                    ("Throw your shoe at the reporter's head to make him shut up.", "입 닥치게 신발을 벗어서 기자의 머리를 향해 집어던집시다.", "wrong_konglish", "국제 외교 브리핑을 폭력 난투극으로 만드는 상스러운 망동입니다."),
                    ("Stutter and look at your shoes because you don't know what to say.", "할 말이 없어서 말을 더듬으며 바닥 신발만 쳐다봅시다.", "mediocre", "언론의 공격에 위축되어 의혹을 키우는 나약한 처신입니다.")
                ]
            },
            {
                "dialogue": "The reporter sat down in shame. The White House, the Elysée, and Downing Street just issued joint commendations. Olivia Pope takes off her white hat and presents it to you. 'You are the greatest fixer this world has ever seen.'",
                "korean": "기자가 부끄러움에 자리에 앉았네. 백악관, 엘리제궁, 다우닝가가 공동 감사 성명을 발표했어. 올리비아 포프가 자신의 상징인 화이트 햇을 벗어 자네에게 건네네. '자네가 이 세상이 목격한 가장 위대한 해결사야.'",
                "hint": "정의를 수호하는 '화이트 햇(White Hat)'의 전설을 이어받는 감동의 마무리.",
                "choices": [
                    ("It's handled, Olivia. We wear the white hat so the light never goes out. Let us stand down the war room; peace has arrived.", "해결되었습니다, 올리비아(It's handled). 빛이 결코 꺼지지 않도록 우리는 화이트 햇을 씁니다. 이제 워룸을 해제하십시오; 평화가 찾아왔습니다.", "native_killer", "'Scandal'의 상징적인 명대사 'It's handled'와 'White Hat'을 완벽하게 오마주한 감동의 피날레입니다."),
                    ("Now I want to run for Queen of the Universe!", "이제 전 우주의 여왕 자리에 출마해봐야지!", "wrong_konglish", "위대한 위기 수습 직후 황당한 과대망상을 늘어놓는 언사입니다."),
                    ("Thank you Olivia, answering questions gives me a sore throat.", "감사합니다 올리비아, 질문에 대답하느라 목이 참 아프네요.", "mediocre", "세계 평화를 지켜낸 웅장한 순간치고는 너무 시시한 푸념입니다.")
                ]
            }
        ],
        "key_expr": "It's handled / Wear the white hat",
        "key_note": "'It's handled'는 올리비아 포프의 시그니처 해결 완료 선언, 'Wear the white hat'은 정의의 편에서 세상을 지킨다는 상징입니다."
    },
    # -------------------------------------------------------------
    # EP 96: Luxury Real Estate (엠파이어 스테이트 빌딩 매각)
    # -------------------------------------------------------------
    {
        "ep_num": 96,
        "title": "뉴욕의 심장: 엠파이어 스테이트 랜드마크 30억 달러 매각",
        "genre": "Luxury Real Estate",
        "speaker": "Ryan Serhant (Billionaire Real Estate Broker)",
        "emoji": "🏙️",
        "synopsis": "맨해튼 엠파이어 스테이트 빌딩 102층 전망대 자정. 전 세계에서 가장 상징적인 뉴욕의 심장부 랜드마크 빌딩 지분 100% 매각을 두고, 뉴욕시 역사보존기금과 글로벌 컨소시엄의 35억 달러 최종 에스크로 계약 서명식을 10분 앞두고 중개인의 최종 선언을 남긴다.",
        "turns": [
            {
                "dialogue": "Thirty-five billion dollars on the table! The entire skyline of New York is glowing beneath our feet. Both sovereign wealth funds demand that the spire's lighting control belongs to them forever. How do you resolve this cultural sovereignty clash?",
                "korean": "테이블 위에 35억 달러야! 뉴욕의 스카이라인 전체가 우리 발아래서 빛나고 있네. 양측 국부펀드 모두 첨탑 조명 제어권만큼은 영구히 자신들의 소유여야 한다고 버티고 있어. 이 문화 주권 충돌을 어떻게 해결할 텐가?",
                "hint": "첨탑 조명 제어권을 영구 시민 공공 신탁(Public Heritage Trust)으로 귀속시키고 조명권 기부 채납에 따른 막대한 세제 혜택을 설계한다.",
                "choices": [
                    ("Dedicate the tower's spire lighting to a perpetual municipal heritage trust for the people of New York, granting both buyers billions in cultural tax credits while keeping the city's beacon free.", "첨탑 조명권을 뉴욕 시민들을 위한 영구 공공 헤리티지 트러스트에 기부 헌정하고, 양측 매수인에겐 수십억 달러의 문화 공익 세제 혜택을 안겨주어 뉴욕의 등대를 지키십시오.", "native_killer", "뉴욕의 영혼을 지키면서도 상업적 거래를 완결 짓는 슈퍼 브로커의 세기적인 솔루션입니다."),
                    ("Turn off the lights forever so the whole building is pitch black.", "건물 전체가 칠흑처럼 캄캄해지도록 조명을 영원히 꺼버립시다.", "wrong_konglish", "뉴욕의 상징을 유령의 집으로 만들고 시민들의 폭동을 자초하는 미친 짓입니다."),
                    ("Tell both buyers to flip a coin on the windy observation deck.", "바람 부는 전망대에서 동전 던지기로 결정하라고 합시다.", "wrong_konglish", "35억 달러 랜드마크 거래를 길거리 도박 취급하는 황당무계한 행동입니다.")
                ]
            },
            {
                "dialogue": "Brilliant! Both funds signed the public lighting trust! But the title company just flagged an unresolved 1931 air-rights easement from the Chrysler family. The closing deadline is midnight! How do you clear the title in three minutes?",
                "korean": "기막힌 해결책이야! 양측 펀드 모두 공공 조명 신탁에 서명했어! 하지만 타이틀 보험사가 크라이슬러 가문의 1931년 미해결 공중권(Air-rights) 지역권을 발견했네. 클로징 마감은 자정이야! 3분 안에 소유권 하자를 어떻게 해결할 텐가?",
                "hint": "미사용 공중권을 크라이슬러 가문 재단과의 긴급 보상 스왑 및 면책 배서(Title Endorsement)로 완결 짓는다.",
                "choices": [
                    ("Execute an accelerated air-rights quitclaim deed with the Chrysler foundation, backed by our underwriter's five-hundred-million-dollar indemnity bond, clearing the deed immediately.", "크라이슬러 재단과 긴급 공중권 권리 포기 증서를 체결하고, 우리 보험사의 5억 달러 손해배상 보증 배서로 보강하여 소유권 하자를 즉각 완벽 소멸시키십시오.", "native_killer", "'Quitclaim deed'와 'indemnity bond'는 초고난도 상업용 부동산 타이틀 하자를 번개처럼 정리하는 궁극의 법률 기술입니다."),
                    ("Tear down the Chrysler building with a giant wrecking ball tonight.", "오늘 밤 거대한 철거용 쇠구슬로 크라이슬러 빌딩을 부숴버립시다.", "wrong_konglish", "뉴욕의 역사 문화재를 테러로 파괴하고 종신형을 선고받을 망동입니다."),
                    ("Cry and tell the buyers that real estate is too complicated.", "부동산은 너무 복잡하다며 울면서 손을 놔버립시다.", "mediocre", "수천억 수수료를 눈앞에 두고 나약하게 포기하는 한심한 태도입니다.")
                ]
            },
            {
                "dialogue": "Midnight bell chimed! Three point five billion dollars wired! The Empire State Building deed is officially transferred! The spire just lit up in brilliant gold! You sold the heart of New York City, Ryan.",
                "korean": "자정 종이 울렸어! 35억 달러 송금 완료! 엠파이어 스테이트 빌딩 등기 이전 공식 완료! 첨탑이 눈부신 황금빛으로 점등되었네! 자네가 뉴욕시의 심장을 팔았어, 라이언.",
                "hint": "뉴욕 부동산 역사의 전설이 된 슈퍼 브로커의 세련되고 웅장한 클로징.",
                "choices": [
                    ("Concrete jungle where dreams are made of. We didn't just sell steel and stone; we sold the soul of human ambition. Let us toast to the capital of the world.", "꿈이 이루어지는 콘크리트 정글(Empire State of Mind). 우리는 단순한 철골과 돌덩이를 판 것이 아니라 인간 야망의 영혼을 중개했습니다. 세계의 수도를 위해 축배를 듭시다.", "native_killer", "알리샤 키스의 'Empire State of Mind'를 우아하게 녹여낸 맨해튼 최고 슈퍼 브로커의 감동적인 피날레입니다."),
                    ("Now I want to jump off the building with a flying squirrel suit!", "날다람쥐 슈트 입고 이 빌딩 꼭대기에서 뛰어내려 봐야지!", "wrong_konglish", "역사적인 거래 성사 직후 자살 행위를 시도하려는 황당한 소리입니다."),
                    ("Thank you Ryan, high elevators make my ears pop.", "감사합니다 라이언, 높은 엘리베이터는 귀가 멍멍하네요.", "mediocre", "뉴욕 역사상 최대 랜드마크 거래의 감격에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Concrete jungle where dreams are made / Quitclaim deed",
        "key_note": "'Concrete jungle'은 맨해튼을 상징하는 시그니처 표현, 'Quitclaim deed'는 부동산 권리 포기 양도 증서를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 97: Hollywood Agency (아카데미 시상식 작품상·남우주연상 영예)
    # -------------------------------------------------------------
    {
        "ep_num": 97,
        "title": "할리우드의 정점: 아카데미 작품상과 남우주연상 제패",
        "genre": "Hollywood Agency",
        "speaker": "Ari Gold (Hollywood Agency Titan)",
        "emoji": "🎬",
        "synopsis": "로스앤젤레스 돌비 극장 아카데미 시상식 백스테이지 그린룸. 당신의 에이전시 소속 배우와 감독이 11개 부문 후보에 올라 남우주연상과 최우수 작품상 트로피를 휩쓴 순간, 오스카 조각상을 손에 쥔 클라이언트들과 함께 샴페인을 터뜨리며 할리우드의 지배를 선언한다.",
        "turns": [
            {
                "dialogue": "Eleven Oscars! Best Picture! Best Actor! Best Director! The golden statues are glittering in our hands! Steven Spielberg and Martin Scorsese just walked in to raise a glass to us! What do you say to the town that tried to break us?!",
                "korean": "오스카 11개 부문 석권! 작품상! 남우주연상! 감독상! 황금 조각상들이 우리 손에서 반짝이고 있어! 스티븐 스필버그와 마틴 스콜세지가 방금 우리를 위해 축배를 들러 들어왔네! 우리를 무너뜨리려 했던 이 바닥을 향해 뭐라고 선언할 텐가?!",
                "hint": "복수심 대신 위대한 스토리텔링의 승리와 영화 예술의 영원성을 선언한다.",
                "choices": [
                    ("They tried to bury our vision, but they forgot we were seeds. Tonight, cinema belongs to the storytellers who never sold their soul. Drink up, gentlemen; this town belongs to art tonight.", "그들은 우리의 비전을 묻어버리려 했지만, 우리가 씨앗이라는 사실을 잊었습니다. 오늘 밤, 시네마는 영혼을 팔지 않은 이야기꾼들의 것입니다. 마십시다, 신사 여러분; 오늘 밤 이 도시는 예술의 것입니다.", "native_killer", "할리우드 거장들과 함께 예술의 불멸성을 찬양하는 압도적인 카리스마의 건배사입니다."),
                    ("I am going to throw these gold statues at the rival agents' cars!", "이 황금 트로피들을 라이벌 에이전트들 자동차에 집어던져야지!", "wrong_konglish", "오스카 11관왕의 영광을 저급한 폭력으로 망쳐버리는 언사입니다."),
                    ("I am very sleepy, please turn off the lights in the theatre.", "너무 졸리니까 극장 불 끄고 다들 조용히 해주세요.", "mediocre", "할리우드 최고의 영광의 순간에 어울리지 않는 무기력한 태도입니다.")
                ]
            },
            {
                "dialogue": "Vanity Fair Oscar Party red carpet is outside, and every studio head in the world is offering blank checks for our next five projects. Do we sign mega-franchise studio deals, or keep our creative autonomy?",
                "korean": "베니티 페어 오스카 파티 레드카펫이 바깥에 펼쳐져 있고, 세상의 모든 스튜디오 대표들이 우리 다음 프로젝트 5편에 백지수표를 내밀고 있어. 메가 프랜차이즈 스튜디오 계약을 맺을 텐가, 아니면 창작의 자율성을 지킬 텐가?",
                "hint": "백지수표에 휘둘리지 않고, 완전한 창작 전권과 극장 배급권이 보장된 독자적 스튜디오 체제로 도약한다.",
                "choices": [
                    ("We take their distribution capital, but keep one hundred percent creative ownership. We don't take orders from studios anymore; we are the studio. Call the trades.", "저들의 배급 자본은 취하되, 창작 소유권은 100% 우리가 쥡니다. 우리는 더 이상 스튜디오의 지시를 받지 않습니다; 우리가 곧 스튜디오입니다. 버라이어티와 데드라인에 특종을 치십시오.", "native_killer", "'Entourage'의 아리 골드가 평생을 꿈꿔온 독립적 메이저 스튜디오 군주로의 등극 선언입니다."),
                    ("Sign away all our rights for quick cash so we can retire tomorrow.", "내일 은퇴할 수 있게 푼돈이나 받고 모든 판권을 넘겨버립시다.", "wrong_konglish", "오스카 11관왕의 위상을 스스로 헐값에 팔아넘기는 어리석은 처신입니다."),
                    ("Tell the studio heads that movies are stupid anyway.", "스튜디오 대표들에게 어차피 영화 따위 바보 같은 장난이라고 조롱합시다.", "wrong_konglish", "영화 산업의 모든 파트너를 적으로 돌려 자멸하는 망언입니다.")
                ]
            },
            {
                "dialogue": "The trades published the front page: 'A New Dynasty Rules Hollywood.' Ari Gold hugs you with tears in his eyes: 'Boom! We conquered the dream factory!' Let's walk into the Vanity Fair gala.",
                "korean": "연예지들이 1면 톱기사로 타전했어: '새로운 왕조가 할리우드를 지배한다.' 아리 골드가 눈물을 글썽이며 자넬 끌어안네: '터졌다(Boom)! 우리가 꿈의 공장을 정복했어!' 베니티 페어 갈라로 걸어 들어가지.",
                "hint": "할리우드 꿈의 공장을 정복한 최고의 엔터테인먼트 타이탄의 당당한 발걸음.",
                "choices": [
                    ("Roll out the red carpet, Ari. We made dreams real on the silver screen, and tonight, the stars shine for us. Let us celebrate our empire.", "레드카펫을 펼치시죠, 아리. 우리는 은막 위에 꿈을 현실로 만들었고, 오늘 밤 별들은 우리를 위해 빛납니다. 우리의 제국을 축하하러 갑시다.", "native_killer", "할리우드 시네마의 영광을 찬양하는 가장 화려하고 멋진 피날레입니다."),
                    ("I want to steal all the caviar from the party buffet!", "파티 뷔페에 있는 캐비어 통째로 주머니에 훔쳐 와야지!", "wrong_konglish", "오스카 11관왕의 제패자로서 품위를 시궁창에 버리는 도벽 언사입니다."),
                    ("Thank you Ari, holding heavy gold statues makes my arm tired.", "감사합니다 아리, 무거운 황금 조각상을 들고 있었더니 팔이 참 아프네요.", "mediocre", "할리우드 역사를 새로 쓴 감격치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "We were seeds / Dream factory",
        "key_note": "'They tried to bury us, they forgot we were seeds'는 억압을 딛고 피어난 예술적 투지, 'Dream factory'는 꿈을 빚어내는 할리우드를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 98: 5-Star Hotel (더 플라자 호텔 개관 100주년 센테니얼 갈라)
    # -------------------------------------------------------------
    {
        "ep_num": 98,
        "title": "더 플라자 호텔: 개관 100주년 세기의 센테니얼 갈라",
        "genre": "5-Star Hotel",
        "speaker": "Monsieur Dupont (Grand Master Hotelier & GM)",
        "emoji": "🏨",
        "synopsis": "뉴욕 5번가와 센트럴파크 사우스 더 플라자 호텔 그랜드 볼룸. 개관 100주년을 기념하는 세기의 센테니얼 갈라. 전 세계 40개국 전·현직 대통령, 왕족, 노벨상 수상자 500명이 집결한 만찬 10분 전, 총지배인과 함께 한 세기를 지켜온 럭셔리 호스피탈리티의 정점을 기념한다.",
        "turns": [
            {
                "dialogue": "One hundred years of kings, presidents, legends, and lovers under this crystal chandelier. Outside, Manhattan changes every second, but inside The Plaza, timeless grace endures. What is your address to our staff before the grand doors open?",
                "korean": "이 크리스털 샹들리에 아래서 100년간 왕들과 대통령들, 전설들과 연인들이 머물렀네. 바깥세상 맨해튼은 매초 변하지만, 플라자 호텔 안에서는 영원한 기품이 살아 숨 쉬지. 그랜드 도어가 열리기 전 우리 호텔리어들에게 전할 자네의 훈화가 뭔가?",
                "hint": "서비스란 단순한 노동이 아니라, 손님의 존엄성을 지키고 역사에 품격을 더하는 예술임을 일깨운다.",
                "choices": [
                    ("Remind every butler, chef, and concierge: we do not merely serve rooms; we curate human memories that outlive generations. Tonight, deliver perfection with every smile and every step.", "모든 집사, 셰프, 컨시어지에게 상기시키십시오: 우리는 단순한 객실을 서비스하는 것이 아니라 세대를 초월해 남을 인간의 기억을 빚어내는 것입니다. 오늘 밤, 매 걸음과 미소마다 완벽을 담아내십시오.", "native_killer", "세계 최고 럭셔리 호텔리어의 심장을 울리는 숭고한 장인 정신과 품격의 극치입니다."),
                    ("Tell the staff to demand ten-dollar tips from every president.", "직원들에게 대통령마다 10달러씩 팁을 내놓으라고 삥을 뜯으라고 시킵시다.", "wrong_konglish", "100년 전통 5성급 호텔의 명예를 구걸로 전락시키는 수치스러운 행동입니다."),
                    ("Turn off the chandeliers and tell the guests to bring flashlights.", "샹들리에를 끄고 손님들에게 각자 손전등이나 켜고 다니라고 합시다.", "wrong_konglish", "센테니얼 갈라를 난장판으로 만들고 호텔 문을 영구히 닫게 만드는 망발입니다.")
                ]
            },
            {
                "dialogue": "The grand doors opened! Five hundred dignitaries gasped at the floral arrangements and orchestral waltz! The President of the United States rises with a vintage champagne glass: 'To the crown jewel of New York!' How do you receive the presidential toast?",
                "korean": "그랜드 도어가 열렸어! 500명의 귀빈들이 환상적인 생화 장식과 오케스트라 왈츠에 탄성을 내뱉었네! 미합중국 대통령이 빈티지 샴페인 잔을 들고 일어섰어: '뉴욕의 왕관에 박힌 가장 찬란한 보석을 위하여!' 대통령의 건배사를 어떻게 화답할 텐가?",
                "hint": "호텔의 역사와 뉴욕시, 그리고 그곳을 거쳐 간 모든 여행자들의 영혼에 감사하며 화답한다.",
                "choices": [
                    ("Raise your glass with quiet majesty: To the city that never sleeps, and to the home that forever welcomes its dreamers. May The Plaza stand as a sanctuary of grace for another hundred years.", "조용한 위엄을 담아 잔을 높이 드십시오: 결코 잠들지 않는 도시 뉴욕을 위하여, 그리고 그 꿈꾸는 이들을 영원히 반겨주는 안식처를 위하여. 플라자 호텔이 또 다른 100년간 기품의 성소로 우뚝 서기를.", "native_killer", "센트럴파크의 밤을 영원히 수놓을 가장 격조 높고 우아한 건배사입니다."),
                    ("Drink the whole bottle in three seconds and burp loudly on the microphone.", "3초 만에 병째로 원샷하고 마이크에 대고 커다랗게 트림을 합시다.", "wrong_konglish", "전 세계 정상들 앞에서 스스로 인간 말종임을 인증하는 추태입니다."),
                    ("Tell the President that his glass is half empty so he is unlucky.", "대통령에게 잔이 반밖에 안 찼으니 재수 없을 거라고 악담을 퍼부읍시다.", "wrong_konglish", "국가 원수를 모욕하고 외교적 결례를 범하는 무례한 처신입니다.")
                ]
            },
            {
                "dialogue": "The room erupted into cheers and waltzes! Monsieur Dupont wipes a tear of joy and hands you the golden master skeleton key of The Plaza: 'You are the soul of this institution. Happy Centennial.'",
                "korean": "연회장 전체가 환호와 왈츠로 넘쳐흘렀어! 뒤퐁 총지배인이 기쁨의 눈물을 훔치며 플라자의 황금 마스터 해골 열쇠를 건네네: '자네가 이 유서 깊은 호텔의 진정한 영혼이야. 100주년을 축하하네.'",
                "hint": "세계 최고 럭셔리 호스피탈리티의 영혼을 계승한 지배인의 따뜻하고 품격 있는 피날레.",
                "choices": [
                    ("Discretion, elegance, and eternity. It has been the honor of my life to serve this sanctuary of dreams. Let the centennial waltz play into the dawn.", "신중함, 우아함, 그리고 영원. 이 꿈의 성소를 섬길 수 있었던 것은 제 인생 최고의 영광이었습니다. 100주년의 왈츠가 새벽까지 울려 퍼지게 하십시오.", "native_killer", "호스피탈리티 산업의 불멸의 영광을 기리는 가장 완벽한 피날레입니다."),
                    ("Now I can use this master key to open every safe and get rich!", "이제 이 마스터키로 모든 객실 금고를 다 털어서 부자 돼야지!", "wrong_konglish", "100년의 영예로운 마스터 열쇠를 도둑질 수단으로 여기는 천박한 언사입니다."),
                    ("Thank you Dupont, walking around the lobby is very tiring.", "감사합니다 뒤퐁 지배인님, 로비 돌아다니느라 다리가 참 아프네요.", "mediocre", "세기의 센테니얼 갈라의 웅장함에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Sanctuary of grace / Timeless elegance",
        "key_note": "'Sanctuary of grace'는 품격의 성소, 'Timeless elegance'는 시대를 초월해 변치 않는 우아함을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 99: Fine Art Auction (10억 달러 모나리자 비공개 소장품 특별 경매)
    # -------------------------------------------------------------
    {
        "ep_num": 99,
        "title": "세기의 경매: 10억 달러 레오나르도 다빈치 비밀 경매",
        "genre": "Fine Art Auction",
        "speaker": "Julian Vance (Chief Global Auctioneer)",
        "emoji": "🎨",
        "synopsis": "모나코 몬테카를로 비밀 해저 볼룸. 루브르 박물관 공인 레오나르도 다빈치의 마지막 미공개 자화상 원본 출품. 전 세계 10대 국부펀드와 비밀 억만장자 수집가 20명이 참석한 가운데, 인류 역사상 최초로 10억 달러(1조 3천억 원) 호가 돌파를 앞둔 마지막 낙찰봉을 쥔다.",
        "turns": [
            {
                "dialogue": "Nine hundred million dollars bid on the telephone from Tokyo! Nine hundred fifty million in the room from the Louvre Acquisition Trust! We are fifty million away from the first billion-dollar sale in human history. Do we hammer or push for the ten figures, Julian?",
                "korean": "도쿄 전화 입찰에서 9억 달러 나왔습니다! 루브르 미술관 인수 트러스트에서 9억 5천만 달러를 객석에서 불렀습니다! 인류 역사상 최초의 10억 달러(1조 3천억) 돌파까지 단 5천만 달러 남았습니다. 낙찰봉을 내리시겠습니까, 아니면 10자리 신기록을 유도하시겠습니까, 줄리언?",
                "hint": "단순한 금전적 가치를 넘어, 인류 문명의 정수를 소장할 수 있는 유일무이한 역사적 순간임을 일깨워 10억 달러를 돌파시킨다.",
                "choices": [
                    ("Hold the gavel. Address the room with quiet reverence: remind them that gold turns to dust and empires fall, but da Vinci's genius is the eternal crown of human civilization. Do I hear one billion?",
                     "낙찰봉을 잠시 멈추십시오. 고요한 경외심으로 장내를 응시하십시오: 금은 먼지로 돌아가고 제국은 무너지지만, 다빈치의 천재성은 인류 문명의 영원한 왕관임을 상기시키십시오. 10억 달러를 부르시겠습니까?",
                     "native_killer",
                     "소더비와 크리스티 300년 역사를 통틀어 가장 위엄 있고 전율을 부르는 최고의 경매사 호가 유도입니다."),
                    ("Bang the wooden hammer quickly and go eat street tacos.", "나무 낙찰봉이나 후딱 치고 나가서 길거리 타코나 사 먹읍시다.", "wrong_konglish", "인류사상 최초의 10억 달러 신기록을 스스로 걷어차는 경솔한 행동입니다."),
                    ("Scream at the billionaires that they are cheapskates.", "억만장자들에게 구두쇠 짠돌이들이라고 삿대질하며 욕설을 퍼부읍시다.", "wrong_konglish", "세계 최고 경매장의 품격을 완전히 파괴하고 즉각 해고당할 망동입니다.")
                ]
            },
            {
                "dialogue": "Paddle number seven went up! One billion dollars! The entire room gasped in breathless awe! But the Swiss bank wire requires a final provenance confirmation signature from the podium. How do you certify this sacred moment?",
                "korean": "7번 팻말이 올라왔습니다! 10억 달러! 장내 전체가 숨을 멎은 채 경외감에 휩싸였습니다! 하지만 스위스 은행 송금을 위해 단상에서 최종 출처 보증 서명이 필요합니다. 이 성스러운 순간을 어떻게 증명하시겠습니까?",
                "hint": "출처의 완전무결함과 문화유산의 공공 전시 협약을 함께 보증하며 완벽히 서명한다.",
                "choices": [
                    ("Sign the master provenance ledger with the diamond-tipped fountain pen: certify its flawless 500-year chain of custody, with a binding clause that the masterpiece must be displayed in public museums for six months every decade.",
                     "다이아몬드 닙 만년필로 마스터 출처 원장에 서명하십시오: 500년간의 티끌 없는 소장 이력을 공인하고, 10년마다 6개월간 일반 대중 미술관에 의무 공개 전시해야 한다는 조항을 결합하십시오.",
                     "native_killer",
                     "개인의 소장을 넘어 인류 공동의 유산으로 보존하는 가장 숭고한 최고위 경매사의 예술 철학입니다."),
                    ("Sign with a red crayon and draw a smiley face on the document.", "빨간 크레파스로 서명하고 계약서에 웃는 얼굴 낙서나 그려 넣읍시다.", "wrong_konglish", "10억 달러짜리 국제 계약서를 장난으로 망쳐버리는 황당한 행동입니다."),
                    ("Refuse to sign because writing your name is too difficult.", "내 이름 쓰는 게 너무 힘들고 귀찮으니 서명을 거부합시다.", "mediocre", "역사적인 순간에 프로의 기본을 저버리는 어리석은 태도입니다.")
                ]
            },
            {
                "dialogue": "Fair warning... at one billion dollars... down comes the gavel! Sold! The world record shattered forever! Julian Vance wipes tears of awe. You just presided over the zenith of art history.",
                "korean": "마지막 경고... 10억 달러에... 낙찰봉이 떨어집니다! 낙찰! 세계 신기록이 영원히 깨졌습니다! 줄리언 밴스가 경외의 눈물을 훔칩니다. 자네가 미술사의 절대적 정점을 지휘했네.",
                "hint": "예술의 영원성과 인류 문화의 위대함을 기리는 불멸의 피날레.",
                "choices": [
                    ("Down comes the gavel, and history is sealed. May this eternal light of the Renaissance continue to inspire humanity for the next five centuries. The auction is concluded.",
                     "낙찰봉이 내려치며 역사가 봉인되었습니다. 이 르네상스의 영원한 빛이 향후 500년간 인류에게 영감을 불어넣기를. 경매를 종료합니다.",
                     "native_killer",
                     "'Down comes the gavel'의 전설적인 마침표를 찍는 인류 미술 경매 역사상 가장 장엄한 클로징입니다."),
                    ("Now give me my ten percent cut so I can buy a spaceship!", "이제 내 수수료 10% 1,300억 내놓아라, 우주선 사러 가야지!", "wrong_konglish", "숭고한 예술적 순간을 파렴치한 돈자랑으로 더럽히는 언사입니다."),
                    ("Thank you Julian, holding the wooden hammer made my fingers stiff.", "감사합니다 줄리언, 나무 망치를 쥐고 있었더니 손가락이 굳었네요.", "mediocre", "10억 달러 세계 신기록의 감격치고는 너무 시시한 푸념입니다.")
                ]
            }
        ],
        "key_expr": "Down comes the gavel / Chain of custody",
        "key_note": "'Down comes the gavel'은 최종 낙찰봉이 떨어지며 역사가 확정됨을 알리는 선언, 'Chain of custody'는 흠결 없는 소장 이력을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 100: Investigative Journalism (퓰리처상 수상 연설: 진실은 영원하다)
    # -------------------------------------------------------------
    {
        "ep_num": 100,
        "title": "진실의 승리: 퓰리처상 수상 연설 '진실은 영원히 침몰하지 않는다'",
        "genre": "Investigative Journalism",
        "speaker": "Ben Bradlee (Legendary Executive Editor & Pulitzer Board)",
        "emoji": "📰",
        "synopsis": "뉴욕 컬럼비아 대학교 로우 메모리얼 라이브러리. 전 세계 언론인 1,000명이 기립한 가운데 거행되는 제110회 퓰리처상 공공봉사상(Public Service Gold Medal) 시상식. 100편의 미국 드라마 시나리오를 집대성한 저널리즘의 대서사시를 마무리하며, 진실의 영원한 가치를 천명하는 마지막 수상 연설대에 오른다.",
        "turns": [
            {
                "dialogue": "One hundred investigations, death threats, courtroom battles, and government wiretaps. Tonight, the Pulitzer Board presents you with the Gold Medal for Public Service. Step up to the podium, reporter. What is your testament to the free press?",
                "korean": "100편의 탐사보도, 살해 협박, 법정 공방, 정부 도청을 이겨내고. 오늘 밤, 퓰리처상 위원회가 자네에게 언론계 최고 영예인 공공봉사상 금메달을 수여하네. 단상으로 올라가게, 기자 양반. 자유 언론을 향한 자네의 증언이 뭔가?",
                "hint": "어떤 권력이나 자본의 압박 앞에서도 굴복하지 않고 오직 약자와 진실의 편에 섰던 숭고한 저널리즘의 사명을 웅변한다.",
                "choices": [
                    ("Raise the gold medal high: A free press does not exist to flatter the powerful; it exists to be the voice of the voiceless and the light that pierces darkness. We write not for applause, but for the truth that outlives empires.",
                     "금메달을 높이 들어 올리십시오: 자유 언론은 권력자에게 아첨하기 위해 존재하는 것이 아닙니다; 목소리 없는 이들의 목소리가 되어주고 어둠을 꿰뚫는 빛이 되기 위해 존재합니다. 우리는 갈채가 아니라 제국보다 오래 살아남을 진실을 위해 씁니다.",
                     "native_killer",
                     "'All the President's Men'과 'Spotlight'를 넘어 퓰리처상의 영혼을 관통하는 가장 감동적이고 역사적인 수상 연설입니다."),
                    ("I won this medal because I am smarter than all other journalists!", "내가 다른 기자들보다 훨씬 똑똑해서 이 메달 딴 겁니다!", "wrong_konglish", "공공봉사의 숭고한 영예를 사적 거만함으로 더럽히는 부끄러운 언사입니다."),
                    ("I want to melt this gold medal and turn it into dental fillings.", "이 금메달 녹여서 치과 금니나 때워 넣어야겠습니다.", "wrong_konglish", "전 세계 언론인들이 지켜보는 무대에서 미친 소리를 늘어놓는 추태입니다.")
                ]
            },
            {
                "dialogue": "The entire Columbia library stood in a thunderous five-minute ovation! Reporters from every continent are wiping tears. Ben Bradlee leans in: 'One last question for the history books: When the storm rages and democracy trembles, what keeps the press unyielding?'",
                "korean": "컬럼비아 도서관 전체가 우레와 같은 5분간의 기립 박수로 화답했네! 전 대륙에서 온 기자들이 눈물을 훔치고 있어. 벤 브래들리가 다가와 묻네: '역사책을 위한 마지막 질문일세: 폭풍이 몰아치고 민주주의가 흔들릴 때, 언론을 꺾이지 않게 지탱하는 것은 무엇인가?'",
                "hint": "어둠이 아무리 깊어도 활자와 진실의 힘은 결코 침몰하지 않는다는 불멸의 신념을 선포한다.",
                "choices": [
                    ("The unyielding conviction that darkness dies in the light, and that courage is contagious. As long as one reporter holds a pen and refuses to blink, liberty shall never perish from this Earth.",
                     "어둠은 빛 속에서 소멸하며, 용기는 전염된다는 흔들림 없는 확신입니다. 단 한 명의 기자가 펜을 쥐고 눈 하나 깜빡이기를 거부하는 한, 자유는 이 땅에서 결코 사라지지 않을 것입니다.",
                     "native_killer",
                     "'Democracy Dies in Darkness'와 링컨의 게티즈버그 연설을 결합한 인류 저널리즘의 불멸의 금자탑입니다."),
                    ("Money! If you give reporters enough cash, they will write anything!", "돈이죠! 기자들한테 돈만 넉넉히 쥐여주면 무슨 기사든 다 써줍니다!", "wrong_konglish", "저널리즘의 숭고한 가치를 기레기 돈벌이로 매도하는 최악의 망언입니다."),
                    ("I think we should stop writing news because newspapers are heavy.", "신문이 무거우니까 이제 뉴스 기사 쓰기를 그만둬야 한다고 생각합니다.", "mediocre", "퓰리처상의 역사적 위엄에 찬물을 끼얹는 황당한 발언입니다.")
                ]
            },
            {
                "dialogue": "Tears streamed down Bradlee's face. The Pulitzer Board stamped the centenary citation: 'To the reporter who held the beacon high when all other lights went out.' You have completed the century odyssey. Dramactor salutes you.",
                "korean": "브래들리의 얼굴에 눈물이 흘러내렸네. 퓰리처 위원회가 100주년 헌사를 날인했어: '다른 모든 빛이 꺼졌을 때 횃불을 높이 들었던 기자에게.' 자네가 100편의 오디세이를 완결했네. 드라맥터(Dramactor)가 자네에게 경례하네.",
                "hint": "100개의 에피소드, 300개의 드라마 턴을 완벽하게 관통한 영광스러운 대단원의 막을 내린다.",
                "choices": [
                    ("The story is told, the truth endures, and the curtain falls. To every actor, reporter, and dreamer who dared to step onto this stage: the world is yours. Curtain call.",
                     "이야기는 완성되었고, 진실은 영원하며, 막이 내립니다. 이 무대에 감히 발을 디뎠던 모든 배우, 기자, 그리고 꿈꾸는 이들에게: 온 세상은 이제 여러분의 것입니다. 커튼콜.",
                     "native_killer",
                     "Dramactor 100개 에피소드 전체를 완벽하게 집대성하고 찬란하게 닫는 불멸의 커튼콜 대사입니다."),
                    ("Now I want to delete the whole website so nobody can read it!", "이제 아무도 못 보게 웹사이트 전체를 삭제해버려야지!", "wrong_konglish", "100개의 명작을 허무하게 파괴하려는 광기 어린 행동입니다."),
                    ("Thank you Ben, speaking for 100 episodes makes my jaw click.", "감사합니다 벤, 100편 내내 대사를 쳤더니 턱관절이 딱딱거리네요.", "mediocre", "100편 대단원의 역사적 감격치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "The truth endures / Curtain call",
        "key_note": "'The truth endures'는 진실은 영원히 침몰하지 않는다는 언론의 불멸의 신조, 'Curtain call'은 모든 여정을 마치고 관객의 환호에 답하는 대단원을 뜻합니다."
    }
]

print(f"Part 5 Loaded {len(EPISODES_81_TO_100)} curated episodes (EP 81 to 100).")

