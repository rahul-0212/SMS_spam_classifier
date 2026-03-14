import pandas as pd
import random

print("="*80)
print("SMS SPAM DATASET PREPARATION")
print("="*80)

# Step 1: Load the real SMS Spam Collection dataset
print("\n[1/4] Loading SMS Spam Collection dataset...")
df = pd.read_csv('SMSSpamCollection', sep='\t', header=None, names=['label', 'message'])
print(f"[OK] Loaded {len(df)} messages from SMS Spam Collection")
print(f"  - Spam: {len(df[df['label']=='spam'])} ({len(df[df['label']=='spam'])/len(df)*100:.1f}%)")
print(f"  - Ham: {len(df[df['label']=='ham'])} ({len(df[df['label']=='ham'])/len(df)*100:.1f}%)")

# Step 2: Generate additional realistic spam messages
print("\n[2/4] Generating additional realistic spam messages...")

# Additional spam messages - betting, lottery, WhatsApp scams, bank alerts, phishing
additional_spam = [
    # Betting & Gambling
    "Bet now on IPL and win 10 lakh rupees! Register at bet365india.com",
    "Place your bets on cricket match today! Minimum deposit 500 Rs. WhatsApp +919876543210",
    "URGENT: Your betting account has 5000 bonus! Claim now at betking.in",
    "Win 1 crore in online casino! Play now: casinoindia.com/play",
    "Bet on football and get 200% bonus! Join now: sportbet.co.in",
    "IPL betting tips - guaranteed wins! Call +917890123456",
    "Deposit 1000 and get 5000 free betting credits! Limited time offer",
    "Online poker tournament - prize pool 50 lakhs! Register: pokerindia.net",
    "Bet on horse racing and win big! Minimum bet 100 Rs only",
    "Cricket betting odds - India vs Pakistan! WhatsApp +918765432109",
    "Roulette online - win up to 10 crore! Play now at rouletteindia.com",
    "Sports betting app - get 1000 Rs signup bonus! Download now",
    "Bet on kabaddi league and win! Deposit via UPI: betmaster.in",
    "Online betting site - 100% safe and secure! Register: safebets.co.in",
    "Win money on every cricket match! Join betting group: +919988776655",
    
    # Lottery & Prize Scams
    "CONGRATULATIONS! You won 25 lakh in KBC lottery! Call 1800-XXX-XXXX to claim",
    "Your mobile number won 10 crore in Kaun Banega Crorepati! Claim at kbc-winner.com",
    "Airtel lottery winner! You won 5 lakh rupees. Contact +919123456789",
    "Government lottery - you are selected! Prize: 15 lakh. Verify at lottery.gov.in",
    "Jio lucky draw winner! You won iPhone 14 Pro + 2 lakh cash! Claim now",
    "BSNL lottery department: You won 8 lakh rupees! Send details to claim",
    "Vodafone Idea lottery - you won 12 lakh! Call +918899776655 immediately",
    "National lottery commission: Your ticket won 20 lakh! Claim within 24 hours",
    "You are the lucky winner of 50 lakh rupees! Pay 5000 processing fee to claim",
    "Congratulations! You won 1 crore in lucky draw! WhatsApp +447310399942",
    "Your email won 30 lakh in international lottery! Claim at lottowin.com",
    "TATA lottery winner! You won Tata Nexon car + 10 lakh cash! Verify now",
    "Reliance Jio lottery: You won 7 lakh rupees! Send OTP to confirm",
    "Government of India lottery - you won 18 lakh! Pay 2000 tax to release funds",
    "Lucky draw winner! You won 40 lakh rupees! Contact lottery.office@gmail.com",
    
    # WhatsApp Scams
    "WhatsApp +447310399942 to claim your prize of 5 lakh rupees!",
    "Join WhatsApp group for daily income 5000 Rs! Message +919876543210",
    "Work from home - earn 50000 per month! WhatsApp +918765432109 for details",
    "WhatsApp part time job - earn 3000 daily! Contact +919988776655",
    "Add me on WhatsApp +447890123456 to receive your lottery prize",
    "WhatsApp business opportunity - invest 10000 earn 1 lakh! +919123456789",
    "Join our WhatsApp group for free betting tips! Message +918899776655",
    "WhatsApp +447310399942 for online data entry jobs - earn 40000/month",
    "Send WhatsApp message to +919876543210 to activate your prize money",
    "WhatsApp investment scheme - double your money in 30 days! +918765432109",
    "Join WhatsApp lottery group - win daily prizes! Contact +919988776655",
    "WhatsApp +447890123456 to claim your KBC prize of 25 lakh",
    "Work from home via WhatsApp - earn 2000 per day! Message +919123456789",
    "WhatsApp trading tips - guaranteed profits! Join now: +918899776655",
    "Add WhatsApp +447310399942 for part-time job earning 60000/month",
    
    # Bank Alerts & Phishing
    "URGENT: Your bank account will be blocked! Verify now at sbi-verify.com",
    "SBI Alert: Suspicious activity detected. Click here to secure account immediately",
    "HDFC Bank: Your account is temporarily locked. Update KYC at hdfc-kyc.in",
    "ICICI Bank: Your debit card will expire. Renew at icici-renewal.com",
    "Axis Bank Alert: Unusual transaction detected. Verify at axisbank-secure.net",
    "Your PNB account shows suspicious login. Reset password at pnb-reset.in",
    "Bank of Baroda: Your account will be closed. Update details at bob-update.com",
    "Kotak Mahindra: Your credit card is blocked. Unblock at kotak-unblock.in",
    "Yes Bank Alert: Verify your account within 24 hours at yesbank-verify.com",
    "IDBI Bank: Your account is under review. Submit documents at idbi-kyc.net",
    "Union Bank: Your debit card is blocked. Activate at unionbank-activate.in",
    "Canara Bank Alert: Update your mobile number at canarabank-update.com",
    "Indian Bank: Your account will be suspended. Verify at indianbank-verify.in",
    "Central Bank: Unusual activity detected. Secure account at centralbank.net",
    "State Bank Alert: Your account needs verification at sbi-secure.co.in",
    
    # Phishing & Scams
    "Your Aadhaar card is blocked! Update at aadhaar-update.in immediately",
    "PAN card verification required! Update at pan-verify.com within 48 hours",
    "Income tax refund of 15000 Rs pending! Claim at incometax-refund.in",
    "Your electricity bill is overdue! Pay now at electricity-payment.com to avoid disconnection",
    "LPG subsidy of 5000 Rs credited! Claim at lpg-subsidy.gov.in",
    "Your passport application is rejected! Reapply at passport-india.net",
    "Driving license renewal required! Renew at dl-renewal.in before expiry",
    "Your voter ID is invalid! Update at voterid-update.gov.in",
    "GST registration expired! Renew at gst-renewal.com immediately",
    "Your insurance policy will lapse! Renew at insurance-renew.in",
    "Credit score check - free report! Get at creditscore-india.com",
    "Your Amazon account is suspended! Verify at amazon-verify.in",
    "Flipkart lucky draw winner! Claim 50000 Rs at flipkart-winner.com",
    "PayTM KYC pending! Complete at paytm-kyc.in to avoid account block",
    "Google Pay verification required! Update at gpay-verify.com",
    "PhonePe account locked! Unlock at phonepe-unlock.in immediately",
    "Your Swiggy account has 500 Rs cashback! Claim at swiggy-offer.com",
    "Zomato gold membership free! Register at zomato-gold.in",
    "Netflix subscription expired! Renew at netflix-renew.in",
    "Hotstar premium free for 1 year! Claim at hotstar-free.com",
    
    # Money & Investment Scams
    "Invest 10000 and earn 50000 in 30 days! Guaranteed returns! Call now",
    "Stock market tips - 100% accurate! Subscribe for 5000 Rs only",
    "Cryptocurrency investment - double your money! Invest at crypto-india.net",
    "Real estate investment - 200% returns in 6 months! WhatsApp +919876543210",
    "Gold investment scheme - earn 15% monthly! Invest now at gold-invest.in",
    "Mutual fund investment - guaranteed 30% returns! Call +918765432109",
    "Binary options trading - earn 1 lakh daily! Register at binary-trade.com",
    "Forex trading course - become millionaire in 1 year! Enroll now",
    "Ponzi scheme - invest 50000 earn 5 lakh! Limited slots available",
    "MLM business opportunity - earn unlimited income! Join at mlm-india.com",
    "Chit fund investment - high returns guaranteed! Invest +919988776655",
    "Share market tips - 90% accuracy! Subscribe for 10000 Rs",
    "Commodity trading - earn 2 lakh monthly! Join at commodity-trade.in",
    "Insurance investment - tax free returns! Invest at insurance-invest.com",
    "Fixed deposit - 20% interest rate! Invest at fd-high-returns.in",
    
    # Loan & Credit Scams
    "Personal loan approved! Get 5 lakh instantly. Apply at quickloan.in",
    "Pre-approved loan of 10 lakh! No documents required. Call +919123456789",
    "Home loan at 5% interest! Apply now at homeloan-india.com",
    "Education loan without collateral! Get 20 lakh at edu-loan.in",
    "Business loan approved! Get 50 lakh in 24 hours. WhatsApp +918899776655",
    "Credit card pre-approved! Limit 2 lakh. Apply at creditcard-instant.com",
    "Gold loan at lowest interest! Get cash in 10 minutes at goldloan.in",
    "Vehicle loan approved! Buy your dream car. Apply at carloan-easy.com",
    "Instant loan - get 1 lakh in 1 hour! No credit check at instantloan.in",
    "Loan against property - get 1 crore! Apply at property-loan.com",
    "Payday loan - get 50000 today! Repay next month at payday-loan.in",
    "Debt consolidation loan - clear all debts! Apply at debt-free.com",
    "Loan for bad credit - get 3 lakh! No rejection at badcredit-loan.in",
    "Emergency loan - get money in 30 minutes! Apply at emergency-cash.com",
    "Loan without income proof - get 2 lakh! Apply at noincome-loan.in",
    
    # Job & Work From Home Scams
    "Work from home - earn 50000 monthly! No investment. Register at wfh-jobs.in",
    "Data entry jobs - earn 3000 daily! Join at dataentry-india.com",
    "Online survey jobs - earn 5000 weekly! Register at survey-jobs.in",
    "Part time jobs - earn 40000 monthly! Apply at parttime-work.com",
    "Copy paste jobs - earn 2000 daily! Join at copypaste-jobs.in",
    "Form filling jobs - earn 30000 monthly! Register at formfilling.com",
    "Ad posting jobs - earn 4000 daily! Join at adposting-jobs.in",
    "Email reading jobs - earn 1000 per email! Register at email-jobs.com",
    "SMS sending jobs - earn 2500 daily! Join at sms-jobs.in",
    "Captcha solving jobs - earn 20000 monthly! Register at captcha-work.com",
    "Online typing jobs - earn 35000 monthly! Join at typing-jobs.in",
    "Mobile recharge business - earn 60000 monthly! Register at recharge-biz.com",
    "Freelance jobs - earn 80000 monthly! Join at freelance-india.in",
    "Content writing jobs - earn 50000 monthly! Register at content-jobs.com",
    "Translation jobs - earn 70000 monthly! Join at translation-work.in",
    
    # Product & Service Scams
    "iPhone 14 Pro at 50% discount! Buy now at iphone-sale.in",
    "Samsung Galaxy S23 for 15000 Rs only! Limited stock at samsung-offer.com",
    "MacBook Air at 30000 Rs! Hurry, buy at macbook-sale.in",
    "Sony PlayStation 5 for 20000 Rs! Order at ps5-india.com",
    "Apple Watch Series 8 for 10000 Rs! Buy at applewatch-sale.in",
    "iPad Pro at 70% off! Limited time offer at ipad-discount.com",
    "AirPods Pro for 5000 Rs only! Buy at airpods-sale.in",
    "Canon DSLR camera at 50% off! Order at camera-discount.com",
    "Smart TV 55 inch for 15000 Rs! Buy at tv-sale.in",
    "Laptop at 80% discount! Limited stock at laptop-offer.com",
    "Branded shoes at 90% off! Shop at shoes-discount.in",
    "Designer clothes at throwaway prices! Buy at fashion-sale.com",
    "Perfumes at 70% discount! Order at perfume-sale.in",
    "Watches at 80% off! Limited time at watch-discount.com",
    "Sunglasses at 60% discount! Buy at sunglass-sale.in",
    
    # Health & Medicine Scams
    "Weight loss pills - lose 10 kg in 10 days! Order at weightloss-india.com",
    "Hair regrowth treatment - 100% guaranteed! Buy at hairgrowth.in",
    "Height increase medicine - grow 6 inches! Order at height-increase.com",
    "Diabetes cure - permanent solution! Buy at diabetes-cure.in",
    "Cancer treatment - herbal medicine! Order at cancer-cure.com",
    "Blood pressure control - natural remedy! Buy at bp-control.in",
    "Cholesterol reduction - guaranteed results! Order at cholesterol-cure.com",
    "Kidney stone removal - without surgery! Buy at kidney-cure.in",
    "Liver detox - cleanse in 7 days! Order at liver-detox.com",
    "Heart disease cure - natural treatment! Buy at heart-cure.in",
    "Arthritis pain relief - instant results! Order at arthritis-cure.com",
    "Asthma cure - permanent solution! Buy at asthma-cure.in",
    "Skin whitening cream - fair in 7 days! Order at fairness-cream.com",
    "Anti-aging cream - look 20 years younger! Buy at anti-aging.in",
    "Memory booster pills - improve IQ! Order at memory-pills.com",
    
    # Airtel/Jio/Vi specific spam
    "Airtel Warning: SPAM | Deposit now and win 1 cr at airtel-lottery.com",
    "Jio offer: Get 1 year free recharge! Claim at jio-free.in",
    "Vi lottery winner! You won 15 lakh rupees. Verify at vi-winner.com",
    "Airtel KYC update required! Update at airtel-kyc.in within 24 hours",
    "Jio SIM will be blocked! Recharge now at jio-recharge.com",
    "Vi account suspended! Activate at vi-activate.in immediately",
    "Airtel bill payment overdue! Pay at airtel-payment.com to avoid disconnection",
    "Jio Prime membership expired! Renew at jio-prime.in",
    "Vi postpaid bill pending! Pay at vi-payment.com",
    "Airtel 5G upgrade free! Register at airtel-5g.in",
    
    # International scams
    "UK visa lottery - you are selected! Apply at uk-visa-lottery.com",
    "US green card lottery winner! Claim at usa-greencard.com",
    "Canada PR visa - guaranteed approval! Apply at canada-pr.in",
    "Australia work visa - get job! Apply at australia-visa.com",
    "Dubai job offer - salary 50000 AED! Apply at dubai-jobs.in",
    "Singapore work permit - guaranteed! Apply at singapore-visa.com",
    "Germany job visa - high salary! Apply at germany-jobs.in",
    "UK work permit - earn in pounds! Apply at uk-workpermit.com",
    "New Zealand PR visa - easy process! Apply at nz-visa.in",
    "Ireland work visa - guaranteed job! Apply at ireland-jobs.com",
]

