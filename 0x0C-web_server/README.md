# Web Server Basics

## Main Role of a Web Server

A web server's primary role is to handle incoming requests from clients (such as web browsers) and respond by serving web pages or other requested content. It manages the communication between clients and the hosted applications or websites.

## Child Process

A child process is a process created by another process, known as the parent process. Child processes inherit certain attributes from the parent process but operate independently. In the context of web servers, child processes are often spawned to handle incoming requests, allowing for better concurrency and performance.

## Parent and Child Processes in Web Servers

Web servers commonly employ a parent-child process model. The parent process manages essential tasks like listening for incoming connections, while child processes handle individual requests. This approach enhances scalability and ensures that one misbehaving request doesn't affect the entire server.

## Main HTTP Requests

The main HTTP requests are:

- **GET**: Retrieves data from the server.
- **POST**: Sends data to the server to create a new resource.
- **PUT**: Updates a resource on the server.
- **DELETE**: Removes a resource from the server.
- **HEAD**: Similar to GET but retrieves only headers, not the actual data.
- **OPTIONS**: Describes the communication options for the target resource.
- **PATCH**: Applies partial modifications to a resource.

## DNS Basics

### What DNS Stands For

DNS stands for Domain Name System.

### DNS Main Role

The primary role of DNS is to translate human-readable domain names (like www.example.com) into IP addresses that machines can understand. It acts as a distributed directory system for the internet, mapping domain names to IP addresses.

## DNS Record Types

### A (Address) Record

A record that maps a domain to an IPv4 address.

### CNAME (Canonical Name) Record

A record that aliases one domain to another, allowing the use of multiple domain names for the same IP address.

### TXT (Text) Record

A record containing text information, often used for verification or providing additional details about a domain.

### MX (Mail Exchange) Record

A record specifying mail servers responsible for receiving email on behalf of a domain.

Feel free to reach out if you have any further questions!
