"** What is 7 to the power of 4?**"
print(7**4)

"** Split this string:**\n",
"\n",
"    s = \"Hi there Sam!\"\n",
"    \n",
"**into a list. **"
s = 'Hi there Sam!'
l = s.split()
print(l)

"** Given the variables:**\n",
"\n",
"    planet = \"Earth\"\n",
"    diameter = 12742\n",
"\n",
"** Use .format() to print the following string: **\n",
"\n",
"    The diameter of Earth is 12742 kilometers."
planet = "Earth"
diameter = 12742
print('The diameter of {} is {} kilometers.'.format(planet, diameter))

"** Given this nested list, use indexing to grab the word \"hello\" **"
lst = [1,2,[3,4],[5,[100,200,['hello']],23,11],1,7]
print(lst[3][1][2][0])

"** Given this nested dictionary grab the word \"hello\". Be prepared, this will be annoying/tricky **"
d = {'k1':[1,2,3,{'tricky':['oh','man','inception',{'target':[1,2,3,'hello']}]}]}
print(d['k1'][3]['tricky'][3]['target'][3])

"** What is the main difference between a tuple and a list? **"
#tupla se define com () e lista com []. Além disso a tupla n é mutável

"** Create a function that grabs the email website domain from a string in the form: **\n",
"\n",
"    user@domain.com\n",
"    \n",
"**So for example, passing \"user@domain.com\" would return: domain.com**"
def func_email_domain(email):
    print(email.split('@')[1])
func_email_domain('user@domain.com')

"** Create a basic function that returns True if the word 'dog' is contained in the input string. Don't worry about edge cases like a punctuation being attached to the word dog, but do account for capitalization. **"