# Additional ham messages for balance
additional_ham = [
    "Hey, how are you doing today?",
    "Can we meet tomorrow at 5pm?",
    "Thanks for your help yesterday!",
    "I'll be late for the meeting, sorry",
    "Did you receive my email?",
    "Let me know when you're free",
    "Happy birthday! Have a great day",
    "Congratulations on your promotion!",
    "I'm stuck in traffic, will reach soon",
    "Can you send me the report?",
    "Let's have lunch together tomorrow",
    "I'll call you in the evening",
    "Thanks for the birthday wishes!",
    "See you at the office",
    "I'm working from home today",
    "Can you pick up some groceries?",
    "I'll be there in 10 minutes",
    "How was your weekend?",
    "Let's catch up soon",
    "I'm feeling much better now",
    "Thanks for the recommendation",
    "I'll send you the details",
    "Can we reschedule our meeting?",
    "I'm on my way",
    "Let me check and get back to you",
    "I'll be available after 3pm",
    "Thanks for understanding",
    "I'll keep you posted",
    "How is your family doing?",
    "I'm excited about the project",
    "Let's discuss this tomorrow",
    "I'll review the document tonight",
    "Can you confirm the time?",
    "I'm looking forward to it",
    "Thanks for checking in",
    "I'll make the reservation",
    "How is the project going?",
    "I'm sorry for the delay",
    "Let me think about it",
    "I'll get the information for you",
    "Thanks for your support",
    "I'm available tomorrow afternoon",
    "Can we postpone until next week?",
    "I'll send you the link",
    "How are you feeling today?",
    "I'm working on it right now",
    "Thanks for the feedback",
    "I'll let you know soon",
    "Got it, thanks!",
    "Sounds good to me",
    "No problem at all",
    "Sure thing!",
    "Okay, see you then",
    "That works for me",
    "I understand",
    "Will do",
    "Perfect timing",
    "Good morning!",
    "Have a great day",
    "Take care",
    "Talk to you soon",
    "Miss you!",
    "Good night",
    "Sweet dreams",
    "Hope you're well",
    "Thinking of you",
    "Love you",
    "Drive safely",
    "Enjoy your vacation",
    "Welcome back!",
    "Congratulations!",
    "Best wishes",
    "Good luck!",
    "Well done",
    "Amazing work",
    "Keep it up",
    "You're the best",
    "Thank you so much",
    "I appreciate it",
    "You're welcome",
    "My pleasure",
    "Anytime",
    "Of course",
    "Absolutely",
    "Definitely",
    "For sure",
    "I agree",
    "Makes sense",
    "I see",
    "Got it",
    "Understood",
    "Noted",
    "Okay",
    "Alright",
    "Cool",
    "Great",
    "Awesome",
    "Perfect",
    "Excellent",
    "Wonderful",
    "Fantastic",
    "Brilliant",
    "Superb",
]

