# 8.3
def make_shirt(size, text):
    print(f"\nSize: {size.upper()}")
    print(f"Message: {text.title()}")

make_shirt('XL', 'ciao bello')
make_shirt(size='S', text='sto usando python')

# 8.4
def default_shirts(size='XL', text='I love Python'):
    print(f"\nSize: {size.upper()}")
    print(f"Message: {text.title()}")

default_shirts('S')