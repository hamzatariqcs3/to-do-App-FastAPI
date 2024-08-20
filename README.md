# FastAPI Project

## Version
0.1.0

## OpenAPI Specification
- OpenAPI 3.1
- [OpenAPI JSON](./openapi.json)

## Endpoints

### Items

- **Create Item**
  - **Endpoint**: `POST /api/items/`
  - **Description**: Create a new item.
  - **Request Body**: 
    ```json
    {
      "name": "string",
      "description": "string",
      "userId": "integer"
    }
    ```

- **Read Items**
  - **Endpoint**: `GET /api/items/`
  - **Description**: Retrieve a list of items.

- **Read Item**
  - **Endpoint**: `GET /api/items/{item_id}`
  - **Description**: Retrieve a specific item by its ID.
  - **Path Parameters**: 
    - `item_id` (integer): The ID of the item to retrieve.

- **Read Item By Name**
  - **Endpoint**: `GET /api/items/search/{item_title}`
  - **Description**: Retrieve an item by its title.
  - **Path Parameters**:
    - `item_title` (string): The title of the item to search for.

- **Delete Item**
  - **Endpoint**: `GET /api/items/delete/{item_id}`
  - **Description**: Delete a specific item by its ID.
  - **Path Parameters**:
    - `item_id` (integer): The ID of the item to delete.

- **Delete Item By Name**
  - **Endpoint**: `GET /api/items/deletewithname/{item_title}`
  - **Description**: Delete an item by its title.
  - **Path Parameters**:
    - `item_title` (string): The title of the item to delete.

### User

- **Create User**
  - **Endpoint**: `POST /api/user/add`
  - **Description**: Create a new user.
  - **Request Body**:
    ```json
    {
      "name": "string",
      "email": "string",
      "age": "integer",
      "address": "string",
      "phone_number": "string"
    }
    ```

## Getting Started

1. **Install Dependencies**
   ```bash
   poetry install
