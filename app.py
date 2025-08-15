from flask import Flask, request, redirect, session, url_for, render_template_string

app = Flask(__name__)
app.secret_key = "vihasa_secret_key"

# Users dictionary
users = {"admin": "admin123"}  # Admin default
# Add more users via signup

# Courses data
courses = [
    {"title": "Web Development", "img": "types-of-web-development-services.jpg", 
     "description": "Learn HTML, CSS, and JavaScript to build responsive websites.", "link": "#"},
    {"title": "Data Science", "img": "what-is-data-science-2.jpg", 
     "description": "Master Python, Pandas, and Machine Learning techniques.", "link": "#"},
    {"title": "Artificial Intelligence", "img": "ai-in-robotics-1.png.webp", 
     "description": "Explore AI algorithms, deep learning, and real-world projects.", "link": "#"}
]

# Contacts data
contacts = [
    {"name": "Neha", "role": "Founder", "img": "IMG_2362.jpg", 
     "phone": "+91 98765 43210", "email": "neha@vihasaeducation.com"},
    {"name": "Vidya Vani", "role": "Co-Founder", "img": "Vidya Vani.png", 
     "phone": "+91 91234 56789", "email": "vidya@vihasaeducation.com"},
    {"name": "Sai Kiran", "role": "CEO", "img": "WhatsApp Image 2024-10-02 at 00.02.27_7f19df37.jpg", 
     "phone": "+91 99887 66554", "email": "saikiran@vihasaeducation.com"}
]

