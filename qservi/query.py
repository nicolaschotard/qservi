import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='CHANGEME',
                             db='db',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

table = "deepCoadd_meas"
try:

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT d.id, d.modelfit_CModel_mag FROM %s AS d WHERE d.modelfit_CModel_mag < 24" % \
              table
        cursor.execute(sql, ('webmaster@python.org',))
        result = cursor.fetchone()
        print(result)
finally:
    connection.close()



    mysql --sock=/qserv/run/var/lib/mysql/mysql.sock --user=root --password=CHANGEME --batch qservTest_case06_mysql -e SELECT d.id, d.coord_ra_deg, d.coord_dec_deg, d.modelfit_CModel_mag FROM deepCoadd_meas d WHERE d.modelfit_CModel_mag < 24