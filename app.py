from flask import Flask, render_template, request
from model import *

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    graph = None
    stationary_points = None
    stability_info = None
    if request.method == 'POST':
        a = float(request.form.get('a', 1))
        b = float(request.form.get('b', 1))
        N_0 = float(request.form.get('N_0', 1.5))
        n = int(request.form.get('n', 20))
        
        plot(N_0, n, a, b)

        stationary_points = get_stationary_points(a, b)
        stability_info = [(N, is_stable(N, a, b)) for N in stationary_points]

    return render_template('index.html', graph='static/plot.png', points=stationary_points, stability_info=stability_info, a=a, b=b, N_0=N_0, n=n)

if __name__ == "__main__":
    app.run(debug=True)
