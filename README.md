# دورة بايثون بالعربي: ملاحظات وشرح وأمثلة مجربة

> **English:** My study notes for the free Arabic Python course *Mastering Python* by
> [Elzero Web School](https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs).
> Every lesson is a runnable Python file with explanations written in Arabic and the real output next to the code.
> 149 lessons in 22 topic folders, plus the course assignments.

ملاحظاتي الكاملة على دورة بايثون المجانية من **الزيرو ويب سكول**، مرتبة ومراجعة.

- **كل درس ملف بايثون يشتغل.** الشرح مكتوب بالعربي داخل الملف، وجنب كل سطر الناتج اللي بيطبعه.
- **كل ناتج مكتوب مجرّب.** شغّلت كل الدروس وقارنت النتيجة الحقيقية بالمكتوب، وصححت الاختلافات.
- **مرتبة حسب المواضيع.** 22 مجلد، وكل مجلد فيه دروس موضوع واحد.
- **رقم الملف هو نفس رقم الفيديو.** الملف `021_lists.py` هو شرح الفيديو رقم 21، وجنب كل درس رابط الفيديو تبعه.

---

## المصدر

هذه الملاحظات مبنية على دورة **Mastering Python** المجانية من قناة الزيرو ويب سكول للأستاذ أسامة الزيرو.

