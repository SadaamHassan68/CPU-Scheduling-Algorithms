from flask import Flask, render_template
import flask

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scheduling', methods=['GET', 'POST'])
def scheduling():
    results = None
    avg_waiting = None
    avg_burst = None
    algorithm = None
    if flask.request.method == 'POST':
        algorithm = flask.request.form.get('algorithm')
        processes = flask.request.form.getlist('process[]')
        bursts = flask.request.form.getlist('burst[]')
        bursts = [int(b) for b in bursts]
        priorities = flask.request.form.getlist('priority[]') if algorithm == 'priority' else None
        if algorithm == 'fcfs':
            waiting_times = [0]
            for i in range(1, len(bursts)):
                waiting_times.append(waiting_times[i-1] + bursts[i-1])
            results = [
                {'process': processes[i], 'burst': bursts[i], 'waiting': waiting_times[i]} for i in range(len(processes))
            ]
        elif algorithm == 'sjf':
            paired = sorted(zip(processes, bursts), key=lambda x: x[1])
            waiting_times = [0]
            for i in range(1, len(paired)):
                waiting_times.append(waiting_times[i-1] + paired[i-1][1])
            results = [
                {'process': paired[i][0], 'burst': paired[i][1], 'waiting': waiting_times[i]} for i in range(len(paired))
            ]
        elif algorithm == 'priority':
            priorities = [int(p) for p in priorities]
            paired = sorted(zip(processes, bursts, priorities), key=lambda x: x[2])
            waiting_times = [0]
            for i in range(1, len(paired)):
                waiting_times.append(waiting_times[i-1] + paired[i-1][1])
            results = [
                {'process': paired[i][0], 'burst': paired[i][1], 'priority': paired[i][2], 'waiting': waiting_times[i]} for i in range(len(paired))
            ]
        avg_waiting = round(sum([row['waiting'] for row in results]) / len(results), 2) if results else 0
        avg_burst = round(sum([row['burst'] for row in results]) / len(results), 2) if results else 0
    return flask.render_template('scheduling.html', results=results, avg_waiting=avg_waiting, avg_burst=avg_burst, algorithm=algorithm)

if __name__ == '__main__':
    app.run(debug=True) 