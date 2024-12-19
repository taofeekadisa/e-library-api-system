<h3>
Project Title: E-Library API System
</h3>

<h4>
Description:
</h4>

<p>
The goal of this project is to create a simple API for managing an online library system. This system allows users to borrow and return books, manage user information, and track the availability of books
</p>

<p>
The system includes the following entities:
</p>

<h5>
1. User: Represents a user of the library.
</h5>
<ul>
<li> id: Unique identifier for the user. </li>
<li> name: Name of the user. </li>
<li> email: Email address of the user. </li>
<li> is_active: Indicates if the user account is active (defaults to True). </li>
</ul>

<h5>
2. Book: Represents a book in the library.
</h5>

<ul>
<li> id: Unique identifier for the book. </li>
<li> title: Title of the book. </li>
<li> author: Author of the book.</li>
<li> is_available: Indicates if the book is available for borrowing (defaults to True). </li>
</ul>

<h5>
3. BorrowRecord: Represents a borrowing record.
</h5>

<ul>
<li> id: Unique identifier for the record. </li>
<li> user_id: ID of the user who borrowed the book. </li>
<li>book_id: ID of the borrowed book..</li>
<li> borrow_date: Date the book was borrowed. </li>
<li> return_date: Date the book was returned (if applicable). </li>
</ul>

<h4>
Requirements:
</h4>

<h4>
API Endpoints:
</h4>

<p>
You are required to create the following endpoints:
</p>

<h5>
1. User Endpoints:
</h5>
<ul>
<li> CRUD operations for User.</li>
<li> Endpoint to deactivate a user, setting is_active to False. </li>
</ul>

<h5>
2. Book Endpoints:
</h5>
<ul>
<li>CRUD operations for Book.</li>
<li> Endpoint to mark a book as unavailable (e.g., if it’s lost or under maintenance).</li>
</ul>

<h5>
3. Borrow Operations:
</h5>

<h6>
<li>Borrow a book:</li>
</h6>

<ul>
<li>Allows an active user to borrow an available book.</li>
<li> A user cannot borrow a book if it’s unavailable or if they have already borrowed the same book.</li>
<li> If the book is successfully borrowed, update its is_available status to False. </li>
<li> If the book cannot be borrowed, return an appropriate response and status code.</li>
</ul>

<h6>
<li>Return a book:</li>
</h6>

<ul>
<li> Marks a borrowed book as returned by updating the return_date in the BorrowRecord and setting the book’s is_available status to True. </li>

</ul>

<h5>
4. Borrow Record Management:
</h5>

<ul>
<li>Endpoint to view borrowing records for a specific user.</li>
<li> Endpoint to view all borrowing records.</li>
</ul>


<h4>
Additional Requirements:
</h4>

<h5>
1. Database:
</h5>
<ul>
<li> Use in-memory data structures (list or dict) for storage. </li>
</ul>

<h5>
2. Validation:
</h5>
<ul>
<li> Use Pydantic models to validate inputs for all endpoints. </li>
</ul>

<h5>
3. Code Structure:
</h5>
<ul>
<li> Follow a modular structure for better readability and maintainability. </li>
<li> Use separate files for models, routes, and application configuration. </li>
</ul>

<h5>
4. Status Codes:
</h5>
<ul>
<li> Use appropriate HTTP status codes for success and error scenarios. </li>
</ul>

<h4>
Constraints:
</h4>

<ol>
<li> Users must be active to perform any operations. </li>
<li> Books must be available to be borrowed. </li>
<li> Each borrowing operation should have a unique BorrowRecord. </li>
</ol>

<h4>
Submission Instructions:
</h4>

<ol>
<li> Develop the project using FastAPI. </li>
<li> Add a README.md file with instructions on how to run the application. </li>
<li> Push your code to a public GitHub repository. </li>
<li> Include test cases to validate your API endpoints (optional for extra credit). </li>
</ol>