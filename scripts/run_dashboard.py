import os
import subprocess

def run_streamlit_dashboard():
    """
    Run the Streamlit dashboard app.
    """
    try:
        print("Starting the Streamlit dashboard...")
        subprocess.run(["streamlit", "run", "../src/dashboard.py"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Error occurred while running the dashboard: {e}")
    except FileNotFoundError:
        print("Streamlit is not installed. Please install Streamlit using 'pip install streamlit'.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    run_streamlit_dashboard()
