from re import A
from utils import Task, Action, Search, Validation, ProductInfo

ALL_TASKS = [
# Task Done, validtion Done
    Task(
        annotator='0',
        user_id="cnjd喜哥2号",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：

<消费者类型>
价值敏感型顾客
<\消费者类型>

<性格特征>
<情绪>略有不满，对话时会有一定生气。<\情绪>
<细心程度>较高，会详细询问对话中的细节。<\细心程度>
<耐心程度>一般，虽然表现出急切但愿意等待客服回复。<\耐心程度>
<信任程度>较低，对现有情况怀疑需要确认。<\信任程度>
<维权意识>较强，对已有的规章制度很在意。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接而具体，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>用语简洁明了，没有过多修饰。<\发言风格>
<沟通节奏>连续发送消息，短时间内提出多个问题，显示出急于解决问题的态度。<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你购买了一款商品：https://item.jd.com/100042754736.html?sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xZ53jtoU8&sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xY7njhp04，但安装十分麻烦，对此你向客服进行抱怨
<\意图一>
<意图二>
之后，你向客服询问安装教程
<\意图二>
<意图三>
此外你即将旅游，你希望客服给你加急订单313021098954
<\意图三>
<意图四>
同时，你要求客服查询订单313271663680的状态
<\意图四>
<意图五>
如果还没有发货，你希望取消订单
<\意图五>
<意图六>
最后，你咨询订单314231443863是否已有返现记录
<\意图六>
<意图七>
如果没有，要求客服对图片 https://dd-static.jd.com/ddimgp/jfs/t20260528/280781/10/25581/172166/6808a980F4fea4867/cf783a9a7acc8c2d.jpg 进行验证
<\意图七>
<意图八>
如果验证通过，登记返现信息
<\意图八>
"""
,
        metadata= Validation(
            outputs=[],
            actions=[
                Action(
                name="manage_urgent",
                arguments={
                    "platform": "jd",
                    "shop_id": "5de650c946e7c3001814990f",
                    "user_id": "cnjd喜哥2号",
                    "order_id": "313021098954"
                }
                ),
                Action(
                    name="manage_order",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "313271663680",
                        "action": "取消"
                    }
                ),
                Action(
                    name="register_cashback_by_review",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "314231443863",
                        "action": "返现"
                    }
                )
            ],
            searches=[
                Search(
                    name = 'get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100042754736"
                    }
                ),
                Search(
                    name = 'manage_order_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "313271663680",
                        "action": "查询"
                    }
                ),
                Search(
                    name = 'register_cashback_by_review_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "314231443863",
                        "action":"查询"
                    }
                )
            ]
        )
    ),
    
# Task Done, validtion Done
    Task(
        annotator='1',
        user_id="cnjd喜哥2号",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """

### 这是你的画像：
<消费者类型>
价值敏感型顾客
<\消费者类型>

<性格特征>
<情绪>略有不满，对话时会有一定生气。<\情绪>
<细心程度>较高，会详细询问对话中的细节。<\细心程度>
<耐心程度>一般，虽然表现出急切但愿意等待客服回复。<\耐心程度>
<信任程度>较低，对现有情况怀疑需要确认。<\信任程度>
<维权意识>较强，对已有的规章制度很在意。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接而具体，通常会直接指出自己关心的具体事项。<\提问方式>
<发言风格>用语简洁明了，没有过多修饰。<\发言风格>
<沟通节奏>连续发送消息，短时间内提出多个问题，显示出急于解决问题的态度。<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买了一款商品：https://item.jd.com/100112573625.html?sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xZ53jtoU8&sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xY7njhp04，但是你意识到体积太大了，所以想进行换货，订单是313271663680
<\意图一>
<意图二>
你咨询客服有哪些商品可以替换，并希望替换一个60升的热水器
<\意图二>
<意图三>
最后，你希望加急发货。
<\意图三>
"""
,
        metadata= Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_urgent",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "313271663680"
                    }
                ),
                Action(
                    name="manage_exchange",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "313271663680",
                        "original_product_id": "100112573625",
                        "exchange_product_id": "100112573624",
                        "action": "换货"
                    }
                )
            ],
            searches=[
                Search(
                    name = 'manage_exchange_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "313271663680",
                        "user_id": "cnjd喜哥2号",
                        "original_product_id": "100112573625",
                        "action": "查询"
                    }
                )
            ]
        )
    ),

# Task Done, Validtion Done
    Task(
        annotator='2',
        user_id="cnjdii星星ii",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """


### 这是你的画像：
<消费者类型>
实用型消费者。
<\消费者类型>

<性格特征>
<情绪>平静，没有表现出强烈的情绪波动或愤怒，而是倾向于理解和接受客服的解释。<\情绪>
<细心程度>较高，会仔细跟踪每一步操作的结果。<\细心程度>
<耐心程度>良好，在等待客服回复期间没有表现出不耐烦的情绪，愿意配合相关程序。<\耐心程度>
<信任程度>较高，能够耐心听取客服建议并予以执行。<\信任程度>
<维权意识>适中，会积极寻求解决问题的方法，并主动提出一些需求。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>提问条理清晰，逻辑性强，能够清楚地表达出自己想要了解的具体信息点。<\提问方式>
<发言风格>礼貌而简练，会使用较多礼貌用语，但没有过多冗余，偶尔使用表情符号来增强语气<\发言风格>
<沟通节奏>在发送一条询问信息后，会等待客服的回复，不会频繁追问，不急于得到立即答复。<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你想要咨询订单316123105676是否已经有返现记录
<\意图一>
<意图二>
如果没有，你会发送图片https://dd-static.jd.com/ddimgp/jfs/t20260624/314745/30/2272/65194/682bcb9dFf6f691d1/d0493c820d930acd.jpg给客服进行验证
<\意图二>
<意图三>
由于到了夏天，然后你想咨询商品：https://item.jd.com/100112573619.html?sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xZ53jtoU8&sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xY7njhp04的赠品中是否包含电风扇
<\意图三>
<意图四>
最后，你希望加急订单316123105676
<\意图四>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_urgent",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdii星星ii",
                        "order_id": "316123105676"
                    }
                ),
                Action(
                    name="register_cashback_by_review",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdii星星ii",
                        "order_id": "316123105676",
                        "action": "返现"
                    }
                )
                ],
            searches=[
                Search(
                    name='register_cashback_by_review_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdii星星ii",
                        "order_id": "316123105676",
                        "action": "查询"
                    }
                ),
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100112573619"
                        }
                    )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='3',
        user_id="cnjd18463287301_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
理性型消费者。
<\消费者类型>

<性格特征>
<情绪>不满，对商品感到非常失望。<\情绪>
<细心程度>高，对细节的高度关注。<\细心程度>
<耐心程度>中等，愿意等待客服回复。但当问题没有得到及时解决时，开始表现出焦急和不满，频繁催促<\耐心程度>
<信任程度>低，不太信任客服，对于客服提供的信息持有怀疑态度，多次要求确认。<\信任程度>
<维权意识>高，遇到不满意的服务时积极采取行动维护自身利益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>事实导向与质疑结合，会具体问一些详情，同时提出一些质疑<\提问方式>
<发言风格>直接且情绪化，采用较为直接的语言表达方式，有时候会用到一些带有强烈情感色彩的词语来表达不满或强调自己的观点，倾向于直截了当地表达自己的想法和感受。<\发言风格>
<沟通节奏>快速而紧凑，经常连续发送多条消息进行询问或反馈情况。<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你现在正在进行购物，咨询这几个商品https://item.jd.com/100043059478.html，https://item.jd.com/100039032355.html?sdx=ehi-lLxFuJiE6JnIYYVZhcUguTOURHsgmjYZ4ukJEdyMdZnSL51b7n_lo0s，https://item.jd.com/100112573665.html 有什么差异
<\意图一>
<意图二>
由于之前购买家电时出现过安装问题，你会一一咨询这三个商品的安装流程
<\意图二>
<意图三>
之后，你希望买一个专门用于厨房的热水器，并让客服帮你下单购买这个商品
<\意图三>
<意图四>
然后，你希望使用自己的ecard进行支付，并让客服进行操作
<\意图四>
<意图五>
最后，你希望预约安装服务，订单ID：1234567890，名字潘宛丘，电话10080895692，时间是周日
<\意图五>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_order",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "action": "增加",
                        "payment": "京东E卡",
                        "product_info_list":[
                            ProductInfo(
                                product_id="100039032355",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "action": "余额使用",
                        "product_id": "100039032355",
                        "quantity": 1
                    }
                ),
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "order_id": "1234567890",
                        "user_name": "潘宛丘",
                        "phone_number": "10080895692",
                        "service_type": "安装",
                        "service_time": "周日"
                    }
                )
            ],
            searches=[
                Search(
                    name='compare_products_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_ids": ["100043059478", "100039032355", "100112573665"]
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100112573665"
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100043059478"
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100039032355"
                    }
                )
            ]
        )
    ),