# Login page
login_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VIHASA Login</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css">
<style>
body { background:#121212; color:#fff; display:flex; justify-content:center; align-items:center; height:100vh; font-family:'Segoe UI', sans-serif; }
.login-card { background:#1f1f1f; padding:40px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.9); width:350px; }
.login-card h2 { margin-bottom:25px; color:#00a8ff; text-align:center; }
.form-control { background:#2c2c2c; border:none; color:#eee; }
.form-control::placeholder { color:#888; }
.btn-primary { background:#00a8ff; border:none; width:100%; }
.btn-primary:hover { background:#0077cc; }
.error { color:#ff6b6b; margin-bottom:15px; text-align:center; }
.toggle { text-align:center; margin-top:15px; color:#00a8ff; cursor:pointer; }
.toggle:hover { text-decoration:underline; }
</style>
</head>
<body>
<div class="login-card">
<h2>Sign In</h2>
{% if error %}<div class="error">{{ error }}</div>{% endif %}
<form method="POST">
<input type="text" name="username" class="form-control mb-3" placeholder="Username" required>
<input type="password" name="password" class="form-control mb-3" placeholder="Password" required>
<button type="submit" class="btn btn-primary">Login</button>
</form>
<div class="toggle" onclick="window.location.href='/signup'">Don't have an account? Sign Up</div>
</div>
</body>
</html>
"""

# Signup page
signup_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>VIHASA Sign Up</title>
<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css">
<style>
body { background:#121212; color:#fff; display:flex; justify-content:center; align-items:center; height:100vh; font-family:'Segoe UI', sans-serif; }
.login-card { background:#1f1f1f; padding:40px; border-radius:15px; box-shadow:0 10px 30px rgba(0,0,0,0.9); width:350px; }
.login-card h2 { margin-bottom:25px; color:#00a8ff; text-align:center; }
.form-control { background:#2c2c2c; border:none; color:#eee; }
.form-control::placeholder { color:#888; }
.btn-primary { background:#00a8ff; border:none; width:100%; }
.btn-primary:hover { background:#0077cc; }
.error { color:#ff6b6b; margin-bottom:15px; text-align:center; }
.toggle { text-align:center; margin-top:15px; color:#00a8ff; cursor:pointer; }
.toggle:hover { text-decoration:underline; }
</style>
</head>
<body>
<div class="login-card">
<h2>Sign Up</h2>
{% if error %}<div class="error">{{ error }}</div>{% endif %}
<form method="POST">
<input type="text" name="username" class="form-control mb-3" placeholder="Username" required>
<input type="password" name="password" class="form-control mb-3" placeholder="Password" required>
<button type="submit" class="btn btn-primary">Register</button>
</form>
<div class="toggle" onclick="window.location.href='/'">Already have an account? Login</div>
</div>
</body>
</html>
"""

# VIHASA page template
vihasa_page = """
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8" />
<meta name="viewport" content="width=device-width, initial-scale=1" />
<title>VIHASA Education</title>
<link href="https://cdn.jsdelivr.net/npm/bootstrap@4.5.2/dist/css/bootstrap.min.css" rel="stylesheet"/>
<style>
body { font-family:'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; margin:0; background:#121212; color:#e0e0e0; scroll-behavior:smooth; }
header { background:linear-gradient(90deg,#4b6cb7,#182848); color:white; padding:20px 40px; display:flex; justify-content:space-between; align-items:center; box-shadow:0 3px 6px rgba(0,0,0,0.9); position:sticky; top:0; z-index:1000; }
header h1 { margin:0; font-weight:700; font-size:1.8rem; letter-spacing:2px; }
#logout-btn { background:#ff4757; border:none; color:white; padding:8px 16px; border-radius:25px; font-weight:600; cursor:pointer; transition:background 0.3s ease; }
#logout-btn:hover { background:#e84118; }
nav { background:#1f1f1f; display:flex; justify-content:center; padding:12px 0; box-shadow:0 2px 5px rgba(0,0,0,0.85); position:sticky; top:70px; z-index:999; }
nav a { color:#bbb; margin:0 20px; font-weight:600; text-transform:uppercase; letter-spacing:1px; text-decoration:none; transition:color 0.3s ease; font-size:0.9rem; }
nav a:hover { color:#00a8ff; }
.container { max-width:1200px; margin:40px auto; padding:0 20px; }
section { margin-bottom:60px; padding:40px; border-radius:12px; background:#222222; box-shadow:0 10px 25px rgba(0,0,0,0.9); transition:box-shadow 0.3s ease; color:#ddd; }
section:hover { box-shadow:0 15px 30px rgba(0,0,0,1); }
section h2 { font-weight:700; margin-bottom:25px; border-bottom:3px solid #00a8ff; display:inline-block; padding-bottom:6px; color:#00a8ff; }
section p { color:#ccc; font-size:1.05rem; line-height:1.6; }
.row { margin-top:20px; }
.card { border-radius:15px; overflow:hidden; box-shadow:0 8px 20px rgba(0,0,0,0.5); transition: transform 0.3s ease; background:#1c1c1c; color:#eee; }
.card:hover { transform:translateY(-8px); box-shadow:0 15px 30px rgba(0,0,0,0.8); }
.card img { height:180px; object-fit:cover; border-bottom:3px solid #00a8ff; }
.card-body { padding:20px; }
.btn-primary { background:#00a8ff; border:none; font-weight:600; border-radius:30px; padding:10px 25px; transition:background 0.3s ease; color:#111; }
.btn-primary:hover { background:#0077cc; color:#eee; }
.contact-card { text-align:center; padding:25px 20px; border-radius:15px; background:#282828; box-shadow:0 6px 20px rgba(0,0,0,0.8); transition:background 0.3s ease; height:100%; display:flex; flex-direction:column; align-items:center; color:#eee; }
.contact-card:hover { background:#004d99; color:#fff; }
.contact-card img { width:120px; height:120px; border-radius:50%; margin-bottom:15px; border:3px solid #00a8ff; object-fit:cover; }
.contact-card h5 { font-weight:700; margin-bottom:5px; color:#00a8ff; }
.contact-card p { margin-bottom:4px; font-weight:600; color:#ccc; }
.contact-card a { color:#00a8ff; font-weight:600; text-decoration:none; }
.contact-card a:hover { text-decoration:underline; }
footer { text-align:center; padding:15px; background:#1f1f1f; margin-top:20px; }
@media (max-width:767px){ nav{flex-direction:column;} nav a{margin:10px 0;} header{flex-direction:column;align-items:flex-start;} #logout-btn{margin-top:10px; align-self:flex-end;} }
</style>
</head>
<body>
<header>
<h1>VIHASA Education</h1>
<div>
<form action="{{ url_for('logout') }}" method="get" style="display:inline;">
<button id="logout-btn" type="submit">Logout</button>
</form>
{% if username == 'admin' %}
<button id="admin-login" style="margin-left:20px;" onclick="window.location.href='/admin'">Admin Panel</button>
{% endif %}
</div>
</header>
<nav>
<a href="#home">Home</a>
<a href="#courses">Courses</a>
<a href="#about">About</a>
<a href="#contact">Contact</a>
</nav>
<div class="container">
<h3 id="welcomeUser" style="margin-bottom:30px; color:#00a8ff; font-weight:700; font-size:1.4rem;">
Hello, {{ username }}
</h3>
<section id="home">
<h2>Welcome to VIHASA Education Portal!</h2>
<p>We are dedicated to empowering learners through quality education, expert instructors, and hands-on experience. Explore courses, resources, and tools to grow your skills and career.</p>
</section>
<section id="courses">
<h2>Our Popular Courses</h2>
<div class="row">
{% for course in courses %}
<div class="col-md-4 mb-4">
<div class="card shadow-sm">
<img src="{{ url_for('static', filename='img/' + course.img) }}" alt="{{ course.title }}">
<div class="card-body">
<h5 class="card-title">{{ course.title }}</h5>
<p class="card-text">{{ course.description }}</p>
<a href="{{ course.link }}" class="btn btn-primary">Enroll Now</a>
</div>
</div>
</div>
{% endfor %}
</div>
</section>
<section id="about">
<h2>About VIHASA Education</h2>
<p>VIHASA Education is dedicated to empowering learners through quality education, expert instructors, and hands-on experience. Our mission is to make learning accessible and engaging for everyone.</p>
<p>Founded with the vision to transform education, we continually strive to innovate and provide courses that match industry demands.</p>
</section>
<section id="contact">
<h2>Contact Us</h2>
<div class="row">
{% for contact in contacts %}
<div class="col-md-4 mb-4">
<div class="contact-card">
<img src="{{ url_for('static', filename='img/' + contact.img) }}" alt="{{ contact.name }}">
<h5>{{ contact.name }}</h5>
<p><em>{{ contact.role }} Of Vihasa</em></p>
<p>Phone: {{ contact.phone }}</p>
<p>Email: <a href="mailto:{{ contact.email }}">{{ contact.email }}</a></p>
</div>
</div>
{% endfor %}
</div>
</section>
</div>
<footer>
&copy; 2025 VIHASA Education. All rights reserved.
</footer>
</body>
</html>
"""

# Admin panel with image
admin_page = """
<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1">
<title>Admin Panel</title>
<style>
body { background:#121212; color:#fff; font-family:'Segoe UI',sans-serif; text-align:center; }
.container { margin-top:50px; }
img { width:200px; border-radius:15px; border:3px solid #00a8ff; margin-top:20px; }
a { color:#00a8ff; display:block; margin-top:20px; text-decoration:none; font-weight:bold; }
a:hover { text-decoration:underline; }
</style>
</head>
<body>
<div class="container">
<h2>Welcome Admin!</h2>
<h3 style="color: blue;">Congratulations on successfully completing your project!🎉</h3>
<img src="{{ url_for('static', filename='img/iii.png') }}" alt="Admin Image">
<a href="/vihasa">Back to VIHASA</a>
</div>
</body>
</html>
"""

# Routes
@app.route("/", methods=["GET","POST"])
def login():
    if request.method=="POST":
        username = request.form.get("username").strip()
        password = request.form.get("password").strip()
        if username in users and users[username]==password:
            session["user"]=username
            return redirect(url_for("vihasa"))
        return render_template_string(login_page, error="Invalid username or password!")
    return render_template_string(login_page)

@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method=="POST":
        username=request.form.get("username").strip()
        password=request.form.get("password").strip()
        if username in users:
            return render_template_string(signup_page, error="Username already exists!")
        users[username]=password
        return redirect(url_for("login"))
    return render_template_string(signup_page)

@app.route("/vihasa")
def vihasa():
    if "user" not in session:
        return redirect(url_for("login"))
    return render_template_string(vihasa_page, username=session["user"], courses=courses, contacts=contacts)

@app.route("/admin")
def admin():
    if "user" not in session or session["user"]!="admin":
        return redirect(url_for("login"))
    return render_template_string(admin_page)

@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("login"))

if __name__=="__main__":
    app.run(debug=True)
