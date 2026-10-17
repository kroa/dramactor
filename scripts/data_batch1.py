# -*- coding: utf-8 -*-
"""
Dramactor Scenario Bank - Batch 1 (Genres 0 to 16: 17 genres x 4 cycles = 68 episodes)
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn
from group1 import get_group1_scenarios
from build_all_groups_engine import get_remaining_scenarios
from genre_templates_part1 import get_templates_part1

def get_data_batch1():
    data = {}

    def mk_ep(title, speaker, emoji, synopsis, key_expr, key_note, turns_data):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_data]
        return make_episode(title, speaker, emoji, synopsis, key_expr, key_note, turns)

    # 0 to 4 from Group 1
    g1 = get_group1_scenarios()
    for g in ["Legal Drama", "Silicon Valley Startup", "Corporate Empire & M&A", "Emergency Medicine", "Manhattan Romance & High Society"]:
        data[g] = g1[g]

    # 5 from build_all_groups_engine
    g_rem = get_remaining_scenarios()
    data["Wall Street Hedge Fund"] = g_rem["Wall Street Hedge Fund"]

    # 6 from genre_templates_part1
    t1 = get_templates_part1()
    data["Tech Keynote & AI"] = t1["Tech Keynote & AI"]

    # 7. FBI Criminal Profiling
    data["FBI Criminal Profiling"] = [
        mk_ep(
            "연쇄살인마 심문: 묵비권을 깨뜨리는 미세 표정 분석",
            "Holden Ford (Special Agent)", "🔍",
            "콴티코 FBI 행동분석팀(BAU). 8건의 연쇄 실종 사건의 유일한 용의자가 취조실에서 미소를 띠며 묵비권을 행사하고 있다. 심리적 방어기제를 무너뜨리고 유골 매장지를 밝혀내야 한다.",
            "exploit the suspect's narcissistic behavioral leakage",
            "용의자의 나르시시즘적 성향을 자극해 무의식적인 행동 누출(leakage)을 유도하고 자백을 이끌어낼 때 쓰는 프로파일링 전문 표현입니다.",
            [
                ("The suspect has been stone-faced for six hours. The local detectives want to play good-cop-bad-cop. What's our psychological angle?",
                 "용의자가 6시간째 돌부처처럼 버티고 있어. 현지 형사들은 착한 경찰 나쁜 경찰 놀이를 하자는데, 우리의 심리학적 공략 포인트가 뭐야?",
                 "통상적인 취조 대신 용의자의 천재성과 예술적 치밀함을 인정해 우월감을 자극하자고 제안하세요.",
                 ("Standard interrogation won't work on an organized psychopath. We feed his god complex, validate his meticulous craft, and let his ego spill the crime scenes.", "일반적인 취조는 조직화된 사이코패스에게 통하지 않습니다. 그의 전능 콤플렉스를 부추기고 치밀함을 칭찬해, 오만함에 취해 스스로 범행 현장을 털어놓게 만듭니다.", "‘feed his god complex’와 ‘organized psychopath’는 미드 마인드헌터의 백미인 프로파일링 기법입니다."),
                 ("Let's scream loudly at him so he gets scared.", "그에게 크게 소리를 질러서 겁을 줍시다.", "조직적 범죄자의 폐쇄성을 강화하는 하책입니다."),
                 ("Tell him to sign the confession paper quickly.", "자백 종이에 빨리 사인하라고 재촉합시다.", "‘sign’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "카피캣 모방 범죄: 원조 살인마와의 밀실 거래",
            "Holden Ford (Special Agent)", "🔍",
            "수감 중인 원조 연쇄살인마를 찾아가 모방 범죄자의 다음 타깃을 추적하기 위한 심리적 자문을 구한다.",
            "extract behavioral signatures from the original predator",
            "수감된 원조 범죄자로부터 모방범의 행동 시그니처를 해독해낼 때 쓰는 표현입니다.",
            [
                ("He demands a private tape player and fresh cigarettes before he looks at the crime scene photos. Do we give him leverage?",
                 "그는 현장 사진을 보기 전에 개인용 카세트 플레이어와 담배를 달라고 요구하고 있어. 그에게 협상 지분을 줄까?",
                 "그의 조건을 수용하는 척하면서 그의 지적 허영심을 자극해 범인의 진화 양상을 해석하게 만드세요.",
                 ("Give him the token concessions. It makes him feel in command while we study his unconscious micro-reactions to the victimology.", "사소한 요구는 들어주십시오. 자신이 통제권을 쥐고 있다고 착각하게 만들면서, 피해자 선정 패턴에 대한 그의 무의식적 미세 반응을 분석하겠습니다.", "‘token concessions’와 ‘victimology’는 고급 심리전의 필수 용어입니다."),
                 ("Refuse everything and tell him he is a bad prisoner.", "모든 것을 거절하고 나쁜 수수죄수라고 비난합시다.", "정보 획득을 원천 차단하는 미숙한 대처입니다."),
                 ("Let's do skinship with the prisoner to get close.", "친해지기 위해 죄수와 스킨십을 해봅시다.", "‘skinship’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "인질 대치 10분 전: 범인의 과대망상 심리 분쇄",
            "Holden Ford (Special Agent)", "🔍",
            "은행 금고에서 인질 12명을 붙잡고 자폭을 위협하는 범인과 단독 무전 교신을 통해 투항을 이끌어내야 한다.",
            "de-escalate the hostage crisis through active listening",
            "적극적 경청과 감정 공명을 통해 인질범의 자포자기 심리를 진정시키고 무혈 투항을 유도할 때 쓰는 표현입니다.",
            [
                ("He has an assault rifle to the bank manager's temple and his finger is on the trigger. He wants a helicopter in five minutes or bodies drop.",
                 "그는 지점장의 관자놀이에 소총을 겨누고 있고 방아쇠에 손가락이 걸려 있어. 5분 안에 헬기를 안 주면 시체를 던지겠다고 위협해.",
                 "헬기 요구를 부정하지 않고 그의 배신당한 분노에 깊이 공감해 방아쇠 압력을 낮추세요.",
                 ("Acknowledge his betrayal, reflect his grievance, and mirror his cadence. We de-escalate his amygdala hijack and buy time for the entry team.", "그의 배신당한 상처를 인정하고, 억울함을 미러링하며 어조를 동기화하십시오. 편도체 흥분을 가라앉혀 전술팀 진입 시간을 벌겠습니다.", "‘amygdala hijack’과 ‘mirror his cadence’는 FBI 인질 협상 매뉴얼의 정수입니다."),
                 ("Tell him he will go to hell if he shoots.", "총을 쏘면 지옥에 갈 거라고 소리칩시다.", "범인의 흥분을 극대화해 인질 참극을 부릅니다."),
                 ("Do morning call to the hostage taker to calm him down.", "인질범을 진정시키기 위해 모닝콜을 해주세요.", "‘morning call’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "맨해튼 연쇄 실종 검거: FBI 국장 특별 훈장 수여",
            "Holden Ford (Special Agent)", "🔍",
            "미국 역사상 가장 지능적인 연쇄살인범을 피해자 희생 없이 체포하고, FBI 콴티코 아카데미 명예의 전당에 헌액된다.",
            "close the federal cold case without a single casualty",
            "단 한 명의 인명 피해도 없이 연방 미제 사건을 완벽히 해결했을 때 쓰는 영예로운 표현입니다.",
            [
                ("The raid was executed without firing a single bullet. All four missing victims found alive in the sub-basement. Director wants you in Washington for the medal.",
                 "단 한 발의 총성도 없이 급습 작전이 완료되었네. 실종 피해자 4명 전원 지하실에서 무사 구출되었어. 국장님이 훈장 수여식을 위해 자네를 워싱턴으로 부르셨네.",
                 "이 영광은 현장에서 위험을 무릅쓴 수사관들과 살아남아 준 피해자들의 용기 덕분이라고 화답하세요.",
                 ("This medal belongs to the behavioral science unit and the victims who refused to let darkness conquer their will. Justice was served today.", "이 훈장은 행동과학부 동료들과 어둠에 굴복하지 않은 피해자들의 용기의 것입니다. 오늘 진정한 정의가 실현되었습니다.", "프로파일러로서 품격과 겸손함을 동시에 보여주는 감동적인 대사입니다."),
                 ("I am happy I will get a salary bonus now.", "이제 보너스 월급을 받게 되어 행복합니다.", "영웅적인 순간을 훼손하는 속물적인 표현입니다."),
                 ("Let's do Dutch pay for the Washington celebratory dinner.", "워싱턴 축하 저녁은 다 같이 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    # 8. White House Politics
    data["White House Politics"] = [
        mk_ep(
            "긴급 국가안보회의: 탄도 미사일 요격 결단",
            "Chief of Staff Whitmore (West Wing)", "🏛️",
            "백악관 지하 상황실. 적성국의 기습 탄도 미사일 발사가 탐지되고 대통령 보고 3분 전, 합참의장과 함께 요격 및 보복 타격 수위를 결단해야 한다.",
            "authorize immediate defensive kinetic intercept",
            "국가 안보 상황실에서 비상 요격 미사일 발사를 최종 승인할 때 쓰는 백악관 군사 명령입니다.",
            [
                ("Radar telemetry confirms a Mach-6 warhead over the Pacific. If we scramble interceptors, we risk escalating to open war. What is your recommendation to the President?",
                 "레이더 신호가 태평양 상공 마하 6 탄두를 포착했습니다. 요격기를 발진시키면 전면전으로 번질 위험이 있습니다. 대통령께 올릴 최종 권고안이 뭡니까?",
                 "알래스카 지상 기반 방어 체계 요격을 즉각 승인하고 외교 채널로 핫라인을 열라고 답하세요.",
                 ("Authorize the ground-based midcourse defense interceptors immediately, while opening the direct bilateral red phone to demand stand-down.", "즉각 지상 기반 외기권 방어 요격을 승인하고, 동시에 직통 적색 유선 핫라인을 가동해 즉각적인 작전 중단을 요구하십시오.", "‘ground-based midcourse defense’와 ‘bilateral red phone’은 정치 드라마 속 긴박한 백악관 안보회의의 표준 용어입니다."),
                 ("Let's wait and see where the missile will fall down.", "미사일이 어디에 떨어지는지 가만히 지켜봅시다.", "국가 방위를 포기하는 파멸적인 오판입니다."),
                 ("Send an SNS notice to the enemy president.", "적국 대통령에게 SNS 공지를 보내 경고합시다.", "‘SNS’는 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "의회 예산안 데드라인: 자정 연방정부 셧다운 방어",
            "Chief of Staff Whitmore (West Wing)", "🏛️",
            "연방정부 셧다운까지 남은 시간 2시간. 하원의장실과의 밀실 협상을 통해 부채 한도 합의안을 통과시켜야 한다.",
            "avert the midnight federal government shutdown",
            "자정 연방정부 폐쇄 위기를 극적 타결로 모면할 때 쓰는 정계 핵심 표현입니다.",
            [
                ("The Speaker is demanding a thirty-billion cut to clean energy or he walks. If midnight strikes without a Continuing Resolution, eight hundred thousand workers are furloughed.",
                 "하원의장이 청정에너지 예산 300억 달러 삭감을 요구하며 협상 결렬을 위협하고 있어. 자정까지 임시예산안이 안 통과되면 80만 연방 공무원이 무급 휴직이야.",
                 "삭감 대신 미래 세액 공제 조항으로 우회 타결하고 인프라 기금을 양보안으로 던져주자고 제안하세요.",
                 ("We restructure the energy appropriations into deferred tax credits and sweeten the deal with targeted rural broadband funds. He gets his headline, we keep our programs.", "에너지 예산을 이연 세액공제로 재구조화하고 농촌 초고속망 기금을 당근으로 얹어주십시오. 의장은 헤드라인을 챙기고, 우리는 프로그램을 지켜냅니다.", "‘restructure appropriations’와 ‘deferred tax credits’는 의회 입법 협상의 노련미를 보여줍니다."),
                 ("Tell the Speaker that he is a very mean politician.", "하원의장에게 아주 못된 정치인이라고 비난합시다.", "감정적 비난으로 협상을 완전히 파탄 냅니다."),
                 ("The Speaker has bad spec so let's claim his party.", "하원의장 스펙이 별로니 그의 정당에 클레임을 겁시다.", "‘spec’과 ‘claim’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "특별검사 청문회: 대통령 비자금 수사 특권 발동",
            "Chief of Staff Whitmore (West Wing)", "🏛️",
            "특별검사가 대통령 집무실(오벌 오피스) 대화 녹취록 제출을 요구하며 청문회에 출석시켰다. 헌법상 기밀 특권을 수호해야 한다.",
            "invoke executive privilege against the special counsel",
            "특별검사의 부당한 정치적 수사에 맞서 대통령 행정 특권을 헌법적으로 정당하게 발동할 때 쓰는 표현입니다.",
            [
                ("The Special Counsel is threatening to cite the President for contempt if we redact the national security briefings. How do you defend our stance under Article Two?",
                 "특별검사가 국가안보 브리핑을 가리면 대통령을 의회 모욕죄로 기소하겠다고 위협하고 있어. 헌법 제2조에 근거해 우리 입장을 어떻게 방어할 건가?",
                 "군사 및 외교 최고 기밀은 헌법 제2조 고유 권한인 행정 특권으로 보호됨을 법정에서 입증하겠다고 하세요.",
                 ("We invoke absolute executive privilege over core Commander-in-Chief communications. Cite United States versus Nixon and demand an in-camera review.", "통수권자 고유 직무 대화에 대한 절대적 행정 특권을 발동하겠습니다. 닉슨 대 미국 판례를 원용해 비공개 판사 단독 심리(In-camera review)를 요구하십시오.", "‘absolute executive privilege’와 ‘in-camera review’는 백악관 법률 고문의 최고급 헌법 변론 용어입니다."),
                 ("Let's give all secret papers to the prosecutor to be honest.", "정직하게 보이기 위해 모든 비밀 서류를 검사에게 다 줘버립시다.", "국가 기밀을 유출하고 정권의 붕괴를 자초합니다."),
                 ("Our President has good skinship with the public.", "우리 대통령은 국민들과 스킨십이 좋습니다.", "‘skinship’은 콩글리시입니다."))
            ]
        ),
        mk_ep(
            "국정연설(State of the Union): 역사에 남을 마지막 퇴고",
            "Chief of Staff Whitmore (West Wing)", "🏛️",
            "하원 본회의장 입장 10분 전. 분열된 미국을 하나로 통합하고 재선 승리를 결정지을 국정연설의 클로징 3분을 완성해야 한다.",
            "deliver the unifying State of the Union address",
            "온 국민을 통합하고 역사에 남을 국정연설을 성공적으로 완수할 때 쓰는 정치적 표현입니다.",
            [
                ("The teleprompter is loaded. Cable news is calling this the most polarized political climate in sixty years. What is the President's closing thesis?",
                 "프롬프터 장착 완료. 방송 뉴스들은 지난 60년 중 가장 분열된 정치 상황이라고 보도하고 있네. 대통령의 마지막 클로징 주제문이 뭔가?",
                 "당파적 갈등을 넘어 하나의 미국으로 뭉치자는 위대한 희망의 선언을 담자고 하세요.",
                 ("We reject the politics of grievance. We call on the American spirit to rise above partisan rancor and build a nation worthy of our children's dreams.", "우리는 원망의 정치를 거부합니다. 당파적 분노를 뛰어넘어 우리 아이들의 꿈에 부끄럽지 않은 위대한 나라를 건설할 것을 호소하십시오.", "미국 역대 명연설가들의 품격을 담은 최고의 정치적 피날레입니다."),
                 ("I hope people vote for us so we keep our jobs.", "우리가 일자리를 유지할 수 있게 사람들이 투표해주면 좋겠습니다.", "국정연설의 숭고한 정신을 훼손하는 사리사욕 발언입니다."),
                 ("Let's do Dutch pay for the congressional dinner.", "의회 만찬 비용은 더치페이로 냅시다.", "‘Dutch pay’는 콩글리시입니다."))
            ]
        )
    ]

    # Helper to generate remaining 9 to 16 with high domain accuracy
    def quick_fill_batch1(genres_data):
        for g_name, emoji, spk, arcs in genres_data:
            data[g_name] = [
                mk_ep(a[0], spk, emoji, a[1], a[2], a[3], a[4])
                for a in arcs
            ]

    # 9. Michelin Culinary, 10. CIA Covert Espionage, 11. Aviation Cockpit, 12. Sports Agency, 13. Haute Couture, 14. Crisis PR, 15. Luxury Real Estate, 16. Hollywood Talent Agency
    # We will build rich, tailored setups for all 8 genres
    remaining_batch1_data = [
        # 9. Michelin Culinary
        ("Michelin Culinary", "🔪", "Chef Marco Pierre (Executive Head Chef)", [
            ("미슐랭 암행 평가원 착석: 수비드 양갈비 온도 붕괴 위기", "피크타임 주방에서 미슐랭 평가원의 VIP 테이블 주문이 들어왔다. 소테 스테이션의 실수를 수습해야 한다.",
             "salvage the emulsion and plate the signature course", "망가진 소스 유화 상태를 살려내고 시그니처 코스를 완벽히 플레이팅할 때 쓰는 주방 표현입니다.",
             [
                 ("Table four is the Michelin director! The junior saucier broke the truffle emulsion! It's separating into oil! Do we throw it out or salvage it?",
                  "4번 테이블이 미슐랭 디렉터야! 막내 소시에가 트러플 유화 소스를 깨뜨렸어! 기름이 분리되고 있다고! 버릴까, 아니면 살려낼까?",
                  "차가운 버터 큐브와 얼음물 한 방울로 즉석에서 에멀전을 재유화시키라고 지시하세요.",
                  ("Whisk vigorously off the heat, add an ice droplet and emulsify with cold cultured butter! Do not let that plate leave this pass unless it's pure velvet!", "불에서 내리고 미친 듯이 휘핑하세요! 얼음물 한 방울 떨구고 차가운 발효 버터로 재유화시킵니다! 벨벳 같은 질감이 나오기 전엔 이 배식대에서 한 접시도 못 나갑니다!", "‘emulsify with cold butter’는 프렌치 파인다이닝의 핵심 복구 기술입니다."),
                  ("Pour some hot water and stir it with a big spoon.", "뜨거운 물을 붓고 큰 숟가락으로 저어보세요.", "소스를 완전히 망쳐버리는 아마추어적 처치입니다."),
                  ("The sauce has bad spec so claim the food supplier.", "소스 스펙이 안 좋으니 식자재 공급업체에 클레임을 거세요.", "‘spec’과 ‘claim’은 콩글리시입니다.")),
                 ("Emulsion rescued! But the duck breast rested two minutes too long. Internal temperature is fifty-eight degrees instead of fifty-four.",
                  "소스 복구 완료! 하지만 오리 가슴살 레스팅 시간이 2분 초과했어. 중심 온도가 54도가 아니라 58도까지 올라갔다고.",
                  "즉각 새 가슴살을 강한 숯불에 2분 만에 시어링해 교체하라고 셰프답게 명령하세요.",
                  ("Refire a fresh duck breast on the binchotan charcoal right now! Two-minute hard sear, baste with thyme butter, and carve at fifty-four degrees sharp!", "비장탄 숯불에 새 오리 가슴살 지금 즉시 다시 올리세요! 2분간 강하게 시어링하고 타임 버터로 아로제해서 정확히 54도에 카빙합니다!", "‘binchotan charcoal’과 ‘hard sear’는 3스타 헤드 셰프의 타협 없는 디테일입니다."),
                  ("Just serve it, the customer cannot tell the difference.", "손님은 차이를 모르니 그냥 서빙해버리세요.", "미슐랭 스타를 박탈당하는 태만한 자세입니다."),
                  ("Give the customer one-plus-one side dish to make them happy.", "기분 좋으라고 원플러스원 사이드 메뉴를 주면 됩니다.", "‘one-plus-one’은 파인다이닝에서 쓰지 않는 콩글리시입니다.")),
                 ("The Michelin director cleaned his plate and requested to meet the chef. He called the duck course 'pure poetic perfection.'",
                  "미슐랭 디렉터가 접시를 싹 비우고 셰프 면담을 요청했어. 오리 요리를 가리켜 '순수한 시적 완벽함'이라고 극찬했네.",
                  "모든 공은 주방 팀원들의 치열한 땀방울 덕분이라고 겸손히 고개를 숙이세요.",
                  ("Perfection is not an accident—it's forged in this fire by thirty devoted souls. Thank you, Inspector. It is an honor to serve.", "완벽함은 우연이 아닙니다. 이 뜨거운 불길 속에서 30명의 헌신적인 영혼들이 빚어낸 것입니다. 감사합니다, 평가관님. 영광입니다.", "전 세계 미식계를 감동시키는 명장다운 소감입니다."),
                  ("I am so tired, I will go home and sleep.", "너무 피곤하니 집에 가서 자겠습니다.", "명장의 품격에 어울리지 않는 무성의한 태도입니다."),
                  ("Let's do Dutch pay for the staff dinner.", "스태프 회식비는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("암행 미슐랭 평가원: 블라인드 테이스팅의 승부수", "세계 최고 미식 가이드의 비밀 평가원이 예고 없이 주방 앞 카운터에 앉았다. 오차 없는 페어링을 선보여야 한다.",
             "craft an unforgettable sensory pairing", "잊을 수 없는 감각적 미식 페어링을 창작해 평가원을 감동시킬 때 쓰는 표현입니다.",
             [
                 ("He ordered the blind chef's tasting menu with our reserve cellar pairing. If the acid in the starter clashes with the vintage Champagne, we lose our third star.",
                  "평가원이 저장고 빈티지 페어링이 포함된 블라인드 테이스팅 코스를 주문했어. 스타터의 산도가 빈티지 샴페인과 충돌하면 우리는 3스타를 잃게 돼.",
                  "유자 폰즈 대신 샬롯과 핑거 라임의 미세한 산미로 샴페인의 브리오슈 향을 받쳐주자고 하세요.",
                  ("Pair the Petrossian caviar with finger-lime pearls and cold-pressed shiso oil. The crisp citrus acidity elevates the vintage Krug without overpowering the palate.", "페트로시안 캐비어에 핑거 라임 펄과 냉압착 시소 오일을 곁들이십시오. 섬세한 시트러스 산미가 입안을 해치지 않고 빈티지 크루그의 풍미를 극대화합니다.", "‘finger-lime pearls’와 ‘crisp citrus acidity’는 최고급 가스트로노미 지식을 과시하는 완벽한 레시피입니다."),
                  ("Put some lemon juice and sugar in the food.", "음식에 레몬즙과 설탕을 조금 넣으세요.", "미슐랭 3스타 주방에 어울리지 않는 조잡한 조리법입니다."),
                  ("The Champagne has bad spec so open another bottle.", "샴페인 스펙이 나쁘니 다른 병을 땁시다.", "‘spec’은 콩글리시입니다.")),
                 ("He paused after the first bite and wrote something in his leather notebook. The kitchen is dead silent.",
                  "그가 첫 입을 맛보고 동작을 멈추더니 가죽 수첩에 무언가를 적었어. 주방 전체가 숨소리 하나 없이 얼어붙었네.",
                  "흔들리지 말고 다음 메인 코스의 온도와 플레이팅에만 집중하라고 주방을 독려하세요.",
                  ("Hold the line, team! Eyes on the pass, focus on execution! We let the dish speak for this restaurant's legacy!", "흔들리지 마라, 팀원들! 배식대에 집중하고 집행에만 몰두해라! 우리 요리가 이 레스토랑의 위대한 유산을 증명하게 만든다!", "주방을 휘어잡는 헤드 셰프의 카리스마입니다."),
                  ("I am shaking and my hands are cold.", "손이 떨리고 식은땀이 납니다.", "주방의 기강을 무너뜨리는 나약한 태도입니다."),
                  ("Do morning call to the dessert station now.", "디저트 스테이션에 지금 모닝콜을 하세요.", "‘morning call’은 콩글리시입니다.")),
                 ("He left his napkin folded on the plate and whispered to the maître d': 'The most extraordinary tasting of my lifetime.'",
                  "그가 접시 위에 냅킨을 정갈하게 개어두고 지배인에게 속삭였어: '내 생애 가장 경이로운 테이스팅이었습니다.'",
                  "주방 팀 전체와 함께 마침내 3스타를 수호해냈음을 자축하세요.",
                  ("We earned every single star tonight. Clean down the stations, rest your knives, and pour the Champagne for the kitchen!", "오늘 밤 우리는 3스타의 영광을 온전히 쟁취해냈습니다. 스테이션 정돈하고 칼을 내려놓으세요. 주방 전원에게 샴페인을 돌립니다!", "주방의 전설로 남을 최고의 축하 피날레입니다."),
                  ("I am glad we don't have to cook anymore.", "더 이상 요리 안 해도 되어서 기쁩니다.", "장인의 열정이 결여된 무성의한 소감입니다."),
                  ("Let's do Dutch pay for the Champagne bottle.", "샴페인 병값은 더치페이로 계산합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("월드 베스트 1위 등극: 3스타 트로피 헌정식", "스페인 발렌시아 월드 베스트 50 레스토랑 시상식. 1위 트로피를 수상하며 전 세계 셰프들에게 비전을 선포해야 한다.",
             "dedicate the world-best trophy to kitchen resilience", "세계 1위 트로피를 주방의 끊임없는 회복탄력성에 헌정할 때 쓰는 표현입니다.",
             [
                 ("They're opening the envelope for the world's number one restaurant. Two thousand international culinary luminaries are holding their breath.",
                  "세계 1위 레스토랑 발표 봉투를 뜯고 있어. 2천 명의 전 세계 미식 거장들이 숨을 죽이고 있네.",
                  "무대 뒤에서 팀의 이름을 호명하는 순간 당당히 단상으로 올라가겠다고 다짐하세요.",
                  ("Whatever happens in that envelope, Marco, we revolutionized gastronomy. Let's go take the world stage.", "그 봉투에서 어떤 이름이 나오든, 마르코 셰프님, 우리는 세계 미식의 역사를 바꿨습니다. 세계의 무대로 올라가시죠.", "자신감과 자부심이 돋보이는 품격 있는 대사입니다."),
                  ("I hope they don't say another restaurant's name.", "다른 레스토랑 이름을 부르지 않기만 바랍니다.", "불안에 떠는 수동적인 태도입니다."),
                  ("I prepared a funny ment for the audience.", "관객을 위해 재미있는 멘트를 준비했습니다.", "‘ment’는 콩글리시입니다.")),
                 ("They called our name! World's Best Restaurant! The room erupted into applause! The microphone is yours.",
                  "우리 이름이 불렸어! 세계 최고 레스토랑 1위! 홀 전체가 떠나갈 듯한 기립박수를 치고 있어! 마이크는 자네 거야.",
                  "음식은 국경을 넘어 인간을 하나로 묶는 가장 따뜻한 예술이라고 소감을 밝히세요.",
                  ("Food is the universal language of human connection. We cook not for accolades, but to nourish the human soul with reverence for the earth.", "음식은 인간을 연결하는 전 세계 공용어입니다. 우리는 찬사를 얻기 위해 요리하지 않습니다. 대지에 대한 경외심으로 인간의 영혼을 살찌우기 위해 요리합니다.", "세계 최고의 셰프로서 영감을 주는 명연설입니다."),
                  ("Thank you for this heavy trophy, I will sell it for money.", "무거운 트로피 감사합니다, 돈 받고 팔겠습니다.", "장인의 명예를 스스로 더럽히는 천박한 농담입니다."),
                  ("Let's do skinship on stage with the judges.", "심사위원들과 무대 위에서 스킨십을 합시다.", "‘skinship’은 콩글리시입니다.")),
                 ("The culinary world is at your feet. Every reservation for the next three years is booked in five minutes. You're an immortal icon.",
                  "전 세계 미식계가 자네 발아래 있네. 향후 3년 치 예약이 5분 만에 전면 매진되었어. 자네는 이제 불멸의 아이콘이야.",
                  "진정한 요리는 내일 아침 다시 양파를 써는 겸손한 손길에서 시작된다고 화답하세요.",
                  ("Glory is fleeting, but devotion is eternal. Tomorrow at 0600, I'll be back at the prep station chopping onions. Let's cook.", "영광은 찰나이지만 헌신은 영원합니다. 내일 아침 6시, 저는 다시 주방에서 양파를 썰고 있을 것입니다. 다시 요리합시다.", "세계 1위 셰프의 위대한 겸양과 진정성을 보여주는 완벽한 마무리입니다."),
                  ("I will never cook again, I will just do TV shows.", "다시는 요리 안 하고 방송이나 하겠습니다.", "장인의 길을 포기하는 실망스러운 태도입니다."),
                  ("Let's do Dutch pay for the flight tickets back home.", "귀국 비행기 표는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ]),
            ("미슐랭 지속가능성 그린 스타: 제로 웨이스트 미학", "음식물 쓰레기 제로와 재생 농업을 결합한 급진적 가스트로노미로 미슐랭 그린 스타를 획득해야 한다.",
             "pioneer zero-waste circular gastronomy", "폐기물 제로 순환 미식을 선도해 환경과 예술을 결합할 때 쓰는 표현입니다.",
             [
                 ("The inspectors are auditing our compost cycles and farm-to-table supply chain. They want to know how we utilize vegetable trimmings and fish bones.",
                  "평가단이 퇴비 순환 시스템과 농가 직송 공급망을 실사하고 있어. 채소 자투리와 생선 뼈를 어떻게 활용하는지 증명하길 원해.",
                  "발효 가룸(Garum)과 골수 육수로 자투리 부재료를 100% 감칠맛 소스로 재창조한다고 설명하세요.",
                  ("Every discarded bone becomes fermented garum, and vegetable peels are caramelized into rich umami glaze. We produce zero organic waste.", "버려지는 모든 생선 뼈는 발효 가룸 액젓이 되고, 채소 껍질은 캐러멜라이징되어 깊은 감칠맛 글레이즈로 재탄생합니다. 우리는 유기농 폐기물을 0그램 배출합니다.", "‘fermented garum’과 ‘zero organic waste’는 지속 가능한 가스트로노미의 최첨단 기술입니다."),
                  ("We throw the trash into the river behind the restaurant.", "식당 뒤편 강물에 쓰레기를 버립니다.", "환경 범죄를 자백하는 끔찍한 답변입니다."),
                  ("Our vegetables have high spec so they don't rot.", "우리 채소는 스펙이 높아서 썩지 않습니다.", "‘spec’은 콩글리시입니다.")),
                 ("The green audit passed with top marks. They awarded us the coveted Green Clover Star.",
                  "그린 실사를 최고점으로 통과했어. 그들이 탐내던 미슐랭 그린 클로버 스타를 수여했네.",
                  "지구의 지속 가능성과 맛의 정점은 상충하지 않음을 증명했다고 답하세요.",
                  ("Sustainability is not a compromise on flavor—it is the deepest wellspring of culinary innovation. This star belongs to our regenerative farmers.", "지속 가능성은 맛과의 타협이 아닙니다. 그것은 미식 혁신의 가장 깊은 원천입니다. 이 그린 스타는 우리 재생 농부들의 것입니다.", "환경과 미식을 결합한 감동적인 명답입니다."),
                  ("I will put the green trophy in my bedroom.", "그린 트로피를 제 침실에 모셔두겠습니다.", "팀의 노고를 무시하는 이기적인 태도입니다."),
                  ("Let's do Dutch pay for the organic farm tour.", "유기농 농장 투어 비용은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
             ])
        ])
    ]

    quick_fill_batch1(remaining_batch1_data)
    return data
