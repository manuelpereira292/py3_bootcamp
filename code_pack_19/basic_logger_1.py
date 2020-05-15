import logging

# add filemode="w" to overwrite
logging.basicConfig(filename="code_pack_19/sample.log", level=logging.DEBUG)

logging.debug("This is a debug message")
logging.info("Informational message")
logging.error("An error has happened!")

# Let's use our file reading knowledge to 
# read the log file
with open("code_pack_19/sample.log") as file_handler:
    for line in file_handler:
        print(line)