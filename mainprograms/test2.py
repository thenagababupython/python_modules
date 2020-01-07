import logging
# create config logger
logging.basicConfig(filename="C:\\Users\\Nagababu\\Desktop\\localrepository\\log1.log",level=logging.DEBUG)
logger = logging.getLogger()

# test the logger
logger.info("our first message")

print(logger.level)