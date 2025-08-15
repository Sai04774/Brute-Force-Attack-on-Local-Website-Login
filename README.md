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

#### 1. Open your Kali Linux terminal and run the following commands:
```
git clone https://github.com/Sai04774/Brute-Force-Login-Enumeration.git
cd Brute-Force-Login-Enumeration
python app.py
```

<img width="655" height="440" alt="Screenshot 2025-08-16 002720" src="https://github.com/user-attachments/assets/3da031d5-f815-45b8-b23d-5c8aacda3c77" />

#### 2. Start Burp Suite and Configure Browser.
- Open Burp Suite and set up the browser to use Burp as a proxy.
- Paste the Target URL in the Browser.

<img width="1706" height="957" alt="Screenshot 2025-08-14 115952" src="https://github.com/user-attachments/assets/38cc43f0-bc45-4dd0-928c-4260e5eacbae" />

![Screenshot 2025-08-14 132416](https://github.com/user-attachments/assets/ed6c4eba-3de3-4ca4-af22-eea54d33f928)

#### 3. Make sure the intercept is on in Burp Suite and use any credentials to post a request.
- Burp Suite will capture the HTTP request sent when you attempt to log in.

<img width="1646" height="922" alt="Screenshot 2025-08-14 120316" src="https://github.com/user-attachments/assets/f9011fda-0428-410b-9f3c-d281fd14c612" />

#### 4. Send Request to Intruder.
-  Right-click the captured login request and select “Send to Intruder” for brute-force testing.

<img width="1650" height="927" alt="Screenshot 2025-08-14 120950" src="https://github.com/user-attachments/assets/ec7cbc06-a23d-4751-8b5e-93a9f33466cc" />

#### 5. Configure Payload Positions.
- Mark the username and/or password fields as payload positions where Burp Suite will try multiple values.

<img width="289" height="48" alt="Screenshot 2025-08-16 003648" src="https://github.com/user-attachments/assets/9618e51b-cacd-4193-9f79-a68201c32816" />

#### 6. Load Username/Password Lists.
- Using the username.txt and password.txt file included in the repository, add the list of common usernames and passwords to the Intruder payload. 

<img width="1487" height="439" alt="Screenshot 2025-08-14 125004" src="https://github.com/user-attachments/assets/44773611-b6e8-4b4d-85fb-2c40184b629c" />

<img width="1476" height="440" alt="Screenshot 2025-08-14 124828" src="https://github.com/user-attachments/assets/93619a0b-6403-4ceb-8304-c2959ce405b6" />


#### 7. Start the Attack.
- Launch the Intruder attack to systematically test combinations.
- Observe the response codes or lengths to identify the correct credentials.
- Notice that one response differs (e.g., a different status code or content length) from the others. This indicates the valid admin username and password.

<img width="1481" height="847" alt="Screenshot 2025-08-16 002251" src="https://github.com/user-attachments/assets/0e48b745-d2cb-4006-8245-7f4cfd3ea360" />

#### 8. Determine Credentials. 
- Now we come to know the password and username for the admin (because of the status codes) and thus we login in to the admin panel using these credentials.

<img width="1236" height="20" alt="Screenshot 2025-08-16 005650" src="https://github.com/user-attachments/assets/a01ebf6d-8f01-4ddb-a438-d961db8e7683" />

#### 9. Access the Admin Panel.
-After logging in, you will be redirected to the front page. There, click on the “Admin Panel” button to enter the restricted admin area of the demo website.

![Screenshot 2025-08-14 134008](https://github.com/user-attachments/assets/7790a5a1-185d-488e-80ba-1a88855025aa)












