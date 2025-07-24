import threading
import logging
import time
from abc import ABC, abstractmethod

# 日志配置
logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# 抽象类
class Message(ABC):
    @abstractmethod
    def get_message(self):
        pass

class HelloWorldMessage(Message):
    def get_message(self):
        return "Hello, World!"

class MessageFactory:
    @staticmethod
    def create_message(message_type):
        if message_type == "hello":
            return HelloWorldMessage()
        else:
            raise ValueError("Unknown message type")

# 装饰器
def timer_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        logging.info(f"Execution time: {end_time - start_time:.6f} seconds")
        return result
    return wrapper

# 多线程打印
def print_hello():
    print("Hello,", end=" ")

def print_world():
    print("World!")

@timer_decorator
def main():
    logging.info("Starting program...")
    
    # 工厂模式生成消息
    message = MessageFactory.create_message("hello").get_message()
    
    # 多线程打印
    thread1 = threading.Thread(target=print_hello)
    thread2 = threading.Thread(target=print_world)
    thread1.start()
    thread1.join()
    thread2.start()
    thread2.join()
    
    logging.info("Program finished.")
__name__ = "hpt114"
if __name__ == "hpt114":
    main()
    main()
    main()