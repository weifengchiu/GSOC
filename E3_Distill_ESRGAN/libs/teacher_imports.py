import sys
import os
from libs import settings
_teacher_directory = settings.Settings(use_student_settings=True)[
    "teacher_directory"]
TEACHER_DIR = os.path.abspath(_teacher_directory)
if _teacher_directory not in sys.path:
  sys.path.insert(0, TEACHER_DIR)
