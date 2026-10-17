# -*- coding: utf-8 -*-
"""
Dramactor Scenario Group Part 1 (Genres 19 to 29: 11 genres x 4 = 44 episodes)
19: Investigative Journalism
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
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_group_part1():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    # 19. Investigative Journalism
    data["Investigative Journalism"] = [
        mk("워터게이트 스타일 지하 주차장 내부고발자 심야 접선", "Ben Bradlee (Executive Investigative Editor)", "📰",
           "워싱턴 D.C. 외곽 지하 주차장 3층. 연방 법무부 고위 관리가 백악관의 사법방해 도청 증거를 넘기겠다고 접선을 요청했다. 도청 미행을 따돌리고 비밀 소식통을 보호하며 문건을 확보해야 한다.",
           "protect the confidential source under shield law doctrine", "취재원 비닉권 원칙에 입각해 비밀 내부고발자를 철통 보호할 때 쓰는 언론 전문 표현입니다.",
           [
               ("Our source is spooked. He says FBI surveillance cars are patrolling the garage perimeter. If we blow his cover, he faces life in prison. Do we abort the meet?",
                "취재원이 겁에 질렸어. FBI 감시 차량이 주차장 외곽을 순찰 중이래. 소식통 정체가 탄로 나면 그는 종신형이야. 접선을 취소할까?",
                "취소하지 말고 미행을 유인할 미끼 차량을 투입한 뒤 비상 계단으로 도보 접근하라고 지시하세요.",
                ("Do not abort. Send our decoy van to the front exit to draw surveillance. We walk down the fire stairwell on foot. We don't abandon Deep Throat.", "취소하지 마십시오. 미끼 밴을 정문 출구로 보내 감시망을 분산시키세요. 우리는 비상계단으로 도보 진입합니다. 우리는 결코 내부고발자를 버리지 않습니다.", "‘decoy van’과 ‘do not abandon Deep Throat’는 탐사보도 기자의 불굴의 용기를 보여주는 대사입니다."),
                ("Let's call the FBI and ask them to go home.", "FBI에 전화해서 집에 가라고 부탁합시다.", "수사기관에 체포를 자초하는 순진한 생각입니다."),
                ("The garage has bad spec so call the manager.", "주차장 스펙이 안 좋으니 관리인에게 따집시다.", "‘spec’은 콩글리시입니다.")),
               ("We got the microfilm! It proves the Attorney General ordered the wiretaps! But the White House counsel is threatening a national security injunction to stop publication.",
                "마이크로필름을 확보했어! 법무장관이 불법 도청을 직접 지시한 증거야! 하지만 백악관 법률고문이 국가안보 가처분 신청으로 인쇄를 막겠다고 협박해.",
                "두 명의 독립 취재원으로 교차 검증을 마쳤으니 수정헌법 제1조의 권리로 인쇄를 강행하자고 편집국장을 설득하세요.",
                ("We have two independent corroborating sources and ironclad provenance. We stand on the First Amendment and start the presses.", "독립된 교차 검증 취재원 두 명과 확고한 증거를 확보했습니다. 우리는 수정헌법 제1조에 입각해 윤전기를 돌려야 합니다.", "‘stand on the First Amendment’와 ‘start the presses’는 언론 자유의 정점을 상징하는 명문장입니다."),
                ("Tell the President that we are very sorry.", "대통령님께 정말 죄송하다고 사과합시다.", "언론인의 사명을 포기하는 비굴한 태도입니다."),
                ("Check the handphone for newspaper delivery.", "신문 배달을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("The morning edition hit the streets! Five hundred thousand copies sold out! The Attorney General just resigned! You won the Pulitzer Prize today, Ben.",
                "조간신문 배포 완료! 50만 부 전량 매진! 법무장관이 방금 자진 사임했어! 자네가 오늘 퓰리처상을 따냈네, 벤.",
                "어둠 속에서 민주주의가 죽지 않도록 진실의 횃불을 밝히는 것이 언론의 존재 이유라고 답하세요.",
                ("Democracy dies in darkness, Ben. As long as we have the courage to print the truth, the people will hold the power.", "민주주의는 암흑 속에서 죽어갑니다, 벤. 우리가 진실을 인쇄할 용기를 잃지 않는 한, 권력은 국민의 손에 남을 것입니다.", "워싱턴 포스트의 불멸의 모토를 담은 최고의 피날레입니다."),
                ("I am glad we don't have to write articles tomorrow.", "내일 기사 안 써도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the newsroom coffee.", "편집국 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("파나마 페이퍼스 페이퍼컴퍼니 비밀 해외 계좌 추적", "Ben Bradlee (Executive Investigative Editor)", "📰",
           "국제탐사보도언론인협회(ICIJ) 비밀 워룸. 전 세계 지도자들과 억만장자들의 2조 달러 조세회피 자료가 담긴 1,100만 건의 기밀 문건이 유출되었다. 금융 빅데이터를 암호 해독해 글로벌 특종을 터뜨려야 한다.",
           "decrypt and cross-examine shell company beneficial ownership",
           "페이퍼컴퍼니의 실제 실소유주를 암호화된 금융 빅데이터로 추적해낼 때 쓰는 탐사보도 전문 표현입니다.",
           [
               ("Eleven million encrypted PDF files! Prime ministers, oligarchs, cartel bosses! A cyber-security firm is already trying to DDoS our investigative server! What's our protocol?",
                "암호화된 PDF 파일 1,100만 건! 총리들, 올리가르히, 마약 카르텔 두목들까지! 보안 회사가 벌써 우리 서버에 디도스 공격을 퍼붓고 있어! 매뉴얼이 뭐야?",
                "서버를 즉시 물리적 에어갭으로 오프라인 격리하고 분산 암호화 파일 시스템으로 취재망을 보호하라고 명령하세요.",
                ("Sever external internet connections immediately! Transition our investigation to an air-gapped, encrypted offline cluster. No hacker touches our leak.", "외부 인터넷 연결을 즉시 차단하십시오! 에어갭 격리된 암호화 오프라인 클러스터로 취재망을 전면 전환하세요. 그 어떤 해커도 우리 유출본에 손댈 수 없습니다.", "‘air-gapped encrypted cluster’는 민감한 글로벌 기밀을 수호하는 완벽한 보안 조치입니다."),
                ("Let's delete the files so bad people don't get angry.", "나쁜 사람들이 화내지 않게 파일을 지워버립시다.", "세기의 특종을 스스로 폐기하는 어리석은 짓입니다."),
                ("The computer has bad spec so call the AS center.", "컴퓨터 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
               ("Data parsed! We linked an offshore shell in the British Virgin Islands directly to the incumbent European Prime Minister! He's threatening criminal libel lawsuits.",
                "데이터 파싱 완료! 영국령 버진아일랜드 페이퍼컴퍼니가 현직 유럽 총리에게 직결된 사실을 확인했어! 그가 형사 명예훼손 소송을 협박하고 있네.",
                "서명된 주주 명부와 스위스 은행 계좌 송금 내역 등 반박 불가능한 물증 사본을 공개하고 동시 합동 보도를 단행하자고 하세요.",
                ("We have his signed beneficial ownership deed and wire transfer receipts. Coordinated simultaneous release across eighty global newspapers tomorrow morning.", "그의 서명이 들어간 실소유주 증서와 송금 영수증을 확보했습니다. 내일 아침 전 세계 80개 신문사와 동시 합동 폭로를 단행합니다.", "‘beneficial ownership deed’와 ‘coordinated simultaneous release’는 정치인의 협박을 일격에 격파하는 언론 연대입니다."),
                ("Tell the Prime Minister that he is a bad leader.", "총리에게 나쁜 지도자라고 훈계나 합시다.", "법적 증거 없이 감정적으로 대응하는 하책입니다."),
                ("Check the handphone for offshore tax rates.", "해외 세율을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Global shockwaves! Prime Minister resigned before noon! Billions in unpaid taxes recovered worldwide! The Panama Papers won the Pulitzer Prize for Public Service!",
                "전 세계 충격파! 해당 총리가 정오 전에 자진 사임했어! 전 세계적으로 수십억 달러의 탈루 세금이 환수되었네! 파나마 페이퍼스가 퓰리처상 공공서비스 부문을 수상했어!",
                "국경을 넘는 진실의 힘이 부패한 권력의 성벽을 무너뜨렸다고 답하세요.",
                ("Corrupt power thrives behind offshore secrecy, Ben, but forensic journalism brings it crashing down. A victory for the global public.", "부패한 권력은 조세회피처의 비밀 뒤에서 번성하지만, 탐사 저널리즘은 그 성벽을 무너뜨립니다. 전 세계 시민의 위대한 승리입니다.", "글로벌 탐사보도의 금자탑을 세우는 감동적인 피날레입니다."),
                ("I am glad we don't have to read PDFs anymore.", "이제 PDF 파일 안 읽어도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the investigative pizza.", "탐사보도팀 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("거대 제약사 임상시험 사망 데이터 은폐 폭로", "Ben Bradlee (Executive Investigative Editor)", "📰",
           "보스턴 유력 일간지 편집국. 블록버스터 신약의 임상 3상에서 40명의 심장마비 사망 데이터가 조작 은폐되었다는 내부 제보. 제약사의 1억 달러 광고 철회 협박에 맞서 진실을 인쇄해야 한다.",
           "expose the falsified clinical trial mortality data",
           "환자들의 생명이 걸린 제약사의 임상 데이터 조작을 전 세계에 폭로할 때 쓰는 표현입니다.",
           [
               ("The pharma giant is our paper's largest advertiser! Their general counsel warns that if we publish, they cancel ten million in ads and sue our journalists personally!",
                "그 거대 제약사는 우리 신문사 최대 광고주야! 법무실장이 기사를 내면 1천만 달러 광고를 끊고 기자 개인을 상대로 소송을 걸겠다고 협박해!",
                "광고 수익보다 독자의 생명이 우선이므로 환자 유족들의 증언과 조작된 연구 노트 사본을 1면에 전격 배치하라고 하세요.",
                ("Our duty is to the patients and the truth, not corporate ad dollars. Put the whistleblower's redlined clinical reports and the victims' obituaries on page one.", "우리의 사명은 기업 광고비가 아니라 환자들과 진실에 있습니다. 내부고발자의 수정 전 임상 보고서와 희생자들의 부고를 1면에 올리십시오.", "‘duty to the patients’와 ‘redlined clinical reports’는 언론인의 진정한 용기와 사명을 증명하는 결단입니다."),
                ("Let's bury the story in the gardening section.", "원예 섹션 구석에 기사를 작게 묻어버립시다.", "언론의 양심을 팔아먹는 치욕적인 타협입니다."),
                ("The medicine has bad spec so tell the pharmacy.", "약 스펙이 안 좋으니 약국에 따집시다.", "‘spec’은 콩글리시입니다.")),
               ("The pharma CEO requested a private meeting in fifteen minutes. He's offering our foundation a fifty-million medical research endowment to hold the story for three months.",
                "제약사 CEO가 15분 내 비공개 면담을 요청했어. 기사를 석 달만 묻어두면 우리 재단에 5천만 달러 연구 기부금을 주겠대.",
                "뇌물성 기부를 단칼에 거절하고 회유 시도 자체를 녹취하여 후속 1면 톱기사로 싣겠다고 통보하세요.",
                ("Tell him the interview is on the record and his bribery attempt will be quoted verbatim above the fold tomorrow morning.", "면담은 공식 취재로 진행되며 그의 회유 시도 발언은 내일 아침 1면 머리기사에 글자 하나 안 바꾸고 실릴 것이라 통보하십시오.", "‘on the record’와 ‘quoted verbatim above the fold’는 부패한 기업인을 침묵시키는 언론의 철퇴입니다."),
                ("Take the fifty million so we can buy new desks.", "새 책상을 살 수 있게 5천만 달러를 받읍시다.", "언론인의 명예를 팔아먹는 범죄 행위입니다."),
                ("Check the handphone for stock prices.", "주가를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("FDA issued an emergency drug recall! Federal prosecutors indicted the pharmaceutical board! Our subscription numbers soared by forty percent! Journalism at its finest.",
                "FDA가 긴급 판매 중단 및 리콜을 명령했어! 연방 검찰이 제약사 이사진 전원을 기소했네! 우리 신문 구독률이 40% 폭등했어! 저널리즘의 진정한 정점이었네.",
                "진실을 인쇄할 때 언론은 세상에서 가장 강력한 정의의 무기가 된다고 답하세요.",
                ("When truth speaks with uncompromised courage, Ben, corporate greed collapses like a house of cards. The press has done its job.", "진실이 타협 없는 용기로 말을 걸 때, 기업의 탐욕은 모래성처럼 무너집니다. 언론은 자신의 사명을 다했습니다.", "스포트라이트(Spotlight)를 연상시키는 전율의 피날레입니다."),
                ("I am glad we can drink coffee quietly now.", "이제 조용히 커피를 마실 수 있어서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the newsroom dinner.", "편집국 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("연방수사국 압수수색 1시간 전 1면 전격 인쇄 결단", "Ben Bradlee (Executive Investigative Editor)", "📰",
           "워싱턴 D.C. 편집국. 국방부의 불법 무인기 민간인 사찰 기밀 파일에 대해 연방수사국(FBI)이 국가기밀누설죄로 압수수색 영장을 발부받아 편집국으로 들이닥치기 1시간 전. 인쇄를 단행해 국민에게 알려야 한다.",
           "order the emergency midnight press run before federal confiscation",
           "연방수사국의 압수수색 영장 집행 전 비상 심야 인쇄를 결단해 진실을 지켜낼 때 쓰는 표현입니다.",
           [
               ("Federal agents are outside the loading dock with a search warrant! If they confiscate the printing plates, the truth is buried forever! Do we roll the presses now?",
                "연방 요원들이 압수수색 영장을 들고 하역장 밖에 와 있어! 인쇄용 동판을 압수당하면 진실은 영원히 묻혀버려! 지금 즉시 윤전기를 돌릴까?",
                "영장 집행관이 편집실 문을 따기 전에 윤전기 풀가동 스위치를 올리고 트럭을 전국으로 발차시키라고 명령하세요.",
                ("Lock the editorial doors and spin the presses at maximum RPM! Roll five thousand copies out the secondary delivery alley before the feds breach the lobby!", "편집국 문을 걸어 잠그고 최대 속도로 윤전기를 돌리십시오! 연방 요원들이 로비 문을 뚫기 전에 보조 배송 골목으로 신문 5천 부를 먼저 발차시키세요!", "‘spin the presses at maximum RPM’은 언론의 자유를 사수하는 숨 막히는 긴급 명령입니다."),
                ("Let's hand over the papers to the FBI nicely.", "FBI에 신문을 고분고분 넘겨줍시다.", "헌법적 권리를 포기하는 비겁한 굴복입니다."),
                ("The printing machine has bad spec so call AS.", "인쇄기 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
               ("The feds breached the lobby! The lead agent is waving a federal court gag order demanding we halt the presses! You have ten seconds to respond.",
                "연방 요원들이 로비로 진입했어! 수석 요원이 법원 보도 금지 명령서를 흔들며 인쇄를 즉각 중단하라고 고함을 지르고 있어! 10초 안에 답변해야 해.",
                "신문은 이미 공공 유통망으로 발차되었으며 언론 출판의 자유는 사법부 명령으로 소급 금지될 수 없다고 헌법을 인용하세요.",
                ("The papers have left the loading dock and entered the public bloodstream, agent. Under the Supreme Court's Pentagon Papers precedent, prior restraint is unconstitutional.", "신문은 이미 하역장을 떠나 대중의 혈관 속으로 들어갔습니다, 요원님. 대법원의 펜타곤 페이퍼스 판례에 따라 사전 검열과 보도 금지는 위헌입니다.", "‘prior restraint is unconstitutional’은 미국 헌법상 언론의 자유를 수호하는 최고의 법률 명문입니다."),
                ("Tell the FBI agent that his uniform is ugly.", "FBI 요원에게 제복이 촌스럽다고 놀려봅시다.", "공무집행방해로 즉각 체포당하는 짓입니다."),
                ("Check the handphone for delivery truck GPS.", "배달 트럭 GPS를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("The trucks cleared the state line! The morning headline is in the hands of ten million Americans! The federal judge vacated the gag order! Freedom of the press stands!",
                "트럭들이 주 경계선을 넘었어! 오늘 아침 머리기사가 1천만 미국 시민의 손에 들어갔네! 연방 판사가 보도 금지 명령을 취소했어! 언론의 자유가 승리했네!",
                "우리가 물러서지 않았기에 진실이 자유의 땅을 지켜냈다고 자부심을 드러내세요.",
                ("They came with badges and warrants, Ben, but they could not silence the ink of a free people. The press stands unconquered.", "그들이 배지와 영장을 들고 왔지만, 자유로운 시민들의 잉크를 침묵시킬 수는 없었습니다. 언론은 꺾이지 않았습니다.", "역사적 언론 승리의 대미를 장식하는 명대사입니다."),
                ("I am glad we can sleep early tonight.", "오늘 밤 일찍 잘 수 있어서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the breakfast bagel.", "아침 베이글은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    return data
