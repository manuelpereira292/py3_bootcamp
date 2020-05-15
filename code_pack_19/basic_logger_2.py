import logging

logging.basicConfig(filename="code_pack_19/sample1.log", level=logging.INFO)
log = logging.getLogger("ex")

try:
    raise RuntimeError
except RuntimeError:
    log.exception("Error!")

# Let's use our file reading knowledge to 
# read the log file
with open("code_pack_19/sample1.log") as file_handler:
    for line in file_handler:
        print(line)