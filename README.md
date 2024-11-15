# TODO List App  

This project is a demonstration of implementing a **TODO list** application using **Clean Architecture** and the principles of **Domain-Driven Design (DDD)** with a **Hexagonal Architecture** approach.  

## Features  
- **Task Management**: Add, update, delete, and mark tasks as completed.  
- **Hexagonal Architecture**: Decouples core business logic from infrastructure and external dependencies.  
- **Clean DDD Principles**: Maintains clear separation between domains, application services, and infrastructure layers.  

## Project Structure  
The project follows the structure based on Clean Architecture:  
- **Domain**: Core business logic and rules, represented by entities, value objects, and domain services.  
- **Application**: Use cases and application logic, orchestrating the flow between the domain and external systems.  
- **Infrastructure**: Adapters and frameworks, including database integration, APIs, and UI components.  
- **Adapters**: Connect external systems to the application and domain layers.  

## Technologies Used  
- **Programming Language**: [Python 3.12] 
- **Framework**: [FastApi]  
- **Database**: [Database, e.g., PostgreSQL, MongoDB]  
- **Testing**: [PyTest]  

## How to Run  
1. Clone the repository:  
   ```bash  
   git clone https://github.com/Alymbekov/ddd-hexagon-architecture.git  
   cd ddd-hexagon-architecture/  
   ```  
2. Install dependencies:  
   ```bash  
   [poetry]  
   ```  
3. Run the application:  
   ```bash  
   [Run command, e.g., npm start, python app.py]  
   ```  

## Contribution  
Feel free to open issues and submit pull requests. Suggestions and improvements are always welcome!  

## License  
This project is licensed under the [MIT License](LICENSE).
