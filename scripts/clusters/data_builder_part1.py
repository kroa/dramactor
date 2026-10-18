# -*- coding: utf-8 -*-
"""
Dramactor Scenario Data Builder: Part 1 (Genres 16 to 27: 12 genres x 4 = 48 episodes)
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
26: Diplomatic Statecraft & Embassy
27: Bio-Hazard & Epidemiology
"""
import sys, os
sys.path.append(os.path.dirname(__file__))
from helper import make_episode, make_turn

def get_builder_part1():
    data = {}
    def mk(t, s, e, syn, ke, kn, turns):
        return make_episode(t, s, e, syn, ke, kn, [make_turn(x[0], x[1], x[2], x[3], x[4], x[5]) for x in turns])

    # 16. Hollywood Talent Agency
    data["Hollywood Talent Agency"] = [
        mk("2억 달러 SF 대작 거장 감독 촬영장 하차 위기", "Ari Gold (Chairman of Talent & Media)", "🎬",
           "워너 브라더스 스튜디오 사운드스테이지. 제작비 2억 달러의 블록버스터 촬영 첫 주, 스튜디오 임원이 거장 감독의 촬영 스타일을 간섭하자 감독이 촬영 중단을 선언했다. 최종 편집권(Final Cut)을 지켜내야 한다.",
           "protect director's final cut privilege against studio interference", "스튜디오의 간섭에 맞서 감독의 최종 편집 권한을 사수할 때 쓰는 표현입니다.",
           [
               ("The studio head is on set demanding we cut thirty pages of dialogue! The director just locked himself in his trailer! We're burning three hundred thousand an hour! Fix this, Ari!",
                "스튜디오 대표가 촬영장에 와서 대사 30페이지를 잘라내라고 난리야! 감독은 트레일러에 문 잠그고 틀어박혔어! 시간당 30만 달러씩 날아가고 있다고! 해결해, 아리!",
                "감독의 트레일러 문을 두드려 스튜디오 대표의 오스카 야망을 자극해 타협 없는 최종 편집권을 받아내겠다고 안심시키세요.",
                ("Step aside, Alan. I'm going into that trailer. I will make the studio head swallow his budget notes and guarantee uncompromised final cut by sundown.", "비켜봐요, 앨런. 내가 저 트레일러로 들어갑니다. 스튜디오 대표가 예산 간섭을 스스로 철회하고 해 지기 전에 완전한 최종 편집권을 보장하도록 만들겠습니다.", "‘swallow budget notes’와 ‘guarantee final cut’은 할리우드 슈퍼 에이전트의 거침없는 카리스마입니다."),
                ("Let's tell the director to say sorry to the studio head.", "감독에게 스튜디오 대표한테 사과하라고 전합시다.", "거장 감독의 자존심을 짓밟고 영화를 파멸시키는 최악의 조언입니다."),
                ("The camera has bad spec so call the AS center.", "카메라 스펙이 안 좋으니 AS 센터에 전화합시다.", "‘spec’과 ‘AS’는 콩글리시입니다.")),
               ("Director opened the door. But the studio head demands twenty million in personal liability insurance if the film goes three days over schedule.",
                "감독이 문을 열었어. 하지만 스튜디오 대표가 촬영 일정이 사흘만 밀려도 2천만 달러의 개인 배상 보험을 걸라고 요구하고 있어.",
                "해외 사전 배급 판권 8천만 달러 선판매 카드를 테이블에 올려 스튜디오의 재정 위험을 완전히 제거하라고 하세요.",
                ("I just closed eighty million in non-refundable foreign pre-sales at Cannes. The studio has zero downside risk. Give my director total creative autonomy.", "내가 방금 칸에서 8천만 달러의 환불 불가 해외 사전 판권을 계약했습니다. 스튜디오의 다운사이드 위험은 0%입니다. 내 감독에게 완전한 창작 자율성을 보장하십시오.", "‘non-refundable foreign pre-sales’와 ‘zero downside risk’는 스튜디오의 간섭을 완전히 분쇄하는 금융 무기입니다."),
                ("Tell the studio head that he is very greedy.", "스튜디오 대표에게 너무 욕심이 많다고 따집시다.", "감정적 비난으로 협상을 결렬시키는 아마추어적 태도입니다."),
                ("Check the handphone for movie ticket reservations.", "영화 예매를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Cameras rolling! Studio head signed the final cut rider! The rough footage is being called a cinematic masterpiece! You saved the picture, Ari.",
                "촬영 재개! 스튜디오 대표가 최종 편집권 특약에 서명했어! 가편집본이 시네마틱 걸작이라고 평가받고 있네! 자네가 영화를 살려냈어, 아리.",
                "할리우드에서 진정한 예술은 오직 타협 없는 신념으로만 지켜진다고 승리를 선언하세요.",
                ("In this town, Alan, commerce bows to genius when you hold the leverage. That's why I get ten percent. Back to work!", "이 동네에서 상업은 레버리지를 쥔 천재성 앞에 무릎 꿇는 법입니다, 앨런. 그게 내가 수수료 10%를 챙기는 이유입니다. 다시 일합시다!", "미드 엔투라지의 아리 골드 명대사를 완벽히 재현한 피날레입니다."),
                ("I am glad we can watch movies for free now.", "이제 영화를 공짜로 볼 수 있어서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the studio steak dinner.", "스튜디오 스테이크 저녁은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("오스카 남우주연상 캠페인 vs 히어로 프랜차이즈 속편", "Ari Gold (Chairman of Talent & Media)", "🎬",
           "베벌리힐스 포시즌스 호텔 프라이빗 스위트. 아카데미 남우주연상 유력 후보인 톱배우가 3천만 달러 히어로 무비 속편 계약과 예술영화 캠페인 사이에서 갈등하고 있다.",
           "orchestrate a historic dual-track Academy Award campaign", "상업적 메가히트 계약과 오스카 오스카 캠페인을 동시에 석권하는 투트랙 전략을 성사시킬 때 쓰는 표현입니다.",
           [
               ("Marvel wants a four-picture commitment by Friday with twenty million up front. But the Academy voters will look down on superhero spandex! What's the strategy?",
                "마블이 선급금 2천만에 4편 연동 계약을 금요일까지 서명하래. 하지만 아카데미 투표인단은 쫄쫄이 히어로 무비를 폄하할 거야! 전략이 뭐야?",
                "마블 계약을 비공개 엠바고로 묶어 오스카 투표 마감 후 발표되도록 일정을 조율하자고 제안하세요.",
                ("We lock the Marvel deal under an ironclad press embargo. We announce the superhero contract at Comic-Con the Monday after you win the Oscar. You get both.", "마블 계약을 철통 엠바고로 묶어두십시오. 오스카 트로피를 수상한 직후 월요일 코믹콘에서 히어로 계약을 발표합니다. 트로피와 1억 달러, 둘 다 손에 쥡니다.", "‘ironclad press embargo’와 ‘announce at Comic-Con’은 예술적 명예와 상업적 거금을 모두 쟁취하는 에이전트의 묘수입니다."),
                ("Tell Marvel that comic books are stupid.", "마블에게 만화책은 멍청하다고 말하세요.", "거액의 기회를 스스로 차버리는 무지한 처사입니다."),
                ("The actor has bad personality so let's claim to him.", "배우가 인성이 나쁘니 그에게 클레임합시다.", "‘claim’은 콩글리시입니다.")),
               ("Academy voters are being swayed by the British candidate. The New York Times published a profile calling our actor a superficial Hollywood celebrity.",
                "아카데미 투표인단이 영국 후보 쪽으로 기울고 있어. 뉴욕타임스가 우리 배우를 천박한 할리우드 연예인이라 깎아내리는 기획 기사를 냈네.",
                "LA 타임스와 버라이어티에 그의 10년간의 인디 연극 헌신과 자선 활동을 조명하는 커버 스토리를 전격 릴리즈하세요.",
                ("Counter with a front-page deep-dive in Variety detailing his fifteen years of classical theater and grassroots philanthropy. Reframe him as an auteur actor.", "버라이어티 1면에 그의 15년간의 고전 연극 헌신과 자선 활동을 심층 보도하십시오. 상업 스타가 아닌 진정한 예술가로 대중의 인식을 재구성합니다.", "‘front-page deep-dive’와 ‘reframe as an auteur actor’는 오스카 판세를 뒤집는 여론 공작의 정석입니다."),
                ("Let's cry and beg the New York Times editor.", "뉴욕타임스 편집장에게 울면서 빌어봅시다.", "아마추어 같고 신뢰를 떨어뜨리는 행동입니다."),
                ("Check the handphone for movie reviews.", "영화 리뷰를 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("And the Oscar goes to... our boy! Standing ovation at the Dolby Theatre! And Marvel just added ten million in backend gross points! You played them like a violin, Ari.",
                "오스카 남우주연상 수상자는... 우리 배우야! 돌비 극장 전원 기립박수! 게다가 마블이 백엔드 흥행 지분 1천만 달러를 추가했네! 자네가 완벽하게 판을 짰어, 아리.",
                "타협하지 않고 최고의 가치를 쟁취하는 것이 할리우드를 지배하는 법이라고 답하세요.",
                ("Gold on the mantle and fifty million in the bank account. That is how Ari Gold does business in Hollywood. Celebrate tonight, conquer tomorrow!", "벽난로 위의 황금 트로피와 통장 속 5천만 달러. 그것이 아리 골드가 할리우드에서 비즈니스하는 방식입니다. 오늘 밤 축하하고, 내일은 세상을 정복합시다!", "할리우드 최고 에이전트의 위엄을 폭발시키는 대사입니다."),
                ("I am glad we don't have to wear suits tomorrow.", "내일 정장 안 입어도 돼서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Beverly Hills champagne.", "베벌리힐스 샴페인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("스트리밍 공룡의 인디 스튜디오 배급권 인수합병", "Ari Gold (Chairman of Talent & Media)", "🎬",
           "선댄스 영화제 메인 스트리트. 심야 상영에서 폭발적 반응을 얻은 인디 걸작의 전 세계 배급권을 두고 넷플릭스와 전통 극장 체인이 5천만 달러 입찰 전쟁을 벌인다.",
           "maximize global theatrical window rights against streaming dominance", "스트리밍 플랫폼의 독점에 맞서 극장 독점 상영 기간과 글로벌 배급권을 극대화할 때 쓰는 표현입니다.",
           [
               ("Netflix offers sixty million for full global rights, but straight to streaming with zero theatrical release! The director refuses to sign. Universal offers thirty with a 45-day window.",
                "넷플릭스가 6천만 달러에 전 세계 판권을 부르며 극장 상영 없는 직행 스트리밍을 고집해! 감독은 서명을 거부하고 있어. 유니버설은 45일 극장 상영에 3천만을 불렀네.",
                "넷플릭스에 2주간의 전 세계 IMAX 극장 한정 상영 조항을 강제하여 6천만 달러 계약을 관철하자고 하세요.",
                ("Demand an exclusive two-week worldwide IMAX qualifying theatrical run from Netflix. They get their prestige streaming buzz, and my director gets his cinema legacy.", "넷플릭스에 2주간의 전 세계 IMAX 극장 독점 상영 조항을 강제하십시오. 그들은 스트리밍 화제성을 얻고, 내 감독은 영화관의 유산을 지킵니다.", "‘exclusive theatrical run’과 ‘prestige buzz’는 스트리밍 공룡을 길들이는 최고의 절충안입니다."),
                ("Tell the director that movie theaters are all going bankrupt.", "감독에게 영화관은 다 망하고 있다고 핀잔을 줍시다.", "아티스트의 신념을 짓밟는 무례한 처사입니다."),
                ("The projector has bad spec so tell the festival.", "영사기 스펙이 안 좋으니 영화제 측에 따집시다.", "‘spec’은 콩글리시입니다.")),
               ("Netflix agreed to the theatrical window! But now their legal team wants all future sequel and television spin-off rights bundled for free. What's the retort?",
                "넷플릭스가 극장 상영에 동의했어! 그런데 법무팀이 향후 모든 속편과 TV 스핀오프 판권을 공짜로 묶어가겠다고 억지를 부려. 반격 답변은?",
                "스핀오프 판권은 감독의 소유로 분리하고 향후 우선 매수권(First Look)만을 부여하겠다고 못 박으세요.",
                ("Tell their lawyers to take a cold shower. Ancillary and episodic spin-off rights remain strictly with my client. They get a first-look matching right, nothing more.", "법무팀에 찬물 끼얹고 정신 차리라고 하세요. 부가 판권과 시리즈 스핀오프 권리는 오직 내 의뢰인 소유입니다. 그들에게 주어지는 것은 우선 협상권뿐입니다.", "‘first-look matching right’와 ‘ancillary rights’는 미래의 수천억 원 가치를 지켜내는 법적 안전판입니다."),
                ("Let's give them all future rights so they are happy.", "그들이 좋아하도록 미래 권리를 다 줘버립시다.", "자산 가치를 날려버리는 무능한 협상입니다."),
                ("Check the handphone for festival schedule.", "영화제 일정을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("Deal closed! Sixty-five million record sale at Sundance! The contract includes worldwide IMAX premiere and retained sequel rights! You just redefined indie cinema.",
                "계약 체결! 선댄스 영화제 역사상 최고액인 6,500만 달러 매각 성사! 전 세계 IMAX 개봉과 속편 권리 보장 포함! 자네가 인디 영화의 역사를 다시 썼네.",
                "진정한 에이전트는 거대 자본 속에서도 예술의 독립성을 수호하는 방패라고 답하세요.",
                ("We don't bow to streaming algorithms, Ari—we command them. Cinema is alive, and my client is rich. That's a wrap!", "우리는 스트리밍 알고리즘에 굴복하지 않습니다, 아리. 알고리즘을 지휘할 뿐입니다. 시네마는 살아있고 내 의뢰인은 부자가 되었습니다. 촬영 끝!", "할리우드 비즈니스의 통쾌한 승리를 선언하는 피날레입니다."),
                ("I am glad we don't have to freeze in Utah anymore.", "유타주 추위에서 더 이상 안 떨어도 돼서 참 좋습니다.", "가벼운 태도로 감동을 반감시킵니다."),
                ("Let's do Dutch pay for the Park City fondue.", "파크시티 퐁뒤는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ]),
        mk("칸 영화제 황금종려상 경쟁작 도난 필름 협상", "Ari Gold (Chairman of Talent & Media)", "🎬",
           "프랑스 리비에라 칸 팔레 데 페스티발. 황금종려상 유력 경쟁작의 최종 DCP 마스터 하드디스크가 호텔 금고에서 도난당했다. 시사회 4시간 전, 몸값 요구 협박을 분쇄하고 영화를 상영해야 한다.",
           "neutralize the film extortionist and secure the premiere DCP master",
           "영화 도난 협박범을 무력화하고 월드 프리미어 마스터 상영본을 사수할 때 쓰는 표현입니다.",
           [
               ("The master hard drive is stolen! Extortionists demand two million euros in encrypted crypto within ninety minutes or they stream the unreleased movie on the dark web!",
                "마스터 하드드라이브를 도난당했어! 협박범들이 90분 안에 암호화폐 2백만 유로를 보내지 않으면 다크웹에 미공개 영화를 생중계하겠대!",
                "송금을 거부하고 디지털 워터마크 추적 코드를 가동해 로컬 와이파이 맥 주소를 역추적하라고 지시하세요.",
                ("Do not wire a single euro. Trigger the forensic forensic digital watermark. Isolate their IP ping within the Croisette fiber loop and dispatch French federal police now.", "단 1유로도 송금하지 마십시오. 법의학적 디지털 워터마크를 가동하세요. 크루아제트 광통신망 내에서 그들의 IP 신호를 특정하고 프랑스 연방경찰을 급파하십시오.", "‘forensic digital watermark’와 ‘isolate IP ping’은 협박범의 목줄을 죄는 최첨단 기술 수사 지시입니다."),
                ("Cry and beg the thief not to upload the film.", "영화 올리지 말아 달라고 도둑에게 울며불며 빌어봅시다.", "조롱만 당하고 영화는 유출되는 최악의 반응입니다."),
                ("The computer spec is bad so buy a new USB.", "컴퓨터 스펙이 안 좋으니 새 USB를 사 오세요.", "‘spec’은 콩글리시입니다.")),
               ("Police raided their yacht and recovered the drive! But the opening reel is corrupted from forced decryption attempts. The red carpet opens in thirty minutes.",
                "경찰이 요트를 급습해 하드드라이브를 회수했어! 하지만 강제 복호화 시도로 오프닝 릴 파일이 깨졌어. 레드카펫 입장이 30분 남았네.",
                "런던 포스트 프로덕션 랩의 클라우드 콜드 스토리지 백업에서 오프닝 릴을 인공위성 전용선으로 직송받으라고 명령하세요.",
                ("Establish a dedicated satellite uplink to our London Soho post-production facility. Download the lossless ProRes master reel directly into the Palais projection servers.", "런던 소호 후반작업 스튜디오로 위성 전용선을 연결하십시오. 무손실 프로레스(ProRes) 마스터 릴을 팔레 상영관 서버로 직접 다운로드하십시오.", "‘dedicated satellite uplink’와 ‘lossless ProRes master’는 상영 참사를 막는 프로페셔널한 기술 대처입니다."),
                ("Tell the festival jury to imagine the first ten minutes.", "영화제 심사위원들에게 첫 10분은 상상해서 보라고 하세요.", "국제적 조롱거리가 되는 황당한 발언입니다."),
                ("Check the handphone for Cannes party tickets.", "칸 파티 티켓을 보려고 핸드폰을 켜세요.", "‘handphone’은 콩글리시입니다.")),
               ("The projection started on time! Flawless screening! Twenty-minute standing ovation! The jury just announced the Palme d'Or! You pulled off a miracle in Cannes.",
                "상영이 정시에 시작되었어! 무결점 스크리닝! 20분간의 전원 기립박수! 심사위원단이 방금 황금종려상을 발표했어! 자네가 칸에서 기적을 일궈냈네.",
                "위대한 시네마는 도둑의 손에 꺾이지 않고 빛으로 세상을 비춘다고 승리를 자축하세요.",
                ("Great cinema cannot be held hostage, Ari. When art speaks to the soul, the entire world bows in reverence. Viva le cinéma!", "위대한 영화는 인질로 붙잡힐 수 없습니다, 아리. 예술이 인간의 영혼에 말을 건넬 때, 온 세상은 경의로 무릎 꿇습니다. 영화 만세!", "칸 영화제 황금종려상의 감동을 완성하는 완벽한 피날레입니다."),
                ("I am glad we can eat baguettes now.", "이제 바게트 빵을 먹을 수 있어서 참 좋습니다.", "가벼운 태도로 엄숙한 분위기를 흐립니다."),
                ("Let's do Dutch pay for the Riviera wine.", "리비에라 와인은 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    return data

