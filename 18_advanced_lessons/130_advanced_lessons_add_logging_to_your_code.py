# Lesson 130 - Advanced Lessons - Add Logging To Your Code
# Video: https://www.youtube.com/watch?v=VwDzQKfYs_k

# --------------------------------------------------
# -- Advanced_Lessons => Add Logging To Your Code --
# --------------------------------------------------
# - Print Out To Console Or File
# - Print Logs Of What Happens
# ------------------------------
# - DEBUG
# - INFO
# - WARNING
# - ERROR
# - CRITICAL
# ----------
# name => Logging Module Give It To The Default Logger.
# -----------------------------------------------------
# Basic Config
# - level => Level of Severity
# - filename => File Name and Extension
# - mode => Mode Of The File a => Append
# - format => Format For The Log Message
# ------------------------
# getLogger => Return a Logger With the Specified Name

import logging

# print(dir(logging))

# ملاحظة مهمة: الأمر basicConfig يعمل مرة واحدة فقط في كل تشغيل للبرنامج
# أي استدعاء بعده يتم تجاهله بصمت، لذلك الأسطر التالية أمثلة منفصلة
# فعل واحدا منها فقط في كل مرة، وبجانب كل مثال شكل السطر الذي يكتبه في الملف my_app.log

# logging.basicConfig(filename="my_app.log", filemode="a") # CRITICAL:root:This Is Critical Message

# logging.basicConfig(filename="my_app.log", filemode="a", format="%(name)s") # root

# logging.basicConfig(filename="my_app.log", filemode="a", format="%(name)s %(levelname)s") # root CRITICAL

# logging.basicConfig(filename="my_app.log", filemode="a", format="%(name)s %(levelname)s %(message)s") # root CRITICAL This Is Critical Message

# logging.basicConfig(filename="my_app.log", filemode="a", format="%(asctime)s %(name)s %(levelname)s %(message)s") # 2026-03-27 21:16:32,296 root CRITICAL This Is Critical Message

# logging.basicConfig(filename="my_app.log", filemode="a", format="(%(asctime)s) => | %(name)s | %(levelname)s => '%(message)s'") # (2026-03-27 21:19:12,663) => | root | CRITICAL => 'This Is Critical Message'

# ----------------------------------------------

# المثال المفعل: نفس الشكل السابق مع تنسيق خاص للتاريخ عن طريق datefmt

logging.basicConfig(filename="my_app.log",
                    filemode="a",
                    format="(%(asctime)s) | %(name)s | %(levelname)s => '%(message)s'",
                    datefmt="%d %B %Y, %H:%M:%S")

logging.critical("This Is Critical Message") # (27 March 2026, 21:29:34) | root | CRITICAL => 'This Is Critical Message'

logging.error("This Is Error Message")       # (27 March 2026, 21:29:34) | root | ERROR => 'This Is Error Message'

logging.warning("This Is Warning Message")   # (27 March 2026, 21:29:34) | root | WARNING => 'This Is Warning Message'

# الرسائل من نوع DEBUG و INFO لا تكتب، لأن المستوى الافتراضي هو WARNING
# لكتابتها نضيف level=logging.DEBUG داخل basicConfig

# ----------------------------------------------

my_logger = logging.getLogger("Albasha") # Albasha لاسم خاص فيا rootمن ال logger هيك غيرت اسم ال

my_logger.warning("This Is Warning Message") # (27 March 2026, 21:40:33) | Albasha | WARNING => 'This Is Warning Message'
