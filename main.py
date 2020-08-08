import sys
import subprocess


if __name__ == '__main__':
    # Q1
    if subprocess.run('python q1_to_pie_chart.py', shell=True).returncode:
        sys.exit(1)
    # Q2
    if subprocess.run('python q2_to_bar_chart.py', shell=True).returncode:
        sys.exit(1)
    # Q3
    if subprocess.run('python q3_to_bar_chart.py', shell=True).returncode:
        sys.exit(1)
    # Q4
    if subprocess.run('python q4_to_bar_chart.py', shell=True).returncode:
        sys.exit(1)
