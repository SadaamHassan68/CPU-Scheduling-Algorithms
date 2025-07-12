# CPU Scheduling Algorithms Web App

This web application allows you to simulate and visualize classic CPU scheduling algorithms:
- **First Come First Serve (FCFS)**
- **Shortest Job First (SJF)**
- **Priority Scheduling** (with FCFS tie-breaker)

You can enter process details, calculate waiting and turnaround times, and view step-by-step calculation explanations in a modal popup.

## Features
- Add/remove processes dynamically
- Input burst time and (for priority) priority number
- Select scheduling algorithm (FCFS, SJF, Priority)
- Calculate and display:
  - Waiting Time (WT)
  - Turnaround Time (TRT)
  - Step-by-step calculation steps for both WT and TRT
- For Priority Scheduling, processes with the same priority are scheduled in the order they were entered (FCFS)
- All calculations and table updates happen instantly in the browser (no page reload)

## How to Use
1. **Select Algorithm:** Choose FCFS, SJF, or Priority from the dropdown.
2. **Enter Processes:**
   - For each process, enter a name and burst time.
   - For Priority Scheduling, also enter a priority number (smaller number = higher priority).
   - Use "Add Process" to add more rows, or "X" to remove a row.
3. **Calculate:**
   - Click the **Calculate** button to compute waiting and turnaround times for all processes.
   - A modal will show step-by-step calculation details for both WT and TRT.
   - The table will update to show the results, and (for SJF/Priority) will be sorted by burst/priority.
4. **Other Tools:**
   - Use the extra buttons to calculate only waiting time, turnaround time, or averages as needed.

## Example
For Priority Scheduling:
| Process | Burst Time | Priority |
|---------|------------|----------|
| P1      | 10         | 3        |
| P2      | 1          | 1        |
| P3      | 2          | 4        |

After calculation, the table will be sorted by priority (and FCFS for ties), and waiting/turnaround times will be shown with step-by-step explanations.

## Setup Instructions

1. **Clone or Download the Repository**
2. **Install Python 3.x** (if not already installed)
3. **Install Flask**
   ```bash
   pip install flask
   ```
4. **Run the App**
   ```bash
   cd "operating ass"
   python app.py
   ```
5. **Open in Browser**
   - Go to [http://127.0.0.1:5000/](http://127.0.0.1:5000/) in your web browser.

## File Structure
- `app.py` - Flask backend (if used)
- `templates/` - HTML templates (mainly `scheduling.html`)
- `static/css/style.css` - Custom styles

## Notes
- All calculations are performed client-side in the browser using JavaScript.
- No data is sent to a server unless you modify the backend.
- For any issues or suggestions, please open an issue or contact the author. 