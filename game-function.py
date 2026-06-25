import time

def stopwatch():
    while True:
        command = input("\nEnter '1' to start the stopwatch or '2' to exit: ").strip()
        
        if command == '1':
            input("Press Enter to START the stopwatch...")
            start_time = time.time()
            
            input("Stopwatch is running... Press Enter to STOP!")
            end_time = time.time()
            
            elapsed_time = end_time - start_time
            print(f"Elapsed time: {elapsed_time:.2f} seconds")
        elif command == '2':
            print("Goodbye!")
            break
        else:
            print("Invalid command! Please try again.")

stopwatch()

