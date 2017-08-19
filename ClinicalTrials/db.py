import psycopg2
from config import config
 
def search(keywords,which_page,size_per_page):
    """ Connect to the PostgreSQL database server """
    conn = None
    try:
        params = config()
        print('Connecting to the PostgreSQL database...')
        conn = psycopg2.connect(**params)
        cur = conn.cursor()     
        query="""select row_to_json(studies) from studies
where overall_status = 'Recruiting'
offset {}
limit {}""".format((which_page-1)*size_per_page,size_per_page)
        cur.execute(query)
        rows = cur.fetchall()
        #print(rows)
        cur.close()

        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print ('Database connection closed.')
