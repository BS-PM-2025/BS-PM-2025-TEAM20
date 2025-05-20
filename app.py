from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

# قاعدة البيانات – يتم إنشاؤها تلقائيًا إذا غير موجودة
def init_db():
    conn = sqlite3.connect('requests.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            document_type TEXT NOT NULL,
            reason TEXT,
            language TEXT,
            delivery_method TEXT
        )
    ''')
    conn.commit()
    conn.close()

# الصفحة الرئيسية - نموذج الطلب
@app.route('/', methods=['GET', 'POST'])
def request_document():
    if request.method == 'POST':
        document_type = request.form['document_type']
        reason = request.form['reason']
        language = request.form['language']
        delivery_method = request.form['delivery_method']

        conn = sqlite3.connect('requests.db')
        c = conn.cursor()
        c.execute('INSERT INTO documents (document_type, reason, language, delivery_method) VALUES (?, ?, ?, ?)',
                  (document_type, reason, language, delivery_method))
        conn.commit()
        conn.close()
        return redirect('/success')
    return render_template('request_form.html')

@app.route('/success')
def success():
    return "✅ تم إرسال الطلب بنجاح!"

if __name__ == '__main__':
    init_db()
    app.run(debug=True)

