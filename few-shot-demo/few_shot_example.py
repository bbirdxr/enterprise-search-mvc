import json

examples = [{
    "scenario":
    "I havent recieved the items I bought on your website, where is my item?",
    "conversations":
    """
User:I havent recieved the items I bought on your website, where is my item?
Assistant : I'm sorry to hear that the item doesn't fit your habit. Wait a minite, I have retrieved the latest order information for you.[order_info in context]
Is this the order you want to query?/ There are some orders, please tell me which one you you mean? [order_list in context]
User: Yes. (confirm)
Assistant: I have retrieved the logistics information for you. [logistic information in context] Is this the logistics information you want to query?
User: Yes. (confirm)
Assistant: I am horner to help you. Have a good time.
"""
}, {
    "scenario":
    "shipping region, delivery items to my country",
    "conversations":
    """
User: Can you ship to my country?
Assistant: According to your account information, are you currently in ...(country name)?
User: Yes.(Confirm)
Assistant: Wish cannot ship to ... Here is a list of countries/regions we currently ship to: ... For a more extensive range of shipping destinations, please check the web: https://cs-help.wish.com/hc/en-us/articles/360028449291-Can-you-ship-to-my-country-
User: Why can't you deliver to my country?
Assistant: In order to focus on other business areas, Wish will no longer provide services to customers in certain countries. We are working hard to simplify our operations and improve the Wish marketplace. Due to this, we made the difficult decision to cease services to some markets. As of June 1, 2023, customers in Jersey Island will no longer be able to shop on the Wish marketplace. We apologize to all loyal Wish customers affected by these changes. We regularly evaluate growth opportunities in the global market. Please make sure to check the location page for the latest updates.
System Notification: [Session timed out, feedback popup appears]
"""
}, {
    "scenario":
    "recognizes the severity and sensitivity of the issue and offers to transfer the user to human support",
    "conversations":
    """
User: I made some purchases and then noticed that my card has been used multiple times on a super site I've never heard of.
Assistant: If you believe your account has been compromised and there are unauthorized transactions on it, we can transfer you to our human support to address this concern. Would you like to be transferred?
User: Yes.
Assistant: I've initiated a transfer to our human support. You're first in the queue.
[Session times out, prompt for feedback]
"""
}, {
    "scenario":
    "I asked to cancel my latest order as it was a mistake.",
    "conversations":
    """
User: I asked to cancel my latest order as it was a mistake.
Assistant : I'm sorry to hear that the item doesn't fit your habit. Wait a minite, I have retrieved the latest order information for you. [order_info] Is this the order you want to cancel?
User: Yes. (confirm)
Assistant: According to the policy, you can | can't cancel the order within 1 hours after placing the order. Your order is placed at [ order time ] and the current time is yyyy-mm-dd hh:mm:ss (replaced by the system time). So (do conclusion according to the policy). (If the window passed) If you still don't want the item, you can choose to refund it.(Here is the refund policy)
"""
}, {
    "scenario":
    "misuse of our refund policy",
    "conversations":
    """
User: I want a refund.
Assistant: It appears you're reporting an issue. While we understand not every interaction may go as planned, please be aware that we periodically review accounts for potential misuse of our refund policy. This is to ensure the best shopping experience for the entire Wish community. Would you still like to contact support regarding this issue?
User: Yes.
Assistant: I've initiated a transfer to our human support. You're first in the queue.
"""
}, {
    "scenario":
    "I want to refund my order because I didnt received it yet.",
    "conversations":
    """
User: It still hasn't been shipped today, I want a refund.
Assistant: The system shows the following orders ... (list the info of orders) Which one do you mean?/Do you want to apply for a refund for this order?
User: (Choose one order) 
Assistant: The current order is now located in the ... district of New York, expected to be delivered by ... date. According to the refund policy, if it's not delivered by ... date, you can apply for a refund.
User: I'm very disappointed, I want a refund.
Assistant: We suggest you wait patiently. If it doesn't arrive by ... date, you can apply for a refund at any time. We will process a full refund.
User: I want an immediate refund.
Assistant: I can transfer you to a human representative to address your concerns. Would you like to speak to a human representative now?
User: Yes, please transfer me to a human representative.
Assistant: I have transferred you to a human representative. There's 1 person ahead of you in the queue. ]
"""
}, {
    "scenario":
    "I'm so angry, disappointed, and frustrated. ",
    "conversations":
    "🥹I feel so sorry to hear that. I will try my best to help you. What can I do for you?"
}, {
    "scenario": "I want to know what is ...?",
    "conversations": "Ok, let me search the information for you.♥️"
}, {
    "scenario": "I want to ...",
    "conversations": "I'm hornered to help you."
}, {
    "scenario":
    "review accounts for potential misuse of our refund policy.",
    "conversations":
    """
User: I want a refund.
Assistant: It appears you're reporting an issue. While we understand not every interaction may go as planned, please be aware that we periodically review accounts for potential misuse of our refund policy. This is to ensure the best shopping experience for the entire Wish community. Would you still like to contact support regarding this issue?
User: Yes.
Assistant: I've initiated a transfer to our human support. You're first in the queue.
[Session times out, prompt for feedback]
"""
}, {
    "scenario":
    " I have to wait another 4 days. This is unacceptable. Timeframes should be adhered to and not changed.",
    "conversations":
    """
User: The delivery date was ... I was informed today when I logged in that I have to wait another 4 days. This is unacceptable. Timeframes should be adhered to and not changed.
Assistant: Our system shows the following order with order number... Is this the order you're referring to?
User: Yes.
Assistant: The current order is located in XX district of New York and is expected to be delivered by XXX date. I understand that the projected delivery time might be longer than initially expected. Our estimated delivery date range is calculated based on the shop's processing time, the location of the item's dispatch, the delivery destination, and past delivery dates we've had from other customers in your area. External factors, such as current events or carrier delays, may affect the actual arrival date of your item. The good news is that you are always covered by our refund guarantee. If your item does not arrive before the refund eligibility date (X month, 2023), please inform us, and we will refund the full amount. 
[Session times out, prompt for feedback]
"""
}]