from app import app

def test_healthz():
    with app.test_client() as c:
        rv = c.get('/healthz')
        assert rv.status_code == 200
        # Check for key content in the HTML response
        assert b"Yashwanth B" in rv.data
        assert b"DevSecOps Engineer" in rv.data
        assert b"yashwanthbhaskar0@gmail.com" in rv.data
        assert b"LinkedIn" in rv.data
        assert b"GitHub" in rv.data
        assert b"Professional Summary" in rv.data
        assert b"Education" in rv.data

