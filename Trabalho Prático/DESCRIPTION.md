# Documento Descritivo

## Introdução
Sistema digital destinado ao gerenciamento de uma biblioteca online. O sistema tem três tipos de usuários: gerente, funcionario e cliente. Os produtos gerenciados pelo sistema são livros digitais com atributos como título, autor, preço e quantidade.

## Utilização para testes do PD
```bash
Usuário PD: pdDesenvolve
Senha PD: pdDesenvolve
```

## Implementação
### Usuários

- **Estrutura de dados**: dicionário.
- **Arquivo de registro**: `users.csv` com colunas `username`, `password` e `role`.
- **Funcionalidades**:
  - Create: `create_user()`
  - Read: `read_user()`
  - Update: `update_user()`
  - Delete: `delete_user()`

### Livros

- **Estrutura de dados**: lista de dicionários.
- **Arquivo de registro**: `books.csv` com colunas `title`, `author`, `price` e `quantity`.
- **Funcionalidades**:
  - Create: `create_book()`
  - Read: `read_book()`
  - Update: `update_book()`
  - Delete: `delete_book()`
  - Buscar: `search_book()`
  - Listar ordenado por nome: `list_books_sorted(by='title')`
  - Listar ordenado por preço: `list_books_sorted(by='price')`

