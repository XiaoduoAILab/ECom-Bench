from utils import Task, Action, Search, Validation

All_Tasks = [
    Task(
        annotator="售后阶段",
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
你购买了商品https://item.jd.com/100140212122.html?sdx=ehi-lLxFuJiE6JnIYIdcjscisTKTRHsgmjYZ4ukJEdyMdZjWL59V5HnirE8，订单号307252585701。现在你对安装很头疼。你想询问安装辅材里有没有水管
<\意图一>
<意图二>
辅材的水管是自备还是安装师傅会携带
<\意图二>
<意图三>
你想询问安装是否收费，水管需要收费吗，水管改造呢？
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
                        "order_id": "313021098954",
                        "phone_number": "14529231388",
                        "service_type": "安装",
                        "user_name": "常静好",
                        "service_time": "周五"
                    }
                ),
            ],
            searches=[
                Search(
                    name="get_product_info",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100140212122",
                    }
                ),
                Search(
                    name="get_installation_service_info",
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
        annotator="售后阶段",
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
你下单了一块新的燃热，你想问这款燃热是否发货了，预计多久能到达
<\意图二>
<意图三>
你想确认是否可以预约周五的安装服务，订单号312491584462，电话号码17325959911
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
                    name="get_logistics_info",
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
        annotator="售后阶段",
        user_id="cnjdjd_7271809d790f9",
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
                        "user_id": "cnjdjd_7271809d790f9",
                        "action": "修改",
                        "order_id": "311199856607",
                        "phone_number": "13358582121"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_logistics_info",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "311199856607",
                        "user_id": "cnjdjd_7271809d790f9"
                    }
                )
            ]
        )
    ),
    Task(
        annotator="售后阶段",
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
你购买了订单，订单号为312491584462。你想了解商品100065930935的维修信息，确认维修应该怎么收费。
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
                        "order_id": "312491584462",
                        "user_id": "cnjdzhongx520970",
                        "action": "换货",
                        "original_product_id": "100065930935",
                        "exchange_product_id": "100112573615"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_repair_info",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100065930935"
                    }
                ),
                Search(
                    name="manage_exchange",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "312491584462",
                        "user_id": "cnjdzhongx520970",
                        "action": "查询",
                        "original_product_id": "100065930935"
                    }
                )
            ]
        )
    )
]