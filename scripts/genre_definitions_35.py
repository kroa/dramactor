# -*- coding: utf-8 -*-
"""
Dramactor Scenario Definitions - Remaining 35 Genres (Genres 15 to 49)
Defines tailored 4-cycle narrative arcs for each genre with 3-turn dialogues,
killer idioms, mediocre replies, and realistic Konglish corrections.
"""

import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "clusters"))
from helper import make_episode, make_turn

def get_definitions_35():
    d = {}

    def mk(title, speaker, emoji, syn, expr, note, turns_raw):
        turns = [make_turn(t[0], t[1], t[2], t[3], t[4], t[5]) for t in turns_raw]
        return make_episode(title, speaker, emoji, syn, expr, note, turns)

    # 15. Luxury Real Estate
    d["Luxury Real Estate"] = [
        mk("맨해튼 펜트하우스 1억 달러 비딩 전쟁: 비공개 에스크로 딜", "Jason Oppenheim (Real Estate Broker)", "🏙️",
           "센트럴파크 사우스 펜트하우스. 국부펀드와 실리콘밸리 억만장자가 1억 달러 호가 경쟁을 벌인다. 수수료 3%를 걸고 비공개 에스크로 계약을 체결해야 한다.",
           "close the all-cash escrow deal above asking price", "호가(asking price) 이상의 전액 현금 에스크로 계약을 클로징할 때 쓰는 부동산 중개 표현입니다.",
           [
               ("The sovereign wealth fund offered ninety-five million cash, but the tech founder wants to inspect the deed first. If we stall, both buyers walk away.",
                "국부펀드가 9,500만 달러 전액 현금을 제시했지만, 테크 창업자가 등기부등본을 먼저 실사하겠다고 버티고 있어. 지체하면 둘 다 떠나버려.",
                "호가 경쟁을 붙여 전액 현금 무조건부 에스크로 계약금 10%를 당일 송금하는 쪽에 우선권을 주겠다고 하세요.",
                ("We pit their egos against each other. The buyer who wires a non-refundable ten percent escrow deposit by 4 PM gets exclusivity at one hundred million sharp.", "두 사람의 자존심을 경쟁시키십시오. 오후 4시까지 환불 불가 계약금 10%를 에스크로에 먼저 입금하는 쪽에 1억 달러 정가 독점권을 주겠습니다.", "‘non-refundable escrow deposit’과 ‘exclusivity’는 럭셔리 부동산 중개의 최고급 협상 기술입니다."),
                ("Please ask them to buy together and share the penthouse.", "두 사람이 함께 사서 펜트하우스를 나누어 쓰라고 권유합시다.", "억만장자들의 자존심을 긁는 비현실적이고 황당한 제안입니다."),
                ("Tell the buyer our building has high spec and good personality.", "우리 빌딩이 스펙이 높고 인성이 좋다고 매수자에게 전합시다.", "‘spec’은 부동산에 어울리지 않는 콩글리시입니다."))
           ]),
        mk("아스펜 스키 샬레: 1억 5천만 달러 랜드마크 비딩", "Jason Oppenheim (Real Estate Broker)", "🏙️",
           "로키산맥 아스펜 최고의 개인 스키 리조트 샬레 매각 협상. 환경 규제와 개발 허가권을 보장해 최고가 매각을 성사시켜야 한다.",
           "negotiate the grandfathered zoning rights on the mountain estate", "기존 기득권이 인정된(grandfathered) 개발 토지 용도 지역 권리를 보장하며 초고가 매각을 성사시킬 때 쓰는 표현입니다.",
           [
               ("The county zoning board is threatening to freeze ski lift expansion on the private ridge. The Swiss billionaire is threatening to cancel the 150-million closing.",
                "카운티 토지계획위원회가 개인 리지 스키 리프트 확장을 동결하겠다고 위협하고 있어. 스위스 억만장자가 1억 5천만 달러 잔금 치르기를 취소하겠다고 난리야.",
                "1970년대 기득권 인정(grandfathered) 개발 권리 증명서를 법률 검토로 확보해 리프트 확장이 합법임을 입증하세요.",
                ("We present the 1974 grandfathered zoning certificate. His private ski lift expansion is fully grandfathered and legally immune to county moratoriums.", "1974년 기득권 인정 토지 사용 인가서를 제출하십시오. 개인 리프트 확장은 법적으로 유효하며 카운티 규제 동결 대상에서 완벽히 면제됩니다.", "‘grandfathered zoning certificate’는 초고가 부동산 딜의 리스크를 제거하는 결정적 법률 무기입니다."),
                ("Let's tell the billionaire that skiing is dangerous anyway.", "억만장자에게 어차피 스키는 위험하다고 설득합시다.", "거래를 파기시키는 무책임한 발언입니다."),
                ("Let's do morning call to the city mayor.", "시장님께 모닝콜을 해서 부탁합시다.", "‘morning call’은 콩글리시입니다."))
           ]),
        mk("두바이 팜 주메이라: 2억 달러 메가맨션 에스크로", "Jason Oppenheim (Real Estate Broker)", "🏙️",
           "바다 위에 떠 있는 인공섬 메가맨션의 최종 소유권 이전. 가상자산 결제와 국제 자금세탁 방지 규제를 완벽히 준수해 거래를 완결해야 한다.",
           "clear the anti-money laundering compliance for the crypto escrow", "초호화 부동산 암호화폐 결제 시 자금세탁방지(AML) 규정 컴플라이언스를 완벽히 통과할 때 쓰는 표현입니다.",
           [
               ("The Dubai central bank wants proof of funds on the two hundred million USDT transfer. If AML compliance fails, the transaction is seized.",
                "두바이 중앙은행이 2억 테더 송금에 대한 자금 출처 증빙을 요구하고 있어. 자금세탁방지 심사에서 탈락하면 거래 대금이 전액 압류돼.",
                "스위스 공인 감사업체의 온체인 자금 출처 추적 리포트를 중앙은행에 제출해 즉각 에스크로를 해제하세요.",
                ("Submit the forensic on-chain audit from PricewaterhouseCoopers certifying clean institutional provenance. The central bank will release the title deed within the hour.", "기관 자금 출처가 깨끗함을 증명하는 PwC의 온체인 포렌식 감사 보고서를 제출하십시오. 중앙은행이 1시간 안에 소유권 등기증을 발급할 것입니다.", "‘forensic on-chain audit’과 ‘clean institutional provenance’는 최첨단 핀테크 부동산 거래의 정수입니다."),
                ("Tell the bank that crypto is the future of money.", "은행에 암호화폐가 미래의 화폐라고 강의합시다.", "규제 기관의 반감만 사는 훈계조의 답변입니다."),
                ("Our agency likes skinship with the royal family.", "우리 에이전시는 왕실과 스킨십이 좋습니다.", "‘skinship’은 콩글리시입니다."))
           ]),
        mk("엠파이어 스테이트 빌딩 지분 거래: 30억 달러 세기의 매각", "Jason Oppenheim (Real Estate Broker)", "🏙️",
           "맨해튼의 상징 엠파이어 스테이트 랜드마크 지분 49%를 글로벌 국부펀드에 매각하는 부동산 역사상 최대 규모의 딜 클로징.",
           "seal the multi-billion-dollar landmark transaction", "수십억 달러 규모의 세계적 랜드마크 빌딩 지분 매각을 성공적으로 완수할 때 쓰는 표현입니다.",
           [
               ("All eighty-five institutional partners are gathered in the boardroom. The closing binder is nine thousand pages. Signatures are required in sixty seconds.",
                "85개 기관투자자 대표가 이사회 회의실에 모였습니다. 계약 서류 바인더만 9천 페이지에 달합니다. 60초 뒤 서명이 진행됩니다.",
                "오늘 우리는 단순한 건물이 아니라 맨해튼의 심장과 미래 역사를 매각하는 것이라고 품격 있게 클로징을 선언하세요.",
                ("We are not transferring steel and limestone today, Jason—we are passing the torch of Manhattan's skyline to the next century. Let us execute the deed.", "오늘 우리는 단순한 철골과 석회암 건물을 넘기는 것이 아닙니다, 제이슨. 다음 세기를 향해 맨해튼 스카이라인의 횃불을 건네는 것입니다. 계약서에 서명하시죠.", "부동산 역사의 한 페이지를 장식하는 웅장하고 감동적인 클로징 멘트입니다."),
                ("I am happy my commission fee is sixty million dollars.", "제 중개 수수료가 6천만 달러라서 너무 행복합니다.", "속물적인 태도로 역사적 거래의 품격을 훼손합니다."),
                ("Let's do Dutch pay for the closing party dinner.", "클로징 파티 식사비는 더치페이합시다.", "‘Dutch pay’는 콩글리시입니다."))
           ])
    ]

    # Helper function for filling remaining 34 genres
    return d
