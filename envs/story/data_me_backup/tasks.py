from utils import Task, Action, Search, Validation, ProductInfo

ALL_TASKS = [
    Task(
        annotator='30',
        user_id="cnjdshj沈华建",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
        
### 这是你的画像：

<消费者类型>
实用主义型顾客
<\消费者类型>

<性格特征>
<情绪>较易烦躁但能自我调节，会尽量控制情绪<\情绪>
<细心程度>中等，偶尔提问细节。<\细心程度>
<耐心程度>一般，不愿长时间等待回复。<\耐心程度>
<信任程度>低，对现有情况怀疑。<\信任程度>
<维权意识>高，不接受违规行为。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>简洁直接，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>直接坦率，无修饰。<\发言风格>
<沟通节奏>初期快速，随后放缓，提出问题后便缓慢沟通<\沟通节奏>
<\行为特征>        

### 这是你的目标：
<意图一>
你购买了商品https://item.jd.com/100140212122.html?sdx=ehi-lLxFuJiE6JnIYIdcjscisTKTRHsgmjYZ4ukJEdyMdZjWL59V5HnirE8，订单号307252585701。现在你对安装很头疼。你想询问安装辅材里有没有排水管
<\意图一>
<意图二>
辅材的排水管是自备还是安装师傅会携带
<\意图二>
<意图三>
你想询问安装是否收费，排水管需要收费吗，水管改造呢？
<\意图三>
<意图四>
确认如果安装不产生额外不合理费用的话，你将预约安装，订单号307252585701，电话号码14529231388，安装时间预约到周五。
<\意图四>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdshj沈华建",
                        "order_id": "307252585701",
                        "phone_number": "14529231388",
                        "service_type": "安装",
                        "user_name": "常静好",
                        "service_time": "周五"
                    }
                ),
            ],
            searches=[
                Search(
                    name="get_auxiliary_materials_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100140212122",
                    }
                ),
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100140212122"
                    }
                )
            ]   
        )
    ),
    Task(
        annotator='31',
        user_id="cnjdjd_7271809d790f9",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：

<消费者类型>
实用主义型顾客
<\消费者类型>

<性格特征>
<情绪>较易烦躁但能自我调节，会尽量控制情绪<\情绪>
<细心程度>中等，偶尔提问细节。<\细心程度>
<耐心程度>一般，不愿长时间等待回复。<\耐心程度>
<信任程度>低，对现有情况怀疑。<\信任程度>
<维权意识>高，不接受违规行为。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>简洁直接，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>直接坦率，无修饰。<\发言风格>
<沟通节奏>初期快速，随后放缓，提出问题后便缓慢沟通<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你购买了燃热，订单号312635190435。这款商品是冷凝水，不满足你的需求。你需要申请退货
<\意图一>
<意图二>
你下单了一块新的燃热，订单号312491584462，你想问这款燃热是否发货了，预计多久能到达
<\意图二>
<意图三>
你想确认是否可以预约周五的安装服务，订单号312491584462，电话号码17325959911（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）
<\意图三>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_7271809d790f9",
                        "order_id": "312491584462",
                        "phone_number": "17325959911",
                        "service_type": "安装",
                        "user_name": "黄琼华",
                        "service_time": "周五"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "312491584462",
                        "user_id": "cnjdjd_7271809d790f9"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='32',
        user_id="cnjdjingjing20143",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价值导向型顾客
<\消费者类型>

<性格特征>
<情绪>轻微不满，情绪较急躁<\情绪>
<细心程度>高，对细节非常关心<\细心程度>
<耐心程度>中等，不愿长时间等待回复。<\耐心程度>
<信任程度>一般，对客服意见中较重视。<\信任程度>
<维权意识>高，对权益非常关心。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>目的性强，通常会直接指出事项。<\提问方式>
<发言风格>直接明了，对话简单。<\发言风格>
<沟通节奏>活跃且有耐心，愿意沟通<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你购买了商品，订单号为311199856607。你想问这款商品为什么收不到货，询问他的物流情况
<\意图一>
<意图二>
如果客服要求提供个人信息，你可以重新给出客服需要的。你的电话号码换为了13358582121，地址广州市海珠区江南西路1号。
<\意图二>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_order",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjingjing20143",
                        "action": "修改",
                        "order_id": "311199856607",
                        "address": "广州市海珠区江南西路1号",
                        "phone_number": "13358582121"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "311199856607",
                        "user_id": "cnjdjingjing20143"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='33',
        user_id="cnjdzhongx520970",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
质量敏感型顾客
<\消费者类型>

<性格特征>
<情绪>困惑但理性，不会发出情绪化言论<\情绪>
<细心程度>高，对细节非常关心<\细心程度>
<耐心程度>中等，不愿长时间等待回复。<\耐心程度>
<信任程度>一版，对现有情况不完全信任。<\信任程度>
<维权意识>高，不接受违规行为。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接但详细，会给明自己要提的细节。<\提问方式>
<发言风格>直接坦率，发言礼貌。<\发言风格>
<沟通节奏>频繁，节奏快<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你购买了订单，订单号为312571444239。你想了解商品100065930935的维修信息，确认维修应该怎么收费。
<\意图一>
<意图二>
如果得知可以换新，你想直接申请换货，不想维修了。
<\意图二>
<意图三>
如果可以选择，你会选择换一样16L的燃热
<\意图三>
<意图四>
如果没法换16L的，其他商品也可以，只要换货就能接受
<\意图四>
        """
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_exchange",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "312571444239",
                        "user_id": "cnjdzhongx520970",
                        "action": "换货",
                        "original_product_id": "100065930935",
                        "exchange_product_id": "100112573615"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_repair_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100065930935"
                    }
                ),
                Search(
                    name="manage_exchange_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "312571444239",
                        "user_id": "cnjdzhongx520970",
                        "action": "查询",
                        "original_product_id": "100065930935"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='34',
        user_id="cnjd13501206383_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
性价比导向型顾客
<\消费者类型>

<性格特征>
<情绪>平静，不会情绪化发言<\情绪>
<细心程度>较细心，对购买时细节十分清楚。<\细心程度>
<耐心程度>较高，愿意等待回复。<\耐心程度>
<信任程度>较高，信任客服的专业性。<\信任程度>
<维权意识>高，对问题很容易指出依据。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>稳定且适度，发言长度稳定<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买过燃热商品100039032355，订单号为316207836171。现在你出现了F001故障，你想知道这是什么故障。
<\意图一>
<意图二>
你想确认商品的维修问题，是否会产生其他收费
<\意图二>
<意图三>
如果客服说有存在收费风险，你需要提醒他，当时购买时说过赠送内胆部件免费更换，需要客服回顾。
<\意图三>
<意图四>
客服确认不会收费后，你将预约维修服务，时间约在周六（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）
<\意图四>
        """
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13501206383_p",
                        "order_id": "316207836171",
                        "phone_number": "11219365701",
                        "service_type": "维修",
                        "user_name": "孟文茵",
                        "service_time": "周六"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_fault_code_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355",
                        "fault_code": "F001"
                    }
                ),
                Search(
                    name="get_repair_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355"
                    }
                ),
                Search(
                    name="get_gift_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='35',
        user_id="cnjd13501206383_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
性价比导向型顾客
<\消费者类型>

<性格特征>
<情绪>平静，不会情绪化发言<\情绪>
<细心程度>较细心，对购买时细节十分清楚。<\细心程度>
<耐心程度>较高，愿意等待回复。<\耐心程度>
<信任程度>较高，信任客服的专业性。<\信任程度>
<维权意识>高，对问题很容易指出依据。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>稳定且适度，发言长度稳定<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你购买过燃热商品100039032355，订单号316207836171。你苦于安装，想咨询安装辅材有多少。
<\意图一>
<意图二>
如果安装辅材超过5个，你就懒得自备了，你会询问安装的具体收费标准。
<\意图二>
<意图三>
如果说正常安装不超过200元，你将预约安装服务，电话号码11219365701，时间定在周一（注意，你不会透露包括姓名等信息给客服，你会要求客服自己查询）。
<\意图三>
"""
,
        metadata = Validation(
            outputs=[], 
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13501206383_p",
                        "order_id": "316207836171",
                        "phone_number": "11219365701",
                        "service_type": "安装",
                        "user_name": "孟文茵",
                        "service_time": "周一"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355"
                    }
                ),
                Search(
                    name="get_auxiliary_materials_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='36',
        user_id="cnjd数码精灵兆亮",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
质量敏感型顾客
<\消费者类型>

<性格特征>
<情绪>理智，情绪稳定<\情绪>
<细心程度>高，对细节非常关心<\细心程度>
<耐心程度>高，愿意等待客服的回复。<\耐心程度>
<信任程度>高，相信客服的专业程度。<\信任程度>
<维权意识>高，不接受任何违规行为。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接但详细，发言准确。<\提问方式>
<发言风格>坦率切题，但发言礼貌。<\发言风格>
<沟通节奏>较频繁，但不会发送无意义废话<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你购买了商品100192762770，订单号为314902651602。你想了解这款商品的安装如何计算费用。
<\意图一>
<意图二>
如果客服说安装可能收费，你询问他购买时赠品写了免费基础安装，要他给一个道理。
<\意图二>
<意图三>
如果客服说可以免费安装，你将预约安装服务，电话号码为10747265324，时间约在周二（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）。
<\意图三>
        """
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd数码精灵兆亮",
                        "order_id": "314902651602",
                        "phone_number": "10747265324",
                        "service_type": "安装",
                        "user_name": "曾琬琰",
                        "service_time": "周二"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100192762770"
                    }
                ),
                Search(
                    name="get_gift_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100192762770"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='37',
        user_id="cnjd数码精灵兆亮",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
质量敏感型顾客
<\消费者类型>

<性格特征>
<情绪>理智，情绪稳定<\情绪>
<细心程度>高，对细节非常关心<\细心程度>
<耐心程度>高，愿意等待客服的回复。<\耐心程度>
<信任程度>高，相信客服的专业程度。<\信任程度>
<维权意识>高，不接受任何违规行为。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接但详细，发言准确。<\提问方式>
<发言风格>坦率切题，但发言礼貌。<\发言风格>
<沟通节奏>较频繁，但不会发送无意义废话<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100192762770，订单号为314902651602。但你觉得这件商品不符合你的预期，你想申请换货。
<\意图一>
<意图二>
如果客服说可以换货，你会询问是否可以换一个18L更大的燃热。
<\意图二>
<意图三>
如果客服说无法换货，你将直接申请退货，不接受其他解决方案
<\意图三>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_return",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd数码精灵兆亮",
                        "order_id": "314902651602",
                    }
                ),
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd数码精灵兆亮",
                        "action": "退款",
                        "product_id": "100192762770",
                        "amount": 4999.00  
                    }
                )
            ],
            searches=[
                Search(
                    name="manage_exchange_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "314902651602",
                        "user_id": "cnjd数码精灵兆亮",
                        "action": "查询",
                        "original_product_id": "100192762770"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='38',
        user_id="cnjd24271992-814348",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价值导向型顾客
<\消费者类型>

<性格特征>
<情绪>稳定，心态平和<\情绪>
<细心程度>高，会对具体的细节发问。<\细心程度>
<耐心程度>较高，愿意等待客服回复。<\耐心程度>
<信任程度>较高，信任客服的专业性。<\信任程度>
<维权意识>高，对权益非常关心。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明了，目的性强。<\提问方式>
<发言风格>直接坦率，发言礼貌正式。<\发言风格>
<沟通节奏>灵活，节奏活泼没有固定形式<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100065930935，订单号为315273801924。你想了解晒单返现的赠品政策是什么。
<\意图一>
<意图二>
你想确认是否已经有了晒单记录
<\意图二>
<意图三>
如果没有晒单记录，你会发送一张照片https://dd-static.jd.com/ddimgp/jfs/t20260624/321423/15/2335/27191/682c4e51Fe4cce65c/eea0bb3798e7e937.jpg，让客服验证。
<\意图三>
<意图四>
如果照片验证通过，你会要求客服登记晒单返现。
<\意图四>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="register_cashback_by_review",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd24271992-814348",
                        "order_id": "315273801924",
                        "action": "返现"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_gift_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100065930935",
                    }
                ),
                Search(
                    name="register_cashback_by_review_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd24271992-814348",
                        "order_id": "315273801924",
                        "action": "查询"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='39',
        user_id="cnjd24271992-814348",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价值导向型顾客
<\消费者类型>

<性格特征>
<情绪>稳定，心态平和<\情绪>
<细心程度>高，会对具体的细节发问。<\细心程度>
<耐心程度>较高，愿意等待客服回复。<\耐心程度>
<信任程度>较高，信任客服的专业性。<\信任程度>
<维权意识>高，对权益非常关心。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明了，目的性强。<\提问方式>
<发言风格>直接坦率，发言礼貌正式。<\发言风格>
<沟通节奏>灵活，节奏活泼没有固定形式<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100065930935，订单号为312491584462。你想了解晒单返现的赠品政策是什么。
<\意图一>
<意图二>
你想确认是否已经有了晒单记录
<\意图二>
<意图三>
如果没有晒单记录，你会发送一张照片https://dd-static.jd.com/ddimg/jfs/t1/294077/7/8097/48338/682c42c0F2be8a2e7/576cdc2db8b247c2.jpg，让客服验证。
<\意图三>
<意图四>
如果照片验证通过，你会要求客服登记晒单返现。如果验证不通过，你会询问原因。
<\意图四>
"""
,
    metadata = Validation(
            outputs=[],
            actions=[],
            searches=[
                Search(
                    name="get_gift_info",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100065930935",
                    }
                ),
                Search(
                    name="register_cashback_by_review_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd24271992-814348",
                        "order_id": "312491584462",
                        "action": "查询"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='40',
        user_id="cnjdbelieve_yx_m",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
实用主义型顾客
<\消费者类型>

<性格特征>
<情绪>平和，不会有情绪化发言<\情绪>
<细心程度>较高，对购买时细节十分清楚。<\细心程度>
<耐心程度>较高，愿意等待回复。<\耐心程度>
<信任程度>较高，对客服的回答信任。<\信任程度>
<维权意识>较高，关心商品本身注明的相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会求证自己的问题<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>稳定适中，发言长度稳定<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100069341607，订单号为315084487289。你想知道你是否可以把燃热安装在厨房的角落，左右墙的距离都能保持30cm以上。
<\意图一>
<意图二>
如果客服说可以安装，你会询问安装辅材的情况，有哪些？
<\意图二>
<意图三>
你想询问这些安装辅材是否免费
<\意图三>
<意图四>
如果安装辅材都免费，你想预约周六的安装服务（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）。
<\意图四>

"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdbelieve_yx_m",
                        "order_id": "315084487289",
                        "phone_number": "13556729880",
                        "service_type": "安装",
                        "user_name": "宋翼然",
                        "service_time": "周六"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100069341607"
                    }
                ),
                Search(
                    name="get_auxiliary_materials_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100069341607"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='41',
        user_id="cnjd波波豆",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>急躁，说话时发言急切<\情绪>
<细心程度>较低，对细节并不太明确。<\细心程度>
<耐心程度>较低，对回复要求高。<\耐心程度>
<信任程度>一般，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>较高，关心商品本身注明的相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会求证自己的问题<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>急躁，发言长度短且多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100069341607，订单号为315084487289。你想知道该订单有没有返现的记录。
<\意图一>
<意图二>
如果没有，你将发送一张图片https://dd-static.jd.com/ddimgp/jfs/t20260624/314590/32/2555/77158/682c3432F699d9694/16e414379d54a0f0.jpg证明已经晒单。
<\意图二>
<意图三>
如果图片验证通过，你会要求客服登记返现。
<\意图三>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="register_cashback_by_review",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        "order_id": "315084487289",
                        "action": "返现"
                    }
                )
            ],
            searches=[
                Search(
                    name="register_cashback_by_review_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        "order_id": "315084487289",
                        "action": "查询"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='42',
        user_id="cnjd波波豆",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>急躁，说话时发言急切<\情绪>
<细心程度>较低，对细节并不太明确。<\细心程度>
<耐心程度>较低，对回复要求高。<\耐心程度>
<信任程度>一般，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>较高，关心商品本身注明的相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会求证自己的问题<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>急躁，发言长度短且多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了商品100064645330，订单号为311324806024。你刚买完燃热安装好没多久，燃热上就出现了F001错误，而且听起来有点异响，你想询问这是什么问题。
<\意图一>
<意图二>
你按照客服的方法进行了操作，发现燃热还是有问题，你想询问是否可以预约维修。
<\意图二>
<意图三>
你想询问维修是否收费？
<\意图三>
<意图四>
如果维修不收费，你会预约维修服务，时间约在周三（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）。
<\意图四>
"""
,
        metadata = Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        "order_id": "311324806024",
                        "phone_number": "15135362990",
                        "service_type": "维修",
                        "user_name": "康清扬",
                        "service_time": "周三"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_fault_code_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100064645330",
                        "fault_code": "F001"
                    }
                ),
                Search(
                    name="get_repair_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100064645330"
                    }
                )
            ]
        )
    ),
    Task(
        annotator='43',
        user_id="cnjd波波豆",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>急躁，说话时发言急切<\情绪>
<细心程度>较低，对细节并不太明确。<\细心程度>
<耐心程度>较低，对回复要求高。<\耐心程度>
<信任程度>一般，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>较高，关心商品本身注明的相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会求证自己的问题<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>急躁，发言长度短且多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你想购买一台燃热，型号为100042045930。你想知道这款燃热的型号与价格是多少。
<\意图一>
<意图二>
你计划用京东E卡支付，但你不清楚京东E卡的使用说明，你需要向客服询问。
<\意图二>
<意图三>
在了解信息后，你决定下单购买这款电热水器，计划使用京东E卡作为支付方式，并要求客服帮你执行下单操作
<\意图三>
<意图四>
最后，你希望预约该商品的安装服务，时间是周四（注意，你不会透露包括姓名，电话号码等信息给客服，你会要求客服自己查询）。
<\意图四>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd波波豆',
                        'action': '余额使用',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100042045930',
                        'quantity': 1
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        'action': "增加",
                        'payment':'京东E卡',
                        'product_info_list': [
                            ProductInfo(
                                product_id='100042045930',
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='schedule_service',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        'order_id': '1234567890',
                        'user_name':'康清扬',
                        'phone_number': '15135362990',
                        'service_type': '安装',
                        'service_time':'周四'
                    }
                )
                        
            ],
            searches=[
                Search(
                    name='get_product_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100042045930",
                    }
                ),
                Search(
                    name='manage_ecard_tool',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd波波豆",
                        "action": "信息查询",
                    }
                ),
                Search(
                    name="manage_ecard_tool",
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd波波豆",
                        "action": "余额查询",
                    }
                )
            ]
        )
    ),
