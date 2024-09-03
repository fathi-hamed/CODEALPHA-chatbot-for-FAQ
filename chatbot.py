import nltk
from nltk.chat.util import Chat, reflections

# JSON data converted to Python list of dictionaries
questions_and_answers = [
    {
        "question": "How can I create an account?",
        "answer": "To create an account, click on the 'Sign Up' button on the top right corner of our website and follow the instructions to complete the registration process."
    },
    {
        "question": "What payment methods do you accept?",
        "answer": "We accept major credit cards, debit cards, and PayPal as payment methods for online orders."
    },
    {
        "question": "How can I track my order?",
        "answer": "You can track your order by logging into your account and navigating to the 'Order History' section. There, you will find the tracking information for your shipment."
    },
    {
        "question": "What is your return policy?",
        "answer": "Our return policy allows you to return products within 30 days of purchase for a full refund, provided they are in their original condition and packaging. Please refer to our Returns page for detailed instructions."
    },
{
  "question": "Do you offer expedited shipping?",
  "answer": "Yes, we offer expedited shipping options for faster delivery. During the checkout process, you can select the desired expedited shipping method."
  },
  {
  "question": "Can I order a product that is out of stock?",
  "answer": "If a product is currently out of stock, you will usually see an option to sign up for product notifications. This way, you will be alerted when the product becomes available again."
  },
  {
  "question": "What is your email newsletter about?",
  "answer": "Our email newsletter provides updates on new product releases, exclusive offers, and helpful tips related to our products. You can subscribe to our newsletter on our website."
  },
  {
  "question": "Can I return a product if I changed my mind?",
  "answer": "Yes, you can return a product if you changed your mind. Please ensure the product is in its original condition and packaging, and refer to our return policy for instructions."
  },
  {
  "question": "Do you offer live chat support?",
  "answer": "Yes, we offer live chat support on our website during our business hours. Look for the chat icon in the bottom right corner to initiate a chat with our customer support team."
  },
  {
  "question": "Can I order a product as a gift?",
  "answer": "Yes, you can order a product as a gift and have it shipped directly to the recipient. During the checkout process, you can enter the recipient's shipping address."
  },
  {
  "question": "What should I do if my discount code is not working?",
  "answer": "If your discount code is not working, please double-check the terms and conditions associated with the code. If the issue persists, contact our customer support team for assistance."
  },
  {
  "question": "Can I return a product if it was a final sale item?",
  "answer": "Final sale items are usually non-returnable and non-refundable. Please review the product description or contact our customer support team to confirm the return eligibility for specific items."
  },
  {
  "question": "Do you offer installation services for your products?",
  "answer": "Installation services are available for select products. Please check the product description or contact our customer support team for more information and to request installation services."
  },
  {
  "question": "Can I order a product that is discontinued?",
  "answer": "Discontinued products are no longer available for purchase. We recommend exploring alternative products on our website."
  },
  {
  "question": "Can I return a product without a receipt?",
  "answer": "A receipt or proof of purchase is usually required for returns. Please refer to our return policy or contact our customer support team for assistance."
  },
  {
  "question": "Can I order a product for delivery to a different country?",
  "answer": "Yes, we offer international shipping to select countries. Please review the available shipping destinations during checkout or contact our customer support for assistance."
  },
  {
  "question": "Can I add a gift message to my order?",
  "answer": "Yes, you can add a gift message during the checkout process. There is usually a section where you can enter your personalized message."
  },
  {
  "question": "Can I request a product demonstration before making a purchase?",
  "answer": "We do not currently offer product demonstrations before purchase. However, you can find detailed product descriptions, specifications, and customer reviews on our website."
  },
  {
  "question": "Can I order a product that is listed as 'coming soon'?",
  "answer": "Products listed as 'coming soon' are not available for immediate purchase. Please sign up for notifications to be informed when the product becomes available."
  },
  {
  "question": "Can I request an invoice for my order?",
  "answer": "Yes, an invoice is usually included with your order. If you require a separate invoice, please contact our customer support team with your order details."
  },
  {
  "question": "Can I order a product that is labeled as 'limited edition'?",
  "answer": "'Limited edition' products may have restricted availability. We recommend placing an order as soon as possible to secure your item."
  },
  {
  "question": "Can I return a product if I no longer have the original packaging?",
  "answer": "While returning a product in its original packaging is preferred, you can still initiate a return without it. Contact our customer support team for guidance in such cases."
  },
  {
  "question": "Can I request a product that is currently out of stock to be reserved for me?",
  "answer": "We do not offer reservations for out-of-stock products. However, you can sign up for product notifications to be alerted when it becomes available again."
  },
  {
  "question": "Can I order a product that is listed as 'pre-order' with other in-stock items?",
  "answer": "Yes, you can place an order with a mix of pre-order and in-stock items. However, please note that the entire order will be shipped once all items are available."
  },
  {
  "question": "Can I return a product if it was damaged during shipping?",
  "answer": "If your product was damaged during shipping, please contact our customer support team immediately. We will guide you through the return and replacement process."
  },
  {
  "question": "Can I request a product that is out of stock to be restocked?",
  "answer": "We strive to restock popular products whenever possible. Please sign up for product notifications to be informed when the item becomes available again."
  },
  {
  "question": "Can I order a product if it is listed as 'backordered'?",
  "answer": "Products listed as 'backordered' are temporarily out of stock but can still be ordered. Your order will be fulfilled once the product is restocked."
  },
  {
  "question": "Can I return a product if it was purchased during a sale or with a discount?",
  "answer": "Yes, you can return a product purchased during a sale or with a discount. The refund will be processed based on the amount paid after the discount."
  },
  {
  "question": "Can I request a product repair or replacement if it is damaged?",
  "answer": "If you receive a damaged product, please contact our customer support team immediately. We will assist you with the necessary steps for repair or replacement."
  },
  {
  "question": "Can I order a product if it is listed as 'out of stock' but available for pre-order?",
  "answer": "If a product is available for pre-order, you can place an order to secure your item. The product will be shipped once it becomes available."
  },
  {
  "question": "Can I return a product if it was purchased as a gift?",
  "answer": "Yes, you can return a product purchased as a gift. However, refunds will typically be issued to the original payment method used for the purchase."
  },
  {
  "question": "Can I request a product if it is listed as 'discontinued'?",
  "answer": "Unfortunately, if a product is listed as 'discontinued,' it is no longer available for purchase. We recommend exploring alternative products on our website."
  },
  {
  "question": "Can I order a product if it is listed as 'sold out'?",
  "answer": "If a product is listed as 'sold out,' it is currently unavailable for purchase. Please check back later or sign up for notifications when it becomes available again."
  },
  {
  "question": "Can I return a product if it was purchased with a gift card?",
  "answer": "Yes, you can return a product purchased with a gift card. The refund will be issued in the form of store credit or a new gift card."
  },
  {
  "question": "Can I request a product if it is not currently available in my size?",
  "answer": "If a product is not available in your size, it may be temporarily out of stock. Please check back later or sign up for size notifications."
  },
  {
  "question": "Can I order a product if it is listed as 'coming soon' but available for pre-order?",
  "answer": "If a product is listed as 'coming soon' and available for pre-order, you can place an order to secure your item before it becomes available."
  },
  {
  "question": "Can I return a product if it was purchased with a discount code?",
  "answer": "Yes, you can return a product purchased with a discount code. The refund will be processed based on the amount paid after the discount."
  },
  {
  "question": "Can I request a custom order or personalized product?",
  "answer": "We do not currently offer custom orders or personalized products. Please explore the available products on our website."
  },
  {
  "question": "Can I order a product if it is listed as 'temporarily unavailable'?",
  "answer": "If a product is listed as 'temporarily unavailable,' it is out of stock but may be restocked in the future. Please check back later or sign up for notifications."
  },
  {
  "question": "Can I return a product if it was damaged due to improper use?",
  "answer": "Our return policy generally covers products that are defective or damaged upon arrival. Damage due to improper use may not be eligible for a return. Please contact our customer support team for assistance."
  },
  {
  "question": "Can I request a product if it is listed as 'coming soon' but not available for pre-order?",
  "answer": "If a product is listed as 'coming soon' but not available for pre-order, you will need to wait until it is officially released and becomes available for purchase."
  },
  {
  "question": "Can I order a product if it is listed as 'on hold'?",
  "answer": "If a product is listed as 'on hold,' it is temporarily unavailable for purchase. Please check back later or sign up for notifications when it becomes available."
  },
  {
  "question": "Can I return a product if I no longer have the original receipt?",
  "answer": "While a receipt is preferred for returns, we may be able to assist you without it. Please contact our customer support team for further guidance."
  },
  {
  "question": "Can I request a product that is listed as 'limited edition' to be restocked?",
  "answer": "Once a limited edition product is sold out, it may not be restocked. Limited edition items are available for a limited time only, so we recommend purchasing them while they are available."
  },
  {
  "question": "Can I order a product if it is listed as 'discontinued' but still visible on the website?",
  "answer": "If a product is listed as 'discontinued' but still visible on the website, it may be an error. Please contact our customer support team for clarification."
  },
  {
  "question": "Can I return a product if it was a clearance or final sale item?",
  "answer": "Clearance or final sale items are typically non-returnable and non-refundable. Please review the product description or contact our customer support team for more information."
  },
  {
  "question": "Can I request a product if it is not listed on your website?",
  "answer": "If a product is not listed on our website, it may not be available for purchase. We recommend exploring the available products or contacting our customer support team for further assistance."
  },
  {
  "question": "Can I order a product if it is listed as 'out of stock' but available for backorder?",
  "answer": "If a product is listed as 'out of stock' but available for backorder, you can place an order to secure your item. The product will be shipped once it becomes available."
  },
  {
  "question": "Can I return a product if it was purchased as part of a bundle or set?",
  "answer": "If a product was purchased as part of a bundle or set, the return policy may vary. Please refer to the specific terms and conditions or contact our customer support team for further guidance."
  },
  {
  "question": "Can I request a product that is listed as 'out of stock' to be restocked?",
  "answer": "We aim to restock popular products whenever possible. Please sign up for product notifications to be alerted when the item becomes available again."
  },
  {
  "question": "Can I order a product if it is listed as 'coming soon' and available for pre-order?",
  "answer": "If a product is listed as 'coming soon' and available for pre-order, you can place an order to secure your item before it becomes available."
  },
  {
  "question": "Can I return a product if it was damaged due to mishandling during shipping?",
  "answer": "If your product was damaged due to mishandling during shipping, please contact our customer support team immediately. We will assist you with the necessary steps for return and replacement."
  },
  {
  "question": "Can I request a product that is listed as 'out of stock' to be reserved for me?",
  "answer": "We do not offer reservations for out-of-stock products. However, you can sign up for product notifications to be alerted when the item becomes available again."
  },
  {
  "question": "Can I order a product if it is listed as 'pre-order' but available for backorder?",
  "answer": "If a product is listed as 'pre-order' and available for backorder, you can place an order to secure your item. The product will be shipped once it becomes available."
  },
  {
  "question": "Can I return a product if it was purchased with store credit?",
  "answer": "Yes, you can return a product purchased with store credit. The refund will be issued in the form of store credit, which you can use for future purchases."
  },
  {
  "question": "Can I request a product that is currently out of stock to be restocked?",
  "answer": "We strive to restock popular products whenever possible. Please sign up for product notifications to be informed when the item becomes available again."
  },
  {
  "question": "Can I order a product if it is listed as 'sold out' but available for pre-order?",
  "answer": "If a product is listed as 'sold out' but available for pre-order, you can place an order to secure your item. The product will be shipped once it becomes available."
  },
  {
  "question": "Can I return a product if it was purchased with a promotional gift card?",
  "answer": "Yes, you can return a product purchased with a promotional gift card. The refund will be issued in the form of store credit or a new gift card."
  },
  {
  "question": "Can I request a product if it is not currently available in my preferred color?",
  "answer": "If a product is not available in your preferred color, it may be temporarily out of stock. Please check back later or sign up for color notifications."
  },
  {
  "question": "Can I order a product if it is listed as 'coming soon' and not available for pre-order?",
  "answer": "If a product is listed as 'coming soon' but not available for pre-order, you will need to wait until it is officially released and becomes available for purchase."
  },
  {
  "question": "Can I return a product if it was purchased during a promotional event?",
  "answer": "Yes, you can return a product purchased during a promotional event. The refund will be processed based on the amount paid after any applicable discounts."
  },
]


# Create pairs from the JSON data
pairs = [(q['question'].lower(), [q['answer']]) for q in questions_and_answers]

# Create a chatbot instance
chatbot = Chat(pairs, reflections)

# Define a function to start the conversation
def start_chat():
    print("Welcome to the Chatbot! Type 'quit' to end the conversation.")
    while True:
        user_input = input("You: ").lower()
        if user_input == 'quit':
            print("Chatbot: Goodbye!")
            break
        else:
            response = chatbot.respond(user_input)
            print("Chatbot:", response)

# Start the conversation
start_chat()
