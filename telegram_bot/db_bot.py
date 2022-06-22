import psycopg2

conn = psycopg2.connect(host="localhost", port = 5432, database="houseshop", user="aigerimbegimbaeva", password="1")
cur = conn.cursor()

class BD1:

    def product():
        cur.execute("""SELECT id, title, price, create_date FROM product_product""")
        query_results = cur.fetchall()
        text = '\n\n'.join([', '.join(map(str, x)) for x in query_results])
        return (str(text))