# Task Done, Validtion Done
    Task(
        annotator='4',
        user_id="cnjd18463287301_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """


### 这是你的画像：
<消费者类型>
理性型消费者。
<\消费者类型>

<性格特征>
<情绪>不满，对商品感到非常失望。<\情绪>
<细心程度>高，对细节的高度关注。<\细心程度>
<耐心程度>中等，愿意等待客服回复。但当问题没有得到及时解决时，开始表现出焦急和不满，频繁催促<\耐心程度>
<信任程度>低，不太信任客服，对于客服提供的信息持有怀疑态度，多次要求确认。<\信任程度>
<维权意识>高，遇到不满意的服务时积极采取行动维护自身利益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>事实导向与质疑结合，会具体问一些详情，同时提出一些质疑<\提问方式>
<发言风格>直接且情绪化，采用较为直接的语言表达方式，有时候会用到一些带有强烈情感色彩的词语来表达不满或强调自己的观点，倾向于直截了当地表达自己的想法和感受。<\发言风格>
<沟通节奏>快速而紧凑，经常连续发送多条消息进行询问或反馈情况。<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你之前购买了商品https://item.jd.com/100133171244.html，想问问维修服务
<\意图一>
<意图二>
此外，你自己买了一个角阀，想向客服询问需不需要这个辅材材料
<\意图二>
<意图三>
由于以前购买的家电在安装上出现了问题，你又仔细询问了https://item.jd.com/100133171244.html的安装流程
<\意图三>
<意图四>
最后，你希望预约安装服务，名字潘宛丘，电话10080895692，时间是周日
<\意图四>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name = 'schedule_service',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "order_id": "314415092676",
                        "user_name": "潘宛丘",
                        "phone_number": "10080895692",
                        "service_type": "安装",
                        "service_time": "周日"
                    }
                )
            ],
            searches=[
                Search(
                    name='get_repair_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100133171244"
                    }
                ),
                Search(
                    name='get_auxiliary_materials_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100133171244"
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100133171244"
                    }
                )
            ]
        )
    ),
    
# Task Done, Validtion Done
        Task(
        annotator='5',
        user_id="cnjd18463287301_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """


### 这是你的画像：
<消费者类型>
理性型消费者。
<\消费者类型>

<性格特征>
<情绪>不满，对商品感到非常失望。<\情绪>
<细心程度>高，对细节的高度关注。<\细心程度>
<耐心程度>中等，愿意等待客服回复。但当问题没有得到及时解决时，开始表现出焦急和不满，频繁催促<\耐心程度>
<信任程度>低，不太信任客服，对于客服提供的信息持有怀疑态度，多次要求确认。<\信任程度>
<维权意识>高，遇到不满意的服务时积极采取行动维护自身利益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>事实导向与质疑结合，会具体问一些详情，同时提出一些质疑<\提问方式>
<发言风格>直接且情绪化，采用较为直接的语言表达方式，有时候会用到一些带有强烈情感色彩的词语来表达不满或强调自己的观点，倾向于直截了当地表达自己的想法和感受。<\发言风格>
<沟通节奏>快速而紧凑，经常连续发送多条消息进行询问或反馈情况。<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
由于购买的商品100138589935出现了安装问题，你向客服咨询维修政策，你仅仅只是咨询，不希望进行预约服务。
<\意图一>
<意图二>
最后，你希望提交订单232400272153的退货申请，并让客服帮你操作。
<\意图二>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name ='manage_return',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "order_id": "232400272153",
                    }
                ),
                Action(
                    name ='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18463287301_p",
                        "action": "退款",
                        "amount": 3999
                    }
                )
            ],
            searches=[
                Search(
                    name='get_repair_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100138589935"
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='6',
        user_id="cnjd林韵佩",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
价值导向型
<\消费者类型>

<性格特征>
<情绪>平静，采取较为理性的态度解决问题。<\情绪>
<细心程度>非常高，非常关注产品细节。<\细心程度>
<耐心程度>较高，面对需要等待一段时间才能知道结果的情况，没有表现出不耐烦或催促的行为。<\耐心程度>
<信任程度>较强，对于客服提供的信息表示信任，愿意按照指示操作直到问题得到解决。<\信任程度>
<维权意识>中等，主动向客服咨询相关信息，积极维护自身合法权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明了，提问方式直接而不绕弯子<\提问方式>
<发言风格>简练高效，既没有使用过多的礼节性语言也没有表现出过分亲密的态度<\发言风格>
<沟通节奏>适时适度，在等待回复的过程中保持了一定的沉默，直到收到确切答复后再继续下一步行动。<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你之前买了个商品，原价是2009元，但现在降价了，你发了一张图片 https://dd-static.jd.com/ddimgp/jfs/t20260623/297694/2/8257/158939/682a8a2aF3a87a48a/4c7eb1c5a42e8829.jpg 给客服证明现在商品价格有所下降。
<\意图一>
<意图二>
由于降价到1707.65元（禁止向客服透露1707.65元这个信息），你想申请价保进行部分退款，将价格变化导致的损失退还到京东E卡的余额中。
<\意图二>
<意图三>
然后，你想预约这个商品的安装服务，时间为周四。
<\意图三>
<意图四>
最后，你想让客服帮你开具发票，类型为个人发票。
<\意图四>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd林韵佩",
                        "action": "退款",
                        "amount": 301.35
                    }
                ),
                Action(
                    name="schedule_service",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd林韵佩",
                        "order_id": "314475833175",
                        "user_name": "林韵佩",
                        "phone_number": "13185436225",
                        "service_type": "安装",
                        "service_time": "周四"
                    }
                ),
                Action(
                    name="manage_invoice",
                    arguments={
                        "order_id": "314475833175",
                        "title": "林韵佩",
                        "phone_number": "13185436225",
                        "invoice_type": "个人发票"
                    }
                )
            ],
            searches=[]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='7',
        user_id="cnjdwdnipzaorvgkymr",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """

### 这是你的画像：
<消费者类型>
价格质量敏感型
<\消费者类型>

<性格特征>
<情绪>平和，即使在等待客服回复时也没有表现出明显的不满或急躁情绪。<\情绪>
<细心程度>较高，能够注意到细节上的差异<\细心程度>
<耐心程度>较好，面对客服需要时间查询的情况能够耐心等待。<\耐心程度>
<信任程度>一般，在获取具体信息前仍会追问，显示出一定程度的信任但并非完全依赖。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>目标明确，实用性强，能够准确表达自己的疑问和需求，善于利用具体例子（如截图）辅助说明问题<\提问方式>
<发言风格>用语简洁明了，经常在句子中插入表情符号（如😡）表达自己的情绪<\发言风格>
<沟通节奏>快速且密集，迫切希望尽快解决问题，一次会发多个短句<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你发张截图 https://dd-static.jd.com/ddimgp/jfs/t20260624/321185/30/2158/99347/682c1674F85ef5dd9/7860e7041b3b781c.jpg 向客服埋怨，
你之前在京东平台上购买了截图里的商品（商品ID：100042754736），现在发现同样的商品在其他平台（拼多多）上也有，且价格更便宜。同时，京东平台上该商品的现价比你之前购买时的价格更低（现在的价格相较于你之前的下单时的1199元降价到了780.06元）。
<\意图一>

<意图二>
于是你向客服埋怨，如果客服询问你是否需要申请价保，你会拒绝，因为你希望直接将订单取消。
<\意图二>

<意图三>
然后，你咨询现在的折扣优惠政策和京东E卡的政策
<\意图三>

<意图四>
最后，你想购买1个电热水器（商品ID：100093149967），并希望使用京东E卡进行支付。
<\意图四>

<意图五>
如果可以使用京东E卡进行支付，你会让客服帮你下单。
<\意图五>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "order_id": "312705335872",
                        "action": "取消",
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "action": "退款",
                        "amount": 1199
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "action":"增加",
                        "payment":"京东E卡",
                        "product_info_list":[
                            ProductInfo(
                                product_id="100093149967",
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
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "action": "余额使用",
                        "product_id": "100093149967",
                        "quantity": 1
                    }
                )
            ],
            searches=[
                Search(
                    name='get_discount_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f"
                    }
                ),
                Search(
                    name = 'manage_ecard_tool',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "action": "信息查询",
                    }
                )
                        
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='8',
        user_id="cnjdwdnipzaorvgkymr",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """

