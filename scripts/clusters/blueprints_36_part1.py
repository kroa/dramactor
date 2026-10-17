# -*- coding: utf-8 -*-
"""
Dramactor Scenario Group: 36 Blueprints - Part 1 (Genres 14 to 25: 12 genres x 4 = 48 episodes)
14: Crisis PR Management
15: Luxury Real Estate
16: Hollywood Talent Agency
17: 5-Star Hotel Hospitality
18: Fine Art Auction & Heist
19: Investigative Journalism
20: Cyber Crime & Zero-Day Hacking
21: Aerospace Defense & Top Gun
22: Space Exploration & Sci-Fi
23: True Crime Detective Noir
24: Organized Crime Syndicate
25: Formula 1 Motor Racing
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_blueprints_part1():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    def make_generic_genre(g_name, speaker, emoji, arcs):
        eps = []
        for arc in arcs:
            eps.append(mk_ep(arc["title"], speaker, emoji, arc["synopsis"], arc["key_expr"], arc["key_note"], arc["turns"]))
        data[g_name] = eps

    # 14. Crisis PR Management
    make_generic_genre(
        "Crisis PR Management", "Olivia Pope (Senior Crisis PR Managing Director)", "🎙️",
        [
            {
                "title": "대선 유력 후보 불륜 스캔들 녹취 유출 진화",
                "synopsis": "워싱턴 D.C. 대선 후보 TV 토론 2시간 전. 유력 상원의원의 은밀한 사생활 녹취 파일이 타블로이드에 유출되기 직전이다. 올리비아 포프의 워룸에서 여론의 주도권을 장악해야 한다.",
                "key_expr": "control the narrative before the twenty-four-hour news cycle opens",
                "key_note": "스캔들 보도가 확산되기 전 선제적 프레이밍으로 언론 주도권을 장악할 때 쓰는 표현입니다.",
                "turns": [
                    ("The Washington Post has the audio tape. They give us one hour for comment before hitting publish. What's the spin?",
                     "워싱턴 포스트가 녹음 파일을 확보했어. 기사 송고 전 우리에게 1시간의 반론 시간을 줬네. 프레임을 어떻게 짤 건가?",
                     "사실을 인정하거나 부인하지 말고 정치 공작 프레임으로 전환해 특별 기자회견을 선제 개최하자고 하세요.",
                     ("We do not comment; we pre-empt. Call a live press briefing in twenty minutes and frame this as foreign cyber-espionage targeting our democracy.", "단순 논평은 안 됩니다. 선제 타격해야 합니다. 20분 내 생중계 기자회견을 열고 민주주의를 겨냥한 외국의 사이버 공작으로 프레이밍하십시오.", "‘pre-empt’와 ‘frame as foreign cyber-espionage’는 스캔들을 국가 안보 이슈로 전환하는 천재적 위기관리입니다."),
                     ("Please beg the editor not to publish the article.", "편집장에게 기사를 내지 말아 달라고 애원합시다.", "기자의 특종 본능만 자극하는 무력한 대처입니다."),
                     ("The senator has bad manner so tell him to resign.", "상원의원이 매너가 나쁘니 사퇴하라고 하세요.", "‘manner’는 콩글리시입니다.")),
                    ("The press briefing stopped the initial bleeding. But CNN just booked the whistleblower for prime-time live tonight.",
                     "기자회견이 1차 출혈은 막았어. 하지만 CNN이 오늘 밤 황금시간대에 내부고발자 단독 생방송 인터뷰를 잡았네.",
                     "그녀가 서명한 비밀 유지 협약서 위반 가처분 신청과 거액의 금전 요구 정황을 폭로해 신빙성을 탄핵하자고 하세요.",
                     ("Serve CNN with an immediate injunction for non-disclosure breach and release bank records showing her financial extortion demands.", "CNN에 즉시 비밀유지 협약 위반 가처분 신청서를 송달하고, 그녀의 거액 금전 요구 정황이 담긴 계좌 내역을 공개하십시오.", "‘injunction for non-disclosure breach’와 ‘financial extortion’은 상대의 신빙성을 즉각 무력화하는 무기입니다."),
                     ("Let's tell the woman to be quiet and go home.", "그 여성에게 조용히 하고 집에 가라고 타일러봅시다.", "언론의 역풍을 부르는 어리석은 대응입니다."),
                     ("Check your handphone for the broadcast schedule.", "방송 일정을 확인하려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                    ("CNN cancelled the interview! The poll numbers held steady, and the debate opened with a standing ovation! You saved the presidency.",
                     "CNN이 인터뷰를 전격 취소했어! 지지율은 흔들리지 않았고 토론회는 기립박수로 시작되었네! 자네가 정권을 지켜냈어.",
                     "위기는 진실을 숨기는 것이 아니라 대중이 믿고 싶어 하는 진실을 설계하는 것이라고 답하세요.",
                     ("Crisis isn't about hiding secrets, Olivia—it's commanding the moral high ground so the storm passes around us. Handled.", "위기는 비밀을 숨기는 것이 아닙니다, 올리비아. 폭풍이 우리를 비껴가도록 도덕적 우위를 장악하는 것입니다. 처리 완료되었습니다.", "미드 스캔들의 시그니처 대사 ‘It's handled’를 완벽히 구현한 마무리입니다."),
                     ("I am glad we don't have to watch CNN tonight.", "오늘 밤 CNN 안 봐도 돼서 참 좋습니다.", "긴박한 승리의 의미를 살리지 못합니다."),
                     ("Let's do Dutch pay for the war room pizza.", "워룸 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
                ]
            },
            {
                "title": "포춘 50대 기업 CEO 횡령 내부고발자 봉쇄",
                "synopsis": "월스트리트 본사 옥상 헬리패드. 최고재무책임자(CFO)가 CEO의 5억 달러 비자금 내역을 SEC에 고발하겠다고 나섰다. 주가 폭락을 막고 질서 있는 승계를 이끌어야 한다.",
                "key_expr": "orchestrate an orderly board succession under executive NDA",
                "key_note": "사법 리스크를 최소화하고 비밀리에 질서 있는 이사회 승계를 성사시킬 때 쓰는 표현입니다.",
                "turns": [
                    ("The whistleblower is at the SEC building right now. If he files, the stock crashes fifty percent by market open. How do we stop him?",
                     "내부고발자가 지금 SEC 빌딩 로비에 있어. 접수되는 순간 개장과 동시에 주가가 50% 폭락해. 어떻게 막을 건가?",
                     "내부 감사 위원회 전권을 위임받은 독립 조사팀을 즉각 출범시키고 CFO를 임시 대표로 추대하겠다고 제안하세요.",
                     ("Intercept him in the lobby. Offer him the interim CEO chair and full authority to lead our independent internal audit before federal regulators step in.", "로비에서 그를 접촉하십시오. 연방 규제당국이 개입하기 전에 임시 대표직과 독립 내부 감사 전권을 부여하겠다고 제안하세요.", "‘interim CEO chair’와 ‘independent internal audit’는 내부고발자를 아군으로 전환하는 파격적 솔루션입니다."),
                     ("Call the police and tell them he is a bad thief.", "경찰에 전화해서 그가 나쁜 도둑이라고 말합시다.", "허위 신고로 법적 처벌을 자초하는 행동입니다."),
                     ("The CEO has bad spec so let's call AS.", "CEO 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
                    ("He took the meeting! But the disgraced founder refuses to step down quietly. He's calling an emergency press conference at the Plaza.",
                     "그가 제안을 수락했어! 하지만 불명예 퇴진할 창업자가 순순히 물러서지 않겠다며 플라자 호텔에서 비상 기자회견을 열겠대.",
                     "창업자의 해외 페이퍼컴퍼니 계좌와 세무조사 파일을 건네며 명예로운 은퇴 발표문과 교환하자고 압박하세요.",
                     ("Slide his offshore tax evasion dossier across the table. He signs the voluntary retirement memo, or he faces twenty years in federal prison.", "해외 조세회피 조사 파일을 책상 위로 밀어 넣으십시오. 자진 사임 메모에 서명하든지, 아니면 연방 교도소에서 20년을 썩든지 선택하게 하세요.", "‘offshore tax evasion dossier’와 ‘voluntary retirement’는 저항하는 거물을 굴복시키는 결정타입니다."),
                     ("Tell the founder to cry on television.", "창업자에게 텔레비전에서 울라고 하세요.", "시장의 조롱거리로 전락하는 대처입니다."),
                     ("Let's send an SNS post to mock the founder.", "창업자를 조롱하기 위해 SNS 글을 올립시다.", "‘SNS’는 콩글리시입니다.")),
                    ("Founder resigned citing health reasons! The stock opened up three percent! The SEC commended our voluntary governance cleanup! Flawless fix.",
                     "창업자가 건강상의 이유를 들어 자진 사임했어! 주가는 개장 직후 3% 상승했네! SEC가 자발적 지배구조 개선을 칭찬했어! 완벽한 해결이었네.",
                     "피를 흘리지 않고 암 덩어리를 도려내는 것이 바로 최고의 위기관리라고 답하세요.",
                     ("The greatest surgery leaves no scar, Olivia. The company survives, the truth is satisfied, and the empire marches on.", "최고의 수술은 흉터를 남기지 않습니다, 올리비아. 회사는 살아남았고, 진실은 지켜졌으며, 제국은 전진합니다.", "위기관리의 거장다운 깊은 통찰을 보여주는 피날레입니다."),
                     ("I am glad we don't have to work this weekend.", "이번 주말에 일 안 해도 돼서 참 좋습니다.", "비즈니스의 긴장감을 떨어뜨립니다."),
                     ("Let's do Dutch pay for the celebratory champagne.", "축하 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
                ]
            },
            {
                "title": "팝스타 개인 비공개 DM 해킹 유출 사태",
                "synopsis": "로스앤젤레스 그래미 어워드 전야제. 글로벌 팝스타의 비공개 인스타그램 DM과 미공개 음원이 다크웹에 유출되며 광고주들의 계약 해지 압박이 시작되었다. 여론을 반전시켜야 한다.",
                "key_expr": "weaponize the leak into an empowering artistic movement",
                "key_note": "사생활 유출 피해를 아티스트의 주체적 권리 신장 운동으로 승화시킬 때 쓰는 표현입니다.",
                "turns": [
                    ("The hackers dumped sixty personal messages online. Sponsors are calling demanding moral termination clauses! Do we apologize?",
                     "해커들이 개인 메시지 60건을 인터넷에 유출했어. 광고주들이 품위 유지 위반 조항을 들며 계약 해지를 요구해! 사과할까?",
                     "사과는 유죄 인정이므로 단칼에 거부하고 사이버 성범죄 피해자로서의 법적 철퇴와 지지를 호소하자고 하세요.",
                     ("Never apologize for being the victim of a federal cyber-crime. We launch an unyielding legal crusade against the perpetrators and stand tall.", "연방 사이버 범죄의 피해자가 된 것에 대해 결코 사과하지 마십시오. 가해자들을 상대로 가차 없는 법적 십자군을 개시하고 당당히 맞서야 합니다.", "‘never apologize for being a victim’은 수세에 몰린 여론을 공격적 지지로 전환하는 원칙입니다."),
                     ("Let's tell the pop star to hide in her bedroom.", "팝스타에게 침실에 숨어있으라고 하세요.", "아티스트의 커리어를 끝장내는 소극적 행동입니다."),
                     ("The singer has bad personality so let's claim to her.", "가수가 인성이 나쁘니 그녀에게 클레임합시다.", "‘claim’은 콩글리시입니다.")),
                    ("The narrative turned! Fans are rallying worldwide. But the hacker threatens to leak her unreleased album track at midnight unless paid one million in crypto.",
                     "여론이 반전되었어! 전 세계 팬들이 결집하고 있어. 하지만 해커가 암호화폐 1백만 달러를 주지 않으면 자정에 미공개 앨범을 유출하겠다고 협박해.",
                     "협박범의 돈줄을 끊기 위해 자정 5분 전에 스트리밍 플랫폼에 해당 트랙을 전격 무료 선공개하자고 제안하세요.",
                     ("Kill their ransom leverage. Release the mastered track on Spotify at 11:55 PM as a free gift to the fans. We turn their extortion into our triumph.", "협박범의 레버리지를 박살 내십시오. 밤 11시 55분에 스포티파이에 마스터링 음원을 팬들을 위한 무료 선물로 전격 공개하세요. 갈취 시도를 우리의 승리로 바꿉니다.", "‘kill their ransom leverage’와 ‘turn extortion into triumph’는 상대를 무력화하는 최고의 한 수입니다."),
                     ("Send the hacker one million dollars right now.", "해커에게 지금 즉시 1백만 달러를 송금합시다.", "추가 협박을 부르는 최악의 굴복입니다."),
                     ("Check your handphone for the crypto wallet code.", "암호화폐 지갑 코드를 보려고 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")),
                    ("The song broke the global streaming record in ten minutes! Two hundred million plays! Sponsors tripled their contract offers! You turned disaster into history.",
                     "노래가 10분 만에 글로벌 스트리밍 기록을 갈아치웠어! 2억 회 재생! 광고주들이 계약금을 3배로 불려왔네! 자네가 재앙을 역사로 바꿨어.",
                     "진정한 아티스트는 어둠 속에서도 자신만의 멜로디를 노래하는 법이라고 축하하세요.",
                     ("When they try to steal your voice, Olivia, you sing loud enough to shatter the glass. Problem solved.", "그들이 당신의 목소리를 훔치려 할 때, 유리창을 깨뜨릴 만큼 더 크게 노래하는 것입니다. 문제 해결되었습니다.", "올리비아 포프의 압도적 해결 능력을 상징하는 명대사입니다."),
                     ("I am glad we can listen to pop songs now.", "이제 팝송을 들을 수 있어서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                     ("Let's do Dutch pay for the LA tacos tonight.", "오늘 밤 LA 타코는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
                ]
            },
            {
                "title": "여객기 엔진 폭발 비상착륙 미디어 워룸",
                "synopsis": "시카고 오헤어 국제공항. 대형 여객기가 엔진 폭발로 비상착륙한 직후, 언론의 정비 불량 의혹 보도가 쏟아지기 시작했다. 희생자가 없는 상황에서 항공사의 브랜드 신뢰도를 수호해야 한다.",
                "key_expr": "lead with radical transparency and unyielding empathy",
                "key_note": "사고 직후 완전한 투명성과 깊은 공감으로 여론의 분노를 잠재울 때 쓰는 표현입니다.",
                "turns": [
                    ("The cable networks are screaming about negligence. The CEO wants to hide in his office until the NTSB preliminary report comes out next month.",
                     "케이블 방송들이 정비 태만이라며 아우성치고 있어. CEO는 다음 달 NTSB 예비 보고서가 나올 때까지 사무실에 숨어있겠대.",
                     "침묵은 죄의 인정이므로 CEO를 즉시 사고 현장으로 보내 승객들에게 고개 숙이고 전액 보상을 선언하게 하세요.",
                     ("Silence is guilt. Put the CEO on the tarmac right now. He looks the passengers in the eye, takes full responsibility, and guarantees lifetime flight care.", "침묵은 곧 유죄 인정입니다. 지금 즉시 CEO를 활주로로 보내십시오. 승객들의 눈을 똑바로 바라보며 전적인 책임을 지고 평생 케어를 약속해야 합니다.", "‘silence is guilt’와 ‘takes full responsibility’는 기업 위기관리의 황금률입니다."),
                     ("Tell the CEO to take a vacation to Hawaii.", "CEO에게 하와이로 휴가나 다녀오라고 하세요.", "국민적 공분을 부르는 파멸의 지름길입니다."),
                     ("The airplane spec is bad so blame the factory.", "비행기 스펙이 안 좋으니 비행기 공장을 탓합시다.", "‘spec’은 콩글리시입니다.")),
                    ("The press briefing worked. But a pilot union representative is on Twitter claiming engines were overdue for ultrasonic blade inspection.",
                     "브리핑은 효과가 있었어. 그런데 조종사 노조 대표가 트위터에 블레이드 초음파 검사 주기를 넘겼다는 폭로 글을 올렸어.",
                     "독립 항공안전재단에 전 비행기 전수 특별 점검을 의뢰하고 모든 점검 기록을 실시간 공개하겠다고 밝히세요.",
                     ("Announce an immediate voluntary fleet-wide grounding for independent ultrasonic inspections led by federal experts. Total openness disarms accusation.", "연방 전문가들이 주도하는 독립 초음파 검사를 위해 전 기종에 대한 자발적 운항 중단을 발표하십시오. 완전한 개방은 모든 의혹을 무장해제시킵니다.", "‘voluntary fleet-wide grounding’은 기업의 결백과 안전 의지를 입증하는 최고 수준의 조치입니다."),
                     ("Threaten to fire the pilot immediately.", "조종사를 즉시 해고하겠다고 협박합시다.", "노조 파업과 내부고발 폭로를 부르는 악수입니다."),
                     ("Check your handphone for airline ticket prices.", "항공권 가격을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
                    ("The FAA verified zero maintenance defects—it was an unprecedented drone collision! Our stock rebounded ten percent! Airline reputation intact!",
                     "연방항공청(FAA)이 정비 결함 제로를 확인했어. 전례 없는 불법 드론 충돌이었네! 주가가 10% 반등했어! 항공사 평판을 완벽히 지켜냈어!",
                     "정직함과 흔들리지 않는 원칙이야말로 가장 강력한 방패라고 화답하세요.",
                     ("Integrity under fire is the only brand that truly endures, Olivia. We told the truth, and the truth protected us. Case closed.", "포화 속에서의 진실성이야말로 진정으로 영원한 유일한 브랜드입니다, 올리비아. 우리는 진실을 말했고, 진실이 우리를 지켰습니다. 종결되었습니다.", "위기 PR의 품격을 보여주는 최고의 마무리입니다."),
                     ("I am glad we don't have to fly today.", "오늘 비행기 안 타도 돼서 참 좋습니다.", "프로페셔널한 긴장감이 아쉬운 답변입니다."),
                     ("Let's do Dutch pay for the Chicago pizza.", "시카고 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
                ]
            }
        ]
    )

    return data
