from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# เก็บข้อมูลวันและเวลาที่ว่างของแต่ละคน
availability_data = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    available_days = request.form.getlist('available_days')
    available_times = request.form.getlist('available_times')

    # เก็บข้อมูลวันและเวลาว่าง
    availability_data.append({
        'name': name,
        'days': available_days,
        'times': available_times
    })

    return redirect(url_for('index'))

@app.route('/result')
def result():
    # หาเวลาที่ทุกคนว่างตรงกัน
    if not availability_data:
        return "No data available."

    common_days = set(availability_data[0]['days'])
    common_times = set(availability_data[0]['times'])

    for availability in availability_data[1:]:
        common_days = common_days.intersection(availability['days'])
        common_times = common_times.intersection(availability['times'])

    return render_template('result.html', common_days=common_days, common_times=common_times)

if __name__ == '__main__':
    app.run(debug=True)
