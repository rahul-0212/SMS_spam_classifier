import pandas as pd
import random

print("="*80)
print("EXPANDING SMS SPAM DATASET TO 10,000+ MESSAGES")
print("="*80)

# Load existing dataset
print("\n[1/3] Loading existing dataset...")
df = pd.read_csv('spam_dataset.csv')
print(f"[OK] Current dataset size: {len(df)} messages")

# Generate more spam variations
print("\n[2/3] Generating additional spam variations...")

# Templates for spam generation
spam_templates = {
    'betting': [
        "Bet on {sport} and win {amount}! Register at {website}",
        "{sport} betting - get {bonus}% bonus! Join {website}",
        "Place bets on {sport}! Minimum deposit {amount}. WhatsApp {phone}",
        "Win {amount} in {sport} betting! Play now at {website}",
        "URGENT: {sport} betting bonus {amount}! Claim at {website}",
    ],
    'lottery': [
        "CONGRATULATIONS! You won {amount} in {company} lottery! Call {phone}",
        "Your number won {amount}! Claim at {website}",
        "{company} lottery winner! Prize: {amount}. Contact {phone}",
        "Lucky draw winner! You won {amount}! Verify at {website}",
        "You are selected for {amount} prize! WhatsApp {phone}",
    ],
    'whatsapp': [
        "WhatsApp {phone} to claim your prize of {amount}!",
        "Join WhatsApp group for daily income {amount}! Message {phone}",
        "Work from home - earn {amount} per month! WhatsApp {phone}",
        "WhatsApp {phone} for {job} - earn {amount}/month",
        "Add me on WhatsApp {phone} to receive your {prize}",
    ],
    'bank': [
        "URGENT: Your {bank} account will be blocked! Verify at {website}",
        "{bank} Alert: Suspicious activity. Click {website} to secure account",
        "{bank}: Your account is locked. Update KYC at {website}",
        "{bank}: Your {card} will expire. Renew at {website}",
        "{bank} Alert: Unusual transaction. Verify at {website}",
    ],
    'phishing': [
        "Your {service} is blocked! Update at {website} immediately",
        "{service} verification required! Update at {website} within 48 hours",
        "{service} refund of {amount} pending! Claim at {website}",
        "Your {service} will be suspended! Verify at {website}",
        "{service} KYC pending! Complete at {website} to avoid block",
    ],
    'loan': [
        "{loan_type} loan approved! Get {amount} instantly. Apply at {website}",
        "Pre-approved loan of {amount}! No documents. Call {phone}",
        "{loan_type} loan at {rate}% interest! Apply at {website}",
        "Instant loan - get {amount} in 1 hour! Apply at {website}",
        "{loan_type} loan - get {amount} in 24 hours. WhatsApp {phone}",
    ],
    'job': [
        "Work from home - earn {amount} monthly! Register at {website}",
        "{job} jobs - earn {amount} daily! Join at {website}",
        "Part time {job} - earn {amount} monthly! Apply at {website}",
        "{job} jobs - earn {amount} per day! Register at {website}",
        "Online {job} - earn {amount} weekly! Join at {website}",
    ],
    'product': [
        "{product} at {discount}% discount! Buy now at {website}",
        "{product} for {amount} only! Limited stock at {website}",
        "{product} at {discount}% off! Hurry, buy at {website}",
        "{product} sale - {discount}% discount! Order at {website}",
        "{product} for {amount}! Limited time at {website}",
    ],
}

# Data for templates
sports = ['cricket', 'football', 'IPL', 'kabaddi', 'tennis', 'horse racing', 'basketball']
amounts = ['5 lakh', '10 lakh', '25 lakh', '50 lakh', '1 crore', '2 crore', '5 crore', '10 crore', '5000 Rs', '10000 Rs', '50000 Rs', '1 lakh']
companies = ['Airtel', 'Jio', 'Vi', 'BSNL', 'KBC', 'TATA', 'Reliance', 'Government', 'National']
phones = ['+919876543210', '+918765432109', '+919988776655', '+447310399942', '+447890123456', '+919123456789', '+918899776655']
websites = ['bet365.in', 'betking.com', 'lottery.in', 'winner.com', 'prize.in', 'claim.com', 'verify.in', 'secure.com', 'kyc.in', 'update.com']
banks = ['SBI', 'HDFC', 'ICICI', 'Axis', 'PNB', 'Kotak', 'Yes Bank', 'IDBI', 'Union Bank', 'Canara Bank']
services = ['Aadhaar', 'PAN card', 'Passport', 'Driving license', 'Voter ID', 'Amazon', 'Flipkart', 'PayTM', 'Google Pay', 'PhonePe']
loan_types = ['Personal', 'Home', 'Education', 'Business', 'Gold', 'Vehicle', 'Credit card']
jobs = ['data entry', 'survey', 'typing', 'form filling', 'ad posting', 'email reading', 'SMS sending', 'captcha solving']
products = ['iPhone 14', 'Samsung Galaxy', 'MacBook', 'iPad', 'AirPods', 'Smart TV', 'Laptop', 'Watch', 'Shoes', 'Perfume']
discounts = ['50', '60', '70', '80', '90']
rates = ['5', '6', '7', '8']
bonuses = ['100', '200', '300']
cards = ['debit card', 'credit card', 'ATM card']
prizes = ['lottery prize', 'cash prize', 'KBC prize', 'lucky draw prize']

