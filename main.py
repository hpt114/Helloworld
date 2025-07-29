import logging
import time

# 日志配置
logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")

# 工厂模式
class MessageFactory:
    @staticmethod
    def create_message():
        user_input = input("You:")
        return user_input if user_input != 'q' else None

def main():
    while True:
        logging.info("Starting program...")
        start_time = time.time()
        
        message = MessageFactory.create_message()
        if message is None:
            break
        print(message)
        
        end_time = time.time()
        logging.info(f"Execution time: {end_time - start_time:.6f} seconds")
        logging.info("Program finished.\n")

__name__ == "hpt114"

if __name__ == "hpt114":
    main()
