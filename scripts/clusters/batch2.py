# -*- coding: utf-8 -*-
"""
Dramactor Scenario Group 2 (Genres 7 to 15: 9 genres x 4 cycles = 36 episodes)
- FBI Criminal Profiling
- White House Politics
- Michelin Culinary
- CIA Covert Espionage
- Aviation Cockpit Emergency
- Sports Agency & Free Agency
- Haute Couture Fashion
- Crisis PR Management
- Luxury Real Estate
"""
import sys
import os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_batch2_scenarios():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [
            make_turn(t[0], t[1], t[2], t[3], t[4], t[5])
            for t in turns_data
        ]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # -------------------------------------------------------------
    # 7. FBI Criminal Profiling
    # -------------------------------------------------------------
    data["FBI Criminal Profiling"] = [
        mk_ep(
            "연쇄살인범 취조실: 묵비권을 무너뜨리는 프로파일링",
            "Special Agent Holden (BAU Profiler)", "🔍",
            "콴티코 FBI 행동분석팀(BAU). 8건의 연쇄 실종 사건의 유일한 용의자가 취조실에서 미소를 띠며 묵비권을 행사하고 있다. 심리적 방어기제를 무너뜨리고 유골 매장지를 밝혀내야 한다.",
            "exploit the narcissistic behavioral leakage",
            "용의자의 오만함을 역이용해 무의식적인 행동 누출(leakage)을 유도하고 자백을 이끌어낼 때 쓰는 프로파일링 전문 표현입니다.",
            [
                (
                    "The suspect has been stone-faced for six hours. The local detectives want to play good-cop-bad-cop. What's our psychological angle?",
                    "용의자가 6시간째 돌부처처럼 버티고 있어. 현지 형사들은 착한 경찰 나쁜 경찰 놀이를 하자는데, 우리의 심리학적 공략 포인트가 뭐야?",
                    "통상적인 취조 대신 용의자의 천재성과 예술적 치밀함을 인정해 우월감을 자극하자고 제안하세요.",
                    ("Standard interrogation won't work on an organized psychopath. We feed his god complex, validate his meticulous craft, and let his ego spill the crime scenes.", "일반적인 취조는 조직화된 사이코패스에게 통하지 않습니다. 그의 전능 콤플렉스를 부추기고 치밀함을 칭찬해, 오만함에 취해 스스로 범행 현장을 털어놓게 만듭니다.", "‘feed his god complex’와 ‘organized psychopath’는 미드 마인드헌터의 백미인 프로파일링 기법입니다."),
                    ("Let's scream loudly at him so he gets scared.", "그에게 크게 소리를 질러서 겁을 줍시다.", "조직적 범죄자의 폐쇄성을 강화하는 하책입니다."),
                    ("Tell him to sign the confession paper quickly.", "자백 종이에 빨리 사인하라고 재촉합시다.", "‘sign’은 콩글리시입니다.")
                ),
                (
                    "He flinched when you mentioned the riverbank. But he won't give up the exact GPS coordinates without a deal off death row.",
                    "강둑을 언급했을 때 미세하게 움찔했어. 하지만 사형 면제 합의 없이는 정확한 GPS 좌표를 불지 않으려 해.",
                    "협상은 불가능하며 시신을 찾지 못하면 그의 걸작이 영원히 묻힌다고 그의 자존심을 벼랑 끝으로 몰아가세요.",
                    ("We don't bargain with predators. If the bodies aren't recovered, history will view him as a sloppy amateur who panicked.", "우리는 포식자와 거래하지 않습니다. 시신이 수습되지 않으면 세상은 당신을 공황에 빠진 서툰 아마추어로 기억할 뿐이라고 자극하십시오.", "‘bargain with predators’와 ‘sloppy amateur’는 나르시시스트를 압박하는 결정적 타격입니다."),
                    ("Maybe we can ask the governor to give him life in prison instead.", "주지사에게 사형 대신 무기징역을 줄 수 있는지 알아볼 수도 있습니다.", "수사관으로서 주도권을 상실하는 약한 모습입니다."),
                    ("Let's promise him delicious cider in jail.", "교도소에서 맛있는 사이다를 주겠다고 약속합시다.", "‘cider’는 콩글리시입니다.")
                ),
                (
                    "He cracked! He drew the exact coordinates on the map. Search-and-rescue just recovered the missing victims. Outstanding behavioral analysis, agent.",
                    "입을 열었어! 지도 위에 정확한 좌표를 그렸네. 수색구조팀이 방금 실종 피해자들을 찾았어. 특급 행동 분석이었네, 요원.",
                    "정의는 과학과 인간 본성에 대한 깊은 통찰에서 시작된다고 담담히 화답하세요.",
                    ("Justice doesn't rely on luck, sir—it rests on decoding the darkness within human nature.", "정의는 운에 기댈 수 없습니다, 팀장님. 인간 본성 속 어둠을 해독해낼 때 비로소 완성됩니다.", "FBI 프로파일러의 무게감을 드러내는 멋진 마무리입니다."),
                    ("I am glad we can finally go to sleep now.", "이제 드디어 잠을 잘 수 있어서 기쁩니다.", "프로다운 긴장감이 아쉬운 답변입니다."),
                    ("Let's do Dutch pay for the Quantico pizza.", "콴티코 피자는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "모방 연쇄범의 시그니처: 원조 살인마와의 밀실 인터뷰",
            "Special Agent Holden (BAU Profiler)", "🔍",
            "연방 최고보안 교도소 지하 독방. 20년 전 연쇄살인마의 미공개 범행 시그니처를 그대로 모방한 카피캣이 등장했다. 수감된 원조 범죄자의 지적 허영심을 자극해 다음 타깃을 특정해야 한다.",
            "decode the evolutionary signature of the copycat",
            "모방범이 진화시킨 범행 시그니처를 분석할 때 쓰는 프로파일링 전문 표현입니다.",
            [
                (
                    "The prisoner refuses to speak unless we grant him outside yard privileges and unmonitored mail. Do we grant concessions?",
                    "수감자가 야외 운동 시간과 검열 없는 우편 특권을 주지 않으면 입을 열지 않겠다고 버텨. 요구를 들어줄까?",
                    "요구를 일축하고 그의 완벽한 범행을 모방범이 조롱하고 훼손하고 있다는 점을 각인시키세요.",
                    ("No concessions. Remind him that this copycat is bastardizing his original masterpiece and stealing his legacy.", "특혜는 없습니다. 모방범이 그의 원작 걸작을 조잡하게 왜곡하고 그의 유산을 가로채고 있다는 점을 각인시키십시오.", "‘bastardizing his masterpiece’는 나르시시스트 범죄자의 질투심을 폭발시키는 킬러 프레이즈입니다."),
                    ("Let us give him what he wants so he talks fast.", "그가 원하는 걸 주고 빨리 말하게 만듭시다.", "범죄자에게 휘둘리는 치명적 실수입니다."),
                    ("We can give him some nice service in prison.", "교도소에서 그에게 좋은 서비스를 좀 줄 수 있습니다.", "‘service’는 콩글리시입니다.")
                ),
                (
                    "His ego couldn't take it. He pointed out that the ligature knot is tied left-handed, unlike his own knot. That cuts our suspect pool by ninety percent.",
                    "자존심이 무너졌군. 밧줄 매듭이 자신과 달리 왼손잡이 방식으로 묶였다는 점을 지적했어. 용의자 후보군이 90% 줄어들었네.",
                    "왼손잡이 외과의 출신 용의자의 최근 이동 반경을 즉시 교차 검증하자고 하세요.",
                    ("Cross-reference left-handed trauma surgeons within a fifty-mile radius of the secondary dump site immediately.", "2차 유기 현장 반경 50마일 이내의 왼손잡이 외상외과 의사들을 즉시 교차 대조하십시오.", "‘cross-reference’와 ‘secondary dump site’는 과학 수사의 정석 표현입니다."),
                    ("I will call many hospitals and ask if they have left-handed doctors.", "여러 병원에 전화해서 왼손잡이 의사가 있는지 물어보겠습니다.", "비효율적이고 아마추어적인 접근입니다."),
                    ("Let's send an SNS message to the suspects.", "용의자들에게 SNS 메시지를 보냅시다.", "‘SNS’는 콩글리시입니다.")
                ),
                (
                    "Suspect in custody! The search warrant turned up the left-handed surgical instruments. You outsmarted two monsters in one day.",
                    "용의자 체포 완료! 압수수색 영장 집행으로 왼손잡이 수술 도구를 확보했어. 자네가 오늘 하루 두 명의 괴물을 압도했네.",
                    "괴물과 싸울 때조차 우리는 인간성을 잃지 않는 법을 배웠다고 답하세요.",
                    ("When you stare into the abyss, Holden, you make sure the abyss flinches first.", "심연을 들여다볼 때, 심연이 먼저 눈을 깜빡이게 만들어야 합니다, 홀든 요원.", "니체의 격언을 멋지게 인용한 프로파일러의 철학적 승리 선언입니다."),
                    ("I am very happy the work was finished successfully.", "일이 성공적으로 끝나서 참 기쁩니다.", "평이하고 감동이 덜한 소감입니다."),
                    ("Let's have a party with morning call tomorrow.", "내일 모닝콜 맞춰놓고 파티합시다.", "‘morning call’은 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "군중 속의 저격수: 지리적 프로파일링(Geographic Profiling)",
            "Special Agent Holden (BAU Profiler)", "🔍",
            "워싱턴 D.C. 도심 주유소 연쇄 저격 사건. 시민들의 공포가 극에 달한 가운데, 범행 장소들의 공간적 분포를 수학적으로 역추적해 저격수의 은신처 반경을 좁혀야 한다.",
            "pinpoint the geographic anchor point of the sniper",
            "연쇄 범죄자의 이동 반경과 은신처 중심점(앵커 포인트)을 역추적할 때 쓰는 지리적 프로파일링 용어입니다.",
            [
                (
                    "Four shootings across three highways in forty-eight hours. The media is calling him the Phantom. The Director wants roadblocks everywhere.",
                    "48시간 동안 3개 고속도로에서 4건의 총격이 발생했어. 언론은 유령이라 부르고 국장은 전 도로 봉쇄를 원해.",
                    "무차별 봉쇄는 패닉만 키우므로 이동 시간과 버퍼존(Buffer Zone)을 분석해 주거 앵커 포인트를 찾아내자고 하세요.",
                    ("Roadblocks will cause mass paralysis. We apply Rossmo's formula to map the criminal buffer zone and isolate his geographic anchor point.", "도로 봉쇄는 대규모 마비만 부릅니다. 로스모 공식을 적용해 범죄 버퍼존을 매핑하고 그의 지리적 주거 앵커 포인트를 분리해내야 합니다.", "‘Rossmo's formula’와 ‘geographic anchor point’는 지리적 프로파일링의 정수입니다."),
                    ("Let's close all gas stations until we find the shooter.", "저격수를 찾을 때까지 모든 주유소를 폐쇄합시다.", "도시 전체를 패닉에 빠뜨리는 무리수입니다."),
                    ("We can tell citizens to wear safe sharp clothes.", "시민들에게 안전하고 날렵한 옷을 입으라고 공지합시다.", "‘sharp’는 콩글리시입니다.")
                ),
                (
                    "The spatial model narrowed the heat map down to a four-block industrial corridor in Silver Spring. But there are over two hundred warehouses.",
                    "공간 모델이 실버 스프링의 4블록 산업 회랑으로 열 지도를 좁혔어. 하지만 창고가 200개가 넘어.",
                    "저격수가 사용한 탄약 보관용 항온 창고와 최근 렌터카 트럭 임대 기록을 결합 대조하자고 하세요.",
                    ("Filter for climate-controlled storage units leased to commercial box trucks within the last fourteen days.", "지난 14일 이내에 박스 트럭용으로 임대된 항온 항습 보관 유닛들을 즉시 필터링하십시오.", "‘climate-controlled storage’와 ‘box trucks’는 저격 차량을 적중시키는 날카로운 수사 지시입니다."),
                    ("We will knock on every door one by one until night.", "밤까지 문을 하나하나 두드려 보겠습니다.", "시간이 생명인 상황에서 너무 느린 방법입니다."),
                    ("Let's check the handphone location of all workers.", "모든 노동자들의 핸드폰 위치를 체크합시다.", "‘handphone’은 콩글리시입니다.")
                ),
                (
                    "Sniper truck located! SWAT breached the warehouse and secured the modified trunk perch before he could fire again. You saved countless lives.",
                    "저격 트럭 발견! SWAT이 창고를 급습해 개조된 트렁크 저격대를 확보했어. 다음 발사를 막았네. 수많은 목숨을 구했어.",
                    "데이터와 인간 행동 심리학이 결합할 때 보이지 않는 범죄자도 그림자를 드러낸다고 답하세요.",
                    ("When behavioral psychology meets rigorous data, no predator remains invisible.", "행동 심리학이 정밀한 데이터와 만날 때, 그 어떤 포식자도 보이지 않는 곳에 숨을 수 없습니다.", "지성과 과학 수사의 승리를 보여주는 멋진 결말입니다."),
                    ("I am glad we don't have to work overtime tonight.", "오늘 밤 야근 안 해도 돼서 다행입니다.", "사명감이 부족하게 느껴집니다."),
                    ("Let's do Dutch pay for the celebration dinner.", "축하 저녁은 더치페이로 합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "청문회 증언: 프로파일링 과학성의 연방 법정 증명",
            "Special Agent Holden (BAU Profiler)", "🔍",
            "연방 항소법원. 피고인 측 변호인단이 BAU의 프로파일링을 '사이비 마술'이라며 증거 배제 신청을 제기했다. 다우버트 기준(Daubert Standard)에 입각해 과학적 신뢰성을 입증해야 한다.",
            "satisfy the Daubert standard of scientific reliability",
            "법정에서 과학적 증거의 엄격한 신뢰성 기준을 충족시킬 때 쓰는 법률 전문 표현입니다.",
            [
                (
                    "Defense counsel is claiming our behavioral analysis is speculative junk science with no empirical foundation. How do you counter their expert?",
                    "변호인이 우리의 행동 분석이 실증적 근거가 없는 추측성 유사 과학이라고 공격하고 있어. 상대 감정인을 어떻게 제압할 건가?",
                    "20년간 5천 건의 연쇄 범죄 실증 데이터베이스와 동료 평가 학술 검증을 제시해 다우버트 기준을 충족시키겠다고 하세요.",
                    ("We present our twenty-year empirical database of five thousand cases, proving peer-reviewed error rates that satisfy every Daubert criteria.", "5천 건의 20년 실증 데이터베이스와 동료 평가 오류율을 제시해 다우버트 기준을 완벽히 충족시키겠습니다.", "‘peer-reviewed error rates’와 ‘Daubert criteria’는 미국 법정에서 과학적 증거의 절대성을 증명하는 용어입니다."),
                    ("Tell the judge that our FBI agents are very smart people.", "판사에게 우리 FBI 요원들이 아주 똑똑한 사람들이라고 말하겠습니다.", "주관적 자화자찬으로 법적 설득력이 없습니다."),
                    ("Our agents have very good spec so we are never wrong.", "우리 요원들은 스펙이 아주 좋아서 절대 틀리지 않습니다.", "‘spec’은 콩글리시입니다.")
                ),
                (
                    "The defense is cross-examining you on false-positive rates. They're trying to bait you into an emotional outburst. Hold the line.",
                    "변호인이 위양성(False-positive) 비율을 물고 늘어지며 당신의 감정적 폭발을 유도하고 있어. 침착하게 중심을 잡아.",
                    "도발에 휘말리지 않고 통계적 유의미성과 다중 수사 단서 교차 검증 원칙을 정밀하게 진술하세요.",
                    ("I do not speculate, counsel. Behavioral profiling generates investigative leads; forensic physical evidence confirms them. The science is unimpeachable.", "변호인, 저는 추측하지 않습니다. 행동 프로파일링은 수사 단서를 제공하고, 물리적 법의학 증거가 이를 입증합니다. 이 과학은 흠잡을 데 없습니다.", "‘unimpeachable’은 법정에서 상대의 공격을 원천 무력화하는 최고 수준의 증언 표현입니다."),
                    ("Please stop asking me annoying questions in court.", "법정에서 짜증 나는 질문 좀 그만하세요.", "감정을 억제하지 못해 신빙성을 잃는 최악의 반응입니다."),
                    ("I prepared a nice ment for the jury so listen to me.", "배심원을 위해 좋은 멘트를 준비했으니 제 말을 들으세요.", "‘ment’는 콩글리시입니다.")
                ),
                (
                    "Motion denied! The judge ruled our profiling evidence fully admissible under Federal Rule 702. The jury convicted on all thirty counts.",
                    "기각 신청 기각! 판사가 연방 증거법 제702조에 따라 프로파일링 증거 능력을 전면 인정했어. 배심원이 30개 혐의 전원 유죄 평결을 내렸네.",
                    "정의는 흔들리지 않는 원칙 위에 세워질 때 영원하다고 답하세요.",
                    ("When science serves justice with unyielding discipline, truth will always prevail.", "과학이 흔들리지 않는 규율로 정의를 받들 때, 진실은 언제나 승리합니다.", "FBI 법정 증언의 품격을 완성하는 명대사입니다."),
                    ("I am glad the trial did not take until next week.", "재판이 다음 주까지 안 끌려서 다행입니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                    ("Let's go drink beer and do Dutch pay tonight.", "오늘 밤 맥주 마시러 가서 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 8. White House Politics
    # -------------------------------------------------------------
    data["White House Politics"] = [
        mk_ep(
            "자정의 비상 안보회의: 대서양 해저 케이블 절단 위기",
            "President Underwood (Chief of Staff)", "🏛️",
            "백악관 웨스트윙 지하 상황실. 대서양 횡단 금융 통신 케이블 3개가 의문의 잠수정에 의해 절단되었다. 월스트리트 개장 6시간 전, 전면적 보복과 비밀 외교 사이에서 대통령의 결단을 이끌어야 한다.",
            "maintain proportional deterrence without triggering hot war",
            "전면전을 피하면서도 적국에 비례적 억제력을 각인시킬 때 쓰는 백악관 외교 안보 전문 표현입니다.",
            [
                (
                    "Wall Street opens in six hours. If international clearing houses stay blind, the dollar collapses by thirty percent. The Pentagon wants airstrikes on their naval base.",
                    "월스트리트 개장까지 6시간 남았어. 국제 결제망이 먹통인 채로 개장하면 달러화가 30% 폭락해. 펜타곤은 적 해군 기지 폭격을 요구하고 있네.",
                    "물리적 폭격은 확전을 부르므로 사이버 사령부의 비대칭 금융 보복 카드를 가동하자고 제안하세요.",
                    ("Air strikes invite world war, Mr. President. We unleash Cyber Command on their sovereign sovereign wealth accounts and freeze their offshore liquidity within sixty seconds.", "공습은 세계대전을 촉발합니다, 각하. 사이버 사령부를 가동해 적국의 국부펀드 계좌를 타격하고 60초 안에 해외 유동성을 동결시켜야 합니다.", "‘Cyber Command’와 ‘freeze offshore liquidity’는 확전 없이 숨통을 조이는 최고위 안보 전략입니다."),
                    ("Let us ask them politely to fix the internet cables.", "인터넷 케이블을 고쳐달라고 공손히 부탁합시다.", "국가 원수 참모로서 나약하기 짝이 없는 발언입니다."),
                    ("Our internet spec is bad so let's call AS.", "우리 인터넷 스펙이 안 좋으니 AS를 부릅시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")
                ),
                (
                    "Their ambassador is on the secure red line. He denies all involvement and claims it was an accidental civilian fishing trawler. What's our retort?",
                    "적국 대사가 비화 핫라인에 연결되었어. 개입 사실을 전면 부인하며 민간 어선의 우발적 사고라고 오리발을 내밀고 있네. 반격 답변이 뭐야?",
                    "위성 음파 탐지 기록을 제시하며 30분 내 케이블 복구 잠수정을 철수하지 않으면 전면 금융 제재를 단행하겠다고 통보하세요.",
                    ("Inform him that satellite sonar signatures confirm their nuclear attack sub. They have thirty minutes to recall their submersible or face total financial quarantine.", "위성 소나 시그니처가 적 핵추진 잠수정임을 입증했다고 통보하십시오. 30분 안에 특수 잠수정을 철수시키지 않으면 전면 금융 격리에 직면할 것입니다.", "‘satellite sonar signatures’와 ‘total financial quarantine’은 거짓말을 분쇄하는 압도적 외교 화법입니다."),
                    ("Tell him that lying to the President is very rude.", "대통령에게 거짓말하는 것은 무례한 짓이라고 말하세요.", "외교적 레버리지가 없는 유치한 훈계입니다."),
                    ("Let's send an SNS post to shame their president.", "적국 대통령을 망신주기 위해 SNS 글을 올립시다.", "‘SNS’는 콩글리시입니다.")
                ),
                (
                    "Submersible recalled! Repair ships are already splicing the fiber lines. Global financial markets are saved before the opening bell. You held the republic together.",
                    "잠수정 철수 확인! 복구선이 이미 광케이블 재연결 작업에 들어갔어. 개장 종이 울리기 전에 글로벌 금융 시장을 구했네. 자네가 공화국을 지켜냈어.",
                    "진정한 권력은 무력을 과시하는 것이 아니라 사용하지 않고도 상대를 굴복시키는 것이라고 답하세요.",
                    ("Supreme power isn't about firing missiles, sir—it's knowing you hold the trigger and compelling peace without a shot.", "최고의 권력은 미사일을 쏘는 데 있지 않습니다, 각하. 방아쇠를 쥐고 있음을 보여줌으로써 총성 없이 평화를 강제하는 것입니다.", "하우스 오브 카드의 깊은 정치 철학을 담은 명대사입니다."),
                    ("I am glad I can go home and eat breakfast.", "집에 가서 아침밥 먹을 수 있어서 기쁩니다.", "역사적 승리의 순간에 긴장을 지나치게 풉니다."),
                    ("Let's do Dutch pay for the White House coffee.", "백악관 커피는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "대통령 탄핵안 표결 2시간 전: 상원의원 스윙보트 확보전",
            "President Underwood (Chief of Staff)", "🏛️",
            "워싱턴 의사당. 야당의 탄핵 소추안 표결을 앞두고 운명을 가를 3명의 중립 성향 상원의원이 결정을 미루고 있다. 백악관 비서실장으로서 그들의 지역구 예산과 정치적 명분을 쥐고 표를 결집시켜야 한다.",
            "whip the undecided votes before the roll call",
            "호명 투표 직전 미결정 의원들의 표를 완벽히 단속해 결집할 때 쓰는 의회 정치 전문 표현입니다.",
            [
                (
                    "Senator Sterling from Ohio holds the deciding vote. He refuses to take the President's call unless we promise a two-billion federal highway earmark for his state.",
                    "오하이오의 스털링 상원의원이 캐스팅보트를 쥐고 있어. 자기 주에 20억 달러 고속도로 특별예산을 배정하지 않으면 대통령 전화를 안 받겠대.",
                    "예산안 서명을 레버리지로 삼되 법안 통과 당일 즉시 행정명령으로 묶어둘 테니 표결에서 찬성표를 던지라고 압박하세요.",
                    ("Tell Sterling he gets his infrastructure funding only after his affirmative vote is entered into the congressional record. No votes, no asphalt.", "스털링 의원에게 의회 기록에 찬성표가 등재된 후에만 인프라 예산이 집행될 것이라고 통보하십시오. 표가 없으면 아스팔트도 없습니다.", "‘No votes, no asphalt’는 워싱턴 의회 협상의 뼈를 때리는 명언입니다."),
                    ("Let us give him all the money he asks for right away.", "그가 요구하는 모든 돈을 지금 당장 줍시다.", "백악관의 권위를 실추시키고 끝없는 요구를 부릅니다."),
                    ("Senator Sterling has bad manner so let's complain to him.", "스털링 의원은 매너가 나쁘니 그에게 항의합시다.", "‘manner’는 콩글리시입니다.")
                ),
                (
                    "Sterling is leaning toward voting no. The opposition leader just offered him the chairmanship of the Senate Appropriations Committee.",
                    "스털링이 반대표로 기울고 있어. 야당 원내대표가 그에게 상원 세출위원장 자리를 제안했네.",
                    "그의 과거 선거자금 비공개 로비 장부를 테이블에 올리고 정치적 생명이 끝날 수 있음을 경고하세요.",
                    ("Slide his pac-finance ledger across the desk. Remind him the Justice Department has jurisdiction over undisclosed offshore campaign donations.", "그의 선거자금 장부를 책상 위로 밀어 넣으십시오. 미신고 해외 후원금에 대한 법무부 수사권이 살아있음을 상기시키세요.", "‘pac-finance ledger’와 ‘undisclosed campaign donations’는 정적을 무릎 꿇리는 강력한 레버리지입니다."),
                    ("We can cry and tell him the President is a good person.", "울면서 대통령님이 좋은 사람이라고 말해봅시다.", "정치적 현실 감각이 전무한 순진한 태도입니다."),
                    ("Please check your handphone for the vote count.", "표 계산을 위해 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")
                ),
                (
                    "The gavel struck! The impeachment article failed by one single vote: Sterling voted with the President! The administration survives.",
                    "의사봉이 울렸어! 탄핵안이 단 한 표 차로 부결되었네. 스털링이 대통령 편에 표를 던졌어! 정권이 살아남았네.",
                    "정치는 감정이 아닌 냉혹한 수 싸움이며 공화국의 권력은 여전히 우리 손에 있다고 선언하세요.",
                    ("In this town, loyalty isn't bought with kindness—it's forged in cold, calculated leverage. We live to rule another day.", "이 도시에서 충성은 온정으로 사는 것이 아닙니다. 냉혹하고 치밀한 레버리지로 벼려내는 것입니다. 우리는 통치하기 위해 다시 살아남았습니다.", "워싱턴 정계의 냉혹한 본질을 꿰뚫는 마키아벨리적 피날레입니다."),
                    ("I am very tired and want to take tomorrow off.", "너무 피곤해서 내일 쉬고 싶습니다.", "승리의 성취감을 만끽하지 못하는 답변입니다."),
                    ("Let's do Dutch pay for the victory champagne.", "승리의 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "대통령 연두교서(State of the Union) 원고 수정 30분 전",
            "President Underwood (Chief of Staff)", "🏛️",
            "의회 합동회의장 입장 30분 전. 대통령의 연두교서 초안에 중산층 의료보험 개혁안을 전격 포함할지를 두고 정책실장과 재무장관이 정면충돌한다. 전 국민 생중계 연설의 역사적 승부수를 던져야 한다.",
            "deliver the defining policy doctrine of the presidency",
            "정권의 역사적 정체성을 규정하는 핵심 국정 철학을 선포할 때 쓰는 표현입니다.",
            [
                (
                    "Treasury warns that announcing universal healthcare coverage will trigger a bond market rebellion. Do we water down the speech or push all-in?",
                    "재무부는 전 국민 의료보장제 발표가 국채 시장의 반발을 부를 거라 경고해. 연설 수위를 낮출까, 아니면 올인할까?",
                    "타협은 레임덕을 부를 뿐이므로 정면 돌파로 국민적 지지를 결집해 시장을 압도하자고 하세요.",
                    ("Watering down the doctrine is political suicide. We go all-in. Frame healthcare not as an entitlement, but as an indispensable pillar of national economic defense.", "철학을 희석하는 것은 정치적 자살입니다. 올인하십시오. 의료보장을 복지 혜택이 아닌 국가 경제 안보의 필수 기둥으로 프레이밍해야 합니다.", "‘water down the doctrine’과 ‘indispensable pillar’는 여론의 주도권을 장악하는 고급 정치 화법입니다."),
                    ("Let's make the speech very short and say nothing controversial.", "논란거리가 없도록 연설을 아주 짧게 만듭시다.", "국정 연설의 영향력을 스스로 깎아먹는 태도입니다."),
                    ("Let us have skinship with the opposition party members.", "야당 의원들과 스킨십을 나눕시다.", "‘skinship’은 콩글리시입니다.")
                ),
                (
                    "The teleprompter operator is asking for the final lock on line forty-two. The opposition plans to remain seated in protest. What's the killer applause hook?",
                    "프롬프터 기사가 42번 문장의 최종 승인을 요구하고 있어. 야당은 침묵 시위를 계획 중이야. 기립박수를 이끌어낼 킬러 훅 문장이 뭐야?",
                    "정파적 분열을 뛰어넘어 환자 가족들의 눈물을 언급하며 양심에 호소하는 펀치라인을 넣자고 하세요.",
                    ("Insert this: 'Cancer doesn't check party registration before it strikes an American family.' Watch every senator in that chamber stand up.", "이 문장을 넣으십시오. '암세포는 미국 가정을 덮칠 때 당적을 확인하지 않습니다.' 본회의장의 모든 상원의원이 기립하는 모습을 보게 될 것입니다.", "정치적 반대파까지 침묵시키고 기립박수를 유도하는 불후의 명문장입니다."),
                    ("Tell the congressmen that they will be punished if they don't clap.", "박수를 치지 않으면 처벌받을 것이라고 의원들에게 경고합시다.", "민주주의 의회를 위협하는 독재적 발언입니다."),
                    ("I prepared a good ment for the television cameras.", "텔레비전 카메라를 위해 좋은 멘트를 준비했습니다.", "‘ment’는 콩글리시입니다.")
                ),
                (
                    "Standing ovation across both sides of the aisle! The cable networks are calling it the greatest State of the Union in modern history. The polls surged sixteen points.",
                    "양당 모두에서 기립박수가 터졌어! 케이블 방송들은 현대사 최고의 연두교서라고 평가하고 있네. 지지율이 16% 급등했어.",
                    "말은 권력의 시작이지만 실행만이 역사를 바꾼다며 입법 속도전을 지시하세요.",
                    ("Rhetoric won the evening, sir; execution secures the history books. Cue the bill sponsors—we vote before midnight tomorrow.", "수사학이 오늘 밤을 승리로 이끌었지만, 역사를 쓰는 것은 실행입니다. 법안 발의 의원들을 소집하십시오. 내일 자정 전에 표결에 부칩니다.", "승리에 안주하지 않고 입법 성과로 직결시키는 최고의 참모 화법입니다."),
                    ("I am happy we can drink beer now.", "이제 맥주를 마실 수 있어서 기쁩니다.", "국정 운영의 무게에 걸맞지 않은 답변입니다."),
                    ("Let's do Dutch pay for the White House victory dinner.", "백악관 축하 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "대법관 후보자 지명 청문회 낙마 위기 돌파",
            "President Underwood (Chief of Staff)", "🏛️",
            "백악관 오벌 오피스. 대통령이 지명한 최초의 소수계 여성 대법관 후보자에 대해 야당이 과거 로펌 수임료 의혹을 제기하며 지명 철회를 요구한다. 지명을 관철하고 헌법의 수호자를 세워야 한다.",
            "stand resolute behind the judicial nominee",
            "정치적 공격 속에서도 사법부 후보자를 확고부동하게 수호할 때 쓰는 표현입니다.",
            [
                (
                    "The Senate Judiciary chairman gave us an ultimatum: withdraw Judge Vance's nomination by 5 PM or they'll release a smear dossier on her family.",
                    "상원 사법위원장이 최후통첩을 보냈어. 오후 5시까지 밴스 판사 지명을 철회하지 않으면 가족에 대한 흑색선전 파일을 공개하겠대.",
                    "협박에 굴복하지 말고 특별 기자회견을 열어 야당의 치졸한 공작을 국민 앞에 폭로하자고 하세요.",
                    ("We do not yield to extortion. Call a prime-time press briefing. We bring Judge Vance into the Rose Garden and expose their smear campaign on national television.", "우리는 협박에 굴복하지 않습니다. 황금시간대 기자회견을 소집하십시오. 밴스 판사를 로즈가든에 세우고 전 국민 생중계로 그들의 공작을 폭로하겠습니다.", "‘yield to extortion’과 ‘expose smear campaign’은 정면 돌파로 상대를 무력화하는 고수들의 화법입니다."),
                    ("Let's withdraw her name quietly so we don't get hurt.", "우리가 다치지 않게 그녀의 이름을 조용히 철회합시다.", "지도자의 신의를 저버리고 약점을 잡히는 행위입니다."),
                    ("Senator has bad personality so let's claim to his mom.", "상원의원 인성이 나쁘니 그의 어머니에게 클레임합시다.", "‘claim’은 콩글리시입니다.")
                ),
                (
                    "The press conference turned the tide. But two moderate senators want to see her tax returns before voting to confirm.",
                    "기자회견이 여론을 바꿨어. 하지만 중도 성향 상원의원 두 명이 인준 투표 전에 그녀의 10년 치 세금 환급 내역을 보자고 요구해.",
                    "모든 금융 내역을 투명하게 의회 열람실에 공개하여 어떤 흠결도 없음을 쐐기 박자고 하세요.",
                    ("Deliver unredacted tax disclosures to the Senate secure reading room within the hour. Total transparency disarms their final defense.", "한 시간 안에 모든 세금 공개 자료를 상원 비공개 열람실에 전달하십시오. 완전한 투명성은 상대의 마지막 방어선을 무력화합니다.", "‘unredacted tax disclosures’와 ‘total transparency disarms’는 논란을 잠재우는 완벽한 전략입니다."),
                    ("Tell them looking at taxes is very impolite.", "세금을 들여다보는 것은 대단히 무례하다고 전하세요.", "의혹을 키우는 부적절한 대처입니다."),
                    ("Please check the handphone for IRS data.", "국세청 데이터를 위해 핸드폰을 확인하세요.", "‘handphone’은 콩글리시입니다.")
                ),
                (
                    "Confirmed fifty-two to forty-eight! Justice Vance is taking the constitutional oath on the South Lawn right now. You reshaped the Supreme Court.",
                    "52대 48로 인준 통과! 밴스 대법관이 지금 사우스론에서 헌법 수호 선서를 하고 있어. 자네가 연방 대법원의 지형을 바꿨네.",
                    "헌법은 권력자의 도구가 아니라 국민의 자유를 지키는 방패라고 화답하세요.",
                    ("Presidents come and go, sir, but the Constitution endures. Today, we placed justice in the hands of an incorruptible guardian.", "대통령은 왔다가 가지만, 헌법은 영원합니다, 각하. 오늘 우리는 불굴의 수호자에게 정의의 칼을 쥐여주었습니다.", "국가적 승리를 헌법적 가치로 승화시키는 감동적인 대사입니다."),
                    ("I am happy we won the points today.", "오늘 점수를 따서 기쁩니다.", "대법관 임명의 숭고한 의미를 살리지 못합니다."),
                    ("Let's do Dutch pay for the party cake.", "파티 케이크는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    # -------------------------------------------------------------
    # 9. Michelin Culinary
    # -------------------------------------------------------------
    data["Michelin Culinary"] = [
        mk_ep(
            "미슐랭 3스타 암행 평가원의 기습 방문: 메인 코스의 온도 붕괴",
            "Chef Marco (Executive Head Chef)", "🔪",
            "시카고 최고급 파인다이닝 레스토랑의 디너 피크타임. 미슐랭 암행 평가원이 VIP 4번 테이블에 착석한 순간, 수비드 양갈비 소테 팬의 버터 온도가 분리되며 위기가 찾아왔다. 주방의 규율을 다잡고 완벽한 한 접시를 내야 한다.",
            "emulsify the reduction sauce under extreme heat",
            "극도의 화력 속에서 소스를 분리되지 않게 완벽한 유화 상태로 완성할 때 쓰는 파인다이닝 조리 전문 표현입니다.",
            [
                (
                    "Table Four just ordered the tasting menu. It's the chief Michelin inspector from Paris! The duck breast sauce just broke on station two! Do we scrape and fire again?",
                    "4번 테이블이 테이스팅 메뉴를 주문했어. 파리 본부의 수석 미슐랭 평가원이야! 2번 스테이션 오리 가슴살 소스가 분리되었어! 버리고 다시 볶을까?",
                    "버리지 말고 차가운 버터 큐브를 투입해 유화시키면서 새 가니시를 45초 안에 올려 플레이팅을 구출하자고 하세요.",
                    ("Don't dump it! Whisk in cold butter cubes off the heat to rescue the emulsion, and fire fresh micro-herbs. Table Four gets perfection in forty seconds!", "버리지 마세요! 불 끄고 차가운 버터 큐브를 휘핑해 유화 상태를 살려내고, 신선한 마이크로 허브를 올리세요. 4번 테이블에 40초 안에 완벽한 접시를 냅니다!", "‘rescue the emulsion’과 ‘whisk in cold butter’는 파인다이닝 키친의 위기를 구하는 최고 셰프의 언어입니다."),
                    ("Just wipe the sauce and serve it quickly.", "소스를 대충 닦아내고 빨리 서빙하세요.", "평가원에게 퇴출당하는 치명적인 실수입니다."),
                    ("The butter has bad spec so call the mart.", "버터 스펙이 안 좋으니 마트에 전화합시다.", "‘spec’은 콩글리시입니다.")
                ),
                (
                    "The duck is out. Now the inspector is asking the sommelier for an unlisted vintage pairing. He's testing our cellar depth.",
                    "오리는 나갔어. 그런데 평가원이 소믈리에에게 메뉴판에 없는 올드 빈티지 페어링을 요구하고 있어. 우리 와인 셀러의 깊이를 시험하는 거야.",
                    "1998년산 바롤로 리제르바를 오픈 디캔팅하여 요리의 트러플 풍미와 완벽한 조화를 선사하자고 지시하세요.",
                    ("Pull the 1998 Barolo Riserva from the reserve locker. Double-decant it immediately. The tertiary truffle notes will complement the duck reduction flawlessly.", "예비 락커에서 1998년산 바롤로 리제르바를 꺼내오세요. 즉시 2중 디캔팅하십시오. 제3의 트러플 향이 오리 소스와 완벽한 조화를 이룰 것입니다.", "‘double-decant’와 ‘tertiary truffle notes’는 미슐랭 3스타의 품격을 보여주는 환상적인 페어링 지시입니다."),
                    ("Give him regular house wine and say it is expensive.", "일반 하우스 와인을 주고 비싼 거라고 거짓말하세요.", "미슐랭 평가원의 미각을 속일 수 없습니다."),
                    ("Let's give him a one-plus-one wine coupon.", "그에게 원플러스원 와인 쿠폰을 줍시다.", "‘one-plus-one’은 콩글리시입니다.")
                ),
                (
                    "Service concluded! The inspector cleaned every plate, stood up, and bowed to the open kitchen! We just locked in three stars for next year!",
                    "서비스 종료! 평가원이 모든 접시를 비우고 일어나 오픈 키친을 향해 고개 숙여 인사했어! 내년 미슐랭 3스타를 확정 지었네!",
                    "요리는 기술이 아니라 접시 위에 담긴 영혼의 진실성이라고 자축하세요.",
                    ("Three stars aren't given for perfection alone, Marco—they are earned when heart and discipline bleed into every single bite.", "3스타는 완벽함만으로 주어지지 않습니다, 마르코. 규율과 열정이 모든 한 입에 스며들 때 비로소 얻어지는 것입니다.", "미슐랭 3스타 셰프다운 감동적인 철학적 찬사입니다."),
                    ("I am glad I can sit on a chair now.", "이제 의자에 앉을 수 있어서 기쁩니다.", "성취의 감동을 반감시키는 답변입니다."),
                    ("Let's do Dutch pay for the kitchen beer.", "주방 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "스타 셰프와 부주방장(Sous Chef)의 전쟁: 시그니처 메뉴 파업",
            "Chef Marco (Executive Head Chef)", "🔪",
            "뉴욕 센트럴파크 앞 미슐랭 2스타 레스토랑. 토요일 밤 만석 디너 10분 전, 수셰프가 처우 개선을 요구하며 조리 라인 파업을 선언했다. 주방의 리더십을 증명하고 혼자서라도 서비스를 완주해야 한다.",
            "command the kitchen line through sheer culinary mastery",
            "압도적인 조리 실력과 카리스마로 흔들리는 주방 라인을 완전히 장악할 때 쓰는 표현입니다.",
            [
                (
                    "The sous-chef walked out with two line cooks! Eighty VIP covers waiting in the dining room! Do we cancel the second seating or push through?",
                    "수셰프가 라인 쿡 두 명을 데리고 나가버렸어! 홀에는 VIP 80명이 기다리고 있는데! 2부 예약을 취소할까, 아니면 강행할까?",
                    "예약 취소는 없으며 자신이 직접 메인 팬을 잡을 테니 파티시에와 인턴들을 조리 라인에 재배치하라고 호통치세요.",
                    ("We never cancel a cover. Move pastry to the cold station, put the apprentices on prep, and I take the sautés myself. Move!", "우리 사전에 예약 취소는 없습니다. 페이스트리를 콜드 파트로 옮기고 실습생들을 프렙에 투입하세요. 메인 팬은 내가 잡습니다. 움직여!", "‘I take the sautés myself’는 주방의 위기를 정면 돌파하는 헤드 셰프의 압도적 카리스마입니다."),
                    ("Let's call the police and arrest the sous-chef.", "경찰을 불러 수셰프를 체포합시다.", "주방 문제를 공권력에 맡기려는 황당한 발상입니다."),
                    ("Tell the customers to eat instant noodles today.", "손님들에게 오늘은 컵라면을 드시라고 안내합시다.", "파인다이닝의 명성을 하루아침에 날리는 행위입니다.")
                ),
                (
                    "We're forty minutes in. Ticket times are slipping by eight minutes. The floor manager is panicking at the pass.",
                    "서비스 40분 경과. 주문 티켓 대기 시간이 8분씩 밀리고 있어. 플로어 매니저가 배식대(Pass)에서 패닉에 빠졌네.",
                    "호흡을 가다듬고 코스 간격을 재조정하며 빵과 아뮤즈 부쉬를 추가 서비스해 테이블 시간을 벌라고 지시하세요.",
                    ("Fire complimentary truffle consommé to every table immediately. Buy us ten minutes of sensory pleasure while we clear this backlog.", "모든 테이블에 트러플 콘소메를 서비스로 즉각 내보내세요. 손님들이 감각적 황홀경에 빠진 사이 밀린 주문을 전부 쳐내겠습니다.", "‘complimentary truffle consommé’와 ‘clear this backlog’는 시간 관리와 고객 만족을 동시에 잡는 셰프의 기지입니다."),
                    ("Tell the guests to wait patiently without talking.", "손님들에게 말없이 얌전히 기다리라고 하세요.", "손님을 훈계하는 최악의 접객 태도입니다."),
                    ("Give them some candy for skinship.", "스킨십을 위해 사탕을 좀 줍시다.", "‘skinship’은 콩글리시입니다.")
                ),
                (
                    "Last check cleared! Every single guest gave a standing ovation as they walked out! You ran a four-man station by yourself and set a revenue record tonight.",
                    "마지막 주문 완료! 나가는 손님들마다 기립박수를 보냈어! 혼자서 4인분 스테이션을 다 치고 오늘 매출 신기록을 세웠네.",
                    "위대한 주방은 사람이 부족할 때가 아니라 열정이 식었을 때 무너지는 법이라고 답하세요.",
                    ("A kitchen doesn't collapse from an empty station, Marco—it dies only when the spirit on the line gives up. We held the line.", "주방은 자리가 비었다고 무너지지 않습니다, 마르코. 라인 위의 영혼이 포기할 때 비로소 죽는 것입니다. 우리는 자리를 지켜냈습니다.", "더 베어(The Bear)를 연상시키는 전율의 주방 승리 선언입니다."),
                    ("I am very happy my hand did not get burned.", "손을 데이지 않아서 아주 다행입니다.", "치열했던 승리의 여운을 깨뜨리는 소심한 반응입니다."),
                    ("Let's do Dutch pay for the victory beer.", "승리의 맥주는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "시크릿 레시피 도난: 파리 본점의 배신자 색출",
            "Chef Marco (Executive Head Chef)", "🔪",
            "미슐랭 3스타 레스토랑의 비밀 연구실. 10년간 개발한 발효 버터와 소스 배합 공식이 라이벌 호텔 체인으로 유출되었다. 미각 블라인드 테스트를 통해 주방 내부의 산업 스파이를 밝혀내야 한다.",
            "unmask the corporate saboteur through palate verification",
            "미각 검증을 통해 주방 내부의 산업 스파이를 색출해낼 때 쓰는 표현입니다.",
            [
                (
                    "The rival hotel just launched our signature aged-koji duck sauce verbatim on their menu! Someone on our prep team sold our proprietary notes.",
                    "경쟁 호텔이 우리 시그니처 발효 누룩 오리 소스를 메뉴판에 글자 하나 안 바꾸고 그대로 출시했어! 우리 프렙 팀 중 누군가 비밀 노트를 팔아넘긴 거야.",
                    "원작자만이 아는 미세 결함 성분을 미끼로 숨겨두었으니 상대 소스를 성분 분석해 배신자를 특정하자고 하세요.",
                    ("I deliberately introduced a rare yuzu-tannin imbalance into the master batch. A lab chromatography test of their sauce will link directly to the traitor's personal locker.", "마스터 배치에 유자 타닌의 미세 불균형을 일부러 심어두었습니다. 상대 소스를 크로마토그래피 검사하면 배신자의 개인 락커로 직결될 것입니다.", "‘yuzu-tannin imbalance’와 ‘chromatography test’는 미식 스릴러의 진수를 보여주는 치밀한 함정입니다."),
                    ("Let us yell at all cooks until someone cries.", "누군가 울 때까지 모든 요리사에게 소리를 지릅시다.", "원시적이고 아무것도 해결하지 못하는 방법입니다."),
                    ("Let's claim the rival hotel on their SNS.", "경쟁 호텔 SNS에 클레임을 남깁시다.", "‘claim’과 ‘SNS’는 콩글리시입니다.")
                ),
                (
                    "The test matched the pastry junior's encrypted drive! He's packing his knives right now. Do we call the police or handle this in-house?",
                    "검사 결과가 페이스트리 막내의 암호화 드라이브와 일치했어! 그가 지금 칼가방을 싸고 있네. 경찰을 부를까, 주방 내부 규율로 처리할까?",
                    "요리업계 전체에 영구 퇴출 통보를 내리고 영업비밀 침해로 연방 검찰에 형사 고발하자고 하세요.",
                    ("Hand him over to the federal prosecutor for industrial espionage and blacklist him across the International Chefs Guild. Integrity is non-negotiable.", "산업 스파이 혐의로 연방 검찰에 넘기고 국제 셰프 길드 전체에 영구 블랙리스트로 등록하십시오. 진실성은 타협할 수 없습니다.", "‘industrial espionage’와 ‘integrity is non-negotiable’은 요리계의 기강을 바로잡는 단호한 조치입니다."),
                    ("Tell him to apologize and say he is sorry.", "사과하고 죄송하다고 말하라고 타일러봅시다.", "배신자를 방조하는 안일한 태도입니다."),
                    ("Take his handphone and throw it into the soup.", "그의 핸드폰을 뺏어서 수프에 던져버립시다.", "‘handphone’은 콩글리시입니다.")
                ),
                (
                    "Rival hotel issued a public retraction and pulled the stolen dish! Our reservation waitlist just blew out to twelve months! You defended the kitchen's honor.",
                    "경쟁 호텔이 공식 사과문을 발표하고 도난 메뉴를 전량 철회했어! 우리 예약 대기 명단이 12개월 뒤까지 꽉 찼네! 주방의 명예를 지켜냈어.",
                    "레시피는 훔칠 수 있어도 셰프의 손끝에 깃든 영혼은 결코 훔칠 수 없다고 답하세요.",
                    ("They can steal our ingredients, Marco, but they can never replicate the soul behind the blade. Back to service.", "그들이 우리의 식재료는 훔칠 수 있을지 몰라도, 칼끝에 깃든 영혼까지 복제할 수는 없습니다. 다시 서비스로 돌아갑시다.", "진정한 거장의 자부심을 보여주는 멋진 마무리입니다."),
                    ("I am glad we have many customers now.", "이제 손님이 많아져서 기쁩니다.", "깊은 예술적 감동이 결여된 대답입니다."),
                    ("Let's do Dutch pay for the victory dinner.", "축하 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        ),
        mk_ep(
            "세계 최고의 레스토랑 월드 투어: 도쿄 팝업 오프닝 나이트",
            "Chef Marco (Executive Head Chef)", "🔪",
            "도쿄 긴자 럭셔리 타워 최상층 팝업 스토어. 일본 현지 식재료만을 사용해 뉴욕의 정체성을 재해석하는 갈라 디너의 밤. 현지 미식 비평가들의 까다로운 입맛을 사로잡아야 한다.",
            "reinterpret indigenous terroir with modern avant-garde technique",
            "현지 고유의 떼루아를 현대적 아방가르드 조리 기법으로 완벽히 재해석해낼 때 쓰는 표현입니다.",
            [
                (
                    "The Tokyo critics are skeptical. They think a Western chef cannot master the subtleties of Tsukiji seafood and dashi. How do we open the menu?",
                    "도쿄 평론가들이 회의적이야. 서양 셰프가 츠키지 해산물과 다시(Dashi)의 미묘한 깊이를 이해하지 못할 거라 생각하고 있어. 오프닝 요리를 어떻게 낼 건가?",
                    "전통 가다랑어포 대신 훈제 칠면조 뼈로 우려낸 혁신적 아메리칸 다시에 홋카이도 성게알을 얹어 충격을 선사하자고 하세요.",
                    ("We defy their expectations. Present a consommé of smoked heritage turkey infused with kombu, crowned with Hokkaido uni. Bridge two worlds in a single sip.", "그들의 선입견을 정면으로 깨부수겠습니다. 다시마를 우려낸 훈제 헤리티지 칠면조 콘소메에 홋카이도 성게알을 올리십시오. 한 모금으로 두 세계를 연결합니다.", "‘smoked heritage turkey infused with kombu’는 창의성의 극치를 보여주는 천재적 메뉴 기획입니다."),
                    ("Just make typical American hamburger for them.", "그들에게 전형적인 미국식 햄버거나 만들어 줍시다.", "파인다이닝 갈라 디너에 어울리지 않는 무성의한 대안입니다."),
                    ("The fish has good spec so don't worry.", "생선 스펙이 좋으니 걱정 마세요.", "‘spec’은 콩글리시입니다.")
                ),
                (
                    "The room went silent after the third course. The dean of Japanese food critics put down his chopsticks and called for the head chef. He looks unreadable.",
                    "3번째 코스가 나간 뒤 객석이 침묵에 휩싸였어. 일본 미식 비평계의 대부가 젓가락을 내려놓고 총괄 셰프를 부르고 있네. 표정을 읽을 수가 없어.",
                    "당당하지만 겸손한 태도로 테이블로 다가가 요리에 담긴 문화적 경의와 철학을 직접 설명하세요.",
                    ("Step to the table with quiet reverence. Explain our culinary dialogue between tradition and innovation. Let humility amplify our mastery.", "조용한 경의를 담아 테이블로 걸어가십시오. 전통과 혁신 사이의 미식적 대화를 설명하세요. 겸손이 우리의 압도적 기량을 더욱 빛나게 할 것입니다.", "‘culinary dialogue between tradition and innovation’은 비평가를 사로잡는 완벽한 셰프의 품격입니다."),
                    ("Tell him that Western food is much better than Japanese food.", "서양 요리가 일본 요리보다 훨씬 훌륭하다고 말하세요.", "현지 문화에 대한 모욕으로 국제적 망신을 초래합니다."),
                    ("Give him a business card for skinship.", "스킨십을 위해 명함을 한 장 건넵시다.", "‘skinship’은 콩글리시입니다.")
                ),
                (
                    "He stood up and bowed ninety degrees! He called it the most revolutionary dining experience in Tokyo in twenty years! The reservation server crashed with fifty thousand hits!",
                    "그가 일어나 90도로 허리를 굽혀 절했어! 지난 20년간 도쿄에서 맛본 가장 혁명적인 식사 경험이라 극찬했네! 예약 서버가 5만 건의 접속으로 폭주했어!",
                    "국경과 문화의 벽을 허무는 것이 바로 요리의 위대한 힘이라고 감사를 표하세요.",
                    ("Culinary art knows no borders, Marco. When respect meets relentless craft, the whole world speaks the same language.", "요리 예술에는 국경이 없습니다, 마르코. 상호 존중이 치열한 장인정신과 만날 때, 온 세상은 같은 언어로 대화합니다.", "세계적 거장 셰프다운 감동의 피날레입니다."),
                    ("I am glad we can make a lot of money in Tokyo.", "도쿄에서 돈을 많이 벌 수 있어서 참 좋습니다.", "상업적인 속물처럼 느껴지는 답변입니다."),
                    ("Let's do Dutch pay for the karaoke tonight.", "오늘 밤 노래방은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다.")
                )
            ]
        )
    ]

    return data

