from app import app

def test_healthz():
    with app.test_client() as c:
        rv = c.get('/healthz')
        assert rv.status_code == 200
        # Check that the expected HTML text is in the response body
        assert b"Hi Iam CHOCHO" in rv.data
        assert b"www.youtube.com/@Chochothechowchow" in rv.data
