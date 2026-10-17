# -*- coding: utf-8 -*-
"""
Dramactor Curated Master Database - Part 4 (Episodes 61 to 80)
Unexpected Twists & Deep Lore across 20 American drama genres.
"""

EPISODES_61_TO_80 = [
    # -------------------------------------------------------------
    # EP 61: Legal (은사의 내부자 거래 변호)
    # -------------------------------------------------------------
    {
        "ep_num": 61,
        "title": "은사의 내부자 거래 기소: 스승과의 법정 독대",
        "genre": "Legal",
        "speaker": "Professor Gerard (Former Law Dean & Senior Counsel)",
        "emoji": "⚖️",
        "synopsis": "뉴욕 남부지방법원 변호인 대기실. 하버드 로스쿨 시절 당신에게 법의 윤리를 가르쳤던 은사가 제약사 합병 관련 내부자 거래 혐의로 연방 검찰에 기소되어, 10년 징역형 플리바게닝 제안을 앞에 두고 고뇌한다.",
        "turns": [
            {
                "dialogue": "The US Attorney offered a plea deal: five years in federal prison and forfeiture of my law license. I taught you everything about ethics. Do you want me to confess to a crime I didn't commit to save my skin?",
                "korean": "연방 검사가 플리바게닝을 제안했어: 연방 교도소 5년형과 변호사 면허 박탈이야. 내가 자네에게 법률 윤리의 모든 것을 가르쳤지. 목숨을 건지겠다고 내가 저지르지도 않은 죄를 자백하길 바라나?",
                "hint": "굴욕적인 자백을 거부하고, 은사의 무고함을 입증할 알고리즘 트레이딩 우연 일치 분석을 준비한다.",
                "choices": [
                    ("Never sign that plea, Professor. The stock purchase coincided with an automated index rebalancing; we take this to trial and clear your name completely.", "절대 그 유죄협상에 서명하지 마십시오, 교수님. 주식 매수는 자동 인덱스 리밸런싱과 우연히 겹친 것뿐입니다. 정식 재판으로 가서 결백을 완전히 입증하겠습니다.", "native_killer", "'Suits'의 하비 스펙터가 은사를 지켜낼 때 보여주는 최고의 의리와 정밀한 법률적 승부수입니다."),
                    ("Take the five years, prison food is not that bad.", "그냥 5년 사세요, 교도소 밥도 그렇게 나쁘진 않습니다.", "wrong_konglish", "존경하는 은사의 명예와 삶을 송두리째 짓밟는 배은망덕한 소리입니다."),
                    ("Tell the prosecutor that older people make mistakes sometimes.", "검사에게 노인들은 가끔 실수도 하는 법이라고 둘러댑시다.", "mediocre", "무죄를 주장해야 할 자리에서 은사를 치매 노인 취급하는 부적절한 태도입니다.")
                ]
            },
            {
                "dialogue": "The prosecutor called my former broker to the stand. He claims I called him from a payphone thirty minutes before the merger leak. It's perjury, but the jury is gasping. How do you cross-examine?",
                "korean": "검사가 내 전 브로커를 증인대에 세웠어. 합병 유출 30분 전에 내가 공중전화로 전화했다고 위증하고 있네. 배심원들이 술렁이고 있어. 어떻게 반대신문할 텐가?",
                "hint": "공중전화 위치 통화기록과 당시 은사의 강의 출석부 타임스탬프로 위증을 격파한다.",
                "choices": [
                    ("Confront the broker with your lecture hall attendance logs and geolocated university security CCTV: he perjured himself for prosecutorial immunity.", "강의실 출석 기록과 대학교 보안 CCTV 타임스탬프를 들이대십시오: 브로커가 자신의 면책을 위해 명백한 위증을 저질렀음을 밝혀내야 합니다.", "native_killer", "반대신문에서 증인의 거짓말을 완벽하게 무너뜨리는 법정 드라마의 쾌감입니다."),
                    ("Cry loudly and ask the jury to feel sorry for the old professor.", "소리 내어 울면서 배심원들에게 늙은 교수님을 불쌍히 여겨달라고 구걸합시다.", "wrong_konglish", "법리와 증거 대신 동정에 호소하여 재판을 패배로 이끄는 나약한 행동입니다."),
                    ("Tell the broker that lying is very bad for his karma.", "브로커에게 거짓말을 하면 업보를 받는다고 설교합시다.", "mediocre", "법정에서 종교적 훈계나 늘어놓는 비전문적인 처신입니다.")
                ]
            },
            {
                "dialogue": "Not Guilty on all counts! The judge sanctioned the US Attorney for prosecutorial misconduct! Gerard embraced you with tears. You surpassed the master today.",
                "korean": "전 공소사실 무죄 평결! 판사가 검찰의 수사권 남용에 징계 처분을 내렸어! 제라드 교수님이 눈물을 흘리며 자넬 안아주었네. 자네가 오늘 스승을 뛰어넘었어.",
                "hint": "은사의 명예를 회복한 제자 변호사의 가슴 벅찬 경의.",
                "choices": [
                    ("The pupil is only as good as the master who forged him. Your honor is restored, Professor Gerard; justice has spoken.", "제자의 성취는 그를 단련시킨 스승의 위대함 덕분입니다. 교수님의 명예가 온전히 회복되었습니다. 정의가 증명되었습니다.", "native_killer", "스승과 제자의 숭고한 유대와 정의의 승리를 기리는 감동적인 클로징입니다."),
                    ("Now you must pay me a million dollars for my legal fee!", "이제 변호사 수임료로 100만 달러 당장 입금하세요!", "wrong_konglish", "눈물겨운 승리 직후 돈독이 오른 모습을 보여 은사를 아연실색하게 만듭니다."),
                    ("Thank you Professor, cross-examination made my voice hoarse.", "감사합니다 교수님, 반대신문 하느라 목이 다 쉬었네요.", "mediocre", "역사적인 무죄 판결의 감동을 단순 목 통증으로 격하시키는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Perjured testimony / Not Guilty",
        "key_note": "'Perjury'는 법정에서의 위증죄, 'Not Guilty on all counts'는 모든 기소 항목에 대한 전면 무죄 평결을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 62: Startup (스텔스 모드 라이벌 유니콘 특허 소송)
    # -------------------------------------------------------------
    {
        "ep_num": 62,
        "title": "스텔스 모드 특허 침해 소송: 라이벌 유니콘의 침공",
        "genre": "Startup",
        "speaker": "Peter Thiel (Contrarian Tech Billionaire)",
        "emoji": "🚀",
        "synopsis": "실리콘밸리 팔로알토 테크 허브. 100억 달러 가치의 라이벌 AI 유니콘이 우리 핵심 아키텍처 특허 침해 가처분 소송을 제기하며 전 세계 앱스토어 배포 중단과 영업 금지를 신청해온다.",
        "turns": [
            {
                "dialogue": "Our rival filed an emergency ITC injunction to block our global SDK downloads. They claim our neural weights infringe on their 2021 patent. If we get enjoined, our Series C valuation drops to zero. How do we counter?",
                "korean": "경쟁사가 우리 글로벌 SDK 다운로드를 차단하려고 긴급 무역위원회(ITC) 수입금지 가처분을 냈어. 우리 신경망 가중치가 저들의 2021년 특허를 침해했대. 가처분이 인용되면 시리즈 C 가치는 0이 돼. 어떻게 반격할 텐가?",
                "hint": "특허 무효 심판(IPR)을 즉각 청구하고, 2019년 오픈소스 논문의 선행기술(Prior Art)을 찾아내 상대 특허 자체를 무력화한다.",
                "choices": [
                    ("File an emergency Inter Partes Review with the Patent Office: introduce the 2019 Stanford open-source whitepaper as indisputable prior art to invalidate their patent.", "특허청에 긴급 특허무효심판(IPR)을 청구하십시오: 2019년 스탠퍼드 오픈소스 논문을 명백한 선행기술로 제출하여 저들의 특허 자체를 무효화해야 합니다.", "native_killer", "'Inter Partes Review'와 'prior art invalidation'은 실리콘밸리 특허 분쟁을 단칼에 끝내는 핵폭탄급 법률 전략입니다."),
                    ("Delete our entire code repository and shut down the company.", "우리 코드 저장소를 전부 삭제하고 회사를 폐업합시다.", "wrong_konglish", "근거 없는 경쟁사의 소송 위협에 겁을 먹고 스스로 자멸하는 최악의 행동입니다."),
                    ("Write a sad letter to the rival CEO begging for mercy.", "경쟁사 대표에게 자비를 베풀어달라고 눈물의 편지나 씁시다.", "wrong_konglish", "냉혹한 비즈니스 전장에서 먹잇감으로 전락하는 비참한 태도입니다.")
                ]
            },
            {
                "dialogue": "Patent Office accepted our IPR! But their legal hitmen are offering a dirty settlement: give them thirty percent of our equity or they drag out the litigation for three years until we bleed out.",
                "korean": "특허청이 우리 무효심판을 받아들였어! 하지만 저들의 법률 사냥꾼들이 추잡한 합의를 제안해왔네: 지분 30%를 넘기지 않으면 3년 동안 소송을 질질 끌어 우리 현금을 말려 죽이겠대.",
                "hint": "독점규제 위반(Antitrust) 역소송과 소송 사기 혐의를 경고하며 무조건적 소 취하를 압박한다.",
                "choices": [
                    ("Counter with a Sherman Antitrust sham litigation lawsuit and seek treble damages. Give them twenty-four hours to withdraw with prejudice, or face total exposure.", "셔먼 반독점법상 사기적 소송 역소송을 제기하고 징벌적 3배 손해배상을 청구하십시오. 24시간 안에 재소 금지 조건으로 소송을 자진 취하하지 않으면 전면전을 각오하라 하십시오.", "native_killer", "'Sham litigation', 'treble damages', 'with prejudice'는 약탈적 특허 괴물을 제압하는 최강의 역공입니다."),
                    ("Sign over the thirty percent equity, we can make more later.", "그냥 지분 30% 넘겨줍시다, 나중에 더 벌면 되죠.", "wrong_konglish", "회사의 미래를 적에게 헌납하는 어리석고 굴종적인 타협입니다."),
                    ("Hire a private detective to slash their tires at night.", "사설탐정을 고용해 밤에 저쪽 회사 타이어에 펑크를 냅시다.", "wrong_konglish", "상법 소송을 형사 범죄로 변질시키는 황당무계한 짓입니다.")
                ]
            },
            {
                "dialogue": "They blinked! Full withdrawal with prejudice signed! The cloud is clear, and Andreessen just wired one hundred million at an eight-billion valuation. Brilliant asymmetric warfare.",
                "korean": "저쪽이 꼬리 내렸어! 재소 금지 완전 소 취하 서명 완료! 먹구름이 걷혔고 안드레센이 기업가치 80억 달러로 1억 달러 투자를 방금 송금했네. 눈부신 비대칭 전쟁의 승리였어.",
                "hint": "시장의 포식자들을 제압하고 독점적 우위를 확립한 창업자의 담대한 선언.",
                "choices": [
                    ("Zero to One achieved. We conquered the predators and secured our monopoly. Back to product engineering; let's build the future.", "제로 투 원(Zero to One)을 달성했습니다. 약탈자들을 정복하고 독점적 입지를 굳혔습니다. 이제 제품 개발로 복귀해 미래를 건설합시다.", "native_killer", "피터 틸의 'Zero to One' 철학을 완벽하게 계승한 테크 창업자의 위대한 승리 선언입니다."),
                    ("I want to buy a yacht and name it 'Patent Killer'!", "요트 하나 사서 이름을 '특허 킬러'라고 짓고 싶네요!", "wrong_konglish", "거대한 도약 직후 가벼운 물질적 과시를 일삼는 경솔한 반응입니다."),
                    ("Thank you Peter, lawyers are very stressful.", "감사합니다 피터, 변호사들은 참 스트레스네요.", "mediocre", "글로벌 유니콘으로 도약한 승리의 감격치고는 너무 무미건조합니다.")
                ]
            }
        ],
        "key_expr": "Prior art / Sham litigation",
        "key_note": "'Prior art'는 특허의 신규성을 부인하는 선행 기술, 'Sham litigation'은 경쟁사를 괴롭히기 위한 사기성 소송을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 63: Corporate (가문의 비밀 유언장 개봉 후계 승계 전쟁)
    # -------------------------------------------------------------
    {
        "ep_num": 63,
        "title": "후계자 승계 전쟁: 가문의 비밀 유언장 개봉",
        "genre": "Corporate",
        "speaker": "Gerri Kellman (General Counsel & Family Trustee)",
        "emoji": "🏢",
        "synopsis": "맨해튼 펜트하우스 서재. 제국의 총수가 혼수상태에 빠진 직후, 가문의 비밀 금고에서 발견된 유언장 추서(Codicil)에 당신의 이름이 단독 후계자로 적혀 있음을 확인한 순간, 이복형제들이 서류 위조를 주장하며 이사회 소집을 요구한다.",
        "turns": [
            {
                "dialogue": "The pencil mark on the addendum is underlined, but Kendall claims it was crossed out. If the board deadlocks at noon, private equity raiders will carve up the conglomerate. What is your legal succession move?",
                "korean": "추서에 연필로 밑줄이 그어져 있지만, 켄달은 지워진 줄이라고 주장하고 있어. 정오에 이사회가 교착되면 사모펀드 약탈자들이 그룹을 공중분해 할 거야. 자네의 법적 승계 전략이 뭔가?",
                "hint": "밑줄의 진위를 다투며 시간을 끌지 않고, 사전에 확보된 가족 신탁(Voting Trust) 의결권을 발동해 주도권을 장악한다.",
                "choices": [
                    ("Invoke the family voting trust agreement: exercise the irrevocable proxy authority designated by Logan to establish immediate operational control.", "가족 의결권 신탁 계약을 발동하십시오: 로건 회장님이 지정한 취소 불능 위임 권한을 행사해 즉각적인 경영권을 확립해야 합니다.", "native_killer", "'Succession'의 진정한 법률 전략인 'Voting trust'와 'irrevocable proxy'로 분쟁을 원천 차단하는 마스터피스입니다."),
                    ("Let the siblings take everything and go work at McDonald's.", "형제들이 다 가져가게 놔두고 난 맥도날드에 취직이나 합시다.", "wrong_konglish", "가문의 제국을 포기하고 무력하게 도망치는 한심한 태도입니다."),
                    ("Erase the pencil mark with a rubber eraser quickly.", "지우개로 연필 자국을 지워서 증거를 인멸합시다.", "wrong_konglish", "사문서 변조죄로 즉각 구속 영장이 떨어지는 중범죄 행위입니다.")
                ]
            },
            {
                "dialogue": "Shiv has leaked the will dispute to Bloomberg to tank our stock price and force a fire sale. The trading halt is looming. How do you silence the market panic in sixty seconds?",
                "korean": "시브가 유언장 분쟁을 블룸버그에 유출해 주가를 폭락시키고 헐값 매각을 유도하고 있어. 거래 정지가 임박했네. 60초 안에 시장의 패닉을 어떻게 잠재울 텐가?",
                "hint": "블룸버그 라이브 생방송에 단독 CEO로 출연해 배당 안정성과 견고한 경영권 승계를 대외에 공표한다.",
                "choices": [
                    ("Go live on Bloomberg immediately: announce unified leadership, reaffirm full-year earnings guidance, and declare a five-hundred-million share buyback.", "즉각 블룸버그 생방송에 출연하십시오: 단일 리더십 확립을 발표하고 연간 실적 가이던스를 재확인하며 5억 달러 자사주 매입을 선언하십시오.", "native_killer", "주가 폭락을 한 방에 숏스퀴즈 반등으로 전환시키는 위대한 후계자의 결단입니다."),
                    ("Cry on camera and tell everyone your sister is mean.", "카메라 앞에서 울면서 여동생이 너무 못됐다고 하소연합시다.", "wrong_konglish", "상장 대기업 CEO의 자질을 의심케 하는 유치한 행동입니다."),
                    ("Hide in the bathroom and pretend you don't hear the phone.", "화장실에 숨어서 전화벨 소리를 못 들은 척합시다.", "mediocre", "경영 위기에서 등을 돌리는 가장 비겁한 회피입니다.")
                ]
            },
            {
                "dialogue": "The stock soared twelve percent! The siblings conceded defeat and accepted minority non-voting shares. You are the undisputed Chief Executive of Waystar Royco. Logan would be proud.",
                "korean": "주가가 12% 폭등했어! 형제들이 패배를 인정하고 무의결권 소수 지분을 수락했네. 자네가 웨이스타 로이코의 반박 불가능한 단독 CEO야. 로건 회장님도 자랑스러워하실 걸세.",
                "hint": "피비린내 나는 왕좌의 게임에서 승리한 제국 후계자의 서늘하고 위엄 넘치는 클로징.",
                "choices": [
                    ("The crown is won, Gerri. Inform the media and call the executive committee: the succession is settled, and the future begins now.", "왕관을 차지했습니다, 제리. 언론에 공식 발표하고 경영위원회를 소집하십시오: 승계는 완결되었으며, 이제 우리의 미래가 시작됩니다.", "native_killer", "'Succession'의 최종 승자다운 품격과 절대적 지배력을 보여주는 최고의 대사입니다."),
                    ("I am going to fire everyone who didn't smile at me today!", "오늘 나한테 안 웃어준 놈들 내일부터 싹 다 해고할 거야!", "wrong_konglish", "승리 직후 속 좁은 보복을 일삼는 폭군의 말로를 부르는 언사입니다."),
                    ("Thank you Gerri, running big companies is very hard.", "감사합니다 제리, 대기업 경영은 참 힘든 일이네요.", "mediocre", "역사적인 승계 완료의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Voting trust / Succession is settled",
        "key_note": "'Voting trust'는 경영권 안정을 위한 의결권 공동 행사 신탁, 'Succession settled'는 후계 승계 분쟁의 완전한 종결을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 64: Medical (혁신 유전자 치료 임상시험 치명적 부작용)
    # -------------------------------------------------------------
    {
        "ep_num": 64,
        "title": "혁신 유전자 치료 임상: 치명적 부작용 딜레마",
        "genre": "Medical",
        "speaker": "Dr. Derek Shepherd (Chief of Neurosurgery)",
        "emoji": "🏥",
        "synopsis": "존스 홉킨스 첨단 뇌신경 연구소. 난치성 교모세포종 환자 10명을 대상으로 한 혁신 바이러스 유전자 치료 3상 임상 중, 첫 환자에게서 급성 사이토카인 폭풍 뇌부종이 발생하며 30분 안에 연구 중단 여부를 결정해야 한다.",
        "turns": [
            {
                "dialogue": "Patient One's intracranial pressure spiked past thirty millimeters of mercury! Massive cerebral edema triggered by viral vector immune reaction! The FDA monitor is demanding an immediate clinical hold. How do we reduce the pressure?!",
                "korean": "1번 환자의 뇌압이 30mmHg를 돌파했어! 바이러스 벡터 면역 반응으로 인한 대규모 뇌부종이야! FDA 감독관은 즉각적인 임상 시험 중단을 요구하고 있어. 뇌압을 어떻게 떨어뜨릴 텐가?!",
                "hint": "임상을 전면 포기하지 않고, 고삼투압 치료와 면역억제 인터루킨 억제제를 병용 투여해 뇌 손상을 막는다.",
                "choices": [
                    ("Administer high-dose hypertonic saline alongside IL-6 receptor antagonists immediately, and prepare an emergency decompressive craniectomy if pressure exceeds thirty-five.", "고농도 고삼투압 식염수와 IL-6 수용체 길항제를 즉시 병용 투여하고, 뇌압이 35를 초과하면 긴급 감압 개두술을 준비하십시오.", "native_killer", "'Hypertonic saline'과 'IL-6 antagonist', 'decompressive craniectomy'는 첨단 신경외과 집중치료의 정석입니다."),
                    ("Put an ice pack on the patient's forehead and wait until tomorrow.", "환자 이마에 얼음주머니나 올려놓고 내일까지 기다려봅시다.", "wrong_konglish", "뇌 탈출증(Brain herniation)으로 환자를 즉각 사망에 이르게 하는 무식한 대처입니다."),
                    ("Tell the FDA monitor that dying is a natural part of medicine.", "FDA 감독관에게 원래 의학이란 사람이 죽기도 하는 법이라고 헛소리합시다.", "wrong_konglish", "의료 윤리를 파괴하고 연구소 문을 영구히 닫게 만드는 망언입니다.")
                ]
            },
            {
                "dialogue": "IL-6 block halted the cytokine cascade! Brain swelling receding, but the vector successfully eliminated ninety-four percent of the malignant tumor cells on MRI! Do we modify the protocol or cancel the trial?",
                "korean": "IL-6 차단제가 사이토카인 연쇄 반응을 멈췄어! 뇌부종이 가라앉고 있고, MRI상 종양 세포의 94%가 사멸했네! 프로토콜을 수정할 텐가, 임상을 취소할 텐가?",
                "hint": "치명적 부작용을 통제할 예방적 면역 조절 프로토콜을 추가하여 인류를 구할 임상을 지속시킨다.",
                "choices": [
                    ("Amend the clinical protocol: incorporate prophylactic immunomodulation twenty-four hours pre-infusion, protecting future patients while curing the cancer.", "임상 프로토콜을 즉시 개정하십시오: 주입 24시간 전 예방적 면역 조절 요법을 의무화하여 미래 환자를 보호하고 암을 완치시켜야 합니다.", "native_killer", "의학의 역사를 진일보시키는 숭고하고 과학적인 혁신 외과의의 판단입니다."),
                    ("Hide the brain swelling data from the FDA so they don't know.", "FDA가 눈치채지 못하게 뇌부종 발생 데이터를 몰래 삭제합시다.", "wrong_konglish", "연구 부정행위 및 위조로 면허가 취소되고 형사 처벌을 받는 중범죄입니다."),
                    ("Cancel the entire cure because science is too scary.", "과학이 너무 무서우니 암 치료제 연구를 영원히 포기합시다.", "mediocre", "수백만 난치병 환자들의 마지막 희망을 저버리는 소극적 포기입니다.")
                ]
            },
            {
                "dialogue": "FDA approved the modified protocol! Patient One is awake, talking, and completely tumor-free! You just pioneered a historic breakthrough in modern oncology, doctor.",
                "korean": "FDA가 수정 프로토콜을 승인했어! 1번 환자가 깨어나서 말을 하고 있고 종양이 완전히 사라졌네! 자네가 현대 종양학의 역사적 돌파구를 열었어, 의사 선생.",
                "hint": "의학의 새 지평을 연 신경외과 의사로서의 깊은 겸손과 환자에 대한 사랑.",
                "choices": [
                    ("It's a beautiful day to save lives, Derek. Let us monitor our pioneer and bring this cure to every cancer ward in the world.", "생명을 구하기 참 아름다운 날이군요, 데릭. 우리의 개척자를 정성껏 돌보고 전 세계 모든 암 병동에 이 치료제를 전합시다.", "native_killer", "'Grey's Anatomy' 데릭 셰퍼드의 전설적인 명대사 'It's a beautiful day to save lives'를 오마주한 감동의 피날레입니다."),
                    ("I want to patent this and charge each patient ten million dollars!", "이거 특허 내서 환자 한 명당 100억씩 받아 챙겨야지!", "wrong_konglish", "의사의 히포크라테스 선서를 저버리고 탐욕을 드러내는 천박한 언사입니다."),
                    ("Thank you Derek, brain surgery makes my neck ache.", "감사합니다 데릭, 뇌수술은 목이 참 뻐근하네요.", "mediocre", "역사적인 의학 혁명의 감격치고는 너무 시시한 반응입니다.")
                ]
            }
        ],
        "key_expr": "Cytokine cascade / Beautiful day to save lives",
        "key_note": "'Cytokine cascade'는 면역 체계가 폭주하는 사이토카인 폭풍, 'Beautiful day to save lives'는 생명을 구하는 외과의의 사명을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 65: Dating (지중해 메가요트 폭풍우 밀폐 선실 고백)
    # -------------------------------------------------------------
    {
        "ep_num": 65,
        "title": "지중해 메가요트 폭풍우: 밀폐된 선실의 고백",
        "genre": "Dating",
        "speaker": "Serena van der Woodsen (Manhattan High Society Icon)",
        "emoji": "🥂",
        "synopsis": "이탈리아 아말피 해안 앞바다를 항해 중인 3억 달러 초대형 럭셔리 요트. 시속 60노트의 지중해 폭풍우로 선실이 정전되고 파도가 갑판을 덮치는 고립된 밤, 맨해튼 최고의 잇걸이 와인 잔을 내려놓으며 감춰왔던 진심을 털어놓는다.",
        "turns": [
            {
                "dialogue": "The captain locked down the salon, and the generator is flickering. Everyone else is panicking on lower decks, but you're just sitting here looking at me like you knew this storm was coming. What are you hiding?",
                "korean": "선장이 살롱을 폐쇄했고 발전기가 깜빡이고 있어. 다른 사람들은 아래 갑판에서 패닉에 빠졌는데, 당신은 마치 이 폭풍이 올 줄 알았다는 듯 날 바라보고 있네. 뭘 숨기고 있는 거야?",
                "hint": "폭풍우 속에서도 흔들리지 않는 침착함과 매혹적인 고백으로 상대의 심장을 뛰게 한다.",
                "choices": [
                    ("The only storm that ever worried me was the one inside your heart, Serena. Let the ocean rage; you're completely safe with me.", "내가 걱정했던 유일한 폭풍은 오직 당신 마음속의 폭풍뿐이었어, 세레나. 바다가 날뛰게 둬; 내 곁에 있는 한 당신은 완벽히 안전하니까.", "native_killer", "'Gossip Girl'의 황금기를 수놓은 세레나를 단숨에 사로잡는 로맨틱하고 강인한 남주의 시그니처 대사입니다."),
                    ("I am so terrified! Where is my lifejacket?!", "나 너무 무서워! 내 구명조끼 어디 갔어?!", "wrong_konglish", "공포에 질려 징징대며 매력을 바닥으로 떨어뜨리는 찌질한 반응입니다."),
                    ("I checked the weather app yesterday, it said sixty percent rain.", "어제 일기예보 앱 봤는데 비 올 확률 60%라고 하더라고요.", "mediocre", "낭만적인 기류를 산통 깨버리는 건조한 팩트 전달입니다.")
                ]
            },
            {
                "dialogue": "Safe? People have been promising me that my entire life, and they always walk away when the society columns print their lies. Why should you be any different?",
                "korean": "안전하다고? 평생 사람들이 내게 그렇게 약속했지만, 사교계 가십 칼럼이 거짓말을 인쇄할 때마다 다들 날 떠나버렸어. 당신이라고 뭐가 다를 건데?",
                "hint": "세간의 평판이나 화려한 껍데기가 아닌, 그녀의 상처와 내면의 고독을 온전히 품어준다.",
                "choices": [
                    ("Because I don't love the glamorous headline; I love the girl who turns off the lights and reads poetry in the dark. I am never walking away.", "난 화려한 헤드라인을 사랑하는 게 아니니까; 조명을 끄고 어둠 속에서 시를 읽는 그 소녀를 사랑하니까. 난 결코 떠나지 않아.", "native_killer", "상류층의 공허함을 꿰뚫어 보고 영혼을 어루만져 주는 가장 완벽한 멜로의 대답입니다."),
                    ("Because I have ten million dollars more than your other ex-boyfriends.", "왜냐면 난 당신의 다른 전 남친들보다 돈이 100억은 더 많으니까요.", "wrong_konglish", "사랑을 천박한 돈자랑으로 치부하여 환멸을 부르는 최악의 발언입니다."),
                    ("Maybe you should stop reading gossip columns then.", "그럼 가십 칼럼을 안 읽으시면 될 텐데요.", "mediocre", "상대의 깊은 마음의 상처를 무시하는 쌀쌀맞은 답변입니다.")
                ]
            },
            {
                "dialogue": "The storm passed. Look... the moon is rising over Capri. I think I've been waiting for someone to see the real me for ten years. Kiss me.",
                "korean": "폭풍이 지나갔어. 봐... 카프리섬 위로 달이 떠오르고 있어. 10년 동안 누군가 내 진짜 모습을 알아봐 주길 기다려온 것 같아. 키스해줘.",
                "hint": "지중해의 달빛 아래서 완성되는 영화 같은 로맨스의 피날레.",
                "choices": [
                    ("Forever starts tonight, Serena. With the moon as our witness, the whole world can fade away.", "우리의 영원이 오늘 밤 시작되는 거야, 세레나. 저 달을 증인 삼아, 온 세상이 사라져도 좋아.", "native_killer", "클래식 할리우드 로맨스의 정점을 찍는 숨 막히게 아름다운 마무리입니다."),
                    ("I ate garlic for dinner, so maybe a high-five instead.", "저녁에 마늘을 많이 먹어서 키스 대신 하이파이브나 합시다.", "wrong_konglish", "일생일대의 로맨틱한 순간을 코미디로 망쳐버리는 황당한 소리입니다."),
                    ("Thank you Serena, renting this yacht was very expensive.", "고마워요 세레나, 이 요트 빌리느라 돈이 참 많이 들었네요.", "mediocre", "환상적인 낭만을 돈 계산으로 전락시키는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Glamorous headline / Moon as our witness",
        "key_note": "'Glamorous headline'은 화려하지만 덧없는 세간의 주목, 'Moon as our witness'는 달을 증인 삼아 맹세하는 클래식 로맨스 표현입니다."
    },
    # -------------------------------------------------------------
    # EP 66: Wall Street (암호화폐 고래 강제 청산 연쇄 마진콜)
    # -------------------------------------------------------------
    {
        "ep_num": 66,
        "title": "암호화폐 고래 청산: 연쇄 마진콜 도미노 방어",
        "genre": "Wall Street",
        "speaker": "Bobby Axelrod (Quantitative Trading Mogul)",
        "emoji": "📈",
        "synopsis": "싱가포르 센토사 퀀트 헷지펀드 워룸. 비트코인과 이더리움이 대형 파생상품 거래소의 50억 달러 고래 포지션 강제 청산으로 10분 만에 40% 폭락하는 플래시 크래시 상황에서, 우리 펀드의 10억 달러 레버리지 롱 포지션을 지켜내야 한다.",
        "turns": [
            {
                "dialogue": "The liquidation engine is dumping twenty thousand coins a second into an empty order book! Cascade liquidation alert! We have six minutes before our cross-margin hits liquidation threshold! Do we inject capital or take the haircut?",
                "korean": "청산 엔진이 텅 빈 호가창에 초당 2만 개씩 덤핑을 때리고 있어! 연쇄 청산 경보! 우리 교차 마진이 청산 임계치에 닿기까지 6분 남았네! 긴급 자금을 투입할 텐가, 손실을 확정 짓고 털릴 텐가?",
                "hint": "거래소 청산 알고리즘의 유동성 공백을 역이용해 장외(OTC) 담보를 스왑하고 숏 스퀴즈 덫을 놓는다.",
                "choices": [
                    ("Do not accept a haircut. Wire fifty million USDC into prime brokerage collateral, short the perpetual funding rate, and place laddered limit bids at the liquidation wick.", "손실 털기를 거부하십시오. 주거래 프라임 브로커리지에 5천만 USDC 담보를 즉시 송금하고, 무기한 펀딩비를 숏 치며 청산 꼬리 저점에 단계별 지정가 매수를 깔아두십시오.", "native_killer", "'Cross-margin', 'perpetual funding rate', 'liquidation wick'은 암호화폐 퀀트 최정상 트레이더의 전문 전술입니다."),
                    ("Sell all coins at the lowest possible price to stop the bleeding.", "출혈을 멈추기 위해 가장 바닥 최저가에 전량 패닉셀을 칩시다.", "wrong_konglish", "고래들의 청산 덤핑에 휘말려 펀드를 완전히 파산시키는 아마추어의 자살골입니다."),
                    ("Write an angry tweet to the CEO of the cryptocurrency.", "암호화폐 회사 대표한테 트위터로 화난 멘션이나 보냅시다.", "wrong_konglish", "탈중앙화 시장의 작동 원리를 모르는 초보적이고 무의미한 앙탈입니다.")
                ]
            },
            {
                "dialogue": "The wick bounced off your bids! But the offshore exchange's matching engine crashed under volume! They're threatening to roll back all trades executed in the last ten minutes. What is our legal and technical defense?",
                "korean": "자네 매수 벽을 맞고 꼬리가 반등했어! 하지만 역외 거래소 매칭 엔진이 거래량 폭증으로 뻗어버렸네! 저들이 지난 10분간 체결된 모든 거래를 롤백하겠다고 위협 중이야. 기술적, 법적 방어책이 뭔가?",
                "hint": "블록체인 분산 원장 트랜잭션 해시 증명을 제시하고 거래소 라이선스 취소 제소로 압박한다.",
                "choices": [
                    ("Broadcast on-chain cryptographic transaction receipts publicly. Inform the exchange board that rolling back executed order books constitutes market manipulation under Singapore MAS law.", "온체인 암호화 트랜잭션 영수증을 즉각 공개 배포하십시오. 체결된 호가창 롤백은 싱가포르 금융청(MAS) 법상 시장 교란 행위임을 통보해 손을 떼게 만드십시오.", "native_killer", "온체인 팩트와 규제기관의 칼날로 중앙화 거래소의 부당한 롤백을 제압하는 정통 방어책입니다."),
                    ("Say okay and let them take back all our profits.", "알겠다고 하고 우리 수익을 전부 다 가져가게 놔둡시다.", "wrong_konglish", "수천억의 정당한 이익을 도둑맞고도 멍하니 방관하는 나약한 태도입니다."),
                    ("Turn off our computer screens so we don't see the bad news.", "나쁜 소식을 안 보게 우리 컴퓨터 모니터 전원을 꺼버립시다.", "wrong_konglish", "문제를 직면하지 않고 숨어버리는 유아적 도피입니다.")
                ]
            },
            {
                "dialogue": "Exchange backed down! Trades finalized! Bitcoin V-shaped back to fifty-eight thousand, and we netted one hundred forty million on the liquidation bounce! You tamed the wild west, partner.",
                "korean": "거래소가 물러섰어! 거래 최종 승인 완료! 비트코인이 5만 8천 달러로 V자 반등했고, 우리가 청산 반등에서 1억 4천만 달러를 챙겼네! 자네가 서부 개척 시대를 길들였어, 파트너.",
                "hint": "변동성의 파도를 지배한 월가와 크립토 최고의 승부사다운 자부심.",
                "choices": [
                    ("Volatility is our oxygen, Bobby. When the machine cascades, human nerve dictates the winner. Transfer the profits to cold storage.", "변동성이야말로 우리의 산소입니다, 바비. 기계가 연쇄 청산에 빠질 때, 인간의 강철 담력이 승자를 결정합니다. 수익을 콜드 스토리지로 이관하십시오.", "native_killer", "'Volatility is our oxygen'은 전설적인 금융 드라마의 명대사를 능가하는 압도적 클로징입니다."),
                    ("I want to buy ten luxury watches and wear them all at once!", "명품 시계 10개 사서 양팔에 다 차고 다녀야지!", "wrong_konglish", "위대한 퀀트 트레이딩 승리 직후 졸부 같은 탐욕을 드러내는 천박한 언사입니다."),
                    ("Thank you Bobby, crypto charts make my eyes burn.", "감사합니다 바비, 코인 차트는 눈이 참 시리네요.", "mediocre", "역대급 플래시 크래시 반등 승리의 카타르시스를 살리지 못한 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Liquidation wick / Volatility is our oxygen",
        "key_note": "'Liquidation wick'은 대규모 청산으로 순간 형성되는 캔들 차트의 긴 꼬리, 'Volatility'는 시장 변동성을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 67: Tech (양자 암호 해독 브레이크스루 국가 안보)
    # -------------------------------------------------------------
    {
        "ep_num": 67,
        "title": "양자 암호 해독 브레이크스루: 국가 안보 명령 대치",
        "genre": "Tech",
        "speaker": "Linus Sterling (Chief Quantum Architect)",
        "emoji": "💻",
        "synopsis": "MIT-하버드 양자 컴퓨팅 극비 연구소. 4,096큐비트 양자 컴퓨터가 전 세계 RSA 암호화 체계를 30초 만에 무력화하는 쇼어 알고리즘 실증에 성공하자, 국방부 요원들이 연구실을 압류하고 국가 기밀 봉인 명령(National Security Letter)을 발부한다.",
        "turns": [
            {
                "dialogue": "Our quantum processor just cracked 4096-bit RSA encryption in twenty-eight seconds! But Homeland Security agents are at the door with a National Security Letter demanding we surrender our quantum source code. Do we hand it over or protect scientific freedom?",
                "korean": "우리 양자 프로세서가 28초 만에 4096비트 RSA 암호를 해독했어! 하지만 국토안보부 요원들이 문앞에서 국가안보서한(NSL)을 들이밀며 양자 소스코드를 넘기라고 요구하고 있네. 넘길 건가, 아니면 과학적 자유를 지킬 건가?",
                "hint": "군사 독점을 막기 위해 즉시 포스트-양자 암호(PQC) 오픈소스 패치를 전 세계에 무료 배포하여 인터넷 전체를 선제 방어한다.",
                "choices": [
                    ("Do not surrender exclusive offensive capability. Simultaneously open-source our Post-Quantum Lattice Cryptography patch to protect the global internet before they seize the servers.", "공격 역량을 군부에 독점시키지 마십시오. 서버가 압류되기 전에 전 세계 인터넷을 방어할 포스트-양자 격자 암호화 패치를 즉시 오픈소스로 전면 공개하십시오.", "native_killer", "'Post-Quantum Lattice Cryptography'와 오픈소스 공개는 암호학의 자유와 보안을 지키는 과학자의 가장 위대한 양심입니다."),
                    ("Sell the quantum code to the highest bidder on the dark web.", "다크웹에서 가장 높은 돈을 부르는 사람에게 양자 코드를 팔아넘깁시다.", "wrong_konglish", "전 세계 금융과 국방망을 테러범에게 넘겨주는 반인륜적 중범죄입니다."),
                    ("Break the quantum computer with a hammer so nobody can use it.", "망치로 양자 컴퓨터를 부숴서 아무도 못 쓰게 만듭시다.", "wrong_konglish", "인류 과학의 위대한 정점을 감정적으로 파괴하는 원시적 행동입니다.")
                ]
            },
            {
                "dialogue": "Patch committed to GitHub! The entire internet is upgrading to post-quantum encryption! But the federal agents are threatening to charge us under the Espionage Act for leaking cryptographic munitions. How do we stand our ground?",
                "korean": "패치가 깃허브에 커밋되었어! 인터넷 전체가 포스트-양자 암호로 업그레이드 중이야! 하지만 연방 요원들이 암호화 군수품 유출 혐의로 간첩법 기소를 협박하고 있어. 어떻게 맞설 텐가?",
                "hint": "버스타인 판례(Bernstein v. DOJ)를 인용해 소프트웨어 코드는 헌법상 보호받는 언론의 자유임을 선언한다.",
                "choices": [
                    ("Cite Bernstein versus Department of Justice: code is protected speech under the First Amendment. Inform the agents our legal defense is backed by the Electronic Frontier Foundation.", "버스타인 대 법무부 판례를 제시하십시오: 컴퓨터 코드는 수정헌법 제1조가 보호하는 표현의 자유입니다. 전자프론티어재단(EFF)이 변호인단을 구성했음을 통보하십시오.", "native_killer", "코드의 헌법적 자유를 수호한 역사적 판례를 구사하는 천재 과학자의 완벽한 법률적 방패입니다."),
                    ("Fall on your knees and beg the agents not to send you to jail.", "무릎을 꿇고 요원들에게 제발 감옥에만 보내지 말아 달라고 싹싹 빕시다.", "wrong_konglish", "자신의 위대한 과학적 신념을 스스로 배신하는 비겁한 굴복입니다."),
                    ("Tell the agents that computers are not real anyway.", "요원들에게 컴퓨터는 원래 가짜 세상이라고 엉뚱한 소리를 늘어놓읍시다.", "mediocre", "국가 비상 대치 상황에서 정신 나간 소리로 치부되는 발언입니다.")
                ]
            },
            {
                "dialogue": "The Attorney General ordered the agents to stand down! The White House praised our proactive defense of national digital infrastructure. You broke the cryptographic barrier and kept the world safe.",
                "korean": "법무장관이 요원 철수 명령을 내렸어! 백악관이 국가 디지털 인프라에 대한 우리의 선제적 방어를 공식 치하했네. 자네가 암호학의 장벽을 깼고 세상을 안전하게 지켜냈어.",
                "hint": "양자 시대를 열어젖힌 수석 아키텍트의 숭고한 과학적 사명감.",
                "choices": [
                    ("Mathematics belongs to all humanity, Linus. Let us calibrate the qubits for medical drug discovery and lead the quantum era forward.", "수학은 모든 인류의 공유 자산입니다, 리누스. 이제 신약 개발을 위해 큐비트를 캘리브레이션하고 양자 시대를 당당히 이끌어갑시다.", "native_killer", "군사적 파괴를 의학적 치유로 전환시키는 진정한 위대한 과학자의 비전입니다."),
                    ("I want to use the quantum computer to win the lottery jackpot!", "양자 컴퓨터로 복권 번호나 맞춰서 잭팟 터뜨려야지!", "wrong_konglish", "인류사적 과학 성과를 하찮은 도박에 쓰려는 천박한 발언입니다."),
                    ("Thank you Linus, quantum physics gives me insomnia.", "감사합니다 리누스, 양자물리학은 불면증을 유발하네요.", "mediocre", "역사적인 양자 혁명의 감격에 비해 지나치게 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Post-Quantum Cryptography / Code is speech",
        "key_note": "'Post-Quantum Cryptography'는 양자컴퓨터로도 뚫을 수 없는 차세대 격자 암호, 'Code is speech'는 코드가 헌법상 표현의 자유임을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 68: FBI (신디케이트 지하 카지노 위장 잠입 신분 노출)
    # -------------------------------------------------------------
    {
        "ep_num": 68,
        "title": "신디케이트 지하 카지노: 위장 잠입 요원의 정체 발각",
        "genre": "FBI",
        "speaker": "Don Falcone (Mob Boss & Underworld Kingpin)",
        "emoji": "🔍",
        "synopsis": "뉴욕 퀸즈 비밀 하이롤러 지하 카지노 VIP 룸. 거대 마피아 카르텔의 1억 달러 돈세탁 증거가 든 외장 하드를 확보하려는 순간, 조직의 보스가 당신의 가짜 신분증을 테이블에 던지며 권총의 공이치기를 당긴다.",
        "turns": [
            {
                "dialogue": "My capo says your offshore shipping company in Delaware doesn't exist on state tax rolls. You've been drinking my Scotch and playing my poker for three weeks. Are you a cop, or do you want to die right here?",
                "korean": "내 부두목이 델라웨어 주 세무 기록에 네 해운 회사가 없다고 보고했어. 3주 동안 내 스카치를 마시고 내 포커 테이블에 앉아 있었지. 경찰이야, 아니면 여기서 그냥 뒈질래?",
                "hint": "공포를 보이지 않고 거물 역외 자산가의 도도한 오만함으로 세무 은폐용 쉘 컴퍼니 구조를 설명해 역공한다.",
                "choices": [
                    ("If my private shipping fleet were visible on public tax rolls, Don Falcone, the IRS would have seized your fifty million last Tuesday. I pay fees for invisibility, not amateur exposure.", "만약 제 사설 선단이 공공 세무 기록에 떴다면, 팔코네 두목님, 지난주 화요일에 국세청이 당신의 5천만 달러를 압류했을 겁니다. 난 은폐를 위해 돈을 내지, 아마추어처럼 노출되지 않습니다.", "native_killer", "'Donnie Brasco'를 능가하는 위장 잠입 요원의 서늘하고 완벽한 블러핑이자 역제압입니다."),
                    ("Yes, I am an FBI agent! Please don't shoot me, I have a cat!", "네, 저 FBI 요원 맞아요! 제발 쏘지 마세요, 집에 고양이가 있어요!", "wrong_konglish", "잠입 신분을 스스로 인정하고 즉각 처형당하는 비참한 자살골입니다."),
                    ("I think your capo is confused, let me call my mom to check.", "당신 부두목이 착각한 것 같으니 우리 엄마한테 전화해서 물어볼게요.", "wrong_konglish", "지하 범죄 보스 앞에서 유아적 발언으로 비웃음과 총알을 자초합니다.")
                ]
            },
            {
                "dialogue": "He lowered the gun, but he slides a steel briefcase across the table. 'Prove your loyalty. Shoot this undercover informant in the chair behind you, and you're my partner forever.' SWAT is ninety seconds away. How do you stall?",
                "korean": "권총을 내렸지만, 철제 서류가방을 테이블 너머로 밀어주네. '네 충성심을 증명해봐. 뒤에 묶인 저 비밀 정보원을 직접 쏴. 그럼 넌 영원히 내 파트너다.' SWAT 진입까지 90초 남았어. 어떻게 시간을 벌 텐가?",
                "hint": "정보원을 직접 처형하지 않고, 그의 고문 디브리핑을 핑계 삼아 배후 공범의 자금 장부를 캐내야 한다며 시간을 번다.",
                "choices": [
                    ("Do not waste a bullet on an expendable mule. He holds the routing transit keys to the cartel's Zurich vault; let me interrogate his account hashes before we dispose of him.", "소모품 끄나풀에게 총알을 낭비하지 마십시오. 저자는 카르텔 취리히 금고의 라우팅 키를 쥐고 있습니다. 처분하기 전에 제가 계좌 해시부터 캐내겠습니다.", "native_killer", "정보원의 목숨을 살리면서도 탐욕스러운 보스의 호기심을 자극해 정확히 90초를 버는 천재적 기지입니다."),
                    ("Shoot the mob boss in the head right now with all six bodyguards watching.", "경호원 6명이 지켜보는 앞에서 두목 머리에 당장 총을 쏩시다.", "wrong_konglish", "순식간에 교차 사격으로 벌집이 되어 사망하는 무모한 행동입니다."),
                    ("Tell the informant that you are very sorry before pulling the trigger.", "방아쇠를 당기기 전에 정보원에게 정말 미안하다고 사과합시다.", "mediocre", "아군 요원을 살해하려는 명백한 살인 방조 행위입니다.")
                ]
            },
            {
                "dialogue": "Flashbangs detonated! 'FBI! Hands in the air!' SWAT breached the glass! Falcone and his crew are face down in zip-ties! Informant is safe, and the master hard drive is secured! Masterpiece in deep cover.",
                "korean": "섬광탄 작렬! 'FBI다! 손들어!' SWAT이 유리창을 깨고 진입했어! 팔코네와 부하들이 바닥에 엎드려 포박되었네! 정보원은 무사하고 마스터 하드드라이브도 확보했어! 위장 수사의 걸작이었네.",
                "hint": "생사의 기로에서 살아남아 거대 카르텔을 일망타진한 전설적인 요원의 보고.",
                "choices": [
                    ("Operation Checkmate complete. Read them their Miranda rights and transport the syndicate hard drives directly to the federal evidence vault.", "체크메이트 작전 완료. 저들에게 미란다 원칙을 고지하고 신디케이트 하드드라이브를 연방 증거 금고로 직송하십시오.", "native_killer", "위장 잠입의 팽팽한 긴장을 풀고 FBI 배지를 다시 찬 수사관의 당당한 위엄입니다."),
                    ("I want to steal all the poker chips from the table for myself!", "포커 테이블에 있는 칩들 내가 싹 다 훔쳐 가야지!", "wrong_konglish", "성공적인 작전 직후 절도범으로 전락하는 부끄러운 언사입니다."),
                    ("Thank you Agent Miller, undercover work is too scary.", "감사합니다 밀러 요원님, 위장 잠입은 너무 무섭네요.", "mediocre", "전설적인 잠입 수사의 영웅치고는 너무 나약한 푸념입니다.")
                ]
            }
        ],
        "key_expr": "Deep cover / Operation Checkmate",
        "key_note": "'Deep cover'는 장기간 신분을 위장해 적의 심장부에 침투하는 수사, 'Operation Checkmate'는 상대를 완벽히 제압한 작전명을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 69: Politics (하원 탄핵 표결 의원 휴게실 막후 거래)
    # -------------------------------------------------------------
    {
        "ep_num": 69,
        "title": "하원 탄핵 표결 1시간 전: 의원 휴게실 막후 거래",
        "genre": "Politics",
        "speaker": "Frank Underwood (House Majority Whip)",
        "emoji": "🏛️",
        "synopsis": "워싱턴 D.C. 국회의사당 하원 의원 전용 클록룸(Cloakroom). 대통령 탄핵소추안 본회의 표결 45분 전, 가결 정족수에 단 2표가 부족한 절체절명의 순간, 흔들리는 당내 반대파 의원들과 밀실 정치의 진검승부를 펼친다.",
        "turns": [
            {
                "dialogue": "Two votes short of two hundred sixteen! If the gavel falls and the impeachment resolution fails, the White House will decapitate our leadership by sunset. What leverage do you have on Congressman Vance?",
                "korean": "216표에서 딱 2표가 모자라! 의사봉이 내려치고 탄핵 결의안이 부결되면, 백악관이 해 지기 전에 우리 지도부의 목을 칠 거야. 밴스 의원을 꺾을 레버리지가 뭔가?",
                "hint": "무의미한 이상론 대신 의원의 지역구 핵심 인프라 예산과 국방위 위원장직 카드로 거래를 완성한다.",
                "choices": [
                    ("Promise his district the three-hundred-million naval shipyard modernization appropriation and offer him the gavel on Armed Services, or leak his offshore PAC logs.", "그의 지역구에 3억 달러 해군 조선소 현대화 예산을 배정하고 국방위원장 의사봉을 제안하십시오. 거절 시엔 해외 후원금 장부를 언론에 넘기겠다고 하십시오.", "native_killer", "'House of Cards'의 프랭크 언더우드가 구사하는 당근과 채찍의 가장 치명적인 원내총무 밀실 정치입니다."),
                    ("Beg him on your knees with tears in your eyes.", "눈물 흘리며 무릎 꿇고 그에게 제발 찬성표를 던져달라고 싹싹 빕시다.", "wrong_konglish", "의회 권력 투쟁에서 나약함을 드러내고 주도권을 완전히 헌납하는 자멸 행위입니다."),
                    ("Tell him that voting is just a game and he can flip a coin.", "투표는 그냥 게임일 뿐이니 동전이나 던져보라고 합시다.", "mediocre", "국가 헌정 질서가 걸린 탄핵 표결을 장난 취급하는 경박한 발언입니다.")
                ]
            },
            {
                "dialogue": "Vance caved and pledged his 'Aye'! But Congresswoman Hayes from Ohio is threatening to switch to 'Nay' on the House floor because of religious pressure from her diocese. The clerk is calling the roll!",
                "korean": "밴스가 굴복하고 찬성표를 맹세했어! 하지만 오하이오의 헤이즈 의원이 교구의 종교적 압력 때문에 본회의장에서 반대표로 돌아서겠다고 위협 중이야. 의사당 서기가 호명 투표를 시작했어!",
                "hint": "헌법 수호의 숭고한 역사적 소명을 일깨우며 그녀의 양심에 쐐기를 박는다.",
                "choices": [
                    ("Look her in the eyes at the rail: remind her that history remembers leaders who defend the Republic against tyrants, while cowards are forgotten footnotes.", "본회의장 난간에서 그녀의 눈을 응시하십시오: 역사는 폭군에 맞서 공화국을 지킨 지도자를 기억하지만, 비겁자는 잊혀진 각주에 불과하다는 점을 각인시키십시오.", "native_killer", "정치인의 마지막 양심과 역사적 명예심을 일깨우는 최고의 촌철살인 설득입니다."),
                    ("Lock her in the cloakroom toilet so she cannot vote.", "투표하러 못 나가게 휴게실 화장실에 그녀를 가둬버립시다.", "wrong_konglish", "국회의원 감금죄로 즉각 연방 교도소에 수감될 불법 폭력 행위입니다."),
                    ("Offer her ten dollars cash to vote our way.", "우리 쪽에 표를 던져주면 현금 10달러를 주겠다고 매수해봅시다.", "wrong_konglish", "의회 뇌물 수수 혐의로 탄핵 대상이 바뀔 황당한 발상입니다.")
                ]
            },
            {
                "dialogue": "Hayes voted 'Aye'! Gavel struck! Impeachment passes two-seventeen to two-fifteen! The Capitol erupted into pandemonium! You whipped the votes and broke the executive branch.",
                "korean": "헤이즈 의원이 찬성표를 던졌어! 의사봉이 내리쳤네! 탄핵안이 217대 215로 가결되었어! 의사당이 열광과 혼란의 도가니에 빠졌네! 자네가 표를 결집시켰고 행정부를 굴복시켰어.",
                "hint": "의회 권력의 정점에 선 원내총무의 냉혹하고 카리스마 넘치는 독백.",
                "choices": [
                    ("Democracy is so overrated, but power is absolute. Inform the Senate: the articles of impeachment are on their way.", "민주주의는 참 과대평가되어 있지만, 권력은 절대적입니다. 상원에 통보하십시오: 탄핵소추안이 지금 이송 중이라고.", "native_killer", "'House of Cards' 프랭크 언더우드의 시그니처 제4의 벽 독백을 완벽히 구현한 최고의 명대사입니다."),
                    ("I want to take the Speaker's gavel and hit people with it!", "하원의장 의사봉 빼앗아서 사람들 머리를 쥐어박고 싶네요!", "wrong_konglish", "역사적인 탄핵 가결 직후 미치광이 같은 폭력성을 드러내는 언사입니다."),
                    ("Thank you Frank, counting votes gives me a headache.", "감사합니다 프랭크, 표 세느라 머리가 참 아프네요.", "mediocre", "국정의 흐름을 뒤바꾼 정치적 대승리에 비해 지나치게 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Whip the votes / Articles of impeachment",
        "key_note": "'Whip the votes'는 의원들의 표를 결집해 당론을 관철하다, 'Articles of impeachment'는 정식 탄핵소추안을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 70: Culinary (암행 미슐랭 평가원과의 즉석 블라인드 테이스팅)
    # -------------------------------------------------------------
    {
        "ep_num": 70,
        "title": "암행 미슐랭 평가원: 주방 앞 즉석 블라인드 테이스팅",
        "genre": "Culinary",
        "speaker": "Chef Marco (Executive Head Chef & Restaurateur)",
        "emoji": "🔪",
        "synopsis": "뉴욕 센트럴파크 사우스 3스타 레스토랑. 마감 직전 혼자 온 신사가 수첩을 꺼내며 미슐랭 가이드 암행 수석 검사관임을 밝히고, 메뉴에 없는 오늘의 즉흥 요리로 레스토랑의 진정한 철학을 시험하겠다고 통보한다.",
        "turns": [
            {
                "dialogue": "The chief Michelin inspector just revealed his badge at table twelve! He is demanding a three-course blind menu using only whatever scraps we have left in the walk-in cooler tonight. How do we build this without prep?",
                "korean": "미슐랭 수석 평가관이 12번 테이블에서 신분증을 꺼냈어! 오늘 밤 냉장고에 남은 자투리 재료만으로 즉흥 3코스 블라인드 테이스팅을 내놓으라네. 사전 준비도 없이 어떻게 구성할 텐가?",
                "hint": "화려한 고급 식재료 대신 제로 웨이스트(Zero-waste) 철학과 극한의 조리 테크닉으로 감동을 이끌어낸다.",
                "choices": [
                    ("Embrace zero-waste gastronomy: turn roasted bone marrow and day-old sourdough into an umami panade, followed by charred allium broth and salt-cured cod collar.", "제로 웨이스트 미식을 선보이십시오: 구운 골수와 하루 지난 사워도우를 유화 퓨레로 만들고, 그을린 파 육수와 소금에 절인 대구 목살 구이로 이어가야 합니다.", "native_killer", "'The Bear'와 최고급 미슐랭 3스타들이 열광하는 'Zero-waste gastronomy'와 천재적인 재료 변용술입니다."),
                    ("Run across the street to McDonald's and plate a Big Mac with parsley.", "길 건너 맥도날드로 뛰어가서 빅맥 위에 파슬리나 얹어 대접합시다.", "wrong_konglish", "미슐랭 평가관을 모욕하고 레스토랑 등재를 영구 박탈당할 희대의 자살골입니다."),
                    ("Tell the inspector that the kitchen is closed and kick him out.", "주방 마감했으니 당장 나가라고 평가관을 쫓아냅시다.", "wrong_konglish", "세계 최고 미식 평가 기관과의 관계를 파탄 내는 최악의 문전박대입니다.")
                ]
            },
            {
                "dialogue": "He devoured the panade, but the cod collar is five minutes away and our pastry chef already went home! He wants an acidic dessert to cut through the richness. What can we spin from dry pantry staples?",
                "korean": "그가 퓨레를 싹싹 비웠지만, 대구 구이는 5분 남았고 디저트 셰프는 이미 퇴근했어! 기름진 맛을 씻어낼 산미 있는 디저트를 원하네. 마른 팬트리 재료로 무엇을 짜낼 텐가?",
                "hint": "발사믹 식초 리덕션과 올리브 오일, 거친 바다 소금을 곁들인 구운 배 소르베를 즉석에서 제조한다.",
                "choices": [
                    ("Poach winter pears in twenty-year aged balsamic and black pepper, spinning a flash-frozen olive oil gelato finished with flaky Maldon sea salt.", "20년 숙성 발사믹과 흑후추에 겨울 배를 졸이고, 말돈 천일염을 곁들인 급속 냉동 올리브 오일 젤라토를 즉석에서 완성하십시오.", "native_killer", "파인다이닝의 정점을 보여주는 천재적 감각의 즉흥 디저트 구성입니다."),
                    ("Give him a pack of fruit bubblegum from your pocket.", "주머니에서 과일 맛 풍선껌 하나 꺼내서 씹으라고 건넵시다.", "wrong_konglish", "미슐랭 3스타의 품격을 유치원생 장난으로 전락시키는 행동입니다."),
                    ("Pour plain white vinegar into a cup and call it fruit juice.", "식초를 컵에 따라서 과일 주스라고 속여서 내놓읍시다.", "wrong_konglish", "손님의 목을 태우고 응급실로 보내게 만드는 엽기적인 짓입니다.")
                ]
            },
            {
                "dialogue": "The inspector stood up and bowed to the open kitchen! He wrote in his leather book: 'An immaculate testament to culinary soul under fire.' We held our three stars!",
                "korean": "평가관이 자리에서 일어나 오픈 주방을 향해 정중히 고개 숙여 절했어! 가죽 수첩에 '극한의 위기 속에서 증명된 요리 영혼의 완전무결한 증거'라고 적었네. 3스타를 지켜냈어!",
                "hint": "요리의 영혼을 증명해낸 마스터 셰프의 숭고한 자부심.",
                "choices": [
                    ("True cooking is not about luxury truffles; it is about heart, discipline, and respect for the ingredient. Clean down the line, chefs. Yes, chef!", "진정한 요리는 사치스러운 트러플이 아니라, 가슴과 규율, 그리고 식재료에 대한 경외심입니다. 주방 청소를 시작하십시오. 예, 셰프!", "native_killer", "'The Bear'의 명대사 'Yes, Chef'와 주방의 규율을 완벽히 녹여낸 감동적인 피날레입니다."),
                    ("Now let's open champagne and dump it on each other's heads!", "이제 샴페인 따서 서로 머리에 들이붓고 난리 쳐보자!", "wrong_konglish", "신성한 주방에서 방종을 일삼아 프로 의식을 깎아먹는 행동입니다."),
                    ("Thank you Marco, cooking without recipes is too stressful.", "감사합니다 마르코, 레시피 없이 요리하는 건 참 스트레스네요.", "mediocre", "미슐랭 3스타를 수호한 역사적 순간치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "Zero-waste gastronomy / Yes, Chef!",
        "key_note": "'Zero-waste gastronomy'는 버려지는 식재료 없이 순환시키는 최고급 요리 철학, 'Yes, Chef!'는 주방의 절대적 규율과 신뢰를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 71: Espionage (동유럽 사이버 정전 안전가옥 탈출)
    # -------------------------------------------------------------
    {
        "ep_num": 71,
        "title": "동유럽 사이버 정전: 고립된 안전가옥 탈출 작전",
        "genre": "Espionage",
        "speaker": "Station Chief Carrie (CIA Covert Operations)",
        "emoji": "🕵️‍♂️",
        "synopsis": "동유럽 부쿠레슈티 외곽 산림 안전가옥. 적국의 사이버 공격으로 도시 전체 전력망이 블랙아웃되고 통신이 두절된 밤, 암살조 8명이 야간 투시경을 쓰고 안전가옥 외곽 철조망을 절단하기 시작한다.",
        "turns": [
            {
                "dialogue": "Power grid down, cellular towers jammed, and thermals show eight hostiles in suppressors breaching the outer perimeter sixty meters out! We have forty seconds before they flash-bang the living room! What is our tactical fallback?",
                "korean": "전력망 다운, 기지국 통신 먹통, 열화상 화면에 소음기를 단 적 8명이 60미터 밖 외곽 철조망을 뚫고 들어오고 있어! 거실로 섬광탄이 들이닥치기까지 40초 남았네! 전술적 퇴각로가 뭔가?",
                "hint": "정면 총격전의 수적 열세를 피하고, 지하실 보일러 연막 트랩을 작동시킨 뒤 지하 배수 수로로 탈출한다.",
                "choices": [
                    ("Rig the diesel furnace with timed thermite to blind their night-vision goggles, while we slip through the concealed sub-floor drainage conduit.", "디젤 보일러에 시한 테르밋을 설치해 적의 야간투시경을 실명시키는 섬광 연막을 터뜨리고, 바닥 밑 은폐 배수관으로 은밀히 빠져나가십시오.", "native_killer", "'Thermite flash'와 'sub-floor drainage conduit'는 수적 열세를 뒤집는 특수작전 생존술의 정점입니다."),
                    ("Walk out the front door with hands up and surrender immediately.", "손들고 앞문으로 당당히 걸어나가 즉각 항복합시다.", "wrong_konglish", "적 암살조에게 현장에서 확인 사살당하는 어리석은 자살 행위입니다."),
                    ("Hide under the bed and pull the blanket over your head.", "침대 밑으로 기어 들어가 이불을 머리끝까지 뒤집어씁시다.", "wrong_konglish", "특수 훈련을 받은 정보 요원으로서 수치스러운 유아적 행동입니다.")
                ]
            },
            {
                "dialogue": "Thermite ignited! Their assault team is disoriented in smoke! But our extraction truck stalled on the frozen river bridge with a punctured radiator. Hostile quadcopters are scanning the treeline. How do we make the border?",
                "korean": "테르밋 작렬! 적 공격조가 연기 속에서 혼란에 빠졌어! 하지만 우리 탈출 트럭이 라디에이터 파손으로 얼어붙은 강 다리 위에서 멈췄네. 적 드론들이 숲을 수색 중이야. 국경을 어떻게 넘을 텐가?",
                "hint": "열상 추적을 피하기 위해 은박 비상 담요를 뒤집어쓰고 강변 협곡을 도보 돌파한다.",
                "choices": [
                    ("Ditch the vehicle, wrap ourselves in thermal Mylar cloaks to defeat drone infrared sensors, and navigate down the gorge toward the NATO border post.", "차량을 유기하고 열 적외선 차단 마일러 망토를 둘러 드론 탐지를 무력화한 뒤, 협곡을 따라 NATO 국경 검문소로 도보 기동하십시오.", "native_killer", "드론 적외선 감시망을 무력화하는 최첨단 위장 침투 전술입니다."),
                    ("Light a giant campfire on the bridge so the helicopters can see us.", "헬기가 우리를 잘 볼 수 있도록 다리 위에 커다란 모닥불을 피웁시다.", "wrong_konglish", "적 공격 헬기에게 미사일 표적 좌표를 스스로 찍어주는 자폭 행위입니다."),
                    ("Sit on the ice and cry until someone comes to rescue us.", "누가 구하러 올 때까지 얼음 위에 주저앉아 엉엉 웁시다.", "mediocre", "저체온증으로 얼어 죽고 기밀을 모두 빼앗기는 나약한 처신입니다.")
                ]
            },
            {
                "dialogue": "Crossed the border line! NATO armored vehicles secured our perimeter! The intelligence dossier is safe, and Langley just confirmed zero casualties. You brought us through the fire, Carrie.",
                "korean": "국경선 돌파! NATO 장갑차들이 우리 외곽을 안전하게 감쌌네! 정보 기밀 서류도 무사하고 랭글리 본부에서 사상자 0명을 확인했어. 자네가 지옥의 불길을 뚫고 우리를 구해냈네, 캐리.",
                "hint": "사선을 넘나들며 아군과 국가를 지켜낸 첩보 사령관의 서늘한 결의.",
                "choices": [
                    ("No agent left behind. Sterilize our gear, secure encrypted comms with Washington, and let our enemies know: America never blinks in the dark.", "단 한 명의 요원도 남겨두지 않는다. 장비를 멸균 정리하고 워싱턴과 암호 통신을 연결하십시오. 그리고 적들에게 알리십시오: 미국은 어둠 속에서도 눈 하나 깜빡이지 않는다고.", "native_killer", "'Homeland'의 캐리 매티슨을 연상시키는 불굴의 투지와 애국심이 빛나는 명대사입니다."),
                    ("I want to drink ten cups of hot soup and take a two-week vacation!", "따뜻한 국물 10그릇 마시고 2주 동안 휴가나 갈래요!", "wrong_konglish", "사선을 넘은 직후 엄정한 군사 보안 규율을 망각한 사적 투정입니다."),
                    ("Thank you Carrie, winter in Eastern Europe is too cold.", "감사합니다 캐리, 동유럽 겨울은 너무 춥네요.", "mediocre", "목숨을 건 탈출 작전의 전율에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Thermal Mylar / Never blink in the dark",
        "key_note": "'Thermal Mylar'는 체온 적외선 방출을 차단하는 특수 은박 시트, 'Never blink'는 위기 앞에서도 결코 물러서지 않음을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 72: Aviation (에어포스 원 공중 급유 비상사태)
    # -------------------------------------------------------------
    {
        "ep_num": 72,
        "title": "공군 1호기(에어포스 원): 공중 급유 비상사태",
        "genre": "Aviation",
        "speaker": "Colonel Mason (Presidential Command Pilot)",
        "emoji": "✈️",
        "synopsis": "대서양 상공 고도 3만 피트. 유럽 순방 중 적국의 전자기 펄스(EMP) 공격으로 에어포스 원의 주 연료 펌프가 손상되어 잔여 연료가 15분 남은 상황에서, 맹렬한 폭풍우를 뚫고 KC-135 공중급유기와의 사투 끝에 공중 급유 붐(Boom) 도킹을 성사시켜야 한다.",
        "turns": [
            {
                "dialogue": "Fuel pressure critical! Ten minutes of fuel remaining with the President of the United States aboard! Severe thunderstorm turbulence is pitching the refueling tanker four feet up and down! Can you hook the boom, Colonel?!",
                "korean": "연료 압력 임계치 도달! 미합중국 대통령이 탑승한 상태에서 잔여 연료 10분! 극심한 뇌우 난기류로 급유기가 상하로 4피트씩 요동치고 있어! 공중 급유 붐을 도킹할 수 있겠나, 대령?!",
                "hint": "자동 조종을 해제하고 수동 비행으로 급유기의 와류(Wake turbulence)를 파고들어 정밀 도킹한다.",
                "choices": [
                    ("Disengage flight director. Hand-fly the stick, lock visual sight on the tanker's belly director lights, and maintain closure rate at precisely one knot.", "비행 디렉터를 해제하십시오. 수동 비행으로 전환하고 급유기 하부 유도등에 시선을 고정한 채 접근 속도를 정확히 1노트로 유지하며 도킹하겠습니다.", "native_killer", "'Air Force One'과 군용 항공술의 최고봉인 수동 공중 급유 정밀 조종술입니다."),
                    ("Tell the President to jump out with an umbrella like Mary Poppins.", "대통령에게 메리 포핀스처럼 우산을 펴고 뛰어내리라고 합시다.", "wrong_konglish", "국가 원수를 공중에서 추락사시키려는 정신 나간 망언입니다."),
                    ("Turn off all four jet engines to glide like a paper airplane.", "종이비행기처럼 활공할 수 있게 제트엔진 4개를 다 꺼버립시다.", "wrong_konglish", "고도 3만 피트에서 양력을 잃고 폭풍우 속으로 추락하는 미친 짓입니다.")
                ]
            },
            {
                "dialogue": "Contact! Boom latched! Fuel transferring at five thousand pounds a minute! But lightning just struck the tanker's left wing, triggering electrical arcing near the nozzle! If a spark ignites vapor, both planes explode! Break away or hold?!",
                "korean": "접촉 성공! 급유 붐 걸렸다! 분당 5천 파운드로 연료 이송 중! 하지만 번개가 급유기 왼쪽 날개를 때려 노즐 근처에 전기 아크가 튀고 있어! 스파크가 유증기에 닿으면 두 비행기 다 폭발해! 분리할 텐가, 버틸 텐가?!",
                "hint": "질소 불활성화 시스템을 급유 배관에 즉각 가동하고 필요 최소량 급유 즉시 안전 분리한다.",
                "choices": [
                    ("Activate nitrogen inerting purge in the fuel manifold immediately, take two thousand pounds for safe diversion, and execute emergency breakaway on my mark.", "급유 매니폴드에 질소 불활성화 퍼지를 즉시 가동하고, 비상 회항에 필요한 2천 파운드만 취한 뒤 제 신호에 맞춰 비상 이탈을 감행하십시오.", "native_killer", "'Nitrogen inerting purge'와 정밀한 안전 분리(Breakaway)는 공중 폭발을 막는 완벽한 프로토콜입니다."),
                    ("Pray to the lightning gods to make the fire cold.", "번개 신에게 불길을 차갑게 식혀달라고 기도합시다.", "wrong_konglish", "과학적 조종실에서 미신에 기대어 비행기 폭발을 방치하는 한심한 태도입니다."),
                    ("Tell the copilot to open the window and blow on the spark.", "부조종사에게 창문을 열고 입으로 불어서 스파크를 끄라고 시킵시다.", "wrong_konglish", "고도 3만 피트에서 여압을 날리고 조종사를 사망시키는 엽기적인 소리입니다.")
                ]
            },
            {
                "dialogue": "Breakaway executed! Tanker cleared! Fuel tanks green with four hours of reserve! Runway lights at Andrews Air Force Base are on the horizon. Outstanding airmanship, pilot. You saved the Commander-in-Chief.",
                "korean": "비상 이탈 성공! 급유기 분리 완료! 4시간 치 예비 연료 확보 녹색 점등! 앤드루스 공군기지 활주로 유도등이 지평선에 보이고 있어. 탁월한 비행 기량이었네, 조종사. 자네가 최고통수권자를 구했어.",
                "hint": "국가 원수의 전용기를 사선에서 구해낸 대통령 전담 조종사의 명예로운 보고.",
                "choices": [
                    ("Air Force One is inbound, steady and secure. Mission completed without a scratch on the seal of the President.", "에어포스 원 접근 중, 안전하고 견고함. 대통령의 휘장에 티끌 하나 묻히지 않고 임무를 완수했습니다.", "native_killer", "대통령 전담 비행단의 자부심과 숭고한 충성심이 묻어나는 감동적인 피날레입니다."),
                    ("Now I want the President to give me a million dollars cash bonus!", "이제 대통령이 나한테 현금 10억 보너스 줘야지!", "wrong_konglish", "군인의 숭고한 사명감을 사적 금전 탐욕으로 더럽히는 언사입니다."),
                    ("Thank you Mason, flying in storms makes me dizzy.", "감사합니다 메이슨 대령님, 폭풍우 비행은 참 어지럽네요.", "mediocre", "에어포스 원 비상 착륙의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Nitrogen inerting purge / Breakaway executed",
        "key_note": "'Nitrogen inerting'은 유증기 폭발을 막는 불활성 질소 정화 기술, 'Breakaway'는 급유 비상 이탈 기동을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 73: Sports Management (올림픽 도핑 스캔들 폭로)
    # -------------------------------------------------------------
    {
        "ep_num": 73,
        "title": "올림픽 도핑 스캔들: 금메달 박탈과 양심의 기로",
        "genre": "Sports Management",
        "speaker": "Jerry Maguire (Veteran Sports Agent)",
        "emoji": "🏈",
        "synopsis": "로잔 국제올림픽위원회(IOC) 본부 호텔. 당신의 소속사 간판 스타이자 100m 금메달리스트 선수가 코치의 강요로 복용한 미승인 펩타이드 도핑 양성 반응 통보를 받자, 1억 달러 스폰서십을 지킬지 양심 선언을 할지 결단해야 한다.",
        "turns": [
            {
                "dialogue": "WADA detected micro-doses of synthetic peptide in sample A. The pharmaceutical sponsor is offering five million to suppress the lab B-sample. If we blow the whistle, our agency loses fifty million in commissions. What do you advise our athlete?",
                "korean": "세계반도핑기구(WADA)가 A샘플에서 미세 합성 펩타이드를 검출했어. 제약 스폰서가 B샘플 검사를 은폐해 주는 대가로 5백만 달러를 주겠대. 우리가 내부 고발하면 에이전시 수수료 5천만 달러가 날아가. 우리 선수에게 뭐라고 조언할 텐가?",
                "hint": "은폐의 유혹을 뿌리치고, 코치의 강압 투여 사실을 선제적으로 자진 신고하여 선수의 출전 자격과 인간적 존엄성을 구한다.",
                "choices": [
                    ("Do not touch that dirty money. Come forward proactively to WADA: expose the rogue coach's coercive protocol, seek mitigated cooperation, and protect the kid's soul.", "그 더러운 돈에 손대지 마십시오. WADA에 선제적으로 자진 신고하십시오: 악덕 코치의 강압적 투여 전말을 폭로하고 협력 감경을 받아내어 이 선수의 영혼을 구해야 합니다.", "native_killer", "'Jerry Maguire'의 진정한 정수인 돈보다 인간의 양심과 선수의 인생을 우선시하는 위대한 리더십입니다."),
                    ("Take the five million and drink champagne with the corrupt coach.", "5백만 달러 챙기고 부패한 코치랑 샴페인이나 마십시다.", "wrong_konglish", "스포츠맨십을 버리고 사기 및 은폐 공범으로 감옥에 갈 자멸 행위입니다."),
                    ("Tell the athlete to run away to another country and change his name.", "선수에게 다른 나라로 도망가서 개명하고 살라고 시킵시다.", "wrong_konglish", "선수의 커리어와 인생을 파탄 내는 무책임하고 황당한 발언입니다.")
                ]
            },
            {
                "dialogue": "The rogue coach is threatening to sue us for defamation and claims he has a signed waiver from the athlete. We have thirty minutes before the international press conference. How do you take control of the narrative?",
                "korean": "악덕 코치가 명예훼손으로 고소하겠다고 협박하며 선수 서명이 든 면책 각서를 흔들고 있어. 국제 기자회견까지 30분 남았네. 언론 프레임을 어떻게 장악할 텐가?",
                "hint": "선수 본인이 직접 단상에 서서 눈물의 참회와 함께 스포츠계 약물 카르텔 척결을 선언하게 한다.",
                "choices": [
                    ("Put the athlete on the podium: let him take moral accountability with complete vulnerability, while presenting our audio evidence of the coach's blackmail.", "선수를 단상에 세우십시오: 완전히 진실된 태도로 도덕적 책임을 인정하게 하고, 코치의 협박이 담긴 음성 녹취 증거를 언론에 공개하십시오.", "native_killer", "여론의 심판을 극적인 지지와 개혁의 아이콘으로 전환시키는 정통 위기관리 PR입니다."),
                    ("Deny everything on Twitter and call the Olympic committee liars.", "트위터에서 전면 부인하고 올림픽 위원회가 거짓말쟁이라고 욕합시다.", "wrong_konglish", "증거 앞에서 발뺌하여 전 세계적인 조롱거리로 전락하는 최악의 패착입니다."),
                    ("Tell the reporters that winning is all that matters anyway.", "기자들에게 어차피 이기는 게 전부 아니냐고 뻔뻔하게 대답합시다.", "wrong_konglish", "스포츠의 모든 가치를 부정하여 영구 제명 처분을 자초하는 망언입니다.")
                ]
            },
            {
                "dialogue": "The world wept with him. WADA gave him a reduced six-month suspension and praised his courage, while the corrupt coach was arrested! Nike just signed him as their anti-doping reform ambassador! You saved his life, Jerry.",
                "korean": "전 세계가 선수와 함께 울었어. WADA는 용기를 칭찬하며 6개월 경감 출전정지만 내렸고 부패한 코치는 체포되었네! 나이키가 그를 반도핑 개혁 앰버서더로 전속 계약했어! 자네가 그의 인생을 구했네, 제리.",
                "hint": "양심과 진실이 물질적 탐욕을 이긴 스포츠 에이전트의 감동적인 피날레.",
                "choices": [
                    ("Show me the heart, and the money follows. Stand tall, champion; redemption is the greatest comeback in sports history.", "진심을 보여주면, 돈은 저절로 따라오는 법입니다. 고개를 드십시오, 챔피언; 구원이야말로 스포츠 역사상 가장 위대한 역전극입니다.", "native_killer", "'Show me the money'를 뛰어넘어 진정한 인간 승리를 보여주는 불멸의 스포츠 드라마 명대사입니다."),
                    ("I knew Nike would give us money, I am so greedy!", "나이키가 돈 줄 줄 알았어, 나 진짜 탐욕스럽다!", "wrong_konglish", "감동적인 구원의 순간을 사적 탐욕으로 더럽히는 저급한 태도입니다."),
                    ("Thank you Jerry, sports press conferences are very tiring.", "감사합니다 제리, 스포츠 기자회견은 참 피곤하네요.", "mediocre", "역사적인 선수의 구원 앞에서 무미건조한 반응입니다.")
                ]
            }
        ],
        "key_expr": "Redemption comeback / Show me the heart",
        "key_note": "'Redemption comeback'은 과오를 딛고 일어서는 구원의 역전극, 'Show me the heart'는 영혼을 울리는 진정성을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 74: Haute Couture (밀라노 런웨이 환경운동가 난입)
    # -------------------------------------------------------------
    {
        "ep_num": 74,
        "title": "밀라노 런웨이: 기습 시위대 난입과 즉흥 쇼 디렉팅",
        "genre": "Haute Couture",
        "speaker": "Miranda Priestly (Vogue Global Editor)",
        "emoji": "👠",
        "synopsis": "밀라노 패션위크 피날레 런웨이 쇼. 쇼 종료 2분을 남겨두고 기후 활동가 6명이 붉은 친환경 페인트를 들고 런웨이로 난입하는 비상사태 속에서, 쇼를 폭력적으로 중단시키지 않고 친환경 재생 패션의 퍼포먼스 아트로 승화시켜야 한다.",
        "turns": [
            {
                "dialogue": "Protesters with red dye just leaped onto the runway in front of the bridal gown! Security wants to tackle them violently on live television. Anna Wintour is frowning. How do you save this show without bloodshed?!",
                "korean": "붉은 염료를 든 시위대가 웨딩드레스 바로 앞 런웨이로 뛰어들었어! 보안요원들은 생방송 카메라 앞에서 저들을 무력으로 진압하려 해. 안나 윈투어가 인상을 찌푸리고 있네. 유혈 사태 없이 이 쇼를 어떻게 살릴 텐가?!",
                "hint": "폭력 진압을 제지하고, 음악을 아방가르드 비트로 바꾸며 모델들이 시위대와 즉흥 행위예술로 어우러지게 연출한다.",
                "choices": [
                    ("Wave off security. Shift the runway music to deep cello drone, and instruct our lead muse to embrace the dye as dynamic performance art.", "보안요원을 제지하십시오. 런웨이 음악을 묵직한 첼로 드론으로 전환하고, 우리 뮤즈가 붉은 염료를 역동적인 행위예술로 승화시켜 포옹하게 하십시오.", "native_killer", "알렉산더 맥퀸의 전설적인 로봇 페인트 분사 쇼를 능가하는 천재 패션 디렉터의 극적인 순발력입니다."),
                    ("Tell the guards to beat up the protesters with iron sticks.", "경비원들에게 쇠파이프로 시위대를 두들겨 패라고 명령합시다.", "wrong_konglish", "전 세계 생중계에서 폭력 참사를 일으켜 브랜드를 영구 매장시키는 최악의 망동입니다."),
                    ("Turn off all the lights and run out of the building screaming.", "조명을 다 끄고 비명 지르며 건물 밖으로 도망칩시다.", "wrong_konglish", "패션계의 여왕 앞에서 패닉에 빠져 도망치는 수치스러운 행동입니다.")
                ]
            },
            {
                "dialogue": "The muse twirled through the crimson mist! The contrast against the pure raw silk looks like an operatic masterpiece! But the activist leader is freezing up in front of the cameras. What is your stage direction?",
                "korean": "뮤즈가 진홍빛 안개 속을 우아하게 회전했어! 순백의 로 실크와 대비되는 붉은빛이 오페라 걸작 같아! 하지만 시위대 리더가 카메라 앞에서 얼어붙었네. 무대 디렉팅이 뭔가?",
                "hint": "시위대의 손을 잡고 런웨이를 함께 걸으며 지속 가능한 패션 혁명의 메시지를 완성한다.",
                "choices": [
                    ("Have the muse take the activist's hand and walk the finale together; crown the moment as a joint manifesto for regenerative haute couture.", "뮤즈가 시위대 리더의 손을 잡고 함께 피날레를 워킹하게 하십시오; 이 순간을 재생 가능한 오뜨 꾸뛰르를 향한 공동 선언문으로 장식하십시오.", "native_killer", "위기를 글로벌 패션계의 가장 위대한 환경 선언으로 승화시키는 마스터 디렉팅입니다."),
                    ("Push the activist off the stage so he breaks his leg.", "시위대를 무대 아래로 밀어버려서 다리를 부러뜨립시다.", "wrong_konglish", "생방송에서 상해 범죄를 저지르는 잔인하고 어리석은 짓입니다."),
                    ("Tell the activist that his jacket looks very cheap.", "시위대에게 너 입고 있는 재킷 참 싸구려 같다고 조롱합시다.", "mediocre", "예술적 절정에서 유치한 텃세나 부리는 천박한 태도입니다.")
                ]
            },
            {
                "dialogue": "Standing ovation! The New York Times just headlined: 'The Most Revolutionary Runway in Milan History.' Even Anna Wintour smiled. You turned chaos into pure genius, darling.",
                "korean": "전원 기립 박수! 뉴욕타임스가 방금 헤드라인으로 뽑았어: '밀라노 역사상 가장 혁명적인 런웨이.' 안나 윈투어마저 미소를 지었네. 자네가 혼돈을 순수한 천재성으로 바꿨어, 달링.",
                "hint": "패션의 패러다임을 바꾼 위대한 크리에이티브 디렉터의 세련된 클로징.",
                "choices": [
                    ("Fashion is not an ornament; it is a cultural mirror. Thank you, Miranda; tomorrow we draft our zero-waste sustainability charter.", "패션은 단순한 장신구가 아니라, 시대를 비추는 문화의 거울입니다. 감사합니다, 미란다; 내일부터 우리의 제로 웨이스트 지속가능성 헌장을 기초하겠습니다.", "native_killer", "'Fashion is a cultural mirror'는 패션 철학의 정점을 찍는 품격 있는 명언입니다."),
                    ("I want to sell that paint-stained dress for ten million euros!", "그 페인트 묻은 드레스 100억에 팔아먹어야지!", "wrong_konglish", "예술적 승리 직후 돈벌이 탐욕을 드러내는 천박한 언사입니다."),
                    ("Thank you Miranda, fashion shows are very loud.", "감사합니다 미란다, 패션쇼는 참 시끄럽네요.", "mediocre", "역사에 남을 런웨이 혁명의 감격을 단순 소음으로 치부하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Cultural mirror / Regenerative couture",
        "key_note": "'Cultural mirror'는 시대를 투영하는 거울로서의 패션, 'Regenerative couture'는 지속 가능한 친환경 명품 의상을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 75: Crisis PR (항공기 엔진 폭발 비상착륙 미디어 워룸)
    # -------------------------------------------------------------
    {
        "ep_num": 75,
        "title": "항공기 엔진 폭발 비상착륙: 미디어 워룸 지휘",
        "genre": "Crisis PR",
        "speaker": "Olivia Pope (Senior Crisis PR Managing Director)",
        "emoji": "🎙️",
        "synopsis": "워싱턴 D.C. 글로벌 항공사 위기관리 본부. 승객 240명을 태운 대형 여객기가 이륙 직후 1번 엔진 폭발로 필라델피아 공항에 동체 착륙 중인 실시간 영상이 CNN에 생중계되는 순간, 주가 폭락과 승객 가족들의 공황을 수습해야 한다.",
        "turns": [
            {
                "dialogue": "Flames shooting from engine one! Social media is screaming that twenty passengers were sucked out of the cabin! The FAA is preparing to ground our entire fleet of four hundred jets. How do we take command of the airwaves?",
                "korean": "1번 엔진에서 화염이 치솟고 있어! 소셜 미디어에는 승객 20명이 기체 밖으로 빨려 나갔다는 가짜 루머가 도배 중이야! FAA는 우리 400대 전 기종 운항 정지를 준비하고 있네. 방송 전파를 어떻게 장악할 텐가?",
                "hint": "미확인 루머를 팩트로 즉각 불식시키고, 승객 전원 생존 착륙 사실과 조종사의 영웅적 비행술을 생방송으로 발표한다.",
                "choices": [
                    ("Establish our CEO live at the podium: confirm emergency landing completed with zero fatalities, praise the captain's heroic airmanship, and open a 24/7 dedicated family hotline.", "대표이사를 즉각 단상에 세우십시오: 사망자 0명으로 비상 착륙이 완료되었음을 확언하고, 기장의 영웅적 비행술에 경의를 표하며 24시간 가족 전담 핫라인을 개설하십시오.", "native_killer", "'Zero fatalities', 'dedicated family hotline'은 항공 재난 PR의 바이블 같은 완벽한 대응입니다."),
                    ("Tell the press that flying on airplanes is always a gamble.", "기자들에게 원래 비행기 타는 건 언제나 도박 같은 일이라고 지껄입시다.", "wrong_konglish", "항공사 면허를 취소당하고 전 세계적인 공분을 부르는 패륜적 망언입니다."),
                    ("Hide behind the desk and turn off all company telephones.", "책상 뒤에 숨어서 회사 모든 전화선을 뽑아버립시다.", "wrong_konglish", "패닉을 극대화하고 기업 평판을 영구히 파멸시키는 최악의 직무 유기입니다.")
                ]
            },
            {
                "dialogue": "Rumors killed, but union engineers are leaking that maintenance warned of fan blade titanium fatigue three weeks ago! The Department of Justice is talking about criminal manslaughter. How do you defend corporate integrity?",
                "korean": "루머는 잡았으나, 노조 엔지니어들이 3주 전에 티타늄 팬 블레이드 피로 균열을 경고했다는 내부 문건을 유출했어! 법무부는 과실치사 혐의를 거론하고 있네. 기업의 진실성을 어떻게 수호할 텐가?",
                "hint": "은폐를 전면 배제하고, NTSB에 전면 협조하며 전 기종 자발적 초음파 전수 검사를 선제적으로 공표한다.",
                "choices": [
                    ("Do not conceal: announce full cooperation with NTSB, ground all fleet engine variants voluntarily for ultrasonic inspection, and establish an independent audit commission.", "절대 은폐하지 마십시오: NTSB 조사에 전면 협조를 선언하고, 전 기종 엔진을 자발적 초음파 전수 점검에 들어가며 독립적인 외부 감사위원회를 발족하십시오.", "native_killer", "위기를 자발적 투명성과 안전 혁신의 계기로 전환시키는 최정상 위기관리 기법입니다."),
                    ("Burn the maintenance records in a metal trash can secretly.", "쇠 쓰레기통에 정비 기록들을 넣고 몰래 불태워버립시다.", "wrong_konglish", "증거인멸죄로 임원 전원이 즉각 수갑을 차는 중범죄 행위입니다."),
                    ("Blame the engine manufacturer and sue them for twenty billion.", "모든 탓을 엔진 제작사에 돌리고 200억 달러 소송이나 겁시다.", "mediocre", "책임 회피로 비쳐 비난 여론을 증폭시키는 미숙한 처신입니다.")
                ]
            },
            {
                "dialogue": "Ultrasonic inspection completed! NTSB commended our voluntary transparency, and airline passenger bookings actually rose eight percent due to trust! You steered this airline through a Category 5 PR hurricane.",
                "korean": "초음파 전수 검사 완료! NTSB가 우리의 자발적 투명성을 공식 치하했고, 신뢰 회복으로 항공권 예약률이 오히려 8% 상승했네! 자네가 5등급 PR 허리케인을 뚫고 항공사를 지켜냈어.",
                "hint": "위기를 신뢰의 발판으로 승화시킨 위기관리 사령관의 묵직한 긍지.",
                "choices": [
                    ("Safety is not a marketing slogan; it is a moral promise. Excellent crisis containment, team; now let us reward that heroic flight crew.", "안전은 마케팅 구호가 아니라 도덕적 약속입니다. 훌륭한 위기 수습이었습니다; 이제 그 영웅적인 승무원들에게 합당한 포상을 내립시다.", "native_killer", "'Safety is a moral promise'는 기업 위기관리의 영원한 금과옥조입니다."),
                    ("I want free lifetime first-class tickets for myself and my friends!", "나랑 내 친구들 평생 퍼스트클래스 무료 탑승권 챙겨줘야지!", "wrong_konglish", "성공적인 위기 수습 직후 개인적 특혜를 탐하는 천박한 태도입니다."),
                    ("Thank you Olivia, answering angry reporters gives me a headache.", "감사합니다 올리비아, 화난 기자들 상대하느라 머리가 참 아프네요.", "mediocre", "기업을 구원해낸 웅장한 순간치고는 너무 시시한 불평입니다.")
                ]
            }
        ],
        "key_expr": "Moral promise / Ultrasonic inspection",
        "key_note": "'Moral promise'는 도덕적 약속, 'Ultrasonic inspection'은 비파괴 초음파 안전 검사를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 76: Luxury Real Estate (두바이 팜 주메이라 메가맨션 2억 불 에스크로)
    # -------------------------------------------------------------
    {
        "ep_num": 76,
        "title": "두바이 팜 주메이라: 2억 달러 메가맨션 에스크로",
        "genre": "Luxury Real Estate",
        "speaker": "Ryan Serhant (Global Super-Broker)",
        "emoji": "🏙️",
        "synopsis": "두바이 팜 주메이라 인공섬 최고급 프론드 해변. 개인 인피니티 비치와 헬리패드가 딸린 2억 달러짜리 초대형 메가맨션을 두고, 유럽의 암호화폐 억만장자와 걸프만 국부펀드가 자정 은행 영업 종료 30분 전 사상 최대의 에스크로 대결을 벌인다.",
        "turns": [
            {
                "dialogue": "We have two buyers at two hundred million dollars: a Swiss crypto billionaire wiring via central bank digital currency, and an Abu Dhabi sovereign fund with a certified wire. How do you close before midnight without regulatory seizure?",
                "korean": "2억 달러에 두 매수인이 붙었어: 중앙은행 디지털 화폐로 송금하려는 스위스 암호화폐 억만장자와 공인 송금을 준비한 아부다비 국부펀드야. 자정 전 규제 당국의 동결 없이 어떻게 클로징할 텐가?",
                "hint": "송금 승인 지연 위험이 있는 암호화폐 대신, 즉각 청산이 보장된 국부펀드의 공식 국책은행 에스크로를 선택한다.",
                "choices": [
                    ("Lock the contract with the sovereign fund via Dubai Land Department's instant escrow ledger, while offering the crypto titan an exclusive right of first refusal on the adjacent beachfront parcel.", "두바이 토지부 즉시 에스크로 원장을 통해 국부펀드와 계약을 확정하고, 암호화폐 거물에겐 인접 비치프론트 부지의 독점 우선협상권을 부여하십시오.", "native_killer", "'Right of first refusal'로 양쪽 VIP 모두를 만족시키며 2억 달러를 클로징하는 탑 브로커의 신의 한 수입니다."),
                    ("Ask both buyers to wrestle on the beach, winner takes the house.", "두 매수인에게 해변에서 모래씨름을 시켜서 이긴 사람이 집을 갖게 합시다.", "wrong_konglish", "2천억 대 자산가들을 조롱하고 거래를 모조리 날려버리는 미친 짓입니다."),
                    ("Take both buyers' money and run away to a tropical island.", "두 사람 돈을 둘 다 받고 열대 섬으로 야반도주합시다.", "wrong_konglish", "국제 사기 혐의로 인터폴 적색수배자가 되는 어처구니없는 발상입니다.")
                ]
            },
            {
                "dialogue": "Fund accepted! Two hundred million cleared! But the developer claims the custom Italian marble imported from Carrara was not included in the fixtures clause and demands ten million extra at the signing table!",
                "korean": "펀드가 수락했어! 2억 달러 송금 완료! 하지만 시행사 측에서 카라라산 수입 맞춤 대리석은 설비 부속물 조항에서 제외되었다며 서명 테이블에서 1천만 달러를 추가 요구하네!",
                "hint": "시행사의 얄팍한 추가 요금 갈취를 계약서의 '완전 합의 조항(Merger Clause)'으로 단칼에 무력화한다.",
                "choices": [
                    ("Invoke Section 14 Merger and Integration Clause: all structural marble fixtures are contractually unified with the deed, and any last-minute extortion triggers immediate liquidated damages.", "제14조 완전통합조항(Merger Clause)을 들이대십시오: 모든 대리석 구조물은 계약상 등기와 일체화되어 있으며, 막판 부당 요구는 즉각적인 위약금 청구 사유임을 경고하십시오.", "native_killer", "'Merger Clause'와 'liquidated damages'는 부동산 계약 막판의 억지 트집을 분쇄하는 철벽 법률 방패입니다."),
                    ("Rip out the marble with crowbars and leave a giant dirt hole.", "쇠지레로 대리석을 뜯어내고 거대한 흙구덩이로 놔둡시다.", "wrong_konglish", "2억 달러짜리 초호화 맨션을 폐허로 만드는 정신 나간 파괴 행위입니다."),
                    ("Pay the ten million out of your own wallet and cry.", "자기 지갑에서 1천만 달러를 꺼내 대신 내주고 웁시다.", "wrong_konglish", "자신의 중개 수수료를 털어 상대의 갈취를 용인하는 어리석은 처신입니다.")
                ]
            },
            {
                "dialogue": "Deed stamped by the Dubai government! Two hundred million dollars finalized! Largest residential real estate transaction in Middle Eastern history! You just conquered the desert, Ryan.",
                "korean": "두바이 정부 공식 등기 날인 완료! 2억 달러 계약 최종 완결! 중동 역사상 최대 규모의 주거용 부동산 거래 기록 경신! 자네가 사막을 정복했어, 라이언.",
                "hint": "세계 최고 하이엔드 부동산 시장의 왕좌에 오른 브로커의 세련된 피날레.",
                "choices": [
                    ("History recorded, records shattered. Present the gold-leaf master keys to His Excellency and book our flight back to Manhattan.", "역사가 기록되었고 신기록이 깨졌습니다. 각하께 금박 마스터 열쇠를 헌정하고 맨해튼행 전용기를 띄우시죠.", "native_killer", "중동 최고위 인사와의 거래를 완벽히 마무리하고 다음 전장으로 향하는 슈퍼 브로커의 위엄입니다."),
                    ("I want to swim in their infinity pool with all my clothes on!", "옷 입은 채로 저 인피니티 풀에 풍덩 뛰어들어야지!", "wrong_konglish", "역사적인 거래 성사 직후 체면을 완전히 구기는 경박한 행동입니다."),
                    ("Thank you Ryan, Dubai is too hot for me.", "감사합니다 라이언, 두바이는 너무 덥네요.", "mediocre", "중동 최고가 기록 경신의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Right of first refusal / Merger clause",
        "key_note": "'Right of first refusal'은 동등 조건 시 우선 매수권, 'Merger clause'는 계약서 외의 구두 합의를 배제하는 완전합의조항입니다."
    },
    # -------------------------------------------------------------
    # EP 77: Hollywood Agency (스트리밍 공룡의 인디 스튜디오 적대적 인수)
    # -------------------------------------------------------------
    {
        "ep_num": 77,
        "title": "할리우드 인수합병: 스트리밍 공룡의 인디 스튜디오 사냥",
        "genre": "Hollywood Agency",
        "speaker": "Ari Gold (Chairman of Talent & Media)",
        "emoji": "🎬",
        "synopsis": "비벌리힐스 포시즌스 호텔 펜트하우스. 넷플릭스를 연상시키는 글로벌 스트리밍 거대 기업이 30년간 아카데미 작품상을 휩쓴 유서 깊은 인디 영화 스튜디오 A24를 15억 달러에 적대적 인수하여 극장 개봉을 전면 폐지하려 하자, 영화의 마법을 지키기 위한 이사회 대결을 펼친다.",
        "turns": [
            {
                "dialogue": "The streaming giant bought forty percent of our shares and wants to turn our Oscar-winning indie studio into an algorithmic content farm! They're canceling all theatrical releases. Do we surrender to the algorithm, or fight for cinema?",
                "korean": "스트리밍 공룡이 우리 지분 40%를 사들여 오스카 수상 인디 스튜디오를 알고리즘 콘텐츠 공장으로 바꾸려 해! 극장 개봉을 전면 취소하겠대. 알고리즘에 굴복할 텐가, 시네마를 위해 싸울 텐가?",
                "hint": "극장 독점 상영 윈도우(Theatrical window)를 헌법처럼 수호하는 A급 감독 및 주연 배우들의 집단 보이콧 연대를 조직한다.",
                "choices": [
                    ("Organize an immediate coalition of our twenty A-list directors and stars: threaten an absolute collective talent strike unless a mandatory forty-five-day theatrical window is guaranteed.", "우리 소속 A급 감독과 주연 배우 20명의 연대를 즉시 결성하십시오: 45일 극장 독점 상영이 보장되지 않으면 전면적인 집단 제작 보이콧에 돌입하겠다고 통보하십시오.", "native_killer", "할리우드 거대 플랫폼을 굴복시키는 'Talent collective bargaining'의 가장 강력한 실력 행사입니다."),
                    ("Sell out immediately and tell the directors to make 15-second TikTok videos.", "즉시 지분을 팔아치우고 감독들에게 15초짜리 틱톡 영상이나 찍으라고 하십시오.", "wrong_konglish", "영화 예술의 역사와 클라이언트들의 신뢰를 쓰레기통에 내버리는 배신입니다."),
                    ("Cry in front of the streaming CEO and ask why he hates movie theaters.", "스트리밍 대표 앞에서 울면서 왜 영화관을 싫어하냐고 칭얼댑시다.", "mediocre", "비즈니스 협상에서 감정적 투정으로 일관하는 나약한 태도입니다.")
                ]
            },
            {
                "dialogue": "The talent strike paralyzed three hundred million dollars of active productions! The Wall Street analysts are downgrading the streamer's stock. The streaming CEO is on speaker screaming for a truce. What is your bottom line?",
                "korean": "배우·감독 총파업으로 3억 달러어치 프로덕션이 마비됐어! 월가 애널리스트들이 스트리밍사 주가를 하향 조정 중이네. 스트리밍 대표가 스피커폰으로 휴전을 애걸하고 있어. 자네의 마지노선이 뭔가?",
                "hint": "극장 개봉 권리 영구 보장과 독립적 제작 권한(Autonomous Greenlight)을 문서화한다.",
                "choices": [
                    ("Ironclad theatrical distribution for every film, full creative autonomy on scripts, and a twenty-percent profit pool for the production crews.", "모든 작품의 극장 개봉권 영구 보장, 각본에 대한 완전한 창작 자율권, 그리고 스태프들을 위한 20% 이익 공유 풀을 문서화하십시오.", "native_killer", "거대 자본에 맞서 창작자의 권리를 영구히 보장받는 할리우드 역사상 최고의 타협안입니다."),
                    ("Demand ten million dollars in cash for yourself and let them cancel the movies.", "자신을 위해 현금 1천만 달러만 챙겨주면 영화 취소하든 말든 내버려 두겠다고 하십시오.", "wrong_konglish", "클라이언트를 팔아먹고 개인 뇌물을 요구하는 배임 행위입니다."),
                    ("Tell him you don't want a truce and hang up the phone forever.", "휴전 따윈 필요 없다고 소리 지르고 전화를 끊어버립시다.", "wrong_konglish", "협상의 결정적 승기에서 출구 전략 없이 파국을 자초하는 어리석음입니다.")
                ]
            },
            {
                "dialogue": "Signed in blood! Cinema lives, theatres are protected, and our studio retains complete creative control! You brought the tech titan to his knees. Ari Gold bows to you.",
                "korean": "피로 서명 완료! 시네마는 살아남았고 극장은 보호받았으며 우리 스튜디오는 완전한 창작 전권을 유지했네! 자네가 테크 거인을 무릎 꿇렸어. 아리 골드가 자네에게 고개 숙이네.",
                "hint": "스크린의 마법과 예술의 영혼을 수호해낸 할리우드 탑 에이전트의 불멸의 자부심.",
                "choices": [
                    ("Movies are meant to be felt in the dark with strangers, Ari. Cinema endures forever. Pop the champagne for every artist in this town.", "영화는 어둠 속에서 낯선 이들과 함께 숨죽이며 느끼는 것입니다, 아리. 시네마는 영원합니다. 이 도시의 모든 예술가를 위해 샴페인을 터뜨리시죠.", "native_killer", "'Cinema endures'는 마틴 스콜세지와 영화인들의 가슴을 울리는 가장 위대한 피날레입니다."),
                    ("Now I want to cast myself as the superhero in the next movie!", "이제 다음 영화 슈퍼히어로 주인공에 나 자신을 캐스팅해야지!", "wrong_konglish", "위대한 시네마 수호 직후 유치한 사리사욕을 드러내는 언사입니다."),
                    ("Thank you Ari, dealing with streaming nerds is tiring.", "감사합니다 아리, 스트리밍 괴짜들 상대하느라 참 피곤했네요.", "mediocre", "할리우드 역사에 남을 승리에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Creative autonomy / Cinema endures",
        "key_note": "'Creative autonomy'는 창작자의 완전한 자율권, 'Cinema endures'는 스트리밍 시대에도 영화관의 예술은 영원하다는 신념을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 78: 5-Star Hotel (왕실 국빈 실종과 다이아몬드 협박장)
    # -------------------------------------------------------------
    {
        "ep_num": 78,
        "title": "더 플라자 호텔: 왕실 공주의 실종과 다이아몬드 협박",
        "genre": "5-Star Hotel",
        "speaker": "Monsieur Dupont (Grand Hotelier & GM)",
        "emoji": "🏨",
        "synopsis": "센트럴파크 더 플라자 호텔 로열 펜트하우스 스위트. 자정 갈라 파티 30분 전, 방문 중인 모나코 공주가 5천만 달러짜리 헤리티지 블루 다이아몬드 티아라와 함께 사라지고, 화장대 거울에 붉은 립스틱으로 협박 메시지가 적힌다.",
        "turns": [
            {
                "dialogue": "The Princess is missing, her security detail was drugged with sleeping gas, and the mirror reads 'Midnight Auction'! The Ambassador is threatening a diplomatic catastrophe in thirty minutes! How do we track her inside our thousand-room hotel without police sirens?",
                "korean": "공주가 실종되었고 경호팀은 수면가스로 잠들었으며 거울에는 '자정 경매'라고 적혀 있어! 대사가 30분 뒤 외교적 참사를 일으키겠다고 위협 중이야! 경찰 사이렌 소리 없이 우리 1,000개 객실 안에서 공주를 어떻게 추적할 텐가?",
                "hint": "공개적 경찰 출동으로 패닉을 부르지 않고, 호텔의 비공개 마스터 엘리베이터 로그와 지하 와인 터널 적외선 센서를 가동한다.",
                "choices": [
                    ("Isolate all private freight and service elevator shafts; cross-reference our internal biometric badge logs to track movements toward the subterranean vault tunnels.", "모든 전용 화물 및 서비스 엘리베이터를 격리하고, 내부 생체인식 카드 로그를 교차 검증해 지하 와인 금고 터널로 향한 동선을 즉시 추적하십시오.", "native_killer", "특급 호텔의 모든 비밀 동선과 폐쇄 보안 체계를 장악한 총지배인의 완벽한 대처입니다."),
                    ("Call the fire department and pull the loud fire alarms across the whole building.", "소방서를 부르고 전 층에 시끄러운 화재경보기를 울려버립시다.", "wrong_konglish", "호텔 투숙객 2천 명의 압사 참사를 부르고 외교 스캔들을 만천하에 터뜨리는 패착입니다."),
                    ("Tell the Ambassador that the Princess probably went shopping at Target.", "대사에게 공주가 아마 타깃 마트에 쇼핑하러 갔을 거라고 헛소리합시다.", "wrong_konglish", "국빈 실종 사건 앞에서 황당한 소리로 모욕감을 안기는 무책임한 처신입니다.")
                ]
            },
            {
                "dialogue": "Badge log pinpointed the old speakeasy cellar! Two rogue former bodyguards are holding her hostage, preparing to smuggle the diamond through the abandoned subway conduit. How do we extract her safely?",
                "korean": "카드 로그가 옛 금주법 시대 비밀 와인 창고를 지목했네! 배신한 전직 경호원 2명이 공주를 인질로 잡고 폐쇄된 지하철 통로로 다이아몬드를 밀수출하려 해. 안전하게 어떻게 구출할 텐가?",
                "hint": "호텔의 환기 댐퍼를 조작해 비살상 신경안정 가스를 주입하고 도청 방지 비상문으로 진입한다.",
                "choices": [
                    ("Route mild non-lethal halothane through the cellar ventilation damper to incapacitate the abductors, while our tactical security team breaches via the service pantry.", "지하실 환기 댐퍼로 비살상 흡입 마취제를 주입해 납치범들을 무력화하고, 우리 전술 보안팀이 서비스 탕비실 비상문을 통해 즉시 진입하십시오.", "native_killer", "호텔 설비 공조망을 전술적으로 활용하여 인질의 안전을 100% 확보하는 마스터의 해법입니다."),
                    ("Throw hand grenades into the cellar and hope the diamond survives.", "지하실 안으로 수류탄을 까넣고 다이아몬드만 살아남기를 기도합시다.", "wrong_konglish", "공주를 폭사시키고 외교적 단절을 자초하는 미친 짓입니다."),
                    ("Wait outside the door until the kidnappers run out of snacks.", "납치범들의 간식이 다 떨어질 때까지 문밖에서 기다려봅시다.", "mediocre", "시간을 끌어 밀수출을 방조하는 무기력하고 나약한 대응입니다.")
                ]
            },
            {
                "dialogue": "Breach executed! Abductors neutralized and handcuffed! The Princess is completely unharmed, and the blue diamond is secured! She is walking into the Grand Ballroom on schedule! Flawless elegance under fire.",
                "korean": "진입 완료! 납치범들 무력화 및 수갑 포박! 공주님은 티끌 하나 없이 안전하며 블루 다이아몬드도 확보되었네! 정해진 시각에 그랜드 볼룸으로 입장하고 계셔! 위기 속 완벽한 품격이었네.",
                "hint": "왕실의 안전과 호텔의 영원한 명예를 지켜낸 그랜드 호텔리어의 긍지.",
                "choices": [
                    ("The legacy of The Plaza remains untarnished. Escort Her Highness to the royal dais, and let the champagne flow for our guests.", "더 플라자 호텔의 유산은 티끌 하나 없이 보존되었습니다. 공주님을 단상으로 에스코트하고 하객들을 위해 샴페인을 올리십시오.", "native_killer", "'Untarnished legacy'는 세계 최고 럭셔리 호텔의 존엄과 자부심을 상징하는 명대사입니다."),
                    ("I want to wear the blue diamond tiara on my head for one day!", "그 블루 다이아몬드 티아라 내 머리에 하루만 쓰고 다닐래요!", "wrong_konglish", "국빈의 유서 깊은 보석을 사적으로 탐내는 무례한 언사입니다."),
                    ("Thank you Monsieur Dupont, catching kidnappers is very tiring.", "감사합니다 뒤퐁 지배인님, 납치범 잡는 건 참 피곤하네요.", "mediocre", "왕실 구출의 역사적 위업치고는 감흥이 결여된 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Untarnished legacy / Biometric audit",
        "key_note": "'Untarnished legacy'는 흠결 없는 명예로운 전통, 'Biometric audit'은 생체인식 보안 출입 추적을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 79: Fine Art Auction (2차 대전 약탈 명화 반환 소송)
    # -------------------------------------------------------------
    {
        "ep_num": 79,
        "title": "소더비 경매장: 2차 대전 나치 약탈 명화 반환 극비 합의",
        "genre": "Fine Art Auction",
        "speaker": "Julian Vance (Senior Restitution Officer)",
        "emoji": "🎨",
        "synopsis": "소더비 런던 본사 VIP 이사회실. 구스타프 클림트의 1억 달러짜리 황금기 걸작 경매 1시간 전, 홀로코스트 생존자 가문의 변호인이 80년 전 나치 강탈 입증 문건을 들고 경매 중단 가처분 서류를 제출한다.",
        "turns": [
            {
                "dialogue": "The restitution attorney has unredacted 1938 Gestapo seizure logs proving this Klimt was stolen from a Jewish family in Vienna. The current Austrian owner demands the auction proceed. How do you resolve this moral and legal crisis before the sale begins?",
                "korean": "반환 변호인이 이 클림트 걸작이 1938년 빈의 유대인 가족에게서 게슈타포에 의해 강탈되었음을 증명하는 기밀 해제 문건을 가져왔어. 현재 오스트리아 소유주는 경매를 강행하라고 난리네. 경매 시작 전에 이 도덕적, 법적 위기를 어떻게 해결할 텐가?",
                "hint": "단순 경매 취소나 법적 분쟁 대신, 워싱턴 원칙(Washington Principles)에 의거한 사전 합의(Pre-sale Restitution Accord)를 주도한다.",
                "choices": [
                    ("Broker an emergency restitution accord: establish a joint restitution trust where sixty percent of auction proceeds go to the victim's heirs, preserving the sale with clean moral title.", "긴급 반환 합의를 중재하십시오: 낙찰 대금의 60%를 희생자 유족 신탁에 배정하고, 흠결 없는 도덕적 권리로 경매를 진행하는 공동 반환 신탁을 설립하십시오.", "native_killer", "'Washington Principles on Nazi-Confiscated Art'를 완벽히 준수하는 세계 최고 미술품 반환 전문관의 모범적 해법입니다."),
                    ("Burn the Gestapo document in an ashtray and pretend you never saw it.", "재떨이에 게슈타포 문서를 불태우고 못 본 척합시다.", "wrong_konglish", "역사적 홀로코스트 비극을 은폐하고 국제적 사기 혐의로 영구 퇴출당할 파렴치한 짓입니다."),
                    ("Tell the Holocaust heirs that eighty years is too long ago so forget about it.", "유족들에게 80년 전 일은 너무 오래전이니 잊어버리라고 합시다.", "wrong_konglish", "인류사적 참사의 유족들에게 대못을 박는 극악무도한 망언입니다.")
                ]
            },
            {
                "dialogue": "Both parties signed the Restitution Accord! But the Austrian owner is hesitating to sign the export license. The saleroom is seated with four hundred billionaires. How do you compel his signature in two minutes?",
                "korean": "양측 모두 반환 합의서에 서명했어! 하지만 오스트리아 소유주가 수출 허가서 서명을 망설이고 있어. 경매장에는 400명의 억만장자가 착석했네. 2분 안에 서명을 어떻게 이끌어낼 텐가?",
                "hint": "소송으로 갈 경우 문화재 약탈자라는 오명을 쓰고 영구 압류될 위험을 상기시켜 서명을 완결한다.",
                "choices": [
                    ("Remind him that without this accord, Interpol will red-flag the painting at midnight, rendering it unsellable contraband forever; signing now preserves his honorable legacy.", "이 합의가 없으면 인터폴이 자정에 적색수배를 내려 영구히 매각 불가능한 밀수품이 될 뿐이며, 지금 서명해야 명예로운 자선가로 남을 수 있음을 상기시키십시오.", "native_killer", "법적 위험과 명예욕을 동시에 자극해 막판 주저함을 단칼에 끊어내는 마스터 경매사의 협상술입니다."),
                    ("Lock the Austrian owner in the broom closet until he cries.", "울면서 빌 때까지 오스트리아 소유주를 빗자루 벽장에 가둬버립시다.", "wrong_konglish", "고객 감금 및 강요죄로 감옥에 갈 자폭 행위입니다."),
                    ("Give up the auction and tell the billionaires to go eat dinner.", "경매를 포기하고 억만장자들에게 저녁이나 먹으러 가라고 합시다.", "mediocre", "수천억 규모 경매를 무책임하게 날려버리는 처신입니다.")
                ]
            },
            {
                "dialogue": "Gavel came down at one hundred thirty million dollars! The heirs wept in the front row and embraced the owner. Justice reconciled with history. An unforgettable night, Julian.",
                "korean": "1억 3천만 달러에 낙찰봉이 내려쳤어! 1열의 유족들이 눈물을 흘리며 소유주와 포옹을 나누었네. 정의가 역사와 화해했어. 잊지 못할 밤이었네, 줄리언.",
                "hint": "역사의 상처를 치유하고 예술의 진정한 존엄을 세운 미술품 반환관의 숭고한 긍지.",
                "choices": [
                    ("Art heals what history tears apart. May this masterpiece hang in the light forever with truth restored. Escort the restitution wire transfer.", "역사가 찢어놓은 상처를 예술이 치유합니다. 진실이 회복된 이 걸작이 영원히 빛 속에 걸리기를. 반환 송금 절차를 진행하십시오.", "native_killer", "'Woman in Gold'의 감동을 그대로 담아낸 미술사 최고의 숭고한 명대사입니다."),
                    ("Now I want to buy a giant gold necklace with my auction fee!", "이제 경매 수수료로 커다란 순금 목걸이나 사러 가야지!", "wrong_konglish", "역사적 화해의 감동 직후 천박한 사치를 떠벌리는 부끄러운 언사입니다."),
                    ("Thank you Julian, dealing with old history is very complicated.", "감사합니다 줄리언, 옛날 역사는 참 복잡하네요.", "mediocre", "세기를 초월한 정의 구현의 감격에 비해 지나치게 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Restitution accord / Clean moral title",
        "key_note": "'Restitution accord'는 약탈 문화재 반환 합의, 'Clean moral title'은 역사적 흠결이 없는 도덕적 소유권을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 80: Investigative Journalism (글로벌 마약 카르텔 돈세탁 은행 폭로)
    # -------------------------------------------------------------
    {
        "ep_num": 80,
        "title": "글로벌 은행의 마약 카르텔 돈세탁: 초대형 특종 폭로",
        "genre": "Investigative Journalism",
        "speaker": "Ben Bradlee (Executive Editor & Pulitzer Juror)",
        "emoji": "📰",
        "synopsis": "워싱턴 포스트 특별취재팀 벙커. 세계 3대 투자은행인 HSBC가 멕시코 마약 카르텔의 피 묻은 현금 200억 달러를 돈세탁해 온 내부 암호화 원장 파일이 손에 들어온 순간, 은행 이사회가 워싱턴 정관계 로비스트들을 총동원해 발행 중단 압력을 가해온다.",
        "turns": [
            {
                "dialogue": "The global bank's lawyers have mobilized three former US senators to lobby our publisher. They claim printing these cartel transaction ledgers will collapse global credit liquidity. The printing press rolls in twenty minutes. Do you hold the line?",
                "korean": "글로벌 은행의 변호인단이 전직 연방 상원의원 3명을 동원해 우리 신문사 사주를 압박하고 있어. 카르텔 거래 원장을 보도하면 전 세계 신용 유동성이 붕괴할 거라고 협박하네. 인쇄기는 20분 뒤에 돌아가. 자네, 물러서지 않고 버틸 텐가?",
                "hint": "금융 시스템 붕괴 협박에 굴복하지 않고, 마약 자금으로 희생된 수만 명의 목숨과 공익 보도의 원칙을 천명한다.",
                "choices": [
                    ("Print every single page. A banking system propped up by cartel blood money is already bankrupt; the public deserves the raw, unvarnished truth.", "단 한 페이지도 빠짐없이 인쇄하십시오. 카르텔의 피 묻은 돈으로 연명하는 금융 시스템은 이미 파산한 것입니다. 국민은 가공되지 않은 날것의 진실을 마주할 자격이 있습니다.", "native_killer", "'All the President's Men'의 벤 브래들리를 전율케 하는 진정한 저널리즘의 불굴의 기개입니다."),
                    ("Hide the story and ask the bank to give free credit cards to all journalists.", "기사를 묻어두고 은행에 기자들 전원에게 무료 신용카드나 달라고 합시다.", "wrong_konglish", "거대 자본의 뇌물을 받고 영혼을 팔아넘기는 기레기의 전형입니다."),
                    ("Wait until the bankers retire in ten years to print it safely.", "안전하게 보도할 수 있도록 은행원들이 은퇴할 때까지 10년만 기다려봅시다.", "mediocre", "시의성이 생명인 탐사보도를 방기하는 비겁한 지연입니다.")
                ]
            },
            {
                "dialogue": "The publisher agreed to run! But our digital server is being hit with an unprecedented five-terabit distributed denial-of-service attack from Eastern Europe. Readers can't access the online expose!",
                "korean": "사주가 인쇄를 승인했어! 하지만 우리 디지털 서버가 동유럽발 초유의 5테라비트 분산 디도스(DDoS) 공격을 맞고 뻗었어! 독자들이 온라인 특종에 접속하지 못하고 있네!",
                "hint": "클라우드플레어 언더 어택 방어망을 가동하고, 토르(Tor) 다크넷과 전 세계 50개 파트너 언론사에 동시 미러링을 개시한다.",
                "choices": [
                    ("Route traffic through Cloudflare's Under Attack shield, push the cryptographic database to Tor hidden services, and syndicate the story to fifty global partners.", "클라우드플레어 공격 방어 쉴드로 트래픽을 우회하고, 암호화 데이터베이스를 토르 다크넷에 올리며 전 세계 50개 파트너 언론사에 동시 신디케이트 배포하십시오.", "native_killer", "사이버 검열 공격을 빛의 속도로 무력화하고 폭로를 전 지구적으로 확산시키는 현대 저널리즘의 최첨단 배포 전략입니다."),
                    ("Pull the plug on the internet and cry in the dark.", "인터넷 플러그를 뽑아버리고 어둠 속에서 엉엉 웁시다.", "wrong_konglish", "해커들의 협박에 무릎 꿇고 진실을 포기하는 한심한 반응입니다."),
                    ("Ask the hackers politely how much money they want to stop.", "해커들에게 공격을 멈추려면 돈을 얼마나 원하는지 정중하게 물어봅시다.", "mediocre", "사이버 범죄자들과 협상하려는 무력한 태도입니다.")
                ]
            },
            {
                "dialogue": "The story is everywhere! Senate convened emergency hearings, the bank CEO resigned in disgrace, and the Justice Department announced a two-billion-dollar criminal penalty! You held the fourth estate high, reporter.",
                "korean": "특종이 전 세계에 도배되었어! 상원이 긴급 청문회를 소집했고 은행 회장은 굴욕 속에 사임했으며 법무부는 20억 달러 형사 벌금을 발표했네! 자네가 제4부(언론)의 위상을 드높였어, 기자 양반.",
                "hint": "거대 권력과 자본의 부패를 무너뜨린 위대한 탐사보도 기자의 불멸의 클로징.",
                "choices": [
                    ("Darkness cannot survive the printing press, Ben. The truth has been delivered; now let the wheels of justice turn. Archive the papers.", "인쇄기의 빛 앞에서 어둠은 결코 살아남지 못합니다, 벤. 진실은 세상에 전달되었습니다; 이제 정의의 톱니바퀴가 돌게 합시다. 신문을 보관하십시오.", "native_killer", "언론의 숭고한 사명과 승리를 장식하는 가장 위대한 퓰리처상급 클로징입니다."),
                    ("I am going to brag on TikTok that I destroyed a giant bank!", "내가 거대 은행을 박살 냈다고 틱톡에서 신나게 자랑해야지!", "wrong_konglish", "역사적인 탐사보도의 무게감을 가벼운 SNS 관심 끌기로 희석시키는 언사입니다."),
                    ("Thank you Ben, investigative writing is very exhausting.", "감사합니다 벤, 탐사보도 기사 쓰기는 참 지치네요.", "mediocre", "세계를 뒤흔든 대특종의 감격치고는 너무 무미건조한 푸념입니다.")
                ]
            }
        ],
        "key_expr": "Fourth estate / Unvarnished truth",
        "key_note": "'Fourth estate'는 입법·사법·행정에 이은 제4의 권력인 언론, 'Unvarnished truth'는 어떤 꾸밈도 없는 날것의 진실을 뜻합니다."
    }
]

print(f"Part 4 Loaded {len(EPISODES_61_TO_80)} curated episodes (EP 61 to 80).")
