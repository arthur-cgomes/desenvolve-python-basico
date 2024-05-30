import csv

users = {}
books = []

def load_users(file_path='Trabalho Prático/csv/users.csv'):
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            users[row['username']] = {
                'password': row['password'],
                'role': row['role']
            }

def save_users(file_path='Trabalho Prático/csv/users.csv'):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['username', 'password', 'role']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for username, info in users.items():
            writer.writerow({'username': username, 'password': info['password'], 'role': info['role']})

def load_books(file_path='Trabalho Prático/csv/books.csv'):
    with open(file_path, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append({
                'title': row['title'],
                'author': row['author'],
                'price': float(row['price']),
                'quantity': int(row['quantity'])
            })

def save_books(file_path='Trabalho Prático/csv/books.csv'):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['title', 'author', 'price', 'quantity']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for book in books:
            writer.writerow(book)

def create_user(username, password, role):
    if username in users:
        print("Usuário já existe")
    else:
        users[username] = {'password': password, 'role': role}
        save_users()

def read_user(username):
    return users.get(username, "Usuário não encontrado")

def update_user(username, password=None, role=None):
    if username in users:
        if password:
            users[username]['password'] = password
        if role:
            users[username]['role'] = role
        save_users()
    else:
        print("Usuário não encontrado")

def delete_user(username):
    if username in users:
        del users[username]
        save_users()
    else:
        print("Usuário não encontrado")

def create_book(title, author, price, quantity):
    books.append({'title': title, 'author': author, 'price': price, 'quantity': quantity})
    save_books()

def read_book(title):
    for book in books:
        if book['title'] == title:
            return book
    return "Livro não encontrado"

def update_book(title, author=None, price=None, quantity=None):
    for book in books:
        if book['title'] == title:
            if author:
                book['author'] = author
            if price:
                book['price'] = price
            if quantity:
                book['quantity'] = quantity
            save_books()
            return
    print("Livro não encontrado")

def delete_book(title):
    for book in books:
        if book['title'] == title:
            books.remove(book)
            save_books()
            return
    print("Livro não encontrado")

def search_book(title):
    return read_book(title)

def list_books_sorted(by='title'):
    if by == 'title':
        sorted_books = sorted(books, key=lambda x: x['title'])
    elif by == 'price':
        sorted_books = sorted(books, key=lambda x: x['price'])
    else:
        print("Opção inválida")
        return
    
    for book in sorted_books:
        print(book)

def login(username, password):
    user = users.get(username)
    if user and user['password'] == password:
        return user['role']
    else:
        print("Nome de usuário ou senha inválidos")
        return None

def main():
    load_users()
    load_books()

    print("📚 Bem-vindo a biblioteca do PD!")
    username = input("Digite seu usuário: ")
    password = input("Digite sua senha: ")
    role = login(username, password)

    if role:
        while True:
            print("\nMenu:")
            if role == 'gerente':
                print("1. Adicionar usuário")
                print("2. Obter usuário")
                print("3. Atualizar usuário")
                print("4. Deletar usuário")
                print("5. Adicionar livro")
                print("6. Obter livro")
                print("7. Atualizar livro")
                print("8. Deletar livro")
                print("9. Buscar livro")
                print("10. Listar de livros ordenados por título")
                print("11. Listar livros ordenados por preço")
                print("12. Sair")
            elif role == 'funcionario':
                print("1. Obter livro")
                print("2. Atualizar livro")
                print("3. Buscar livro")
                print("4. Listar de livros ordenados por título")
                print("5. Listar livros ordenados por preço")
                print("6. Sair")
            elif role == 'cliente':
                print("1. Obter livro")
                print("2. Buscar livro")
                print("3. Listar de livros ordenados por título")
                print("4. Listar livros ordenados por preço")
                print("5. Sair")

            choice = input("Escolha uma opção: ")

            if role == 'gerente':
                if choice == '1':
                    username = input("Digite o nome do novo usuário: ")
                    password = input("Digite a senha do novo usuário: ")
                    role = input("Insira a permissão (gerente/funcionario/cliente): ")
                    create_user(username, password, role)
                elif choice == '2':
                    username = input("Digite o nome do usuário para obter: ")
                    print(read_user(username))
                elif choice == '3':
                    username = input("Digite o nome de usuário para atualizar: ")
                    password = input("Digite a nova senha (ou deixe em branco): ")
                    role = input("Insira a nova função (ou deixe em branco): ")
                    update_user(username, password or None, role or None)
                elif choice == '4':
                    username = input("Digite o nome de usuário para excluir: ")
                    delete_user(username)
                elif choice == '5':
                    title = input("Insira o título do livro: ")
                    author = input("Insira o autor do livro: ")
                    price = float(input("Insira o preço do livro: "))
                    quantity = int(input("Insira a quantidade do livro: "))
                    create_book(title, author, price, quantity)
                elif choice == '6':
                    title = input("Digite o título do livro para ler: ")
                    print(read_book(title))
                elif choice == '7':
                    title = input("Insira o título do livro para atualizar: ")
                    author = input("Insira o novo autor (ou deixe em branco): ")
                    price = input("Insira o novo preço (ou deixe em branco): ")
                    quantity = input("Insira a nova quantidade (ou deixe em branco): ")
                    update_book(title, author or None, float(price) if price else None, int(quantity) if quantity else None)
                elif choice == '8':
                    title = input("Digite o título do livro para excluir: ")
                    delete_book(title)
                elif choice == '9':
                    title = input("Digite o título do livro para pesquisar: ")
                    print(search_book(title))
                elif choice == '10':
                    list_books_sorted(by='title')
                elif choice == '11':
                    list_books_sorted(by='price')
                elif choice == '12':
                    break
            elif role == 'funcionario':
                if choice == '1':
                    title = input("Digite o título do livro para ler: ")
                    print(read_book(title))
                elif choice == '2':
                    title = input("Insira o título do livro para atualizar: ")
                    author = input("Insira o novo autor (ou deixe em branco): ")
                    price = input("Insira o novo preço (ou deixe em branco): ")
                    quantity = input("Insira a nova quantidade (ou deixe em branco): ")
                    update_book(title, author or None, float(price) if price else None, int(quantity) if quantity else None)
                elif choice == '3':
                    title = input("Digite o título do livro para pesquisar: ")
                    print(search_book(title))
                elif choice == '4':
                    list_books_sorted(by='title')
                elif choice == '5':
                    list_books_sorted(by='price')
                elif choice == '6':
                    break
            elif role == 'cliente':
                if choice == '1':
                    title = input("Digite o título do livro para ler: ")
                    print(read_book(title))
                elif choice == '2':
                    title = input("Digite o título do livro para pesquisar: ")
                    print(search_book(title))
                elif choice == '3':
                    list_books_sorted(by='title')
                elif choice == '4':
                    list_books_sorted(by='price')
                elif choice == '5':
                    break
            else:
                print("Opção inválida")

if __name__ == "__main__":
    main()
