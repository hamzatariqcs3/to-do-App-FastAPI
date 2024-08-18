# to-do-App-FastAPI
 

This is a FastAPI project that provides a simple REST API for managing items. Below are the available endpoints and their descriptions.

## Endpoints

### 1. **POST /items/**
   - **Description**: Create a new item.
   - **Request Body**:
     - `name` (string): The name of the item.
     - `description` (string, optional): A description of the item.
   - **Response**: The created item.

### 2. **GET /items/**
   - **Description**: Retrieve a list of all items.
   - **Response**: A list of all items.

### 3. **GET /items/{item_id}**
   - **Description**: Retrieve a specific item by its ID.
   - **Path Parameters**:
     - `item_id` (int): The ID of the item to retrieve.
   - **Response**: The item with the specified ID.

### 4. **GET /items/search/{item_title}**
   - **Description**: Retrieve items that match a specific name or title.
   - **Path Parameters**:
     - `item_title` (string): The title or part of the title of the item to search for.
   - **Response**: A list of items that match the given title.

### 5. **GET /items/delete/{item_id}**
   - **Description**: Delete a specific item by its ID.
   - **Path Parameters**:
     - `item_id` (int): The ID of the item to delete.
   - **Response**: The deleted item (before deletion).

### 6. **GET /items/deletewithname/{item_title}**
   - **Description**: Delete items that match a specific name or title.
   - **Path Parameters**:
     - `item_title` (string): The title or part of the title of the item(s) to delete.
   - **Response**: A list of the deleted items (before deletion).

## Schemas

### Item Schema
- **id** (int): The unique identifier of the item.
- **name** (string): The name of the item.
- **description** (string, optional): A description of the item.
