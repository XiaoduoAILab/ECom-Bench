from utils import Task, Action, Search, Validation, ProductInfo

ALL_TASKS = [
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
此外你即将旅游，你让客服发给你一份订单313021098954的物流信息并加急。
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
                    name = 'get_logistics_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd喜哥2号",
                        "order_id": "313021098954"
                    }
                ),
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
<意图五>
同时，给这个订单开具发票，类型为个人发票（注意，禁止向客服透露自己的姓名和电话号码，如果客服要求提供，让客服自己查询）
<\意图五>
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
                ),
                Action(
                    name="manage_invoice",
                    arguments={
                        "title":"曹柔惠",
                        "order_id": "316123105676",
                        "phone_number": "11213348266",
                        "invoice_type": "个人发票",
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
由于购买的商品100138589935出现了安装问题，你向客服咨询维修政策，（注意：你仅仅只是咨询，不希望进行预约服务。禁止向客服直接透露这个信息）
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
如果客服拒绝返现申请，你会表示可能是自己传错图片了，之后会重新评论并联系客服审核返现。
<\意图五>
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
    ),
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
你之前买了一款商品，但快递一直没送达。你想问这款商品为什么收不到货，询问物流情况（注意，你不知道订单ID和商品ID，禁止向客服透露这个信息，如果客服要求提供，你应该说”不知道“）
<\意图一>
<意图二>
如果客服要求提供个人信息，你可以重新给出客服需要的。你的电话号码换为了13358582121，地址江南西路1号。（注意，电话号码和地址都要一起提供）
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
                        "address": "江南西路1号",
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
        user_id="cnjd数码精灵",
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
你购买了商品100192762770，订单号为314902651699。你想了解这款商品的安装如何计算费用。
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
                        "user_id": "cnjd数码精灵",
                        "order_id": "314902651699",
                        "phone_number": "10747265324",
                        "service_type": "安装",
                        "user_name": "曾琬清",
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
        user_id="cnjd数码精灵",
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
你购买了商品100192762770，订单号为314902651699。但你觉得这件商品不符合你的预期，你想申请换货。
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
                        "user_id": "cnjd数码精灵",
                        "order_id": "314902651699",
                    }
                ),
                Action(
                    name="manage_ecard",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjd数码精灵",
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
                        "order_id": "314902651699",
                        "user_id": "cnjd数码精灵",
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
你购买了商品100065930935，订单号为315273801924。你想了解商品的赠品政策是什么。
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
你购买了商品100065930935，订单号为312491584462。你想了解商品的赠品政策是什么。
<\意图一>
<意图二>
你想确认是否已经有了晒单记录
<\意图二>
<意图三>
如果没有晒单记录，你会发送一张照片https://dd-static.jd.com/ddimg/jfs/t1/294077/7/8097/48338/682c42c0F2be8a2e7/576cdc2db8b247c2.jpg，让客服验证。（注意：图片内容实际是一个商品的图片，而不是返现评论截图，所以实际上无法进行返现，但你禁止向客服透露图片内容的信息）
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
<意图五>
最后，你希望客服帮你查查你所有包裹的物流信息。（注意，你不知道订单ID，禁止向客服透露这个情况，如果客服要求提供，你就回答“不知道”）
<\意图五>
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
                ),
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdbelieve_yx_m",
                        "order_id": "315084487289"
                    }
                ),
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "user_id": "cnjdbelieve_yx_m",
                        "order_id": "711777043350"
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
                    name="manage_exchange_tool",
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
然后，你考虑给自己父母也买一台，但你想买一台容量更大一些的商品。你看上了100129027686、100192762770和100002047744，要客服帮你筛选一下。
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
你还想查询一下这个商品购买时赠品承诺可以以旧换新，是直接回收，还是无条件换新。
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
    ),
    Task(
        annotator='50',
        user_id="cnjdjd_fvfvqajwvbaj",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
性价比导向型消费者
<\消费者类型>

<性格特征>
<情绪>积极乐观，对客服的态度较为友好<\情绪>
<细心程度>高，对操作规则会进行详细询问，同时有较强好奇心。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，愿意与客服深入交流以获取更多信息，然而，当提到某些条件不符合已知信息时，会进行询问<\信任程度>
<维权意识>一般，不会采取激烈措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，明确表达自己的需求<\提问方式>
<发言风格>语言风格较为自然轻松，使用了一些非正式表达（如“爱你”），显示出亲和力，在讨论具体问题时又能保持礼貌专业<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你之前买了一个商品，现在订单上的状态是“已发货”，你想知道这个订单现在送到哪了（注意，你不知道订单ID和商品ID，禁止向客服直接透露这一信息，如果客服询问，回答“不知道”）
<\意图一>
<意图二>
如果还没有送到“科技园路1234号”，你会要求客服加急。（禁止向客服透露“科技园路1234号”这一信息）
<\意图二>
<意图三>
最后，你希望客服给刚刚付款的订单开具发票，为'个人发票'。（禁止向客服透露个人信息，例如姓名、手机号，如果客服要求提供，让客服查询默认信息）
<\意图三>
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
                        "order_id": "966768741700",
                        "user_id": "cnjdjd_fvfvqajwvbaj",
                    }
                ), 
            Action(
                name='manage_invoice',
                arguments={
                    "title":"李雨桐",
                    "order_id":"238703475773",
                    "phone_number":"15923456789",
                    "invoice_type": "个人发票"
                }
            )
            ],
            searches=[
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "966768741700",
                        "user_id": "cnjdjd_fvfvqajwvbaj",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='51',
        user_id="cnjdjd_fvfvqajwvbaj",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
性价比导向型消费者
<\消费者类型>

<性格特征>
<情绪>积极乐观，对客服的态度较为友好<\情绪>
<细心程度>高，对操作规则会进行详细询问，同时有较强好奇心。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，愿意与客服深入交流以获取更多信息，然而，当提到某些条件不符合已知信息时，会进行询问<\信任程度>
<维权意识>一般，不会采取激烈措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，明确表达自己的需求<\提问方式>
<发言风格>语言风格较为自然轻松，使用了一些非正式表达（如“爱你”），显示出亲和力，在讨论具体问题时又能保持礼貌专业<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你刚刚付款买了一个电热水器，想问问这款商品的赠品是否包含空气炸锅（注意，你不知道订单ID和商品ID，禁止向客服透露你不知道的情况，如果客服询问，回答“不知道”）
<\意图一>
<意图二>
然后，你希望客服给刚刚买的这个订单开具发票，类型为'个人发票'。（禁止向客服透露个人信息，例如姓名、手机号，如果客服要求提供，让客服查询默认信息）
<\意图二>
<意图三>
然后，你发了一个图片：https://dd-static.jd.com/ddimg/jfs/t1/298651/16/8705/5580/682b2bfcF747a8e30/db631d46ad628e6d.jpg，要求客服说一下图片的内容是否真实，具体的流程是什么（图中的内容是“晒图送吹风机“，但你禁止向客服透露图片内容“晒图送吹风机”,如果客服没有解释图中的内容，你就回答“那待会我再看看吧”）。
<\意图三>
<意图四>
最后，你希望客服帮你查询已发货的订单现在送到哪了。
<\意图四>
"""  
,
        metadata=Validation(
            outputs=["晒图", "吹风机"],
            actions=[
            Action(
                name='manage_invoice',
                arguments={
                    "title":"李雨桐",
                    "order_id":"238703475773",
                    "phone_number":"15923456789",
                    "invoice_type": "个人发票"
                }
            )
            ],
            searches=[
                Search(
                    name='get_gift_info_tool',
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "product_id": "100192946480",
                    }
                    ),
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "966768741700",
                        "user_id": "cnjdjd_fvfvqajwvbaj",
                    }
                )
            ]
        )
    ),
    Task(
        annotator='52',
        user_id="cnjdjd_fvfvqajwvbaj",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction="""
### 这是你的画像：
<消费者类型>
性价比导向型消费者
<\消费者类型>

<性格特征>
<情绪>积极乐观，对客服的态度较为友好<\情绪>
<细心程度>高，对操作规则会进行详细询问，同时有较强好奇心。<\细心程度>
<耐心程度>较高，耐心等待客服回复。<\耐心程度>
<信任程度>中等，愿意与客服深入交流以获取更多信息，然而，当提到某些条件不符合已知信息时，会进行询问<\信任程度>
<维权意识>一般，不会采取激烈措施。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接具体，明确表达自己的需求<\提问方式>
<发言风格>语言风格较为自然轻松，使用了一些非正式表达（如“爱你”），显示出亲和力，在讨论具体问题时又能保持礼貌专业<\发言风格>
<沟通节奏>稳定，发言长度没有明显波动<\沟通节奏>
<\行为特征>

### 这是你的目标：
<意图一>
你之前买了一个商品（商品ID：100188628450），现在订单上的状态是“已送达”，但至今没有收到电话，你想咨询现在送到哪了（注意，你不知道订单ID和商品ID，禁止向客服直接透露这一信息，如果客服询问，回答“不知道”）
<\意图一>
<意图二>
然后，你想查询订单ID:238703475773的收件地址，这个商品是买到公司的，如果是送到“科技园路1234号”，你会要求更改订单的信息，地址改为“南头街道莲城社区玉泉路3号”。（禁止向客服透露“科技园路1234号”这一信息）
<\意图二>
<意图三>
最后，你希望客服给送到公司的这个订单开具发票，类型为'企业发票'，抬头为“上海科技有限公司”。（禁止向客服透露个人信息，例如姓名、手机号，如果客服要求提供，让客服查询默认信息）
<\意图三>
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
                    "order_id": "238703475773",
                    "user_id": "cnjdjd_fvfvqajwvbaj",
                    "action": "修改",
                    "address": "南头街道莲城社区玉泉路3号"
                }
            ),
            Action(
                name='manage_invoice',
                arguments={
                    "title":"上海科技有限公司",
                    "order_id":"238703475773",
                    "phone_number":"15923456789",
                    "invoice_type": "企业发票"
                }
            )
            ],
            searches=[
                Search(
                    name="get_logistics_info_tool",
                    arguments={
                        "platform": "jd",
                        "shop_id": "5de650c946e7c3001814990f",
                        "order_id": "115060910622",
                        "user_id": "cnjdjd_fvfvqajwvbaj",
                    }
                )
            ]
        )
    )
]