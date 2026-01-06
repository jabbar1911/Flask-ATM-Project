from flask import Flask, request,url_for,redirect,render_template ,make_response, flash
from datetime import datetime

app=Flask(__name__)
# Generated using: import secrets; secrets.token_hex(32)
app.secret_key = '8c851a0065b2c05d358826500e1e603373c8195cf7ac1c2d577acdc57ca449f7'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register',methods=['GET',"POST"])
def register():
    """
    Handle user registration.
    Validates inputs, ensures unique username, and creates a new user account.
    """
    if request.method=='POST':
        username=request.form['username']
        useremail=request.form['email']
        contact=request.form['contact']
        pin=request.form['pin']
        confirm_pin=request.form['confirm_pin']
        if pin != confirm_pin:
            flash('PINs do not match', 'danger')
            return redirect(url_for('register'))
            
        if len(pin) != 4 or not pin.isdigit():
            flash('PIN must be exactly 4 digits', 'danger')
            return redirect(url_for('register'))
            
        if len(contact) != 10 or not contact.isdigit():
            flash('Phone number must be exactly 10 digits', 'danger')
            return redirect(url_for('register'))

        if username not in users:
            # Create user with initial data and empty transaction history
            users[username]={'email':useremail,'contact':contact,'pin':pin,'amount':0,'transactions':[]}
            print(users)
            flash('Registration Successful. Please Login.', 'success')
            return redirect(url_for('login'))
        else:
            flash('User already exists....', 'danger')
            return redirect(url_for('register'))
        
    return render_template('registration.html')

@app.route('/login',methods=['GET','POST'])
def login():
    """
    Handle user login.
    Verifies username and PIN.
    """
    if request.method=='POST':
        login_username=request.form['username']
        if login_username in users:
            login_pin=request.form['pin']
            pin=users[login_username]['pin']
            if login_pin==pin:
                # return render_template('dashboard.html')
                response=make_response(redirect(url_for('dashboard')))
                response.set_cookie('username',login_username)
                flash('Login Successful', 'success')
                return response
            else:
                flash('Invalid PIN', 'danger')
                return redirect(url_for('login'))
        else:
            flash('Username not found', 'danger')
            return redirect(url_for('login'))
    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    """
    Display user dashboard.
    Requires user to be logged in (checked via cookie).
    """
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
    """
    Handle fund deposits.
    Updates balance and records transaction.
    Enforces deposit limits and constraints.
    """
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        amount = int(request.form['amount'])
        pin = request.form['pin']
        
        if amount > 50000:
            flash('Deposit limit is 50,000', 'warning')
            return redirect(url_for('deposit'))
            
        if amount % 100 != 0:
            flash('Amount must be in multiples of 100', 'warning')
            return redirect(url_for('deposit'))
        
        if users[username]['pin'] == pin:
            users[username]['amount'] += amount
            transaction = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'type': 'Credit',
                'amount': amount
            }
            users[username]['transactions'].append(transaction)
            flash('Amount Deposited Successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid PIN', 'danger')
            return redirect(url_for('deposit'))
            
    return render_template('deposit.html')

@app.route('/withdraw', methods=['GET', 'POST'])
def withdraw():
    """
    Handle fund withdrawals.
    Updates balance and records transaction.
    Checks for sufficient funds and withdrawal limits.
    """
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))

    if request.method == 'POST':
        amount = int(request.form['amount'])
        pin = request.form['pin']

        if amount > 10000:
            flash('Withdraw limit is 10,000', 'warning')
            return redirect(url_for('withdraw'))
        
        if amount % 100 != 0:
            flash('Amount must be in multiples of 100', 'warning')
            return redirect(url_for('withdraw'))
            
        if users[username]['amount'] < amount:
            flash('Insufficient Balance', 'danger')
            return redirect(url_for('withdraw'))

        if users[username]['pin'] == pin:
            users[username]['amount'] -= amount
            transaction = {
                'date': datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
                'type': 'Debit',
                'amount': amount
            }
            users[username]['transactions'].append(transaction)
            flash('Amount Withdrawn Successfully', 'success')
            return redirect(url_for('dashboard'))
        else:
            flash('Invalid PIN', 'danger')
            return redirect(url_for('withdraw'))
            
    return render_template('withdraw.html')

@app.route('/delete', methods=['GET', 'POST'])
def delete():
    """
    Handle account deletion.
    Permanently removes user data if PIN is verified.
    """
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
        
    if request.method == 'POST':
        pin = request.form['pin']
        if users[username]['pin'] == pin:
            del users[username]
            return redirect(url_for('logout'))
        else:
            flash('Invalid PIN', 'danger')
            return redirect(url_for('delete'))
            
    return render_template('delete.html')
@app.route('/statement')
def statement():
    """
    Display transaction history.
    Shows reversed list of transactions (newest first).
    """
    username = request.cookies.get('username')
    if not username:
        return redirect(url_for('login'))
    
    user_data = users.get(username)
    if user_data:
        transactions = user_data.get('transactions', [])
        # Sort transactions by date (newest first) - assuming appending makes them oldest first, so reverse
        transactions = transactions[::-1]
        return render_template('statement.html', transactions=transactions, username=username)
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    """
    Handle user logout.
    Clears the session cookie.
    """
    flash('You have been logged out.', 'info')
    response=make_response(redirect(url_for('index')))
    response.delete_cookie('username')
    return response

users={}

if __name__ == "__main__":
    app.run(debug=False)
    