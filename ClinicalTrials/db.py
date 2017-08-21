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
        query="""
SELECT row_to_json(t)
FROM(
SELECT t_search.nct_id,t_search.start_date,t_search.brief_title,t_search.overall_status,t_search.phase
FROM (SELECT s.nct_id as nct_id,
      	s.start_date as start_date,
      	s.brief_title as brief_title,
        s.overall_status as overall_status,
        s.phase as phase,
 		to_tsvector(s.brief_title) ||
        to_tsvector(s.official_title) ||
        to_tsvector(k.name) as 
document
FROM studies s
INNER JOIN keywords k ON s.nct_id=k.nct_id) t_search
WHERE t_search.document @@ to_tsquery(\'{}\')
OFFSET {}
LIMIT {}) t""".format(keywords,(which_page-1)*size_per_page,size_per_page)
        cur.execute(query)
        rows = cur.fetchall()
        print(query)
        cur.close()

        return rows
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print ('Database connection closed.')
