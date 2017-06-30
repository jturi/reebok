from django.test import TestCase

# Create your tests here.
for i in range(1, 150):
    for j in range(1, 150):
        if i / j > 0.447:
            if i / j < 0.448:
                div = i / j
                fstring = f'{div:.4f}'
                print("Results: %d / %d = %s" %(i, j, fstring))