# Create additional spam dataframe
spam_df = pd.DataFrame({
    'label': ['spam'] * len(additional_spam),
    'message': additional_spam
})

# Create additional ham dataframe
ham_df = pd.DataFrame({
    'label': ['ham'] * len(additional_ham),
    'message': additional_ham
})

print(f"[OK] Generated {len(additional_spam)} additional spam messages")
print(f"[OK] Generated {len(additional_ham)} additional ham messages")

# Step 3: Combine all datasets
print("\n[3/4] Combining datasets...")
combined_df = pd.concat([df, spam_df, ham_df], ignore_index=True)

# Shuffle the dataset
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)

print(f"[OK] Combined dataset size: {len(combined_df)} messages")
print(f"  - Spam: {len(combined_df[combined_df['label']=='spam'])} ({len(combined_df[combined_df['label']=='spam'])/len(combined_df)*100:.1f}%)")
print(f"  - Ham: {len(combined_df[combined_df['label']=='ham'])} ({len(combined_df[combined_df['label']=='ham'])/len(combined_df)*100:.1f}%)")

# Step 4: Save to CSV
print("\n[4/4] Saving to spam_dataset.csv...")
combined_df.to_csv('spam_dataset.csv', index=False)
print(f"[OK] Dataset saved successfully!")

print("\n" + "="*80)
print("DATASET PREPARATION COMPLETE")
print("="*80)
print(f"\nFinal dataset statistics:")
print(f"  Total messages: {len(combined_df)}")
print(f"  Spam messages: {len(combined_df[combined_df['label']=='spam'])}")
print(f"  Ham messages: {len(combined_df[combined_df['label']=='ham'])}")
print(f"  Spam percentage: {len(combined_df[combined_df['label']=='spam'])/len(combined_df)*100:.1f}%")
print(f"\nDataset saved as: spam_dataset.csv")
print("="*80)
