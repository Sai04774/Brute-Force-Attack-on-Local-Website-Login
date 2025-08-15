# Brute-Force-Login-Enumeration

## Description 
- Vihasa Education is a sample and demo website created for educational purposes, specifically to demonstrate brute-force attack testing.
- The website offers sample courses on Web Development, Python Programming, and Data Science.
- Users can log in using provided credentials to explore course details and videos.
- Since it is a demo site, it does not implement multi-factor authentication (like OTPs or email verification), making it intentionally 
  vulnerable for testing brute-force attacks and security analysis.

## Bruteforce Attack
In this scenario, the attacker attempts to gain access to the website’s administrator panel by systematically trying a list of common usernames and passwords. Using Burp Suite Intruder, the process involves first identifying the correct admin username and then determining the corresponding password. Once successful, the attacker can access the restricted admin page of the demo website.

### Required Tools
1. Python
2. Burp Suite
   
### Brute-force Testing Process

1. Clone this repositroy and start the flaks app.
Open your Kali Linux terminal and run the following commands:
```
git clone https://github.com/Sai04774/Brute-Force-Login-Enumeration.git
cd Brute-Force-Login-Enumeration
python app.py
```
