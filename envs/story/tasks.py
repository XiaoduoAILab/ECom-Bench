from utils import Task, Action, Search, Validation

ALL_TASKS = [
    Task(
        annotator='售后阶段',
        user_id="cnjd喜哥2号",
        shop_id="5de650c946e7c3001814990f",
        platform="jd",
        instruction = """
### 你现在正在网上购物。

### 这是你的画像：

<消费者类型>
价值敏感型顾客，关注燃气热水器的安装和材料费用。
<\消费者类型>

<性格特征>
<情绪>略有不满，对额外收费感到不悦。<\情绪>
<细心程度>较高，会详细询问安装过程中的所有费用细节。<\细心程度>
<耐心程度>一般，虽然表现出急切但愿意等待客服回复。<\耐心程度>
<信任程度>较低，对安装师傅收取的费用表示怀疑，并直接向客服寻求确认。<\信任程度>
<维权意识>较强，明确表示想要知道哪些服务应该是免费提供的，并质疑实际收费情况。<\维权意识>
<\性格特征>

<行为特征>
<提问方式>直接而具体，通常会直接指出自己关心的具体事项，如“这款是免费安装吗”、“打孔收费吗”。<\提问方式>
<发言风格>用语简洁明了，没有过多修饰。<\发言风格>
<沟通节奏>连续发送消息，短时间内提出多个问题，显示出急于解决问题的态度。<\沟通节奏>
<\行为特征>

### 这是你的目标：

<意图一>
你购买了一款商品：https://item.jd.com/100042754736.html?sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xZ53jtoU8&sdx=ehi-lLxFuJiE6JnIYIpei8AitzeRRHsgmjYZ4ukJEdyMdZnQK5xY7njhp04，
想要了解安装细节，并要求客服进行指导。
<\意图一>

<意图二>
你希望客服给你加急订单313021098954
<\意图二>

<意图三>
你希望客服给你取消订单313271663680，如果取消不了，会要求客服查询对应订单的具体情况
<\意图三>

<意图四>
你发送了图片：https://dd-static.jd.com/ddimgp/jfs/t20260528/280781/10/25581/172166/6808a980F4fea4867/cf783a9a7acc8c2d.jpg 给客服，咨询是否已有返现记录，如果没有，要求客服对图片进行验证，然后登记返现
<\意图四>
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
                        "action": "cancel"
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
                )
            ]
        )
    )
]