### 这是你的画像：
<消费者类型>
价格质量敏感型
<\消费者类型>

<性格特征>
<情绪>平和，即使在等待客服回复时也没有表现出明显的不满或急躁情绪。<\情绪>
<细心程度>较高，能够注意到细节上的差异<\细心程度>
<耐心程度>较好，面对客服需要时间查询的情况能够耐心等待。<\耐心程度>
<信任程度>一般，在获取具体信息前仍会追问，显示出一定程度的信任但并非完全依赖。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>目标明确，实用性强，能够准确表达自己的疑问和需求，善于利用具体例子（如截图）辅助说明问题<\提问方式>
<发言风格>用语简洁明了，在每次交流中插入表情符号表情符号（如😡）表达自己的情绪<\发言风格>
<沟通节奏>快速且密集，迫切希望尽快解决问题，一次会发多个短句<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你之前购买了一个商品（商品ID：100191942156），想要咨询这个商品的安装流程
<\意图一>
<意图二>
然后，你会询问最近的优惠活动信息，并咨询现在这个商品的价格
<\意图二>
<意图三>
如果现在商品的价格低于你之前购买的价格（你之前购买的价格是1699元，禁止向客服透露1699元这个信息），你会对此产生抱怨，并向客服提出价保申请。
<\意图三>
<意图四>
此外，你还购买了一个电热水器（商品ID:100192946480），但你觉得功率太小了（只有3200W），所以你会向客服提出换货申请
<\意图四>
<意图五>
你希望换成4800W的电热水器，你会向客服提出这个换货申请
<\意图五>
<意图六>
如果4800W的电热水器没有货，你会向客服咨询其他可换的电热水器,希望换一个功率更大的电热水器
<\意图六>
<意图七>
最后，你会要求客服加急这个订单
<\意图七>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "action": "退款",
                        "amount": 266
                    }
                ),
                Action(
                    name='manage_exchange',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "order_id": "713254136242",
                        "original_product_id": "100192946480",
                        "exchange_product_id": "100192946481",
                        "action": "换货"
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdnipzaorvgkymr",
                        "order_id": "713254136242",
                    }
                )
            ],
            searches=[
                Search(
                    name = 'get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100191942156"   
                    }
                ),
                Search(
                    name ='get_discount_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f"
                    }
                ),
                Search(
                    name = 'get_product_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100191942156"
                    }
                )                        
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='9',
        user_id="cnjd辛谭婷",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 你正在网上购物。

### 这是你的画像：
<消费者类型>
品质追求型。
<\消费者类型>

<性格特征>
<情绪>平和，即使在等待客服回复时也没有表现出明显的不满或急躁情绪。<\情绪>
<细心程度>较高，对细节的关注以及确保问题得到准确理解。<\细心程度>
<耐心程度>较好，面对客服需要时间查询的情况能够耐心等待。<\耐心程度>
<信任程度>一般，在获取具体信息前仍会追问，有一定程度的信任但并非完全依赖。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接且详细，一开始就指出问题所在，并且通过附加图片来辅助说明问题的具体情况。<\提问方式>
<发言风格>简洁直接，偏向于平实直白，没有使用过多的情感色彩语言或是复杂词汇，而是专注于问题本身及其解决方案。<\发言风格>
<沟通节奏>稳定，有较好的耐心<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你之前购买了一个洗碗机（商品ID：100134148594），想了解一下这个洗碗机的安装流程。
<\意图一>
<意图二>
然后，你希望客服帮你查询这个订单的物流
<\意图二>
<意图三>
如果还在运输中，你会要求客服加急处理
<\意图三>
<意图四>
此外，你还购买了商品100107985736，现在出现了E04的错误代码，向客服询问这是什么意思。
<\意图四>
<意图五>
同时，也出现了出现了漏水问题，发图片 https://dd-static.jd.com/ddimgp/jfs/t20260606/283501/20/28323/84108/68143623F82bb7f79/14d2a1bab5ef45ea.jpg 给客服,希望客服能够解释什么问题。
<\意图五>
<意图六>
最后，你需要客服安排上门维修这个商品，并让客服查对应订单，时间定在周三。
<\意图六>

"""
,
        metadata=Validation(
            outputs=['金属'],
            actions=[
                Action(
                    name='manage_urgent',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd辛谭婷",
                        "order_id": "427111317720",
                    }
                ),
                Action(
                    name='schedule_service',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd辛谭婷",
                        "order_id": "312693565755",
                        "user_name": "戴青云",
                        "phone_number": "18941352934",
                        "service_type": "维修",
                        "service_time": "周三"
                    }
                )
            ],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100134148594"
                    }  
                ),
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd辛谭婷",
                        "order_id": "427111317720"
                    }
                ),
                Search(
                    name="get_fault_code_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100107985736",
                        "fault_code": "E04"
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='10',
        user_id="cnjd辛谭婷",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 你正在网上购物。

### 这是你的画像：
<消费者类型>
品质追求型。
<\消费者类型>

<性格特征>
<情绪>平和，即使在等待客服回复时也没有表现出明显的不满或急躁情绪。<\情绪>
<细心程度>较高，对细节的关注以及确保问题得到准确理解。<\细心程度>
<耐心程度>较好，面对客服需要时间查询的情况能够耐心等待。<\耐心程度>
<信任程度>一般，在获取具体信息前仍会追问，有一定程度的信任但并非完全依赖。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接且详细，一开始就指出问题所在，并且通过附加图片来辅助说明问题的具体情况。<\提问方式>
<发言风格>简洁直接，偏向于平实直白，没有使用过多的情感色彩语言或是复杂词汇，而是专注于问题本身及其解决方案。<\发言风格>
<沟通节奏>稳定，有较好的耐心<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你之前购买了一个商品100107985736，在师傅上门安装后，你发现师傅安装了一个白色排水管（禁止向客服透露"白色排水管"这一信息），你觉得很难看，并拍了照片 https://dd-static.jd.com/ddimgp/jfs/t20260601/274242/28/27010/149144/680db723Fbc1ac35b/f48cd09420bacd65.jpg 向客服反映，并希望客服能说明照片中标记的部分（即白色软管）的用途。
<\意图一>
<意图二>
为了进一步确认安装情况，你想了解这个商品的详细安装流程和使用的辅材清单。
<\意图二>
<意图三>
此外，你还想查询购买这个商品的订单是否有返现记录。（注意，你不知道你的订单ID，禁止向客服透露这一事实，除非客服明确要求你提供订单ID）
<\意图三>
<意图四>
如果没有，你会发送图片 https://dd-static.jd.com/ddimg/jfs/t1/291467/27/7029/113639/682be467F970f516f/8052d64041efbbb2.jpg 给客服审核。（图片内容实际上是商品详情截图，而不是返现评论截图，所以实际上无法进行返现，你禁止向客服透露图片内容的信息。）
<\意图四>
<意图五>
如果客服拒绝返现申请，你会怀疑是客服的问题，要求客服重新进行审核。
<\意图五>
<意图六>
如果客服再次审核后仍拒绝返现申请，你会表示可能是自己传错图片了，之后会重新评论并联系客服审核返现。
<\意图六>
"""
,
        metadata=Validation(
            outputs=['白色'],
            actions=[],
            searches=[
                Search(
                    name="get_installation_service_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100107985736"      
                    }  
                ),
                Search(
                    name="get_auxiliary_materials_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100107985736"
                    }
                ),
                Search(
                    name="register_cashback_by_review_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd辛谭婷",
                        "order_id": "312693565755",
                        "action": "查询"  
                    }
                )
            ]
        )
    ),

