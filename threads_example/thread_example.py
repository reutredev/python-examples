import threading
import time

def worker(text):
    cnt = 0
    print(text)
    while not done:
        time.sleep(1)
        cnt+=1
        print(cnt)


done = False
t = threading.Thread(target=worker, args=("A",), daemon=True)
t.start()
input("Press enter to stop\n")
done = True

