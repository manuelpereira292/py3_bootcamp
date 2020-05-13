import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="sample.log", level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

# Let's use our file reading knowledge to 
# read the log file
with open("sample.log") as file_handler:
    for line in file_handler:
        print(line)