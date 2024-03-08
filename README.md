# BTP405 - Project 1
Student Name: Renata Toleugazina

## Tools and Technologies
- Programming Language: Python
- Database: MySQL
- Version Management: Git
- Container Technology: Docker
- Testing the API: curl / Invoke-RestMethod (Windows)

## Setting up MySQL with Docker

```
docker pull container-registry.oracle.com/mysql/community-server:latest
```
```
docker run --name=mysql1 -p 3306:3306 -e MYSQL_ROOT_PASSWORD=password --restart on-failure -d container-registry.oracle.com/mysql/community-server:latest
```

GET Request:
```
def do_GET(self):
    self._set_response()
    cursor.execute("SELECT health_id, status, description FROM HEALTH")
    for (note_id, title, content) in cursor:
        self.wfile.write("{}, {}, {}".format(health_id, status, description).encode('utf-8'))
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8010 
```
Test command (curl):
```
curl 127.0.0.1:8010 
```

PUT Request:
```
def do_PUT(self):
    self._set_response()
    cursor.execute("INSERT INTO HEALTH (STATUS, DESCRIPTION) values ('Good', 'Keep it up.')")
    cnx.commit()
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8010 -Method PUT 
```
Test command (curl):
```
curl -X PUT 127.0.0.1:8010 
```

POST Request:
```
def do_POST(self):
    self._set_response()
    cursor.execute("UPDATE HEALTH SET DESCRIPTION = 'Maintain a healthy lifestyle' WHERE STATUS = 'Good'")
    cnx.commit()
```
Test command (Windows PowerShell):
```
Invoke-RestMethod -Uri localhost:8010 -Method POST 
```
Test command (curl):
```
curl -X POST 127.0.0.1:8010 
```

Build a docker image:
```
docker build -t vietpham/healthcare:v1 .
``` 
Run a docker container:
```
docker run -p 8010:8010 vietpham/healthcare:v1
```
