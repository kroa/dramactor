# -*- coding: utf-8 -*-
"""
Dramactor Curated Master Database - Part 2 (Episodes 21 to 40)
High-stakes narrative arcs across 20 American drama genres.
"""

EPISODES_21_TO_40 = [
    # -------------------------------------------------------------
    # EP 21: Legal (대배심 기소 위기)
    # -------------------------------------------------------------
    {
        "ep_num": 21,
        "title": "대배심 기소 위기: 검찰의 비밀 녹취록 공개",
        "genre": "Legal",
        "speaker": "Jessica Pearson (Managing Partner)",
        "emoji": "⚖️",
        "synopsis": "뉴욕 남부지검 대배심 출석 30분 전 피어슨 하드먼 대회의실. 연방 검사가 의뢰인의 은밀한 통화 도청 녹취록을 들이밀며 즉각 기소를 예고한다. 로펌의 명운을 걸고 증거 배제 전략을 찾아야 한다.",
        "turns": [
            {
                "dialogue": "The US Attorney just leaked a wiretap recording of our client discussing offshore accounts. The Grand Jury votes at two. What is our motion to suppress?",
                "korean": "연방 검사가 우리 의뢰인이 해외 계좌를 논의한 도청 녹취록을 방금 유출했어. 대배심 투표는 2시야. 증거 배제 신청 논리가 뭐야?",
                "hint": "불법 도청 또는 절차적 하자를 지적하여 대배심 투표 전 녹취록을 무력화해야 한다.",
                "choices": [
                    ("File an emergency motion alleging Title Three wiretap violations and demand an immediate evidentiary hearing.", "통신감청법 제3조 위반을 이유로 긴급 증거 배제 신청을 내고 즉각적인 증거 청문회를 요구하십시오.", "native_killer", "'Title Three wiretap violations'와 'evidentiary hearing'은 미 연방법정의 정통 증거 무력화 필살기입니다."),
                    ("Tell the press that the prosecutor is a very bad person.", "기자들에게 검사가 아주 나쁜 사람이라고 말합시다.", "wrong_konglish", "법적 쟁점을 무시하고 감정적으로 여론에 호소하는 패착입니다."),
                    ("We should ask the client if he really said that.", "의뢰인에게 진짜 그렇게 말했는지 물어봅시다.", "mediocre", "마감 직전 증거 능력 다툼 대신 뒷북 확인에 머무는 미숙한 대응입니다.")
                ]
            },
            {
                "dialogue": "The judge will never grant an evidentiary hearing without prima facie proof of bad faith. Where is your smoking gun against the FBI?",
                "korean": "판사는 수사기관의 명백한 악의를 입증하는 일응의 증거 없이는 증거 청문회를 절대 열어주지 않을 거야. FBI에 맞설 결정적 증거가 어디 있지?",
                "hint": "수사기관의 영장 집행 하자나 악의를 입증할 구체적 정황을 제시한다.",
                "choices": [
                    ("The warrant timestamp predates the magistrate's signature by forty minutes. They monitored privileged spousal calls illegally.", "영장 집행 시각이 판사의 서명보다 40분 앞서 있습니다. 부부간 특권 대화까지 불법 감청했습니다.", "native_killer", "'Warrant timestamp'와 'privileged spousal calls'는 법정 스릴러의 판도를 뒤집는 완벽한 스모킹 건입니다."),
                    ("I think FBI agents are usually careless.", "FBI 요원들이 보통 부주의하다고 생각합니다.", "wrong_konglish", "법정에서 통하지 않는 개인적 억측에 불과합니다."),
                    ("We can pray that the judge is in a good mood.", "판사의 기분이 좋기를 기도해봅시다.", "mediocre", "증거와 법리로 싸우지 않는 비전문적인 자세입니다.")
                ]
            },
            {
                "dialogue": "Judge tossed the wiretap! The prosecutor is packing his files in disgrace. You just saved this firm from national ruin.",
                "korean": "판사가 녹취록을 각하했어! 검사가 굴욕 속에 서류를 챙겨 나가고 있네. 자네가 방금 이 로펌을 전국적 파멸에서 구해냈어.",
                "hint": "극적인 승소 후 시니어 파트너의 찬사에 자신감 넘치게 화답한다.",
                "choices": [
                    ("Never doubt our defense, Jessica. When they fight dirty, we teach them the rules of engagement.", "우리 변호인단을 결코 의심하지 마십시오, 제시카. 저들이 더럽게 싸울 때, 우리가 교전 수칙을 가르쳐주는 법입니다.", "native_killer", "'Suits' 특유의 세련되고 압도적인 로펌 파트너 카리스마가 돋보이는 대사입니다."),
                    ("I was so lucky, I had goosebumps all over.", "너무 운이 좋았어요, 온몸에 닭살이 돋았습니다.", "wrong_konglish", "치밀한 법률적 승리를 단순한 운으로 폄하하는 발언입니다."),
                    ("Thank you Jessica, I need to sleep now.", "감사합니다 제시카, 이제 잠을 좀 자야겠어요.", "mediocre", "승리의 여운을 이어가지 못하는 밋밋한 반응입니다.")
                ]
            }
        ],
        "key_expr": "Motion to suppress / Rules of engagement",
        "key_note": "'Motion to suppress'는 증거 배제 신청, 'Rules of engagement'는 교전 수칙 및 행동 원칙을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 22: Startup (시리즈 B 투자 유치)
    # -------------------------------------------------------------
    {
        "ep_num": 22,
        "title": "시리즈 B 투자 유치: 악덕 VC의 50% 지분 희석 함정",
        "genre": "Startup",
        "speaker": "Don Valentine (Predatory Lead VC)",
        "emoji": "🚀",
        "synopsis": "샌프란시스코 샌드힐 로드 VC 본사. 유니콘 진입을 앞둔 AI 스타트업 창업자에게 5천만 달러 투자 조건으로 2배 참여형 우선주와 50% 지분 희석 독소 조항을 내민다.",
        "turns": [
            {
                "dialogue": "Fifty million dollars on the table, but with a 2x participating liquidation preference and three board seats. Take it or watch your runway burn out in forty-five days.",
                "korean": "5천만 달러가 테이블에 있네. 단, 2배 참여형 청산우선권과 이사회 의석 3석 조건이야. 받든지, 아니면 45일 뒤 런웨이가 타버리는 걸 지켜보든가.",
                "hint": "스타트업의 경영권을 뺏으려는 독소 조항(Liquidation preference)을 단호히 거부하고 반격한다.",
                "choices": [
                    ("A 2x participating preference is predatory. We counter with a 1x non-participating preference, capped at one board seat, or we walk.", "2배 참여형 청산우선권은 약탈적입니다. 1배 비참여형 우선권과 이사회 1석으로 역제안하며, 거절 시 테이블을 떠나겠습니다.", "native_killer", "'2x participating preference'의 독소성을 짚고 '1x non-participating'으로 카운터를 날리는 정통 실리콘밸리 협상술입니다."),
                    ("Fifty million is a big money, so I will sign anything you want.", "5천만 달러는 큰돈이니 원하시는 대로 다 사인하겠습니다.", "wrong_konglish", "창업자 지분과 회사 경영권을 고스란히 헌납하는 자살골입니다."),
                    ("Can you give us forty million with fewer bad words?", "나쁜 조건 빼고 4천만 달러만 주실 수 있나요?", "mediocre", "투자 계약의 핵심 법적 개념을 짚지 못한 모호한 절충안입니다.")
                ]
            },
            {
                "dialogue": "You think Sequoia or Andreessen will touch you after I blackball you across the valley? You're playing with fire, kid.",
                "korean": "내가 밸리 전역에 자네 블랙리스트를 돌린 후에도 세콰이어나 안드레센이 거들떠볼 것 같나? 자넨 불장난을 치고 있어, 꼬마야.",
                "hint": "VC의 블랙리스트 협박에 흔들리지 않고 폭발적인 매출 지표와 경쟁 텀시트로 맞받아친다.",
                "choices": [
                    ("Our annual recurring revenue tripled this quarter with zero customer churn. Andreessen's term sheet arrived an hour ago, fully priced.", "우리 연간 반복 매출은 고객 이탈 0%로 이번 분기 3배 성장했습니다. 안드레센의 텀시트가 1시간 전에 도착했습니다.", "native_killer", "숫자와 강력한 대안(BATNA)으로 상대의 오만을 짓밟는 완벽한 창업자의 압도적 승부수입니다."),
                    ("Please don't tell bad rumors about me to other VCs.", "제발 다른 VC들에게 저에 대해 나쁜 소문 내지 말아주세요.", "wrong_konglish", "약점을 보이고 굴복하여 투자자에게 완전히 먹잇감이 되는 발언입니다."),
                    ("We have a lot of good software code in GitHub.", "저희 깃허브에 좋은 소프트웨어 코드가 아주 많습니다.", "mediocre", "재무적 지표 경쟁에서 기술적 자랑으로 빗나가는 아마추어적 답변입니다.")
                ]
            },
            {
                "dialogue": "Alright, you win. 1x non-participating, clean common equity valuation, seventy million pre-money. Let's build a decacorn together.",
                "korean": "좋아, 자네가 이겼어. 1배 비참여형, 깔끔한 보통주 평가, 프리 밸류 7천만 달러. 함께 데카콘 기업을 만들어보세.",
                "hint": "항복을 받아내고 유리한 조건으로 텀시트를 확정 짓는 당당한 마무리.",
                "choices": [
                    ("Wire the funds to Silicon Valley Bank. We execute on our product roadmap starting Monday.", "실리콘밸리 은행으로 펀드를 송금하십시오. 월요일부터 우리 제품 로드맵 실행에 돌입합니다.", "native_killer", "'Execute on our roadmap'은 탑티어 스타트업 리더의 흔들림 없는 실행력을 상징합니다."),
                    ("Yippee! I am rich now! Let's buy fancy cars!", "만세! 나 이제 부자다! 멋진 차 사러 가자!", "wrong_konglish", "투자금의 성격을 망각하고 사적 유흥을 떠벌리는 경망스러운 태도입니다."),
                    ("Thank you Don, that was very scary.", "감사합니다 돈, 정말 무서웠어요.", "mediocre", "긴장감 넘쳤던 승리의 권위를 깎아내리는 유약한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Liquidation preference / Decacorn",
        "key_note": "'Liquidation preference'는 회사 매각 시 투자금 우선 변제권, 'Decacorn'은 기업가치 100억 달러 이상의 스타트업을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 23: Corporate (적대적 M&A 방어)
    # -------------------------------------------------------------
    {
        "ep_num": 23,
        "title": "적대적 M&A 방어: 독약 조항(Poison Pill) 가동",
        "genre": "Corporate",
        "speaker": "Logan Roy (Patriarch & Media Tycoon)",
        "emoji": "🏢",
        "synopsis": "웨이스타 로이코 본사 최상층 이사회실. 행동주의 헤지펀드가 40% 지분 확보를 통한 적대적 인수를 공식 선언하자, 가문의 제국을 지키기 위한 독약 조항(Poison Pill) 가동을 논의한다.",
        "turns": [
            {
                "dialogue": "The hedge fund snakes bought up twelve percent overnight through dark pools. They're staging a proxy fight to decapitate me. Do we trigger the shareholder rights plan?",
                "korean": "그 헤지펀드 뱀 같은 놈들이 다크풀을 통해 하룻밤 사이에 12%를 사들였어. 날 참수하려고 위임장 대결을 벌이려는 거야. 주주 권리 계획(포이즌 필)을 가동할 텐가?",
                "hint": "적대적 매수자의 지분을 희석시키기 위해 이사회의 포이즌 필 결의를 주도한다.",
                "choices": [
                    ("Trigger the flip-in poison pill immediately. Flood existing shareholders with discounted shares to dilute their stake down to six percent.", "즉시 플립인 포이즌 필을 가동하십시오. 기존 주주들에게 할인된 신주를 대량 배정하여 저들의 지분을 6%로 희석시켜야 합니다.", "native_killer", "'Flip-in poison pill'과 'dilute their stake'는 적대적 M&A를 방어하는 가장 공격적이고 치명적인 기업 법무 전술입니다."),
                    ("Sell the whole company and go on vacation to Europe.", "회사 전체를 팔아버리고 유럽으로 휴가나 떠납시다.", "wrong_konglish", "'Succession'의 로건 로이 앞에서 이런 말을 하면 즉각 해고당합니다."),
                    ("Ask the hedge fund nicely to return our shares.", "헤지펀드에 주식을 다시 돌려달라고 좋게 부탁해봅시다.", "mediocre", "월스트리트의 약육강식 생리를 전혀 이해하지 못한 순진한 발언입니다.")
                ]
            },
            {
                "dialogue": "The SEC will crawl all over our board minutes. If we dilute, Wall Street might dump our stock by twenty points. Are you willing to stomach the bleeding?",
                "korean": "SEC가 우리 이사회 회의록을 샅샅이 뒤질 거야. 지분을 희석하면 월가가 우리 주식을 20포인트나 내던질 수도 있어. 자네 그 출혈을 견뎌낼 각오가 돼 있나?",
                "hint": "단기적 주가 폭락의 고통을 감수하고 경영권 사수를 위한 확고한 결기를 증명한다.",
                "choices": [
                    ("Short-term volatility is the price of sovereignty. We hold the fortress; the market will re-price our strength once the raiders retreat.", "단기 변동성은 기업 주권을 지키기 위한 대가입니다. 요새를 사수하십시오. 약탈자들이 물러나면 시장은 우리 강인함을 재평가할 것입니다.", "native_killer", "'Succession' 속 거물들이 구사하는 제국 수호의 숭고하고 단호한 언어입니다."),
                    ("If the stock drops, my bonus will be zero, so I hate it.", "주가가 떨어지면 제 보너스가 날아가니 전 결사반대입니다.", "wrong_konglish", "개인의 사리사욕만 따지며 오너의 거대한 시야를 거스르는 최악의 답변입니다."),
                    ("Maybe we can give them just half of what they want.", "그들이 원하는 것의 절반만 주는 타협안은 어떨까요?", "mediocre", "적대적 세력에게 문을 열어주는 어정쩡하고 위험한 절충입니다.")
                ]
            },
            {
                "dialogue": "The raiders choked on the dilution! Their liquidity dried up and they just withdrew their tender offer. You're a killer. Welcome to the inner circle.",
                "korean": "약탈자들이 희석의 늪에 걸려 숨이 턱 막혔어! 유동성이 말라붙더니 방금 공개매수를 철회했네. 자넨 진짜 킬러야. 내 이너서클에 들어온 걸 환영하네.",
                "hint": "치열한 기업 전쟁에서 승리하고 오너의 전폭적인 신임을 얻는다.",
                "choices": [
                    ("The throne remains untouchable, Logan. Now let us turn around and acquire their prime media assets on clearance.", "왕좌는 불가침입니다, 로건. 이제 반격하여 저들의 핵심 미디어 자산을 헐값에 인수합시다.", "native_killer", "방어에 그치지 않고 역인수 공세로 나아가는 최고의 승부사다운 피날레입니다."),
                    ("Thank you Logan, can I have a bigger office now?", "감사합니다 로건, 이제 더 큰 사무실 주실 수 있나요?", "wrong_konglish", "위대한 승리 직후 사소한 특혜를 요구해 품격을 떨어뜨립니다."),
                    ("Good job to everyone, it was a long board meeting.", "모두 수고하셨습니다, 참 긴 이사회였네요.", "mediocre", "역사적인 M&A 전쟁의 승리치고는 지나치게 평범합니다.")
                ]
            }
        ],
        "key_expr": "Poison pill / Price of sovereignty",
        "key_note": "'Poison pill'은 적대적 M&A 시 기존 주주에게 신주인수권을 부여해 지분을 희석하는 방어 전략을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 24: Medical (초대형 태풍 속 응급실 코드 블랙)
    # -------------------------------------------------------------
    {
        "ep_num": 24,
        "title": "초대형 태풍 속 정전: 응급실 코드 블랙",
        "genre": "Medical",
        "speaker": "Dr. Miranda Bailey (Chief of Surgery)",
        "emoji": "🏥",
        "synopsis": "카테고리 5 태풍이 시애틀을 강타하며 병원 비상 발전기마저 침수된 자정. 40명의 중환자가 밀려드는 응급실에 전력 차단과 산소 공급 중단 경보가 울린다.",
        "turns": [
            {
                "dialogue": "Substation flooded! Backup generators just tripped, and ICU ventilators are on twelve-minute internal batteries. How do we keep forty intubated patients alive?",
                "korean": "변전소 침수! 비상 발전기가 방금 트립됐고, 중환자실 인공호흡기 배터리가 12분 남았어. 기도 삽관된 환자 40명을 어떻게 살려둘 건가?",
                "hint": "기계적 장비가 멈춘 극한 상황에서 즉시 수동 환기 및 트리아지(Triage) 체계를 가동한다.",
                "choices": [
                    ("Mobilize all residents with manual ambu bags immediately. Prioritize post-op cardiac cases and establish a bucket brigade for oxygen tanks.", "모든 레지던트를 즉각 수동 앰부백 환기에 투입하십시오. 심장 수술 환자를 최우선 배치하고 산소 탱크 운반조를 편성해야 합니다.", "native_killer", "'Manual ambu bags'와 'bucket brigade for oxygen'은 응급의학 재난 프로토콜의 표준입니다."),
                    ("Tell the patients to hold their breath until morning.", "환자들에게 아침까지 숨을 참으라고 전달합시다.", "wrong_konglish", "의학적으로 불가능하고 환자를 질식사시키는 황당한 발언입니다."),
                    ("Run outside and try to fix the high-voltage wire.", "밖으로 뛰어나가 고압 전선을 고쳐봅시다.", "mediocre", "의사의 본분을 망각하고 감전 위험에 뛰어드는 비이성적 행동입니다.")
                ]
            },
            {
                "dialogue": "Trauma Bay 1 has an open aortic aneurysm bleeding out in pitch darkness. Flashlights only. Do we operate without suction, or let him code?",
                "korean": "1번 외상 구역에 대동맥류 파열 환자가 칠흑 같은 어둠 속에서 과다출혈 중이야. 손전등뿐이야. 석션 없이 수술할 텐가, 아니면 심정지를 지켜볼 텐가?",
                "hint": "최악의 시야와 기구 부재 속에서 환자를 살리기 위한 과감한 외과적 결단을 내린다.",
                "choices": [
                    ("Cross-clamp the aorta by blind tactile palpation under surgical loupes. We don't lose a life on my watch.", "수술용 루페를 끼고 촉진으로 대동맥을 블라인드 클램핑하겠습니다. 제 당직 시간에 환자를 잃을 수 없습니다.", "native_killer", "'Grey's Anatomy'의 전설적인 외과의를 연상시키는 고난도 촉진 클램핑과 숭고한 사명감입니다."),
                    ("It is too dark, we should give up and wait for sunshine.", "너무 어두우니 포기하고 해 뜰 때까지 기다립시다.", "wrong_konglish", "환자의 사망을 방치하는 명백한 의료 과실 및 의무 유기입니다."),
                    ("Let's close the patient's belly and transfer him to another city.", "환자 복부를 닫고 다른 도시 병원으로 이송합시다.", "mediocre", "태풍 속에서 출혈 환자를 이송하는 것은 즉각 사망으로 이어집니다.")
                ]
            },
            {
                "dialogue": "The clamp held! Bleeding controlled, and auxiliary power just came back online. You held this trauma center together with your bare hands, doctor.",
                "korean": "클램프가 버텼어! 출혈 잡혔고 보조 전력이 방금 복구되었네. 자네가 맨손으로 이 외상센터를 지켜냈어, 의사 선생.",
                "hint": "절체절명의 위기를 극복하고 환자의 생명을 살려낸 동료들과 연대를 나눈다.",
                "choices": [
                    ("Vital signs stabilized. Check on pediatric ICU next; nobody dies tonight in this hospital.", "생체 징후 안정되었습니다. 다음 소아 중환자실을 확인하겠습니다. 오늘 밤 이 병원에서 아무도 죽지 않습니다.", "native_killer", "'Nobody dies tonight'은 의학 드라마 속 진정한 영웅 외과의의 불멸의 신념입니다."),
                    ("I want to sue the city power company for my overtime.", "야근 수당 때문에 시 전력회사를 고소하고 싶네요.", "wrong_konglish", "기적의 생환 직후 속 좁은 불평을 늘어놓는 부적절한 태도입니다."),
                    ("Thank you Dr. Bailey, surgery was very hard.", "감사합니다 베일리 박사님, 수술이 참 힘들었네요.", "mediocre", "격정적인 구명의 순간치고는 감흥이 부족합니다.")
                ]
            }
        ],
        "key_expr": "Cross-clamp / On my watch",
        "key_note": "'Cross-clamp'는 혈관을 집게로 차단해 출혈을 막는 응급 지혈술, 'On my watch'는 내 책임 하에를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 25: Dating (햄튼 자선 갈라)
    # -------------------------------------------------------------
    {
        "ep_num": 25,
        "title": "햄튼 자선 갈라: 상류층 전 약혼자와의 재회",
        "genre": "Dating",
        "speaker": "Blair Waldorf (Upper East Side Socialite)",
        "emoji": "🥂",
        "synopsis": "뉴욕 햄튼 해변의 초호화 자선 갈라 파티. 3년 전 파혼했던 맨해튼 부동산 재벌 후계자가 새 연인과 함께 나타나 당신의 자존심을 긁으며 샴페인 잔을 건넨다.",
        "turns": [
            {
                "dialogue": "Look who finally surfaced from the shadows. I hear you've been doing charity work in Brooklyn. Tell me, do you miss the private jets, or are you pretending to love being ordinary?",
                "korean": "그늘에서 드디어 모습을 드러낸 게 누군가 했네. 브루클린에서 자선 사업이나 하고 다닌다며? 솔직히 말해봐, 전용기가 그립지 않아, 아니면 평범한 척하는 삶이 마음에 드는 거야?",
                "hint": "상류층의 유치한 도발에 품위와 기품을 잃지 않고 우아하게 반격한다.",
                "choices": [
                    ("Luxury is easy to buy; true purpose requires substance. But I see your conversation is as vacuous as the day we parted.", "사치는 돈으로 살 수 있지만, 진정한 목적은 내면의 깊이를 요하죠. 하지만 당신의 대화는 우리가 헤어진 날만큼이나 여전히 공허하군요.", "native_killer", "'Gossip Girl'의 블레어 월도프도 감탄할 만한 우아하고도 치명적인 상류층 카운터펀치입니다."),
                    ("You are so mean! I hate your private jet anyway!", "너 너무 못됐어! 어차피 네 전용기 따위 하나도 안 부러워!", "wrong_konglish", "감정 조절에 실패하고 초라한 질투심을 드러내는 패착입니다."),
                    ("Brooklyn is a very nice place with many coffee shops.", "브루클린은 커피숍도 많고 아주 살기 좋은 동네입니다.", "mediocre", "상대의 날 선 풍자를 간파하지 못하고 엉뚱한 동네 자랑에 그칩니다.")
                ]
            },
            {
                "dialogue": "Always so sharp. The auctioneer is about to open bidding for the polo club endowment. Care to match my fifty-thousand-dollar pledge, or should I donate in your name?",
                "korean": "여전히 날카롭네. 경매사가 곧 폴로 클럽 기부금 경매를 시작할 거야. 내가 부를 5만 달러에 맞춰볼 텐가, 아니면 네 이름으로 대신 기부해줄까?",
                "hint": "돈으로 굴욕을 주려는 졸부의 얄팍한 호가에 지혜와 진짜 영향력으로 응수한다.",
                "choices": [
                    ("Keep your petty fifty thousand. I just endowed the entire youth scholarship fund anonymously at two million. Enjoy your polo pony.", "그 푼돈 5만 달러는 간직하세요. 난 방금 청소년 장학 기금 전액에 2백만 달러를 익명 기부했으니까요. 폴로 말이나 즐기시죠.", "native_killer", "스케일 자체가 다른 기부와 차분한 조롱으로 상대를 단숨에 압도하는 완벽한 반전입니다."),
                    ("I have zero dollars in my pocket right now.", "저 지금 주머니에 한 푼도 없는데요.", "wrong_konglish", "사교계 파티에서 스스로의 자존감을 바닥으로 내팽개치는 태도입니다."),
                    ("Fifty thousand is too expensive for a horse club.", "말 클럽에 5만 달러는 너무 비싼 금액 같네요.", "mediocre", "사교계의 기부 문화를 이해하지 못하는 서민적 반응입니다.")
                ]
            },
            {
                "dialogue": "Two million...?! The whole room is whispering about you. You really haven't lost your touch, have you? Join me for a drink on the veranda.",
                "korean": "2백만 달러라고...?! 연회장 전체가 네 이야기로 수군거리고 있어. 너 정말 기품을 잃지 않았구나? 베란다에서 한잔 더 할래?",
                "hint": "완벽하게 굴복한 전 연인에게 주도권을 쥔 채 쿨하게 등을 돌린다.",
                "choices": [
                    ("I prefer drinking with people who have more ambition than inheritance. Good evening.", "전 유산보다 야망이 큰 사람들과 잔을 기울이는 걸 선호해요. 좋은 저녁 보내시길.", "native_killer", "마지막 한마디까지 완벽한 도도함과 자존감을 보여주는 로맨스 드라마의 정점입니다."),
                    ("Okay, let's drink until we get drunk together!", "좋아요, 우리 같이 취할 때까지 마셔봐요!", "wrong_konglish", "방금 세운 위엄을 한순간에 날려버리는 주책스러운 태도입니다."),
                    ("Thank you, maybe another time when I am free.", "감사합니다, 다음에 한가할 때나 한번 보죠.", "mediocre", "여운이 약하고 평범한 거절입니다.")
                ]
            }
        ],
        "key_expr": "True purpose / Lost one's touch",
        "key_note": "'True purpose'는 삶의 진정한 의미, 'Lose one's touch'는 고유의 기량이나 감각을 잃다를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 26: Wall Street (SEC 금융감독원 압수수색)
    # -------------------------------------------------------------
    {
        "ep_num": 26,
        "title": "SEC 금융감독원 불시 압수수색: 트레이딩 룸 봉쇄",
        "genre": "Wall Street",
        "speaker": "Bobby Axelrod (Billionaire Hedge Fund Titan)",
        "emoji": "📈",
        "synopsis": "월스트리트 초호화 헤지펀드 액스 캐피탈. 오전 9시 30분 개장 직전, SEC(증권거래위원회)와 FBI 연방 요원들이 압수수색 영장을 들고 트레이딩 플로어를 덮친다.",
        "turns": [
            {
                "dialogue": "Federal marshals on the elevator! They have a search warrant for algorithmic trading logs. Every trader is freezing up. How do we keep this firm trading?",
                "korean": "연방 집행관들이 엘리베이터를 타고 올라오고 있어! 알고리즘 트레이딩 로그에 대한 압수수색 영장을 가졌어. 트레이더들이 패닉에 빠졌네. 어떻게 거래를 계속 유지시킬 텐가?",
                "hint": "영장의 범위를 법률적으로 엄격히 제한하고 트레이더들의 동요를 막아야 한다.",
                "choices": [
                    ("Confine them to conference room C. Demand a copy of the affidavit, invoke attorney-client privilege on proprietary code, and keep order routing open.", "저들을 C 회의실로 격리하십시오. 선서진술서 사본을 요구하고, 고유 코드에 변호사-의뢰인 비닉특권을 주장하며 주문 라우팅을 유지하십시오.", "native_killer", "'Billions'의 바비 액슬로드가 즉각 감탄할 월가 최정상 위기관리 수칙입니다."),
                    ("Delete all database hard drives with a giant magnet.", "거대한 자석으로 모든 데이터베이스 하드디스크를 지웁시다.", "wrong_konglish", "증거인멸죄로 즉각 구속 영장이 발부되는 중범죄 행위입니다."),
                    ("Run out the back door and hide in Starbucks.", "뒷문으로 도망쳐서 스타벅스에 숨어있읍시다.", "mediocre", "패닉에 빠진 초보적이고 비겁한 반응입니다.")
                ]
            },
            {
                "dialogue": "Lead agent says if we execute a single trade on semiconductor futures, he'll arrest the head of the desk for obstruction of justice. Do we pull the plug?",
                "korean": "수사 팀장이 반도체 선물 주문을 하나라도 넣으면 데스크 헤드를 공무집행방해로 체포하겠다고 협박해. 플러그를 뽑을 건가?",
                "hint": "수사관의 불법적인 구두 협박을 법적 녹취로 맞받아치며 헌법적 거래 권리를 지킨다.",
                "choices": [
                    ("Put our general counsel on speaker. Inform the agent that trading without a formal asset freeze injunction constitutes unlawful regulatory interference.", "사내 법무총괄을 스피커폰으로 연결하십시오. 정식 자산동결 가처분 없는 매매 방해는 불법적인 공권력 남용임을 경고하십시오.", "native_killer", "법적 근거 없는 수사관의 월권을 정확한 법리로 제압하는 냉철한 지성입니다."),
                    ("We must obey whatever the agent says because he has a gun.", "총을 가지고 있으니 요원이 시키는 대로 무조건 따라야 합니다.", "wrong_konglish", "정당한 법적 권리를 스스로 포기하고 수백억의 손실을 자초하는 나약한 태도입니다."),
                    ("Ask the agent if he wants to buy some stocks with us.", "수사관에게 우리랑 같이 주식 좀 사보겠냐고 물어봅시다.", "mediocre", "뇌물 수수 미수 혐의를 추가할 수 있는 어처구니없는 제안입니다.")
                ]
            },
            {
                "dialogue": "The US Attorney called off the raid! Our offshore execution held, and we just netted eighty-four million on the morning squeeze. You're an iron general.",
                "korean": "연방 검사가 수색대를 철수시켰어! 해외 주문 집행이 버텨줬고, 오전 숏스퀴즈로 방금 8천 4백만 달러 순익을 챙겼네. 자넨 강철 장군이야.",
                "hint": "국가 권력의 압박 속에서도 막대한 수익을 지켜낸 승리의 희열을 만끽한다.",
                "choices": [
                    ("They bring handcuffs, we bring balance sheets. Wire the bonuses to the trading desk and let's conquer the afternoon bell.", "저들이 수갑을 들고 올 때, 우리는 재무제표로 승부합니다. 트레이딩 데스크에 보너스를 입금하고 오후 장을 정복하러 가시죠.", "native_killer", "월스트리트 헤지펀드의 절대적인 냉혹함과 지배력을 상징하는 명대사입니다."),
                    ("I am shaking like a leaf, I almost cried.", "나뭇잎처럼 벌벌 떨었어요, 거의 울 뻔했습니다.", "wrong_konglish", "압도적 승리 후 유약함을 드러내어 오너의 신뢰를 깎습니다."),
                    ("Thank you Bobby, stock market is very scary.", "감사합니다 바비, 주식 시장은 참 무섭네요.", "mediocre", "월가의 야수 같은 카리스마가 전혀 느껴지지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Attorney-client privilege / Squeeze",
        "key_note": "'Attorney-client privilege'는 변호사-의뢰인 간 비밀유지 특권, 'Squeeze'는 공매도 세력을 압박해 주가를 폭등시키는 전략을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 27: Tech (글로벌 클라우드 다운 제로데이 익스플로잇)
    # -------------------------------------------------------------
    {
        "ep_num": 27,
        "title": "글로벌 클라우드 다운: 제로데이 익스플로잇 긴급 패치",
        "genre": "Tech",
        "speaker": "Linus Sterling (Chief Technology Officer)",
        "emoji": "💻",
        "synopsis": "실리콘밸리 하이퍼스케일 클라우드 데이터센터 워룸. 전 세계 5억 명의 인프라가 멈춘 사상 초유의 제로데이 커널 취약점 공격 앞에서 30분 안에 글로벌 패치를 배포해야 한다.",
        "turns": [
            {
                "dialogue": "All three hundred availability zones in North America and Europe are returning 500 errors. Memory corruption exploit in the hypervisor core. Do we hot-patch in production or sever network gateways?",
                "korean": "북미와 유럽 전역 300개 가용 영역에서 500 에러를 뿜고 있어. 하이퍼바이저 코어의 메모리 손상 취약점이야. 프로덕션에 핫패치를 바로 때릴 텐가, 아니면 네트워크 게이트웨이를 끊을 텐가?",
                "hint": "전면 차단 시 전 세계 금융망이 마비되므로 정밀한 프로덕션 핫패치 배포를 지휘한다.",
                "choices": [
                    ("Deploy the micro-kernel memory fence patch via blue-green canary deployment, starting with ten percent traffic.", "블루-그린 카나리 배포로 10% 트래픽부터 마이크로 커널 메모리 펜스 핫패치를 단계별 적용하십시오.", "native_killer", "'Canary deployment'와 'micro-kernel memory fence'는 전 세계 최상급 인프라 아키텍트의 완벽한 기술적 해법입니다."),
                    ("Turn off all computers and unplug the power cables.", "모든 컴퓨터를 끄고 전원 코드를 뽑아버립시다.", "wrong_konglish", "전 세계 수십만 기업의 데이터를 날려버리는 원시적이고 파멸적인 행동입니다."),
                    ("Wait for Microsoft and Apple to solve this problem for us.", "마이크로소프트나 애플이 대신 해결해줄 때까지 기다려봅시다.", "mediocre", "자체 클라우드 인프라를 운영하는 빅테크 CTO로서 책임감 없는 태도입니다.")
                ]
            },
            {
                "dialogue": "Canary node two failed checksum! The hacker is injecting randomized payload offsets. If we push to the main cluster, we might brick thirty thousand servers.",
                "korean": "카나리 2번 노드 체크섬 실패! 해커가 난수화된 페이로드 오프셋을 주입하고 있어. 메인 클러스터에 밀어 넣으면 3만 대 서버가 벽돌이 될 수도 있어.",
                "hint": "동적 페이로드 난독화를 격리 가상화 컨테이너(Sandboxing)로 무력화한다.",
                "choices": [
                    ("Isolate the tainted memory segment with eBPF runtime tracing and redirect malicious packets to a sinkhole honey-pot.", "eBPF 런타임 추적으로 오염된 메모리 세그먼트를 격리하고 악성 패킷을 싱크홀 허니팟으로 우회시키십시오.", "native_killer", "최첨단 리눅스 커널 보안 기법인 eBPF와 허니팟 우회를 정확히 구사하는 마스터 엔지니어의 해법입니다."),
                    ("Pray to the software gods that the server doesn't break.", "서버가 고장 나지 않도록 소프트웨어 신에게 기도합시다.", "wrong_konglish", "엔지니어링 상황실에서 과학적 분석 대신 미신에 의존하는 어처구니없는 발언입니다."),
                    ("Ask the hacker how much money he wants via email.", "이메일로 해커에게 돈을 얼마나 원하는지 물어봅시다.", "mediocre", "시스템 패치 대신 즉각 굴복하려는 비전문적인 대처입니다.")
                ]
            },
            {
                "dialogue": "eBPF filter locked down the exploit! All thirty thousand bare-metal instances are green. Latency is back below two milliseconds. You just saved the internet.",
                "korean": "eBPF 필터가 취약점을 완벽 차단했어! 3만 대 베어메탈 인스턴스가 전부 정상 가동 중이야. 지연 시간도 2ms 아래로 회복됐네. 자네가 방금 인터넷을 구했어.",
                "hint": "글로벌 재앙을 막아낸 테크 리더의 쿨하고 프로페셔널한 사후 점검.",
                "choices": [
                    ("Commit the patch to upstream kernel, push post-mortem to the status page, and buy the engineering team pizza.", "업스트림 커널에 패치를 커밋하고 상태 페이지에 사후 분석 보고서를 게시한 뒤, 엔지니어링 팀에 피자를 쏘시죠.", "native_killer", "'Commit upstream', 'post-mortem'은 실리콘밸리 엔지니어링 문화의 진정한 품격을 드러냅니다."),
                    ("I am never writing code again, this job gives me gray hair.", "다시는 코딩 안 할 겁니다, 이 일 때문에 흰머리가 나네요.", "wrong_konglish", "위대한 기술적 승리 후 징징거리는 미숙한 반응입니다."),
                    ("Thank you Linus, computers are really complicated.", "감사합니다 리누스, 컴퓨터는 정말 복잡하군요.", "mediocre", "전 세계를 구한 수석 아키텍트다운 전문성이 결여된 평이한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Canary deployment / Post-mortem",
        "key_note": "'Canary deployment'는 위험을 최소화하기 위해 일부 사용자에게 먼저 배포하는 기법, 'Post-mortem'은 장애 사후 분석을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 28: FBI (은행 인질극 무전 심리전)
    # -------------------------------------------------------------
    {
        "ep_num": 28,
        "title": "맨해튼 은행 인질극: 무전기를 통한 협상관의 심리전",
        "genre": "FBI",
        "speaker": "Agent Miller (Crisis Negotiation Unit Lead)",
        "emoji": "🔍",
        "synopsis": "월스트리트 연방 은행 본점. 자동소총으로 무장한 전직 특수부대 탈영병들이 22명의 민간인을 인질로 잡고 헬기를 요구하며 10분마다 1명씩 사살하겠다고 카운트다운을 시작한다.",
        "turns": [
            {
                "dialogue": "He has twenty-two civilians wired with plastic explosives. The SWAT tactical team wants to breach, but thermal cameras show crossfire traps. How do we open the dialogue?",
                "korean": "인질범이 민간인 22명에게 플라스틱 폭약을 감아놨어. SWAT 전술팀은 강습을 원하지만 열화상 카메라상에 교차사격 함정이 포착됐네. 어떻게 대화를 열 것인가?",
                "hint": "적대감을 낮추고 신뢰를 쌓기 위한 FBI 위기 협상 수칙(Active Listening)을 구사한다.",
                "choices": [
                    ("Establish active listening: acknowledge his military service, validate his stress, and offer a dedicated landline without tactical threats.", "적극적 경청을 확립하십시오. 그의 군 복무를 인정하고 스트레스에 공감하며, 전술적 위협 없이 전용 유선 통화선을 제안하십시오.", "native_killer", "'Mindhunter'와 FBI 인질협상 바이블인 적극적 경청(Active Listening)과 공감 형성 기법입니다."),
                    ("Shout through the megaphone that he will go to hell.", "확성기로 그에게 지옥에 갈 거라고 소리 지릅시다.", "wrong_konglish", "인질범을 극단적으로 자극하여 인질 사살을 촉발하는 최악의 행위입니다."),
                    ("Tell him we don't care about his feelings at all.", "우리는 네 감정에 전혀 관심 없다고 말합시다.", "mediocre", "협상의 문을 닫아버리는 무성의한 대응입니다.")
                ]
            },
            {
                "dialogue": "He took the phone. He's demanding a refueling chopper on the roof in five minutes, or he executes the branch manager. How do we buy time?",
                "korean": "전화를 받았네. 5분 안에 옥상에 재급유된 헬기를 대기시키지 않으면 지점장을 처형하겠다고 해. 어떻게 시간을 벌 텐가?",
                "hint": "요구를 전면 거부하지 않으면서도 물리적 지연을 합리화하여 인질의 안전을 확보한다.",
                "choices": [
                    ("Explain that FAA airspace clearance requires twelve minutes and offer immediate medical supplies and water for the hostages in exchange for the clock.", "FAA 영공 허가에 12분이 소요됨을 논리적으로 설명하고, 시간을 연장하는 대가로 인질들을 위한 응급 의약품과 생수를 교환 제안하십시오.", "native_killer", "거절 대신 현실적 절차를 납득시키고 인질의 생존 환경을 개선하는 마스터 협상술입니다."),
                    ("Tell him helicopters are out of stock in New York city.", "뉴욕 시에 헬리콥터 재고가 다 떨어졌다고 말합시다.", "wrong_konglish", "명백한 거짓말로 인질범의 격노와 총격을 부릅니다."),
                    ("Tell him to go ahead and shoot whoever he wants.", "마음대로 아무나 쏘라고 말합시다.", "mediocre", "인질의 목숨을 포기하는 파멸적인 태도입니다.")
                ]
            },
            {
                "dialogue": "He agreed to release the four wounded hostages in exchange for the medical kit! His perimeter defense is relaxing. Outstanding psychological profiling, partner.",
                "korean": "구급상자를 받는 대가로 부상당한 인질 4명을 석방하기로 동의했어! 저자의 방어 태세가 누그러지고 있네. 탁월한 심리 프로파일링이었어, 파트너.",
                "hint": "인질 구출의 결정적 발판을 마련한 협상관의 침착한 후속 지시.",
                "choices": [
                    ("Secure the released civilians, debrief them on bomb wiring, and gently guide the suspect toward a peaceful surrender.", "석방된 민간인을 안전 확보하고 폭약 배선 정보를 디브리핑한 뒤, 용의자를 평화적 자수로 부드럽게 유도하십시오.", "native_killer", "유혈 사태 없이 사건을 종결짓는 FBI 최정상 위기협상관의 품격입니다."),
                    ("Let's throw a grenade inside right now while he is distracted!", "한눈파는 사이에 지금 당장 수류탄을 던져 넣읍시다!", "wrong_konglish", "폭약이 설치된 은행 안으로 수류탄을 던지는 자살 행위입니다."),
                    ("Thank you Agent Miller, negotiating is so tiring.", "감사합니다 밀러 요원님, 협상은 참 피곤하네요.", "mediocre", "긴장감 넘치는 작전 도중 사기를 떨어뜨리는 무기력한 발언입니다.")
                ]
            }
        ],
        "key_expr": "Active listening / Debrief",
        "key_note": "'Active listening'은 상대의 심리를 파악해 설득하는 적극적 경청, 'Debrief'는 작전 직후 세부 정보를 청취·보고함을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 29: Politics (상원 인준 청문회)
    # -------------------------------------------------------------
    {
        "ep_num": 29,
        "title": "상원 인준 청문회: 과거 스캔들에 대한 정면 돌파",
        "genre": "Politics",
        "speaker": "Senator Sterling (Judiciary Committee Chairman)",
        "emoji": "🏛️",
        "synopsis": "워싱턴 D.C. 국회의사당 상원 사법위원회 청문회장. 국무장관 지명자인 당신에게 야당 중진 의원이 10년 전 비밀 외교 기금 의혹을 제기하며 전국 생중계 마이크 앞에서 사퇴를 압박한다.",
        "turns": [
            {
                "dialogue": "Nominee, a recently unredacted cable suggests you authorized backchannel payments during the hostage crisis in Bogota. Are you a diplomat, or a rogue operator violating federal law?",
                "korean": "지명자, 최근 기밀 해제된 전문에 따르면 귀하가 보고타 인질 사태 당시 막후 자금 지급을 승인했다고 되어 있습니다. 귀하는 외교관입니까, 아니면 연방법을 어긴 독단적 공작원입니까?",
                "hint": "적대적인 이분법 프레임 질문에 휘말리지 않고 국가 안보와 법적 정당성을 웅변한다.",
                "choices": [
                    ("I acted under direct presidential authority pursuant to the War Powers Resolution, saving nine American lives without surrendering our strategic deterrence.", "저는 전쟁권한법에 의거한 대통령의 직접 권한에 따라 행동했으며, 국가의 전략적 억지력을 훼손하지 않고 9명의 미국인 생명을 구했습니다.", "native_killer", "'House of Cards'나 'The West Wing' 속 최고위 공직자의 당당하고 흠잡을 데 없는 헌법적 답변입니다."),
                    ("I don't remember anything, my memory is very bad.", "전 아무것도 기억 안 납니다, 기억력이 아주 나빠서요.", "wrong_konglish", "무책임한 발뺌으로 위증 혐의와 즉각 낙마를 초래합니다."),
                    ("Why are you asking me such mean questions on TV?", "왜 TV 생방송에서 저한테 이렇게 못된 질문만 하십니까?", "mediocre", "국가 지도자 후보로서의 품격을 잃고 감정적으로 징징대는 모습입니다.")
                ]
            },
            {
                "dialogue": "The minority leader is calling for your immediate recusal from Middle East negotiations. How can our allies trust your moral compass after this?",
                "korean": "야당 원내대표가 중동 협상에서 귀하의 즉각적인 제척을 요구하고 있습니다. 이런 의혹 속에서 우리 동맹국들이 어떻게 귀하의 도덕적 나침반을 신뢰하겠습니까?",
                "hint": "도덕적 정당성과 동맹국들과의 굳건한 외교적 신뢰 자산을 천명한다.",
                "choices": [
                    ("Trust is forged in crisis, not partisan debate. Our allies stand with leaders who make agonizing calls to defend the free world, not armchair critics.", "신뢰는 정쟁이 아닌 위기 속에서 단련됩니다. 우리 동맹들은 방구석 비평가가 아니라 자유 세계 수호를 위해 고뇌에 찬 결단을 내리는 지도자를 신뢰합니다.", "native_killer", "정치적 공세를 단숨에 무력화하고 국가적 지도자의 위엄을 세우는 명연설입니다."),
                    ("Our allies don't trust us anyway, so it doesn't matter.", "어차피 동맹들도 우리 안 믿으니까 별 상관없습니다.", "wrong_konglish", "외교 관계 전체를 파탄 낼 수 있는 위험천만한 망언입니다."),
                    ("I promise I will never do backchannels again.", "다시는 뒷거래 안 하겠다고 약속드리겠습니다.", "mediocre", "과거의 정당한 국가 행위를 스스로 죄악시하며 위축되는 나약한 태도입니다.")
                ]
            },
            {
                "dialogue": "That gavel just sounded. Bipartisan confirmation passed sixty-two to thirty-eight. Madam Secretary, you carried that committee like a statesman.",
                "korean": "의사봉이 방금 울렸습니다. 초당적 인준안이 62대 38로 통과되었습니다. 장관님, 진정한 정치가답게 상원 위원회를 압도하셨습니다.",
                "hint": "인준 통과 후 국가와 세계 평화를 위한 사명감을 다짐한다.",
                "choices": [
                    ("The mandate is secured. Inform the diplomatic corps: America's foreign policy is steady, resolute, and open for engagement.", "국민의 위임이 확보되었습니다. 외교관들에게 전하십시오: 미국의 외교 정책은 흔들림 없고 단호하며 대화에 열려 있다고 말입니다.", "native_killer", "국무장관으로서 세계 무대에 던지는 가장 웅장하고 결의에 찬 취임 성명입니다."),
                    ("Finally! Now I get free bodyguard service!", "드디어! 이제 나도 무료 경호 서비스 받는다!", "wrong_konglish", "국가 중책을 사적 특권으로 여기는 천박한 반응입니다."),
                    ("Thank you Senator, politicians talk too much.", "감사합니다 의원님, 정치인들은 참 말이 많네요.", "mediocre", "역사적인 인준의 무게감을 희석시키는 가벼운 푸념입니다.")
                ]
            }
        ],
        "key_expr": "Strategic deterrence / Partisan debate",
        "key_note": "'Strategic deterrence'는 전략적 전쟁 억지력, 'Partisan debate'는 당리당략에 치우친 정쟁을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 30: Culinary (블랙 트러플 미스터리 박스 TV 요리 대결)
    # -------------------------------------------------------------
    {
        "ep_num": 30,
        "title": "블랙 트러플 미스터리 박스: TV 요리 대결 결승",
        "genre": "Culinary",
        "speaker": "Gordon Ramsay (World Renowned Master Chef)",
        "emoji": "👨‍🍳",
        "synopsis": "런던 생방송 스튜디오. 마스터셰프 그랜드 파이널 결승전 20분 전, 미스터리 박스에서 이탈리아 피에몬테산 최고급 화이트 트러플과 메인 오리 가슴살이 공개된다.",
        "turns": [
            {
                "dialogue": "Twenty minutes left on the clock! The skin on that duck breast isn't rendering, and your truffle reduction looks like wallpaper paste! What is your turnaround plan, chef?!",
                "korean": "시계에 20분 남았어! 저 오리 가슴살 껍질 지방이 전혀 안 녹아내리고 있고, 트러플 리덕션 소스는 벽지 풀때기 같잖아! 어떻게 만회할 거야, 셰프?!",
                "hint": "고든 램지의 극심한 호통 속에서도 패닉에 빠지지 않고 완벽한 조리 테크닉으로 수습한다.",
                "choices": [
                    ("Score the skin diagonally, hard sear on cold cast iron, and deglaze the pan with aged Madeira wine to emulsify the truffle glaze.", "껍질에 대각선 칼집을 내고 차가운 무쇠 팬에서 강하게 마이야르를 낸 뒤, 숙성 마데이라 와인으로 디글레이징해 트러플 글레이즈를 유화시키겠습니다.", "native_killer", "'Score the skin', 'cold cast iron', 'deglaze with Madeira'는 프로페셔널 셰프의 완벽한 테크닉 용어입니다."),
                    ("I will put tomato ketchup on the duck so nobody tastes it.", "아무도 맛 모르게 오리에 토마토케첩을 바르겠습니다.", "wrong_konglish", "고든 램지에게 즉각 멱살을 잡히고 방송에서 퇴출당할 모욕적인 발언입니다."),
                    ("Sorry Gordon, my hands are shaking too much.", "죄송해요 고든, 손이 너무 떨려요.", "mediocre", "주방에서 자신감을 상실하고 징징거리는 나약한 태도입니다.")
                ]
            },
            {
                "dialogue": "You have three minutes to plate! If that duck is one degree over medium rare, you are handing the trophy to your opponent. Are you confident in your internal temp?",
                "korean": "플레이팅까지 3분 남았어! 저 오리가 미디엄 레어에서 1도라도 넘어가면 자넨 상대에게 트로피를 갖다 바치는 거야. 내부 온도에 자신 있어?",
                "hint": "고기의 레스팅과 심부 온도를 과학적으로 확신하며 플레이팅을 완성한다.",
                "choices": [
                    ("Rested precisely at fifty-four degrees Celsius. The juices are locked. Shaving paper-thin truffle slices onto the caramelized crust now, chef.", "섭씨 54도에서 정확히 레스팅 완료했습니다. 육즙이 가두어졌습니다. 캐러멜라이징된 크러스트 위에 종이처럼 얇은 트러플 슬라이스를 올리겠습니다, 셰프.", "native_killer", "정밀한 온도 제어와 예술적인 플레이팅으로 심사위원을 전율케 하는 완벽한 대답입니다."),
                    ("I forgot to check temperature, maybe it is raw inside.", "온도 확인을 깜빡했는데, 어쩌면 속이 날것일지도 모릅니다.", "wrong_konglish", "식중독 위험과 요리의 기본을 망각한 치명적인 고백입니다."),
                    ("Medium rare is just pink color, so it looks fine.", "미디엄 레어는 그냥 분홍빛이니까 대충 괜찮아 보입니다.", "mediocre", "정밀함이 생명인 파인다이닝 결승에서 안이한 감에 의존하는 답변입니다.")
                ]
            },
            {
                "dialogue": "Taste that. Absolutely bloody gorgeous. The acidity cuts right through the richness. You cooked with passion and finesse. Step up to the podium, champion.",
                "korean": "맛 좀 보게. 완전히 미치도록 훌륭해. 산미가 기름진 맛을 완벽하게 잡아줬어. 열정과 섬세함으로 요리했군. 단상으로 올라오게, 챔피언.",
                "hint": "미슐랭 스타 셰프의 극찬을 받으며 챔피언의 영예를 겸손하고 당당하게 수락한다.",
                "choices": [
                    ("Thank you, Chef. Cooking from the heart with discipline is everything. It is an honor to present my craft to you.", "감사합니다, 셰프님. 규율을 품고 진심으로 요리하는 것이 제 전부입니다. 셰프님께 제 요리를 선보일 수 있어 영광이었습니다.", "native_killer", "장인 정신과 숭고한 겸손함을 갖춘 진정한 마스터셰프의 우승 소감입니다."),
                    ("I am the greatest chef ever, all other contestants are losers!", "내가 역사상 최고의 요리사다, 다른 참가자들은 다 패배자야!", "wrong_konglish", "오만방자함으로 시청자와 심사위원 모두의 눈살을 찌푸리게 하는 저급한 태도입니다."),
                    ("I want to eat a hamburger now because I am hungry.", "배고프니까 이제 햄버거나 먹으러 가고 싶네요.", "mediocre", "영광스러운 승리의 피날레 분위기를 깨뜨리는 뜬금없는 발언입니다.")
                ]
            }
        ],
        "key_expr": "Render the fat / Bloody gorgeous",
        "key_note": "'Render the fat'은 고기 지방을 서서히 녹여 바삭하게 굽다, 'Bloody gorgeous'는 고든 램지의 시그니처 극찬 표현입니다."
    },
    # -------------------------------------------------------------
    # EP 31: Espionage (비엔나 중앙역 망명 과학자 구출)
    # -------------------------------------------------------------
    {
        "ep_num": 31,
        "title": "비엔나 중앙역: 동유럽 망명 과학자 구출 작전",
        "genre": "Espionage",
        "speaker": "Station Chief Carrie (CIA Vienna Station Head)",
        "emoji": "🕵️‍♂️",
        "synopsis": "비엔나 중앙역 3번 플랫폼. 극초음속 미사일 설계도를 소지한 적국 망명 수석 핵물리학자가 추적 요원들에게 포위되기 3분 전, 안전 가옥으로의 전광석화 같은 구출을 완수해야 한다.",
        "turns": [
            {
                "dialogue": "Asset spotted in front of the clock tower with the blue umbrella, but two hostile FSB tails are closing in from sector north. Do we snatch him now or burn the operation?",
                "korean": "타깃이 시계탑 앞 파란 우산 쪽에서 포착됐으나, 적국 FSB 요원 2명이 북쪽 구역에서 좁혀오고 있어. 지금 바로 낚아챌 텐가, 아니면 작전을 파기할 텐가?",
                "hint": "공개된 역내에서 총격전 없이 연막 분산과 군중 침투를 통해 타깃을 안전하게 확보한다.",
                "choices": [
                    ("Deploy flash distraction at the luggage carousel to split their tails, while our sweeper guides the asset through the service tunnel.", "수하물 수취대 쪽에 섬광 교란을 일으켜 적 추적조를 분산시키고, 우리 스위퍼 요원이 타깃을 비상 보수 터널로 유도하십시오.", "native_killer", "'Flash distraction', 'sweeper', 'service tunnel'은 냉전 첩보 스릴러의 완벽한 엑스필(Exfil) 전술입니다."),
                    ("Walk up to the FSB agents and ask them to please stop following.", "FSB 요원들에게 다가가 제발 따라오지 말아 달라고 부탁합시다.", "wrong_konglish", "첩보전에서 적 요원에게 정중히 자비를 구하는 어처구니없는 자살 행위입니다."),
                    ("Shoot guns into the ceiling to make people scream.", "사람들이 비명 지르게 천장에 총을 난사합시다.", "mediocre", "민간인 대량 압사 사고를 유발하고 현지 경찰에 즉시 체포되는 아마추어 행동입니다.")
                ]
            },
            {
                "dialogue": "Asset is in the service tunnel, but the FSB activated biometric rail gates and sealed the exits. We have ninety seconds before Austrian anti-terror units breach.",
                "korean": "타깃이 터널 안으로 들어왔지만, 적들이 생체인식 철도 게이트를 작동시켜 출구를 봉쇄했어. 오스트리아 대테러 부대가 진입하기까지 90초 남았네.",
                "hint": "철도 통제실 해킹이나 외교 번호판 차량을 이용한 즉각적인 탈출로를 확보한다.",
                "choices": [
                    ("Override gate relays with our cyber payload and extraction vehicle with diplomatic plates is idling at loading dock four.", "사이버 페이로드로 게이트 릴레이를 무력화하십시오. 4번 하역장에 외교 번호판을 단 탈출 차량이 대기 중입니다.", "native_killer", "전자전과 외교 면책 특권을 결합한 CIA 탑티어 현장 요원의 기민한 탈출술입니다."),
                    ("Tell the asset to climb through the toilet pipes.", "타깃에게 화장실 배수관을 기어서 탈출하라고 지시합시다.", "wrong_konglish", "노령의 핵물리학자를 배수관에 가두어 질식시키는 황당한 지시입니다."),
                    ("Surrender to the Austrian police and hope they like us.", "오스트리아 경찰에 투항하고 그들이 우리를 좋아해 주길 바랍시다.", "mediocre", "국가급 전략 자산을 적국에 빼앗길 위험에 노출시키는 나약한 포기입니다.")
                ]
            },
            {
                "dialogue": "Wheels up! Extraction bird just cleared Austrian airspace heading for Ramstein Air Base. The missile blueprints are secure. Masterclass in tradecraft.",
                "korean": "이륙 완료! 탈출 수송기가 람슈타인 공군기지를 향해 오스트리아 영공을 방금 벗어났어. 미사일 설계도도 무사해. 첩보 공작의 교과서 같은 활약이었네.",
                "hint": "작전 성공 후 흔적을 지우고 복귀하는 프로페셔널 정보 요원의 결의.",
                "choices": [
                    ("Burn all burner phones, sterilize the safe house, and report to Langley: mission accomplished without a footprint.", "모든 대포폰을 폐기하고 안전 가옥을 멸균 청소한 뒤 랭글리에 보고하십시오: 어떤 흔적도 없이 임무 완수했다고.", "native_killer", "'Sterilize the safe house', 'without a footprint'는 최정예 CIA 블랙 옵스의 서늘하고 완벽한 마무리입니다."),
                    ("I want to take a selfie at the airport and post it online.", "공항에서 셀카 찍어서 인스타그램에 올리고 싶어요.", "wrong_konglish", "비밀 공작 요원의 신원을 만천하에 공개하는 최악의 보안 위반입니다."),
                    ("Thank you Carrie, espionage is very stressful.", "감사합니다 캐리, 스파이 일은 참 스트레스가 심하네요.", "mediocre", "성공적인 비밀 작전의 긴장감에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Tradecraft / Sterilize the safe house",
        "key_note": "'Tradecraft'는 첩보 공작의 전문 기술 및 노하우, 'Sterilize'는 증거와 지문을 완벽히 인멸함을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 32: Aviation (태평양 상공 난기류 및 유압 상실)
    # -------------------------------------------------------------
    {
        "ep_num": 32,
        "title": "태평양 상공 난기류: 유압 시스템 전면 상실",
        "genre": "Aviation",
        "speaker": "Captain 'Sully' Miller (Veteran Senior Captain)",
        "emoji": "✈️",
        "synopsis": "고도 3만 5천 피트 태평양 한가운데 야간 비행. 극심한 청천난기류(CAT)로 2번 엔진 파편이 수평 꼬리날개를 타격하며 유압 3계통이 전부 압력을 잃고 조종간이 굳어버린다.",
        "turns": [
            {
                "dialogue": "Triple hydraulic failure! Control column is completely locked and the nose is pitching down twenty degrees toward the ocean! How do we control our flight attitude?!",
                "korean": "유압 3계통 전멸! 조종간이 완전히 잠겼고 기수가 바다를 향해 20도 급강하하고 있어! 비행 자세를 어떻게 제어할 텐가?!",
                "hint": "조종면이 굳은 상태에서 양쪽 엔진의 추력 차이(Differential thrust)만으로 비행기를 조종한다.",
                "choices": [
                    ("Fly by differential throttle thrust: firewall engine one and pull back engine two to raise the nose, use rudder trim manually.", "좌우 차등 추력으로 조종하십시오: 1번 엔진을 최대 출력으로 올리고 2번을 당겨 기수를 들고, 러더 트림을 수동 조작해야 합니다.", "native_killer", "유나이티드 232편 기적의 생환에서 입증된 'Differential throttle thrust' 비상 조종술입니다."),
                    ("Let go of the controls and jump out with the only parachute.", "조종간을 놓고 기장님 혼자 유일한 낙하산을 메고 탈출하세요.", "wrong_konglish", "300명의 승객을 버리고 혼자 도망치려는 패륜적이고 불가능한 발언입니다."),
                    ("Pull the steering wheel with both hands as hard as possible.", "조종간을 양손으로 있는 힘껏 세게 당겨봅시다.", "mediocre", "유압이 빠진 기계식 잠금 상태에서 무의미하게 체력만 낭비하는 행동입니다.")
                ]
            },
            {
                "dialogue": "Nose leveled at twelve thousand feet, but fuel is leaking and Honolulu is four hundred miles away. Can we stretch the glide or do we ditch at sea?",
                "korean": "1만 2천 피트에서 수평은 잡았으나 연료가 누출되고 있고 호놀룰루는 400마일 밖이야. 활공으로 닿을 수 있을까, 아니면 해상 불시착을 감행해야 하나?",
                "hint": "야간 거친 파도 속 해상 불시착의 치명적 위험을 피하고 비상 활주로 착륙을 시도한다.",
                "choices": [
                    ("Ditching at night in heavy swells is fatal. Calculate best glide speed, dump remaining fuel, and vector toward Midway Atoll emergency strip.", "야간의 높은 파도 속 해상 불시착은 치명적입니다. 최적 활공 속도를 계산하고 잔여 연료를 배출한 뒤 미드웨이 환초 비상 활주로로 기수를 돌리십시오.", "native_killer", "정밀한 항공 항법과 승객 생존율을 극대화하는 위대한 기장의 냉철한 판단입니다."),
                    ("Turn off both engines right now to save gasoline.", "휘발유를 아끼기 위해 지금 당장 두 엔진을 모두 꺼버립시다.", "wrong_konglish", "제트엔진 연료를 가솔린으로 착각하고 양력을 잃어 추락을 자초하는 황당한 발언입니다."),
                    ("Ask the flight attendants to vote on what to do.", "승무원들에게 투표를 해서 결정하자고 물어봅시다.", "mediocre", "비행 조종의 절대적 책임을 승무원 투표로 미루는 무책임한 처신입니다.")
                ]
            },
            {
                "dialogue": "Midway runway in sight! Wheels touching down... reverse thrusters deployed! We're stopped on the centerline! All three hundred souls safe!",
                "korean": "미드웨이 활주로 시야 확보! 바퀴 접지... 역추진 장치 전개! 중앙선 위에 완전히 멈췄어! 승객 승무원 300명 전원 무사 생환했네!",
                "hint": "기적의 착륙을 완수한 후 조종사로서 최고의 안도와 긍지를 표현한다.",
                "choices": [
                    ("Evacuation slides armed. Notify Pacific Command that flight 811 has landed safely. Outstanding airmanship, Captain.", "비상 탈출 슬라이드 대기. 태평양사령부에 811편 안전 착륙을 타전하십시오. 탁월한 비행 기량이었습니다, 기장님.", "native_killer", "'Airmanship'은 프로페셔널 조종사의 품격과 기술을 칭송하는 최고의 항공 경의 표현입니다."),
                    ("I thought we were going to die, I wet my pants.", "진짜 죽는 줄 알고 바지에 실례할 뻔했습니다.", "wrong_konglish", "기적의 비행 직후 조종실의 존엄성을 깎아내리는 천박한 언사입니다."),
                    ("Thank you Sully, airplanes are too dangerous.", "감사합니다 설리 기장님, 비행기는 너무 위험하네요.", "mediocre", "역사에 남을 비상착륙의 감격을 퇴색시키는 평범한 반응입니다.")
                ]
            }
        ],
        "key_expr": "Differential thrust / Airmanship",
        "key_note": "'Differential thrust'는 엔진 추력 차이로 기체를 선회·승강시키는 기법, 'Airmanship'은 조종사의 탁월한 비행 기량을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 33: Sports Management (슈퍼볼 MVP 라커룸 불화)
    # -------------------------------------------------------------
    {
        "ep_num": 33,
        "title": "슈퍼볼 MVP 라커룸 불화: 드래프트 1순위의 반란",
        "genre": "Sports Management",
        "speaker": "Jerry Maguire (Super Agent & Agency Founder)",
        "emoji": "🏈",
        "synopsis": "슈퍼볼 결승전 하프타임 라커룸. 14점 차로 뒤지는 절체절명의 위기에서, 2억 달러 몸값의 간판 쿼터백과 신인 와이드 리시버가 패스 루트를 두고 주먹다짐 직전까지 충돌한다.",
        "turns": [
            {
                "dialogue": "Our star quarterback is refusing to throw to the rookie receiver, and the locker room is split down the middle! We have ten minutes before second-half kickoff. How do you fix this team, Jerry?!",
                "korean": "우리 스타 쿼터백이 신인 리시버에게 패스 안 던지겠다고 버티고, 라커룸이 둘로 쪼개졌어! 후반전 킥오프까지 10분 남았네. 이 팀을 어떻게 수습할 건가, 제리?!",
                "hint": "두 스타 선수의 자존심을 건드리지 않으면서 오직 우승이라는 공통 목표로 결집시킨다.",
                "choices": [
                    ("Remind both men that personal legacies are won with rings, not personal vendettas. Call the slant-route play and demand they execute.", "개인의 유산은 사적인 원한이 아니라 우승 반지로 완성된다는 점을 상기시키십시오. 슬랜트 루트 작전을 부르고 실행을 명령하십시오.", "native_killer", "'Personal legacies are won with rings'는 스포츠 에이전트 영화의 가슴을 때리는 감동적 리더십입니다."),
                    ("Tell the coach to cancel the game and let everyone go home.", "감독에게 경기를 취소하고 다 집에 가자고 말합시다.", "wrong_konglish", "슈퍼볼 결승전에서 경기를 기권하자는 상식 밖의 황당한 제안입니다."),
                    ("Offer both players a hundred dollars cash if they hug each other.", "서로 포옹하면 현금 100달러씩 주겠다고 제안해봅시다.", "mediocre", "수억 달러 몸값의 프로 선수들을 유치원생 취급하는 어설픈 중재입니다.")
                ]
            },
            {
                "dialogue": "Quarterback says if the rookie drops one more ball, he wants him benched permanently, or he demands a trade tomorrow. Do you back the veteran or the future?",
                "korean": "쿼터백이 신인이 공 하나만 더 떨어뜨리면 영구 벤치로 보내든가, 아니면 내일 당장 트레이드를 요구하겠대. 베테랑을 편들 텐가, 팀의 미래를 편들 텐가?",
                "hint": "어느 한쪽의 편을 들지 않고 챔피언십 멘탈리티로 두 사람의 화학작용을 폭발시킨다.",
                "choices": [
                    ("Demand greatness from both: tell the veteran to throw with trust, and look the rookie in the eye to catch everything in his zip code.", "둘 모두에게 위대함을 요구하십시오: 베테랑에겐 신뢰를 담아 던지라 하고, 신인에겐 자기 구역 안의 모든 공을 낚아채라고 눈을 보며 명하십시오.", "native_killer", "'Jerry Maguire'의 진정한 정수인 선수들의 심장을 뛰게 하는 영혼의 코칭입니다."),
                    ("Tell the quarterback he is old and useless now.", "쿼터백에게 이제 늙고 쓸모없으니 입 닥치라고 소리 지릅시다.", "wrong_konglish", "프랜차이즈 스타를 모욕하여 팀을 완전히 파멸시키는 최악의 언사입니다."),
                    ("Flip a coin to see whose side we take.", "동전을 던져서 누구 편을 들지 결정합시다.", "mediocre", "리더십을 운에 맡겨버리는 무책임한 처신입니다.")
                ]
            },
            {
                "dialogue": "Hail Mary touchdown as time expired! The rookie caught the veteran's sixty-yard spiral in the endzone! World Champions! You brought this family together!",
                "korean": "경기 종료 직전 헤일메리 터치다운 성공! 신인이 엔드존에서 베테랑의 60야드 스파이럴 패스를 낚아챘어! 월드 챔피언 등극! 자네가 이 팀을 하나로 묶었네!",
                "hint": "역사적 역전승 직후 감격을 나누며 전설적인 명대사로 축하한다.",
                "choices": [
                    ("They showed us the heart, now tomorrow the world shows them the money! Savor this Lombardi trophy, gentlemen!", "선수들이 심장을 보여줬으니, 내일은 세상이 돈을 보여줄 차례입니다! 롬바르디 트로피를 만끽하십시오, 챔피언들!", "native_killer", "'Show me the money'와 'Lombardi trophy'를 완벽하게 버무린 최고의 스포츠 에이전트 세리머니입니다."),
                    ("I made a lot of bets on this game, I am rich!", "나 이 경기에 불법 베팅 많이 걸어놨는데 대박 났다!", "wrong_konglish", "불법 도박 사실을 자백하여 리그에서 영구 퇴출당할 어리석은 발언입니다."),
                    ("Thank you Jerry, football is too loud.", "감사합니다 제리, 풋볼은 너무 시끄럽네요.", "mediocre", "슈퍼볼 우승의 전율에 찬물을 끼얹는 평범한 한마디입니다.")
                ]
            }
        ],
        "key_expr": "Lombardi trophy / Hail Mary",
        "key_note": "'Lombardi trophy'는 NFL 슈퍼볼 우승 트로피, 'Hail Mary'는 경기 막판 승부를 뒤집는 기적의 장거리 패스를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 34: Haute Couture (멧 갈라 레드카펫 1시간 전)
    # -------------------------------------------------------------
    {
        "ep_num": 34,
        "title": "멧 갈라 레드카펫 1시간 전: 드레스 훼손 사태",
        "genre": "Haute Couture",
        "speaker": "Miranda Priestly (Vogue Global Editor-in-Chief)",
        "emoji": "👠",
        "synopsis": "뉴욕 메트로폴리탄 미술관 멧 갈라 현장 앞 프라이빗 드레싱 스위트. 레드카펫 입장 45분 전, 50만 달러 상당의 맞춤 오뜨 꾸뛰르 실크 드레스 트레인이 메이크업 오일에 오염된다.",
        "turns": [
            {
                "dialogue": "A grease stain on unrefined Lyon silk forty minutes before the stairs. Anna is waiting, the paparazzi are screaming, and my lead muse looks like a tragic disaster. Tell me why I shouldn't fire you right now.",
                "korean": "계단 입장 40분 전에 리옹산 실크 위에 기름 얼룩이라니. 안나 윈투어가 기다리고 있고 파파라치들이 아우성인데, 내 뮤즈가 비극적 참사 꼴을 하고 있잖아. 내가 왜 자넬 지금 당장 해고하지 말아야 하는지 말해봐.",
                "hint": "얼룩을 감추는 대신 해체와 재구성을 통해 오히려 아방가르드한 예술적 명작으로 재탄생시킨다.",
                "choices": [
                    ("Don't conceal it; deconstruct it. Sheer the stained train into a dramatic asymmetric high-low hem and pin vintage sapphire brooches along the fold.", "숨기지 말고 해체하십시오. 오염된 트레인을 과감하게 비대칭 하이-로우 헴라인으로 커팅하고 주름을 따라 빈티지 사파이어 브로치를 장식하겠습니다.", "native_killer", "'악마는 프라다를 입는다'의 미란다 프리슬리를 경탄케 할 천재 패션 디렉터의 아방가르드한 순발력입니다."),
                    ("Put a giant bath towel over her head and run.", "뮤즈 머리에 커다란 목욕 수건을 덮어씌우고 도망칩시다.", "wrong_konglish", "패션계의 여왕 앞에서 스스로 커리어를 끝장내는 기괴한 행동입니다."),
                    ("Tell the photographers that grease is the new trend.", "사진기자들에게 기름 얼룩이 요즘 새로운 유행이라고 우겨봅시다.", "mediocre", "설득력 없는 변명으로 프로페셔널한 비평가들의 조롱을 부릅니다.")
                ]
            },
            {
                "dialogue": "Shear a five-hundred-thousand-dollar archive gown with scissors? If this looks tacky, your name will be permanently erased from Paris to Milan.",
                "korean": "50만 달러짜리 아카이브 드레스를 가위로 자르겠다고? 이게 촌스러워 보인다면, 자네 이름은 파리에서 밀라노까지 영구히 지워질 거야.",
                "hint": "미적 확신과 역사적 레퍼런스를 제시하며 완벽한 드레이핑으로 증명한다.",
                "choices": [
                    ("Alexander McQueen proved that danger is the essence of couture. Trust my eye, Miranda; this will redefine tonight's red carpet.", "알렉산더 맥퀸은 위험성이야말로 오뜨 꾸뛰르의 본질임을 증명했습니다. 제 안목을 믿으십시오, 미란다. 오늘 밤 레드카펫을 재정의할 것입니다.", "native_killer", "패션사적 레퍼런스와 흔들리지 않는 예술적 자신감으로 수석 편집장을 굴복시키는 대사입니다."),
                    ("I am just guessing, so please don't sue me if it is ugly.", "그냥 대충 짐작한 거니까 못생겨도 고소는 하지 마세요.", "wrong_konglish", "자신의 디자인에 책임을 지지 않으려는 아마추어적 발언입니다."),
                    ("Maybe we can borrow a cheap dress from Zara nearby.", "근처 자라 매장에서 저렴한 드레스 하나 빌려오면 어떨까요?", "mediocre", "멧 갈라의 격식을 전혀 모르는 패션 문외한의 소리입니다.")
                ]
            },
            {
                "dialogue": "The Met steps went dead silent, then exploded into applause. Vogue Runway just crowned it the look of the decade. Perhaps you do have a pulse after all.",
                "korean": "메트로폴리탄 계단이 숨을 죽이더니, 폭발적인 환호가 터져 나왔어. 보그 런웨이가 방금 10년 만의 최고의 룩으로 선정했네. 자네에게도 제법 감각이란 게 있었군.",
                "hint": "미란다의 까다로운 칭찬을 우아하게 넘기며 패션 디렉터의 위엄을 굳힌다.",
                "choices": [
                    ("Perfection is boring, Miranda; vision is eternal. Now let us escort our muse to the Grand Gala.", "완벽함은 지루하지만, 예술적 비전은 영원합니다, 미란다. 이제 우리의 뮤즈를 그랜드 갈라로 에스코트하시죠.", "native_killer", "'The Devil Wears Prada'의 정점을 찍는 가장 품격 있고 세련된 디자이너의 화답입니다."),
                    ("Yay! Can I have a picture with Rihanna now?", "와우! 이제 리한나랑 같이 사진 찍어도 되나요?", "wrong_konglish", "세계 최고 패션 디렉터의 품위를 잃고 극성 팬처럼 구는 경박한 반응입니다."),
                    ("Thank you Miranda, sewing clothes is hard work.", "감사합니다 미란다, 바느질은 참 힘든 노동이네요.", "mediocre", "예술적 쾌거를 단순 노역으로 격하시키는 아쉬운 소감입니다.")
                ]
            }
        ],
        "key_expr": "Deconstruct / Essence of couture",
        "key_note": "'Deconstruct'는 기존 패션의 구조를 해체해 재창조하다, 'Haute couture'는 최고급 맞춤 의상을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 35: Crisis PR (글로벌 톱스타 개인 DM 해킹 유출)
    # -------------------------------------------------------------
    {
        "ep_num": 35,
        "title": "글로벌 엔터사 해킹: 톱스타 개인 DM 유출 진화",
        "genre": "Crisis PR",
        "speaker": "Olivia Pope (Crisis Management Fixer)",
        "emoji": "🎙️",
        "synopsis": "워싱턴 D.C. 위기관리 전략 벙커. 오스카 남우주연상 배우의 스마트폰이 해킹되어 동료 배우와 감독들을 험담한 사적인 DM 수백 장이 해외 찌라시 사이트에 실시간 유출되기 시작한다.",
        "turns": [
            {
                "dialogue": "Three gossip outlets just published screenshots of our client calling his director an illiterate hack. Sponsors are already drafting termination notices. How do we take the air out of this room?",
                "korean": "3개 가십 매체가 우리 의뢰인이 감독을 글도 못 쓰는 무능력자라고 욕한 DM 캡처를 올렸어. 스폰서들은 벌써 계약 해지 통지서를 작성 중이야. 어떻게 이 화재의 산소를 차단할 텐가?",
                "hint": "유출 사실의 진위 공방으로 시간을 끌지 않고, 즉각적인 해킹 피해자 규정과 선제적 유머로 맞받아친다.",
                "choices": [
                    ("Do not dispute the messages; pivot to federal cybercrime victimhood. Have the client post a self-deprecating video laughing with that exact director.", "메시지 진위 공방을 벌이지 말고 연방 사이버 범죄 피해자로 프레임을 전환하십시오. 의뢰인이 바로 그 감독과 어깨동무하고 유쾌하게 자폭하는 영상을 올리게 하십시오.", "native_killer", "'Scandal'의 올리비아 포프다운 빛의 속도 프레임 전환과 유머를 활용한 위기 진화술입니다."),
                    ("Tell the press that the client was drunk and hates everyone.", "기자들에게 의뢰인이 술에 취해 모두를 증오한다고 솔직히 털어놓읍시다.", "wrong_konglish", "불난 집에 휘발유를 들이붓고 배우의 인성을 만천하에 매장시키는 발언입니다."),
                    ("Pay the gossip site ten million dollars in cash secretly.", "가십 사이트에 비밀리에 현금 천만 달러를 건넵시다.", "mediocre", "공갈 협박범의 먹잇감이 되어 더 큰 2차 폭로를 자초하는 악수입니다.")
                ]
            },
            {
                "dialogue": "The sponsor's board is demanding a public apology on live television tonight, or they pull their twenty-million-dollar endorsement. Do we put him on air?",
                "korean": "광고주 이사회가 오늘 밤 생방송에서 공개 사과를 하지 않으면 2천만 달러짜리 전속 계약을 해지하겠다고 최후통첩을 보냈어. 배우를 생방송에 세울 텐가?",
                "hint": "굴욕적인 생방송 사과 대신 품위 있는 공동 자선 기금 발표로 광고주의 체면을 세워준다.",
                "choices": [
                    ("Never grovel on live TV. Co-host a joint charity fundraiser with the sponsor to support cyber-bullying victims, turning their outrage into brand goodwill.", "생방송에서 비굴하게 무릎 꿇지 마십시오. 광고주와 공동으로 사이버 폭력 피해자 지원 자선 기금을 출범시켜 저들의 분노를 브랜드 호감도로 치환하십시오.", "native_killer", "위기를 오히려 기업의 ESG 사회공헌 브랜드 캠페인으로 승화시키는 최상급 PR 기법입니다."),
                    ("Tell the sponsor we will boycott their luxury bags forever.", "광고주에게 당신네 명품 가방을 평생 불매하겠다고 협박합시다.", "wrong_konglish", "광고주를 적으로 돌려 수백억의 위약금 소송을 당하는 파멸적 대응입니다."),
                    ("Cry on TV and beg the audience to forgive him.", "TV에 나가서 울면서 시청자들에게 용서해달라고 싹싹 빕시다.", "mediocre", "톱스타로서의 신비감과 카리스마를 완전히 잃고 우스꽝스러워집니다.")
                ]
            },
            {
                "dialogue": "The video went hyper-viral! The director posted, 'He's right, my script was terrible!' and fans are praising their brotherhood. You turned a disaster into a PR masterclass.",
                "korean": "자폭 영상이 초대형 바이럴을 탔어! 감독이 '맞아, 내 각본 쓰레기였지!'라고 유쾌하게 댓글을 달았고 팬들은 둘의 찐 우정에 열광 중이야. 자네가 참사를 PR 교과서로 바꿨네.",
                "hint": "위기를 완벽하게 수습한 위기관리 전문가로서의 묵직한 자부심.",
                "choices": [
                    ("The storm is weathered. Inform the client to stay offline for forty-eight hours while we lock in his next contract.", "폭풍은 지나갔습니다. 의뢰인에게 48시간 동안 SNS를 끄고 조용히 대기하라 전하십시오. 그사이 다음 계약을 확정 짓겠습니다.", "native_killer", "위기 극복 후에도 방심하지 않고 클라이언트를 통제하는 탑 해결사의 진면목입니다."),
                    ("Now I want to read all the other leaked celebrity messages!", "이제 다른 연예인들 유출된 문자도 다 구경해봐야지!", "wrong_konglish", "고객의 기밀을 다루는 전문가로서 기본적 윤리의식이 결여된 발언입니다."),
                    ("Thank you Olivia, people on Twitter are so scary.", "감사합니다 올리비아, 트위터 사람들은 너무 무섭네요.", "mediocre", "여론 전쟁의 사령관답지 않은 연약한 한탄입니다.")
                ]
            }
        ],
        "key_expr": "Take the air out of the room / Weather the storm",
        "key_note": "'Take the air out of the room'은 논란의 산소를 차단해 불씨를 끄다, 'Weather the storm'은 난국을 극복함을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 36: Luxury Real Estate (맨해튼 랜드마크 브라운스톤 국부펀드)
    # -------------------------------------------------------------
    {
        "ep_num": 36,
        "title": "맨해튼 랜드마크 브라운스톤: 국부펀드와의 압박 협상",
        "genre": "Luxury Real Estate",
        "speaker": "Ryan Serhant (Billionaire Real Estate Broker)",
        "emoji": "🏙️",
        "synopsis": "센트럴파크 웨스트 역사적 랜드마크 브라운스톤 대저택. 중동 국부펀드가 6천만 달러 전액 현금 매수를 제시했으나, 유서 깊은 뉴욕 자선재단 매도인은 건물 원형 보존 조항을 양보하지 않는다.",
        "turns": [
            {
                "dialogue": "The Sovereign Wealth Fund has sixty million cash ready to wire, but the seller won't sign unless they guarantee the 1890s ballroom remains untouched forever. How do we break this deadlock?",
                "korean": "국부펀드는 6천만 달러 현금 송금 준비가 끝났는데, 매도인은 1890년대 무도회장 원형을 영구 보존한다는 보장이 없으면 도장을 못 찍겠대. 이 교착상태를 어떻게 깰 텐가?",
                "hint": "자산 보존의 역사적 상징성을 국부펀드의 브랜드 가치로 포장하여 타협을 이끌어낸다.",
                "choices": [
                    ("Structure the ballroom as a tax-advantaged historic preservation easement, allowing the fund to claim millions in deductions while protecting heritage.", "무도회장을 세제 혜택이 주어지는 역사 보존 지역권으로 설정하여, 유산을 지키면서도 펀드 측에 수백만 달러의 감면 혜택을 안겨주십시오.", "native_killer", "'Historic preservation easement'는 맨해튼 하이엔드 부동산 법률의 최고봉 절세·보존 양립 솔루션입니다."),
                    ("Tear down the ballroom at midnight so there is nothing to fight about.", "싸울 일 없게 자정에 무도회장을 몰래 불도저로 밀어버립시다.", "wrong_konglish", "문화재 보호법 위반으로 형사 처벌을 받고 거래를 완전히 파탄 냅니다."),
                    ("Tell the seller to stop caring about old dusty rooms.", "매도인에게 먼지 쌓인 옛날 방 따위 신경 끄라고 핀잔을 줍시다.", "wrong_konglish", "의뢰인의 유서 깊은 가치관을 모욕하여 즉각 계약을 파기당합니다.")
                ]
            },
            {
                "dialogue": "The fund likes the tax deduction, but they demand an exclusive closing window of seventy-two hours or they divert the capital to a London townhouse. Can our escrow team move that fast?",
                "korean": "펀드 측이 절세 혜택은 마음에 들어 하지만, 72시간 안에 클로징하지 않으면 런던 타운하우스로 자금을 돌리겠다고 압박해. 우리 에스크로 팀이 그렇게 빨리 움직일 수 있나?",
                "hint": "긴급 타이틀 조사와 24시간 에스크로 가동을 지휘하며 거래를 마감한다.",
                "choices": [
                    ("Mobilize our title insurer for an accelerated priority search, wire the hard deposit into dual-signature escrow, and close by Friday noon.", "소유권 보험사를 총동원해 우선순위 고속 실사를 진행하고, 이중 서명 에스크로에 계약금을 예치하여 금요일 정오까지 클로징하십시오.", "native_killer", "'Accelerated priority search'와 'dual-signature escrow'는 탑티어 브로커의 번개 같은 실행력입니다."),
                    ("Tell them real estate takes six months, so be patient.", "부동산은 원래 6개월 걸리니까 인내심을 가지라고 말합시다.", "wrong_konglish", "글로벌 큰손 고객의 자금 스케줄을 무시해 수십억 수수료를 허공에 날립니다."),
                    ("Ask the bank to work on weekends without overtime pay.", "은행원들에게 주말에 야근 수당 없이 일해달라고 부탁해봅시다.", "mediocre", "실현 불가능하고 비현실적인 요청으로 시간을 낭비합니다.")
                ]
            },
            {
                "dialogue": "Escrow cleared! Sixty million transferred, deed recorded with the city, and the landmark ballroom is preserved for history. That's a masterstroke, partner.",
                "korean": "에스크로 통과! 6천만 달러 송금 완료, 뉴욕시에 등기 이전 완료, 유서 깊은 무도회장도 역사 속에 보존되었네. 완벽한 신의 한 수였어, 파트너.",
                "hint": "역사적 건축물 보존과 기록적 거래를 동시에 완수한 브로커의 품격 있는 자축.",
                "choices": [
                    ("We protected history and printed capital in one single transaction. Let's send the crystal decanter to both principals.", "우리는 한 번의 거래로 역사를 지켜내고 막대한 수익을 창출했습니다. 양측 오너에게 고급 크리스털 디캔터를 선물로 보냅시다.", "native_killer", "품격과 실익을 모두 거머쥔 맨해튼 최고급 부동산 브로커의 세련된 마무리입니다."),
                    ("I want to move into that brownstone and live there myself.", "저 브라운스톤에 제가 직접 들어가서 살고 싶네요.", "wrong_konglish", "고객의 자산에 사적인 탐욕을 드러내는 부적절한 언사입니다."),
                    ("Thank you Ryan, selling houses is very tiring.", "감사합니다 라이언, 집 파는 일은 참 피곤하네요.", "mediocre", "역대급 랜드마크 거래의 웅장함을 살리지 못하는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Preservation easement / Dual-signature escrow",
        "key_note": "'Preservation easement'는 역사 건축물 보존에 따른 세제 혜택 권리, 'Escrow'는 거래 대금 결제 예치 제도를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 37: Hollywood Agency (칸 영화제 황금종려상 도난 필름)
    # -------------------------------------------------------------
    {
        "ep_num": 37,
        "title": "칸 영화제 황금종려상 경쟁작: 도난 필름 협상",
        "genre": "Hollywood Agency",
        "speaker": "Ari Gold (Top Hollywood Super-Agent)",
        "emoji": "🎬",
        "synopsis": "프랑스 칸 크루아제트 거리 해변 호텔 펜트하우스. 내일 밤 황금종려상 공식 갈라 스크리닝을 앞두고, 거장 감독의 영화 원본 디지털 마스터 드라이브가 도난당하며 500만 유로 몸값 요구가 들어온다.",
        "turns": [
            {
                "dialogue": "Some cyber pirate in Marseille stole the uncompressed DCP master drive of our Cannes premiere! If we don't pay five million by midnight, they leak the ending on 4chan! What is your play, hotshot?!",
                "korean": "마르세유의 어떤 사이버 해적이 우리 칸 영화제 출품작의 무압축 DCP 마스터 드라이브를 훔쳐 갔어! 자정까지 5백만 유로 안 주면 4chan에 결말을 유출하겠대! 어떻게 할 거야, 에이스?!",
                "hint": "몸값을 지급해 범죄를 조장하지 않고, 디지털 워터마크 역추적과 칸 집행위원회의 보안 상영 시스템을 가동한다.",
                "choices": [
                    ("Do not pay a single cent. Activate the forensic digital watermark embedded in the frames to geolocate the drive, and notify Interpol.", "단 1센트도 주지 마십시오. 프레임에 심어진 포렌식 디지털 워터마크를 가동해 드라이브의 위치를 추적하고 인터폴에 공조 요청하십시오.", "native_killer", "'Forensic digital watermark'와 인터폴 공조는 할리우드 스튜디오 보안 프로토콜의 정석입니다."),
                    ("Give them five million euros and say thank you very much.", "5백만 유로를 다 주고 대단히 고맙다고 인사합시다.", "wrong_konglish", "해적의 협박에 무릎 꿇고 영화 산업 전체를 인질로 내주는 어리석은 굴복입니다."),
                    ("Cancel the movie premiere and tell everyone to go home.", "영화 상영을 취소하고 모두 집에 가라고 공지합시다.", "mediocre", "황금종려상 수상 기회를 스스로 걷어차는 비겁한 도망입니다.")
                ]
            },
            {
                "dialogue": "Interpol is raiding the IP address, but the screening is in four hours and our backup drive is locked in a bank vault in Paris. How do we get the movie onto the Palais screen?!",
                "korean": "인터폴이 IP를 급습 중이지만 상영은 4시간 뒤고 백업 드라이브는 파리 은행 금고에 묶여 있어. 영화를 어떻게 팔레 드 페스티벌 스크린에 올릴 텐가?!",
                "hint": "군용 암호화 위성 전송망을 활용해 고속 다이렉트 스트리밍 상영을 성사시킨다.",
                "choices": [
                    ("Charter a high-speed encrypted satellite pipeline from the French Ministry of Culture direct to the festival projection booth.", "프랑스 문화부의 초고속 암호화 위성 파이프라인을 전세 내어 영화제 영사실로 다이렉트 전송하십시오.", "native_killer", "'Entourage'의 아리 골드도 입을 다물지 못할 정관계와 기술을 결합한 기적의 돌파구입니다."),
                    ("Tell the actors to go up on stage and act the movie live for two hours.", "배우들에게 무대에 올라가서 2시간 동안 라이브로 연기하라고 시킵시다.", "wrong_konglish", "블록버스터 예술 영화를 즉흥 학예회로 전락시키는 황당한 발상입니다."),
                    ("Show an old cartoon instead and hope the judges don't notice.", "대신 옛날 만화영화나 틀어주고 심사위원들이 눈치채지 못하길 기도합시다.", "mediocre", "세계 최고 영화제에서 영구 퇴출당할 어이없는 속임수입니다.")
                ]
            },
            {
                "dialogue": "The satellite feed held in 8K crystal clarity! A fifteen-minute standing ovation, and the Jury President was crying! Palme d'Or locked! We own European cinema!",
                "korean": "위성 송출이 8K 극강 화질로 완벽히 버텼어! 15분간의 기립 박수가 터졌고 심사위원장이 눈물을 흘렸네! 황금종려상 확정이야! 우리가 유럽 영화계를 집어삼켰어!",
                "hint": "세계 최고 영화제 제패 후 영화 산업의 정점에 선 카리스마로 화답한다.",
                "choices": [
                    ("The art was protected, the thieves are in handcuffs, and our worldwide distribution rights just quintupled. Call the private jet, Ari.", "예술은 지켜졌고 도둑들은 수갑을 찼으며 전 세계 배급권 가치는 5배로 폭등했습니다. 전용기를 대기시키시죠, 아리.", "native_killer", "할리우드 최고 에이전트의 거침없는 승리와 상업적 대성공을 알리는 명대사입니다."),
                    ("I am tired of France, I want a cheeseburger now.", "프랑스 지겨워요, 지금 당장 치즈버거나 먹고 싶네요.", "wrong_konglish", "세계 영화사의 전설적인 승리 직후 분위기를 깨뜨리는 천박한 투정입니다."),
                    ("Thank you Ari, movie festivals are quite loud.", "감사합니다 아리, 영화제는 참 시끄러운 곳이네요.", "mediocre", "황금종려상의 벅찬 감격에 비해 지나치게 무미건조합니다.")
                ]
            }
        ],
        "key_expr": "Forensic watermark / Standing ovation",
        "key_note": "'Forensic watermark'는 불법 유출 경로를 추적하는 미세 식별 코드, 'Standing ovation'은 열광적인 기립 박수를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 38: 5-Star Hotel (억만장자 로열 웨딩 파파라치 드론 침투)
    # -------------------------------------------------------------
    {
        "ep_num": 38,
        "title": "세계 억만장자 결혼식: 파파라치 드론 침투 차단",
        "genre": "5-Star Hotel",
        "speaker": "Monsieur Dupont (Grand Hotelier & GM)",
        "emoji": "🏨",
        "synopsis": "센트럴파크 전경이 내려다보이는 더 플라자 루프탑 테라스. 2천만 달러짜리 글로벌 로열 패밀리 비공개 결혼식 서약 5분 전, 불법 파파라치 드론 3기가 상공에 진입한다.",
        "turns": [
            {
                "dialogue": "Three high-definition camera drones are hovering sixty feet above the bride's veil! The Royal Family is threatening to walk out and sue us for breach of privacy. How do we neutralize this intrusion?!",
                "korean": "신부의 면사포 60피트 상공에 고화질 카메라 드론 3기가 떠 있어! 왕실 일가가 즉각 철수하고 사생활 침해로 우리를 고소하겠다고 위협 중이야. 이 침입을 어떻게 무력화할 텐가?!",
                "hint": "총기 사격 등 위험한 물리력 대신 지향성 전파 방해 드론 재머(Drone Jammer)와 보안 차양막을 전개한다.",
                "choices": [
                    ("Deploy our tactical directional RF drone jammer to force an automatic return-to-home, while unfurling the silk acoustic privacy canopies.", "전술 지향성 주파수 드론 재머를 가동해 드론을 강제 자동 회항시키고, 실크 방음 프라이버시 차양막을 즉시 펼치십시오.", "native_killer", "'Directional RF jammer'와 'privacy canopy'는 세계 최고 럭셔리 호텔의 첨단 VIP 방호 프로토콜입니다."),
                    ("Throw champagne bottles at the sky until one hits a drone.", "드론에 맞을 때까지 샴페인 병을 하늘로 집어던집시다.", "wrong_konglish", "유리 파편이 하객들에게 쏟아져 대규모 부상을 초래하는 몰상식한 행동입니다."),
                    ("Ask the bride to smile and wave at the camera nicely.", "신부에게 카메라를 보고 예쁘게 웃으며 손을 흔들어달라고 부탁합시다.", "wrong_konglish", "수백억 비공개 결혼식의 보안 요구를 짓밟고 고객을 모욕하는 처신입니다.")
                ]
            },
            {
                "dialogue": "Drones scrambled and forced down! But the groom's brother has been locked out of the penthouse elevator by Secret Service. The wedding march plays in two minutes!",
                "korean": "드론 전파를 교란해 강제 착륙시켰네! 하지만 신랑의 형이 비밀경호국에 의해 펜트하우스 엘리베이터에서 차단당했어. 결혼 행진곡이 2분 뒤에 울리네!",
                "hint": "경호팀과의 즉각적인 생체 신원 확인과 전용 VIP 서비스 통로로 지체 없이 안내한다.",
                "choices": [
                    ("Escort him through the private service freight elevator using master biometric override and present him directly to the altar.", "마스터 생체인식 오버라이드로 전용 서비스 화물 엘리베이터를 가동해 그를 제단 앞으로 직접 에스코트하십시오.", "native_killer", "호텔 내부 동선과 마스터 권한을 완벽히 장악한 특급 호텔 지배인의 기민한 대처입니다."),
                    ("Tell him to take the stairs up ninety floors by foot.", "90층 계단을 걸어서 뛰어 올라오라고 지시합시다.", "wrong_konglish", "하객을 탈진시키고 결혼식을 파탄 내는 무책임한 발언입니다."),
                    ("Tell the band to play a song for thirty minutes to wait.", "밴드에게 30분 동안 아무 노래나 연주하며 기다리라고 합시다.", "mediocre", "국빈급 결혼식의 엄격한 의전 스케줄을 망쳐버리는 안이한 지연입니다.")
                ]
            },
            {
                "dialogue": "The vows were spoken without a single flashbulb leaking. The Ambassador personally thanked us for preserving royal dignity under pressure. Exemplary service, colleague.",
                "korean": "단 한 컷의 플래시 유출도 없이 결혼 서약이 완결되었네. 대사관 측에서 위기 속에서도 왕실의 품위를 지켜준 데 대해 친히 감사를 표했어. 모범적인 서비스였네, 동료여.",
                "hint": "완벽한 프라이버시 방어를 완수한 5성급 호텔리어의 품격 있는 응답.",
                "choices": [
                    ("Discretion is our greatest luxury. Let us ensure the midnight banquet exceeds every royal expectation.", "신중한 기밀 유지는 우리 호텔의 가장 위대한 사치입니다. 자정 만찬이 왕실의 모든 기대를 뛰어넘도록 완벽히 준비하겠습니다.", "native_killer", "'Discretion is our greatest luxury'는 럭셔리 호스피탈리티의 진수를 보여주는 명대사입니다."),
                    ("I am going to eat the wedding cake now because it looks tasty.", "웨딩케이크가 맛있어 보이니 저나 먹으러 가겠습니다.", "wrong_konglish", "고객의 축하연 음식을 탐내는 프로 의식 없는 천박한 행동입니다."),
                    ("Thank you Monsieur Dupont, weddings are very chaotic.", "감사합니다 뒤퐁 지배인님, 결혼식은 참 정신이 없네요.", "mediocre", "격조 높은 호텔리어의 전문성이 결여된 평이한 한탄입니다.")
                ]
            }
        ],
        "key_expr": "Directional jammer / Discretion is luxury",
        "key_note": "'Directional jammer'는 특정 방향의 무선 전파를 무력화하는 보안 장비, 'Discretion'은 사생활 보호와 신중함을 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 39: Fine Art Auction (8천만 불 모네 수련 위작 의혹)
    # -------------------------------------------------------------
    {
        "ep_num": 39,
        "title": "소더비 경매장: 8천만 불 모네 수련 위작 의혹 감정",
        "genre": "Fine Art Auction",
        "speaker": "Julian Vance (Chief Art Conservator & Auctioneer)",
        "emoji": "🎨",
        "synopsis": "소더비 뉴욕 본사 비밀 복원 연구실. 오늘 저녁 이브닝 세일의 하이라이트인 클로드 모네의 8천만 달러짜리 '수련'에 대해, 프랑스 미술사가가 자외선 안료 위작 의혹을 제기하며 경매 취소를 요구한다.",
        "turns": [
            {
                "dialogue": "A whistleblower art historian claims the Prussian blue pigment on the lilies contains synthetic polymers invented in the 1950s. The auction opens in twenty minutes. Do we withdraw the lot?",
                "korean": "내부 고발 미술사가가 수련에 쓰인 프러시안 블루 안료에 1950년대 발명된 합성 폴리머가 포함되어 있다고 주장해. 경매는 20분 뒤에 시작하네. 출품을 철회해야 할까?",
                "hint": "단순 안료 검사를 넘어 복원 이력(Conservation restoration layer)인지 원본 캔버스인지 분광 분석으로 즉각 판별한다.",
                "choices": [
                    ("Do not cancel. Run high-resolution Raman spectroscopy on the sub-surface canvas layer to prove the synthetic polymer is merely a 1960s conservation varnish.", "취소하지 마십시오. 캔버스 하부층에 고해상도 라만 분광 분석을 실시해 합성 폴리머가 1960년대 복원 바니시 레이어일 뿐임을 과학적으로 입증하십시오.", "native_killer", "'Raman spectroscopy'와 'conservation varnish'는 세계 최고 미술품 감정사들의 결정적 과학 감정 용어입니다."),
                    ("Burn the painting so nobody can know if it was real or fake.", "진짜인지 가짜인지 아무도 모르게 그림을 태워버립시다.", "wrong_konglish", "인류의 위대한 문화유산을 파괴하고 즉각 교도소로 향하는 광기 어린 발언입니다."),
                    ("Tell the buyers we will give them a half-price discount.", "구매자들에게 반값으로 깎아줄 테니 그냥 사 가라고 말합시다.", "wrong_konglish", "위작 의혹을 인정하고 경매소의 200년 신뢰를 파탄 내는 최악의 대응입니다.")
                ]
            },
            {
                "dialogue": "Spectroscopy confirms: 1914 lead-white base with 1962 documented varnish! But the press leaked the rumor to the saleroom floor. Bidders are terrified of bidding. How do you restore confidence from the podium?",
                "korean": "분광 분석 결과 확인: 1962년 공인된 바니시 아래 1914년 연백 베이스 원본 맞음! 하지만 언론이 객석에 소문을 흘렸어. 입찰자들이 공포에 질려 있어. 단상에서 어떻게 신뢰를 되살릴 텐가?",
                "hint": "세계 최고 권위 연구소의 공인 리포트와 무제한 진품 환불 보증을 단상에서 단호히 선언한다.",
                "choices": [
                    ("Step to the podium with the spectrometer analysis, read the museum provenance, and offer an unconditional twenty-year house guarantee on authenticity.", "분광 분석 리포트를 들고 단상에 서서 미술관 출처 이력을 낭독하고, 경매소 이름으로 20년 무조건 진품 보증을 선언하십시오.", "native_killer", "소더비 수석 경매사의 절대적 권위와 책임감으로 객석의 공포를 단숨에 잠재우는 명대사입니다."),
                    ("Cry loudly and tell the room that rich people are too suspicious.", "소리 내어 울면서 부자들은 의심이 너무 많다고 객석을 비난합시다.", "wrong_konglish", "경매장을 난장판으로 만들고 경매사 자격을 박탈당할 수치스러운 행동입니다."),
                    ("Whisper to the front row that it might be fake after all.", "앞줄 관객에게 진짜 가짜일지도 모른다고 귓속말합시다.", "mediocre", "루머를 스스로 확산시켜 입찰을 전면 중단시키는 자폭 행위입니다.")
                ]
            },
            {
                "dialogue": "Bidding exploded to eighty-six million! Hammer slammed down to applause! You saved the integrity of our auction house with science and iron nerve.",
                "korean": "호가가 8천 6백만 달러까지 폭발했어! 박수갈채 속에 낙찰봉이 내려쳤네! 자네가 과학과 강철 같은 담력으로 우리 경매소의 진실성을 지켜냈어.",
                "hint": "역사적 명작의 진실을 수호하고 경매를 대성공으로 이끈 감격을 나눈다.",
                "choices": [
                    ("True art withstands scrutiny, Julian. Pack the masterpiece into the climatic crate and escort the wire transfer.", "진정한 예술은 철저한 검증을 견뎌내는 법입니다, 줄리언. 걸작을 항온항습 상자에 포장하고 대금 송금 절차를 진행하십시오.", "native_killer", "'True art withstands scrutiny'는 명화의 영원성과 감정사의 자부심을 기리는 격조 높은 명언입니다."),
                    ("Now I can brag to my friends that I touched a Monet!", "이제 친구들한테 내가 모네 그림 만져봤다고 자랑해야지!", "wrong_konglish", "위대한 감정 승리 직후 유치한 사적 자랑으로 격을 떨어뜨립니다."),
                    ("Thank you Julian, art history is very stressful.", "감사합니다 줄리언, 미술사는 참 스트레스가 심하네요.", "mediocre", "경매 신기록의 감동에 어울리지 않는 평범한 소감입니다.")
                ]
            }
        ],
        "key_expr": "Raman spectroscopy / Withstand scrutiny",
        "key_note": "'Raman spectroscopy'는 비파괴 레이저 분광 안료 분석법, 'Withstand scrutiny'는 엄밀한 조사를 견뎌내다를 뜻합니다."
    },
    # -------------------------------------------------------------
    # EP 40: Investigative Journalism (파나마 페이퍼스 거대 탈세 폭로)
    # -------------------------------------------------------------
    {
        "ep_num": 40,
        "title": "파나마 페이퍼스: 거대 페이퍼 컴퍼니 탈세 폭로",
        "genre": "Investigative Journalism",
        "speaker": "Ben Bradlee (Executive Investigative Editor)",
        "emoji": "📰",
        "synopsis": "워싱턴 포스트 탐사보도 특별취재팀 벙커. 1,100만 건의 역외 탈세 비밀 계좌 파일 분석 완료 2시간 전, 거대 다국적 은행의 법무팀이 수천억 소송 협박 서한을 들고 편집국장을 찾아온다.",
        "turns": [
            {
                "dialogue": "The mega-bank's white-shoe law firm is threatening a two-hundred-million-dollar libel suit and an emergency court injunction if we name their offshore tax shells tomorrow morning. Do we hold the print presses?",
                "korean": "거대 은행의 일류 로펌이 내일 아침 그들의 역외 페이퍼컴퍼니 실명을 공개하면 2억 달러 명예훼손 소송과 긴급 법원 가처분 신청을 내겠다고 협박해. 인쇄기를 멈춰야 할까?",
                "hint": "위협에 굴복하지 않고 엄격한 팩트체크와 공익 보도의 원칙을 고수하며 정면 출판을 지시한다.",
                "choices": [
                    ("Do not hold a single press. Every wire transfer has three-way cryptographic verification. We print on page one and let the public judge.", "인쇄기를 단 1초도 멈추지 마십시오. 모든 송금 내역은 3자 암호학적 교차 검증을 마쳤습니다. 1면에 대서특필하고 여론의 심판을 받게 하십시오.", "native_killer", "'Spotlight'와 'The Post' 속 전설적인 탐사보도 편집국의 불굴의 저널리즘 정신입니다."),
                    ("Delete the bank's name and write about cute animals instead.", "은행 이름을 지우고 대신 귀여운 동물 기사나 씁시다.", "wrong_konglish", "권력의 협박 앞에 진실을 버리고 황색 언론으로 전락하는 부끄러운 굴복입니다."),
                    ("Ask the bank how much money they can pay us to keep quiet.", "은행 측에 조용히 있는 대가로 돈을 얼마나 줄 수 있는지 흥정해봅시다.", "wrong_konglish", "취재를 빌미로 공갈 갈취를 시도하는 중범죄 행위입니다.")
                ]
            },
            {
                "dialogue": "The Attorney General just called my private line asking for a national security delay. How do we respond to the federal government without compromising our source?",
                "korean": "법무장관이 내 직통 전화로 전화해서 국가 안보를 이유로 보도 유예를 요청했어. 취재원을 보호하면서 연방 정부에 어떻게 답해야 할까?",
                "hint": "국가 안보 핑계 뒤에 숨은 부패를 지적하고 헌법상 보장된 언론의 자유를 단호히 설파한다.",
                "choices": [
                    ("Inform the Attorney General that exposing billionaire tax fraud protects national economic security, and that the First Amendment does not negotiate.", "억만장자들의 탈세를 폭로하는 것이야말로 국가 경제 안보를 지키는 길이며, 수정헌법 제1조는 협상의 대상이 아니라고 법무장관에게 통보하십시오.", "native_killer", "국가 권력의 부당한 외압을 헌법적 가치로 단호히 제압하는 최고의 답변입니다."),
                    ("Say yes sir and hand over all our secret USB drives to the FBI.", "네 장관님 하고 모든 비밀 USB 드라이브를 FBI에 넘겨줍시다.", "wrong_konglish", "취재원을 사지로 몰아넣고 언론의 독립성을 팔아넘기는 배신입니다."),
                    ("Tell the Attorney General to call us back next year.", "법무장관에게 내년에 다시 전화 달라고 합시다.", "mediocre", "국가 비상 상황에서 무책임하고 무성의하게 응대하는 태도입니다.")
                ]
            },
            {
                "dialogue": "The papers hit the streets! Senate just launched an emergency inquiry, the bank's stock dropped twenty percent, and three prime ministers are under investigation. Pulitzer gold, reporter.",
                "korean": "신문이 가판대에 깔렸어! 상원이 긴급 청문회를 발의했고 은행 주가는 20% 폭락했으며 총리 3명이 수사 대상에 올랐네. 퓰리처상 감이야, 기자 양반.",
                "hint": "진실의 승리를 확인하고 저널리즘의 사명을 굳건히 다짐한다.",
                "choices": [
                    ("Democracy thrives in the light, Ben. Let us archive the files for the global consortium and follow the money wherever it leads.", "민주주의는 빛 속에서 번영합니다, 벤. 전 세계 탐사보도 컨소시엄을 위해 파일을 아카이빙하고, 돈의 궤적을 끝까지 추적합시다.", "native_killer", "'Democracy Dies in Darkness'와 'Follow the money'를 완벽히 오마주한 위대한 탐사보도의 결말입니다."),
                    ("I am going to buy a champagne bottle and get totally drunk!", "샴페인 한 병 사서 완전 만취할 때까지 마셔야지!", "wrong_konglish", "역사적인 보도 성과 직후 방종을 일삼는 가벼운 태도입니다."),
                    ("Thank you Ben, writing articles gives me eye strain.", "감사합니다 벤, 기사 쓰느라 눈이 너무 침침하네요.", "mediocre", "퓰리처급 보도의 숭고함에 찬물을 끼얹는 사소한 신체적 불평입니다.")
                ]
            }
        ],
        "key_expr": "Democracy thrives in the light / Follow the money",
        "key_note": "'Follow the money'는 워터게이트 사건의 전설적 취재 지침, 'Democracy thrives'는 언론의 자유가 지키는 민주주의 가치를 뜻합니다."
    }
]

print(f"Part 2 Loaded {len(EPISODES_21_TO_40)} curated episodes (EP 21 to 40).")
