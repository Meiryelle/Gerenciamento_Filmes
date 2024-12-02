from flask import Flask, render_template, request, redirect, flash, url_for, session
from flask_mysqldb import MySQL

app = Flask(__name__)
app.secret_key = '12345'


app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = '12345' 
app.config['MYSQL_DB'] = 'cadastro_de_filmes_db'

mysql = MySQL(app)
@app.route('/')
def index():
    try:
        cur = mysql.connection.cursor()
        cur.execute('SELECT * FROM filmes')
        filmes = cur.fetchall()
        cur.close()
        return render_template('index.html', filmes=filmes)
    except Exception as e:
        return f"Erro ao acessar o banco de dados: {str(e)}"

@app.route('/add', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        titulo = request.form['titulo']
        diretor = request.form['diretor']
        genero = request.form['genero']
        ano = request.form['ano']

        cur = mysql.connection.cursor()
        cur.execute(
            'INSERT INTO filmes (titulo, diretor, genero, ano) VALUES (%s, %s, %s, %s)',
            (titulo, diretor, genero, ano)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    return render_template('add.html')

@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    cur = mysql.connection.cursor()

    if request.method == 'POST':
        titulo = request.form['titulo']
        diretor = request.form['diretor']
        genero = request.form['genero']
        ano = request.form['ano']

        cur.execute(
            'UPDATE filmes SET titulo = %s, diretor = %s, genero = %s, ano = %s WHERE id = %s',
            (titulo, diretor, genero, ano, id)
        )
        mysql.connection.commit()
        cur.close()

        return redirect(url_for('index'))

    cur.execute('SELECT * FROM filmes WHERE id = %s', (id,))
    filme = cur.fetchone()
    cur.close()
    return render_template('edit.html', filme=filme)

@app.route('/deletar/<int:id>')
def deletar(id):
    cur = mysql.connection.cursor()
    cur.execute('DELETE FROM filmes WHERE id = %s', (id,))
    mysql.connection.commit()
    cur.close()

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)