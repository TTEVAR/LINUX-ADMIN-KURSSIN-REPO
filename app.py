from flask import Flask, jsonify, render_template_string
import mysql.connector

app = Flask(__name__)

# Main page route
@app.route('/')
def home():
    html = """
    <html>
        <head>
            <title>Ya bois LEMPING page</title>
            <style>
                body {
                    background-color: #990099;  /* light grey background */
                    font-family: Papyrus;
                    display: flex;
                    flex-direction: column;
                    justify-content: center;
                    align-items: center;
                    height: 100vh;
                    margin: 0;
                }
		h1 {
			color: #2c3e50;
			font-size: 48px;
			margin-bottom: 30px;
			padding: 20px 40px;
			border: 3px solid #3498db;
			border-radius: 15px;
			box-shadow: 0 0 15px #3498db, 0 0 30px #3498db, 0 0 50px #3498db;
			text-align: center;
			background-color: #ecf0f1;
		}
                p {
                   	 font-size: 24px;
                   	 color: #66ff00;
			 margin-top: 20px;
			 padding: 15px 30px;
			 border: 2px solid #e74c3c;
			 border-radius: 12px;
			 box-shadow: 0 0 10px #e74c3c, 0 0 20px #e74c3c;
			 background-color: #FFFF00;
                }
		.button-link {
			display: inline-block;
			padding: 12px 24px;
			background-color: #4CAF50;
			color: white;
			text-decoration: none;
			border-radius: 8px;
			font-size: 18px
			font-weight: bold;
			transition: background-color 0.3s ease;
		}
		.button-link:hover {
			background-color: #45a049;
		}
                #sql-time {
                    font-weight: bold;
                    color: #e74c3c;  /* red-ish for visibility */
                }
            </style>
        </head>
        <body>
	    <h1>Welcome Reviewer to Ya bois LEMPING Server!</h1>
            <p>Current SQL server time: <span id="sql-time">Loading...</span></p>
            <p><a href="/data-analysis" class="button-link">Press to indulge in some DATA</a></p>
            <script>
                async function fetchTime() {
                    try {
                        const response = await fetch('/time');
                        const data = await response.json();
                        document.getElementById('sql-time').textContent = data.time;
                    } catch (error) {
                        document.getElementById('sql-time').textContent = "Error fetching time";
                        console.error(error);
                    }
                }
                fetchTime();  // fetch immediately
                setInterval(fetchTime, 5000);  // update every 5 seconds
            </script>
        </body>
    </html>
    """
    return html

# API endpoint to fetch current SQL time
@app.route('/time')
def get_time():
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="exampleuser",
            password="Yup#2025",  # <-- Replace with your actual DB password
            database="exampledb"
        )
        cursor = conn.cursor()
        cursor.execute("SELECT NOW();")
        result = cursor.fetchone()
        current_time = result[0]  # Extract datetime from tuple
        cursor.close()
        conn.close()
        return jsonify({'time': str(current_time)})
    except Exception as e:
        # Return error if DB query fails
        return jsonify({'time': f"Error: {str(e)}"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
