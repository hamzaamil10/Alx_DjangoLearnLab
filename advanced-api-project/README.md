# Advanced API Project

## Book Endpoints

| Method | Endpoint              | Description             | Permissions        |
|--------|-----------------------|-------------------------|--------------------|
| GET    | /api/books/           | List all books          | Public             |
| GET    | /api/books/<id>/      | Get book by ID          | Public             |
| POST   | /api/books/create/    | Create a new book       | Authenticated only |
| PUT    | /api/books/<id>/update/ | Update an existing book | Authenticated only |
| DELETE | /api/books/<id>/delete/ | Delete a book           | Authenticated only |

### Notes
- Generic views used: `ListAPIView`, `RetrieveAPIView`, `CreateAPIView`, `UpdateAPIView`, `DestroyAPIView`.
- Custom behavior added to prevent duplicate titles.
- Search filter enabled for title and author.