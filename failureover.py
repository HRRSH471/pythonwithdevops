HOST='database-1.canwco2ws99r.us-east-1.rds.amazonaws.com'
USER="admin"
PASS="Admin123"
AZ={'us-east-1': 'ip-172-16-4-49'}
NOW=datetime.now().strftime("%H,%M,%S")
Print(now)
# AZ={}
print ("Phase-1 Config loaded")

# phase-2
try:
    cur=pymysql.connect(host=HOST,
                        user=USER,
                        password=PASS,
                        connect_timeout=10).cursor()
    cur.execute("SELECT @@hostname")
    print("Connected at region A:" ,AZ)
except Exception as e:
    print("Error :",e)