# Generate spam messages
generated_spam = []

for category, templates in spam_templates.items():
    for _ in range(500):  # Generate 500 messages per category
        template = random.choice(templates)
        message = template.format(
            sport=random.choice(sports),
            amount=random.choice(amounts),
            company=random.choice(companies),
            phone=random.choice(phones),
            website=random.choice(websites),
            bank=random.choice(banks),
            service=random.choice(services),
            loan_type=random.choice(loan_types),
            job=random.choice(jobs),
            product=random.choice(products),
            discount=random.choice(discounts),
            rate=random.choice(rates),
            bonus=random.choice(bonuses),
            card=random.choice(cards),
            prize=random.choice(prizes)
        )
        generated_spam.append(message)

print(f"[OK] Generated {len(generated_spam)} spam messages from templates")

# Generate more ham variations
ham_templates = [
    "Hey, {greeting}",
    "Can we meet {time}?",
    "Thanks for {action}!",
    "I'll be {status}",
    "Did you {action}?",
    "Let me know when you're {status}",
    "{greeting}! Have a great day",
    "I'm {status}, will reach soon",
    "Can you {action}?",
    "Let's {action} together",
    "I'll call you {time}",
    "See you {location}",
    "I'm working {location} today",
    "I'll be there {time}",
    "How was your {event}?",
    "Let's catch up {time}",
    "I'm feeling {emotion} now",
    "Thanks for the {item}",
    "I'll send you the {item}",
    "Can we reschedule {event}?",
    "I'm on my way to {location}",
    "Let me check and {action}",
    "I'll be available {time}",
    "Thanks for {action}",
    "I'll keep you {action}",
    "How is your {item} doing?",
    "I'm excited about the {item}",
    "Let's discuss this {time}",
    "I'll review the {item} tonight",
    "Can you confirm the {item}?",
    "I'm looking forward to {event}",
    "Thanks for {action}",
    "I'll make the {item}",
    "How is the {item} going?",
    "I'm sorry for the {item}",
    "Let me think about {item}",
    "I'll get the {item} for you",
    "Thanks for your {item}",
    "I'm available {time}",
    "Can we postpone until {time}?",
    "I'll send you the {item}",
    "How are you feeling {time}?",
    "I'm working on {item} right now",
    "Thanks for the {item}",
    "I'll let you know {time}",
]

greetings = ['how are you', 'what\'s up', 'good morning', 'good evening', 'hi there']
times = ['tomorrow', 'today', 'this evening', 'next week', 'in the morning', 'after lunch', 'at 5pm']
actions = ['your help', 'the update', 'checking in', 'understanding', 'waiting', 'calling', 'sending', 'reviewing']
statuses = ['free', 'busy', 'late', 'ready', 'available', 'stuck in traffic', 'on my way']
locations = ['at the office', 'from home', 'at the meeting', 'at home', 'downtown']
events = ['weekend', 'vacation', 'meeting', 'presentation', 'interview', 'trip']
emotions = ['much better', 'great', 'tired', 'excited', 'happy', 'good']
items = ['report', 'document', 'details', 'information', 'files', 'link', 'address', 'reservation', 'project', 'family', 'support', 'feedback']

generated_ham = []

for _ in range(4000):  # Generate 4000 ham messages
    template = random.choice(ham_templates)
    message = template.format(
        greeting=random.choice(greetings),
        time=random.choice(times),
        action=random.choice(actions),
        status=random.choice(statuses),
        location=random.choice(locations),
        event=random.choice(events),
        emotion=random.choice(emotions),
        item=random.choice(items)
    )
    generated_ham.append(message)

print(f"[OK] Generated {len(generated_ham)} ham messages from templates")

# Create dataframes
spam_df = pd.DataFrame({
    'label': ['spam'] * len(generated_spam),
    'message': generated_spam
})

ham_df = pd.DataFrame({
    'label': ['ham'] * len(generated_ham),
    'message': generated_ham
})

# Combine with existing dataset
print("\n[3/3] Combining all datasets...")
final_df = pd.concat([df, spam_df, ham_df], ignore_index=True)

# Remove duplicates
final_df = final_df.drop_duplicates(subset=['message'], keep='first')

# Shuffle
final_df = final_df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"[OK] Final dataset size: {len(final_df)} messages")
print(f"  - Spam: {len(final_df[final_df['label']=='spam'])} ({len(final_df[final_df['label']=='spam'])/len(final_df)*100:.1f}%)")
print(f"  - Ham: {len(final_df[final_df['label']=='ham'])} ({len(final_df[final_df['label']=='ham'])/len(final_df)*100:.1f}%)")

# Save to CSV
final_df.to_csv('spam_dataset.csv', index=False)
print(f"\n[OK] Dataset saved as spam_dataset.csv")

print("\n" + "="*80)
print("DATASET EXPANSION COMPLETE")
print("="*80)
print(f"\nFinal statistics:")
print(f"  Total messages: {len(final_df)}")
print(f"  Spam messages: {len(final_df[final_df['label']=='spam'])}")
print(f"  Ham messages: {len(final_df[final_df['label']=='ham'])}")
print(f"  Spam percentage: {len(final_df[final_df['label']=='spam'])/len(final_df)*100:.1f}%")
print("="*80)
