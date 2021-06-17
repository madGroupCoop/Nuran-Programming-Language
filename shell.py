import Nuran

while True:
    text = input('Nuran > ')
    result, error = Nuran.run('<stdin>', text)

    if error:
        print(error.as_string())
    else:
        print(result)