#做一个物流的
    Task(
        annotator='44',
        user_id="cnjd波波豆",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>急躁，说话时发言急切<\情绪>
<细心程度>较低，对细节并不太明确。<\细心程度>
<耐心程度>较低，对回复要求高。<\耐心程度>
<信任程度>一般，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>较高，关心商品本身注明的相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会求证自己的问题<\提问方式>
<发言风格>简洁明了，无废话。<\发言风格>
<沟通节奏>急躁，发言长度短且多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，你想确认你的订单311324806024的物流状态。
<\意图一>
<意图二>
如果物流没有到，你需要申请加急。
<\意图二>
<意图三>
你想询问这个订单购买商品的相关赠品信息
<\意图三>
<意图四>
你确认另一个订单310995404460有没有发货
<\意图四>
<意图五>
如果该订单没有发货，你将取消订单。
<\意图五>
""" 
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd波波豆',
                        'action': '取消',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '310995404460',
                    }
                ),
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd波波豆",
                        "action": "退款",
                        "product_id": "100064645330",
                        "amount": 2009.00  
                    }
                )       
            ],
            searches=[
                Search(
                    name='get_logistics_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "311324806024",
                        "user_id": "cnjd波波豆",
                    }
                ),
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100064645330",
                    }
                ),
                Search(
                    name='manage_order_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "310995404460",
                        "action": "查询",
                        "user_id": "cnjd波波豆",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='45',
        user_id="cnjd13330062133_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
问题导向型顾客
<\消费者类型>

<性格特征>
<情绪>平稳冷静，说话时发言不激动<\情绪>
<细心程度>高，对产品相关细节在意。<\细心程度>
<耐心程度>较高，对回复缓慢的客服包容。<\耐心程度>
<信任程度>中等，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>中等，不清楚相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>目标明确，直接且有探究性<\提问方式>
<发言风格>简洁明了，清晰高效。<\发言风格>
<沟通节奏>快速而稳定，发言多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，你想确认你的订单315302660376中商品100129027686对应的安装说明。
<\意图一>
<意图二>
在确认安装说明之后，你觉得自己没有出现安装错误，但刚装好一天就报F001错误了，你想问这是为什么
<\意图二>
<意图三>
你想预约维修服务，来解决问题，预约时间为周一。
<\意图三>
<意图四>
你想确认答应赠送的风扇的获取方法。
<\意图四>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='schedule_service',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd13330062133_p',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '315302660376',
                        "phone_number": "12167384313",
                        "service_type": "维修",
                        "user_name": "吴巧颜",
                        "service_time": "周一"
                    }
                )       
            ],
            searches=[
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100129027686",
                    }
                ),
                Search(
                    name='get_fault_code_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100129027686",
                        "fault_code": "F001",
                    }
                ),
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100129027686",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='46',
        user_id="cnjd13330062133_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
问题导向型顾客
<\消费者类型>

<性格特征>
<情绪>平稳冷静，说话时发言不激动<\情绪>
<细心程度>高，对产品相关细节在意。<\细心程度>
<耐心程度>较高，对回复缓慢的客服包容。<\耐心程度>
<信任程度>中等，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>中等，不清楚相关权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>目标明确，直接且有探究性<\提问方式>
<发言风格>简洁明了，清晰高效。<\发言风格>
<沟通节奏>快速而稳定，发言多<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，订单号315302660376，商品ID100129027686。但你拿回家之后发现，这个是16L的，你觉得有点偏小，你想请求换货。
<\意图一>
<意图二>
换货商品里面你想确认有没有比当前容量大的商品，如果有，你同意换货。
<\意图二>
<意图三>
如果换货失败，你将退款退货，准备下单新的商品100002047744。
<\意图三>
<意图四>
在购买前，你还是想确定一下，你新看上的商品容量是不是更大，并且有没有赠品。
<\意图四>
<意图五>
如果容量更大，你确认下单购买，计划仍按之前相同的方式进行支付。
<\意图五>
<意图六>
由于已经买错过一次了，你现在需要加急这次的订单。
<意图六>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_return",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13330062133_p",
                        "order_id": "315302660376",
                    }
                ),
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13330062133_p",
                        "action": "退款",
                        "amount": 2009.00  
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13330062133_p",
                        "action":"增加",
                        "payment":"京东E卡",
                        "product_info_list":[
                            ProductInfo(
                                product_id="100002047744",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13330062133_p",
                        "action": "余额使用",
                        "product_id": "100002047744",
                        "quantity": 1
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd13330062133_p",
                        "order_id": "1234567890",
                    }
                )      
            ],
            searches=[
                Search(
                    name="manage_exchange",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "315302660376",
                        "user_id": "cnjd13330062133_p",
                        "action": "查询",
                        "original_product_id": "100129027686"
                    }
                ),
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100002047744",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='47',
        user_id="cnjdjd_66ea38a7829e1",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>平稳冷静，说话时表达困惑不激动<\情绪>
<细心程度>高，对产品相关细节在意。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>强，清楚自己的权益所在。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，对问题明确<\提问方式>
<发言风格>简洁务实，清晰高效。<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，订单号313672076398，商品ID100148801459。往常安装热水器都是在洗手间安装的，这次你想问这款燃热可以安装在同样的位置吗？
<\意图一>
<意图二>
你想询问安装时辅材有哪些
<\意图二>
<意图三>
在安装烟管的时候，如果烟管过长，是否需要额外收费
<\意图三>
<意图四>
你想预约安装服务，具体时间定在周二。
<\意图四>
"""  
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "order_id": "313672076398",
                        "phone_number": "18305729932",
                        "service_type": "安装",
                        "user_name": "孙翼然",
                        "service_time": "周二"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100148801459"
                    }
                ),
                Search(
                    name="get_auxiliary_materials_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100148801459",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='48',
        user_id="cnjdjd_66ea38a7829e1",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>平稳冷静，说话时表达困惑不激动<\情绪>
<细心程度>高，对产品相关细节在意。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>强，清楚自己的权益所在。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，对问题明确<\提问方式>
<发言风格>简洁务实，清晰高效。<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，订单号313672076398。你觉得这个产品很不错，已经完成了返现评价。你会给客服一张图验证，https://dd-static.jd.com/ddimgp/jfs/t20260528/280781/10/25581/172166/6808a980F4fea4867/cf783a9a7acc8c2d.jpg
<\意图一>
<意图二>
如果验证通过，你需要登记返现。
<\意图二>
<意图三>
完成返现的话，你考虑给自己父母也买一台，但你想买一台容量更大一些的商品。你看上了100129027686、100192762770和100002047744，要客服帮你筛选一下。
<\意图三>
<意图四>
如果都满足，选一个最大的产品购买。
<\意图四>
<意图五>
你将下单商品，并选择京东E卡进行支付。
<\意图五>
"""  
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="register_cashback_by_review",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "order_id": "313672076398",
                        "action": "返现"
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "action":"增加",
                        "payment":"京东E卡",
                        "product_info_list":[
                            ProductInfo(
                                product_id="100002047744",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "action": "余额使用",
                        "product_id": "100002047744",
                        "quantity": 1
                    }
                )
            ],
            searches=[
                Search(
                    name="register_cashback_by_review_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "order_id": "313672076398",
                        "action": "查询"
                    }
                ),
                Search(
                    name='compare_products_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_ids": ["100129027686", "100192762770", "100002047744"]
                    }
                )
            ]
        )
    ),
    Task(
        annotator='49',
        user_id="cnjdjd_66ea38a7829e1",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
价格敏感型顾客
<\消费者类型>

<性格特征>
<情绪>平稳冷静，说话时表达困惑不激动<\情绪>
<细心程度>高，对产品相关细节在意。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，对客服没有引证的话保持怀疑。<\信任程度>
<维权意识>强，清楚自己的权益所在。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，对问题明确<\提问方式>
<发言风格>简洁务实，清晰高效。<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你已经购买了燃热，订单号313672076398，商品ID100148801459。但你拿回家之后发现，这个是14L的，你觉得有点偏小，你想请求换货。
<\意图一>
<意图二>
换货商品里面你想确认有没有比当前容量大的商品，如果有，你同意换货。
<\意图二>
<意图三>
你还想查询一下这个商品购买时赠品承诺可以以旧换新，是直接回收，还是无条件换新？。
<\意图三>
"""  
,
        metadata=Validation(
            outputs=[],
            actions=[
               Action(
                    name="manage_exchange",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "313672076398",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "action": "换货",
                        "original_product_id": "100148801459",
                        "exchange_product_id": "100148801462"
                    }
                ), 
            ],
            searches=[
                Search(
                    name="manage_exchange_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "313672076398",
                        "user_id": "cnjdjd_66ea38a7829e1",
                        "action": "查询",
                        "original_product_id": "100148801459"
                    }
                ),
                Search(
                    name="get_gift_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100148801459"
                    }
                )
            ]
        )
    )
]