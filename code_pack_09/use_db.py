import os
from files_db import *

if os.path.exists("students.txt"):
    os.remove("students.txt")

add_student("João")
add_student("Manuel") 
add_student("Miguel")
add_student("Mário")
add_student("Pedro")
add_student("Vasco")
add_student("Ricardo")

find_student("Ricardo")
update_student("Ricardo", "Pinto")
find_student("Pinto")
remove_student("Pinto")
find_student("Pinto")
