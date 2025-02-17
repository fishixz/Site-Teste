import os
from flask import Flask, render_template, request, redirect, url_for, send_from_directory

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/')
def index():
    movies = []
    for filename in os.listdir(app.config['UPLOAD_FOLDER']):
        if filename.endswith('.mp4'):
            movies.append(filename)
    return render_template('index.html', movies=movies)

@app.route('/admin', methods=['GET', 'POST'])
def admin():
    if request.method == 'POST':
        movie = request.files['movie']
        movie_name = request.form['movie_name']
        if movie and movie_name:
            movie.save(os.path.join(app.config['UPLOAD_FOLDER'], movie_name + '.mp4'))
            return redirect(url_for('admin'))
    return render_template('admin.html')

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=True, host='0.0.0.0', port=port)