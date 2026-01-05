# 31-12-25,1-1-26
from flask import Flask, request,url_for,redirect,render_template ,make_response

app=Flask(__name__)
@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET',"POST"])
# @app.route('/registration.html')
def register():
    if request.method=='POST':
        # username=request.form.get('username')
        username=request.form['username']
        useremail=request.form['email']
        contact=request.form['contact']
        pin=request.form['pin']
        confirm_pin=request.form['confirm_pin']
        if username not in users:
            # users[contact]={'username':username,'email':useremail,'pin':pin} //my method
            users[username]={'email':useremail,'contact':contact,'pin':pin,'amount':0}
            # return users # to check details
            print(users)
            return redirect(url_for('login'))
        else:
            return 'User already exists....'
        
    return render_template('registration.html')

@app.route('/login',methods=['GET','POST'])
# @app.route('/login.html')
def login():
    if request.method=='POST':
        # login_contact=request.form['contact'] # if my method is used in register function
        login_username=request.form['username']
        if login_username in users:
            login_pin=request.form['pin']
            pin=users[login_username]['pin']
            if login_pin==pin:
                # return render_template('dashboard.html')
                response=make_response(redirect(url_for('dashboard')))
                response.set_cookie('username',login_username)
                return response
            else:
                return 'invalid pin....'
        else:
            return 'Username not found....'
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    username=request.cookies.get('username')
    if username:
        user_data = users[username]
        balance = user_data['amount']
        email = user_data['email']
        contact = user_data['contact']
        return render_template('dashboard.html', username=username, balance=balance, email=email, contact=contact)
    else:
        return redirect(url_for('login'))

@app.route('/deposit', methods=['GET', 'POST'])
def deposit():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        amount = int(request.form['amount'])
        pin = request.form['pin']
        
        if amount > 50000:
            return "Deposit limit is 50,000"
            
        if amount % 100 != 0:
            return "Amount must be in multiples of 100"
        
        if users[username]['pin'] == pin:
            users[username]['amount'] += amount
            return redirect(url_for('dashboard'))
        else:
            return "Invalid PIN"
            
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        amount = int(request.form['amount'])
        pin = request.form['pin']

        if amount > 10000:
            return "Withdraw limit is 10,000"
        
        if amount % 100 != 0:
            return "Amount must be in multiples of 100"
            
        if users[username]['amount'] < amount:
            return "Insufficient Balance"

        if users[username]['pin'] == pin:
            users[username]['amount'] -= amount
            return redirect(url_for('dashboard'))
        else:
            return "Invalid PIN"
            
    return render_template('withdraw.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        pin = request.form['pin']
        if users[username]['pin'] == pin:
            del users[username]
            return redirect(url_for('logout'))
        else:
            return "Invalid PIN"
            
    return render_template('delete.html')

@app.route('/logout')
def logout():
    response=make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    return response

users={}

if __name__ == "__main__":
    app.run(debug=False)