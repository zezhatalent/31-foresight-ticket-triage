PRIORITY_1_CUES = ["angry", "unacceptable", "legal", "manager", "escalate", "worst"]
PRIORITY_2_CUES = ["days", "still not", "pending", "delayed", "no response"]

QUEUE_RULES = [
    ("payments", ["payment", "paid", "upi", "refund", "deduct", "transaction"]),
    ("account_access", ["login", "otp", "password", "locked", "invalid"]),
    ("returns_warranty", ["return", "exchange", "replacement", "defective", "warranty", "broken"]),
    ("b2b_sales", ["quotation", "bulk", "gst invoice", "corporate", "purchase order"]),
]

SUGGESTED_REPLIES = {
    "payments": "We've escalated your payment issue to our payments team — you'll get an update within 24 hours.",
    "account_access": "Our login team can fix this quickly. Please try resending the OTP; if it fails again we'll reset access manually.",
    "returns_warranty": "Your request qualifies under warranty/return policy. Free pickup will be scheduled within 24 hours.",
    "b2b_sales": "Thanks for your interest! Our corporate sales team will send a quotation with GST details today.",
}


def triage(ticket: dict) -> dict:
    text = f"{ticket.get('subject', '')} {ticket.get('body', '')}".lower()
    queue, hits = "general", 0
    for name, keywords in QUEUE_RULES:
        n = sum(1 for kw in keywords if kw in text)
        if n > hits:
            queue, hits = name, n
    priority = "P1" if any(c in text for c in PRIORITY_1_CUES) else "P2" if any(c in text for c in PRIORITY_2_CUES) else "P3"
    confidence = min(95, 55 + hits * 12 + (10 if queue != "general" else 0))
    return {
        "queue": queue,
        "priority": priority,
        "confidence": confidence,
        "suggested_reply": SUGGESTED_REPLIES.get(queue, "Thanks for reaching out — our team will respond within one business day."),
    }


if __name__ == "__main__":
    import json

    with open("tickets_mock.json", encoding="utf-8") as f:
        tickets = json.load(f)
    print("=== ForeSight Triage — routing decisions ===\n")
    for t in tickets:
        d = triage(t)
        lane = "AI" if d["confidence"] >= 70 else "HUMAN REVIEW"
        print(f"{t['id']} [{d['priority']}] -> {d['queue']} ({d['confidence']}% conf) [{lane}]")
        print(f"   reply: {d['suggested_reply']}\n")
