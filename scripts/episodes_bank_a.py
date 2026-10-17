# -*- coding: utf-8 -*-
"""
Dramactor Scenario Bank A - Genres 1 to 25 (100 episodes total: 25 genres x 4 cycles)
"""

def get_episodes_bank_a():
    bank = {}

    # Helper function to generate clean 3-turn episodes
    def ep(title, speaker, emoji, synopsis, key_expr, key_note, turns):
        return {
            "title": title,
            "speaker": speaker,
            "emoji": emoji,
            "synopsis": synopsis,
            "key_expr": key_expr,
            "key_note": key_note,
            "turns": turns
        }

    # 1. Legal Drama
    bank["Legal Drama"] = [
        ep(
            "비밀 유지 합의(NDA) 파기: 특허 분쟁 10억 달러의 전야",
            "Harvey Specter (Managing Partner)", "👔",
            "상대 로펌이 고객사의 비밀 유지 합의를 파기하고 긴급 가처분 신청을 제기했다. 하비 스펙터와 함께 10억 달러 규모의 반격을 개시해야 한다.",
            "file a motion to dismiss with prejudice",
            "소송을 영구 기각(재제소 금지)해달라고 법원에 강력히 요청할 때 쓰는 정통 법정 표현입니다.",
            [
                {
                    "dialogue": "Opposing counsel just served us with an emergency injunction. If we blink, our client loses exclusive patent rights. What's our immediate countermove?",
                    "korean": "상대측 변호인단이 방금 긴급 가처분 신청서를 송달했어. 우리가 주춤하는 순간 우리 의뢰인은 독점 특허권을 잃게 돼. 즉각적인 반격 카드가 뭐야?",
                    "hint": "기각 신청을 제기해 상대의 기선을 완전히 제압하겠다고 하비에게 단호하게 답하세요.",
                    "choices": [
                        ("We file a motion to dismiss with prejudice and hit them with a retaliatory countersuit.", "소송 영구 기각 신청을 내고 보복성 맞소송으로 타격을 입히겠습니다.", "native_killer", "‘motion to dismiss with prejudice’는 법정 드라마에서 상대의 기선을 꺾는 결정적 법률 용어입니다."),
                        ("I will write a letter to the judge asking to cancel their petition.", "판사에게 편지를 써서 그들의 신청을 취소해달라고 요청하겠습니다.", "mediocre", "문법적으로 의미는 통하지만 로펌 파트너에게 보고하기에는 전문성이 결여된 표현입니다."),
                        ("Let's claim the opposition party for their bad behavior.", "상대방의 나쁜 행동에 대해 클레임을 제기합시다.", "wrong_konglish", "‘claim’은 권리 주장이나 보험금 청구이며, 법적 소송은 ‘sue’ 또는 ‘file a countersuit’을 씁니다.")
                    ]
                },
                {
                    "dialogue": "Judge Hall doesn't grant motions lightly. Tanner has three former executives willing to sign affidavits against us. How do you neutralize their testimony?",
                    "korean": "홀 판사는 기각 신청을 쉽게 받아들이지 않아. 태너는 우리에게 불리한 진술서에 서명하겠다는 전직 임원 세 명을 확보했어. 그들의 증언을 어떻게 무력화할 거지?",
                    "hint": "그들의 진술이 증거 능력이 없는 전문 증거(hearsay)임을 지적해 탄핵하겠다고 답하세요.",
                    "choices": [
                        ("We impeach their credibility on cross-examination and strike their affidavits as inadmissible hearsay.", "반대신문에서 증인들의 신빙성을 탄핵하고, 전문 증거로서 진술서의 증거 능력을 배제시키겠습니다.", "native_killer", "‘impeach their credibility’와 ‘inadmissible hearsay’는 미국 법정 공방의 꽃인 핵심 증거법 용어입니다."),
                        ("I will ask them many difficult questions so they cannot answer properly.", "그들에게 어려운 질문을 많이 던져서 제대로 대답하지 못하게 만들겠습니다.", "mediocre", "의도는 전달되지만 어소 변호사다운 세련된 법정 어휘가 부족합니다."),
                        ("We can find their cunning background and tell the judge.", "그들의 커닝한 과거를 찾아서 판사에게 말할 수 있습니다.", "wrong_konglish", "‘cunning’은 한국식으로 부정행위를 뜻할 때 잘못 쓰이지만, 원어민에게는 ‘교활한’ 뜻의 형용사입니다.")
                    ]
                },
                {
                    "dialogue": "They're offering a twenty-million settlement if we sign before noon. Pearson wants to settle. Do we take the deal or go for blood?",
                    "korean": "정오 전에 서명하면 2천만 달러에 합의하겠다고 제안해왔어. 피어슨 대표는 합의를 원해. 합의안을 받을까, 아니면 끝까지 밀어붙일까?",
                    "hint": "합의는 협상 불가이며 배심원 재판에서 완승을 거두겠다고 확신에 찬 어조로 답하세요.",
                    "choices": [
                        ("That offer is an insult. We have them backed into a corner—let's take this to a jury verdict.", "그 제안은 모욕입니다. 상대를 궁지에 몰아넣었으니 배심원 평결까지 가서 끝장을 보시죠.", "native_killer", "‘backed into a corner’와 ‘take this to a jury verdict’는 승세를 확신할 때 쓰는 강력한 미드 단골 표현입니다."),
                        ("I think twenty million is okay, but maybe we can ask for a little more.", "2천만 달러도 괜찮지만, 조금 더 달라고 요구해볼 수도 있을 것 같습니다.", "mediocre", "자신감이 부족하고 우유부단하게 들립니다."),
                        ("Please tell Pearson we should sign the contract for Dutch pay.", "피어슨에게 더치페이로 계약서에 사인하자고 전해주세요.", "wrong_konglish", "‘Dutch pay’는 콩글리시이며, 비용 분담은 ‘split the cost’나 ‘settlement division’이라고 합니다.")
                    ]
                }
            ]
        ),
        ep(
            "대배심 증인 출석: 연방 검찰의 함정 수사 돌파",
            "Harvey Specter (Managing Partner)", "👔",
            "연방 검찰이 기습 소환장을 발부해 우리 의뢰인을 대배심 증언대에 세우려 한다. 위증죄의 덫을 피하고 수사를 종결시켜야 한다.",
            "invoke Fifth Amendment privilege",
            "묵비권(수정헌법 제5조)을 전략적으로 행사하면서도 배심원에게 결백을 각인시킬 때 쓰는 표현입니다.",
            [
                {
                    "dialogue": "The US Attorney subpoenaed our CFO for tomorrow's grand jury. If he misspoke even one syllable, it's a perjury trap. What's the protocol?",
                    "korean": "연방 검사가 내일 대배심에 우리 CFO를 소환했어. 한 음절이라도 말실수를 하면 바로 위증죄의 덫에 걸려. 대응 지침이 뭐야?",
                    "hint": "수정헌법 제5조 묵비권을 행사하되 객관적 회계 감사가 말하도록 하자고 답하세요.",
                    "choices": [
                        ("We invoke his Fifth Amendment privilege and let the forensic audit trail speak for itself.", "수정헌법 제5조 묵비권을 행사하고, 회계 감사의 객관적 증거 기록이 스스로 증명하게 만듭니다.", "native_killer", "‘invoke the Fifth’와 ‘speak for itself’는 연방 수사 방어의 교과서적인 킬러 표현입니다."),
                        ("Tell the CFO to stay quiet and not say anything to the prosecutor.", "CFO에게 조용히 있고 검사에게 아무 말도 하지 말라고 전달하겠습니다.", "mediocre", "직설적이지만 전략적 깊이와 전문 법률 용어가 부재합니다."),
                        ("We must tell the police that our CFO has a high spec and good personality.", "우리 CFO는 스펙이 높고 인성이 좋다고 경찰에게 말해야 합니다.", "wrong_konglish", "‘spec’은 취업 스펙을 뜻하는 콩글리시이며, 연방 검찰은 ‘prosecutors’입니다.")
                    ]
                },
                {
                    "dialogue": "The prosecutor leaked grand jury leaks to the Wall Street Journal. Our client's stock dropped eight percent in pre-market trading.",
                    "korean": "검사가 대배심 내용을 월스트리트 저널에 고의로 유출했어. 우리 의뢰인 주가가 개장 전 거래에서 8%나 폭락했어.",
                    "hint": "검사의 직무유기 징계 청구와 즉각 보도 금지 명령을 신청하자고 하세요.",
                    "choices": [
                        ("We file for prosecutorial misconduct sanctions and demand an immediate gag order.", "검사의 직무유기 및 기밀 누설에 대한 징계 청구와 함께 즉각적인 보도 금지 명령을 신청하겠습니다.", "native_killer", "‘prosecutorial misconduct’와 ‘gag order’는 언론 플레이에 맞서는 최고 수준의 법률 반격 카드입니다."),
                        ("We should write a protest to the newspaper editor immediately.", "신문사 편집장에게 즉시 항의 서한을 써야 합니다.", "mediocre", "효과가 미미하고 사건의 핵심 법적 쟁점을 비켜나간 대응입니다."),
                        ("Let's send an SNS post to clear our company's image.", "우리 회사 이미지를 쇄신하기 위해 SNS 게시물을 올립시다.", "wrong_konglish", "‘SNS’는 콩글리시이며 원어민은 ‘social media’라고 표현합니다.")
                    ]
                },
                {
                    "dialogue": "They're offering immunity if our client implicates the board chairman. One signature, and our CFO walks free.",
                    "korean": "우리 의뢰인이 이사회 의장을 지목하면 면책권을 주겠다고 제안했어. 서명 하나면 우리 CFO는 자유의 몸이 돼.",
                    "hint": "갈라치기 이간책이라며 단칼에 거절하고 단일 대오로 맞서자고 하세요.",
                    "choices": [
                        ("It's a textbook divide-and-conquer play. We reject the immunity deal and fight as a united front.", "전형적인 갈라치기 이간책입니다. 면책 거래를 단칼에 거절하고 단일 대오로 맞서 싸우겠습니다.", "native_killer", "‘divide-and-conquer’와 ‘united front’는 압박 수사 협상에서 주도권을 뺏기지 않는 강력한 표현입니다."),
                        ("I think it is too dangerous to betray the chairman of the board.", "이사회 의장을 배신하는 것은 너무 위험하다고 생각합니다.", "mediocre", "방어적이고 수동적인 태도로 보입니다."),
                        ("Let's make a meeting with the chairman to discuss after service.", "의장과 미팅을 잡아 애프터 서비스에 대해 논의합시다.", "wrong_konglish", "‘after service’는 콩글리시이며 사후 대책은 ‘follow-up’입니다.")
                    ]
                }
            ]
        ),
        ep(
            "파트너 총회 탄핵 표결: 하비 스펙터의 왕좌 방어",
            "Harvey Specter (Managing Partner)", "👔",
            "라이벌 파트너들이 하비의 독단적인 의사결정을 구실로 매니징 파트너 해임안을 상정했다. 파트너십 지분을 지키고 반란을 진압해야 한다.",
            "quash the mutiny before the opening gavel",
            "회의가 시작되기도 전에 반란이나 불리한 표결을 사전 차단할 때 쓰는 고위급 표현입니다.",
            [
                {
                    "dialogue": "Hardman has rallied twelve senior partners behind closed doors. They have the votes to strip my name off the wall tomorrow morning.",
                    "korean": "하드먼이 밀실에서 시니어 파트너 12명을 포섭했어. 내일 아침 내 이름을 로펌 간판에서 떼어낼 표를 확보했단 말이지.",
                    "hint": "하드먼의 해외 계좌 지출 내역을 테이블에 던져 개회 전 반란을 진압하자고 하세요.",
                    "choices": [
                        ("We drop Hardman's offshore expense accounts on the table and quash this mutiny before the opening gavel.", "하드먼의 해외 차명 계좌 지출 내역을 테이블에 던져두고, 개회 봉이 울리기도 전에 반란을 진압하겠습니다.", "native_killer", "‘quash this mutiny’는 정적의 반란을 제압할 때 카리스마를 폭발시키는 최고급 표현입니다."),
                        ("We should call each partner and ask them to vote for Harvey.", "파트너들에게 일일이 전화해서 하비에게 투표해달라고 부탁해야 합니다.", "mediocre", "애걸하는 듯한 인상을 주어 로펌 내 입지를 약화시킵니다."),
                        ("Please give me the handphone number of the bad partners.", "그 나쁜 파트너들의 핸드폰 번호를 제게 알려주세요.", "wrong_konglish", "‘handphone’은 콩글리시이며 ‘cell phone’ 또는 ‘mobile phone’이 맞습니다.")
                    ]
                },
                {
                    "dialogue": "Jessica Pearson is on the fence. She won't back me unless she knows we won't trigger a client exodus. How do you assure her?",
                    "korean": "제시카 피어슨이 중립을 지키고 있어. 주요 고객들의 연쇄 이탈이 없을 거라는 확신이 없으면 날 지지하지 않을 거야. 어떻게 설득할 거지?",
                    "hint": "톱 3 고객사로부터 잔류 확약서를 확보했음을 알리세요.",
                    "choices": [
                        ("I already secured retention letters from our top three Fortune 500 accounts. Her equity is ironclad.", "이미 톱3 포춘 500 고객사들로부터 잔류 확약서를 확보했습니다. 대표님의 지분 가치는 확고부동합니다.", "native_killer", "‘retention letters’와 ‘ironclad’는 비즈니스와 파트너십을 안심시키는 결정적 신뢰 표현입니다."),
                        ("I told the clients to stay with us and they said they might do so.", "고객들에게 우리와 계속 가자고 말했고 그들도 그럴 수도 있다고 했습니다.", "mediocre", "확신이 없고 불확실한 전달 방식입니다."),
                        ("Our clients like our skinship, so they will never go away.", "우리 고객들은 우리의 스킨십을 좋아해서 절대 떠나지 않을 것입니다.", "wrong_konglish", "‘skinship’은 콩글리시이며 깊은 유대 관계는 ‘rapport’를 씁니다.")
                    ]
                },
                {
                    "dialogue": "The vote passed. We won by two ballots. But Hardman won't go quietly. He's taking the real estate department with him.",
                    "korean": "표결을 통과했어. 2표 차이로 이겼지. 하지만 하드먼이 조용히 물러날 리 없어. 부동산 팀 전체를 데리고 나가려 해.",
                    "hint": "경업 금지 조항을 즉각 집행하고 고객 계좌 접근을 전부 동결시키자고 하세요.",
                    "choices": [
                        ("Enforce the non-compete clause immediately and freeze his client accounts before he steps off the elevator.", "경업 금지 조항을 즉각 집행하고, 그가 엘리베이터에서 내리기 전에 고객 계좌 접근을 전부 동결시키겠습니다.", "native_killer", "‘enforce the non-compete’와 ‘freeze accounts’는 분열 위기를 즉시 차단하는 프로페셔널한 조치입니다."),
                        ("We will tell the real estate team not to follow Hardman.", "부동산 팀 변호사들에게 하드먼을 따라가지 말라고 타이르겠습니다.", "mediocre", "순진하고 법적 강제력이 없는 대처 방식입니다."),
                        ("Let's give them a one-plus-one salary bonus so they stay.", "그들이 남도록 원플러스원 연봉 보너스를 줍시다.", "wrong_konglish", "‘one-plus-one’은 마트 행사 콩글리시이며 보너스는 ‘retention package’입니다.")
                    ]
                }
            ]
        ),
        ep(
            "연방 대법원 랜드마크 판결: 15분의 공개 구두 변론",
            "Harvey Specter (Managing Partner)", "👔",
            "미국 전역의 기업 비밀과 내부고발자 보호법을 뒤바꿀 역사적 연방 대법원 구두 변론의 날. 9인의 대법관 앞에서 법리의 정점을 증명해야 한다.",
            "stand on the bedrock of constitutional jurisprudence",
            "헌법적 법리와 정의의 근간에 확고히 서서 논리를 펼칠 때 쓰는 격조 높은 법정 표현입니다.",
            [
                {
                    "dialogue": "You have precisely fifteen minutes at the podium before the Chief Justice cuts your microphone. What is your opening hook?",
                    "korean": "대법원장이 마이크를 끄기 전까지 연단에서 당신에게 주어진 시간은 정확히 15분이야. 대법관들의 귀를 사로잡을 오프닝 훅이 뭐야?",
                    "hint": "본 사건은 단순 기업의 탐욕이 아닌 헌법적 자유의 반석 위에 서 있다고 선언하세요.",
                    "choices": [
                        ("Mr. Chief Justice, this case does not rest on corporate greed—it stands on the bedrock of constitutional liberty.", "존경하는 대법원장님, 본 사건은 단순한 기업의 탐욕이 아니라 헌법적 자유의 반석 위에 서 있는 문제입니다.", "native_killer", "‘stands on the bedrock of...’는 연방 대법원 공개 변론의 품격을 극대화하는 명문장입니다."),
                        ("Good morning judges, today I want to explain why our company is right.", "판사님들 좋은 아침입니다, 오늘 우리 회사가 왜 옳은지 설명해 드리고 싶습니다.", "mediocre", "대법원 호칭 예절이 결여된 캐주얼한 표현입니다."),
                        ("Hello sirs, I prepared a nice ment for this meeting today.", "안녕하십니까 나리들, 오늘 이 미팅을 위해 좋은 멘트를 준비해왔습니다.", "wrong_konglish", "‘ment’는 콩글리시이며 개회 진술은 ‘opening statement’입니다.")
                    ]
                },
                {
                    "dialogue": "Justice Scalia's successor is leaning forward. She asks how our interpretation prevents rogue whistleblowers from stealing trade secrets. Answer her.",
                    "korean": "스칼리아 후임 대법관이 몸을 앞으로 기울였어. 우리의 해석이 어떻게 악성 내부고발자의 기업 비밀 절도를 방지할 수 있는지 묻고 있어. 답변해.",
                    "hint": "형사적 불법 폭로는 보호하되 원천 코드는 침해될 수 없다는 명확한 기준을 제시하세요.",
                    "choices": [
                        ("We draw a bright-line rule: disclosures of criminal illegality are protected, but proprietary source code remains inviolable.", "우리는 명확한 사법적 기준선을 제시합니다. 형사적 불법 행위 폭로는 보호받되, 독점 원천 코드는 침해될 수 없습니다.", "native_killer", "‘bright-line rule’과 ‘remains inviolable’은 대법원 판례를 관통하는 명확하고 강력한 법률 표현입니다."),
                        ("We will make sure bad people are punished and good people are safe.", "나쁜 사람들은 처벌받고 착한 사람들은 안전하도록 확실히 하겠습니다.", "mediocre", "초등학생 수준의 단순한 논리로 대법관의 지적 기준에 미치지 못합니다."),
                        ("Do not worry, we have a strong morning call system to monitor them.", "걱정 마세요, 그들을 감시하는 강력한 모닝콜 시스템이 있습니다.", "wrong_konglish", "‘morning call’은 콩글리시(wake-up call)이며 감시는 ‘oversight’입니다.")
                    ]
                },
                {
                    "dialogue": "The gavel fell. The Chief Justice just announced a unanimous 9-0 opinion in our favor. You just rewrote American corporate law.",
                    "korean": "봉이 울렸어. 대법원장이 만장일치 9대 0으로 우리 승소 판결을 선고했어. 자네가 방금 미국 기업법의 역사를 새로 쓴 거야.",
                    "hint": "단순한 승리를 넘어 다음 100년을 이끌 판례를 세웠다고 화답하세요.",
                    "choices": [
                        ("We didn't just win a case today, Harvey—we set a binding precedent for the next century.", "오늘 우리는 단순한 소송에서 이긴 것이 아닙니다, 하비. 다음 100년을 이끌 구속력 있는 판례를 세운 겁니다.", "native_killer", "‘set a binding precedent’는 법조인 생애 최고의 영예를 축하하는 완벽한 피날레 대사입니다."),
                        ("I am very happy that the result was good and we got high scores.", "결과가 좋고 높은 점수를 받아서 매우 기쁩니다.", "mediocre", "대법원 승소의 무게감에 어울리지 않는 가벼운 소감입니다."),
                        ("Let's go drink beer and do Dutch pay to celebrate our win.", "맥주 마시러 가서 더치페이로 승리를 축하합시다.", "wrong_konglish", "‘Dutch pay’는 콩글리시이며, ‘The drinks are on me’가 자연스럽습니다.")
                    ]
                }
            ]
        )
    ]

    return bank
