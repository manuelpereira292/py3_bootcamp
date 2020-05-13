import logging

logging.basicConfig(filename="sample.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")

# Let's use our file reading knowledge to 
# read the log file
with open("sample.log") as file_handler:
    for line in file_handler:
        print(line)