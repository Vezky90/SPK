from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import os

app = Flask(__name__)

# Data alternatif dan kriteria
alternatives = {
    "Alternatif A": [70, 80, 90],
    "Alternatif B": [80, 60, 75],
    "Alternatif C": [60, 70, 85]
}

weights = [0.4, 0.3, 0.3]  # Bobot untuk masing-masing kriteria

@app.route('/')
def index():
    return render_template('index.html', alternatives=alternatives)

@app.route('/result', methods=['POST'])
def result():
    # Normalisasi
    max_values = [max(col) for col in zip(*alternatives.values())]
    scores = {}
    for alt, values in alternatives.items():
        norm = [v / m for v, m in zip(values, max_values)]
        total = sum(w * n for w, n in zip(weights, norm))
        scores[alt] = round(total, 4)

    # Buat grafik
    plt.clf()
    names = list(scores.keys())
    values = list(scores.values())
    plt.bar(names, values, color='skyblue')
    plt.title("Hasil SPK - SAW")
    plt.ylabel("Skor")
    plt.savefig('static/graph.png')

    return render_template('result.html', scores=scores, image_path='static/graph.png')

if __name__ == "__main__":
    app.run(debug=True)


