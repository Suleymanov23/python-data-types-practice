# %%
a = 10
b = -5

# %%
### 1. a və b-nin cəmini tapın
cem = a + b
print(cem)

# %%
### 2. Nəticənin növü nədir? (a və b cəmin)
print(type(cem))

# %%
### 3. Onu (a və b cəmini) float-a çevir və nəticəni çap et.
f_cem = float(cem)
print(f_cem)

# %%
### 4. Məlumat növünü çap et.
print(type(f_cem))

# %%
a = 3.5
b = 2.0

# %%
### 5. a və b-ni vurun.
x = a * b
print(x)

# %%
### 6. Nəticənin məlumat növü nədir?
print(type(x))

# %%
### 7. Nəticəni int-ə çevir və nəticəni çap et.
int_x = int(x)
print(int_x)

# %% md
# Strings: str
# %%
text = "I love Data analysis"

# %%
# 1. Sətirin uzunluğunu təyin etmək üçün bir Python kodu yazın.
length = len(text)
print(length)

# %%
# 2. "I love Data analysis" mətnindən yalnız "love" sözünü seçin və ekrana capa verin.
print(text.split())

# %%
# 3. "I love Data analysis" mətnindəki "love" sözünü "like" sözü ilə dəyişdirin.
replaced_text = text.replace('love', 'like')
print(replaced_text)

# %%
name = "Elisa"
age = "30"

# %%
# 4. F-string metodu ilə bir cümlə yaradan və çap edən Python kodu yazın.
print(f'Onun adı {name}-dır və o, {age} yaşındadır.')

# %%
# 5. Cümlə daxilində "Elisa" alt sətirinin indeksini tapmaq üçün bir Python kodu yazın.
cumle = f'Onun adı {name}-dır və o, {age} yaşındadır.'
cavab = cumle.find('Elisa')
print(cavab)

# %%
number = 0.1234

# %%
# 6 Bu ədədi fərqli onluq (1f 2f və 3f ) ilə formatlamaq və çap etmək üçün F-string metodundan istifadə edən bir Python kodu yazın.
print(f'1f format: {number:.1f}')
print(f'2f format: {number:.2f}')
print(f'3f format: {number:.3f}')

# %% md
# Bool
# %%
# 1 Python-da iki məntiqi dəyişən yaradın: is_student və is_teacher.
is_student = True
is_teacher = False

# %% md
# Lists
# %%
fruit_selection = ["apple", "banana", "cherry", "date", "elderberry"]

# %%
# 1. Meyvələri əlifba sırasına görə sıralamaq üçün bir Python kodu yazın. Sıralanmış siyahını çap edin.
fruit_selection.sort()
print(fruit_selection)

# %%
# 2. fruit_selection siyahısının sonuna "orange" meyvəsini əlavə edən bir Python kodu yazın.
fruit_selection.append('orange')
print(fruit_selection)

# %%
# 3. fruit_selection siyahısının son elementini silin və onu çap edin.
removed = fruit_selection.pop()
print(removed)

# %%
numbers =

# %%
# 4. Rəqəmlərin siyahısını kiçikdən böyüyə sıralayın və çatışmayan rəqəmləri əlavə edin.
numbers.sort()
numbers.append(2)
print(numbers)

# %%
text = "I-love-Data-analysis"

# %%
# 5. Bu mətnin bir siyahıya çevrilməsi üçün Python kodu yazın. Siyahını "text_list" kimi saxlayın.
text_list = text.split(sep='-')
text_list_2 = list(text)

# %%
# 6 Bu siyahını çap edin və siyahını yenidən mətnə çevirin.
print(text_list)
again_text = '-'.join(text_list)
print(again_text)
again_text_2 = ''.join(text_list_2)

# %%
# 7. Elementlərin sayını hesablayın və nəticələri müqayisə edin.
print(len(text_list))
print(len(text))

if len(text) > len(text_list):
    print('textin elementi daha çoxdur')
else:
    print('text_list elementi daha çoxdur')

# %% md
# Dictionaries
# %%
product_dict = {
    "Laptop": ["Dell", 999.99],
    "Smartphone": ["Apple", 799.99],
    "Headphones": ["Sony", 129.95],
    "Tablet": ["Samsung", 349.99]
}

# %%
# 1. product_dict lüğətinin açarlarını (keys) və dəyərlərini (values) çap edin.
print(product_dict.keys())
print(product_dict.values())

# %%
# 2. "Smartphone" yazısını dəyişdirin.
product_dict['Smartphone'] = ["Samsung", 500]

# %%
# 3. "Smartphone" açarının dəyərini çap edin.
print(product_dict['Smartphone'])

# %% md
# Tuple
# %%
my_tuple = ("Auto", "Fahrrad", "Motorrad")

# %%
# 1. Python-da my_tuple tuplenin ilk və son elementini çap edin.
print(my_tuple)
print(my_tuple[-1])

# %%
# 2 Python-da my_tuple tuplenin ilk elementini silin.
list_version = list(my_tuple)
list_version.pop(0)
my_tuple = tuple(list_version)
print(my_tuple)

# %% md
# Set
# %%
# 1 "Auto", "Fahrrad" və "Motorrad" dəyərləri ilə bir Python seti yaradın.
my_set = {"Auto", "Fahrrad", "Motorrad"}

# %%
# 2 Artıq yaradılmış setə "Auto" elementini əlavə edin.
my_set.add('Auto')

# %%
# 3 my_set-dəki elementlərin sayını hesablayın və my_set-i çap edin.
print(len(my_set))
print(my_set)
