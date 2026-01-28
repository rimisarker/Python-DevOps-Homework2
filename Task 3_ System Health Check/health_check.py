import json 

def process_server_data(json_string):
    try:
        
        data = json.loads(json_string)
        
    
        for server in data["servers"]:
            name = server["name"]
            status = server["status"]
            print(f"Server: {name} | Status: {status}")
            
    except json.JSONDecodeError:
        
        print("Error: Invalid JSON format found!")


mock_api = '{"servers": [{"name": "web-01", "status": "up"}, {"name": "db-01", "status": "down"}]}'


process_server_data(mock_api)