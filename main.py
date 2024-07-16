import fitz

doc = fitz.open('pdfs/testpdf.pdf')

for page in doc:
    text = page.get_text()
    print(text)

print("hello worldfdssdf")
print("git testing git testing help help 123")