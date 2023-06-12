# Homework: Lesson 2 [Volkov Anton]
# The English language has five vowels: A, E, I, O, and U
# Please count each vowel occurrence in the text below
# (sum of lowercase and capital cases)
# and write output as a table, something like this:
# -----------------
# | vowel | count |
# -----------------
# |   a   |  11   |
# |   e   |  23   |
#   ...
# -----------------

poem_text = """I wandered lonely as a cloud
That floats on high o'er vales and hills,
When all at once I saw a crowd,
A host, of golden daffodils;
Beside the lake, beneath the trees,
Fluttering and dancing in the breeze.

Continuous as the stars that shine
And twinkle on the Milky Way,
They stretched in never-ending line
Along the margin of a bay:
Ten thousand saw I at a glance,
Tossing their heads in sprightly dance."""

# 1. Count each vowel occurrence in the text
# (sum of lowercase and capital cases)
# and write output as a table
sep_num = 17
print('-' * sep_num)
print(f'|{"vowel":^7}|{"count":^7}|')
print('-' * sep_num)
print(
    f'|{"a":^7}|{poem_text.lower().count("a"):^7}|' +
    f'\n|{"e":^7}|{poem_text.lower().count("e"):^7}|' +
    f'\n|{"i":^7}|{poem_text.lower().count("i"):^7}|' +
    f'\n|{"o":^7}|{poem_text.lower().count("o"):^7}|' +
    f'\n|{"u":^7}|{poem_text.lower().count("u"):^7}|',
)
print('-' * sep_num)

# 2. Modify the text where each vowel is replaced with
# A->À;  a->à ; E-> É ; e->é; I->Í , i->í ; O->Ó ; o->ó; U->Ú; u->ú
# and print it
poem_text_replaced = (
    poem_text.replace('A', 'À')
    .replace('a', 'à')
    .replace('E', 'É')
    .replace('e', 'é')
    .replace('I', 'Í')
    .replace('i', 'í')
    .replace('O', 'Ó')
    .replace('o', 'ó')
    .replace('U', 'Ú')
    .replace('u', 'ú')
)
print(poem_text_replaced)
