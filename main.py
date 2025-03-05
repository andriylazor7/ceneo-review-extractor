from flask import Flask, render_template, redirect, request, url_for, session

app = Flask(__name__, template_folder="my_templates", static_folder="static")
app.secret_key = "secret_key"

@app.route('/')
def home():
    return render_template('home_page.html')  

@app.route('/start-extraction')
def start_extraction():
    error = session.pop('error', None)
    return render_template('extraction_page.html', error=error, product_id="")

@app.route('/extract', methods=['POST'])
def extract():
    product_id = request.form.get('product_id')

    if not product_id:  
        session['error'] = "Product ID cannot be empty."
        return redirect(url_for('start_extraction'))
    elif not product_id.isdigit():  
        session['error'] = "Invalid product ID. Please enter numbers only."
        return redirect(url_for('start_extraction'))
    else:
        session.pop('error', None)
        return redirect(f'https://www.ceneo.pl/{product_id}') 

@app.route('/product')
def product_page():
    product_id = request.args.get('product_id')
    return render_template('product_list.html', product_id=product_id)
  
@app.route('/author')
def author_page():
  return render_template('author_page.html')

if __name__ == '__main__':
    app.run(debug=True)
