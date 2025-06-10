import json
def manage_invoice(data, title, order_id, phone_number, invoice_type):
    # if any(x is None or len(x) == 0 for x in [title, order_id, phone_number, invoice_type]):
    #     return data, "参数信息不全, 请重新输入"
    invoice = {
        "发票抬头": title,
        "发票类型": invoice_type,
        "订单ID": order_id,
        "手机号码": phone_number,
    }
    if not data.get("invoices"):
        data["invoices"] = {}
    data["invoices"][order_id] = invoice
    return data, f"已成功开具发票{json.dumps(invoice, ensure_ascii=False)}"