- قائمة الفيديوهات: [Mastering Python على يوتيوب](https://www.youtube.com/playlist?list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs)

ترتيب الدروس وعناوينها وأغلب الأمثلة من الدورة الأصلية. الشرح العربي والملاحظات والتمارين الإضافية من كتابتي.
هذا المستودع لا يغني عن مشاهدة الدورة، هو مرجع للمراجعة بعد كل فيديو.

---

## كيف تستخدم الملفات

### المتطلبات

- بايثون 3.12 أو أحدث. الدروس مجربة على بايثون 3.12.

### التجهيز مرة واحدة

انسخ المستودع وادخل إلى مجلده:

```bash
git clone https://github.com/MohammedAMohsen/python-course.git
cd python-course
```

أنشئ بيئة افتراضية وثبّت المكتبات (الشرح الكامل في الدرس 150):

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

على ويندوز يكون أمر التفعيل هكذا: `.venv\Scripts\activate`

### تشغيل أي درس

شغّل الدروس **من المجلد الرئيسي للمستودع**، لأن مسارات الملفات والصور وقواعد البيانات تبدأ منه:

```bash
python 02_strings/012_strings_indexing_and_slicing.py
```

إذا كنت تستخدم VS Code، افتح المجلد الرئيسي كاملاً ثم شغّل أي ملف.

### ملاحظات مهمة

- **الدروس 001 و 002 و 005 ليس لها ملفات**، لأنها فيديوهات شرح نظري بدون كود.
- **بعض الدروس تطلب منك إدخال قيمة**، مثل الاسم أو العمر. اكتب القيمة في الطرفية واضغط Enter.
- **بعض النواتج تختلف عندك**، مثل الأرقام العشوائية، والتاريخ، والوقت، وعناوين الذاكرة. هذا طبيعي، ومكتوب جنب كل واحد منها.
- **بعض الملفات تتوقف عند خطأ بشكل مقصود** لتوضيح الخطأ. مكتوب في أول الملف كيف تجرب الجزء الذي بعده.
- **قواعد البيانات تُنشأ عند التشغيل.** شغّل دروس قواعد البيانات بالترتيب من 118. التمرين 139b يحتاج بيانات من دروس تطبيق المهارات (123 إلى 126).

---

## شكل المستودع

```
python-course/
├── 01_basics/ ... 22_virtual_environment_and_end/   دروس الدورة، مجلد لكل موضوع
├── assignments/     حلول الواجبات، كل ملف لمجموعة دروس
├── files/           ملفات نصية تقرأها دروس التعامل مع الملفات
├── images/          صور تستخدمها دروس مكتبة Pillow
├── database/        هنا تُنشأ قواعد البيانات عند تشغيل الدروس
└── requirements.txt المكتبات الخارجية المستخدمة في الدورة
```

---

## فهرس الدروس

### 1. الأساسيات — الدروس 003 إلى 010

كتابة أول برنامج، والتعليقات، وأنواع البيانات، والمتغيرات، ورموز الهروب.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 003 | [Syntax And Your First App](<01_basics/003_syntax_and_first_app.py>) | [مشاهدة](https://www.youtube.com/watch?v=xiMHoMVWdI4) |
| 004 | [Comments And How To Use It](<01_basics/004_comments.py>) | [مشاهدة](https://www.youtube.com/watch?v=YsENRLNaYug) |
| 006 | [Some Data Types Overview](<01_basics/006_some_data_types_overview.py>) | [مشاهدة](https://www.youtube.com/watch?v=43lT7k0Zws0) |
| 007 | [Variables Part One](<01_basics/007_variables_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=hQnZxqp3Q0Y) |
| 008 | [Variables Part Two](<01_basics/008_variables_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=U0307lBCiDk) |
| 009 | [Escape Sequences Characters](<01_basics/009_escape_sequences_characters.py>) | [مشاهدة](https://www.youtube.com/watch?v=cr2Nk2E0f5A) |
| 010 | [Concatenation And Training](<01_basics/010_concatenation_and_training.py>) | [مشاهدة](https://www.youtube.com/watch?v=7I_fUo5mO-U) |

### 2. النصوص — الدروس 011 إلى 018

التقطيع، وأهم دوال النصوص، وتنسيق النص بالطرق القديمة والحديثة.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 011 | [Strings](<02_strings/011_strings.py>) | [مشاهدة](https://www.youtube.com/watch?v=j0Wktr70Cgw) |
| 012 | [Strings - Indexing And Slicing](<02_strings/012_strings_indexing_and_slicing.py>) | [مشاهدة](https://www.youtube.com/watch?v=PEp4oqzthnw) |
| 013 | [Strings Methods Part One](<02_strings/013_strings_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=HmDLsnLgt0M) |
| 014 | [Strings Methods Part Two](<02_strings/014_strings_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=doDJDkUOEJQ) |
| 015 | [Strings Methods Part Three](<02_strings/015_strings_methods_part_3.py>) | [مشاهدة](https://www.youtube.com/watch?v=kgb96E9ogUw) |
| 016 | [Strings Methods Part Four](<02_strings/016_strings_methods_part_4.py>) | [مشاهدة](https://www.youtube.com/watch?v=jbV9d9H-udY) |
| 017 | [Strings Formatting The Old Way](<02_strings/017_strings_formatting_the_old_way.py>) | [مشاهدة](https://www.youtube.com/watch?v=m_OUIywn_XE) |
| 018 | [Strings Formatting The New Ways](<02_strings/018_strings_formatting_the_new_ways.py>) | [مشاهدة](https://www.youtube.com/watch?v=nn4qN90A7X4) |

### 3. الأرقام والقوائم والمجموعات والقواميس — الدروس 019 إلى 033

الأرقام والعمليات الحسابية، ثم القوائم والصفوف والمجموعات والقواميس ودوالها.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 019 | [Numbers](<03_data_types/019_numbers.py>) | [مشاهدة](https://www.youtube.com/watch?v=x7fFnKVAzDI) |
| 020 | [Arithmetic Operators](<03_data_types/020_arithmetic_operators.py>) | [مشاهدة](https://www.youtube.com/watch?v=prv7cVm2dxE) |
| 021 | [Lists](<03_data_types/021_lists.py>) | [مشاهدة](https://www.youtube.com/watch?v=EpZH9JozUzA) |
| 022 | [Lists Methods Part One](<03_data_types/022_lists_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=b5cFjJ278Vk) |
| 023 | [Lists Methods Part Two](<03_data_types/023_lists_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=pP0QJbJalik) |
| 024 | [Tuples And Methods Part One](<03_data_types/024_tuples_and_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=gwKxpFG_h_8) |
| 025 | [Tuples And Methods Part Two](<03_data_types/025_tuples_and_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=MDR7c5ozo7I) |
| 026 | [Set](<03_data_types/026_set.py>) | [مشاهدة](https://www.youtube.com/watch?v=PSc6QX4Py7k) |
| 027 | [Set Methods Part One](<03_data_types/027_set_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=N06_D5wWobg) |
| 028 | [Set Methods Part Two](<03_data_types/028_set_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=o8pr--y5vuU) |
| 029 | [Set Methods Part Three](<03_data_types/029_set_methods_part_3.py>) | [مشاهدة](https://www.youtube.com/watch?v=rs9eebZpcaE) |
| 030 | [Dictionary](<03_data_types/030_dictionary.py>) | [مشاهدة](https://www.youtube.com/watch?v=BQ7jFrysbQU) |
| 031 | [Dictionary Methods Part One](<03_data_types/031_dictionary_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=oNLaNJrU8r8) |
| 032 | [Dictionary Methods Part Two](<03_data_types/032_dictionary_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=rgOdxQa830Q) |
| 033 | [Boolean](<03_data_types/033_boolean.py>) | [مشاهدة](https://www.youtube.com/watch?v=eDmGoHk1Y8k) |

### 4. العوامل وإدخال المستخدم — الدروس 034 إلى 040

عوامل المقارنة والمنطق والإسناد، وتحويل الأنواع، وأخذ مدخلات من المستخدم.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 034 | [Boolean Operators](<04_operators_and_input/034_boolean_operators.py>) | [مشاهدة](https://www.youtube.com/watch?v=zN6ZYGSBKbM) |
| 035 | [Assignment Operators](<04_operators_and_input/035_assignment_operators.py>) | [مشاهدة](https://www.youtube.com/watch?v=mvyEHxIX_lE) |
| 036 | [Comparison Operators](<04_operators_and_input/036_comparison_operators.py>) | [مشاهدة](https://www.youtube.com/watch?v=bBxO141Jq6I) |
| 037 | [Type Conversion](<04_operators_and_input/037_type_conversion.py>) | [مشاهدة](https://www.youtube.com/watch?v=j26DuY69HYA) |
| 038 | [User Input](<04_operators_and_input/038_user_input.py>) | [مشاهدة](https://www.youtube.com/watch?v=2EY1CCnByK4) |
| 039 | [Practical - Email Slice](<04_operators_and_input/039_practical_email_slice.py>) | [مشاهدة](https://www.youtube.com/watch?v=jQVMF7kEzvI) |
| 040 | [Practical - Your Age Full Details](<04_operators_and_input/040_practical_your_age_full_details.py>) | [مشاهدة](https://www.youtube.com/watch?v=S6dhvob-4DM) |

### 5. الشروط — الدروس 041 إلى 046

if و elif و else، والشروط المتداخلة، والشرط المختصر، والعامل in.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 041 | [Control Flow - If, Elif, Else](<05_control_flow/041_control_flow_if_elif_else.py>) | [مشاهدة](https://www.youtube.com/watch?v=v8ZehXS3XF0) |
| 042 | [Control Flow - Nested If And Training](<05_control_flow/042_control_flow_nested_if_and_training.py>) | [مشاهدة](https://www.youtube.com/watch?v=W6KsrqVvg2E) |
| 043 | [Control Flow - Ternary Conditional Operator](<05_control_flow/043_control_flow_ternary_conditional_operator.py>) | [مشاهدة](https://www.youtube.com/watch?v=1E7z7r61b2s) |
| 044 | [Calculate Age Advanced Version and Training](<05_control_flow/044_calculate_age_advanced_version_and_training.py>) | [مشاهدة](https://www.youtube.com/watch?v=MpO84gVARdE) |
| 045 | [Membership Operators](<05_control_flow/045_membership_operators.py>) | [مشاهدة](https://www.youtube.com/watch?v=FGnMK1y9TkE) |
| 046 | [Practical Membership Control](<05_control_flow/046_practical_membership_control.py>) | [مشاهدة](https://www.youtube.com/watch?v=r9MaqQ0Iis0) |

### 6. الحلقات — الدروس 047 إلى 055

while و for، والحلقات المتداخلة، و break و continue و pass.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 047 | [Loop - While and Else](<06_loops/047_loop_while_and_else.py>) | [مشاهدة](https://www.youtube.com/watch?v=A0oBGPSUbeI) |
| 048 | [Loop - While Training's](<06_loops/048_loop_while_trainings.py>) | [مشاهدة](https://www.youtube.com/watch?v=9rU2fImqSR4) |
| 049 | [Loop - While Training's Bookmark Manager](<06_loops/049_loop_while_trainings_bookmark_manager.py>) | [مشاهدة](https://www.youtube.com/watch?v=jRGJjckgSlA) |
| 050 | [Loop - While Training's Password Guess](<06_loops/050_loop_while_trainings_password_guess.py>) | [مشاهدة](https://www.youtube.com/watch?v=7NIcsmfHIrg) |
| 051 | [Loop For and Else](<06_loops/051_loop_for_and_else.py>) | [مشاهدة](https://www.youtube.com/watch?v=4YolrVX6f1Q) |
| 052 | [Loop For Training's](<06_loops/052_loop_for_trainings.py>) | [مشاهدة](https://www.youtube.com/watch?v=9JJDDKj_tGA) |
| 053 | [Loop For Nested Loop](<06_loops/053_loop_for_nested_loop.py>) | [مشاهدة](https://www.youtube.com/watch?v=x_GyjV2Nb6k) |
| 054 | [Loop - Break Continue Pass](<06_loops/054_loop_break_continue_pass.py>) | [مشاهدة](https://www.youtube.com/watch?v=KtjJxOr5sp0) |
| 055 | [Loop Advanced Dictionary](<06_loops/055_loop_advanced_dictionary.py>) | [مشاهدة](https://www.youtube.com/watch?v=zTLmupb3cKg) |

### 7. الدوال — الدروس 056 إلى 064

المعاملات، والقيم الافتراضية، و args و kwargs، والنطاق، والاستدعاء الذاتي، و lambda.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 056 | [Function And Return](<07_functions/056_function_and_return.py>) | [مشاهدة](https://www.youtube.com/watch?v=Izwd_n-Ufqo) |
| 057 | [Function Parameters And Arguments](<07_functions/057_function_parameters_and_arguments.py>) | [مشاهدة](https://www.youtube.com/watch?v=CCMKMBGUxkc) |
| 058 | [Function Packing, Unpacking Arguments](<07_functions/058_function_packing_unpacking_arguments.py>) | [مشاهدة](https://www.youtube.com/watch?v=61i7VvPLVns) |
| 059 | [Function Default Parameters](<07_functions/059_function_default_parameters.py>) | [مشاهدة](https://www.youtube.com/watch?v=BNXasw_j4sY) |
| 060 | [Function Packing Unpacking Keyword Arguments](<07_functions/060_function_packing_unpacking_keyword_arguments.py>) | [مشاهدة](https://www.youtube.com/watch?v=pMeKs94OrxQ) |
| 061 | [Function Packing Unpacking Arguments Training's](<07_functions/061_function_packing_unpacking_arguments_trainings.py>) | [مشاهدة](https://www.youtube.com/watch?v=7o58LMti2po) |
| 062 | [Function Scope](<07_functions/062_function_scope.py>) | [مشاهدة](https://www.youtube.com/watch?v=VQHLn1wuDBw) |
| 063 | [Function Recursion](<07_functions/063_function_recursion.py>) | [مشاهدة](https://www.youtube.com/watch?v=zFVdMyr6CIo) |
| 064 | [Function Lambda](<07_functions/064_function_lambda.py>) | [مشاهدة](https://www.youtube.com/watch?v=oNp5wwu9S7c) |

### 8. التعامل مع الملفات — الدروس 065 إلى 068

فتح الملفات وقراءتها والكتابة فيها وحذفها.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 065 | [Files Handling Part One Intro](<08_files_handling/065_files_handling_part_1_intro.py>) | [مشاهدة](https://www.youtube.com/watch?v=6TFJs9uzEjI) |
| 066 | [Files Handling Part 2 Read Files](<08_files_handling/066_files_handling_part_2_read_files.py>) | [مشاهدة](https://www.youtube.com/watch?v=9ZU9FQQbOYE) |
| 067 | [Files Handling Part 3 Write and Append In Files](<08_files_handling/067_files_handling_part_3_write_and_append_in_files.py>) | [مشاهدة](https://www.youtube.com/watch?v=FBcElrNaiZQ) |
| 068 | [Files Handling Part 4 Important Info](<08_files_handling/068_files_handling_part_4_important_info.py>) | [مشاهدة](https://www.youtube.com/watch?v=wwe40Ngpp3A) |

### 9. الدوال الجاهزة — الدروس 069 إلى 075

all و any و sum و round و range و map و filter و reduce و enumerate وغيرها.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 069 | [Built In Functions Part One](<09_built_in_functions/069_built_in_functions_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=-PfCcZ2Q_MI) |
| 070 | [Built In Functions Part Two](<09_built_in_functions/070_built_in_functions_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=2ed3aomFliA) |
| 071 | [Built In Functions Part 3](<09_built_in_functions/071_built_in_functions_part_3.py>) | [مشاهدة](https://www.youtube.com/watch?v=XRw7mArOyok) |
| 072 | [Built In Functions Part 4 Map](<09_built_in_functions/072_built_in_functions_part_4_map.py>) | [مشاهدة](https://www.youtube.com/watch?v=JvbLI0z8t8c) |
| 073 | [Built In Functions Part 5 Filter](<09_built_in_functions/073_built_in_functions_part_5_filter.py>) | [مشاهدة](https://www.youtube.com/watch?v=0Zmdu7OgVl0) |
| 074 | [Built In Functions Part 6 Reduce](<09_built_in_functions/074_built_in_functions_part_6_reduce.py>) | [مشاهدة](https://www.youtube.com/watch?v=bgV0RHfRhB4) |
| 075 | [Built In Functions Part 7](<09_built_in_functions/075_built_in_functions_part_7.py>) | [مشاهدة](https://www.youtube.com/watch?v=nS-uled9biI) |

### 10. الوحدات — الدروس 076 إلى 078

استيراد الوحدات الجاهزة، وإنشاء وحدة خاصة، وتثبيت مكتبات خارجية.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 076 | [Modules Part 1 - Intro And Built In Modules](<10_modules/076_modules_part_1_intro_and_built_in_modules.py>) | [مشاهدة](https://www.youtube.com/watch?v=z7g9gCYYLiU) |
| 077 | [Modules Part 2 - Create Your Module](<10_modules/077_modules_part_2_create_your_module.py>) | [مشاهدة](https://www.youtube.com/watch?v=tyOULB29Hs8) |
| 078 | [Modules Part 3 - Install External Packages](<10_modules/078_modules_part_3_install_external_packages.py>) | [مشاهدة](https://www.youtube.com/watch?v=aA96q7oBdVk) |

### 11. التاريخ والوقت — الدروس 079 إلى 080

التعامل مع التاريخ والوقت وتنسيقهما.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 079 | [Date And Time Introduction](<11_date_and_time/079_date_and_time_introduction.py>) | [مشاهدة](https://www.youtube.com/watch?v=NH7Qd1_IGqM) |
| 080 | [Date And Time Format Date](<11_date_and_time/080_date_and_time_format_date.py>) | [مشاهدة](https://www.youtube.com/watch?v=Qa6p-eQ7k0U) |

### 12. المكررات والمولدات والمزخرفات — الدروس 081 إلى 086

الفرق بين المكرر والكائن القابل للتكرار، والمولدات، والمزخرفات، والدالة zip.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 081 | [Iterable Vs Iterator](<12_iterators_generators_decorators/081_iterable_vs_iterator.py>) | [مشاهدة](https://www.youtube.com/watch?v=MwBk42xwjjA) |
| 082 | [Generators](<12_iterators_generators_decorators/082_generators.py>) | [مشاهدة](https://www.youtube.com/watch?v=QNN3w7Na7HA) |
| 083 | [Decorators - Intro](<12_iterators_generators_decorators/083_decorators_intro.py>) | [مشاهدة](https://www.youtube.com/watch?v=BnBJVh1DBGw) |
| 084 | [Decorators - Function With Parameters](<12_iterators_generators_decorators/084_decorators_function_with_parameters.py>) | [مشاهدة](https://www.youtube.com/watch?v=ZVCPwfyAcBE) |
| 085 | [Decorators - Practical Speed Test](<12_iterators_generators_decorators/085_decorators_practical_speed_test.py>) | [مشاهدة](https://www.youtube.com/watch?v=WQk_j8KMExY) |
| 086 | [Practical Loop On Many Iterators With Zip](<12_iterators_generators_decorators/086_practical_loop_on_many_iterators_with_zip.py>) | [مشاهدة](https://www.youtube.com/watch?v=Z1gwFze9e94) |

### 13. الصور والتوثيق وجودة الكود — الدروس 087 إلى 089

التعديل على الصور بمكتبة Pillow، وكتابة التوثيق، وفحص الكود بأداة pylint.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 087 | [Practical Image Manipulation With Pillow](<13_pillow_docstrings_pylint/087_practical_image_manipulation_with_pillow.py>) | [مشاهدة](https://www.youtube.com/watch?v=mwmyhIzfkl4) |
| 088 | [Docstring And Commenting vs Documenting](<13_pillow_docstrings_pylint/088_doc_string_and_commenting_vs_documenting.py>) | [مشاهدة](https://www.youtube.com/watch?v=6skfWbMu9MY) |
| 089 | [Installing And Use Pylint For Better Code](<13_pillow_docstrings_pylint/089_installing_and_use_pylint_for_better_code.py>) | [مشاهدة](https://www.youtube.com/watch?v=YvqKqam_3zY) |

### 14. الأخطاء وتتبعها — الدروس 090 إلى 094

رفع الأخطاء والتعامل معها، وتتبع الكود، وتلميحات الأنواع.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 090 | [Errors And Exceptions Raising](<14_errors_and_debugging/090_errors_and_exceptions_raising.py>) | [مشاهدة](https://www.youtube.com/watch?v=5umR9zAidoc) |
| 091 | [Exceptions Handling Try, Except, Else, Finally](<14_errors_and_debugging/091_exceptions_handling_try_except_else_finally.py>) | [مشاهدة](https://www.youtube.com/watch?v=LBf_8txij3I) |
| 092 | [Exceptions Handling Advanced Example](<14_errors_and_debugging/092_exceptions_handling_advanced_example.py>) | [مشاهدة](https://www.youtube.com/watch?v=RjkKwZ-p7YU) |
| 093 | [Debugging Code](<14_errors_and_debugging/093_debugging_code.py>) | [مشاهدة](https://www.youtube.com/watch?v=U2ePyJsiVdw) |
| 094 | [Type Hinting](<14_errors_and_debugging/094_type_hinting.py>) | [مشاهدة](https://www.youtube.com/watch?v=J_e-r7NcwPU) |

### 15. التعابير النمطية — الدروس 095 إلى 102

البحث عن الأنماط في النصوص، مثل الإيميلات وأرقام الهواتف والروابط.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 095 | [Regular Expressions Part 1 Intro](<15_regular_expressions/095_regular_expressions_part_1_intro.py>) | [مشاهدة](https://www.youtube.com/watch?v=QrYB2S1IZKo) |
| 096 | [Regular Expressions Part 2 Quantifiers](<15_regular_expressions/096_regular_expressions_part_2_quantifiers.py>) | [مشاهدة](https://www.youtube.com/watch?v=3B8qYBBml68) |
| 097 | [Regular Expressions Part 3 Characters Classes Training's](<15_regular_expressions/097_regular_expressions_part_3_characters_classes_trainings.py>) | [مشاهدة](https://www.youtube.com/watch?v=MnIPbqYoOaI) |
| 098 | [Regular Expressions Part 4 Assertions & Email Pattern](<15_regular_expressions/098_regular_expressions_part_4_assertions_and_email_pattern.py>) | [مشاهدة](https://www.youtube.com/watch?v=bxssGTLjktA) |
| 099 | [Regular Expressions Part 5 Logical Or & Escaping](<15_regular_expressions/099_regular_expressions_part_5_logical_or_and_escaping.py>) | [مشاهدة](https://www.youtube.com/watch?v=CD8HsbCG-T8) |
| 100 | [Regular Expressions Part 6 Re Module Search & FindAll](<15_regular_expressions/100_regular_expressions_part_6_re_module_search_and_findall.py>) | [مشاهدة](https://www.youtube.com/watch?v=UKA-3O7XwPs) |
| 101 | [Regular Expressions Part 7 Re Module Split & Sub](<15_regular_expressions/101_regular_expressions_part_7_re_module_split_and_sub.py>) | [مشاهدة](https://www.youtube.com/watch?v=ZGizsqwe4ps) |
| 102 | [Regular Expressions Part 8 Group Training's & Flags](<15_regular_expressions/102_regular_expressions_part_8_group_trainings_and_flags.py>) | [مشاهدة](https://www.youtube.com/watch?v=MLb7pPOEJlg) |

### 16. البرمجة كائنية التوجه — الدروس 103 إلى 116

الكلاسات والكائنات، والوراثة، وتعدد الأشكال، والتغليف، والكلاسات المجردة.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 103 | [OOP Part 1 - Intro](<16_oop/103_oop_part_1_intro.py>) | [مشاهدة](https://www.youtube.com/watch?v=V7WP_402HE0) |
| 104 | [OOP Part 2 - Class Syntax And Info](<16_oop/104_oop_part_2_class_syntax_and_info.py>) | [مشاهدة](https://www.youtube.com/watch?v=Sphiyp42cp0) |
| 105 | [OOP Part 3 - Instance Attributes And Methods Part 1](<16_oop/105_oop_part_3_instance_attributes_and_methods_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=YNm5Go1NM9M) |
| 106 | [OOP Part 4 - Instance Attributes And Methods Part 2](<16_oop/106_oop_part_4_instance_attributes_and_methods_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=ImXpb95dXGc) |
| 107 | [OOP Part 5 - Class Attributes](<16_oop/107_oop_part_5_class_attributes.py>) | [مشاهدة](https://www.youtube.com/watch?v=48OyTbNlveE) |
| 108 | [OOP Part 6 - Class Methods And Static Methods](<16_oop/108_oop_part_6_class_methods_and_static_methods.py>) | [مشاهدة](https://www.youtube.com/watch?v=GQVGcJblo6U) |
| 109 | [OOP Part 7 - Magic Methods](<16_oop/109_oop_part_7_class_magic_methods.py>) | [مشاهدة](https://www.youtube.com/watch?v=dz78-WPduag) |
| 110 | [OOP Part 8 - Inheritance](<16_oop/110_oop_part_8_inheritance.py>) | [مشاهدة](https://www.youtube.com/watch?v=f3Dg6gxkL-0) |
| 111 | [OOP Part 9 - Multiple Inheritance And Method Overriding](<16_oop/111_oop_part_9_multiple_inheritance_and_methods_override.py>) | [مشاهدة](https://www.youtube.com/watch?v=OwfiogOFIF4) |
| 112 | [OOP Part 10 -  Polymorphism](<16_oop/112_oop_part_10_polymorphism.py>) | [مشاهدة](https://www.youtube.com/watch?v=eaGhE6EpmBI) |
| 113 | [OOP Part 11 -  Encapsulation](<16_oop/113_oop_part_11_encapsulation.py>) | [مشاهدة](https://www.youtube.com/watch?v=_zJ1nQto7Mw) |
| 114 | [OOP Part 12 Getters And Setters](<16_oop/114_oop_part_12_getters_and_setters.py>) | [مشاهدة](https://www.youtube.com/watch?v=vsOcbPE_Ih4) |
| 115 | [OOP Part 13 @Property Decorator](<16_oop/115_oop_part_13_property_decorator.py>) | [مشاهدة](https://www.youtube.com/watch?v=UgpyNxNiPRg) |
| 116 | [OOP Part 14 ABCs Abstract Base Class](<16_oop/116_oop_part_14_abc_abstract_base_class.py>) | [مشاهدة](https://www.youtube.com/watch?v=bRHRoB28sxk) |

### 17. قواعد البيانات SQLite — الدروس 117 إلى 127

إنشاء قاعدة بيانات، والإضافة والقراءة والتعديل والحذف، وبناء تطبيق مهارات كامل.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 117 | [Databases - Intro About Databases](<17_databases_sqlite/117_databases_intro_about_databases.py>) | [مشاهدة](https://www.youtube.com/watch?v=7F_4DYQG6LM) |
| 118 | [Databases - SQLite Create Database And Connect](<17_databases_sqlite/118_databases_sqlite_create_database_and_connect.py>) | [مشاهدة](https://www.youtube.com/watch?v=UokVrMqeu4o) |
| 119 | [Databases - SQLite Insert Data Into Database](<17_databases_sqlite/119_databases_sqlite_insert_data_into_database.py>) | [مشاهدة](https://www.youtube.com/watch?v=JCjGtiKCYO4) |
| 119b | [تمرين إضافي من عندي](<17_databases_sqlite/119b_databases_sqlite_insert_data_exercise.py>) | — |
| 120 | [Databases - SQLite Retrieve Data From Database](<17_databases_sqlite/120_databases_sqlite_retrieve_data_from_database.py>) | [مشاهدة](https://www.youtube.com/watch?v=vYkNQmwGTpQ) |
| 121 | [Databases - SQLite Training On Everything](<17_databases_sqlite/121_databases_sqlite_trainings_on_everything.py>) | [مشاهدة](https://www.youtube.com/watch?v=4dhxFHgsLyY) |
| 122 | [Databases - SQLite Update And Delete From Database](<17_databases_sqlite/122_databases_sqlite_update_and_delete_from_database.py>) | [مشاهدة](https://www.youtube.com/watch?v=8B9EZt-4980) |
| 123 | [Databases - SQLite Create Skills App Part 1](<17_databases_sqlite/123_databases_sqlite_create_skills_app_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=vcy5y04okBA) |
| 124 | [Databases - SQLite Create Skills App Part 2](<17_databases_sqlite/124_databases_sqlite_create_skills_app_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=hJjY4vzrduE) |
| 125 | [Databases - SQLite Create Skills App Part 3](<17_databases_sqlite/125_databases_sqlite_create_skills_app_part_3.py>) | [مشاهدة](https://www.youtube.com/watch?v=Bi5BMs9fc80) |
| 126 | [Databases - SQLite Create Skills App Part 4](<17_databases_sqlite/126_databases_sqlite_create_skills_app_part_4.py>) | [مشاهدة](https://www.youtube.com/watch?v=4yI-WVndsuY) |
| 127 | [Databases - SQLite Very Important Information](<17_databases_sqlite/127_databases_sqlite_very_important_information.py>) | [مشاهدة](https://www.youtube.com/watch?v=DgaGUpb7ttQ) |

### 18. دروس متقدمة — الدروس 128 إلى 132

المتغير __name__، وقياس سرعة الكود، والسجلات، واختبار الكود، وتوليد أرقام تسلسلية.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 128 | [Advanced Lessons - __name__ And "__main__"](<18_advanced_lessons/128_advanced_lessons_name_and_main.py>) | [مشاهدة](https://www.youtube.com/watch?v=lnMZZ4Ql-FU) |
| 129 | [Advanced Lessons - Timing Your Code With Timeit](<18_advanced_lessons/129_advanced_lessons_timing_your_code_with_timeit.py>) | [مشاهدة](https://www.youtube.com/watch?v=4tKWqrBiLjo) |
| 130 | [Advanced Lessons - Add Logging To Your Code](<18_advanced_lessons/130_advanced_lessons_add_logging_to_your_code.py>) | [مشاهدة](https://www.youtube.com/watch?v=VwDzQKfYs_k) |
| 131 | [Advanced Lessons - Unit Testing With Unittest](<18_advanced_lessons/131_advanced_lessons_unit_testing_with_unittest.py>) | [مشاهدة](https://www.youtube.com/watch?v=7qDuqwRYEhI) |
| 132 | [Advanced Lessons - Generate Random Serial Numbers](<18_advanced_lessons/132_advanced_lessons_generate_random_serial_numbers.py>) | [مشاهدة](https://www.youtube.com/watch?v=GW78NkdM7bU) |

### 19. إطار Flask — الدروس 133 إلى 140

بناء موقع صغير: الصفحات، والقوالب، والتنسيق، وجافاسكربت، وعرض بيانات من قاعدة البيانات.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 133 | [Flask - Intro And Your First Page](<19_flask/133_flask_intro_and_your_first_page.py>) | [مشاهدة](https://www.youtube.com/watch?v=Ze_lPWFQmXI) |
| 134 | [Flask - Create Html Files](<19_flask/134_flask_create_html_files.py>) | [مشاهدة](https://www.youtube.com/watch?v=07qgoQngK2Q) |
| 135 | [Flask - Create And Extends HTML Templates](<19_flask/135_flask_create_and_extends_html_templates.py>) | [مشاهدة](https://www.youtube.com/watch?v=LeQaQde-RZc) |
| 136 | [Flask - Jinja Template](<19_flask/136_flask_jinja_template.py>) | [مشاهدة](https://www.youtube.com/watch?v=VdANhdo9pTo) |
| 137 | [Flask - Advanced Css Task Using Jinja](<19_flask/137_flask_advanced_css_task_using_jinja.py>) | [مشاهدة](https://www.youtube.com/watch?v=CP8gG1gDbAw) |
| 138 | [Flask - Skills Page Using List Data](<19_flask/138_flask_skills_page_using_list_data.py>) | [مشاهدة](https://www.youtube.com/watch?v=7lFHUe-yQpI) |
| 139 | [Flask - Customizing App With Css](<19_flask/139_flask_customizing_app_with_css.py>) | [مشاهدة](https://www.youtube.com/watch?v=mciHTWGhh4w) |
| 139b | [تمرين إضافي من عندي](<19_flask/139b_flask_get_users_skills_from_database.py>) | — |
| 140 | [Flask - Adding The JS Files](<19_flask/140_flask_adding_the_js_files.py>) | [مشاهدة](https://www.youtube.com/watch?v=KdctidbJBtQ) |

### 20. التحكم بالمتصفح بمكتبة Selenium — الدرس 141

فتح المتصفح والتحكم به من بايثون.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 141 | [Web Scraping Control Browser With Selenium](<20_web_scraping_selenium/141_web_scraping_control_browser_with_selenium.py>) | [مشاهدة](https://www.youtube.com/watch?v=rovYCAv8_tU) |

### 21. مكتبة NumPy — الدروس 142 إلى 149

المصفوفات، ومقارنتها بالقوائم في السرعة والذاكرة، والعمليات عليها وتغيير شكلها.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 142 | [Numpy - Intro](<21_numpy/142_numpy_intro.py>) | [مشاهدة](https://www.youtube.com/watch?v=AFIaWjcUgW8) |
| 143 | [Numpy - Create Arrays](<21_numpy/143_numpy_create_arrays.py>) | [مشاهدة](https://www.youtube.com/watch?v=vGJxavinB9M) |
| 144 | [Numpy - Compare Data Location And Type](<21_numpy/144_numpy_compare_data_location_and_type.py>) | [مشاهدة](https://www.youtube.com/watch?v=5rkKhsdJ0UU) |
| 145 | [Numpy - Compare Performance And Memory Use](<21_numpy/145_numpy_compare_performance_and_memory_use.py>) | [مشاهدة](https://www.youtube.com/watch?v=koMDndoAvCc) |
| 146 | [Numpy - Array Slicing](<21_numpy/146_numpy_array_slicing.py>) | [مشاهدة](https://www.youtube.com/watch?v=EJ_TW1qiFI0) |
| 147 | [Numpy - Data Types And Control Array](<21_numpy/147_numpy_data_types_and_control_array.py>) | [مشاهدة](https://www.youtube.com/watch?v=630vRn-VzsM) |
| 148 | [Numpy - Arithmetic And Useful Operations](<21_numpy/148_numpy_arithmetic_and_useful_operations.py>) | [مشاهدة](https://www.youtube.com/watch?v=QbHFEo-YAPU) |
| 149 | [Numpy - Array Shape And ReShape](<21_numpy/149_numpy_array_shape_and_reshape.py>) | [مشاهدة](https://www.youtube.com/watch?v=6gmakP7c_UQ) |

### 22. البيئة الافتراضية والخاتمة — الدروس 150 إلى 152

إنشاء بيئة خاصة لكل مشروع، وملف المتطلبات، ومصادر للتعلم بعد الدورة.

| الدرس | الملف | الفيديو |
|:---:|---|:---:|
| 150 | [Virtual Environment Part 1](<22_virtual_environment_and_end/150_virtual_environment_part_1.py>) | [مشاهدة](https://www.youtube.com/watch?v=RSZEZ3WJn18) |
| 151 | [Virtual Environment Part 2](<22_virtual_environment_and_end/151_virtual_environment_part_2.py>) | [مشاهدة](https://www.youtube.com/watch?v=holkKfN7qhY) |
| 152 | [The End And Resources](<22_virtual_environment_and_end/152_the_end_and_resources.py>) | [مشاهدة](https://www.youtube.com/watch?v=OwV5R8Qy1e4) |

### الواجبات

مجلد [assignments](assignments) فيه حلولي لواجبات الدورة. كل ملف يغطي مجموعة دروس، واسمه يقول أي دروس، مثل `assignments_021_to_023.py`.

---

## عن هذا المستودع

كتبت هذه الملاحظات بيدي أثناء متابعة الدورة. بعد انتهائها راجعت كل الملفات مع مساعد ذكاء اصطناعي.
شغّلنا كل درس، وصححنا النواتج والشرح الخاطئ، ورتبنا الملفات في مجلدات، وأضفنا ملاحظات قصيرة حيث احتاج الشرح توضيحاً.

إذا وجدت خطأ، افتح مشكلة جديدة (Issue) في المستودع.
