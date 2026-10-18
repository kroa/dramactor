# -*- coding: utf-8 -*-
"""
Dramactor Scenario Pack A (Genres 13 to 30: 18 genres x 4 cycles = 72 episodes)
"""
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn

def get_pack_a():
    d = {}

    def mk(title, speaker, emoji, syn, expr, note, turns_raw):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_raw]
        return make_episode(title, speaker, emoji, syn, expr, note, turns)

    # 13. Haute Couture Fashion
    d["Haute Couture Fashion"] = [
        mk("파리 패션위크 런웨이 10분 전: 헤드 드레스 파손 사태", "Miranda Priestly (Editor-in-Chief)", "👗",
           "파리 그랑 팔레 패션위크 피날레 10분 전. 피날레 웨딩드레스의 크리스털 레이스가 찢어졌다. 미란다 프리슬리의 날카로운 시선 앞에서 즉석 재봉으로 기적을 연출해야 한다.",
           "re-drape the silhouette from scratch", "런웨이 직전 파손된 오트쿠튀르 실루엣을 즉석에서 재해석해 드레이핑할 때 쓰는 패션 하우스 표현입니다.",
           [
               ("The crystal bodice tore right down the spine! The lights dim in eight minutes. We either send her out bare or cancel the finale. What do you do?",
                "크리스털 코르셋이 등뼈 라인을 따라 찢어졌어! 8분 뒤에 암전이야. 모델을 헐벗은 채 내보내든가 피날레 쇼를 취소해야 해. 어떻게 할 건가?",
                "가위로 레이스를 뜯어내고 실크 시폰으로 과감한 비대칭 백리스 실루엣을 즉석 드레이핑하자고 하세요.",
                ("Give me the shears and five yards of black silk chiffon! We slash the damaged lace and re-drape a dramatic asymmetrical backless silhouette on the fly!", "가위와 5야드 검은 실크 시폰 주세요! 찢어진 레이스를 과감히 잘라내고 즉석에서 드라마틱한 비대칭 백리스 실루엣을 드레이핑하겠습니다!", "‘re-drape an asymmetrical backless silhouette’는 패션 드라마의 아드레날린을 폭발시키는 대사입니다."),
                ("Let's stitch it with scotch tape very quickly.", "스카치테이프로 재빨리 붙여봅시다.", "오트쿠튀르 컬렉션을 조롱거리로 만드는 최악의 땜질입니다."),
                ("The dress has bad spec so claim the fabric factory.", "드레스 스펙이 안 좋으니 원단 공장에 클레임을 거세요.", "‘spec’과 ‘claim’은 콩글리시입니다.")),
               ("The drape looks striking, but the model is trembling. She refuses to walk without a rehearsal in this new gown. Calm her down.",
                "드레이프는 파격적이지만 모델이 떨고 있어. 연습도 안 해본 새 드레스를 입고는 런웨이에 서지 않겠다고 버틴다네. 모델을 진정시키게.",
                "이 실루엣은 당신만을 위해 탄생한 세상 유일의 걸작이라며 턱을 치켜들고 걸으라고 자존감을 북돋우세요.",
                ("You are not wearing a dress, Naomi—you are wearing art forged in fire. Hold your chin high, own that runway, and make every editor bow before you.", "너는 지금 단순한 옷을 입은 게 아니야, 나오미. 불길 속에서 탄생한 살아있는 예술을 입은 거야. 턱을 치켜들고, 런웨이를 지배해. 모든 편집장들이 네 앞에 무릎 꿇게 만들어.", "탑모델의 야성을 일깨우는 패션 디렉터의 명대사입니다."),
                ("If you don't walk, you will never get a job again.", "안 걸으면 다시는 일자리 못 얻을 줄 알아.", "모델의 공포심을 가중해 런웨이 사고를 부르는 폭언입니다."),
                ("Do morning call with your agency to get courage.", "용기를 얻기 위해 에이전시와 모닝콜을 하세요.", "‘morning call’은 콩글리시입니다.")),
               ("The curtain fell. The French fashion press is crying tears of joy! Anna Wintour just gave a standing ovation! You saved the house of haute couture.",
                "막이 내렸네. 프랑스 패션 기자단이 감격의 눈물을 흘리고 있어! 안나 윈투어가 기립박수를 쳤다고! 자네가 오트쿠튀르 하우스를 구원했어.",
                "진정한 패션은 우아함과 파괴의 경계에서 탄생한다고 품격 있게 화답하세요.",
                ("Couture is not perfection, Miranda—it is beauty born from chaos. Tonight, the house is reborn.", "오트쿠튀르는 완벽함이 아닙니다, 미란다. 혼돈 속에서 탄생하는 숭고한 아름다움입니다. 오늘 밤, 우리 하우스는 다시 태어났습니다.", "패션계의 전설로 등극하는 최고의 피날레 소감입니다."),
                ("I am happy I can take a rest and eat bread.", "이제 쉬면서 빵이나 먹을 수 있어 행복합니다.", "정상급 디자이너답지 못한 소박한 소감입니다."),
                ("Let's do Dutch pay for the champagne tonight.", "오늘 밤 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("라이벌 하우스의 디자인 표절: 기습 프라이빗 쇼 개최", "Miranda Priestly (Editor-in-Chief)", "👗",
           "밀라노 경쟁 명품 브랜드가 우리 가을 컬렉션을 그대로 유출해 표절 쇼를 준비 중이다. 24시간 전에 프라이빗 비밀 런웨이를 열어 선수를 쳐야 한다.",
           "stage an ambush private runway before the counterfeiters",
           "표절 브랜드를 응징하기 위해 24시간 먼저 기습 프라이빗 쇼를 열고 원조의 위엄을 각인시킬 때 쓰는 표현입니다.",
           [
               ("Gucci's sub-brand is staging a replica of our velvet line tomorrow at 10 AM. If they show first, we look like copycats. What's our tactical play?",
                "경쟁 브랜드가 내일 오전 10시에 우리 벨벳 라인 복제품 쇼를 열 계획이야. 그들이 먼저 공개하면 우리가 카피캣으로 전락해. 우리의 반격수가 뭐야?",
                "오늘 자정 루브르 피라미드 지하에서 전 세계 인플루언서 100명을 소집해 기습 쇼를 열자고 제안하세요.",
                ("We call an unannounced midnight show tonight at the Louvre Pyramid. Invite the top fifty global editors by secret courier and reveal the originals first.", "오늘 자정 루브르 피라미드에서 기습 심야 쇼를 엽니다. 톱50 글로벌 편집장들에게 비밀 전령으로 초대장을 보내 원조 컬렉션을 먼저 세상에 공개하십시오.", "‘midnight ambush show’는 패션 전쟁의 판도를 뒤엎는 천재적인 기습 전략입니다."),
                ("Let's post an angry message on the rival CEO's social media.", "라이벌 대표의 SNS에 화난 댓글을 달아봅시다.", "품격을 깎아먹는 유치한 인터넷 감정싸움입니다."),
                ("The rival has bad spec so let's claim them.", "라이벌이 스펙이 나쁘니 클레임을 겁시다.", "‘spec’과 ‘claim’은 콩글리시입니다."))
           ]),
        mk("럭셔리 복합기업의 적대적 인수 거부: 독립 아틀리에 수호", "Miranda Priestly (Editor-in-Chief)", "👗",
           "LVMH 스타일 거대 명품 지주회사가 10억 유로 적대적 인수를 시도하며 장인들의 해고를 요구한다. 가문의 아틀리에와 장인 정신을 지켜내야 한다.",
           "preserve artisanal independence against corporate raiders",
           "사모펀드와 거대 명품 복합기업의 기업 사냥에 맞서 100년 전통 아틀리에의 장인 독립성을 수호할 때 쓰는 표현입니다.",
           [
               ("Bernard's conglomerate just bought forty percent of our voting shares. They want to fire sixty master tailors and offshore production to automated factories.",
                "베르나르의 복합기업이 우리 의결권 주식 40%를 매집했어. 60명의 수석 장인들을 해고하고 생산을 자동화 공장으로 외주 돌리겠다고 압박하더군.",
                "프랑스 문화재 보호 재단과 영구 장인 신탁을 결성해 생산 라인 이전을 법적으로 원천 봉쇄하자고 하세요.",
                ("We transfer the atelier's historic craft patents into an inviolable French Heritage Trust. No corporate predator can offshore a living national treasure.", "아틀리에의 역사적 공예 특허를 불가침의 프랑스 문화유산 신탁으로 양도하겠습니다. 그 어떤 기업 사냥꾼도 살아있는 인간문화재를 해외로 빼돌릴 수 없습니다.", "‘inviolable Heritage Trust’는 장인 정신을 자본의 탐욕으로부터 지켜내는 숭고한 법률 방패입니다."),
                ("Tell the tailors to work faster so the big company likes them.", "대기업 마음에 들도록 장인들에게 일이나 더 빨리하라고 닦달합시다.", "장인 정신의 영혼을 파괴하는 굴종적인 태도입니다."),
                ("Give the raiders a one-plus-one dress discount.", "기업 사냥꾼들에게 원플러스원 드레스 할인을 제안합시다.", "‘one-plus-one’은 콩글리시입니다."))
           ]),
        mk("메트로폴리탄 미술관 회고전: 불멸의 패션 레거시", "Miranda Priestly (Editor-in-Chief)", "👗",
           "뉴욕 메트 갈라 레드카펫 오프닝. 당신의 30년 패션 여정을 총망라한 단독 회고전이 열린다. 전 세계 카메라 앞에서 패션의 진정한 예술성을 선언해야 한다.",
           "cement the immortal fashion legacy at the Met Gala",
           "메트로폴리탄 미술관 회고전을 통해 일시적 유행을 넘어선 불멸의 예술적 레거시를 각인시킬 때 쓰는 표현입니다.",
           [
               ("All seven hundred steps of the Met are lined with the world's elite. You're the first independent designer in thirty years to receive a solo retrospective. Speak to history.",
                "메트 계단 전체가 전 세계 엘리트들로 가득 찼네. 30년 만에 단독 회고전을 여는 최초의 독립 디자이너야. 역사 앞에 한 말씀 남기게.",
                "패션은 껍데기가 아니라 영혼을 보호하는 갑옷이라는 철학을 품격 있게 전하세요.",
                ("Fashion is not frivolity—it is the armor we wear to face the battles of the world. May this collection remind us that beauty is humanity's most resilient defiance.", "패션은 사치가 아닙니다. 세상의 모든 풍파에 맞서기 위해 우리가 입는 영혼의 갑옷입니다. 이 컬렉션이 아름다움이란 인간의 가장 강인한 저항임을 증명하길 바랍니다.", "메트 갈라 역사에 영원히 남을 장엄하고 감동적인 헌사입니다."),
                ("I am happy my clothes are very expensive now.", "내 옷들이 이제 아주 비싸져서 기쁩니다.", "장인의 위대한 회고전을 돈벌이로 격하시키는 천박한 소감입니다."),
                ("Let's do Dutch pay for the after-party cocktail.", "애프터 파티 칵테일은 더치페이로 마십시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    # 14. Crisis PR Management
    d["Crisis PR Management"] = [
        mk("CEO 딥페이크 비자금 영상 바이럴: 1시간 내 포렌식 반박", "Olivia Pope (Crisis Management Director)", "🚨",
           "글로벌 테크 기업 CEO가 마약과 비자금을 요구하는 조작 딥페이크 영상이 트위터 1위에 올랐다. 주가 폭락을 막고 1시간 안에 기술적 위조를 증명해야 한다.",
           "debunk the viral deepfake with forensic biometric proof",
           "SNS에 바이럴된 악성 딥페이크 영상을 생체 음성 및 광학 포렌식 증거로 신속히 반박해 위기를 진화할 때 쓰는 PR 표현입니다.",
           [
               ("The video has eighty million views in forty minutes! The stock dropped fifteen percent! The board is demanding the CEO resign by noon. How do we kill the viral fire?",
                "영상이 40분 만에 8천만 뷰를 찍었어! 주가는 15% 폭락했고! 이사회가 정오까지 CEO 사임을 요구하고 있어. 이 바이럴 화재를 어떻게 끌 거지?",
                "영상 속 동공 반사와 음성 스펙트로그램의 인공 합성 결함을 즉시 팩트체크 영상으로 공개하자고 하세요.",
                ("Do not resign! We publish an emergency forensic biometric breakdown showing the irregular eye-reflection artifacts and synthetic audio latency. We turn the story into an attack on democracy.", "사임은 절대 안 됩니다! 눈동자 빛 반사 아티팩트와 합성 음성 지연을 증명하는 생체 포렌식 분석 영상을 즉시 배포하십시오. 이 사태를 민주주의에 대한 사이버 테러 프레임으로 역전시킵니다.", "‘forensic biometric breakdown’과 ‘turn the story’는 위기관리 PR의 교과서적인 프레임 전환술입니다."),
                ("Let's apologize to the public for the bad video.", "나쁜 영상에 대해 대중에게 머리 숙여 사과합시다.", "조작된 가짜 영상에 사과하여 혐의를 인정하는 치명적인 자살골입니다."),
                ("The video has bad spec so claim Twitter.", "영상이 스펙이 나쁘니 트위터에 클레임을 겁시다.", "‘spec’과 ‘claim’은 콩글리시입니다."))
           ]),
        mk("글로벌 리콜 사태: 의회 청문회 전야 혹독한 모의 훈련", "Olivia Pope (Crisis Management Director)", "🚨",
           "자율주행 소프트웨어 결함 의혹으로 의회 청문회에 소환된 CEO. 공격적인 상원의원들의 질문을 돌파할 미디어 트레이닝을 완수해야 한다.",
           "prep the CEO to withstand hostile congressional grilling",
           "공격적인 의회 청문회 압박 신문에 맞서 최고경영자의 흔들림 없는 답변 태도와 메시지를 훈련시킬 때 쓰는 표현입니다.",
           [
               ("Senator Hayes will put victim families in the front row and call the CEO a cold-blooded murderer on live television. How do we keep him from losing his temper?",
                "헤이즈 의원은 피해자 유가족을 방청석 맨 앞줄에 앉혀두고 생방송에서 CEO를 냉혈한 살인마라고 몰아세울 거야. 그가 평정심을 잃지 않게 어떻게 훈련시키지?",
                "공격에 맞받아치지 말고 유가족을 향해 깊은 애도를 표한 뒤 안전 혁신을 위한 무제한 공개 검증을 선언하게 하세요.",
                ("Every attack must be pivoted with solemn empathy. He looks the families in the eye, shares their grief, and immediately pledges an open-source safety audit with zero defensiveness.", "모든 공격적인 질문을 진심 어린 공감으로 피벗하십시오. 가족들의 눈을 똑바로 바라보며 슬픔을 나누고, 어떤 변명도 없이 전면 오픈소스 안전 감사를 서약하게 만듭니다.", "‘pivoted with solemn empathy’와 ‘zero defensiveness’는 의회 청문회 여론전을 완승으로 이끄는 정석입니다."),
                ("Tell the senator that he is an idiot who knows nothing about software.", "소프트웨어도 모르는 바보라고 상원의원에게 소리치게 합시다.", "의회 모욕죄로 체포되어 기업을 완전히 파멸시킵니다."),
                ("Do morning call to the CEO so he is not sleepy in Congress.", "의회에서 졸지 않도록 CEO에게 모닝콜을 해주세요.", "‘morning call’은 콩글리시입니다."))
           ]),
        mk("정치인 스캔들: 기자회견장 프레임 전환의 마술", "Olivia Pope (Crisis Management Director)", "🚨",
           "대선 후보의 혼외자 스캔들이 터지기 30분 전. 폭로 언론사의 프레임을 무력화하고 오히려 유권자의 감동을 이끌어내는 기자회견을 설계해야 한다.",
           "pivot the media narrative from scandal to redemption",
           "치명적인 사생활 스캔들을 진솔한 고백과 구원의 서사로 전환해 지지율 반등을 이끌어낼 때 쓰는 표현입니다.",
           [
               ("The Washington Post is going to print in twenty minutes with the mistress's sworn affidavit. If we stay silent, his political career is buried. What's the play?",
                "워싱턴 포스트가 20분 뒤에 내연녀의 진술서를 인쇄기에 걸 예정이야. 침묵하면 후보의 정치 생명은 매장돼. 우리의 작전이 뭐야?",
                "신문 인쇄 전에 아내와 함께 긴급 생방송 기자회견을 열어 과오를 고백하고 가족의 용서를 구하는 선제타격을 하세요.",
                ("We preempt their print run. The candidate walks out with his wife, owns his past human failing without evasion, and asks the American people for grace. We control the narrative.", "신문 인쇄를 선제 차단합니다. 후보가 아내의 손을 잡고 나와 과거의 인간적 과오를 회피 없이 인정하고, 국민에게 용서를 구하게 하십시오. 우리가 내러티브를 통제합니다.", "‘preempt their print run’과 ‘control the narrative’는 스캔들을 잠재우는 올리비아 팝 스타일의 마스터스트로크입니다."),
                ("Let's pay ten million dollars to bribe the newspaper editor.", "신문사 편집장에게 1천만 달러를 주고 뇌물로 입을 막읍시다.", "사법 방해죄로 형사 처벌을 받는 범죄 행위입니다."),
                ("Send an SNS selfie to show their family skinship.", "가족 스킨십을 보여주기 위해 SNS 셀카를 올립시다.", "‘skinship’과 ‘SNS’는 콩글리시입니다."))
           ]),
        mk("국가적 재난 위기 커뮤니케이션: 국민 신뢰 회복의 대단원", "Olivia Pope (Crisis Management Director)", "🚨",
           "전국적인 통신망 블랙아웃 사태 속에서 기업의 책임을 인정하고, 100% 보상안과 재발 방지책을 발표해 신뢰를 되살려야 한다.",
           "restore public trust with radical accountability and restitution",
           "국가적 위기 속에서 완전한 투명성과 즉각적인 피해보상으로 무너진 공공의 신뢰를 재건할 때 쓰는 표현입니다.",
           [
               ("The entire country was without 911 emergency communications for six hours. The public outrage is incandescent. What is our closing message to the nation?",
                "전국 911 긴급 통신망이 6시간 동안 마비되었어. 국민적 분노가 백열등처럼 타오르고 있네. 국민들을 향한 우리의 최종 메시지가 무엇인가?",
                "어떤 핑계도 대지 않고 전액 피해 보상과 영구적 독립 안전 위원회 설치를 국민 앞에 무릎 꿇고 약속하세요.",
                ("We offer zero excuses. We pledge full restitution to every affected citizen and surrender our network architecture to independent public oversight. We earn back your trust step by step.", "어떤 핑계도 대지 않겠습니다. 피해를 입은 모든 국민께 전액 배상하고, 통신망 구조를 독립 시민 감시단에 완전히 개방하겠습니다. 여러분의 신뢰를 한 걸음씩 다시 얻겠습니다.", "‘zero excuses’와 ‘independent public oversight’는 국가적 재난에서 기업을 살려내는 진정성의 극치입니다."),
                ("Tell the public that technology sometimes breaks down so they should deal with it.", "기술은 가끔 고장 나는 법이니 국민들이 알아서 감수하라고 전합시다.", "불매 운동과 집단 소송을 폭발시키는 최악의 망언입니다."),
                ("Let's do Dutch pay for the emergency damage repair.", "비상 복구 비용은 국민들과 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    # Helper function for procedural expansion of remaining 16 genres
    return d

