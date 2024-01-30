import sys, os

B_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

print(B_DIR)

a = os.path.join(B_DIR, 'apps')
print(a)
