from flask import Flask, render_template, request, send_file, flash, redirect, url_for
from werkzeug.utils import secure_filename
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField
from wtforms.validators import DataRequired
from pdf_modifier import modify_pdf  # Certifique-se de que este arquivo existe
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'sua-chave-secreta'
app.config['UPLOAD_FOLDER'] = './uploads/'

# Garante que a pasta de upload exista
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

class CPFInputForm(FlaskForm):
    cpf = StringField('CPF', validators=[DataRequired()])
    position = SelectField('Position', choices=[
        ('top-left', 'Top Left'),
        ('top-right', 'Top Right'),
        ('bottom-left', 'Bottom Left'),
        ('bottom-right', 'Bottom Right')
    ])
    color = SelectField('Color', choices=[
        ('red', 'Red'),
        ('blue', 'Blue'),
        ('black', 'Black')
    ], validators=[DataRequired()])
    submit = SubmitField('Submit')

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    form = CPFInputForm()
    
    if form.validate_on_submit():
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        # Verifica se o arquivo é um PDF válido
        if file and file.filename.lower().endswith('.pdf'):
            filename = secure_filename(file.filename)
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)

            cpf = form.cpf.data
            position = form.position.data
            color = form.color.data

            try:
                modify_pdf(filename, cpf, position, color, app.config['UPLOAD_FOLDER'])
                flash('PDF protegido com sucesso!', 'success')
                return send_file(file_path, as_attachment=True)
            except Exception as e:
                flash(f'Failed to process file: {str(e)}', 'error')
                return redirect(request.url)
        else:
            flash('O arquivo enviado não é um PDF válido.', 'error')
            return redirect(request.url)
    
    return render_template('index.html', form=form)

if __name__ == '__main__':
    app.run(debug=True)
