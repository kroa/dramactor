# -*- coding: utf-8 -*-
"""
Dramactor Scenario Group 1 (Genres 0 to 4: 5 genres x 4 cycles = 20 episodes)
- Legal Drama
- Silicon Valley Startup
- Corporate Empire & M&A
- Emergency Medicine
- Manhattan Romance & High Society
"""
from helper import make_episode, make_turn

def get_group1_scenarios():
    data = {}

    # -------------------------------------------------------------
    # 0. Legal Drama
    # -------------------------------------------------------------
    data["Legal Drama"] = [
        make_episode(
            "비밀 유지 합의(NDA) 파기: 특허 분쟁 10억 달러의 전야",
            "Harvey Specter (Managing Partner)", "👔",
            "상대 로펌이 고객사의 비밀 유지 합의를 파기하고 긴급 가처분 신청을 제기했다. 하비 스펙터와 함께 10억 달러 규모의 반격을 개시해야 한다.",
            "file a motion to dismiss with prejudice",
            "소송을 영구 기각(재제소 금지)해달라고 법원에 강력히 요청할 때 쓰는 정통 법정 표현입니다.",
            [
                make_turn(
                    "Opposing counsel just served us with an emergency injunction. If we blink, our client loses exclusive patent rights. What's our immediate countermove?",
                    "상대측 변호인단이 방금 긴급 가처분 신청서를 송달했어. 우리가 주춤하는 순간 우리 의뢰인은 독점 특허권을 잃게 돼. 즉각적인 반격 카드가 뭐야?",
                    "기각 신청을 제기해 상대의 기선을 완전히 제압하겠다고 하비에게 단호하게 답하세요.",
                    ("We file a motion to dismiss with prejudice and hit them with a retaliatory countersuit.", "소송 영구 기각 신청을 내고 보복성 맞소송으로 타격을 입히겠습니다.", "‘motion to dismiss with prejudice’는 법정 드라마에서 상대의 기선을 꺾는 결정적 법률 용어입니다."),
                    ("I will write a letter to the judge asking to cancel their petition.", "판사에게 편지를 써서 그들의 신청을 취소해달라고 요청하겠습니다.", "문법적으로 의미는 통하지만 로펌 파트너에게 보고하기에는 전문성이 결여된 표현입니다."),
                    ("Let's claim the opposition party for their bad behavior.", "상대방의 나쁜 행동에 대해 클레임을 제기합시다.", "‘claim’은 권리 주장이나 보험금 청구이며, 법적 소송은 ‘sue’ 또는 ‘file a countersuit’을 씁니다.")
                ),
                make_turn(
                    "Judge Hall doesn't grant motions lightly. Tanner has three former executives willing to sign affidavits against us. How do you neutralize their testimony?",
                    "홀 판사는 기각 신청을 쉽게 받아들이지 않아. 태너는 우리에게 불리한 진술서에 서명하겠다는 전직 임원 세 명을 확보했어. 그들의 증언을 어떻게 무력화할 거지?",
                    "그들의 진술이 증거 능력이 없는 전문 증거(hearsay)임을 지적해 탄핵하겠다고 답하세요.",
                    ("We impeach their credibility on cross-examination and strike their affidavits as inadmissible hearsay.", "반대신문에서 증인들의 신빙성을 탄핵하고, 전문 증거로서 진술서의 증거 능력을 배제시키겠습니다.", "‘impeach their credibility’와 ‘inadmissible hearsay’는 미국 법정 공방의 꽃인 핵심 증거법 용어입니다."),
                    ("I will ask them many difficult questions so they cannot answer properly.", "그들에게 어려운 질문을 많이 던져서 제대로 대답하지 못하게 만들겠습니다.", "의도는 전달되지만 어소 변호사다운 세련된 법정 어휘가 부족합니다."),
                    ("We can find their cunning background and tell the judge.", "그들의 커닝한 과거를 찾아서 판사에게 말할 수 있습니다.", "‘cunning’은 한국식으로 부정행위를 뜻할 때 잘못 쓰이지만, 원어민에게는 ‘교활한’ 뜻의 형용사입니다.")
                ),
                make_turn(
                    "They're offering a twenty-million settlement if we sign before noon. Pearson wants to settle. Do we take the deal or go for blood?",
                    "정오 전에 서명하면 2천만 달러에 합의하겠다고 제안해왔어. 피어슨 대표는 합의를 원해. 합의안을 받을까, 아니면 끝까지 밀어붙일까?",
                    "합의는 협상 불가이며 배심원 재판에서 완승을 거두겠다고 확신에 찬 어조로 답하세요.",
                    ("That offer is an insult. We have them backed into a corner—let's take this to a jury verdict.", "그 제안은 모욕입니다. 상대를 궁지에 몰아넣었으니 배심원 평결까지 가서 끝장을 보시죠.", "‘backed into a corner’와 ‘take this to a jury verdict’는 승세를 확신할 때 쓰는 강력한 미드 단골 표현입니다."),
                    ("I think twenty million is okay, but maybe we can ask for a little more.", "2천만 달러도 괜찮지만, 조금 더 달라고 요구해볼 수도 있을 것 같습니다.", "자신감이 부족하고 우유부단하게 들립니다."),
                    ("Please tell Pearson we should sign the contract for Dutch pay.", "피어슨에게 더치페이로 계약서에 사인하자고 전해주세요.", "‘Dutch pay’는 콩글리시이며, 비용 분담은 ‘split the cost’나 ‘settlement division’이라고 합니다.")
                )
            ]
        ),
        make_episode(
            "대배심 증인 출석: 연방 검찰의 함정 수사 돌파",
            "Harvey Specter (Managing Partner)", "👔",
            "연방 검찰이 기습 소환장을 발부해 우리 의뢰인을 대배심 증언대에 세우려 한다. 위증죄의 덫을 피하고 수사를 종결시켜야 한다.",
            "invoke Fifth Amendment privilege",
            "묵비권(수정헌법 제5조)을 전략적으로 행사하면서도 배심원에게 결백을 각인시킬 때 쓰는 표현입니다.",
            [
                make_turn(
                    "The US Attorney subpoenaed our CFO for tomorrow's grand jury. If he misspoke even one syllable, it's a perjury trap. What's the protocol?",
                    "연방 검사가 내일 대배심에 우리 CFO를 소환했어. 한 음절이라도 말실수를 하면 바로 위증죄의 덫에 걸려. 대응 지침이 뭐야?",
                    "수정헌법 제5조 묵비권을 행사하되 객관적 회계 감사가 말하도록 하자고 답하세요.",
                    ("We invoke his Fifth Amendment privilege and let the forensic audit trail speak for itself.", "수정헌법 제5조 묵비권을 행사하고, 회계 감사의 객관적 증거 기록이 스스로 증명하게 만듭니다.", "‘invoke the Fifth’와 ‘speak for itself’는 연방 수사 방어의 교과서적인 킬러 표현입니다."),
                    ("Tell the CFO to stay quiet and not say anything to the prosecutor.", "CFO에게 조용히 있고 검사에게 아무 말도 하지 말라고 전달하겠습니다.", "직설적이지만 전략적 깊이와 전문 법률 용어가 부재합니다."),
                    ("We must tell the police that our CFO has a high spec and good personality.", "우리 CFO는 스펙이 높고 인성이 좋다고 경찰에게 말해야 합니다.", "‘spec’은 취업 스펙을 뜻하는 콩글리시이며, 연방 검찰은 ‘prosecutors’입니다.")
                ),
                make_turn(
                    "The prosecutor leaked grand jury leaks to the Wall Street Journal. Our client's stock dropped eight percent in pre-market trading.",
                    "검사가 대배심 내용을 월스트리트 저널에 고의로 유출했어. 우리 의뢰인 주가가 개장 전 거래에서 8%나 폭락했어.",
                    "검사의 직무유기 징계 청구와 즉각 보도 금지 명령을 신청하자고 하세요.",
                    ("We file for prosecutorial misconduct sanctions and demand an immediate gag order.", "검사의 직무유기 및 기밀 누설에 대한 징계 청구와 함께 즉각적인 보도 금지 명령을 신청하겠습니다.", "‘prosecutorial misconduct’와 ‘gag order’는 언론 플레이에 맞서는 최고 수준의 법률 반격 카드입니다."),
                    ("We should write a protest to the newspaper editor immediately.", "신문사 편집장에게 즉시 항의 서한을 써야 합니다.", "효과가 미미하고 사건의 핵심 법적 쟁점을 비켜나간 대응입니다."),
                    ("Let's send an SNS post to clear our company's image.", "우리 회사 이미지를 쇄신하기 위해 SNS 게시물을 올립시다.", "‘SNS’는 콩글리시이며 원어민은 ‘social media’라고 표현합니다.")
                ),
                make_turn(
                    "They're offering immunity if our client implicates the board chairman. One signature, and our CFO walks free.",
                    "우리 의뢰인이 이사회 의장을 지목하면 면책권을 주겠다고 제안했어. 서명 하나면 우리 CFO는 자유의 몸이 돼.",
                    "갈라치기 이간책이라며 단칼에 거절하고 단일 대오로 맞서자고 하세요.",
                    ("It's a textbook divide-and-conquer play. We reject the immunity deal and fight as a united front.", "전형적인 갈라치기 이간책입니다. 면책 거래를 단칼에 거절하고 단일 대오로 맞서 싸우겠습니다.", "‘divide-and-conquer’와 ‘united front’는 압박 수사 협상에서 주도권을 뺏기지 않는 강력한 표현입니다."),
                    ("I think it is too dangerous to betray the chairman of the board.", "이사회 의장을 배신하는 것은 너무 위험하다고 생각합니다.", "방어적이고 수동적인 태도로 보입니다."),
                    ("Let's make a meeting with the chairman to discuss after service.", "의장과 미팅을 잡아 애프터 서비스에 대해 논의합시다.", "‘after service’는 콩글리시이며 사후 대책은 ‘follow-up’입니다.")
                )
            ]
        ),
        make_episode(
            "파트너 총회 탄핵 표결: 하비 스펙터의 왕좌 방어",
            "Harvey Specter (Managing Partner)", "👔",
            "라이벌 파트너들이 하비의 독단적인 의사결정을 구실로 매니징 파트너 해임안을 상정했다. 파트너십 지분을 지키고 반란을 진압해야 한다.",
            "quash the mutiny before the opening gavel",
            "회의가 시작되기도 전에 반란이나 불리한 표결을 사전 차단할 때 쓰는 고위급 표현입니다.",
            [
                make_turn(
                    "Hardman has rallied twelve senior partners behind closed doors. They have the votes to strip my name off the wall tomorrow morning.",
                    "하드먼이 밀실에서 시니어 파트너 12명을 포섭했어. 내일 아침 내 이름을 로펌 간판에서 떼어낼 표를 확보했단 말이지.",
                    "하드먼의 해외 계좌 지출 내역을 테이블에 던져 개회 전 반란을 진압하자고 하세요.",
                    ("We drop Hardman's offshore expense accounts on the table and quash this mutiny before the opening gavel.", "하드먼의 해외 차명 계좌 지출 내역을 테이블에 던져두고, 개회 봉이 울리기도 전에 반란을 진압하겠습니다.", "‘quash this mutiny’는 정적의 반란을 제압할 때 카리스마를 폭발시키는 최고급 표현입니다."),
                    ("We should call each partner and ask them to vote for Harvey.", "파트너들에게 일일이 전화해서 하비에게 투표해달라고 부탁해야 합니다.", "애걸하는 듯한 인상을 주어 로펌 내 입지를 약화시킵니다."),
                    ("Please give me the handphone number of the bad partners.", "그 나쁜 파트너들의 핸드폰 번호를 제게 알려주세요.", "‘handphone’은 콩글리시이며 ‘cell phone’ 또는 ‘mobile phone’이 맞습니다.")
                ),
                make_turn(
                    "Jessica Pearson is on the fence. She won't back me unless she knows we won't trigger a client exodus. How do you assure her?",
                    "제시카 피어슨이 중립을 지키고 있어. 주요 고객들의 연쇄 이탈이 없을 거라는 확신이 없으면 날 지지하지 않을 거야. 어떻게 설득할 거지?",
                    "톱 3 고객사로부터 잔류 확약서를 확보했음을 알리세요.",
                    ("I already secured retention letters from our top three Fortune 500 accounts. Her equity is ironclad.", "이미 톱3 포춘 500 고객사들로부터 잔류 확약서를 확보했습니다. 대표님의 지분 가치는 확고부동합니다.", "‘retention letters’와 ‘ironclad’는 비즈니스와 파트너십을 안심시키는 결정적 신뢰 표현입니다."),
                    ("I told the clients to stay with us and they said they might do so.", "고객들에게 우리와 계속 가자고 말했고 그들도 그럴 수도 있다고 했습니다.", "확신이 없고 불확실한 전달 방식입니다."),
                    ("Our clients like our skinship, so they will never go away.", "우리 고객들은 우리의 스킨십을 좋아해서 절대 떠나지 않을 것입니다.", "‘skinship’은 콩글리시이며 깊은 유대 관계는 ‘rapport’를 씁니다.")
                ),
                make_turn(
                    "The vote passed. We won by two ballots. But Hardman won't go quietly. He's taking the real estate department with him.",
                    "표결을 통과했어. 2표 차이로 이겼지. 하지만 하드먼이 조용히 물러날 리 없어. 부동산 팀 전체를 데리고 나가려 해.",
                    "경업 금지 조항을 즉각 집행하고 고객 계좌 접근을 전부 동결시키자고 하세요.",
                    ("Enforce the non-compete clause immediately and freeze his client accounts before he steps off the elevator.", "경업 금지 조항을 즉각 집행하고, 그가 엘리베이터에서 내리기 전에 고객 계좌 접근을 전부 동결시키겠습니다.", "‘enforce the non-compete’와 ‘freeze accounts’는 분열 위기를 즉시 차단하는 프로페셔널한 조치입니다."),
                    ("We will tell the real estate team not to follow Hardman.", "부동산 팀 변호사들에게 하드먼을 따라가지 말라고 타이르겠습니다.", "순진하고 법적 강제력이 없는 대처 방식입니다."),
                    ("Let's give them a one-plus-one salary bonus so they stay.", "그들이 남도록 원플러스원 연봉 보너스를 줍시다.", "‘one-plus-one’은 마트 행사 콩글리시이며 보너스는 ‘retention package’입니다.")
                )
            ]
        ),
        make_episode(
            "연방 대법원 랜드마크 판결: 15분의 공개 구두 변론",
            "Harvey Specter (Managing Partner)", "👔",
            "미국 전역의 기업 비밀과 내부고발자 보호법을 뒤바꿀 역사적 연방 대법원 구두 변론의 날. 9인의 대법관 앞에서 법리의 정점을 증명해야 한다.",
            "stand on the bedrock of constitutional jurisprudence",
            "헌법적 법리와 정의의 근간에 확고히 서서 논리를 펼칠 때 쓰는 격조 높은 법정 표현입니다.",
            [
                make_turn(
                    "You have precisely fifteen minutes at the podium before the Chief Justice cuts your microphone. What is your opening hook?",
                    "대법원장이 마이크를 끄기 전까지 연단에서 당신에게 주어진 시간은 정확히 15분이야. 대법관들의 귀를 사로잡을 오프닝 훅이 뭐야?",
                    "본 사건은 단순 기업의 탐욕이 아닌 헌법적 자유의 반석 위에 서 있다고 선언하세요.",
                    ("Mr. Chief Justice, this case does not rest on corporate greed—it stands on the bedrock of constitutional liberty.", "존경하는 대법원장님, 본 사건은 단순한 기업의 탐욕이 아니라 헌법적 자유의 반석 위에 서 있는 문제입니다.", "‘stands on the bedrock of...’는 연방 대법원 공개 변론의 품격을 극대화하는 명문장입니다."),
                    ("Good morning judges, today I want to explain why our company is right.", "판사님들 좋은 아침입니다, 오늘 우리 회사가 왜 옳은지 설명해 드리고 싶습니다.", "대법원 호칭 예절이 결여된 캐주얼한 표현입니다."),
                    ("Hello sirs, I prepared a nice ment for this meeting today.", "안녕하십니까 나리들, 오늘 이 미팅을 위해 좋은 멘트를 준비해왔습니다.", "‘ment’는 콩글리시이며 개회 진술은 ‘opening statement’입니다.")
                ),
                make_turn(
                    "Justice Scalia's successor is leaning forward. She asks how our interpretation prevents rogue whistleblowers from stealing trade secrets. Answer her.",
                    "스칼리아 후임 대법관이 몸을 앞으로 기울였어. 우리의 해석이 어떻게 악성 내부고발자의 기업 비밀 절도를 방지할 수 있는지 묻고 있어. 답변해.",
                    "형사적 불법 폭로는 보호하되 원천 코드는 침해될 수 없다는 명확한 기준을 제시하세요.",
                    ("We draw a bright-line rule: disclosures of criminal illegality are protected, but proprietary source code remains inviolable.", "우리는 명확한 사법적 기준선을 제시합니다. 형사적 불법 행위 폭로는 보호받되, 독점 원천 코드는 침해될 수 없습니다.", "‘bright-line rule’과 ‘remains inviolable’은 대법원 판례를 관통하는 명확하고 강력한 법률 표현입니다."),
                    ("We will make sure bad people are punished and good people are safe.", "나쁜 사람들은 처벌받고 착한 사람들은 안전하도록 확실히 하겠습니다.", "초등학생 수준의 단순한 논리로 대법관의 지적 기준에 미치지 못합니다."),
                    ("Do not worry, we have a strong morning call system to monitor them.", "걱정 마세요, 그들을 감시하는 강력한 모닝콜 시스템이 있습니다.", "‘morning call’은 콩글리시(wake-up call)이며 감시는 ‘oversight’입니다.")
                ),
                make_turn(
                    "The gavel fell. The Chief Justice just announced a unanimous 9-0 opinion in our favor. You just rewrote American corporate law.",
                    "봉이 울렸어. 대법원장이 만장일치 9대 0으로 우리 승소 판결을 선고했어. 자네가 방금 미국 기업법의 역사를 새로 쓴 거야.",
                    "단순한 승리를 넘어 다음 100년을 이끌 판례를 세웠다고 화답하세요.",
                    ("We didn't just win a case today, Harvey—we set a binding precedent for the next century.", "오늘 우리는 단순한 소송에서 이긴 것이 아닙니다, 하비. 다음 100년을 이끌 구속력 있는 판례를 세운 겁니다.", "‘set a binding precedent’는 법조인 생애 최고의 영예를 축하하는 완벽한 피날레 대사입니다."),
                    ("I am very happy that the result was good and we got high scores.", "결과가 좋고 높은 점수를 받아서 매우 기쁩니다.", "대법원 승소의 무게감에 어울리지 않는 가벼운 소감입니다."),
                    ("Let's go drink beer and do Dutch pay to celebrate our win.", "맥주 마시러 가서 더치페이로 승리를 축하합시다.", "‘Dutch pay’는 콩글리시이며, ‘The drinks are on me’가 자연스럽습니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 1. Silicon Valley Startup
    # -------------------------------------------------------------
    data["Silicon Valley Startup"] = [
        make_episode(
            "시리즈 B 텀시트 서명 전야: 청산 우선권(Liquidation Preference) 담판",
            "Alistair Finch (Lead Angel VC)", "🚀",
            "샌드힐 로드 정상급 VC가 5천만 달러 투자 텀시트에 2배수 참가적 청산 우선권(2x Participating Liquidation)을 슬그머니 삽입했다. 창업자 지분을 지켜내야 한다.",
            "non-participating liquidation preference",
            "투자자가 원금만 우선 회수하고 추가 잔여 재산 분배에는 참가하지 못하게 막는 스타트업 표준 방어 조항입니다.",
            [
                make_turn(
                    "Our investment committee is firm on the 2x participating preference. If the market cools down, our downside must be insured. Do you sign or forfeit the round?",
                    "우리 투자심의위원회는 2배수 참가적 우선권 조항을 결코 양보할 수 없습니다. 시장이 식을 경우 손실 방어가 필수입니다. 서명합니까, 아니면 이번 라운드를 포기합니까?",
                    "해당 조항은 협상 불가이며 표준 1배수 비참가적 조건이 아니면 텀시트를 찢겠다고 강경하게 맞서세요.",
                    ("That 2x clause is a non-starter. We accept a clean 1x non-participating preference, or we take Sequoia's competing offer.", "2배수 조항은 협상 불가입니다. 깔끔한 1배수 비참가적 우선권이 아니라면 세쿼이아의 경쟁 오퍼를 수락하겠습니다.", "‘is a non-starter’와 ‘clean 1x non-participating preference’는 실리콘밸리 창업자가 VC를 압도하는 최고급 협상 표현입니다."),
                    ("I think your condition is very hard for us, please reduce it a little bit.", "당신의 조건은 저희에게 너무 힘드니 조금만 깎아주시면 감사하겠습니다.", "애원하는 듯한 태도로 스타트업의 협상력을 급격히 떨어뜨립니다."),
                    ("Please understand our venture condition and cancel the option.", "저희 벤처의 컨디션을 이해해주시고 옵션을 캔슬해주세요.", "‘venture’는 기업명사로 단독 사용이 어색하며, 조건 취소는 ‘waive the clause’를 씁니다.")
                ),
                make_turn(
                    "Sequoia won't give you our enterprise network. What guarantees your annual recurring revenue hits forty million by fourth quarter?",
                    "세쿼이아는 우리만큼의 B2B 엔터프라이즈 네트워크를 제공하지 못합니다. 4분기까지 연간 반복 매출(ARR) 4천만 달러를 달성할 보장이 뭡니까?",
                    "이미 포춘 100대 기업 12개 사와 3년 선결제 계약을 체결해 파이프라인이 꽉 차 있다고 제시하세요.",
                    ("We have twelve Fortune 100 multi-year enterprise contracts locked in escrow. Our net retention rate is sitting at a stellar one hundred forty percent.", "이미 12개 포춘 100 기업과 다년 독점 계약을 에스크로에 묶어두었습니다. 순매출 유지율(NRR)은 140%에 달합니다.", "‘locked in escrow’와 ‘net retention rate’는 SaaS 지표에서 투자자의 입을 다물게 만드는 결정타입니다."),
                    ("We have many meetings with big companies and they really like our app.", "대기업들과 미팅을 많이 했고 그들이 우리 앱을 진짜 좋아합니다.", "막연하고 검증되지 않은 주관적 주장으로 들립니다."),
                    ("Our employees have high spec and we do morning call to work hard.", "우리 직원들은 스펙이 높고 열심히 일하기 위해 모닝콜도 합니다.", "‘spec’과 ‘morning call’은 대표적인 콩글리시로 실리콘밸리 VC에게 비웃음을 삽니다.")
                ),
                make_turn(
                    "Fair enough. We strip the 2x clause. But I want a personal board observer seat with full information rights.",
                    "좋습니다. 2배수 조항은 빼겠습니다. 하지만 전면적인 정보 열람권을 가진 이사회 옵저버 자리를 제게 보장하십시오.",
                    "정보 열람권은 부여하되 기밀 개발 프로젝트는 제외하는 표준 NDA 조건을 달아 승낙하세요.",
                    ("You have your observer seat subject to customary board governance and strict IP firewalls. Let's wire the funds.", "통상적인 이사회 거버넌스 및 엄격한 IP 방화벽 준수를 전제로 옵저버 자리를 승인합니다. 펀딩 송금을 집행하시죠.", "‘customary board governance’와 ‘wire the funds’는 스타트업 딜 클로징의 완벽한 매너입니다."),
                    ("Okay, you can come to our board meeting and listen to everything.", "좋습니다, 우리 이사회 미팅에 오셔서 모든 것을 들으셔도 됩니다.", "비밀 유지와 견제 장치 없이 너무 쉽게 문을 열어주는 표현입니다."),
                    ("Thank you sir, let us do fighting together for our win-win.", "감사합니다 나리, 윈윈을 위해 함께 파이팅합시다.", "‘fighting’은 한국식 응원 콩글리시이며, 협업은 ‘Let's build something great together’입니다.")
                )
            ]
        ),
        make_episode(
            "런웨이 3주 전: 비상 브릿지 론과 브레이크이븐 도약",
            "Alistair Finch (Lead Angel VC)", "🚀",
            "현금 소진율(Burn Rate)이 치솟아 회사 잔고가 3주 치 런웨이만 남았다. 구조조정 없이 브릿지 론을 유치하고 흑자 전환(Breakeven)을 증명해야 한다.",
            "slash the burn rate and extend the runway",
            "비용 소진율을 대폭 삭감하고 회사 생존 기간을 연장할 때 쓰는 스타트업 핵심 생존 용어입니다.",
            [
                make_turn(
                    "Your cash burn is three hundred grand a week. At this rate, payroll bounces on the thirty-first. Why should we bridge your runway?",
                    "주당 현금 소모액이 30만 달러입니다. 이 속도라면 31일에 월급 계좌가 부도납니다. 우리가 왜 당신들의 런웨이에 브릿지 론을 대줘야 합니까?",
                    "유료 마케팅을 전면 제로화하고 오가닉 추천 바이럴로 전환해 이번 달 바로 현금흐름 흑자를 찍겠다고 답하세요.",
                    ("We slashed our paid customer acquisition cost to zero and pivoted entirely to organic product-led growth. We hit cash-flow positive in thirty days.", "유료 마케팅 비용을 즉각 전면 삭감하고 오가닉 제품 주도 성장(PLG)으로 피벗했습니다. 30일 이내에 현금흐름 흑자를 달성합니다.", "‘slashed customer acquisition cost’와 ‘cash-flow positive’는 위기 돌파형 창업자의 최고의 답변입니다."),
                    ("We will ask employees to work for free for one month.", "직원들에게 한 달 동안 무급으로 일해달라고 부탁하겠습니다.", "노동법 위반이자 팀 붕괴를 자초하는 최악의 답변입니다."),
                    ("Let's ask our users to do Dutch pay for our server fee.", "우리 유저들에게 서버비를 더치페이해달라고 요청합시다.", "‘Dutch pay’는 콩글리시이며, 유저 과금은 ‘tier pricing’ 또는 ‘subscription fee’입니다.")
                ),
                make_turn(
                    "Product-led growth takes quarters to compound. If Amazon Web Services shuts down your GPU clusters next Tuesday, the product dies.",
                    "제품 주도 성장은 복리 효과가 나기까지 수 분기가 걸립니다. 다음 주 화요일에 AWS가 GPU 클러스터를 차단하면 제품 자체가 죽습니다.",
                    "AWS와 이미 100만 달러 크레딧 연장 협상을 완료했으며 엔비디아 인큐베이터 파트너십을 맺었다고 밝히세요.",
                    ("We already secured a one-million-dollar emergency compute credit line directly with AWS, fully backed by Nvidia's Inception tier.", "이미 엔비디아 인셉션 프로그램의 보증을 받아 AWS로부터 100만 달러 규모의 비상 연산 크레딧 라인을 확보했습니다.", "‘secured an emergency compute credit line’은 인프라 위기를 단숨에 해소하는 전문적인 대답입니다."),
                    ("I will tell the cloud provider to wait until we get rich.", "클라우드 회사에 우리가 부자가 될 때까지 기다려달라고 말하겠습니다.", "비즈니스 상식에 어긋나는 비현실적인 대응입니다."),
                    ("Our server has good spec so it will not die easily.", "우리 서버는 스펙이 좋아서 쉽게 죽지 않을 것입니다.", "‘spec’은 콩글리시이며 서버 사양은 ‘high-end infrastructure’ 또는 ‘hardware tier’입니다.")
                ),
                make_turn(
                    "You're tougher than you look. I'll wire a three-million SAFE bridge note this afternoon. Don't make me regret this.",
                    "생각보다 훨씬 강단이 있군요. 오늘 오후 3백만 달러 규모의 SAFE 브릿지 투자금을 송금하겠습니다. 내가 후회하게 만들지 마십시오.",
                    "투자 원금의 10배 수익으로 보답하겠다며 흔들림 없는 자신감을 보여주세요.",
                    ("You won't regret a cent. We'll turn this bridge into a tenfold valuation jump before our Series C. Thank you, Alistair.", "단 1센트도 후회하지 않으실 겁니다. 시리즈 C 전에 이 브릿지 투자를 10배의 기업가치 도약으로 되돌려드리겠습니다.", "‘tenfold valuation jump’는 투자자에게 최고의 아드레날린을 선사하는 확신의 클로징입니다."),
                    ("Thank you for the money, I will buy some food for my staff.", "돈 감사합니다, 직원들에게 맛있는 밥을 사주겠습니다.", "투자금의 용도를 오해하는 가벼운 태도로 보입니다."),
                    ("Please give me your handphone number so we can have dinner meeting.", "저녁 미팅을 할 수 있게 당신의 핸드폰 번호를 제게 주십시오.", "‘handphone’은 콩글리시이며 비즈니스 만남은 ‘dinner meeting’ 대신 ‘connect over dinner’가 자연스럽습니다.")
                )
            ]
        ),
        make_episode(
            "빅테크의 제품 카피캣 공격: 지적재산권(IP) 맞소송과 시장 선점",
            "Alistair Finch (Lead Angel VC)", "🚀",
            "구글과 메타가 우리 핵심 기능을 그대로 베낀 무료 제품을 출시했다. 언론 플레이와 법적 대응을 결합해 독점 사용자 기반을 지켜내야 한다.",
            "weaponize our patent portfolio against the tech giants",
            "거대 기업의 복제 위협에 맞서 스타트업의 특허 포트폴리오를 무기화해 역공을 펼칠 때 쓰는 표현입니다.",
            [
                make_turn(
                    "TechCrunch just leaked that Meta is bundling your core spatial audio algorithm for free into their ecosystem. Wall Street thinks you're dead on arrival.",
                    "테크크런치가 메타가 당신의 핵심 공간 음향 알고리즘을 생태계에 무료로 번들링한다는 기사를 유출했습니다. 월가는 당신들이 이제 끝났다고 봅니다.",
                    "대기업의 카피캣은 우리 기술이 차세대 표준임을 증명한 것이며, 원천 특허 침해 소송으로 배상금을 물릴 기회라고 답하세요.",
                    ("Their blatant imitation is the ultimate market validation. We hold four foundational patents on that latency layer—we're taking them to federal court.", "그들의 노골적인 모방은 우리 기술이 시장의 정답임을 증명한 것입니다. 우리는 해당 저지연 레이어에 4개의 원천 특허를 보유하고 있으며, 연방 법원으로 끌고 갈 것입니다.", "‘market validation’과 ‘foundational patents’는 위기를 기회로 치환하는 스타트업 CEO의 최고 화법입니다."),
                    ("I think big companies are very bad and unfair to small companies.", "대기업들은 작고 어린 기업들에게 너무 나쁘고 불공평하다고 생각합니다.", "감정적인 불평에 불과하며 투자자를 안심시키지 못합니다."),
                    ("Let's send an SNS protest claiming their skinship with our code.", "우리 코드와 그들의 스킨십에 대해 클레임하는 SNS 항의를 올립시다.", "‘SNS’, ‘claim’, ‘skinship’이 뒤섞인 최악의 콩글리시 문장입니다.")
                ),
                make_turn(
                    "Meta's legal budget is infinite. They will stall discovery for three years until your legal fund drains dry.",
                    "메타의 법무 예산은 무한합니다. 그들은 당신들의 소송 자금이 바닥날 때까지 증거개시 절차를 3년 동안 질질 끌 것입니다.",
                    "실리콘밸리 톱 티어 소송 펀딩사로부터 승소 조건부 5천만 달러 소송 비용을 전액 유치했다고 반박하세요.",
                    ("We partnered with a top-tier litigation finance fund. They're covering one hundred percent of our legal costs in exchange for a slice of the settlement.", "이미 최상위 소송 금융 펀드와 파트너십을 체결했습니다. 합의금의 일부를 나누는 조건으로 소송 비용 100%를 그들이 전액 부담합니다.", "‘litigation finance fund’는 골리앗 대기업을 상대로 소송 비용 소진을 방지하는 최첨단 방어 카드입니다."),
                    ("We will ask the government to give us free lawyer service.", "정부에 무료 변호사 서비스를 제공해달라고 요청하겠습니다.", "기업 특허 소송의 현실과 동떨어진 순진한 발상입니다."),
                    ("Do not worry, we have good cunning skill to hide our code.", "걱정 마세요, 우리 코드를 숨기는 좋은 커닝 스킬이 있습니다.", "‘cunning’은 콩글리시이며, 보안 기술은 ‘proprietary encryption’입니다.")
                ),
                make_turn(
                    "The press is turning in your favor. The New York Times just ran a front-page op-ed calling you David against Goliath. How do you capitalize on this momentum?",
                    "언론 여론이 완전히 우리 쪽으로 돌아섰습니다. 뉴욕타임스가 골리앗에 맞선 다윗이라며 1면 기고문을 실었습니다. 이 모멘텀을 어떻게 수익화할 겁니까?",
                    "엔터프라이즈 프라이버시 서밋을 개최하고 유럽 정부 기관들과 독점 납품 계약을 체결하겠다고 선언하세요.",
                    ("We launch the 'Sovereign Tech Initiative' today, closing enterprise deals with EU regulators who refuse to be locked into Big Tech's walled garden.", "오늘 ‘자립형 테크 이니셔티브’를 발표하고, 빅테크의 폐쇄적 생태계에 갇히기를 거부하는 EU 규제 기관들과 독점 계약을 체결하겠습니다.", "‘walled garden’과 ‘Sovereign Tech Initiative’는 빅테크의 독점에 맞서 시장을 독점하는 전략적 프레임워크입니다."),
                    ("We will give free coffee coupon to people who share the news.", "뉴스를 공유하는 사람들에게 무료 커피 쿠폰을 나눠주겠습니다.", "스케일업 단계의 글로벌 기업 전략에 걸맞지 않은 소모적인 이벤트입니다."),
                    ("Let's give customers one-plus-one discount after service.", "고객들에게 원플러스원 할인과 애프터 서비스를 제공합시다.", "‘one-plus-one’과 ‘after service’는 전문 SaaS 업계에서 쓰이지 않는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "나스닥 벨 타종: 100억 달러 데카콘(Decacorn)의 탄생",
            "Alistair Finch (Lead Angel VC)", "🚀",
            "창업 5년 만에 타임스퀘어 나스닥 마켓사이트 전광판 앞에 섰다. 시초가 폭등 속에서 전 세계 투자자들을 향해 회사의 백년 비전을 선포해야 한다.",
            "ring the opening bell on a ten-billion-dollar valuation",
            "기업가치 100억 달러의 신화적인 상장일 오프닝 벨을 울릴 때 쓰는 기념비적 표현입니다.",
            [
                make_turn(
                    "The pre-market order book is oversubscribed by forty times. Trading opens in sixty seconds. Look at the Nasdaq tower—that's your face on Times Square.",
                    "장 시작 전 매수 주문 장부가 40배나 초과 청약되었습니다. 60초 뒤 거래가 시작됩니다. 나스닥 타워를 보세요. 타임스퀘어 전체가 당신 얼굴입니다.",
                    "이 순간은 숫자가 아니라 전 인류의 컴퓨팅 방식을 재정의한 여정의 시작일 뿐이라고 선언하세요.",
                    ("This IPO isn't the finish line, Alistair—it's Day One of rewiring the global computational infrastructure.", "이번 상장은 결승선이 아닙니다, 알리스테어. 전 세계 컴퓨팅 인프라를 혁신하는 진정한 ‘첫날(Day One)’의 시작일 뿐입니다.", "아마존 제프 베조스의 ‘Day One’ 철학을 계승한 위대한 창업자의 시그니처 멘트입니다."),
                    ("I am so nervous that my heart is beating very fast.", "가슴이 너무 빨리 뛰어서 엄청 긴장됩니다.", "세계적인 테크 거물로 도약하는 순간에 어울리지 않는 나약한 표현입니다."),
                    ("I prepared a nice ment for this morning call event.", "오늘 이 모닝콜 행사를 위해 멋진 멘트를 준비해왔습니다.", "‘ment’와 ‘morning call’은 연설 및 개장 행사와 무관한 한국식 콩글리시입니다.")
                ),
                make_turn(
                    "The bell rang. The stock opened at eighty-five dollars, up seventy percent from the IPO price. CNBC wants your live reaction to the retail frenzy.",
                    "종이 울렸습니다. 공모가보다 70% 폭등한 85달러에 시초가가 형성되었습니다. CNBC가 이 개미 투자자들의 열광에 대한 실시간 소감을 원합니다.",
                    "단기 주가 변동에 일희일비하지 않고 10년 뒤 잉여현금흐름 창출에만 집중하겠다고 의연하게 인터뷰하세요.",
                    ("We don't manage this company for quarter-to-quarter stock pops. We build enduring enterprise value that compounds over decades.", "우리는 분기별 주가 급등을 위해 이 회사를 경영하지 않습니다. 우리는 수십 년에 걸쳐 복리로 성장할 영속적인 기업가치를 구축합니다.", "‘quarter-to-quarter stock pops’와 ‘compounds over decades’는 워런 버핏 수준의 깊이를 보여주는 명답입니다."),
                    ("I think our price will go up much higher so please buy a lot.", "우리 주가가 훨씬 더 올라갈 테니 많이 사주시면 좋겠습니다.", "증권거래위원회(SEC) 규정 위반 소지가 있는 미성숙한 발언입니다."),
                    ("Everyone, let's do fighting together and enjoy Dutch pay tonight.", "여러분 모두 함께 파이팅하고 오늘 밤은 더치페이로 즐깁시다.", "‘fighting’과 ‘Dutch pay’는 글로벌 생중계 인터뷰에서 품격을 떨어뜨리는 표현입니다.")
                ),
                make_turn(
                    "Your seed stake is now worth two point four billion dollars liquid. You're officially on the Forbes billionaire list. How does it feel to win Silicon Valley?",
                    "당신의 초기 지분 가치는 이제 현금화 가능한 24억 달러(약 3조 2천억 원)입니다. 공식 포브스 억만장자 명단에 올랐습니다. 실리콘밸리를 정복한 기분이 어떻습니까?",
                    "부의 축적이 아니라 혁신의 가능성에 감사하며 다음 세대 창업자들을 육성하겠다고 품격 있게 마무리하세요.",
                    ("Capital is merely fuel for human audacity. We will deploy these resources to mentor and fund the next generation of impossible dreamers.", "자본은 단지 인간의 담대한 도전을 위한 연료일 뿐입니다. 우리는 이 자원을 다음 세대의 위대한 도전자들을 육성하는 데 아낌없이 투자할 것입니다.", "‘fuel for human audacity’는 실리콘밸리의 전설적인 리더들이 남기는 불멸의 어록입니다."),
                    ("I am going to buy a big house in Beverly Hills and three sports cars.", "비벌리힐스에 큰 집을 사고 스포츠카 세 대를 살 계획입니다.", "천박하고 단견적인 졸부의 인상을 풍깁니다."),
                    ("Thank you, let's have a meeting to discuss my salary bonus spec.", "감사합니다, 제 연봉 보너스 스펙을 논의하기 위해 미팅을 잡읍시다.", "‘spec’과 ‘meeting’을 남발하는 부자연스러운 문장입니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 2. Corporate Empire & M&A
    # -------------------------------------------------------------
    data["Corporate Empire & M&A"] = [
        make_episode(
            "적대적 공개매수(Tender Offer): 경영권 방어용 황금낙하산 가동",
            "Logan Roy (Media Mogul Chairman)", "🏢",
            "행동주의 사모펀드가 장내 지분 매집을 통해 40% 공개매수를 선언했다. 이사회 의결권을 장악하고 적대적 인수를 원천 분쇄해야 한다.",
            "trigger the golden parachute and poison pill",
            "적대적 M&A 시도를 무산시키기 위해 기존 주주들에게 헐값 신주인수권을 부여하고 경영진 교체 비용을 극대화하는 방어 전략입니다.",
            [
                make_turn(
                    "They're offering thirty percent above market to our retail shareholders. If forty percent tender by Friday, I'm out of my own building. What's your defense?",
                    "그들이 소액주주들에게 시장가보다 30% 웃돈을 얹어 제안했어. 금요일까지 40%가 주식을 넘기면 내가 내 빌딩에서 쫓겨나. 방어 전략이 뭐야?",
                    "즉각 독약 조항(Poison Pill)을 가동해 기존 주주들에게 50% 할인 신주 배정을 단행하자고 제안하세요.",
                    ("We trigger the flip-in poison pill immediately, diluting their voting bloc into oblivion while our treasury absorbs the float.", "즉각 플립인 포이즌 필을 발동해 적들의 의결권 지분을 완전히 희석시키고, 자사주 펀드로 유통 주식을 흡수하겠습니다.", "‘flip-in poison pill’과 ‘dilute into oblivion’은 월가 경영권 분쟁 드라마의 최고급 전문 용어입니다."),
                    ("I will tell the shareholders that the chairman is a very nice person.", "주주들에게 우리 회장님이 매우 좋은 분이라고 호소하겠습니다.", "감정적인 호소로 냉혹한 금융 시장에서 아무 효과가 없습니다."),
                    ("Let's claim the buyer for their rude meeting action.", "무례한 미팅 행동에 대해 매수자에게 클레임을 겁니다.", "‘claim’은 소송이나 항의를 표현하기에 매우 어색한 콩글리시입니다.")
                ),
                make_turn(
                    "The Delaware Chancery Court might enjoin the poison pill if they smell entrenchment. How do we justify it under Unocal standards?",
                    "델라웨어 형평법원은 경영진의 자리보전 꼼수로 보이면 포이즌 필을 효력 정지시킬 수도 있어. 유노칼 판례 기준에 맞춰 어떻게 정당화할 건가?",
                    "적들의 공개매수가 기업의 장기적 주주 가치를 파괴하는 약탈적 자산 매각형 공격임을 입증하자고 하세요.",
                    ("We demonstrate a coercive, two-tiered tender offer designed to strip corporate assets. Our board's defensive response is proportional and reasonable under Unocal.", "적들의 제안이 기업 자산을 해체하려는 강압적 2단계 공개매수임을 입증하겠습니다. 우리 이사회의 방어 조치는 유노칼 판례상 비례적이고 합리적입니다.", "‘coercive two-tiered tender offer’와 ‘proportional and reasonable’은 미국 회사법상 경영권 방어의 핵심 법리입니다."),
                    ("We will say to the judge that we really want to keep our jobs.", "판사에게 우리가 일자리를 지키고 싶다고 사정하겠습니다.", "사리사욕으로 비쳐 패소를 자초하는 답변입니다."),
                    ("Our company has high spec so we can handle this easily.", "우리 회사는 스펙이 좋아서 이 일을 쉽게 핸들할 수 있습니다.", "‘spec’과 ‘handle’을 오용한 콩글리시입니다.")
                ),
                make_turn(
                    "They blink. Their financing bank just withdrew their commitment letter. We hold the empire. Pour yourself a scotch.",
                    "놈들이 물러섰어. 주관 은행이 방금 자금 조달 확약서를 철회했더군. 우리가 제국을 지켜냈네. 스카치 한 잔 따르게.",
                    "단순한 방어에 그치지 않고 상대 사모펀드의 핵심 포트폴리오를 역인수하자고 승부사 기질을 발휘하세요.",
                    ("We shouldn't just celebrate defense, Logan. Let's launch a Pac-Man counter-bid and swallow their flagship fund whole.", "단순한 방어 성공에 머물지 마시죠, 로건 회장님. 팩맨 역인수를 개시해 상대의 주력 펀드를 통째로 집어삼킵시다.", "‘Pac-Man counter-bid’는 피인수 기업이 역으로 인수자를 공격하는 전설적인 역공 전략 용어입니다."),
                    ("Thank you sir, let's take a rest and eat dinner.", "감사합니다 회장님, 이제 쉬면서 저녁이나 먹으러 가시죠.", "긴장감을 이어가지 못하는 맥없는 답변입니다."),
                    ("Let us do Dutch pay for the scotch bottle tonight.", "오늘 밤 스카치 병은 더치페이로 계산하시죠.", "재벌 총수와의 축배 자리에서 ‘더치페이’를 꺼내는 부적절한 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "사모펀드(PEF)의 레버리지드 바이아웃(LBO): 실사(Due Diligence) 격돌",
            "Logan Roy (Media Mogul Chairman)", "🏢",
            "글로벌 1위 사모펀드가 200억 달러 LBO 인수를 제안하며 기밀 회계 장부 실사에 착수했다. 기업가치를 뻥튀기하고 숨겨진 우발 채무를 방어해야 한다.",
            "negotiate the EBITDA multiple and carve out liabilities",
            "에비타(상각전영업이익) 멀티플 배수를 극대화하고 잠재 부채를 거래 대상에서 분리 매각할 때 쓰는 M&A 핵심 표현입니다.",
            [
                make_turn(
                    "Blackstone's forensic accountants are auditing our overseas streaming subsidiaries. They claim our reported EBITDA is inflated by four hundred million.",
                    "블랙스톤의 회계 감사팀이 우리 해외 스트리밍 자회사를 샅샅이 뒤지고 있어. 우리 공시 에비타가 4억 달러나 부풀려졌다고 트집을 잡더군.",
                    "해당 비용은 일회성 인프라 감가상각이며 조정 에비타(Adjusted EBITDA) 기준으로 기업가치가 오히려 저평가되었다고 방어하세요.",
                    ("Those are non-recurring capital expenditures. When adjusted for one-off studio acquisitions, our underlying cash flow multiple justifies a premium.", "그 항목들은 일회성 자본적 지출입니다. 단발성 스튜디오 인수를 조정한 순수 현금흐름 배수는 오히려 프리미엄을 정당화합니다.", "‘non-recurring capital expenditures’와 ‘underlying cash flow multiple’은 회계 실사에서 주도권을 잡는 최고급 표현입니다."),
                    ("Maybe our accounting team made a small mistake on the numbers.", "우리 회계팀이 숫자에 작은 실수를 했을 수도 있습니다.", "자신의 과실을 스스로 인정해 인수가를 후려치게 만드는 최악의 발언입니다."),
                    ("Tell them not to cunning our secret book.", "그들에게 우리 비밀 장부를 커닝하지 말라고 전하세요.", "‘cunning’은 콩글리시이며, 정밀 감사는 ‘audit’ 또는 ‘inspect’입니다.")
                ),
                make_turn(
                    "They want a fifty percent earn-out provision tied to next year's subscriber growth. That means half our cash is locked in jeopardy.",
                    "놈들이 내년 구독자 순증치에 연동된 50%의 언아웃(Earn-out) 지급 조건을 걸었어. 매각 대금 절반이 볼모로 잡힌다는 뜻이야.",
                    "사후 성과급인 언아웃을 거부하고 전액 계약 즉시 클로징 현금으로 지급받는 확정가(Locked Box) 방식으로 협상하세요.",
                    ("We reject any contingent earn-out structure. We demand a locked-box closing mechanism with full cash consideration at signing.", "사후 성과 연동 언아웃 구조는 거부합니다. 서명 즉시 전액 현금으로 확정 지급받는 ‘락트박스(Locked-box)’ 방식을 관철시키겠습니다.", "‘contingent earn-out’과 ‘locked-box closing mechanism’은 M&A 계약의 리스크를 제거하는 프로페셔널한 조항입니다."),
                    ("I think fifty percent is too much, can we make it forty percent?", "50%는 너무 많은 것 같으니 40%로 해주시면 안 될까요?", "협상의 프레임에 말려들어 수세에 몰리는 답변입니다."),
                    ("We can give them one-plus-one free trial for subscribers.", "구독자들에게 원플러스원 무료 체험을 주면 됩니다.", "수천억 원 M&A 협상에 어울리지 않는 마트 할인식 콩글리시입니다.")
                ),
                make_turn(
                    "Deal signed. Two hundred and ten million in enterprise value, all cash. You just handed me the biggest liquidity event in media history.",
                    "계약서에 도장을 찍었네. 기업가치 2억 1천만 달러, 전액 현금 완납일세. 자네가 미디어 역사상 최대 규모의 유동성 현금화를 내 손에 쥐여줬어.",
                    "회장님의 위대한 결단 덕분이며 이제 다음 글로벌 플랫폼 합병을 준비하자고 담대하게 답하세요.",
                    ("A victory of this magnitude secures your dynasty for three generations. Now we pivot from seller to acquirer of the next frontier.", "이 정도 규모의 승리는 3대에 걸친 로이 가문의 왕조를 보장합니다. 이제 우리는 매도자에서 다음 개척지의 지배적 인수자로 전환할 때입니다.", "‘secures your dynasty’와 ‘pivot from seller to acquirer’는 거대 기업 총수를 전율하게 만드는 위대한 피날레입니다."),
                    ("I hope I can get a high promotion spec after this deal.", "이 딜이 끝나고 높은 승진 스펙을 얻을 수 있기를 희망합니다.", "‘spec’을 남발하며 개인의 밥그릇만 챙기는 인상을 줍니다."),
                    ("Let's send an SNS photo to brag about our meeting.", "우리 미팅을 자랑하기 위해 SNS 사진을 올립시다.", "‘SNS’는 콩글리시이며 기밀 M&A 거래 직후 경솔한 언행입니다.")
                )
            ]
        ),
        make_episode(
            "주주총회 표 대결: 행동주의 펀드의 이사회 장악 시도 격퇴",
            "Logan Roy (Media Mogul Chairman)", "🏢",
            "월가 최고의 행동주의 펀드가 기관투자자들을 포섭해 사외이사 4석 교체 주주제안을 올렸다. 의결권 대리행사(Proxy Fight)에서 완승을 거두어야 한다.",
            "win the decisive proxy fight on the AGM floor",
            "정기 주주총회(AGM) 표 대결에서 압도적인 표차로 승리해 경영권을 수호할 때 쓰는 표현입니다.",
            [
                make_turn(
                    "Institutional Shareholder Services just recommended a vote against our slate of directors. The Vanguard and BlackRock proxies are wavering.",
                    "의결권 자문사 ISS가 방금 우리 측 이사 선임안에 반대 권고를 냈어. 뱅가드와 블랙록의 위임장 표가 흔들리고 있단 말이야.",
                    "자사주 10억 달러 소각 및 특별 배당 정책을 긴급 발표해 기관투자자들의 표심을 우리 쪽으로 확정시키자고 하세요.",
                    ("We announce an immediate one-billion-dollar share repurchase and special dividend hike. Cash in their pockets will override ISS advice every single time.", "즉각 10억 달러 규모의 자사주 매입 소각과 특별 배당금 인상을 전격 발표하겠습니다. 기관들의 주머니에 들어갈 현금은 언제나 ISS 권고안을 압도합니다.", "‘share repurchase’와 ‘special dividend hike’는 주주총회 표 대결에서 승리를 보장하는 필승 카드입니다."),
                    ("We can write a letter to the shareholders asking them to trust us.", "주주들에게 우리를 믿어달라는 편지를 쓰면 어떨까요.", "아무런 경제적 실익이 없는 공허한 호소입니다."),
                    ("Our board members have good personality and skinship with staff.", "우리 이사회 멤버들은 인성이 좋고 직원들과 스킨십도 잘합니다.", "‘skinship’은 콩글리시이며 전문성 평가와 무관한 표현입니다.")
                ),
                make_turn(
                    "The activist fund CEO is taking the microphone on the floor right now, accusing us of empire-building at the expense of returns. Cut him down.",
                    "행동주의 펀드 대표가 지금 주총장 마이크를 잡고 우리가 주주 수익을 희생해 개인 제국을 쌓고 있다고 비난하고 있어. 저자의 숨통을 끊어놔.",
                    "상대 펀드가 과거 3년간 파산시킨 기업들의 참담한 실적을 스크린에 띄워 투기 자본의 민낯을 폭로하세요.",
                    ("We project their five-year asset-stripping record onto the main monitors. Show the room that their 'reforms' leave pension funds bankrupt and workers jobless.", "그들이 지난 5년간 자산을 헐값 매각해온 파괴적 전력을 메인 스크린에 띄우겠습니다. 그들의 ‘개혁’이 연기금을 파산시키고 노동자들을 길거리로 내몰았음을 만천하에 폭로하십시오.", "‘asset-stripping record’와 ‘leave pension funds bankrupt’는 주주총회 현장을 뒤흔드는 압도적인 웅변술입니다."),
                    ("Tell him to stop talking because he is speaking too loudly.", "그가 너무 시끄럽게 말하니 말을 멈추라고 소리치겠습니다.", "유치한 감정싸움으로 장내 통제력을 상실하게 만듭니다."),
                    ("He has bad manners so let's call the security for after service.", "매너가 나쁜 자이니 애프터 서비스로 경호원을 부릅시다.", "‘after service’는 콩글리시이며, 강제 퇴장은 ‘escort off the premises’입니다.")
                ),
                make_turn(
                    "The ballots are certified. Seventy-four percent voted for our board slate. The activists are running for the exit doors. You own this room.",
                    "개표 결과가 공식 인증되었네. 74%가 우리 이사회 안건에 찬성표를 던졌어. 행동주의 놈들이 비상구로 도망치고 있더군. 자네가 주총장을 완전히 지배했어.",
                    "적들의 지분을 패배자 할인 가격으로 장외 매수해 후환을 완전히 제거하자고 완벽한 마무리를 제안하세요.",
                    ("Let's buy back their remaining shares at a ten percent fire-sale discount before the closing bell. We don't leave wounded wolves at our borders.", "장 마감 전에 그들의 잔여 지분을 10% 떨이 할인 가격으로 장외 매수해 버리시죠. 국경에 상처 입은 늑대를 살려둘 수는 없습니다.", "‘fire-sale discount’와 ‘leave wounded wolves’는 적을 완벽하게 굴복시키는 승자의 언어입니다."),
                    ("I am happy we won the election today.", "오늘 선거에서 이겨서 기분이 좋습니다.", "일반 정치 선거와 주주총회 경영권 방어를 혼동한 표현입니다."),
                    ("Let us do Dutch pay to celebrate our win tonight.", "오늘 밤 승리를 축하하며 더치페이로 밥을 먹읍시다.", "‘Dutch pay’는 품격을 깨뜨리는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "글로벌 지주회사 체제 완성: 세기의 가문 승계 협약",
            "Logan Roy (Media Mogul Chairman)", "🏢",
            "스위스 제네바 비밀 패밀리 오피스. 로이 가문의 수천억 달러 신탁 자산 승계 구조를 완성하고 차기 총수의 영구적 경영권을 법적으로 확정해야 한다.",
            "cement the family trust and absolute voting control",
            "가문 신탁을 공고히 하고 절대적 의결권 장악을 법적으로 영구화할 때 쓰는 최고위 경영권 표현입니다.",
            [
                make_turn(
                    "My three children have hired separate Wall Street litigators to break the irrevocable family trust. If they crack it, the empire shatters into three pieces.",
                    "내 세 자식 놈들이 취소불능 가문 신탁을 깨부수려고 각자 월가 소송 전문 변호사들을 고용했어. 저들이 신탁을 깨뜨리면 제국은 세 조각으로 공중분해 돼.",
                    "신탁 계약서에 불복 분쟁 제기 시 상속 자격을 즉각 박탈하는 노콘테스트(No-contest) 조항을 발동하자고 하세요.",
                    ("We trigger the forfeiture in terrorem clause. Any heir who challenges your governance automatically forfeits their beneficial interest in its entirety.", "즉각 ‘상속권 박탈(In terrorem)’ 조항을 발동하겠습니다. 회장님의 지배구조에 도전하는 후계자는 그 즉시 신탁 수익권을 전액 영구 몰수당합니다.", "‘forfeiture in terrorem clause’는 가문 신탁 분쟁을 원천 차단하는 가장 치명적인 영미 상속법 조항입니다."),
                    ("Tell your kids that family love is more important than money.", "자녀분들에게 돈보다 가족 간의 사랑이 중요하다고 타이르겠습니다.", "수조 원 승계 싸움에서 비웃음만 사는 나이브한 소리입니다."),
                    ("Let's make a meeting to discuss their allowance spec.", "용돈 스펙에 대해 상의하기 위해 가족 미팅을 잡읍시다.", "‘spec’과 ‘meeting’을 오용한 유치한 표현입니다.")
                ),
                make_turn(
                    "They will claim I signed under duress or mental incapacity. The Swiss trustees are trembling under their subpoenas.",
                    "놈들은 내가 강박이나 심신미약 상태에서 서명했다고 주장할 걸세. 스위스 수탁인들이 소환장을 받고 벌벌 떨고 있어.",
                    "세계 최고의 독립 신경학 권위자 3인의 공증 감정서와 공증인 비디오 녹취록을 완비했다고 안심시키세요.",
                    ("We have three independent heads of neurology certifying full testamentary capacity on videotaped sworn affidavit. Their challenge is dead on arrival.", "이미 3명의 독립 신경학회장들이 전적인 유언 능력을 공증 진술서와 비디오로 완벽히 입증해두었습니다. 그들의 소송은 시작도 전에 기각될 것입니다.", "‘testamentary capacity’와 ‘dead on arrival’은 유언 무효 소송을 단숨에 궤멸시키는 완벽한 방어입니다."),
                    ("I can show the doctor's note from yesterday saying you are fine.", "회장님이 건강하시다는 어제 자 의사 소견서를 보여주면 됩니다.", "수천억 달러 가문 신탁을 방어하기엔 너무나 조악한 서류입니다."),
                    ("Do not worry, our morning call was very clear today.", "걱정 마세요, 오늘 모닝콜 때 회장님 목소리가 아주 또렷하셨습니다.", "‘morning call’은 콩글리시(wake-up call)입니다.")
                ),
                make_turn(
                    "They surrendered. The Swiss court sealed the trust irrevocably. The board just elected you co-chairman with permanent succession power. You're royalty.",
                    "놈들이 백기를 들었네. 스위스 법원이 신탁을 취소불능으로 영구 봉인했어. 이사회가 방금 자네를 영구 승계권을 가진 공동 회장으로 선출했네. 자네가 왕이야.",
                    "단순한 왕좌에 머물지 않고 제국을 영원불멸의 미래 지배자로 진화시키겠다고 서약하세요.",
                    ("A crown is not inherited, Logan—it is forged in crisis. Under our joint command, this empire will rule the century.", "왕관은 상속받는 것이 아닙니다, 로건 회장님. 위기 속에서 스스로 담금질하는 것입니다. 우리의 공동 지휘 아래 이 제국은 100년을 지배할 것입니다.", "‘forged in crisis’는 셰익스피어 비극과 현대 비즈니스 드라마의 정점을 잇는 최고의 명대사입니다."),
                    ("Thank you, I will buy expensive clothes with my new salary.", "감사합니다, 새로 받는 월급으로 비싼 옷을 사 입겠습니다.", "권력의 정점에 선 군주답지 못한 가벼운 처신입니다."),
                    ("Let's do Dutch pay for the celebration dinner.", "축하 저녁 식사는 더치페이로 합시다.", "‘Dutch pay’는 품격을 깨뜨리는 콩글리시입니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 3. Emergency Medicine
    # -------------------------------------------------------------
    data["Emergency Medicine"] = [
        make_episode(
            "다발성 외상 환자 후송: 트라우마 베이 1초의 기도 확보",
            "Dr. Derek Sloan (Chief of Trauma Surgery)", "🏥",
            "고속도로 8중 추돌 사고로 혈압이 급락하고 다발성 갈비뼈 골절로 기도 삽관이 불가능한 환자가 실려왔다. 트라우마 베이에서 1초 만에 응급 윤상갑상절개술을 집도해야 한다.",
            "perform an emergency surgical cricothyroidotomy",
            "기도가 완전히 폐쇄되어 일반 삽관이 불가능할 때 목을 절개해 1초 만에 산소를 공급하는 응급 외과 술기입니다.",
            [
                make_turn(
                    "Pulse is thready at one-forty, systolic pressure dropping through seventy. O-negative blood is running, but severe facial trauma obstructs the vocal cords. We can't intubate!",
                    "맥박 140회로 미약하고 수축기 혈압 70선까지 무너지고 있습니다. O형 음성 혈액 주입 중이지만 안면 중증 외상으로 성대가 전혀 안 보입니다. 일반 삽관이 불가능합니다!",
                    "즉각 윤상갑상막을 촉지하고 10번 메스로 윤상갑상절개술을 집도해 산소를 확보하겠다고 선언하세요.",
                    ("Scalpel, number ten blade! I'm performing an immediate surgical cricothyroidotomy. Prep the tracheostomy tube and bag him now!", "10번 메스 주세요! 즉각 응급 윤상갑상절개술을 집도합니다. 기관절개관 연결하고 지금 즉시 앰부 배깅 시작하세요!", "‘surgical cricothyroidotomy’와 ‘bag him now’는 의학 드라마 응급실 골든타임을 가르는 정통 외과 전문 용어입니다."),
                    ("Please try to put the tube in his mouth again carefully.", "환자 입속으로 튜브를 다시 한번 조심스럽게 넣어보세요.", "시간을 지체하여 환자를 뇌사 상태로 몰아넣는 위험천만한 지시입니다."),
                    ("Give the patient a morning call so he can wake up.", "환자가 깨어날 수 있게 모닝콜을 해주세요.", "‘morning call’은 콩글리시이며, 환자 의식 확인은 ‘check consciousness’입니다.")
                ),
                make_turn(
                    "Airway secured! Saturation bouncing back to ninety-five. But the ultrasound shows massive free fluid in Morrison's pouch. Splenic rupture!",
                    "기도 확보 완료! 산소포화도 95%까지 회복되었습니다. 하지만 복부 초음파(FAST) 상 모리슨와에 대량의 복강 내 출혈이 보입니다. 비장 파열입니다!",
                    "즉각 트라우마 수술실 1번으로 직행해 응급 개복술 및 비장 절제술을 집도하겠다고 명령하세요.",
                    ("Call the blood bank for a Massive Transfusion Protocol! Push four units of PRBCs and roll straight into OR One for an exploratory laparotomy!", "혈액원에 즉시 대량 수혈 프로토콜(MTP) 발동하세요! 농축적혈구 4파인트 밀어 넣고 응급 개복술 위해 1번 수술실로 직행합니다!", "‘Massive Transfusion Protocol’과 ‘exploratory laparotomy’는 외상외과의 꽃인 긴급 수술 호출 용어입니다."),
                    ("Let's wait for thirty minutes to see if the bleeding stops.", "출혈이 멈추는지 30분 동안 지켜봅시다.", "저혈량성 쇼크로 환자를 사망에 이르게 하는 치명적인 오판입니다."),
                    ("Tell the family we need their sign for after service.", "보호자에게 애프터 서비스를 위해 사인이 필요하다고 하세요.", "‘sign’과 ‘after service’는 동의서(consent form)에 쓰지 않는 콩글리시입니다.")
                ),
                make_turn(
                    "Peritoneal cavity packed with lap pads. Bleeder clamped and cross-matched. Systolic pressure stabilizing at one-ten. You just pulled him back from the morgue.",
                    "복강 내 패킹 완료. 출혈 혈관 결찰 및 교차시험 완료되었습니다. 수축기 혈압 110으로 완벽히 안정되었습니다. 선생님이 방금 영안실 문턱에서 환자를 끌고 오셨습니다.",
                    "모든 팀원의 일사불란한 협업 덕분이라며 중환자실(ICU) 모니터링을 빈틈없이 지시하세요.",
                    ("Outstanding work by everyone in this trauma bay. Transfer him to the surgical ICU and maintain arterial line hemodynamics. We're not losing this kid.", "트라우마 베이 전 팀원들 훌륭했습니다. 외과계 중환자실로 이송하고 동맥관 혈역학 모니터링 유지하세요. 이 환자 절대 놓치지 않습니다.", "‘maintain arterial line hemodynamics’는 외상센터 치프 서전의 완벽한 리더십 마무리입니다."),
                    ("I am tired, I will go sleep in the lobby chair.", "피곤하니 로비 의자에 가서 잠이나 자겠습니다.", "중증 외상 환자 케어 직후 의료인으로서 매우 무책임한 발언입니다."),
                    ("Let us do Dutch pay for the emergency surgery fee.", "응급 수술 비용은 다 함께 더치페이로 냅시다.", "‘Dutch pay’는 부적절한 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "신경외과 응급 개두술: 뇌압 급상승과 집도의의 결단",
            "Dr. Derek Sloan (Chief of Trauma Surgery)", "🏥",
            "뇌동맥류 파열로 인한 지주막하 출혈(SAH) 환자. 동공 부동증(Anisocoria)이 발생하며 뇌탈출(Herniation) 1분 전 위기다. 개두술로 혈종을 제거해야 한다.",
            "perform an emergent decompressive hemicraniectomy",
            "두개골 절반을 열어 뇌압을 낮추고 뇌탈출을 방지하는 신경외과의 초응급 뇌수술입니다.",
            [
                make_turn(
                    "Left pupil is blown, fixed at six millimeters. ICP monitor reads forty-eight. The uncus is herniating into the brainstem. We have four minutes before brain death!",
                    "좌측 동공 산대, 6mm로 고정되었습니다. 뇌압 수치 48까지 치솟았습니다. 뇌구가 뇌간으로 탈출하고 있습니다. 뇌사까지 4분 남았습니다!",
                    "만니톨과 고장성 식염수를 급속 투여하며 감압성 반구 두개골 절제술을 집도하겠다고 명령하세요.",
                    ("Push three percent hypertonic saline and two hundred of mannitol now! Shave the scalp, prep the craniotome—we're performing an emergent decompressive hemicraniectomy!", "3% 고장성 식염수와 만니톨 200cc 즉각 풀드립하세요! 두피 면도하고 크래니오톰 준비, 즉각 응급 감압성 반구 두개골 절제술 집도합니다!", "‘decompressive hemicraniectomy’는 신경외과 뇌압 위기를 극복하는 최고난도 수술 명칭입니다."),
                    ("Put an ice pack on his head to cool down the brain.", "뇌를 식히기 위해 머리에 얼음주머니를 올려놓으세요.", "뇌탈출 환자에게 무의미한 민간요법에 불과합니다."),
                    ("The patient has bad spec so his brain is weak.", "환자가 스펙이 안 좋아서 뇌가 약합니다.", "‘spec’은 취업 스펙 콩글리시이며 환자 건강 상태와 무관합니다.")
                ),
                make_turn(
                    "Bone flap elevated. Dura is tense and dark blue. Once we incise the dura, high-pressure subdural hematoma will erupt under arterial pressure.",
                    "두개골 절편 들어 올렸습니다. 경막이 암청색으로 팽팽하게 부풀었습니다. 경막을 절개하는 순간 고압의 경막하 혈종이 동맥혈 압력으로 솟구칠 겁니다.",
                    "석션 팁 두 대를 동시에 대기시키고 신속하게 혈종을 감압한 뒤 출혈 동맥류를 클리핑하자고 지시하세요.",
                    ("Double suction ready! Number eleven blade to nick the dura, aspirate the clot, and isolate the middle cerebral bifurcation for titanium aneurysm clipping.", "더블 석션 즉시 대기! 11번 메스로 경막 미세 절개 후 혈종 흡입하고, 티타늄 동맥류 클립으로 중대뇌동맥 분기부 결찰합니다!", "‘titanium aneurysm clipping’과 ‘aspirate the clot’는 뇌수술 장면의 긴박감을 최고조로 끌어올리는 표현입니다."),
                    ("Close your eyes and cut the membrane very fast.", "눈을 감고 막을 아주 빠르게 자르세요.", "의학적 상식에 어긋나는 위험한 발언입니다."),
                    ("Please handle the brain with good skinship.", "뇌를 좋은 스킨십으로 다뤄주세요.", "‘skinship’은 콩글리시이며, 섬세한 조작은 ‘meticulous tissue handling’입니다.")
                ),
                make_turn(
                    "Aneurysm clipped cleanly! Pulsations returned to the cortical vessels. Intracranial pressure plummeted to twelve. Look at his pupils—symmetrical and reactive!",
                    "동맥류 완벽히 클리핑 완료! 대뇌 피질 혈관의 정상 박동이 돌아왔습니다. 뇌압 12로 급강하했습니다. 동공 보세요, 대칭으로 반응합니다!",
                    "기적 같은 회생이라며 두개골 재건까지 무균 처치를 완벽히 유지하라고 치프 서전답게 명령하세요.",
                    ("Flawless execution under immense pressure. Apply synthetic dural graft and loosely approximate the scalp. Get him to Neuro-ICU for strict blood pressure titration.", "극한의 압박 속에서 무결점 집도였습니다. 인공 경막 이식재 대고 두피 봉합하세요. 신경계 중환자실로 올려 혈압 정밀 조절 들어갑니다.", "‘blood pressure titration’과 ‘synthetic dural graft’는 신경외과 수술의 품격을 완성하는 단어입니다."),
                    ("I am happy the head operation is over.", "머리 수술이 끝나서 참 다행입니다.", "치프 서전의 무게감에 어울리지 않는 초보적인 표현입니다."),
                    ("Let's do Dutch pay for the bone glue fee.", "두개골 접착제 비용은 더치페이로 계산합시다.", "‘Dutch pay’는 병원에서 쓰지 않는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "대규모 생물학 오염 환자 유입: 응급실 오염제거(Decon) 프로토콜",
            "Dr. Derek Sloan (Chief of Trauma Surgery)", "🏥",
            "공업 단지 화학공장 폭발 사고로 미상의 유기인계 독성 가스에 노출된 환자 수십 명이 응급실로 쏟아져 들어온다. 병원 전체 마비를 막고 2차 오염을 차단해야 한다.",
            "lock down the ER and initiate hazmat decontamination",
            "응급실을 즉각 봉쇄하고 위험물질(Hazmat) 제독 절차를 가동해 병원 감염을 차단할 때 쓰는 긴급 의료 명령입니다.",
            [
                make_turn(
                    "First wave of victims collapsed in the ambulance bay! Paramedics are vomiting, pinpoint pupils everywhere. It's organophosphate nerve agent! They're rushing through the sliding doors!",
                    "구급차 하차장에서 1차 피해자들이 쓰러졌습니다! 구급대원들도 구토하고 있고 전원 동공 축소 증세입니다. 유기인계 신경독성물질입니다! 환자들이 응급실 자동문으로 밀고 들어옵니다!",
                    "응급실 자동문을 즉각 락다운하고 제독 텐트 외부 설치 전까지 단 한 명도 들여보내지 말라고 엄명하세요.",
                    ("Lock down the double doors now! Do not breach the perimeter! Scramble the Hazmat decontamination tent in the parking lot and suit up in Level C gear!", "응급실 이중문 즉각 봉쇄하세요! 경계선 뚫리면 안 됩니다! 주차장에 유독물질 제독 텐트 즉시 전개하고 전원 레벨 C 보호구 착용하세요!", "‘breach the perimeter’와 ‘Hazmat decontamination’은 생화학 재난 드라마의 심장을 뛰게 하는 명령입니다."),
                    ("Open the doors and let them inside to lie down.", "문을 열고 그들이 안으로 들어와 눕게 해주세요.", "응급실 전체를 독가스로 오염시켜 수백 명을 위험에 빠뜨리는 최악의 지시입니다."),
                    ("Ask the victims to do a meeting about their symptoms.", "피해자들에게 증상에 대한 미팅을 열어보라고 하세요.", "‘meeting’을 남발하는 어색한 콩글리시입니다.")
                ),
                make_turn(
                    "Decon showers running. But three pediatric patients in respiratory arrest inside the hot zone need atropine immediately. We're running low on autoinjectors!",
                    "제독 샤워 가동되었습니다. 하지만 핫존 내부에서 호흡 정지가 온 소아 환자 3명에게 아트로핀 투여가 시급합니다. 자동 주사기 재고가 바닥나고 있습니다!",
                    "병원 국가비축물자(SNS) 캐비닛을 열고 정맥용 아트로핀과 프랄리독심을 고용량으로 공급하라고 지시하세요.",
                    ("Crack the federal stockpile cache in the pharmacy basement! Push high-dose intravenous atropine until pulmonary secretions dry up, backed by pralidoxime!", "약제부 지하 국가비축물자 캐시 금고를 여세요! 폐 분비물이 마를 때까지 고용량 정맥용 아트로핀 밀어 넣고 프랄리독심으로 보강하세요!", "‘pulmonary secretions dry up’과 ‘federal stockpile cache’는 신경독 해독의 정석 의학 지침입니다."),
                    ("Give the babies warm tea to drink.", "아기들에게 따뜻한 차를 마시게 하세요.", "호흡 정지 환자에게 질식을 유발하는 위험한 오답입니다."),
                    ("The medicine has good spec so one drop is enough.", "그 약은 스펙이 좋아서 한 방울이면 충분합니다.", "‘spec’은 의약품 용량에 쓰지 않는 콩글리시입니다.")
                ),
                make_turn(
                    "All forty-two victims decontaminated. Secretions controlled, vitals stable. Zero hospital staff compromised. CDC hazmat units just arrived to take over.",
                    "피해자 42명 전원 제독 완료되었습니다. 분비물 억제되었고 활력징후 안정되었습니다. 병원 의료진 2차 감염 0건입니다. 질병통제센터(CDC) 재난팀이 인계하러 방금 도착했습니다.",
                    "한 사람의 희생도 없이 방어선을 지켜낸 의료진에게 경의를 표하며 질병통제센터에 상황을 브리핑하세요.",
                    ("Outstanding discipline under biological fire. Hand over the patient rosters to CDC and send all staff through secondary monitoring. We held the line.", "생화학 참호전 속에서 보여준 탁월한 규율이었습니다. 환자 명부를 CDC에 인계하고 전 직원 2차 모니터링 통과시키세요. 우리가 방어선을 지켜냈습니다.", "‘held the line’과 ‘under biological fire’는 의학 재난 드라마를 마무리하는 최고의 명문장입니다."),
                    ("I will go home right now and drink beer.", "지금 당장 집에 가서 맥주나 마시겠습니다.", "제독 절차 확인 전 무단이탈하는 위험한 태도입니다."),
                    ("Let's do Dutch pay for the hazmat suit cleaning.", "방호복 세탁비는 다 함께 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "샴쌍둥이 뇌 분리 수술: 28시간 기적의 집도",
            "Dr. Derek Sloan (Chief of Trauma Surgery)", "🏥",
            "두개골과 대뇌 상시상정맥동(Superior Sagittal Sinus)을 공유하는 샴쌍둥이의 영구 분리 수술. 전 세계 신경외과 서전들의 이목이 쏠린 수술실에서 28시간의 집도를 완성해야 한다.",
            "dissect the shared superior sagittal sinus",
            "두 아기가 공유하는 뇌의 거대 정맥동 혈관을 혈전이나 뇌경색 없이 0.1mm 오차로 분리해낼 때 쓰는 최고난도 수술 표현입니다.",
            [
                make_turn(
                    "Hour twenty-two. We have split the frontal lobes, but the superior sagittal sinus is shared over six centimeters. One slip of the micro-scissors and both babies bleed out.",
                    "수술 22시간 경과. 전두엽 분리는 끝났지만, 상시상정맥동 6cm를 두 아기가 완벽히 공유하고 있습니다. 미세 가위가 0.1mm만 삐끗해도 두 아기 모두 과다출혈로 사망합니다.",
                    "혈관 바이패스 그라프트를 걸고 헤파린 주입 후 현미경 시야 하에서 정맥동 혈관벽을 재건 분리하겠다고 선언하세요.",
                    ("Position the operative microscope at forty-times zoom. We place temporary micro-vascular clips, reconstruct the sinus wall with saphenous vein graft, and divide them millimeter by millimeter.", "수술 현미경 배율 40배로 올리세요. 미세 혈관 클립 걸고 대복재정맥 이식재로 정맥동 혈관벽 재건하면서 1밀리미터씩 정밀 분리합니다!", "‘saphenous vein graft’와 ‘micro-vascular clips’는 고난도 혈관 재건의 정점을 보여주는 표현입니다."),
                    ("Let's close our eyes and pray to God to help us cut.", "눈을 감고 신께 잘 잘라달라고 기도합시다.", "수술실에서 미신에 기대는 비과학적인 태도입니다."),
                    ("Be careful with the baby skinship during the surgery.", "수술 중 아기 스킨십에 주의하세요.", "‘skinship’은 콩글리시입니다.")
                ),
                make_turn(
                    "Twin A's EEG shows slowing wave activity! Right hemisphere is suffering venous congestion. The bypass graft is clotting!",
                    "쌍둥이 A의 뇌파가 급격히 느려지고 있습니다! 우측 반구에 정맥 울혈이 발생하고 있습니다. 바이패스 혈관에 혈전이 차오르고 있습니다!",
                    "즉각 국소 tPA 혈전용해제를 주입하고 풍선 카테터로 혈전을 흡입해 혈류를 재개통시키라고 명령하세요.",
                    ("Inject intracranial tPA directly into the graft lumen and advance the Fogarty catheter! Flush with heparinized saline until flow restores!", "이식 혈관 내강에 두개 내 tPA 즉각 직접 주입하고 포가티 카테터 진입하세요! 혈류 재개통될 때까지 헤파린 생리식염수로 플러시합니다!", "‘intracranial tPA’와 ‘Fogarty catheter’는 혈관 폐색 급변 상황을 타개하는 완벽한 처치입니다."),
                    ("Slap the baby's foot to make him wake up.", "아기 발바닥을 때려서 깨워보세요.", "개두술 중 뇌정맥 폐색 환자에게 아무 효과 없는 엉뚱한 행동입니다."),
                    ("Tell the nurse to do after service quickly.", "간호사에게 애프터 서비스를 빨리하라고 하세요.", "‘after service’는 수술실에서 쓰이지 않는 콩글리시입니다.")
                ),
                make_turn(
                    "Hour twenty-eight. Both babies separated onto their own tables. Brain waves synchronized. Two distinct hearts beating. Derek, look what you just achieved.",
                    "수술 28시간 경과. 두 아기가 마침내 각자의 독립된 수술대로 분리되었습니다. 뇌파 양쪽 모두 정상 동기화. 두 개의 심장이 따로 뛰고 있습니다. 데릭 선생, 당신이 해낸 걸 보세요.",
                    "인류 의학의 한계를 함께 넘어준 30명의 수술팀 전체에게 깊은 존경을 표하며 마무리하세요.",
                    ("Two individual lives, two bright futures. This triumph belongs to all thirty surgeons, anesthesiologists, and scrub nurses who gave their blood and souls today.", "두 개의 온전한 생명, 두 개의 찬란한 미래입니다. 오늘의 기적은 피와 영혼을 쏟아부은 30명의 집도의, 마취의, 수술 간호사 모두의 것입니다.", "시청자들의 눈물샘을 자극하는 메디컬 드라마 역사상 최고의 피날레 대사입니다."),
                    ("I am going to post this on my blog to get many likes.", "좋아요를 많이 받기 위해 블로그에 올리겠습니다.", "환자 개인정보 보호법 위반 소지가 있는 경솔한 발언입니다."),
                    ("Let's all do Dutch pay for the surgery celebration dinner.", "수술 축하 회식은 다 같이 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 4. Manhattan Romance & High Society
    # -------------------------------------------------------------
    data["Manhattan Romance & High Society"] = [
        make_episode(
            "소호 갤러리 오프닝 갈라: 전 연인의 약혼 발표와 샴페인 독대",
            "Serena Van Der Woodsen (Socialite)", "🥂",
            "뉴욕 소호의 최상류층 아트 갈라 파티. 억만장자 상속남과 약혼을 전격 발표한 전 연인이 샴페인 글라스를 들고 당신에게 다가온다. 상류 사교계의 가면을 쓴 채 우아하게 기선을 제압해야 한다.",
            "maintain composure under high-society scrutiny",
            "상류 사교계의 쏟아지는 시선과 파파라치 앞에서도 완벽한 품격과 여유를 유지할 때 쓰는 표현입니다.",
            [
                make_turn(
                    "Everyone in Manhattan is watching us right now. They expected you to skip my engagement gala. Aren't you going to congratulate me on my billionaire fiancé?",
                    "지금 맨해튼 사교계 전체가 우리를 쳐다보고 있어. 다들 네가 내 약혼 갈라에 도망칠 줄 알았거든. 내 억만장자 약혼자와의 결혼 축하 인사 안 해줄 거야?",
                    "흔들림 없는 미소로 그의 약혼을 축하하며, 당신의 진짜 행복이 진품인지 가품인지 우아하게 떠보세요.",
                    ("Congratulations, Serena. He bought you a magnificent diamond, but we both know diamonds can't buy an ounce of genuine devotion.", "약혼 축하해, 세레나. 그가 멋진 다이아몬드를 사줬더군. 하지만 다이아몬드로도 진정한 영혼의 헌신은 단 1온스도 살 수 없다는 걸 우리 둘 다 알잖아.", "‘genuine devotion’과 품격 있는 도발은 미국 하이틴·상류층 로맨스 드라마의 시그니처 화법입니다."),
                    ("I am very sad and angry that you marry another man.", "네가 다른 남자와 결혼해서 너무 슬프고 화가 나.", "찌질하고 감정을 주체하지 못하는 패배자로 비칩니다."),
                    ("Let's do skinship like old days in the corner.", "구석에 가서 예전처럼 스킨십이나 하자.", "‘skinship’은 콩글리시이며 품격을 바닥으로 떨어뜨리는 최악의 성희롱적 표현입니다.")
                ),
                make_turn(
                    "He gives me security, legacy, and a seat at the Metropolitan Museum board. Can your pride really compete with a dynasty?",
                    "그는 나에게 안정과 가문의 유산, 그리고 메트로폴리탄 미술관 이사회 자리를 약속했어. 너의 자존심이 정말 한 가문의 왕조와 경쟁할 수 있다고 생각해?",
                    "황금 감옥에 갇힌 새는 날 수 없다며, 진짜 자유와 열정은 자신이 쥐고 있음을 각인시키세요.",
                    ("A gilded cage is still a cage, darling. You chose a family dynasty; you forfeited the only person who ever saw your true soul.", "금빛으로 칠해졌을지언정 새장은 결국 새장일 뿐이야. 넌 가문의 왕조를 택했고, 네 진짜 영혼을 유일하게 알아봐 준 사람을 영원히 잃어버린 거지.", "‘a gilded cage is still a cage’는 상류층 정략결혼의 허상을 찌르는 매혹적인 명문장입니다."),
                    ("You are a bad gold digger who only likes money.", "너는 돈만 밝히는 나쁜 꽃뱀에 불과해.", "저급하고 유치한 비난으로 사교계에서 조롱거리가 됩니다."),
                    ("Please call me on my handphone when you are lonely.", "외로울 때 내 핸드폰으로 전화 줘.", "‘handphone’은 콩글리시이며 매력이 전혀 없는 미련입니다.")
                ),
                make_turn(
                    "Her hands are trembling. She sets down her glass. 'Meet me on the rooftop terrace in ten minutes. No cameras, no bodyguards. Just us.'",
                    "세레나의 손이 미세하게 떨립니다. 그녀가 샴페인 잔을 테이블에 내려놓습니다. '10분 뒤에 루프탑 테라스로 와. 카메라도 경호원도 없이, 오직 우리 둘만.'",
                    "비밀스러운 만남을 수락하되, 이번에는 과거의 상처가 아닌 새로운 룰로 시작하자고 리드하세요.",
                    ("Ten minutes on the terrace, Serena. But when we step onto that roof, we leave the Upper East Side lies at the door.", "루프탑 테라스에서 10분 뒤에 보지, 세레나. 하지만 그 문을 나서는 순간, 어퍼이스트사이드의 가식적인 거짓말들은 문밖에 두고 와.", "‘leave the lies at the door’는 숨 막히는 텐션을 최고조로 끌어올리는 로맨틱한 킬러 멘트입니다."),
                    ("Okay, I will run to the rooftop very fast right now.", "알겠어, 지금 당장 루프탑으로 엄청 빨리 뛰어갈게.", "안달 난 태도로 신비감을 완전히 잃어버립니다."),
                    ("Let's do Dutch pay for the rooftop cocktail.", "루프탑 칵테일은 더치페이로 마시자.", "‘Dutch pay’는 낭만을 산산조각 내는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "센트럴파크 프라이빗 클럽: 상류층 상속녀의 비밀스러운 계약",
            "Serena Van Der Woodsen (Socialite)", "🥂",
            "맨해튼 5번가 최고급 회원제 클럽의 밀실. 정략결혼을 파기하려는 사교계 퀸이 거액의 신탁 펀드를 미끼로 가짜 약혼자 역할을 제안한다.",
            "enter a high-stakes fake engagement",
            "상류층의 정략결혼을 파탄 내기 위해 계약 약혼 관계에 돌입할 때 쓰는 상류층 로맨스 단골 소재 표현입니다.",
            [
                make_turn(
                    "If I don't produce a respectable fiancé before the shareholders' ball, my grandfather hands my trust fund to my cousin. I need you to play my lover for ninety days.",
                    "주주 총회 무도회 전까지 존경받을 만한 약혼자를 데려가지 않으면 할아버지가 내 신탁 펀드를 사촌에게 넘길 거야. 90일 동안 내 연인 역할을 해줘.",
                    "단순한 돈벌이가 아니라 상류 사교계 전체를 뒤흔들 연극의 지휘권을 요구하세요.",
                    ("I don't play a puppet for trust fund games, Serena. If I'm your fiancé, we play by my script, in front of every camera in New York.", "난 신탁 펀드 놀음의 꼭두각시 노릇은 안 해, 세레나. 내가 네 약혼자가 된다면 뉴욕의 모든 카메라 앞에서 내 각본대로 움직이는 거야.", "‘play a puppet’과 ‘by my script’는 관계의 주도권을 완전히 가져오는 섹시하고 당당한 대사입니다."),
                    ("How much money will you give me to be your boyfriend?", "남자친구 역할을 해주면 돈을 얼마나 줄 건가요?", "단순한 고용인 취급을 자초하는 품격 없는 질문입니다."),
                    ("Let's make a meeting to discuss our love spec.", "우리의 연애 스펙을 상의하기 위해 미팅을 합시다.", "‘spec’과 ‘meeting’을 오용한 콩글리시입니다.")
                ),
                make_turn(
                    "My mother will put you through a pedigree audit. She'll check your watch, your polo handicap, and your family crest. Can you survive the Waldorf scrutiny?",
                    "우리 엄마가 네 가문 족보 감사를 시작할 거야. 네 손목시계, 폴로 경기 핸디캡, 가문 문장까지 전부 검증할 텐데, 월도프 가문의 날카로운 시선을 견딜 수 있겠어?",
                    "가짜 혈통 따위는 필요 없으며 나의 존재감 하나로 당신 어머니를 매료시키겠다고 답하세요.",
                    ("Pedigree is an illusion bought by old money. I won't pretend to be royalty—I will make your mother realize I am the only man who can tame you.", "족보란 구시대 귀족들이 돈으로 산 환상일 뿐이야. 왕족인 척 흉내 낼 생각 없어. 당신 어머니에게 당신을 길들일 수 있는 유일한 남자가 나라는 걸 똑똑히 보여줄 테니까.", "‘pedigree is an illusion’과 ‘tame you’는 사교계 모친의 편견을 박살 내는 매력적인 킬러 표현입니다."),
                    ("I will rent an expensive suit and fake my father's job.", "비싼 수트를 빌려 입고 아버지 직업을 거짓말로 지어내겠습니다.", "들통날 거짓말로 자멸하는 길입니다."),
                    ("I have high spec in my university grades so I am confident.", "대학교 학점 스펙이 높아서 자신 있습니다.", "‘spec’은 콩글리시입니다.")
                ),
                make_turn(
                    "She smiles for the first time in months. 'You're infuriating, arrogant, and completely reckless. Deal. The Hamptons Fourth of July gala is our premiere.'",
                    "세레나가 몇 달 만에 처음으로 환하게 미소 짓습니다. '넌 정말 사람 미치게 하고, 오만하고, 대책 없이 무모해. 좋아, 계약 성립이야. 햄튼 독립기념일 갈라가 우리의 공식 데뷔 무대야.'",
                    "맨해튼 전체가 우리 약혼에 열광하게 만들자며 샴페인 잔을 부딪치세요.",
                    ("To our scandalous debut, Serena. Let's give Manhattan something they will talk about for the rest of their lives.", "우리의 스캔들 가득한 데뷔를 위하여, 세레나. 평생토록 이야기할 화젯거리를 맨해튼에 선물해 주지.", "‘scandalous debut’는 로맨스 드라마 에피소드 엔딩의 설렘을 완성하는 대사입니다."),
                    ("Thank you for the contract, I will do my best.", "계약 감사합니다, 최선을 다하겠습니다.", "직원의 업무 다짐처럼 들려 로맨틱한 기류가 식어버립니다."),
                    ("Let's do Dutch pay for the gala tickets tonight.", "오늘 밤 갈라 티켓은 더치페이로 합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "햄튼 여름 별장 파티: 파파라치를 따돌린 한밤의 보트 탈출",
            "Serena Van Der Woodsen (Socialite)", "🥂",
            "햄튼 억만장자 비치 하우스의 화려한 파티장. 파파라치와 사교계 기자들의 집요한 플래시 세례를 뚫고, 달빛 비치는 대서양 바다로 둘만의 한밤 요트 탈출을 감행한다.",
            "escape the paparazzi frenzy under the moonlight",
            "사교계 언론의 광기 어린 플래시 세례를 따돌리고 둘만의 로맨틱한 탈출을 감행할 때 쓰는 표현입니다.",
            [
                make_turn(
                    "There are forty telephoto lenses pointed at the terrace right now. Page Six is live-streaming our argument. If we walk through the front gate, we get torn to pieces.",
                    "지금 테라스를 향해 망원 렌즈 40대가 겨눠져 있어. 페이지 식스가 우리 언쟁을 생중계하고 있단 말이야. 정문으로 나갔다간 갈기갈기 찢겨.",
                    "정문 대신 백사장 개인 선착장에 정박해둔 스피드보트로 바다를 가르며 탈출하자고 리드하세요.",
                    ("Forget the front gate. The Riva speedboat is idling at the private pier. Kick off your heels, Serena—we're taking the Atlantic.", "정문 따위는 잊어. 개인 선착장에 리바 스피드보트 시동 걸려 있어. 하이힐 벗어 던져, 세레나. 대서양 바다로 탈출한다.", "‘kick off your heels’와 ‘taking the Atlantic’은 로맨스 영화 명장면을 재현하는 박력 넘치는 대사입니다."),
                    ("Let's call the police and complain about the reporters.", "경찰에 전화해서 기자들에 대해 불평을 늘어놓읍시다.", "수동적이고 답답한 대처로 매력이 반감됩니다."),
                    ("Please wait, I need to check my handphone SNS.", "잠깐만요, 핸드폰 SNS를 확인해야 합니다.", "‘handphone’과 ‘SNS’는 콩글리시입니다.")
                ),
                make_turn(
                    "The wind is catching her silk gown. She kicks off her Louboutins into the sand. 'You're insane! The tide is coming in and Montauk is twenty nautical miles away!'",
                    "바닷바람이 그녀의 실크 드레스를 흩날립니다. 세레나가 루부탱 구두를 모래사장에 벗어 던집니다. '너 미쳤어! 밀물이 들어오고 있고 몬톡 항구까지는 20해리나 된단 말이야!'",
                    "두려움을 떨쳐내고 내 손을 잡으면 평생 잊지 못할 밤을 선물하겠다고 확신을 주세요.",
                    ("Take my hand and jump. The open ocean doesn't care about Manhattan rumors—tonight, the world is ours.", "내 손 잡고 뛰어내려. 드넓은 바다는 맨해튼의 소문 따윈 신경 쓰지 않아. 오늘 밤, 세상은 우리 둘만의 것이야.", "‘the world is ours’는 여주인공의 심장을 멎게 만드는 불멸의 로맨틱 명대사입니다."),
                    ("If you are scared, we can go back inside the party.", "무서우면 파티장 안으로 다시 돌아가도 됩니다.", "순간의 로맨틱한 기세를 스스로 꺾어버리는 나약한 태도입니다."),
                    ("Let's do skinship on the boat to stay warm.", "따뜻하게 보트 위에서 스킨십이나 합시다.", "‘skinship’은 콩글리시입니다.")
                ),
                make_turn(
                    "The twin engines roar, spray washing over the teak deck under a canopy of stars. Serena laughs breathlessly, leaning her head on your shoulder. 'I never want to go back.'",
                    "트윈 엔진이 굉음을 울리며 밤하늘 별빛 아래 티크 원목 데크 위로 하얀 물보라가 튑니다. 세레나가 숨이 차도록 웃으며 당신 어깨에 머리를 기댑니다. '나 다시는 맨해튼으로 돌아가고 싶지 않아.'",
                    "뉴욕이 우리를 찾지 못할 세상 끝까지 달려가겠다고 속삭이세요.",
                    ("Then we don't go back. We chart our own course toward the dawn, beyond the reach of their gilded city.", "그럼 돌아가지 마. 그 화려한 도시의 손길이 닿지 않는 곳, 새벽 여명이 비치는 저 너머로 우리만의 항로를 여는 거야.", "‘beyond the reach of their gilded city’는 한 편의 영화 같은 여운을 남기는 로맨틱 클로징입니다."),
                    ("Tomorrow is Monday so we have to go back to work.", "내일 월요일이라 출근해야 하니 돌아가야 합니다.", "낭만을 박살 내는 지극히 현실적인 찬물 끼얹기입니다."),
                    ("Let's do Dutch pay for the boat gasoline tomorrow.", "내일 보트 기름값은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        make_episode(
            "파리 오페라 극장 귀빈석: 세기의 정략결혼 파기와 프러포즈",
            "Serena Van Der Woodsen (Socialite)", "🥂",
            "파리 팔레 가르니에 오페라 극장의 로열 박스 석. 유럽 왕실 귀족과의 세기의 결혼 서약식을 10분 앞두고, 턱시도를 입은 당신이 샹들리에 불빛 아래 그녀의 손을 가로챈다.",
            "sweep her away before the vows are spoken",
            "세기의 결혼 서약이 낭독되기 직전 극적으로 사랑하는 여인을 구출해낼 때 쓰는 시네마틱 프러포즈 표현입니다.",
            [
                make_turn(
                    "The Prince is waiting at the altar downstairs. The French archbishop has the wedding register open. Why are you here in Paris? Why did you follow me across the ocean?",
                    "아래 제단에서 왕세자가 기다리고 있어. 프랑스 대주교가 혼인 서약서를 펼쳤단 말이야. 왜 파리까지 온 거야? 왜 바다를 건너 날 쫓아온 건데?",
                    "거짓된 왕관을 버리고 오직 진실한 사랑인 나를 선택하라고 심장을 흔드세요.",
                    ("Because you don't belong to a European throne, Serena. You belong to the wild, untamed love we built together in the heart of the night.", "넌 유럽의 왕좌 따위에 어울리는 여자가 아니니까, 세레나. 넌 한밤의 심장부에서 우리가 함께 일군 거칠고 순수한 사랑에 어울리는 사람이야.", "‘belong to the wild, untamed love’는 여주인공의 심장에 비수를 꽂는 감성 킬러 표현입니다."),
                    ("I bought an airplane ticket because I miss you.", "보고 싶어서 비행기 표 끊어서 왔습니다.", "웅장한 파리 오페라 하우스의 분위기에 어울리지 않는 평이한 답변입니다."),
                    ("Your prince has bad spec so don't marry him.", "네 왕자 스펙이 별로니까 그와 결혼하지 마.", "‘spec’은 콩글리시입니다.")
                ),
                make_turn(
                    "Tears glisten on her eyelashes, refracting the crystal chandeliers. 'If I walk away with you, I lose my title, my family inheritance, and my standing in Paris. What do you have to offer me?'",
                    "크리스털 샹들리에 빛이 그녀의 속눈썹에 맺힌 눈물방울에 반사됩니다. '내가 너와 함께 떠나면 난 작위도, 가문의 상속도, 파리 사교계의 명성도 모두 잃게 돼. 넌 내게 무엇을 줄 수 있는데?'",
                    "코트 주머니에서 반지를 꺼내며 영원히 변치 않을 자유와 목숨을 건 헌신을 바치겠다고 프러포즈하세요.",
                    ("I offer you no gilded titles, only an unbreakable ring and a lifetime where you never have to pretend to be someone you're not. Marry me, Serena.", "화려한 작위 따윈 줄 수 없어. 오직 부서지지 않을 이 반지 하나와, 네가 아닌 다른 사람인 척 연기하지 않아도 될 평생의 삶을 줄게. 나와 결혼해 줘, 세레나.", "‘never have to pretend to be someone you're not’은 가식에 지친 상류층 여주인공을 완전히 무너뜨리는 프러포즈 명대사입니다."),
                    ("I have a good job and high salary so don't worry.", "좋은 직장과 높은 연봉이 있으니 걱정 마세요.", "현실적인 직장인 어필로 낭만적 몰입감을 깨뜨립니다."),
                    ("Let's do morning call together every day.", "매일 아침 모닝콜을 같이 하자.", "‘morning call’은 콩글리시입니다.")
                ),
                make_turn(
                    "She drops her diamond bouquet onto the velvet floor. She grabs your lapels and kisses you passionately as the opera overture swells. 'Get me out of this dress. Take me home.'",
                    "세레나가 다이아몬드 부케를 벨벳 바닥에 떨어뜨립니다. 오페라 서곡이 웅장하게 울려 퍼지는 가운데 그녀가 당신의 턱시도 깃을 부여잡고 뜨겁게 입을 맞춥니다. '이 드레스에서 날 꺼내줘. 날 집으로 데려가 줘.'",
                    "그녀의 손을 잡고 파리의 밤거리로 뛰쳐나가며 영원한 사랑을 맹세하세요.",
                    ("From Paris to Manhattan, from this moment to our last breath—you are home, my love.", "파리에서 맨해튼까지, 이 순간부터 우리의 마지막 숨결까지—내 사랑, 내 곁이 바로 당신의 영원한 집이야.", "시청자들의 기립박수를 이끌어내는 역사상 가장 완벽한 로맨틱 피날레입니다."),
                    ("Hurry up, taxi fee is getting expensive.", "빨리 갑시다, 택시비 많이 나옵니다.", "감동을 와장창 깨뜨리는 경박한 태도입니다."),
                    ("Let's do Dutch pay for the wedding ring.", "결혼반지 값은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    return data

