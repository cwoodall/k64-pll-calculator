from flask import Flask, request, jsonify, render_template
import logging

from .. import PLLSolver

logging.basicConfig()
logger = logging.getLogger(__name__)
app = Flask(__name__)

def compose_json_error(e):
    return jsonify({
        "status": "error",
        "payload": {
            "error": "{}".format(e)
        }
    })

def compose_json_success(solution):
    return jsonify({
        "status": "success",
        "payload": solution.serialize()
    })

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/solve')
def solve():
    try:
        freq_in = int(float(request.args.get('fin')))
        freq_out = int(float(request.args.get('fout')))
    except Exception as e:
        return compose_json_error(e)
    solver = PLLSolver()

    try:
        solver.solve(freq_in, freq_out)
    except Exception as e:
        return compose_json_error(e)

    return compose_json_success(solver)
