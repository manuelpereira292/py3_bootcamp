#--- Bad Way
import logging
import otherMod

def main():
    """
    The main entry point of the application
    """
    logging.basicConfig(filename="code_pack_19/bad_way/mySnake.log", level=logging.INFO)
    logging.info("Program started")
    result = otherMod.add(7, 8)
    logging.info("Done!")

if __name__ == "__main__":
    main()