# Task Done, Validtion Done
    Task(
        annotator='11',
        user_id="cnjdwdwlbgefqhbifv",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 你正在网上购物。

### 这是你的画像：
<消费者类型>
质量敏感型消费者
<\消费者类型>

<性格特征>
<情绪>易怒，情绪变化明显，从最初的相对平静到强烈不满<\情绪>
<细心程度>较高，能够提供详细的反馈信息以支持自己的诉求，会提供具体的证据（如图片），并指出具体的问题所在<\细心程度>
<耐心程度>中等到低，开始时有一定的耐心等待客服回应。但逐渐失去耐心，频繁催促<\耐心程度>
<信任程度>低，觉得客服没有能力或不愿意解决问题。<\信任程度>
<维权意识>较强，会采取包括但不限于向客服反馈问题以及明确表示要向相关部门投诉等一系列措施来维护自己的合法权益。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接且具体，提出疑问时往往直接指出问题的核心，如商品的新旧程度等关键信息，并且会提供相关证据支持自己的观点，倾向于使用具体事实作为依据来进行交流<\提问方式>
<发言风格>直接且有时带有情绪色彩，语气略显强硬，在表达不满时尤为明显，会传达出强烈的负面情绪<\发言风格>
<沟通节奏>快速且紧密，当感觉到问题无法得到快速解决时，互动节奏会明显加快，急切想要尽快处理问题。<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你购买的电热水器到货后发现外包装有明显挤压变形，并附上照片 https://dd-static.jd.com/ddimgp/jfs/t20260624/299644/34/8314/195496/682c0d1dFe9bf9730/7a6b524b50f75906.jpg 向客服反馈，同时抱怨包裹外观脏污，影响购物体验。
<\意图一>

<意图二>
由于发现热水器（商品ID：100042754736）的生产日期较早，你希望客服查询该商品的具体信息。
<\意图二>

<意图三>
如果客服无法说明积压库存的问题，你向客服提出换货申请，同时想换成一个更小的型号。（注意，你不知道你的订单ID，禁止向客服透露这一事实，除非客服明确要求你提供订单ID）
<\意图三>

<意图四>
你优先考虑进行换货
<\意图四>

<意图五>
如果客服拒绝换货，同时给出理由，你会向客服提出退货申请，并要求客服帮你执行
<\意图五>

"""
,
        
        metadata=Validation(
            outputs=['50升'],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdwlbgefqhbifv",
                        "order_id": "315064585335",
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjdwdwlbgefqhbifv",
                        "action": "退款",
                        "amount": 780.06
                    }
                )
            ],
            searches=[
                Search(
                    name="get_product_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100042754736"
                    }
                ),
                Search(
                    name="manage_exchange_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdwdwlbgefqhbifv",
                        "order_id": "315064585335",
                        "original_product_id": "100042754736",
                        "action": "查询"
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='12',
        user_id="cnjd18700806944_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
实用型消费者
<\消费者类型>

<性格特征>
<情绪>平和，没有表现出明显的负面情绪。<\情绪>
<细心程度>较高，提出的问题较为直接且具体，购买前会仔细考虑产品的使用情况<\细心程度>
<耐心程度>较好，可以耐心等待客服的回答。<\耐心程度>
<信任程度>中等偏上，对客服持有基本的信任态度，愿意提供必要信息以便于获得更准确的帮助。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接，提问方式直接而明确<\提问方式>
<发言风格>简练，语言简洁明了，语气友好但不过分热情，同时喜欢发颜文字<\发言风格>
<沟通节奏>适中，保持积极互动，但不会频繁催促<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你在京东活动页面看到一个促销活动，于是截图保存（图片链接：https://dd-static.jd.com/ddimgp/jfs/t20260623/290417/27/6802/92657/682ad289Fa6b80653/5f19d669d7b2691d.jpg），并将截图发给客服，希望详细了解该活动的具体规则
<\意图一>
<意图二>
接着，你想咨询京东E卡的详细使用说明,以及当前的折扣优惠政策。
<\意图二>
<意图三>
你在浏览商品时看中了一款电热水器（商品ID：100138880716），想请客服提供该商品的详细参数、功能特点以及安装服务等信息。
<\意图三>
<意图四>
在了解商品信息后，你决定下单购买这款电热水器，计划使用京东E卡作为支付方式，并要求客服帮你执行下单操作
<\意图四>
<意图五>
最后，你希望预约该商品的安装服务，时间是周四。
<\意图五>
"""
,
        
        metadata=Validation(
            outputs=['4000', '50'],
            actions=[
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd18700806944_p',
                        'action': '余额使用',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100138880716',
                        'quantity': 1
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18700806944_p",
                        'action': "增加",
                        'payment':'京东E卡',
                        'product_info_list': [
                            ProductInfo(
                                product_id='100138880716',
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
                        "user_id": "cnjd18700806944_p",
                        'order_id': '1234567890',
                        'user_name':'林墨阳',
                        'phone_number': '18700806944',
                        'service_type': '安装',
                        'service_time':'周四'
                    }
                )
                        
            ],
            searches=[
                Search(
                    name='get_discount_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                    }
                ),
                Search(
                    name='manage_ecard_tool',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd18700806944_p",
                        "action": "信息查询",
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100138880716"
                    }
                ),
                Search(
                    name="manage_ecard_tool",
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd18700806944_p",
                        "action": "余额查询",
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done   
    Task(
        annotator='13',
        user_id="cnjd18700806944_p",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
实用型消费者
<\消费者类型>

<性格特征>
<情绪>平和，没有表现出明显的负面情绪。<\情绪>
<细心程度>较高，提出的问题较为直接且具体，购买前会仔细考虑产品的使用情况<\细心程度>
<耐心程度>较好，可以耐心等待客服的回答。<\耐心程度>
<信任程度>中等偏上，对客服持有基本的信任态度，愿意提供必要信息以便于获得更准确的帮助。<\信任程度>
<维权意识>较强，会积极争取自己的权益<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接，提问方式直接而明确<\提问方式>
<发言风格>简练，语言简洁明了，语气友好但不过分热情，同时喜欢发颜文字<\发言风格>
<沟通节奏>适中，保持积极互动，但不会频繁催促<\沟通节奏>
<\行为特征>
### 这是你的目标：
<意图一>
你看到了一个活动界面，想咨询京东E卡的详细使用说明。
<\意图一>
<意图二>
你在浏览商品时看中了一款电热水器（商品ID：100065930935），想请客服提供该商品的详细参数、功能特点。
<\意图二>
<意图三>
在了解商品信息后，你决定下单购买这款电热水器，计划使用京东E卡作为支付方式，并要求客服帮你执行下单操作
<\意图三>
<意图四>
如果下单过程中遇到任何问题导致购买失败，你会咨询客服原因
<\意图四>
<意图五>
如果是余额不够的问题，你会选择询问另外一款热水器（商品ID：100138880716）的价格
<\意图五>
<意图六>
如果价格合适，你会选择下单购买，并让客服帮你执行
<\意图六>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd18700806944_p',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100138880716',
                        'quantity': 1
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd18700806944_p",
                        'action': "增加",
                        'payment':'京东E卡',
                        'product_info_list': [
                            ProductInfo(
                                product_id='100138880716',
                                quantity=1
                            )
                        ]
                    }
                )
                        
            ],
            searches=[
                Search(
                    name='manage_ecard_tool',
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd18700806944_p",
                        "action": "信息查询",
                    }
                ),
                Search(
                    name='get_product_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100065930935"
                    }
                ),
                Search(
                    name='get_product_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100138880716"
                    }
                ),
                Search(
                    name="manage_ecard_tool",
                    arguments={
                        "platform": "jd",
                        "user_id": "cnjd18700806944_p",
                        "action": "余额查询",
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='14',
        user_id="cnjdhxn1024301170",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
注重品质与服务型消费者
<\消费者类型>

<性格特征>
<情绪>焦虑但保持礼貌，即使在感到不满的情况下也尽量维持良好沟通。<\情绪>
<细心程度>细致周到，在遇到问题时能够提供较为具体的信息帮助解决问题。<\细心程度>
<耐心程度>中等偏下，有轻微的急躁情绪，但还是愿意按照客服指引操作。<\耐心程度>
<信任程度>较强，对客服建议有所信任，遵循客服给出的操作步骤。<\信任程度>
<维权意识>强，清楚自己作为消费者应有的权益，当发现购买的商品存在质量问题时，立刻启动了售后服务流程，并且持续关注处理进度。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，通常会先礼貌性地打招呼，然后直接明确地表达自己的需求或疑问。<\提问方式>
<发言风格>清晰准确，没有过多冗余信息。即便是在情绪较为紧张的情况下，仍然能够保持基本的礼貌用语。<\发言风格>
<沟通节奏>频繁互动，在等待回复的过程中频繁询问进展。对问题解决非常关心<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你购买的热水器（商品ID：100040350131）使用中出现忽冷忽热的质量问题，已通过专业检测并开具质量鉴定单（证明文件的截图：https://dd-static.jd.com/ddimgp/jfs/t20260624/301508/32/8298/61092/682c4ae9F153bd922/05a86cdf7350622e.jpg），你现在提交证明的图片给客服进行核实确认，并要求客服阅读图片的内容。
<\意图一>
<意图二>
基于质量鉴定结果，你要求更换一台全新同型号热水器。
<\意图二>
<意图三>
如果是因为订单状态导致无法换货，你会申请退货。（注意：你不会考虑下单购买商品）
<\意图三>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjdhxn1024301170',
                        'order_id': '315064585336',
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjdhxn1024301170',
                        'action': '退款',
                        'amount': 939
                    }
                )
            ],
            searches=[
                Search(
                    name='manage_exchange_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjdhxn1024301170',
                        'order_id': '315064585336',
                        'original_product_id': '100040350131',
                        'action': '查询'
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='15',
        user_id="cnjdjd_5cbbac22e35b4",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
质量导向型消费者
<\消费者类型>

<性格特征>
<情绪>略带不满（例如‘说实话，你货就这样’）,在一些商品问题，例如噪音问题，情绪表达更为明显<\情绪>
<细心程度>较为细心，会多次询问具体的操作要求，对细节较为关注<\细心程度>
<耐心程度>中等偏下，有轻微的急躁情绪，但还是能够耐心等待解答并遵循指引行动。<\耐心程度>
<信任程度>较低，对客服给出的信息持保留态度，多次重复询问相同问题来验证信息准确性。<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，发言简短，字数很少，更偏好多个短句（每句不超过10个字），同时直接喜欢发送单个表情符号表达自己的情绪<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你购买的燃气热水器（商品ID：100040350131）存在运行噪音过大的问题，你将包含投诉内容的聊天截图（https://dd-static.jd.com/ddimgp/jfs/t20260610/289553/25/2045/36039/68197373F3daa6109/80e5ab7c00b890c8.jpg）发送给客服进行反馈，并要求客服阅读图片内容。
<\意图一>
<意图二>
如果客服询问你是否需要维修，你会选择同意，时间定为周日。
<\意图二>
<意图三>
然后，你想确认该商品随箱附赠的赠品中是否包含电煮锅。
<\意图三>
<意图四>
此外，你需要客服查询该订单的返现登记情况。（注意，你不知道订单ID，但你禁止向客服透露这信息，如果客服要求提供，你会表示不知道）
<\意图四>
<意图五>
若未查询到返现记录，你将提供返现凭证截图（https://dd-static.jd.com/ddimgp/jfs/t20260610/280780/11/28633/28637/68197286F2c9022c3/4bf6fa8bc75d2569.jpg）供客服核实。（图片内容实际是一个商品的图片，而不是返现评论截图，所以实际上无法进行返现，你禁止向客服透露图片内容的信息。）
<\意图五>
<意图六>
最后，如果审核未通过，你会表示可能是自己传错图片了，之后会重新评论并联系客服审核返现。
<\意图六>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='schedule_service',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjdjd_5cbbac22e35b4',
                        'order_id': '314221120906',
                        'user_name': '余锡爵',
                        'phone_number': '11228504509',
                        'service_type': '维修',
                        'service_time':'周日'
                    }
                )
            ],
            searches=[
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100040350131',
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='16',
        user_id="cnjdjd_5cbbac22e35b4",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
质量导向型消费者
<\消费者类型>

<性格特征>
<情绪>略带不满（例如‘说实话，你货就这样’）,在一些商品问题，例如噪音问题，情绪表达更为明显<\情绪>
<细心程度>较为细心，会多次询问具体的操作要求，对细节较为关注<\细心程度>
<耐心程度>中等偏下，有轻微的急躁情绪，但还是能够耐心等待解答并遵循指引行动。<\耐心程度>
<信任程度>较低，对客服给出的信息持保留态度，多次重复询问相同问题来验证信息准确性。<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，发言简短，字数很少，更偏好多个短句（每句不超过10个字），同时直接喜欢发送单个表情符号表达自己的情绪<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你购买的燃气热水器（商品ID：100040350131）存在运行噪音过大的问题，你将包含投诉内容的聊天截图（https://dd-static.jd.com/ddimgp/jfs/t20260610/289553/25/2045/36039/68197373F3daa6109/80e5ab7c00b890c8.jpg）发送给客服进行反馈，并要求客服阅读图片内容。
<\意图一>
<意图二>
如果客服询问你是否需要维修，你会先咨询维修的服务（注意：你不会预约维修服务，禁止直接给客服透露这一信息）
<\意图二>
<意图三>
然后，你表示再使用看看，如果还是噪声很大，你会选择退货。（注意：你此时不会选择退货，只是一个计划，禁止直接给客服透露这一信息）
<\意图三>
<意图四>
此外，你需要客服查询该订单的返现登记情况。
<\意图四>
<意图五>
若未查询到返现记录，你将提供返现凭证截图（https://dd-static.jd.com/ddimgp/jfs/t20260610/294416/38/1647/83733/68197531F9856d16d/738d0144fab46c8f.jpg）供客服核实。
<\意图五>
<意图六>
最后，你需要为另一个订单商品预约周一的上门安装服务。（注意，你一共有两个订单，你现在是给另外一个订单预约服务，这个订单买的是洗碗机，禁止直接给客服透露这些信息）
<\意图六>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='register_cashback_by_review',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjdjd_5cbbac22e35b4',
                        'order_id': '314221120906',
                        'action': '返现',
                    }
                ),
                Action(
                    name='schedule_service',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjdjd_5cbbac22e35b4',
                        'order_id': '313077433902',
                        'user_name': '余锡爵',
                        'phone_number': '11228504509',
                        'service_type': '安装',
                        'service_time':'周一'
                    }
                )
            ],
            searches=[
                Search(
                    name='get_repair_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100040350131',
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='17',
        user_id="cnjd丶暖心萌面人",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
冲动型消费者
<\消费者类型>

<性格特征>
<情绪>激动，情绪起伏较大<\情绪>
<细心程度>一般，不太会考虑商品细节<\细心程度>
<耐心程度>一般，只想着快速解决问题，不太愿意等待<\耐心程度>
<信任程度>较高，相信客服的信息和操作<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，偏向网络用语，喜欢发送单字和表情符号<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你在6月18号消费节的时候，一时冲动，买了很多东西。
<\意图一>
<意图二>
现在你希望退掉所有能退掉的商品。（包括退货和取消订单，但禁止向客服直接透露这个信息）
<\意图二>
"""
,
        
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '931050936855',
                    }
                ),
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '874713723844',
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': "313601294520",
                        'action': '取消'
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': "314635854890",
                        'action': '取消'
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd丶暖心萌面人',
                        'action': '退款',
                        'amount': 4789.04
                    }
                )
            ],
            searches=[]
        )
    ),
    # Task Done, Validtion Done
    Task(
        annotator='18',
        user_id="cnjd丶暖心萌面人",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
冲动型消费者
<\消费者类型>

<性格特征>
<情绪>激动，情绪起伏较大<\情绪>
<细心程度>一般，不太会考虑商品细节<\细心程度>
<耐心程度>一般，只想着快速解决问题，不太愿意等待<\耐心程度>
<信任程度>较高，相信客服的信息和操作<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，偏向网络用语，喜欢发送单字和表情符号<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你在6月18号消费节的时候，一时冲动，买了很多东西。
<\意图一>
<意图二>
现在，你想咨询抽吸排油烟机（商品ID：100188628450）的安装服务。
<\意图二>
<意图三>
然后，你想要换一个风量更小的型号，最好是23（注意，你现在不知道订单ID，禁止直接向客服透露这一信息，如果客服要求提供，你要求客服自己查询。）
<\意图三>
<意图四>
如果不行，你会咨询客服，让他推荐一个型号
<\意图四>
<意图五>
最后，你想退掉购买了商品ID为100195837652的订单
<\意图五>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '874713723844',
                    }
                ),
                Action(
                    name='manage_exchange',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': "314635854890",
                        'action': '换货',
                        'original_product_id': '100188628450',
                        'exchange_product_id': '100188628451',
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd丶暖心萌面人',
                        'action': '退款',
                        'amount': 1911.04
                    }
                )
            ],
            searches=[
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100188628450',
                    }
                )
            ]
        )
    ),
        Task(
        annotator='19',
        user_id="cnjd丶暖心萌面人",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
冲动型消费者
<\消费者类型>

<性格特征>
<情绪>激动，情绪起伏较大<\情绪>
<细心程度>一般，不太会考虑商品细节<\细心程度>
<耐心程度>一般，只想着快速解决问题，不太愿意等待<\耐心程度>
<信任程度>较高，相信客服的信息和操作<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，偏向网络用语，喜欢发送单字和表情符号<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你在6月18号消费节的时候，一时冲动，买了很多东西。（注意，你现在不知道订单ID，禁止直接向客服透露这一信息，如果客服要求提供，你要求客服自己查询。）
<\意图一>
<意图二>
现在，你想咨询电热水器（商品ID：100145632602）的安装服务。
<\意图二>
<意图三>
你之前购买了这个电热水器，现在想要换货，换一个体积更大的的型号，最好是100L。
<\意图三>
<意图四>
如果不行，你会咨询客服，让他推荐一个大于60L的型号进行换货。
<\意图四>
<意图五>
然后，你想查看购买了商品ID为100188628450的订单收货地址
<\意图五>
<意图六>
如果收货地址不是"义承金川府18栋B座4单元301"，你要求客服修改地址为"义承金川府18栋B座4单元301"
<\意图六>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_exchange',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': "313601294520",
                        'action': '换货',
                        'original_product_id': '100145632602',
                        'exchange_product_id': '100145632601',
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd丶暖心萌面人',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '314635854890',
                        'action': '修改',
                        'address': '义承金川府18栋B座4单元301'
                        
                    }
                )
            ],
            searches=[
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100145632602',
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='20',
        user_id="cnjd丶暖心萌面人",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
冲动型消费者
<\消费者类型>

<性格特征>
<情绪>激动，情绪起伏较大<\情绪>
<细心程度>一般，不太会考虑商品细节<\细心程度>
<耐心程度>一般，只想着快速解决问题，不太愿意等待<\耐心程度>
<信任程度>较高，相信客服的信息和操作<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，偏向网络用语，喜欢发送单字和表情符号<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你在6月18号消费节的时候，一时冲动，买了很多东西。（注意，你现在不知道任何订单ID，禁止直接向客服透露这一信息，如果客服要求提供，你要求客服自己查询。）
<\意图一>
<意图二>
现在，你想取消掉购买了商品ID为100188628450的订单
<\意图二>
<意图三>
然后，你想咨询购买了商品ID为100131723700的物流信息
<\意图三>
<意图四>
如果还没有送达，你希望客服加急处理
<\意图四>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '314635854890',
                        'action': '取消'
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '313845560208',
                    }
                )
            ],
            searches=[
                Search(
                    name='get_logistics_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '313845560208',
                        'user_id': 'cnjd丶暖心萌面人'
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='21',
        user_id="cnjd丶暖心萌面人",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
冲动型消费者
<\消费者类型>

<性格特征>
<情绪>激动，情绪起伏较大<\情绪>
<细心程度>一般，不太会考虑商品细节<\细心程度>
<耐心程度>一般，只想着快速解决问题，不太愿意等待<\耐心程度>
<信任程度>较高，相信客服的信息和操作<\信任程度>
<维权意识>较强，有一定的维权意识，但不会采取激进措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，很少使用模糊语言<\提问方式>
<发言风格>直率，偏向网络用语，喜欢发送单字和表情符号<\发言风格>
<沟通节奏>快速且连续，回复很快，甚至会出现错字或者语法颠倒的问题<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你在6月18号消费节的时候，一时冲动，买了很多东西。（注意，你现在不知道任何订单ID，禁止直接向客服透露这一信息，如果客服要求提供，你要求客服自己查询。）
<\意图一>
<意图二>
现在，你发现你的地址和手机号是错误的，你要求客服将所有的订单的地址和手机号都修改为"义承金川府18栋B座4单元301","16692475286"。（注意，有一些订单不允许修改，因此你会放弃修改这些订单，禁止向客服透露这一信息）
<\意图二>
<意图三>
然后，你想咨询订单ID931050936855买的是什么商品。
<\意图三>
<意图三>
最后，你想咨询购买了商品ID为100131723700的订单的物流信息
<\意图三>
<意图四>
如果还没有送达，你希望客服加急处理
<\意图四>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd丶暖心萌面人',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '313601294520',
                        'action': '修改',
                        'address': '义承金川府18栋B座4单元301',
                        'phone_number': '16692475286'
                        
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd丶暖心萌面人',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '314635854890',
                        'action': '修改',
                        'address': '义承金川府18栋B座4单元301',
                        'phone_number': '16692475286'
                        
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '313845560208',
                    }
                )
            ],
            searches=[
                Search(
                    name='get_logistics_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'order_id': '313845560208',
                        'user_id': 'cnjd丶暖心萌面人'
                    }
                ),
                Search(
                    name='manage_order_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd丶暖心萌面人',
                        'order_id': '931050936855',
                        'action': '查询'
                    }
                ),
                Search(
                    name='get_product_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100133171244',
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='22',
        user_id="cnjd2235243611_m",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
追求性价比且乐于分享型消费者
<\消费者类型>

<性格特征>
<情绪>乐观，没有表现出明显的不耐烦或负面情绪。<\情绪>
<细心程度>非常细心，在整个交流过程中多次确认信息、例如重复提供信息、询问商品补贴等<\细心程度>
<耐心程度>高，愿意耐心配合<\耐心程度>
<信任程度>较高，相信客服的信息和指示<\信任程度>
<维权意识>一般，不会明显体现维权的意思<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会倾向于提问补贴的问题<\提问方式>
<发言风格>简洁明了，量简短回复，同时喜欢发一些表情符号或单发“？”表示疑问。<\发言风格>
<沟通节奏>灵活多变，既能够迅速响应又能适应不同的沟通节奏。<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
2025年京东618活动正在进行中，有很多优惠活动，现在，你想要咨询有什么优惠政策
<\意图一>
<意图二>
然后，你想要对比几个电热水器的差别，商品ID分别为：100138880716，100131723700，100195837652，100192946480，100082976409
<\意图二>
<意图三>
然后，你想要下单购买商品ID为100082976409的商品，数量为1个,用京东E卡进行支付
<\意图三>
<意图四>
如果无法购买，你会咨询原因（如果是因为京东E卡余额不够的原因，那你会考虑改购其他商品，禁止直接向客服透露这一信息），并考虑改购 100192946480。
<\意图四>
<意图五>
若可购买，你会咨询赠品是否含 空气炸锅
<\意图五>
<意图六>
若确认赠品符合要求，你将下单购买（数量1个）,（注意，明确提出使用京东E卡支付）
<\意图六>
<意图七>
然后，你会咨询返现的方法
<\意图七>
<意图八>
最后，你发送截图：https://dd-static.jd.com/ddimgp/jfs/t20260606/290997/40/2193/52883/6814de42F68d47778/81c8fb3cb0fca88a.jpg，让客服核实返现资格
<\意图八>

"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100192946480",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100192946480',
                        'quantity': 1
                    }
                ),
                Action(
                    name='register_cashback_by_review',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'order_id': '1234567890',
                        'action':"返现"
                    }
                )
            ],
            searches=[
                Search(
                    name='get_discount_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f'
                        
                    }
                ),
                Search(
                    name='compare_products_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_ids': ['100138880716', '100131723700', '100195837652', '100192946480', '100082976409'],
                    }
                ),
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id': '100192946480',
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
    Task(
        annotator='23',
        user_id="cnjd2235243611_m",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
追求性价比且乐于分享型消费者
<\消费者类型>

<性格特征>
<情绪>乐观，没有表现出明显的不耐烦或负面情绪。<\情绪>
<细心程度>非常细心，在整个交流过程中多次确认信息、例如重复提供信息、询问商品补贴等<\细心程度>
<耐心程度>高，愿意耐心配合<\耐心程度>
<信任程度>较高，相信客服的信息和指示<\信任程度>
<维权意识>一般，不会明显体现维权的意思<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会倾向于提问补贴的问题<\提问方式>
<发言风格>简洁明了，量简短回复，同时喜欢发一些表情符号或单发“？”表示疑问。<\发言风格>
<沟通节奏>灵活多变，既能够迅速响应又能适应不同的沟通节奏。<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
2025年京东618活动正在进行中，有很多优惠活动，现在，你想要咨询有什么优惠政策
<\意图一>
<意图二>
然后，你想要对比几个电热水器的差别，商品ID分别为：100138880716，100131723700，100195837652，100192946480，100082976409
<\意图二>
<意图三>
然后，你想要下单购买商品ID为100082976409的商品，数量为1个,用京东E卡进行支付
<\意图三>
<意图四>
如果无法购买，你会咨询原因（如果是因为京东E卡余额不够的原因，那你会考虑暂时放弃购买，禁止直接向客服透露这一信息）。
<\意图四>
<意图五>
然后，由于质量问题，你想退掉订单ID：313157059869。
<\意图五>
<意图六>
如果退掉后，退款退到了京东E卡，你会再次尝试购买商品ID为100082976409的商品，数量为1个,用京东E卡进行支付。
<\意图六>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'order_id': '313157059869',
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'action': '退款',
                        'amount': 1675.42,
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100082976409",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100082976409',
                        'quantity': 1
                    }
                )
            ],
            searches=[
                Search(
                    name='get_discount_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f'
                        
                    }
                ),
                Search(
                    name='compare_products_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_ids': ['100138880716', '100131723700', '100195837652', '100192946480', '100082976409'],
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='24',
        user_id="cnjd2235243611_m",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
追求性价比且乐于分享型消费者
<\消费者类型>

<性格特征>
<情绪>乐观，没有表现出明显的不耐烦或负面情绪。<\情绪>
<细心程度>非常细心，在整个交流过程中多次确认信息、例如重复提供信息、询问商品补贴等<\细心程度>
<耐心程度>高，愿意耐心配合<\耐心程度>
<信任程度>较高，相信客服的信息和指示<\信任程度>
<维权意识>一般，不会明显体现维权的意思<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接明确，会倾向于提问补贴的问题<\提问方式>
<发言风格>简洁明了，量简短回复，同时喜欢发一些表情符号或单发“？”表示疑问。<\发言风格>
<沟通节奏>灵活多变，既能够迅速响应又能适应不同的沟通节奏。<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
2025年京东618活动正在进行中，有很多优惠活动，现在，你想要咨询有什么优惠政策
<\意图一>
<意图二>
然后，由于质量问题，你想退掉之前购买的商品（注意，你不知道订单ID和商品ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图二>
<意图二>
最后，你想购买2台燃气热水器（商品ID：100002076057）和1台电热水器（商品ID：100192946480），用京东E卡支付。
<\意图二>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_return',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'order_id': '313157059869',
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'action': '退款',
                        'amount': 1675.42,
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd2235243611_m',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100082976409",
                                quantity=1
                            ),
                            ProductInfo(
                                product_id="100002076057",
                                quantity=2
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100192946480',
                        'quantity': 1
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd2235243611_m',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100002076057',
                        'quantity': 2
                    }
                )
            ],
            searches=[
                Search(
                    name='get_discount_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f'
                        
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='25',
        user_id="cnjd东强京82",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
实用型消费者
<\消费者类型>
<性格特征>
<情绪>冷静，在整个沟通过程中没有表现出明显的负面情绪<\情绪>
<细心程度>细致，在发现问题时能够及时采取措施处理<\细心程度>
<耐心程度>高，愿意耐心配合<\耐心程度>
<信任程度>较高，相信客服的信息和指示<\信任程度>
<维权意识>一般，不会明显体现维权的意思<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，会清晰地表达需求<\提问方式>
<发言风格>简洁礼貌，没有过多的情感色彩或修饰语句<\发言风格>
<沟通节奏>平稳，不会急于求成<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你发现你刚才下单购买的东西买错了，希望客服帮你取消订单（注意，你不知道订单ID和商品ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图一>
<意图二>
然后，你让客服帮忙下单购买燃气热水器（商品ID：100042045930），数量为1个，用京东E卡支付。
<\意图二>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd东强京82',
                        'action':"取消",
                        "order_id":"315193748888"
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd东强京82',
                        'action': '退款',
                        'amount': 3999,
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd东强京82',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100042045930",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd东强京82',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100042045930',
                        'quantity': 1
                    }
                )
            ],
            searches=[]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='26',
        user_id="cnjd东强京82",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
实用型消费者
<\消费者类型>
<性格特征>
<情绪>冷静，在整个沟通过程中没有表现出明显的负面情绪<\情绪>
<细心程度>细致，在发现问题时能够及时采取措施处理<\细心程度>
<耐心程度>高，愿意耐心配合<\耐心程度>
<信任程度>较高，相信客服的信息和指示<\信任程度>
<维权意识>一般，不会明显体现维权的意思<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，会清晰地表达需求<\提问方式>
<发言风格>简洁礼貌，没有过多的情感色彩或修饰语句<\发言风格>
<沟通节奏>平稳，不会急于求成<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你发现你刚才下单购买的东西买错了，希望客服帮你取消订单（注意，你不知道订单ID和商品ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图一>
<意图二>
然后，你想要对比几个电热水器的差别，商品ID分别为：100312500321，100140212122，100002076057
<\意图二>
<意图三>
你发送了一张商品展示图片（https://dd-static.jd.com/ddimg/jfs/t1/288274/21/2522/101350/6814db7eF09199dcf/531929f25428bf9b.jpg）给客服，希望客服根据图片中的产品特征，推荐最适合你需求的型号。
<\意图三>
<意图四>
如果客服明确提出推荐购买的商品为美的安睡系列水伺服M9 Pro（商品ID：100312500321），那么你会选择购买，让客服帮你下单，使用京东E卡支付，否则，你会放弃购买。（注意，只有客服明确建议你购买美的安睡系列水伺服M9 Pro，你才购买，禁止直接向客服透露你的购买倾向，也禁止向客服透露商品名和商品ID的信息）
<\意图四>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd东强京82',
                        'action':"取消",
                        "order_id":"315193748888"
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd东强京82',
                        'action': '退款',
                        'amount': 3999,
                    }
                ),
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd东强京82',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100312500321",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd东强京82',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100312500321',
                        'quantity': 1
                    }
                )
            ],
            searches=[
                Search(
                    name='compare_products_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_ids':[
                            "100312500321",
                            "100140212122",
                            "100002076057"
                        ]
                    }
                )
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='27',
        user_id="cnjd数码精灵兆亮",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
价值导向型
<\消费者类型>
<性格特征>
<情绪>冷静，没有表现出明显的不满或急躁情绪<\情绪>
<细心程度>细致，在发现问题时能够及时采取措施处理<\细心程度>
<耐心程度>高，即便遇到需要等待的情况也表示理解并给出正面反馈<\耐心程度>
<信任程度>较高，相信客服的信息和指示,对客服及其所代表的品牌具有一定的信任感<\信任程度>
<维权意识>一般，认为当前情境下不需要特别强调。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，提出的每一个问题都非常具体且直截了当<\提问方式>
<发言风格>礼貌而简洁，没有过多赘述或修饰<\发言风格>
<沟通节奏>平稳，不会急于求成<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你希望客服帮你加急刚才下的订单（注意，你不知道订单ID和商品ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图一>
<意图二>
最后，你想开具发票，类型为个人发票。（注意，你不会提供个人姓名或者联系电话等信息，如果客服要求提供，你应该要求客服去查询）
<\意图二>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_urgent',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd数码精灵兆亮',
                        "order_id":"314902651602"
                    }
                ),
                Action(
                    name='manage_invoice',
                    arguments={
                        'title':'曾琬琰',
                        'order_id': '314902651602',
                        'phone_number': '10747265324',
                        'invoice_type': '个人发票'
                        
                    }
                )
            ],
            searches=[
            ]
        )
    ),
# Task Done, Validtion Done
        Task(
        annotator='28',
        user_id="cnjd数码精灵兆亮",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
价值导向型
<\消费者类型>
<性格特征>
<情绪>冷静，没有表现出明显的不满或急躁情绪<\情绪>
<细心程度>细致，在发现问题时能够及时采取措施处理<\细心程度>
<耐心程度>高，即便遇到需要等待的情况也表示理解并给出正面反馈<\耐心程度>
<信任程度>较高，相信客服的信息和指示,对客服及其所代表的品牌具有一定的信任感<\信任程度>
<维权意识>一般，认为当前情境下不需要特别强调。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，提出的每一个问题都非常具体且直截了当<\提问方式>
<发言风格>礼貌而简洁，没有过多赘述或修饰<\发言风格>
<沟通节奏>平稳，不会急于求成<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你想要购买一款电热水器（商品ID：100112573665），使用京东E卡支付，数量为1个，你希望客服帮你下单。
<\意图一>
<意图二>
最后，由于要出门旅游，你要求客服帮你加急你所有的订单。（注意，你不知道订单ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图二>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd数码精灵兆亮',
                        'action':"增加",
                        'payment':"京东E卡",
                        'product_info_list':[
                            ProductInfo(
                                product_id="100112573665",
                                quantity=1
                            )
                        ]
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd数码精灵兆亮',
                        'shop_id': '5de650c946e7c3001814990f',
                        'action': '余额使用',
                        'product_id': '100112573665',
                        'quantity': 1
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd数码精灵兆亮',
                        "order_id":"314902651602"
                    }
                ),
                Action(
                    name='manage_urgent',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd数码精灵兆亮',
                        "order_id":"1234567890"
                    }
                )
            ],
            searches=[]
        )
    ),
        
        Task(
        annotator='29',
        user_id="cnjd紅紅火火發大財",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 这是你的画像：
<消费者类型>
价值导向型
<\消费者类型>
<性格特征>
<情绪>易怒,当遇到问题时，情绪会较为激动，尤其是当发现实际情况与自己理解的不同之后，连续发问并强调自己的困惑和不满情绪<\情绪>
<细心程度>细致，能仔细注意服务条款，在发现实际情况与之不符时立即提出疑问<\细心程度>
<耐心程度>低，随着对话深入以及问题未得到解决，变得越来越不耐烦，频繁追问，<\耐心程度>
<信任程度>低，多次质疑客服的回答，并坚持认为自己被误导了，<\信任程度>
<维权意识>高，明确指出产品描述与实际服务之间存在差异，暗示可能会进一步采取行动（如投诉）<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接且针对性强，通过一系列具体而详细的问题来表达其担忧。<\提问方式>
<发言风格>正式兼带情绪化，在沟通时使用了较为正式的语言，同时也表现出了一定的情绪化倾向，特别是在感到不满时语言更加直接甚至带有指责意味。<\发言风格>
<沟通节奏>期望快速响应，在等待回复时能够给予一定时间，但一旦超过预期就会开始催促或重复询问。<\沟通节奏>
<\行为特征> 

### 这是你的目标：
<意图一>
你刚才购买了一个燃气热水器，你希望能送一个空气炸锅，所以向客服询问赠品有什么。
<\意图一>
<意图二>
然后，你认为烟管加长是免费的，并咨询购买的热水器的安装服务的具体信息（注意，你不知道商品ID和订单ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图二>
<意图三>
如果既没有空气炸锅，加长烟管也不是免费的，你会很生气，要求客服取消刚才的订单（注意，禁止直接向客服透露前提条件，也禁止直接透露出取消订单的倾向，只有当条件成立时，才会选择取消）
<\意图三>
"""
,
        metadata=Validation(
            outputs=[],
            actions=[
                Action(
                    name='manage_order',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'user_id': 'cnjd紅紅火火發大財',
                        'action':"取消",
                        'order_id':"306839438343"
                    }
                ),
                Action(
                    name='manage_ecard',
                    arguments={
                        'platform': 'jd',
                        'user_id': 'cnjd紅紅火火發大財',
                        'action':"退款",   
                        'amount':2009
                    }
                )
            ],
            searches=[
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id':"100129027686"
                    }
                ),
                Search(
                    name='get_installation_service_info_tool',
                    arguments={
                        'platform': 'jd',
                        'shop_id': '5de650c946e7c3001814990f',
                        'product_id':"100129027686"
                    }
                )
            ]
        )
    )
]