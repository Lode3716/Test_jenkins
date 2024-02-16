"""
   
 auth : l.devigne

"""
import threading

lock = threading.Lock()


def t01():
    with lock:
        for i in range(10):
            print(threading.current_thread().name, i)


def t02():
    with lock:
        for i in range(10):
            print(threading.current_thread().name, i)


def main():
    th1 = threading.Thread(target=t01)
    th2 = threading.Thread(target=t02)
    th1.start()
    th2.start()
    # On attend la fin du thread
    th1.join()
    th2.join()
    print("La fin")
    print(threading.current_thread().name)


if __name__ == '__main__':
    main()
