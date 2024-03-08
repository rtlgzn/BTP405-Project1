from http.server import HTTPServer, BaseHTTPRequestHandler
import mysql.connector

# Establish connection to MySQL
connection = mysql.connector.connect(user='admin', password='password', host='localhost', database='HealthDB')
cursor = connection.cursor()

# Define the HEALTH table structure
create_table_query = """
CREATE TABLE IF NOT EXISTS HEALTH (
  HEALTH_ID INT AUTO_INCREMENT NOT NULL,
  STATUS VARCHAR(14) NOT NULL,
  DESCRIPTION VARCHAR(50) NOT NULL,
  PRIMARY KEY (HEALTH_ID)
)
"""

# Execute the query to create the table if it doesn't exist
cursor.execute(create_table_query)

class RequestHandler(BaseHTTPRequestHandler):
    def set_response_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self.set_response_headers()
        query = "SELECT HEALTH_ID, STATUS, DESCRIPTION FROM HEALTH"
        cursor.execute(query)
        for health_id, status, description in cursor:
            self.wfile.write(f"{health_id}, {status}, {description}".encode('utf-8'))

    def do_PUT(self):
        self.set_response_headers()
        insert_query = "INSERT INTO HEALTH (STATUS, DESCRIPTION) VALUES ('Good', 'Keep it up.')"
        cursor.execute(insert_query)
        connection.commit()

    def do_POST(self):
        self.set_response_headers()
        update_query = "UPDATE HEALTH SET DESCRIPTION = 'Maintain a healthy lifestyle' WHERE STATUS = 'Good'"
        cursor.execute(update_query)
        connection.commit()

def run_server(port=8010):
    server_address = ('', port)
    http_server = HTTPServer(server_address, RequestHandler)
    print(f"HTTP server running on port {port}...")
    try:
        http_server.serve_forever()
    except KeyboardInterrupt:
        pass
    finally:
        http_server.server_close()
        print("HTTP server stopped.")

if __name__ == '__main__':
    run_server()

# Properly close the cursor and connection
cursor.close()
connection.close()
