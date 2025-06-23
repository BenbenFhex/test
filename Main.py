
import time
import os
import threading

def monitor_server1():
    last_value = ""
    while True:
        if os.path.exists("server1_data.txt"):
            with open("server1_data.txt", "r") as f:
                current_value = f.read().strip()
            if current_value and current_value != last_value:
                print(f"Server1: {current_value}")
                last_value = current_value
        time.sleep(0.1)  # Check more frequently

def monitor_server2():
    last_value = ""
    while True:
        if os.path.exists("server2_data.txt"):
            with open("server2_data.txt", "r") as f:
                current_value = f.read().strip()
            if current_value and current_value != last_value:
                print(f"Server2: {current_value}")
                last_value = current_value
        time.sleep(0.1)  # Check more frequently

def main():
    print("Main.py is now running...")
    print("Monitoring servers independently...")
    
    # Start independent threads for each server
    thread1 = threading.Thread(target=monitor_server1, daemon=True)
    thread2 = threading.Thread(target=monitor_server2, daemon=True)
    
    thread1.start()
    thread2.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("Shutting down...")

if __name__ == "__main__":
    main()


